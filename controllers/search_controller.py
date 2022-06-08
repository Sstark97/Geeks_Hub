"""Archivo de rutas de las Búsquedas"""
from bottle import get, template, redirect
from models.film import Film
from models.profile import Profile
from config.config import DATA_BASE
from config.local_storage import local_storage

@get('/search')
def search_content():
    """Página de inicio de la Búsqueda de Contenido"""

    user = local_storage.getItem("profile")
    local_storage.setItem("path", "search")

    if user:
        profile = Profile(DATA_BASE)
        avatar_perfil = profile.select(["Imagen"],{"Cod_Perfil":user})[0][0]
        films = Film(DATA_BASE)
        rows_content = films.union_content()
    
    else:
        redirect('/')

    return template('list_content', rows_content=rows_content, search=True, avatar=avatar_perfil)
