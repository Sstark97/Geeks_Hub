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
    """Página de registro de peliculas."""
    form = FilmsForm(request.POST)
    return template('films_form', form=form, path='/admin/films/new')

@post('/admin/films/new')
def series_process():
    """Procesa el formulario de registro de peliculas."""
    form = FilmsForm(request.POST) 
    films = Film(DATA_BASE)
    if form.submit.data and form.cover_page and form.validate():
        image_data = request.files.get('cover_page')
        file_path = f"static/img/films/{image_data.filename}"

        with open(file_path, 'wb') as file:
            file.write(image_data.file.read())

        form_data = {
            'Cod_Pelicula': films.code_generator(),
            'Titulo' : form.title.data,
            'Calificacion_Edad' : form.age_rating.data,
            'Genero' : form.genre.data,
            'Director' : form.director.data,
            'Puntuacion_Media' : float(form.average_score.data),
            'Productor' : form.productor.data,
            'Sinopsis' : form.synopsis.data,
            'Fecha_Publicacion' : str(form.release_date.data),
            'Portada': file_path,
            'Trailer' : form.trailer.data,
            'Duracion' : form.duration.data
        }
        
        films.insert(form_data)
        redirect('/admin/films')
    return template('films_form', form=form)
