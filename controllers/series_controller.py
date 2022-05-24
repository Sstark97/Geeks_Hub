"""Archivo de Rutas de las Series."""
import sys
from bottle import get
from models.series import Series
from config.config import DATA_BASE
sys.path.append('models')

@get('/series')
def series_index():
    """Página de inicio de las Series."""
    series = Series(DATA_BASE)

    # Añadir 
    # series.insert({'Cod_Serie':'S028' ,'N_Temporada': 1 , 'Titulo': 'WandaVision', 'Calificacion_Edad': '16', 
    # 'Genero': 'Ciencia Ficcion', 'Director': 'Kevin Feige', 'Puntuacion_Media':4.99, 'productor': 'Marvel Studios',
    # 'Sinopsis':'Wanda y Vision','Fecha_Publicacion': '2021-03-11', 'Portada': 'https://www.impawards.com/2021/posters/wandavision.jpg',
    # 'Trailer': 'https://www.youtube.com/watch?v=vCfjy6S6Nu0','Capitulos': 9})
    # row = series.select(['*'], {"Titulo": "WandaVision"})

    # Actualizar
    # series.update({'Puntuacion_Media': 5.00, 'Capitulos': 12 }, {'Cod_Serie': 'S028'})
    # row = series.select(['*'], {"Titulo": "WandaVision"})

    # Eliminar
    # series.delete({'Cod_Serie': 'S028'})
    
    # Select por generos
    # row = series.select(['*'],{"Genero": "Ciencia Ficcion"})

    # Select de todas las series
    row = series.select(['*'])

    return str(row)
    