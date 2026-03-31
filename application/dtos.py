"""
application/dtos.py
====================
Data Transfer Objects (DTOs) para la capa de aplicación.

Los DTOs son objetos simples usados para transportar datos entre capas
sin exponer las entidades del dominio directamente a la presentación.

Esto evita el acoplamiento entre la presentación y el dominio, y permite
que cada capa evolucione independientemente.

Clases que debe contener:
--------------------------

ScanRequestDTO:
    Datos de entrada para iniciar un escaneo.
    Atributos:
        - target_path (str): Ruta del archivo o directorio a escanear.
        - scan_type (str): Tipo de escaneo ('quick', 'full', 'custom').
        - include_extensions (list[str]): Extensiones a incluir (vacío = todas).

ScanResponseDTO:
    Datos de salida después de completar un escaneo.
    Atributos:
        - total_files_scanned (int): Cantidad total de archivos revisados.
        - threats_found (int): Número de amenazas detectadas.
        - threat_list (list[dict]): Lista simplificada de amenazas (path, nivel).
        - duration_seconds (float): Tiempo total del escaneo en segundos.
        - status (str): 'clean' si no hay amenazas, 'infected' si las hay.

QuarantineRequestDTO:
    Datos de entrada para solicitar cuarentena de un archivo.
    Atributos:
        - file_path (str): Ruta completa del archivo a aislar.
        - reason (str): Razón de la cuarentena (nombre de la firma detectada).

QuarantineResponseDTO:
    Datos de salida tras intentar una cuarentena.
    Atributos:
        - success (bool): True si el archivo fue movido exitosamente.
        - quarantine_path (str): Nueva ubicación del archivo en cuarentena.
        - error_message (str | None): Mensaje de error si success es False.

CleanupRequestDTO:
    Datos de entrada para iniciar una limpieza del sistema.
    Atributos:
        - include_temp (bool): Si debe limpiar carpetas temporales del SO.
        - include_quarantine (bool): Si debe eliminar los archivos en cuarentena.
        - custom_paths (list[str]): Rutas adicionales a limpiar.

CleanupReportDTO:
    Datos de salida tras completar una limpieza.
    Atributos:
        - files_deleted (int): Cantidad de archivos eliminados.
        - space_freed_mb (float): Espacio liberado en megabytes.
        - errors (list[str]): Archivos que no pudieron eliminarse y su razón.
        - success (bool): True si la limpieza completó sin errores críticos.
"""
