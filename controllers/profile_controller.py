"""Archivo de Rutas de los Perfiles."""
import sys
from datetime import date
from bottle import get, request, template, redirect, post
from models.profile import Profile
from models.favorites import Favorites
from config.config import DATA_BASE, AVATARS
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

    with open("./static/file/login.txt", "r", encoding="UTF8") as fichero:
        correo = fichero.readline()

    print(request.POST.get("avatar"))

    if form.btn_continue.data and request.POST.get("avatar") != None and form.validate():
        today = date.today()
        favorites.insert({"Fecha_Creacion": today.strftime("%Y-%m-%d")})
        cod_favorites = favorites.select(["Cod_Favoritos"])[-1][0]

        form_data = {
            'Cod_Perfil' : personal_profile.code_generator(),
            'Correo' : correo,
            'Nickname' : form.nickname.data,
            'Imagen' : request.POST.get("avatar"),
            "Cod_Favoritos" : cod_favorites
        }

        personal_profile.insert(form_data)
        print(form_data)
        redirect("/select_profiles")


    print(form.errors)
    return template('profile', rows=AVATARS, form=form)
