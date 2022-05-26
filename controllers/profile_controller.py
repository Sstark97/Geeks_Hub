"""Archivo de Rutas de los Perfiles."""
import sys
from bottle import get, request, template, redirect, post
from models.profile import Profile
from config.config import DATA_BASE
from forms.profile_form import ProfileForm
sys.path.append('models')
sys.path.append('forms')

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

@get('/profiles')
def profile():
    """Página para mostrar el formulario"""
    form = ProfileForm(request.POST)
    return template('profile', form=form)

@post('/profiles')
def profile_process():
    """Página para procesar el formulario"""
    form = ProfileForm(request.POST) 
    profile = Profile(DATA_BASE)

    if form.save.data and form.validate():
        form_data = {
            'nickname' : form.nickname.data,
            'imagen' : form.imagen.data
        }

        print(form_data)
        redirect("/")

    print(form.errors)
    return template('profile', form=form)
