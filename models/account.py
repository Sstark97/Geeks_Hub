"""Fichero para el modelo Account."""
from models.model import Model
from config.config import ACCOUNT

class Account(Model):
    """Clase que maneja la Tabla Cuenta."""
    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = ACCOUNT
