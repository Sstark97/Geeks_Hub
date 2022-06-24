"""Archivo de Rutas de las Series."""
from os import remove
from datetime import datetime, date
from bottle import get, post, request, template, redirect, auth_basic, FileUpload
from utils.admin_auth import is_authenticated_user
from utils.login_decorator import login_required
from models.series import Series
from models.profile import Profile
from models.favorites import Favorites
from models.history import History
from config.config import DATA_BASE, SERIES_FIELDS, GENRES_FIELDS
from config.local_storage import local_storage
from forms.series_form import SeriesForm
from forms.delete_content_form import DeleteContentForm


@get('/admin/series')
@auth_basic(is_authenticated_user)
def series_index():
    """Página de inicio de las Series."""
    series = Series(DATA_BASE)
    rows = series.select(['Cod_Serie', 'Titulo', 'N_Temporada'])

    return template(
        'admin_content',
        title="Series",
        class_content="series",
        content="series",
        cod="Cod_Serie",
        content_title="Titulo",
        content_third_row="N_Temporada",
        rows=rows
    )


@get('/admin/series/new')
@auth_basic(is_authenticated_user)
def series_new():
    """Página de registro de series."""

    form = SeriesForm(request.POST)
    return template(
        'series_form',
        title="Nueva Serie",
        form=form,
        error="",
        path='/admin/series/new'
    )


@post('/admin/series/new')
@auth_basic(is_authenticated_user)
def series_process():
    """Procesa el formulario de registro de series."""

    form = SeriesForm(request.POST)
    series = Series(DATA_BASE)
    error = "Debes seleccionar una imagen" if not isinstance(form.cover_page.data, FileUpload) else ""

    if form.submit.data and form.validate() and error == "":
        image_data = request.files.get('cover_page')
        file_path = f"static/img/series/{image_data.filename}"

        with open(file_path, 'wb') as file:
            file.write(image_data.file.read())

        form_data = {
            'Cod_Serie': series.code_generator("S", "Cod_Serie"),
            'N_Temporada': form.season.data,
            'Titulo': form.title.data,
            'Calificacion_Edad': form.age_rating.data,
            'Genero': form.GENRES.data,
            'Director': form.director.data,
            'Puntuacion_Media': float(form.average_score.data),
            'Productor': form.productor.data,
            'Sinopsis': form.synopsis.data,
            'Fecha_Publicacion': str(form.release_date.data),
            'Portada': file_path,
            'Trailer': form.trailer.data,
            'Capitulos': form.chapters.data
        }

        series.insert(form_data)
        redirect('/admin/series')

    return template(
        'series_form',
        form=form,
        error=error,
        title="Nueva Serie",
        path='/admin/series/new'
    )


@get('/series/<cod>')
@login_required
def view_series(cod):
    """Página de visualización de Series para los usuarios."""

    series = Series(DATA_BASE)
    row = series.select(['*'], {'Cod_Serie': cod})[0]
    seasons = list(map(lambda x: x[0], series.select(
        ['Cod_Serie'], {'Titulo': row[2]})))
    user = local_storage.getItem("profile")

    personal_profile = Profile(DATA_BASE)
    favorites = Favorites(DATA_BASE)
    history = History(DATA_BASE)

    avatar_perfil = personal_profile.select(
        ["Imagen"], {"Cod_Perfil": user})[0][0]
    cod_profile_perfil = personal_profile.select(
        ["Cod_Favoritos"], {"Cod_Perfil": user})[0][0]

    profile_favorites = favorites.content(
        cod_profile_perfil, ["Cod_Serie", "N_Temporada"], ["Cod_Pelicula"])
    profile_history = history.content(
        user, ["Cod_Serie", "N_Temporada"], ["Cod_Pelicula"])

    cod_favorites = [row[0] for row in profile_favorites]
    cod_history = [row[0] for row in profile_history]

    favorite = cod in cod_favorites
    history = cod in cod_history

    serie = {
        'Cod_Contenido': row[0],
        'Titulo': row[2],
        'N_Temporada': row[1],
        'Calificacion_Edad': row[3],
        'Genero': row[4],
        'Director': row[5],
        'Puntuacion_Media': row[6],
        'Productor': row[7],
        'Sinopsis': row[8],
        'Fecha_Publicacion': row[9],
        'Portada': row[10],
        'Trailer': row[11],
        'Capitulos': row[12]
    }

    path = local_storage.getItem("path")

    return template(
        'view_content',
        title=row[2],
        content_type="series",
        path=path,
        avatar=avatar_perfil,
        content=serie,
        fields=SERIES_FIELDS,
        seasons=seasons,
        favorite=favorite,
        history=history,
        cod=cod
    )



@post('/series/<cod>')
@login_required
def procces_series(cod):
    """Agrega/ Elimina una serie de favoritos."""
    user = local_storage.getItem("profile")
    favorite = request.POST.get('favorite_btn')
    history = request.POST.get('history_btn')

    personal_profile = Profile(DATA_BASE)

    if favorite == "favorite_action":
        favorites = Favorites(DATA_BASE)
        cod_profile_perfil = personal_profile.select(
            ["Cod_Favoritos"], {"Cod_Perfil": user})[0][0]

        profile_favorites = favorites.content(
            cod_profile_perfil, ["Cod_Serie", "N_Temporada"], ["Cod_Pelicula"])

        cod_favorites = [row[0] for row in profile_favorites]

        if cod not in cod_favorites:
            favorites.insert_favorite_content(cod_profile_perfil, cod)
        else:
            favorites.delete_favorite_content(cod_profile_perfil, cod)

    elif history == "history_action":
        history = History(DATA_BASE)

        profile_history = history.content(
            user, ["Cod_Serie", "N_Temporada"], ["Cod_Pelicula"])

        cod_history = [row[0] for row in profile_history]

        if cod not in cod_history:
            today = date.today()
            history.insert({'Cod_Perfil': user, 'Cod_Contenido': cod,
                            "Fecha_Visualizacion": today.strftime("%Y-%m-%d")})
        else:
            history.delete({'Cod_Perfil': user, 'Cod_Contenido': cod})

    redirect(f'/series/{cod}')



@get('/admin/series/<cod>')
@auth_basic(is_authenticated_user)
def admin_series_view(cod):
    """Página de visualización de series."""

    series = Series(DATA_BASE)
    row = series.select(['*'], {'Cod_Serie': cod})[0]

    serie = {
        'Cod_Serie': row[0],
        'Titulo': row[2],
        'N_Temporada': row[1],
        'Calificacion_Edad': row[3],
        'Genero': row[4],
        'Director': row[5],
        'Puntuacion_Media': row[6],
        'Productor': row[7],
        'Sinopsis': row[8],
        'Fecha_Publicacion': row[9],
        'Portada': row[10],
        'Trailer': row[11],
        'Capitulos': row[12]
    }

    return template(
        'admin_view_content',
        title=row[2],
        content_type="series",
        content=serie,
        fields=SERIES_FIELDS,
        cod=cod
    )


@get('/admin/series/edit/<cod>')
@auth_basic(is_authenticated_user)
def series_edit(cod):
    """Página de edición de series."""

    series = Series(DATA_BASE)
    row = series.select(['*'], {'Cod_Serie': cod})[0]
    formatted_date = datetime.strptime(row[9], '%Y-%m-%d')

    form = SeriesForm(request.POST)
    form.title.data = row[2]
    form.season.data = row[1]
    form.age_rating.data = row[3]
    form.GENRES.data = row[4]
    form.director.data = row[5]
    form.average_score.data = row[6]
    form.productor.data = row[7]
    form.synopsis.data = row[8]
    form.release_date.data = formatted_date
    form.trailer.data = row[11]
    form.chapters.data = row[12]

    return template(
        'series_form',
        title="Editar Serie",
        form=form,
        error="",
        path=f'/admin/series/edit/{cod}'
    )


@post('/admin/series/edit/<cod>')
@auth_basic(is_authenticated_user)
def series_process_edit(cod):
    """Procesa el formulario de edición de series."""

    form = SeriesForm(request.POST)
    series = Series(DATA_BASE)
    file_path = ""

    if form.submit.data and form.cover_page and form.validate():

        if form.cover_page and request.files.get('cover_page'):
            image_data = request.files.get('cover_page')
            file_path = f"static/img/series/{image_data.filename}"

            with open(file_path, 'wb') as file:
                file.write(image_data.file.read())

        form_data = {
            'N_Temporada': form.season.data,
            'Titulo': form.title.data,
            'Calificacion_Edad': form.age_rating.data,
            'Genero': form.GENRES.data,
            'Director': form.director.data,
            'Puntuacion_Media': float(form.average_score.data),
            'Productor': form.productor.data,
            'Sinopsis': form.synopsis.data,
            'Fecha_Publicacion': str(form.release_date.data),
            'Trailer': form.trailer.data,
            'Capitulos': form.chapters.data
        }

        if file_path != "":
            img_path = series.get(['Portada'], {'Cod_Serie': cod})[0]
            remove(img_path)
            form_data['Portada'] = file_path

        series.update(form_data, {'Cod_Serie': cod})
        redirect('/admin/series')

    return template(
        'series_form',
        form=form,
        title="Editar Serie",
        path=f'/admin/series/edit/{cod}',
        error=""
    )


@get('/admin/series/delete/<cod>')
@auth_basic(is_authenticated_user)
def series_delete_index(cod):
    """Eliminar una serie."""

    form = DeleteContentForm(request.POST)
    series = Series(DATA_BASE)
    serie_title = series.get(['Titulo'], {'Cod_Serie': cod})

    return template(
        'admin_delete_content',
        title="Eliminar Serie",
        content="Serie",
        uri="series",
        content_title=serie_title,
        cod=cod,
        form=form
    )


@post('/admin/series/delete/<cod>')
@auth_basic(is_authenticated_user)
def series_delete(cod):
    """Procesa la eliminación de una serie."""

    form = DeleteContentForm(request.POST)

    if form.delete.data:
        series = Series(DATA_BASE)
        img_path = series.get(['Portada'], {'Cod_Serie': cod})[0]
        remove(img_path)

        series.delete({'Cod_Serie': cod})
        redirect('/admin/series')

    if form.cancel.data:
        redirect('/admin/series')


@get('/series')
@login_required
def home_series():
    """Página de inicio de Series"""

    user = local_storage.getItem("profile")
    fields = [
        "Cod_Serie AS 'Cod_Contenido'",
        "Titulo",
        "Genero",
        "N_Temporada",
        "Portada",
        "Trailer",
        "Director",
        "Productor",
        "Sinopsis",
        "Capitulos",
        "Puntuacion_Media",
        "0 AS 'Duracion'"
    ]

    personal_profile = Profile(DATA_BASE)
    series = Series(DATA_BASE)
    favorites = Favorites(DATA_BASE)

    # Top Contenido para el Slider
    top_carrousel = series.top_content(fields, 4)

    # Favoritos del Perfil
    cod_perfil = personal_profile.select(
        ["Cod_Favoritos"], {"Cod_Perfil": user})[0][0]
    avatar_perfil = personal_profile.select(
        ["Imagen"], {"Cod_Perfil": user})[0][0]
    profile_favorites = favorites.content(cod_perfil, [
                                            "Portada", "Trailer", "Titulo", "Genero", "N_Temporada", "Cod_Serie"], [])

    # Top 10 Contenido
    top_ten = series.top_content(fields, 10)

    # Contenido por Genero
    content_by_genre = {
        genre: series.select(fields, {"Genero": genre})
        for genre in GENRES_FIELDS
    }

    local_storage.setItem("path", "series")

    return template(
        'home',
        title="Geeks Hub - Series",
        slider=top_carrousel,
        favorites=profile_favorites,
        top_ten=top_ten,
        all_content=content_by_genre,
        avatar=avatar_perfil
    )
