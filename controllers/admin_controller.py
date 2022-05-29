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

    films = films.top_films(["Portada","Titulo"], 5)
    series = series.top_series(["Portada","Titulo"], 5)
    
    return template('admin_index', films=films, series=series)
