"""Fichero para el modelo History."""
from models.model import Model
from config.config import HISTORY

class History(Model):
    """Clase que maneja la Tabla Historial."""
    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = HISTORY
