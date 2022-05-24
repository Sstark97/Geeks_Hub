"""Fichero para el modelo Profile."""
from models.model import Model
from config.config import PROFILE

class Profile(Model):
    """Clase que maneja la Tabla Perfil."""
    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = PROFILE
