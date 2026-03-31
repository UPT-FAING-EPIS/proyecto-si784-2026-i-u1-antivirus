"""
presentation/report_formatter.py
==================================
Formateador de reportes y resultados para la interfaz CLI.

Este archivo convierte los DTOs y entidades del dominio en texto
formateado y colorido para mostrar al usuario en la terminal.

Centralizar el formateo aquí permite cambiar toda la presentación
visual sin tocar la lógica de negocio o los casos de uso.

Usa la librería 'rich' para tablas, colores, barras de progreso y paneles.

Depende de:
    - application/dtos.py  → recibe los DTOs para formatear
    - Librería externa: rich (Table, Console, Panel, Progress)

Clases que debe contener:
--------------------------

ReportFormatter:
    Generador de reportes visuales en terminal.

    Constructor:
        Instancia el Console de rich que se usará para todas las impresiones.
        Define un mapa de colores por nivel de amenaza:
            CRITICAL → rojo brillante, HIGH → rojo, MEDIUM → amarillo, LOW → cyan.

    Método: format_scan_report(result: ScanResponseDTO) -> None
        Muestra el reporte completo de un escaneo.
        Incluye:
            - Panel con estadísticas generales (archivos escaneados, amenazas, duración).
            - Si hay amenazas, tabla con columnas: Archivo | Nivel | Categoría.
            - Mensaje de "Sistema limpio" si no hay amenazas (en verde).

    Método: format_threat_table(threats: list[dict]) -> None
        Muestra una tabla formateada de amenazas detectadas.
        Cada fila muestra: ruta del archivo, nivel de amenaza (coloreado),
        nombre de la firma detectada y categoría del malware.

    Método: format_quarantine_list(files: list[dict]) -> None
        Muestra la lista de archivos actualmente en cuarentena.
        Tabla con columnas: Nombre original | Fecha de cuarentena | Nivel de amenaza.
        Si la lista está vacía, muestra un mensaje informativo.

    Método: format_cleanup_report(report: CleanupReportDTO) -> None
        Muestra el resultado de la limpieza del sistema.
        Incluye: archivos eliminados, espacio liberado en MB,
        y lista de errores si los hubo.

    Método: show_progress_bar(total: int, description: str) -> Progress
        Crea y retorna una barra de progreso de rich para operaciones largas.
        Usada principalmente durante el escaneo de directorios grandes.

    Método: show_alert(message: str, level: str) -> None
        Muestra un panel de alerta visual con bordes de color según el nivel.
        Usado para alertas de protección en tiempo real.
"""
