"""
presentation/cli_interface.py
==============================
Interfaz principal de línea de comandos (CLI) del antivirus.

Este archivo es el punto de entrada de la interfaz de usuario.
Recibe las acciones del usuario, las traduce en llamadas a los casos de uso,
y muestra los resultados formateados en pantalla.

REGLA: Esta capa NO debe contener lógica de negocio. Solo presentación.
Si hay una decisión de negocio, pertenece a application/ o domain/.

Depende de:
    - application/scan_use_case.py       → ejecuta escaneos
    - application/protection_use_case.py → activa/desactiva protección
    - application/quarantine_use_case.py → gestiona cuarentena
    - application/cleanup_use_case.py    → ejecuta limpieza
    - application/dtos.py                → construye los DTOs de entrada
    - presentation/menu_handler.py       → delega el menú principal
    - presentation/report_formatter.py  → formatea los resultados

Clases que debe contener:
--------------------------

CLIInterface:
    Controlador principal de la interfaz de usuario en terminal.

    Constructor:
        Recibe el DependencyContainer para obtener los casos de uso.
        Obtiene las instancias de los 4 casos de uso desde el contenedor.
        Instancia el MenuHandler y el ReportFormatter.

    Método: run() -> None
        Punto de entrada principal de la interfaz.
        Muestra el banner de bienvenida del antivirus.
        Inicia el bucle principal del menú (loop hasta que el usuario salga).
        Al salir, cierra la conexión a la base de datos y detiene el monitor.

    Método: display_scan_result(result: ScanResponseDTO) -> None
        Recibe el resultado del escaneo y lo pasa al ReportFormatter.
        Si hay amenazas, pregunta al usuario si desea cuarentenar cada una.

    Método: display_threat_alert(threat_file) -> None
        Muestra una alerta visual urgente cuando la protección en tiempo real
        detecta un archivo sospechoso recién creado o descargado.
        Usa colores llamativos (rojo) con la librería rich.

    Método: prompt_quarantine_confirmation(file_path: str) -> bool
        Muestra al usuario el path del archivo amenazante y pregunta
        si desea enviarlo a cuarentena. Retorna True si confirma.

    Método: show_banner() -> None
        Muestra el banner ASCII de bienvenida del antivirus con nombre,
        versión y descripción breve del sistema. Usa la librería rich.

    Método: show_protection_status(is_active: bool) -> None
        Muestra en pantalla si la protección en tiempo real está
        activa (verde) o inactiva (rojo).
"""
