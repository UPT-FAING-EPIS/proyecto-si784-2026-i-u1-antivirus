"""
config/settings.py
====================
Configuraciones globales del sistema antivirus.

Este archivo centraliza todas las variables de configuración del proyecto.
Permite cambiar el comportamiento del sistema desde un único punto,
sin modificar el código de los módulos de negocio.

Puede cargar valores desde un archivo .env usando python-dotenv,
con valores por defecto razonables si las variables no están definidas.

Uso:
    from config.settings import Settings
    settings = Settings()
    db_path = settings.DB_PATH

Clases que debe contener:
--------------------------

Settings:
    Contenedor de todas las configuraciones del sistema.

    Constructor:
        Carga las variables de entorno desde el archivo .env (si existe).
        Asigna valores por defecto a cada configuración si no están en .env.

    Atributos principales:
        DB_PATH (str):
            Ruta al archivo de base de datos SQLite.
            Default: 'antivirus.db' (en el directorio raíz del proyecto).

        QUARANTINE_DIR (str):
            Ruta de la carpeta donde se mueven los archivos en cuarentena.
            Default: './quarantine' (carpeta en el directorio raíz).

        TEMP_DIRS (list[str]):
            Lista de directorios temporales del sistema operativo a limpiar.
            Se auto-detecta según el sistema operativo en uso.

        SCAN_EXTENSIONS (list[str]):
            Extensiones de archivo que el scanner debe analizar.
            Default: ['.exe', '.dll', '.bat', '.ps1', '.vbs', '.js', '.pdf',
                      '.docm', '.xlsm', '.zip', '.rar', '.jar', '.py']

        MAX_FILE_SIZE_MB (int):
            Tamaño máximo en MB de un archivo para ser escaneado.
            Archivos más grandes se omiten por razones de rendimiento.
            Default: 100 (100 MB).

        MONITOR_DIRECTORY (str):
            Directorio que la protección en tiempo real vigilará por defecto.
            Default: directorio de Descargas del usuario actual.

        AUTO_QUARANTINE_LEVELS (list[str]):
            Niveles de amenaza que se cuarentenan automáticamente sin preguntar.
            Default: ['CRITICAL', 'HIGH'].

        APP_VERSION (str):
            Versión actual del sistema antivirus para mostrar en el banner.
            Default: '1.0.0'.
"""
