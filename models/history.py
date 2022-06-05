"""Fichero para el modelo History."""
import sqlite3
from models.model import Model
from config.config import HISTORY, SERIES, FILM


class History(Model):
    """Clase que maneja la Tabla Historial."""

    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = HISTORY

    def content(self, cod_profile, fields_series=None, fields_film=None):
        """Muestra el contenido del Historial."""
        rows = None
        query = ""

        if len(fields_series) != 0 and len(fields_film) != 0:
            query = f"""
                        SELECT {', '.join(fields_series)}
                        FROM {self._table_name} INNER JOIN {SERIES}
                                                ON {self._table_name}.Cod_Contenido = {SERIES}.Cod_Serie
                        WHERE {self._table_name}.Cod_Perfil = "{cod_profile}"
                        UNION
                        SELECT {', '.join(fields_film)}, 0 AS "Temporada"
                        FROM {self._table_name} INNER JOIN {FILM}
                                                ON {self._table_name}.Cod_Contenido = {FILM}.Cod_Pelicula
                        WHERE {self._table_name}.Cod_Favoritos = "{cod_profile}"
                    """

        elif len(fields_series) != 0 and len(fields_film) == 0:
            query = f"""
                        SELECT {', '.join(fields_series)}
                        FROM {self._table_name} INNER JOIN {SERIES}
                                                ON {self._table_name}.Cod_Contenido = {SERIES}.Cod_Serie
                        UNION
                        SELECT {', '.join(fields_film)}, 0 AS "Temporada"
                        FROM {self._table_name} INNER JOIN {FILM}
                                                ON {self._table_name}.Cod_Contenido = {FILM}.Cod_Pelicula
                    """

        elif len(fields_series) == 0 and len(fields_film) != 0:
            query = f"""
                        SELECT {', '.join(fields_film)}, 0 AS "Temporada"
                        FROM {self._table_name} INNER JOIN {FILM}
                                                ON {self._table_name}.Cod_Contenido = {FILM}.Cod_Pelicula
                        WHERE {self._table_name}.Cod_Favoritos = "{cod_profile}"
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
