"""
application/quarantine_use_case.py
====================================
Caso de uso: Cuarentena de archivos (Quarantine).

Este archivo orquesta la lógica de negocio para aislar archivos
detectados como amenazas en una carpeta segura del sistema.

Un archivo en cuarentena está desactivado: no puede ejecutarse
ni afectar al sistema, pero no se elimina permanentemente.

Dependencias que recibe por inyección (constructor):
    - manager: IQuarantineManager → gestiona el movimiento físico del archivo

Clases que debe contener:
--------------------------

QuarantineUseCase:
    Orquestador del proceso de cuarentena.

    Método: execute(request: QuarantineRequestDTO) -> QuarantineResponseDTO
        Flujo interno:
            1. Recibe el path del archivo amenazante desde el DTO.
            2. Valida que el archivo existe antes de intentar moverlo.
            3. Crea un ThreatFile con la información del archivo.
            4. Delega el movimiento físico al IQuarantineManager.
            5. Si el movimiento falla, captura la excepción y retorna
               un QuarantineResponseDTO con success=False y el mensaje de error.
            6. Si tiene éxito, retorna el DTO con la nueva ruta del archivo.

    Método: list_quarantined() -> list[dict]
        Retorna una lista simplificada de todos los archivos en cuarentena,
        formateada para ser consumida directamente por la presentación.

    Método: restore_file(file_path: str) -> bool
        Solicita al IQuarantineManager restaurar un archivo de cuarentena
        a su ubicación original. Retorna True si fue exitoso.

    Método: _validate_file_exists(path: str) -> bool  [privado]
        Verifica internamente que el archivo a cuarentenar existe y es accesible.
        Lanza InvalidFilePathException si no existe.
"""
