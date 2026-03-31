"""
presentation/menu_handler.py
==============================
Manejador del menú principal de la interfaz CLI.

Este archivo gestiona la lógica de navegación entre las opciones
del menú principal del antivirus. Traduce la selección del usuario
en la acción correspondiente de cada caso de uso.

Separa la responsabilidad del menú de la responsabilidad de la interfaz
principal, siguiendo el principio de Single Responsibility.

Depende de:
    - presentation/cli_interface.py → recibe referencia para mostrar resultados
    - application/dtos.py           → construye los DTOs de solicitud
    - Todos los casos de uso        → recibe referencias por inyección

Clases que debe contener:
--------------------------

MenuHandler:
    Gestor de la navegación y selección del menú de usuario.

    Constructor:
        Recibe referencias a todos los casos de uso (scan, protection,
        quarantine, cleanup) y a la CLIInterface para mostrar resultados.

    Método: show_main_menu() -> None
        Muestra en pantalla el menú principal con las 4 opciones:
            [1] System Scan     - Escanear el sistema
            [2] Real-Time Protection - Activar/Desactivar protección
            [3] Quarantine Manager  - Ver y gestionar cuarentena
            [4] PC Cleanup      - Limpiar el sistema
            [0] Exit            - Salir del programa
        Usa la librería rich para formatear la tabla del menú.

    Método: handle_selection(option: int) -> None
        Enruta la selección del usuario al método correspondiente.
        Usa un diccionario de mapeo {opción: método} en lugar de
        múltiples if/elif (más limpio y extensible).

    Método: handle_scan() -> None
        Solicita al usuario la ruta a escanear.
        Construye el ScanRequestDTO con la ruta ingresada.
        Llama al ScanUseCase y pasa el resultado a la CLIInterface.

    Método: handle_protection() -> None
        Verifica el estado actual de la protección en tiempo real.
        Si está activa, la detiene. Si está inactiva, la inicia.
        Solicita al usuario el directorio a monitorear si va a activarla.
        Muestra el nuevo estado al terminar.

    Método: handle_quarantine() -> None
        Muestra el menú de cuarentena con sub-opciones:
            [1] Ver archivos en cuarentena
            [2] Restaurar un archivo
            [3] Volver al menú principal
        Llama al QuarantineUseCase según la sub-opción elegida.

    Método: handle_cleanup() -> None
        Muestra una vista previa de los archivos que serán eliminados.
        Solicita confirmación al usuario antes de ejecutar la limpieza.
        Llama al CleanupUseCase y muestra el reporte resultante.
"""
