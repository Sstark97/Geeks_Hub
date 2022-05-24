"""Fichero para el modelo Series"""
from models.model import Model
from config.config import SERIES

class Film(Model):
    """Clase que maneja la Tabla Serie."""
    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = SERIES
