"""Archivo de Rutas del administrador."""
from bottle import get, template, auth_basic
from controllers.film_controller import *
from controllers.series_controller import *
from utils.admin_auth import is_authenticated_user
from config.config import DATA_BASE
from models.film import Film
from models.series import Series

@get('/admin')
@auth_basic(is_authenticated_user)
def admin():
    """Página de inicio del administrador de la aplicación."""
    series = Series(DATA_BASE)
    films = Film(DATA_BASE)

    films = films.top_content(["Cod_Pelicula","Portada","Titulo"], 5)
    series = series.top_content(["Cod_Serie","Portada","Titulo"], 5)
    
    return template('admin_index', films=films, series=series)
