"""Archivo de rutas de las Búsquedas"""
from bottle import get, template
from models.film import Film
from models.profile import Profile
from config.config import DATA_BASE
from config.local_storage import local_storage
from utils.login_decorator import login_required

@get('/search')
@login_required
def search_content():
    """Página de inicio de la Búsqueda de Contenido"""

    user = local_storage.getItem("profile")
    local_storage.setItem("path", "search")

    profile = Profile(DATA_BASE)
    avatar_perfil = profile.select(["Imagen"],{"Cod_Perfil":user})[0][0]
    films = Film(DATA_BASE)
    rows_content = films.union_content()

    return template(
                    'list_content', 
                    title= "Geeks Hub - Buscador",
                    rows_content=rows_content, 
                    search=True, 
                    avatar=avatar_perfil
                    )
