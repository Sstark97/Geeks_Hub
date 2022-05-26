"""Fichero para el modelo Film."""
from models.model import Model
from config.config import FILM

class Film(Model):
    """Clase que maneja la Tabla Pelicula."""
    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = FILM
    def code_generator(self):
        """Genera un código único para la Pelicula."""
        conn = self._connect()
        cursor = conn.cursor()
        query = 'SELECT COUNT(Pelicula.Cod_Pelicula) + 1 FROM Pelicula'
        cursor.execute(query)
        contador = cursor.fetchone()[0]
        cod_pelicula = ""
        
        if contador < 10:
            cod_pelicula = f"P00{contador}"
        elif contador < 100:
            cod_pelicula = f"P0{contador}"
        elif contador < 1000:
            cod_pelicula = f"P{contador}"
        cursor.close()
        conn.close()
        return cod_pelicula
