"""
application/cleanup_use_case.py
=================================
Caso de uso: Limpieza del sistema (PC Cleanup).

Este archivo orquesta la lógica de negocio para limpiar archivos
temporales y basura del sistema operativo.

La limpieza NO toca archivos del usuario ni del sistema operativo crítico.
Solo elimina archivos temporales seguros y, opcionalmente, la cuarentena.

Dependencias que recibe por inyección (constructor):
    - cleanup_service: ICleanupService → localiza y elimina archivos temporales
    - quarantine_manager: IQuarantineManager → accede a la lista de cuarentena

Clases que debe contener:
--------------------------

PCCleanupUseCase:
    Orquestador de la limpieza del sistema.

    Método: preview(request: CleanupRequestDTO) -> list[str]
        Muestra al usuario qué archivos SERÍAN eliminados sin eliminarlos aún.
        Útil para presentar una vista previa antes de confirmar la limpieza.
        Flujo interno:
            1. Llama a ICleanupService.find_temp_files() para obtener la lista.
            2. Si include_quarantine es True, agrega los archivos de cuarentena.
            3. Retorna la lista combinada de rutas.

    Método: execute(request: CleanupRequestDTO) -> CleanupReportDTO
        Realiza la limpieza efectiva del sistema.
        Flujo interno:
            1. Llama a preview() para obtener la lista de archivos a eliminar.
            2. Delega la eliminación al ICleanupService.
            3. Registra cuántos archivos se eliminaron y cuántos bytes se liberaron.
            4. Captura errores individuales sin detener toda la operación.
            5. Construye y retorna un CleanupReportDTO con el resumen completo.

    Método: _calculate_total_size(paths: list[str]) -> int  [privado]
        Calcula el tamaño total en bytes de los archivos que serán eliminados.
        Maneja individualmente los errores de acceso a archivos no accesibles.
"""
