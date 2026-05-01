# frontend_python/utils.py
import sys
import os

def resource_path(relative_path):
    """
    Obtiene la ruta absoluta del recurso.
    Funciona tanto en modo desarrollo como cuando está empaquetado con PyInstaller.
    """
    if getattr(sys, 'frozen', False):
        # Si está empaquetado con PyInstaller
        base_path = sys._MEIPASS
    else:
        # Si se ejecuta como script normal
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)

def get_engine_path():
    """
    Busca secureguard_engine.exe
    En desarrollo: está en frontend_python/
    Empaquetado: estará en la misma carpeta que el .exe
    """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, "secureguard_engine.exe")

def get_signatures_path():
    """
    Busca la carpeta de firmas (assets/signatures)
    Como assets está DENTRO de frontend_python, usamos ruta directa
    """
    return resource_path(os.path.join("assets", "signatures"))