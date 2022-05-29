"""Archivo de Rutas de las Peliculas."""
import sys
from os import remove
from datetime import datetime
from bottle import get, post, request, template, redirect
from models.film import Film
from config.config import DATA_BASE, FILM_FIELDS
from forms.films_form import FilmsForm
from forms.delete_content_form import DeleteContentForm

@get('/admin/films')
def series_index():
    """Página de inicio de las Peliculas."""
    peliculas = Film(DATA_BASE)
    rows = peliculas.select(['Cod_Pelicula','Titulo', 'Genero'])

    return template('admin_content',title="Pelicula", content="films", cod="Cod_Pelicula", 
        content_title="Titulo", content_third_row="Genero" ,rows=rows)

@get('/admin/films/new')
def series_new():
    """Página de registro de series."""
    form = FilmsForm(request.POST)
    return template('films_form', form=form, path='/admin/films/new')
