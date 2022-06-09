"""Fichero para el modelo Account."""
import sqlite3
from models.model import Model
from config.config import ACCOUNT, PROFILE

class Account(Model):
    """Clase que maneja la Tabla Cuenta."""
    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = ACCOUNT

    def n_profiles(self, fields, where):
        """Obtiene una lista de filas de la tabla."""

        clave = list(where.keys())[0] 
        value = where[clave]
        where_clause = f"{clave} LIKE ?"
        query = f"""
                    SELECT COUNT({', '.join(fields)})
                    FROM {self._table_name} INNER JOIN {PROFILE} ON {self._table_name}.Correo = {PROFILE}.Correo
                    WHERE {self._table_name}.{where_clause}
                """

        rows = None

        try:
            conn = self._connect()
            cursor = conn.cursor()
            if where == 0:
                cursor.execute(query)
            elif len(list(where.values())) == 1:
                cursor.execute(query, (value,))
            else:
                cursor.execute(query, value)
            rows = cursor.fetchall()
            conn.close()
        
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)
        
        finally:
            if conn:
                conn.close()

        return rows
