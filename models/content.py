"""Fichero para el modelo Contenido."""
from models.auto_generate import AutoGenerate

class Content(AutoGenerate):
    """Clase que maneja los distinos Contenidos."""
    def __init__(self, db_name, table_name):
        """Constructor de la clase Content."""
        super().__init__(db_name, table_name)
    
    def top_content(self, fields, limit):
        """Devuelve los mejores contenidos hasta el limite."""
        conn = self._connect()
        cursor = conn.cursor()
        query = f"SELECT {', '.join(fields)} FROM {self._table_name} ORDER BY Puntuacion_Media DESC LIMIT ?"
        cursor.execute(query, (limit,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
