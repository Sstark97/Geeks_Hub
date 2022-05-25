"""Fichero para el modelo Film."""
from models.model import Model
from config.config import FILM

class Film(Model):
    """Clase que maneja la Tabla Pelicula."""
    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = FILM
