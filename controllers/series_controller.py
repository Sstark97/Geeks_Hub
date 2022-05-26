"""Archivo de Rutas de las Series."""
import sys
from os import remove
from bottle import get, post, request, template, redirect
from models.series import Series
from config.config import DATA_BASE
from forms.series_form import SeriesForm
from forms.delete_content_form import DeleteContentForm

sys.path.append('models')
sys.path.append('forms')

@get('/admin/series')
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
    rows = series.select(['Cod_Serie','Titulo', 'N_Temporada'])

    return template('admin_content',title="Series", cod="Cod_Serie", content_title="Titulo", content_third_row="N_Temporada" ,rows=rows)

@get('/admin/series/new')
def series_new():
    """Página de registro de series."""
    form = SeriesForm(request.POST)
    return template('series_form', form=form)

@post('/admin/series/new')
def series_process():
    """Procesa el formulario de registro de series."""
    form = SeriesForm(request.POST) 
    series = Series(DATA_BASE)
    if form.submit.data and form.cover_page and form.validate():
        image_data = request.files.get('cover_page')
        file_path = f"static/img/series/{image_data.filename}"

        with open(file_path, 'wb') as file:
            file.write(image_data.file.read())

        form_data = {
            'Cod_Serie': series.code_generator(),
            'N_Temporada' : form.season.data,
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
            'Capitulos' : form.chapters.data
        }
        
        series.insert(form_data)
        redirect('/admin/series')
    return template('series_form', form=form)

@get('/admin/series/delete/<cod>')
def series_delete_index(cod):
    """Eliminar una serie."""
    form = DeleteContentForm(request.POST)
    series = Series(DATA_BASE)
    serie_title = series.get(['Titulo'], {'Cod_Serie': cod})

    return template('admin_delete_content', title="Eliminar Serie",content="Serie", content_title=serie_title, cod=cod, form=form)

@post('/admin/series/delete/<cod>')
def series_delete(cod):
    """Procesa la eliminación de una serie."""
    form = DeleteContentForm(request.POST)
    if form.delete:
        series = Series(DATA_BASE)
        img_path = series.get(['Portada'], {'Cod_Serie': cod})[0]
        remove(img_path)

        series.delete({'Cod_Serie': cod})
        redirect('/admin/series')

    return redirect('/admin/series')
    
