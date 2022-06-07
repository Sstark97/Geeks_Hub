"""Archivo de Rutas de la lista de Favoritos."""
import sys
from bottle import get, template, redirect
from models.favorites import Favorites
from models.profile import Profile
from config.config import DATA_BASE
from config.local_storage import local_storage
sys.path.append('models')

@get('/favorites')
def favorites_index():
    """Página de inicio de la lista de Favoritos."""
    user = local_storage.getItem("profile")

    if user:
        personal_profile = Profile(DATA_BASE)
        favorites = Favorites(DATA_BASE)

        local_storage.setItem("path", "favorites")

        # Favoritos del Perfil
        cod_perfil = personal_profile.select(["Cod_Favoritos"],{"Cod_Perfil":user})[0][0]
        avatar_perfil = personal_profile.select(["Imagen"],{"Cod_Perfil":user})[0][0]
        profile_favorites = favorites.content(cod_perfil, ["Portada", "Trailer", "Titulo", "Genero","Cod_Serie", "N_Temporada"], 
            ["Portada", "Trailer", "Titulo", "Genero","Cod_Pelicula"])

    else: 
        redirect('/')

    return template('list_content', rows_content=profile_favorites, search=False, title="Lista de Favoritos", avatar=avatar_perfil)
    