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
def films_index():
    """Página de inicio de las Peliculas."""
    peliculas = Film(DATA_BASE)
    rows = peliculas.select(['Cod_Pelicula','Titulo', 'Genero'])

    return template('admin_content',title="Pelicula", content="films", cod="Cod_Pelicula", 
        content_title="Titulo", content_third_row="Genero" ,rows=rows)

@get('/admin/films/new')
def films_new():
    """Página de registro de peliculas."""
    form = FilmsForm(request.POST)
    return template('films_form', form=form, path='/admin/films/new')

@post('/admin/films/new')
def films_process():
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

@get('/admin/films/<cod>')
def films_view(cod):
    """Página de visualización de Peliculas."""
    films = Film(DATA_BASE)
    row = films.select(['*'],{'Cod_Pelicula': cod})
    print(row)

    return template('admin_view_content', title=row[0][1], content=row, content_type="films", fields=FILM_FIELDS, img_col=9,  cod=cod)

@get('/admin/films/edit/<cod>')
def films_edit(cod):
    """Página de edición de Peliculas."""
    films = Film(DATA_BASE)
    row = films.select(['*'], {'Cod_Pelicula': cod})[0]
    print(row[8])
    formatted_date= datetime.strptime(row[8], '%Y-%m-%d')
    print(formatted_date)

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

    return template('films_form', form=form, path=f'/admin/films/edit/{cod}')

@post('/admin/films/edit/<cod>')
def films_process_edit(cod):
    """Procesa el formulario de edición de Peliculas."""
    form = FilmsForm(request.POST)
    films = Film(DATA_BASE)
    file_path = ""
    if form.submit.data and form.cover_page and form.validate():
        if form.cover_page and request.files.get('cover_page'):
            image_data = request.files.get('cover_page')
            file_path = f"static/img/films/{image_data.filename}"

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
