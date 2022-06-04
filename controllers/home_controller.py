"""Archivo de Rutas de la paǵina Home."""
import sys
from bottle import get, template, redirect
from models.profile import Profile
from models.film import Film
from models.favorites import Favorites
# from models.history import History
from config.config import DATA_BASE, GENRES_FIELDS
from config.local_storage import local_storage
sys.path.append('models')

@get('/home')
def home_index():
    """Página de inicio de la App"""

    user = local_storage.getItem("profile")

    if user:
        personal_profile = Profile(DATA_BASE)
        films = Film(DATA_BASE)
        favorites = Favorites(DATA_BASE)

        # Top Contenido para el Slider
        top_carrousel = films.union_content(4)

        # Favoritos del Perfil
        cod_perfil = personal_profile.select(["Cod_Favoritos"],{"Cod_Perfil":user})[0][0]
        print(cod_perfil)
        profile_favorites = favorites.content(cod_perfil, ["Portada", "Trailer", "Titulo", "Genero", "N_Temporada"], ["Portada", "Trailer", "Titulo", "Genero"])

        # Top 10 Contenido
        top_ten = films.union_content(10)

        # Contenido por Genero
        content_by_genre = {}

        for genre in GENRES_FIELDS:
            content = films.union_content(0,{"Genero":genre})
            content_by_genre[genre] = content
        
    else: 
        redirect('/')
    
    return template('home',slider=top_carrousel, favorites=profile_favorites, top_ten=top_ten, all_content=content_by_genre)