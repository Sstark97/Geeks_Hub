"""Fichero para el modelo Film."""
from models.content import Content
from config.config import FILM

class Film(Content):
    """Clase que maneja la Tabla Pelicula."""
    def __init__(self, db_name, table_name=FILM):
        super().__init__(db_name, table_name)
