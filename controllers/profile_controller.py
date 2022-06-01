"""Archivo de Rutas de los Perfiles."""
import sys
from bottle import get, request, template, redirect, post
from models.profile import Profile
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
    profile = Profile(DATA_BASE)

    with open("./static/file/login.txt", "r", encoding="UTF8") as fichero:
        correo = fichero.readline()

    print(request.POST.get("avatar"))

    if form.btn_continue.data and request.POST.get("avatar") != None and form.validate():
        form_data = {
            'cod_perfil' : profile.code_generator(),
            'correo' : correo,
            'nickname' : form.nickname.data,
            'imagen' : request.POST.get("avatar")
        }

        profile.insert(form_data)
        redirect("/")


    print(form.errors)
    return template('profile', rows=AVATARS, form=form)

@get('/select_profile')
def select_profile():
    """Página para mostrar la selección de perfiles"""

    with open("./static/file/login.txt", "r", encoding="UTF8") as fichero:
        correo = fichero.readline()

    profile = Profile(DATA_BASE)
    rows = profile.select(['*'], {'Correo': correo})

    return template('select_profiles', rows=rows)

@post('/select_profile')
def select_profile_process():
    """Página para procesar la selección de perfiles"""

    redirect('/profiles')
