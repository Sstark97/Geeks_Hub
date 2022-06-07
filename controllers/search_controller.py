"""Archivo de rutas de las Búsquedas"""
from bottle import get, request, template, redirect, post, auth_basic
from models.film import Film
from models.profile import Profile
from config.config import DATA_BASE
from config.local_storage import local_storage

@get('/search')
def search_content():
    """Página de inicio de la Búsqueda de Contenido"""

    user = local_storage.getItem("profile")

    if user:
        profile = Profile(DATA_BASE)
        avatar_perfil = profile.select(["Imagen"],{"Cod_Perfil":user})[0][0]

    films = Film(DATA_BASE)
    rows_content = films.union_content()

    

    return template('search_content', rows_content=rows_content, avatar=avatar_perfil)
