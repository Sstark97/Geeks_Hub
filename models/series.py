"""Fichero para el modelo Series"""
from models.content import Content
from config.config import SERIES

class Series(Content):
    """Clase que maneja la Tabla Serie."""
    def __init__(self, db_name, table_name=SERIES):
        super().__init__(db_name, table_name)
