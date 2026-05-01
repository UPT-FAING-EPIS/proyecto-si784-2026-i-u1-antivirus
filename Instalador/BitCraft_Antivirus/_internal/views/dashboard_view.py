import customtkinter as ctk
import threading

class DashboardView(ctk.CTkFrame):
    def __init__(self, parent, bridge):
        super().__init__(parent)
        self.bridge = bridge
        self.bridge.register_callback(self.on_event)

        # Título
        self.label_title = ctk.CTkLabel(self, text="SecureGuard Dashboard",
                                        font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.pack(pady=30)

        # Indicador de estado
        self.status_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.status_frame.pack(pady=20)
        self.status_circle = ctk.CTkLabel(self.status_frame, text="●",
                                          text_color="#2ECC71", font=("Arial", 48))
        self.status_circle.pack(side="left", padx=10)
        self.status_text = ctk.CTkLabel(self.status_frame, text="Sistema Protegido",
                                        font=ctk.CTkFont(size=16))
        self.status_text.pack(side="left")

        # Botón de Escaneo
        self.scan_btn = ctk.CTkButton(self, text="🔍 Escanear Equipo (Rápido)",
                                      command=self.start_scan, width=250, height=45)
        self.scan_btn.pack(pady=30)

        # Barra de progreso
        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.set(0)

        # Estadísticas
        self.stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.stats_frame.pack(pady=30)
        
        ctk.CTkLabel(self.stats_frame, text="SecureGuard v0.3.0",
                     font=ctk.CTkFont(size=12)).pack()
        ctk.CTkLabel(self.stats_frame, text="Motor: Activo",
                     font=ctk.CTkFont(size=12)).pack()

    def start_scan(self):
        self.scan_btn.configure(state="disabled", text="Escaneando...")
        self.progress.pack(pady=10)
        self.progress.start()
        threading.Thread(target=self.run_scan, daemon=True).start()

    def run_scan(self):
        self.bridge.send_command({
            "action": "scan",
            "path": "C:\\Users\\Public"
        })
        self.after(0, self.scan_finished)

    def scan_finished(self):
        self.progress.stop()
        self.progress.pack_forget()
        self.scan_btn.configure(state="normal", text="🔍 Escanear Equipo (Rápido)")
        self.status_circle.configure(text="●", text_color="#2ECC71")
        self.status_text.configure(text="Escaneo completado - Sistema Protegido")

    def on_event(self, event):
        if event.get("event") == "threat_detected":
            self.after(0, self.show_threat, event)

    def show_threat(self, event):
        self.status_circle.configure(text="●", text_color="#E74C3C")
        self.status_text.configure(text=f"⚠️ ¡Amenaza detectada! {event.get('file', 'Archivo desconocido')}")