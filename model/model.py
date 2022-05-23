""" Fichero de definicion del Modelo generico"""
import sqlite3
from abc import ABC

class Model(ABC):
    """Clase que representa un modelo de datos generico con todas sus operaciones basicas."""
    def __init__(self, db_name):
        self._table_name = ""
        self.db_name = db_name

    def _connect(self):
        """Conexión a la base de datos."""
        conn = sqlite3.connect(self.db_name)
        return conn

    def insert(self, data):
        """Inserta una fila en la tabla."""
        data_keys = list(data.keys()) 
        data_values = list(data.values())
        
        query = f"INSERT INTO {self._table_name} ({', '.join(data_keys)}) VALUES ({', '.join(['?'] * len(data_values))})"

        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query, data_values)
            conn.commit()
            cursor.close()
            
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)

        finally:
            if conn:
                conn.close()
    
    def update(self, data, where):
        """Actualiza una fila en la tabla."""
        data_keys = list(data.keys())
        data_values = list(data.values())
        where_key = list(where.keys())[0]      
        query = f"UPDATE {self._table_name} SET {', '.join([f'{key} = ?' for key in data_keys])} WHERE {where_key} LIKE ?"
        
        values = data_values + [where[where_key]]
        values = tuple(values)   

        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
        
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)
        
        finally:
            if conn:
                conn.close()
    
    def delete(self, where):
        """Elimina una fila de la tabla."""
        clave = list(where.keys())[0] 
        value = where[clave]
        where_clause = f"{clave} LIKE ?"
        query = f"DELETE FROM {self._table_name} WHERE {where_clause}"

        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query, (value,))
            conn.commit()
            cursor.close()
        
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)
        
        finally:
            if conn:
                conn.close()
    
    def get(self, fields, where):
        """Obtiene una fila de la tabla."""
        clave = list(where.keys())[0] 
        value = where[clave]
        where_clause = f"{clave} LIKE ?"
        query = f"SELECT {', '.join(fields)} FROM {self._table_name} WHERE {where_clause}"
        row = None

        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query, (value,))
            row = cursor.fetchone()
            conn.close()
        
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)
        
        finally:
            if conn:
                conn.close()

        return row
