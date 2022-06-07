"""Fichero para el modelo Contenido."""
import sqlite3
from models.auto_generate import AutoGenerate
from config.config import SERIES, FILM

class Content(AutoGenerate):
    """Clase que maneja los distinos Contenidos."""
    
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
    
    def union_content(self, limit = 0, where = 0):
        """Obtiene una lista de filas de la tabla."""
        if where == 0 and limit != 0:
            query = f"""
                        SELECT Cod_Serie AS "Cod_Contenido", Titulo, Genero, N_Temporada, Portada, Trailer, Director, Productor, 
                        Sinopsis, Capitulos, Puntuacion_Media, 0 AS "Duracion"
                        FROM {SERIES} 
                        UNION 
                        SELECT Cod_Pelicula AS "Cod_Contenido", Titulo, Genero, 0 AS "Temporada", Portada, Trailer, Director, 
                        Productor, Sinopsis, 0 AS "Capitulos", Puntuacion_Media, Duracion
                        FROM {FILM}
                        ORDER BY Puntuacion_Media DESC LIMIT {limit}
                    """

        elif where == 0 and limit == 0:
            query = f"""
                        SELECT Cod_Serie AS "Cod_Contenido", Titulo, Genero, N_Temporada, Portada, Trailer, Director, Productor, 
                        Sinopsis, Capitulos, Puntuacion_Media, 0 AS "Duracion"
                        FROM {SERIES}
                        UNION 
                        SELECT Cod_Pelicula AS "Cod_Contenido", Titulo, Genero, 0 AS "Temporada", Portada, Trailer, Director, 
                        Productor, Sinopsis, 0 AS "Capitulos", Puntuacion_Media, Duracion
                        FROM {FILM}
                        ORDER BY Titulo
                    """

        elif len(list(where.values())) == 1 and limit == 0: 
            clave = list(where.keys())[0] 
            value = where[clave]
            where_clause = f"{clave} LIKE ?"
            query = f"""
                        SELECT Cod_Serie AS "Cod_Contenido", Titulo, Genero, N_Temporada, Portada, Trailer, Director, Productor, 
                        Sinopsis, Capitulos, Puntuacion_Media, 0 AS "Duracion"
                        FROM {SERIES}
                        WHERE {where_clause}
                        UNION 
                        SELECT Cod_Pelicula AS "Cod_Contenido", Titulo, Genero, 0 AS "Temporada", Portada, Trailer, Director, 
                        Productor, Sinopsis, 0 AS "Capitulos", Puntuacion_Media, Duracion
                        FROM {FILM}
                        WHERE {where_clause}
                    """

        rows = None

        try:
            conn = self._connect()
            cursor = conn.cursor()
            if where == 0:
                cursor.execute(query)
            elif len(list(where.values())) == 1:
                cursor.execute(query, (value,value,))
            rows = cursor.fetchall()
            conn.close()
        
        except sqlite3.Error as error:
            print("Error while executing sqlite script", error)
        
        finally:
            if conn:
                conn.close()

        return rows
