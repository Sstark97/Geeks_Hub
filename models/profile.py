"""Fichero para el modelo Profile."""
from models.auto_generate import AutoGenerate
from config.config import PROFILE

class Profile(AutoGenerate):
    """Clase que maneja la Tabla Perfil."""
    def __init__(self, db_name, table_name=PROFILE):
        super().__init__(db_name, table_name)
        