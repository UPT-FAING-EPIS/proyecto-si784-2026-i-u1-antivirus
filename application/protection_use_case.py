"""
application/protection_use_case.py
====================================
Caso de uso: Protección en tiempo real (Real-Time Protection).

Este archivo orquesta la lógica de negocio para monitorear el sistema
de archivos en tiempo real y reaccionar ante nuevos archivos detectados.

Cuando el usuario descarga o crea un archivo, este caso de uso verifica
automáticamente si coincide con alguna firma sospechosa.

Dependencias que recibe por inyección (constructor):
    - monitor: IFileMonitor → observador del sistema de archivos
    - scanner: IFileScanner → motor de escaneo para verificar nuevos archivos
    - repository: ISignatureRepository → consulta de firmas
    - quarantine_use_case: QuarantineUseCase → para aislar amenazas encontradas

Clases que debe contener:
--------------------------

RealTimeProtectionUseCase:
    Orquestador de la protección en tiempo real.

    Método: start(directory: str) -> None
        Inicia el monitoreo de un directorio.
        Registra el callback interno _on_new_file en el IFileMonitor.
        El monitor corre en un hilo separado (gestionado por infraestructura).

    Método: stop() -> None
        Detiene el monitoreo de forma segura.
        Llama a IFileMonitor.stop_monitoring().

    Método: is_active() -> bool
        Retorna True si el monitoreo está activo en este momento.

    Método: _on_new_file(file_path: str) -> None  [privado, callback interno]
        Se ejecuta cada vez que el monitor detecta un nuevo archivo.
        Flujo interno:
            1. Recibe la ruta del nuevo archivo.
            2. Espera brevemente si el archivo aún está siendo escrito (pausa pequeña).
            3. Solicita al IFileScanner que lo analice.
            4. Si se detecta una amenaza, llama al QuarantineUseCase automáticamente.
            5. Notifica al sistema de presentación (via callback registrable externamente).

    Método: set_alert_callback(callback: callable) -> None
        Permite a la capa de presentación registrar una función
        que será llamada con el ThreatFile cuando se detecte una amenaza.
        Esto desacopla la presentación del caso de uso.
"""
