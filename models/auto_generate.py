"""Fichero para el modelo Auto_Generate."""
from models.model import Model

class AutoGenerate(Model):
    """Métodos para generar códigos únicos."""

    def __init__(self, db_name, table_name):
        """Constructor de la clase Auto_Generate."""
        super().__init__(db_name)
        self._table_name = table_name
    
    def code_generator(self, format_code, table_code):
        """Genera un código único para una Tabla"""
        conn = self._connect()
        cursor = conn.cursor()
        query = f'SELECT COUNT({table_code}) + 1 FROM {self._table_name}'
        cursor.execute(query)
        contador = cursor.fetchone()[0]
        cod_table = ""

        if contador < 10:
            cod_table = f"{format_code}00{contador}"
        elif contador < 100:
            cod_table = f"{format_code}0{contador}"
        elif contador < 1000:
            cod_table = f"{format_code}{contador}"
                
        cursor.close()
        conn.close()
        return cod_table
