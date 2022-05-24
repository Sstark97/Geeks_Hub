"""Fichero para el modelo Suscripciones."""
from models.model import Model
from config.config import FILM

class Film(Model):
    """Clase que maneja la Tabla Suscriciones."""
    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = FILM
