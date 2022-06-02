"""Archivo de Rutas de las Peliculas."""
import sys
from os import remove
from datetime import datetime
from bottle import get, post, request, template, redirect, auth_basic
from utils.admin_auth import is_authenticated_user
from models.film import Film
from config.config import DATA_BASE, FILM_FIELDS
from forms.films_form import FilmsForm
from forms.delete_content_form import DeleteContentForm
sys.path.append('static')

@get('/admin/films')
@auth_basic(is_authenticated_user)
def films_index():
    """Página de inicio de las Peliculas."""
    peliculas = Film(DATA_BASE)
    rows = peliculas.select(['Cod_Pelicula','Titulo', 'Genero'])

    return template('admin_content',title="Peliculas", class_content="films", content="films", cod="Cod_Pelicula", 
        content_title="Titulo", content_third_row="Genero" ,rows=rows)

@get('/admin/films/new')
@auth_basic(is_authenticated_user)
def films_new():
    """Página de registro de peliculas."""
    form = FilmsForm(request.POST)
    return template('films_form',title="Nueva Película", form=form, path='/admin/films/new')

@post('/admin/films/new')
@auth_basic(is_authenticated_user)
def films_process():
    """Procesa el formulario de registro de peliculas."""
    form = FilmsForm(request.POST) 
    films = Film(DATA_BASE)
    if form.submit.data and form.cover_page and form.validate():
        image_data = request.files.get('cover_page')
        file_path = f"static/img/movies/{image_data.filename}"

        with open(file_path, 'wb') as file:
            file.write(image_data.file.read())

        form_data = {
            'Cod_Pelicula': films.code_generator("P", "Cod_Pelicula"),
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

@get('/admin/films/<cod>')
@auth_basic(is_authenticated_user)
def films_view(cod):
    """Página de visualización de Peliculas."""
    films = Film(DATA_BASE)
    row = films.select(['*'],{'Cod_Pelicula': cod})[0]

    film = {
        'Cod_Pelicula': row[0],
        'Titulo' : row[1],
        'Calificacion_Edad' : row[2],
        'Genero' : row[3],
        'Director' : row[4],
        'Puntuacion_Media' : row[5],
        'Productor' : row[6],
        'Sinopsis' : row[7],
        'Fecha_Publicacion' : row[8],
        'Portada': row[9],
        'Trailer' : row[10],
        'Duracion' : row[11]
    }

    return template('admin_view_content', title=row[1], content_type="films", content=film, fields=FILM_FIELDS, cod=cod)

@get('/admin/films/edit/<cod>')
@auth_basic(is_authenticated_user)
def films_edit(cod):
    """Página de edición de Peliculas."""
    films = Film(DATA_BASE)
    row = films.select(['*'], {'Cod_Pelicula': cod})[0]
    formatted_date= datetime.strptime(row[8], '%Y-%m-%d')

    form = FilmsForm(request.POST)
    form.title.data = row[1]
    form.age_rating.data = row[2]
    form.genre.data = row[3]
    form.director.data = row[4]
    form.average_score.data = row[5]
    form.productor.data = row[6]
    form.synopsis.data = row[7]
    form.release_date.data = formatted_date
    form.trailer.data = row[10]
    form.duration.data = row[11]

    return template('films_form', title="Editar Película", form=form, path=f'/admin/films/edit/{cod}')

@post('/admin/films/edit/<cod>')
@auth_basic(is_authenticated_user)
def films_process_edit(cod):
    """Procesa el formulario de edición de Peliculas."""
    form = FilmsForm(request.POST)
    films = Film(DATA_BASE)
    file_path = ""
    if form.submit.data and form.cover_page and form.validate():
        if form.cover_page and request.files.get('cover_page'):
            image_data = request.files.get('cover_page')
            file_path = f"static/img/movies/{image_data.filename}"

            with open(file_path, 'wb') as file:
                file.write(image_data.file.read())

        form_data = {
            'Titulo' : form.title.data,
            'Calificacion_Edad' : form.age_rating.data,
            'Genero' : form.genre.data,
            'Director' : form.director.data,
            'Puntuacion_Media' : float(form.average_score.data),
            'Productor' : form.productor.data,
            'Sinopsis' : form.synopsis.data,
            'Fecha_Publicacion' : str(form.release_date.data),
            'Trailer' : form.trailer.data,
            'Duracion' : form.duration.data
        }

        if file_path != "":
            img_path = films.get(['Portada'], {'Cod_Pelicula': cod})[0]
            remove(img_path)
            form_data['Portada'] = file_path

        films.update(form_data, {'Cod_Pelicula': cod})
        redirect('/admin/films')
    return template('films_form', form=form)

@get('/admin/films/delete/<cod>')
@auth_basic(is_authenticated_user)
def films_delete_index(cod):
    """Eliminar una Pelicula."""
    form = DeleteContentForm(request.POST)
    films = Film(DATA_BASE)
    film_title = films.get(['Titulo'], {'Cod_Pelicula': cod})

    return template('admin_delete_content', title="Eliminar Pelicula",content="Pelicula", uri="films", content_title=film_title, cod=cod, form=form)

@post('/admin/films/delete/<cod>')
@auth_basic(is_authenticated_user)
def films_delete(cod):
    """Procesa la eliminación de una Pelicula."""
    form = DeleteContentForm(request.POST)
    if form.delete.data:
        films = Film(DATA_BASE)
        img_path = films.get(['Portada'], {'Cod_Pelicula': cod})[0]
        remove(img_path)

        films.delete({'Cod_Pelicula': cod})
        redirect('/admin/films')

    if form.cancel.data:
        redirect('/admin/films')
