"""Archivo de Rutas del administrador."""
from bottle import get, template
from controllers.film_controller import *
from controllers.series_controller import *
from config.config import DATA_BASE
from models.film import Film
from models.series import Series

@get('/admin')
def admin():
    """Página de inicio del administrador de la aplicación."""
    series = Series(DATA_BASE)
    films = Film(DATA_BASE)

    top_films = films.top_films(["Portada","Titulo"], 5)
    top_series = series.top_series(["Portada","Titulo"], 5)

    return str(top_series)

    # top_5_series = series.select(['Cod_Serie', 'Titulo', 'Genero'], {})
    # top_5_films = films.select(['Cod_Pelicula', 'Titulo', 'Genero'], 'Cod_Pelicula', 'DESC', 5)
    
    return template('admin_index.tpl')
