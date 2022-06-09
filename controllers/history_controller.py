"""Archivo de Rutas de los Historiales."""
import sys
from bottle import get, template, redirect
from models.history import History
from models.profile import Profile
from config.config import DATA_BASE
from config.local_storage import local_storage
sys.path.append('models')


@get('/history')
def history_index():
    """Página de inicio de los Historiales."""
    user = local_storage.getItem("profile")

    if user:
        personal_profile = Profile(DATA_BASE)
        history = History(DATA_BASE)

        local_storage.setItem("path", "history")

        # Historial del Perfil
        avatar_perfil = personal_profile.select(
            ["Imagen"],
            {"Cod_Perfil": user}
        )[0][0]
        profile_history = history.content(
            user,
            ["Portada", "Trailer", "Titulo", "Genero", "Cod_Serie", "N_Temporada"],
            ["Portada", "Trailer", "Titulo", "Genero", "Cod_Pelicula"]
        )

    else:
        redirect('/')

    return template(
        'list_content',
        rows_content=profile_history,
        search=False,
        title="Geeks Hub - Historial",
        head="Historial",
        avatar=avatar_perfil
    )
