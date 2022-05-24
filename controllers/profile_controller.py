"""Archivo de Rutas de los Perfiles."""
import sys
from bottle import get
from models.profile import Profile
from config.config import DATA_BASE
sys.path.append('models')

@get('/profiles')
def profiles_index():
    """Página de inicio de los Perfiles."""
    perfiles = Profile(DATA_BASE)

    # Añadir
    # perfiles.insert({"Cod_Perfil" : "Perfil14", "Correo" : "javimartel@hotmail.com", "Nickname" : "Javi3", "Imagen" : "Imagen3", "Cod_Favoritos" : "FV14"})
    # row = perfiles.select(["*"], {"Correo" : "javimartel@hotmail.com"})

    # Actualizar
    # perfiles.update({"Nickname" : "Miguel"}, {"Nickname" : "Javi3"})

    # Eliminar
    # perfiles.delete({"Cod_Perfil" : "Perfil14"})
    
    # Select Correo Hotmail
    # row = perfiles.select(['*'],  {"Correo": "%@hotmail%"})

    # Select de todos los perfiles
    row = perfiles.select(['*'])

    return str(row)