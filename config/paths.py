"""
config/paths.py
================
Constantes de rutas del sistema resueltas con pathlib.

Este archivo centraliza todas las rutas del proyecto usando pathlib.Path,
que funciona correctamente en Windows, Linux y macOS sin cambios de código.

Usar pathlib en lugar de strings directos para rutas es una buena práctica
que evita errores de separadores (/ vs \) entre sistemas operativos.

No contiene clases. Solo constantes de nivel de módulo:

Constantes que debe definir:
-----------------------------

BASE_DIR (Path):
    Directorio raíz del proyecto.
    Se calcula automáticamente como el directorio padre de este archivo.
    Ejemplo: Path(__file__).resolve().parent.parent

DB_FILE_PATH (Path):
    Ruta completa al archivo de base de datos SQLite.
    Construida como: BASE_DIR / 'antivirus.db'

QUARANTINE_PATH (Path):
    Ruta completa a la carpeta de cuarentena.
    Construida como: BASE_DIR / 'quarantine'
    Se crea automáticamente si no existe al importar este módulo.

QUARANTINE_INDEX_PATH (Path):
    Ruta al archivo JSON que indexa los archivos en cuarentena.
    Construida como: QUARANTINE_PATH / 'quarantine_index.json'

SCHEMA_SQL_PATH (Path):
    Ruta al archivo SQL de creación de la base de datos.
    Construida como: BASE_DIR / 'schema.sql'
    Útil para inicializar la BD en entornos nuevos.

ENV_FILE_PATH (Path):
    Ruta al archivo .env de variables de entorno.
    Construida como: BASE_DIR / '.env'
"""
