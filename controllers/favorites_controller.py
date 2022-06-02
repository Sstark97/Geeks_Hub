"""Archivo de Rutas de la lista de Favoritos."""
import sys
from bottle import get
from models.favorites import Favorites
from config.config import DATA_BASE
sys.path.append('models')

@get('/favorites')
def favorites_index():
    """Página de inicio de la lista de Favoritos."""
    favorites = Favorites(DATA_BASE)

    # # Añadir 
    # favorites.insert({"Cod_Favoritos": "FV13", "Fecha_Creacion": "2022-05-01"})
    # row = favorites.select(['*'], {"Cod_Favoritos": "FV13"})

    # # Actualizar
    # favorites.update({"Fecha_Creacion": "2022-04-01"}, {"Cod_Favoritos": "FV13"})
    # row = favorites.select(['*'], {"Cod_Favoritos": "FV13"})

    # Eliminar
    # favorites.delete({"Cod_Favoritos": "FV13"})
    
    # # Select de todo el contenido
    row = favorites.content("FV05", ["Cod_Contenido", "Titulo", "Genero", "N_Temporada"], ["Cod_Contenido", "Titulo", "Genero"])

    # # Select de series
    # row = favorites.content("FV05", ["Cod_Contenido", "Titulo", "Genero", "N_Temporada"], [])

    # # Select de películas
    # row = favorites.content("FV05", [], ["Cod_Contenido", "Titulo", "Genero"])

    return str(row)
    