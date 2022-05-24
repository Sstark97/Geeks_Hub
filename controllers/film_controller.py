"""Archivo de Rutas de las Peliculas."""
import sys
from bottle import get
from models.film import Film
from config.config import DATA_BASE
sys.path.append('models')

@get('/films')
def index():
    """Página de inicio de las Peliculas."""
    peliculas = Film(DATA_BASE)

    # Añadir 
    # peliculas.insert({'Cod_Pelicula':'P029' ,'Titulo': 'El Padrino', 'Calificacion_Edad': '18', 
    # 'Genero': 'Drama', 'Director': 'Francis Ford Coppola', 'Puntuacion_Media':4.94, 'productor': 'Paramount Pictures',
    # 'Sinopsis':'El Padrino','Fecha_Publicacion': '1972-12-11', 'Portada': 'https://www.impawards.com/1972/posters/padrino.jpg',
    # 'Trailer': 'https://www.youtube.com/watch?v=z_p5XD-bZbE', 'Duracion': 154})
    # row = peliculas.select(['*'], {"Titulo": "El Padrino"})

    # Actualizar
    # peliculas.update({'Titulo': 'El Padrino 2', 'Puntuacion_Media': 4.99}, {'Cod_Pelicula': 'P029'})
    # row = peliculas.select(['*'], {"Titulo": "El Padrino 2"})

    # Eliminar
    # peliculas.delete({'Cod_Pelicula': 'P029'})
    row = peliculas.select(['*'])

    return str(row)