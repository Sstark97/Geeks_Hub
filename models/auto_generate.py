"""Fichero para el modelo Auto_Generate."""
import re
from models.model import Model

class AutoGenerate(Model):
    """Métodos para generar códigos únicos."""

    def __init__(self, db_name, table_name):
        """Constructor de la clase Auto_Generate."""
        super().__init__(db_name)
        self._table_name = table_name
    
    def __diff_calculate(self, cursor, contador, table_code):
        """Calcula la diferencia entre el contador y el número de filas de la tabla."""
        last_content = f'SELECT {table_code} FROM {self._table_name} ORDER BY {table_code} DESC LIMIT 1'
        cursor.execute(last_content)

        last_code = int(re.findall('[0-9]+', cursor.fetchone()[0])[0])
        diff = (last_code - contador) + 1

        return diff
    
    def code_generator(self, format_code, table_code):
        """Genera un código único para una Tabla"""
        conn = self._connect()
        cursor = conn.cursor()
        query = f'SELECT COUNT({table_code}) FROM {self._table_name}'
        cursor.execute(query)
        contador = cursor.fetchone()[0]

        diff = self.__diff_calculate(cursor, contador, table_code)
        contador += diff

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
