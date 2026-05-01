# frontend_python/engine_bridge.py
import subprocess
import json
import threading
import queue
import time
import os
import sys
from utils import get_engine_path, get_signatures_path


class EngineBridge:
    """
    Puente de comunicación entre la GUI de Python (frontend) 
    y el motor del antivirus escrito en Rust (backend).
    """
    
    def __init__(self, engine_path=None):
        if engine_path is None:
            engine_path = get_engine_path()
        
        self.engine_path = engine_path
        self.process = None
        self.queue = queue.Queue()
        self.running = False
        self.callbacks = []
        self.lock = threading.Lock()

    def start_daemon(self, signatures_path=None):
        """
        Inicia el motor del antivirus como un proceso hijo.
        """
        if self.running:
            return
        
        if signatures_path is None:
            signatures_path = get_signatures_path()
        
        try:
            # Verificar que el ejecutable existe
            if not os.path.exists(self.engine_path):
                raise FileNotFoundError(f"SecureGuard Engine no encontrado en: {self.engine_path}")
            
            self.process = subprocess.Popen(
                [self.engine_path, "daemon", signatures_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            )
            self.running = True
            
            # Hilos para leer la salida y monitorear el proceso
            threading.Thread(target=self._read_output, daemon=True).start()
            threading.Thread(target=self._monitor_process, daemon=True).start()
            
        except FileNotFoundError as e:
            raise RuntimeError(str(e))
        except Exception as e:
            raise RuntimeError(f"No se pudo iniciar SecureGuard Engine: {e}")

    def stop_daemon(self):
        """
        Detiene el motor del antivirus de manera ordenada.
        """
        if self.process and self.running:
            try:
                # Intentar apagado ordenado
                self.send_command({"action": "shutdown"}, wait_for_response=False)
                time.sleep(0.5)
                self.process.terminate()
                self.process.wait(timeout=3)
            except:
                try:
                    self.process.kill()
                except:
                    pass
            finally:
                self.running = False
                print("[EngineBridge] Motor detenido")

    def send_command(self, command: dict, wait_for_response=True, timeout=30):
        """
        Envía un comando JSON al motor y opcionalmente espera respuesta.
        """
        with self.lock:
            if not self.running or self.process is None:
                return {"status": "error", "message": "SecureGuard Engine no está corriendo"}
            
            try:
                cmd_json = json.dumps(command) + "\n"
                self.process.stdin.write(cmd_json)
                self.process.stdin.flush()
            except Exception as e:
                self.running = False
                return {"status": "error", "message": f"Error enviando comando: {e}"}
        
        if wait_for_response:
            try:
                response = self.queue.get(timeout=timeout)
                return json.loads(response)
            except queue.Empty:
                return {"status": "error", "message": "Timeout esperando respuesta del motor"}
            except json.JSONDecodeError:
                return {"status": "error", "message": "Respuesta inválida del motor"}
        else:
            return {"status": "ok", "message": "Comando enviado"}

    def register_callback(self, callback):
        """
        Registra una función callback para eventos del motor.
        """
        if callback not in self.callbacks:
            self.callbacks.append(callback)

    def unregister_callback(self, callback):
        """
        Elimina un callback registrado.
        """
        if callback in self.callbacks:
            self.callbacks.remove(callback)

    def is_running(self):
        """
        Verifica si el motor está corriendo.
        """
        return self.running and self.process is not None and self.process.poll() is None

    def restart_daemon(self, signatures_path=None):
        """
        Reinicia el motor del antivirus.
        """
        self.stop_daemon()
        time.sleep(1)
        self.start_daemon(signatures_path)

    # --- Métodos de conveniencia para comandos comunes ---

    def scan_file(self, file_path):
        """Escanea un archivo específico"""
        return self.send_command({
            "action": "scan_file",
            "file_path": file_path
        })

    def scan_directory(self, directory_path):
        """Escanea un directorio completo"""
        return self.send_command({
            "action": "scan_directory",
            "directory": directory_path
        })

    def get_status(self):
        """Obtiene el estado actual del motor"""
        return self.send_command({
            "action": "get_status"
        })

    def enable_protection(self):
        """Activa la protección en tiempo real"""
        return self.send_command({
            "action": "enable_protection"
        })

    def disable_protection(self):
        """Desactiva la protección en tiempo real"""
        return self.send_command({
            "action": "disable_protection"
        })

    def get_quarantine_list(self):
        """Obtiene la lista de archivos en cuarentena"""
        return self.send_command({
            "action": "get_quarantine"
        })

    def restore_from_quarantine(self, file_hash):
        """Restaura un archivo de la cuarentena"""
        return self.send_command({
            "action": "restore_quarantine",
            "file_hash": file_hash
        })

    def run_cleaner(self):
        """Ejecuta la limpieza del sistema"""
        return self.send_command({
            "action": "run_cleaner"
        })

    def check_updates(self):
        """Verifica si hay actualizaciones disponibles"""
        return self.send_command({
            "action": "check_updates"
        })

    def update_signatures(self):
        """Actualiza las firmas de malware"""
        return self.send_command({
            "action": "update_signatures"
        })

    def get_system_info(self):
        """Obtiene información del sistema desde el motor"""
        return self.send_command({
            "action": "get_system_info"
        })

    # --- Métodos internos ---

    def _read_output(self):
        """
        Lee continuamente la salida stdout del motor.
        Separa eventos (broadcast) de respuestas a comandos.
        """
        while self.running and self.process and self.process.stdout:
            try:
                line = self.process.stdout.readline()
                if not line:
                    break
                
                line = line.strip()
                if line:
                    try:
                        data = json.loads(line)
                        if "event" in data:
                            # Es un evento broadcast, notificar a callbacks
                            for cb in self.callbacks:
                                try:
                                    cb(data)
                                except Exception as e:
                                    print(f"[EngineBridge] Error en callback: {e}")
                        else:
                            # Es una respuesta a un comando
                            self.queue.put(line)
                    except json.JSONDecodeError:
                        # Ignorar líneas que no son JSON
                        pass
            except Exception as e:
                print(f"[EngineBridge] Error leyendo salida: {e}")
                break
        
        self.running = False

    def _monitor_process(self):
        """
        Monitorea si el proceso del motor sigue vivo.
        """
        while self.running:
            if self.process and self.process.poll() is not None:
                exit_code = self.process.poll()
                print(f"[EngineBridge] El motor se ha detenido (código: {exit_code})")
                self.running = False
                break
            time.sleep(1)