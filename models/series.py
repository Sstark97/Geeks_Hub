"""Fichero para el modelo Series"""
from models.model import Model
from config.config import SERIES

class Series(Model):
    """Clase que maneja la Tabla Serie."""
    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = SERIES
    
    def code_generator(self):
        """Genera un código único para la serie."""
        conn = self._connect()
        cursor = conn.cursor()
        query = 'SELECT COUNT(Serie.Cod_Serie) + 1 FROM Serie'
        cursor.execute(query)
        contador = cursor.fetchone()[0]
        cod_serie = ""
        
        if contador < 10:
            cod_serie = f"S00{contador}"
        elif contador < 100:
            cod_serie = f"S0{contador}"
        elif contador < 1000:
            cod_serie = f"S{contador}"
        cursor.close()
        conn.close()
        return cod_serie
    
    def top_series(self, fields, limit):
        """Devuelve las mejores series hasta el limite."""
        conn = self._connect()
        cursor = conn.cursor()
        query = f"SELECT {', '.join(fields)} FROM {SERIES} ORDER BY Puntuacion_Media DESC LIMIT ?"
        cursor.execute(query, (limit,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
