"""Fichero para el modelo Favourites"""
import sqlite3
from models.model import Model
from config.config import FAVORITES, SERIES, FILM, FAVORITES_CONTENT

class Favorites(Model):
    """Clase que maneja la tabla Favoritos"""
    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = FAVORITES
    
    def insert_favorite_content(self, cod_favorite, cod_content):
        """Inserta un contenido en la lista de favoritos"""
        query = f"""
                    INSERT INTO {FAVORITES_CONTENT} (Cod_Favoritos, Cod_Contenido)
                    VALUES ("{cod_favorite}", "{cod_content}")
                """
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)

        finally:
            if conn:
                conn.close()
                
        return True

    def content(self, cod_content, fields_series=None, fields_film=None):
        """Muestra el contenido enlazado a la lista de favoritos"""
        rows = None
        query = ""

        if len(fields_series) != 0 and len(fields_film) != 0:
            query = f"""
                        SELECT {', '.join(fields_series)}
                        FROM {self._table_name} INNER JOIN {FAVORITES_CONTENT} 
                                                ON {self._table_name}.Cod_Favoritos = {FAVORITES_CONTENT}.Cod_Favoritos
                                                INNER JOIN {SERIES}
                                                ON {FAVORITES_CONTENT}.Cod_Contenido = {SERIES}.Cod_Serie
                        WHERE {self._table_name}.Cod_Favoritos = "{cod_content}"
                        UNION
                        SELECT {', '.join(fields_film)}, 0 AS "Temporada"
                        FROM {self._table_name} INNER JOIN {FAVORITES_CONTENT} 
                                                ON {self._table_name}.Cod_Favoritos = {FAVORITES_CONTENT}.Cod_Favoritos
                                                INNER JOIN {FILM}
                                                ON {FAVORITES_CONTENT}.Cod_Contenido = {FILM}.Cod_Pelicula
                        WHERE {self._table_name}.Cod_Favoritos = "{cod_content}"
                    """

        elif len(fields_series) != 0 and len(fields_film) == 0:
            query = f"""
                        SELECT {', '.join(fields_series)}
                        FROM {self._table_name} INNER JOIN {FAVORITES_CONTENT} 
                                                ON {self._table_name}.Cod_Favoritos = {FAVORITES_CONTENT}.Cod_Favoritos
                                                INNER JOIN {SERIES}
                                                ON {FAVORITES_CONTENT}.Cod_Contenido = {SERIES}.Cod_Serie
                        WHERE {self._table_name}.Cod_Favoritos = "{cod_content}"
                    """

        elif len(fields_series) == 0 and len(fields_film) != 0:
            query = f"""
                        SELECT {', '.join(fields_film)}, 0 AS "Temporada"
                        FROM {self._table_name} INNER JOIN {FAVORITES_CONTENT} 
                                                ON {self._table_name}.Cod_Favoritos = {FAVORITES_CONTENT}.Cod_Favoritos
                                                INNER JOIN {FILM}
                                                ON {FAVORITES_CONTENT}.Cod_Contenido = {FILM}.Cod_Pelicula
                        WHERE {self._table_name}.Cod_Favoritos = "{cod_content}"
                    """

        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)

        finally:
            if conn:
                conn.close()

        return rows
