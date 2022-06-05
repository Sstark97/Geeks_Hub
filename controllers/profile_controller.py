"""Archivo de Rutas de los Perfiles."""
import sys
from datetime import date
from bottle import get, request, template, redirect, post
from models.profile import Profile
from models.favorites import Favorites
from config.config import DATA_BASE, AVATARS
from config.local_storage import local_storage
from forms.profile_form import ProfileForm
sys.path.append('models')
sys.path.append('forms')

@get('/profiles')
def profile():
    """Página para mostrar el formulario"""
    form = ProfileForm(request.POST)
    return template('profile', rows=AVATARS, form=form)

@post('/profiles')
def profile_process():
    """Página para procesar el formulario"""
    form = ProfileForm(request.POST) 
    personal_profile = Profile(DATA_BASE)
    favorites = Favorites(DATA_BASE)

    correo = local_storage.getItem("email")

    if form.btn_continue.data and request.POST.get("avatar") != None and form.validate():
        today = date.today()
        favorites.insert({"Fecha_Creacion": today.strftime("%Y-%m-%d")})
        cod_favorites = favorites.select(["Cod_Favoritos"])[-1][0]

        form_data = {
            'Cod_Perfil' : personal_profile.code_generator("PR", "Cod_Perfil"),
            'Correo' : correo,
            'Nickname' : form.nickname.data,
            'Imagen' : request.POST.get("avatar"),
            "Cod_Favoritos" : cod_favorites
        }

        personal_profile.insert(form_data)
        redirect("/select_profile")

    return template('profile', rows=AVATARS, form=form)

@get('/select_profile')
def select_profile():
    """Página para mostrar la selección de perfiles"""

    correo = local_storage.getItem("email")

    personal_profile = Profile(DATA_BASE)
    rows = personal_profile.select(['*'], {'Correo': correo})
    form = ProfileForm(request.POST) 
    return template('select_profiles', rows=rows, form=form)

@post('/select_profile')
def select_profile_process():
    """Página para procesar la selección de perfiles"""
    correo = local_storage.getItem("email")
    personal_profile = Profile(DATA_BASE)
    rows = personal_profile.select(['*'], {'Correo': correo})
    form = ProfileForm(request.POST) 

    if request.POST.get("profile_code"):
        codigo = request.POST.get("profile_code")
        print("HOLA")
        print(codigo)
        
        local_storage.setItem("profile",codigo)

        redirect('/home')
    
    return template('select_profiles', rows=rows, form=form)
