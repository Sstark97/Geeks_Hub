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

    if form.btn_continue.data and request.POST.get("avatar") and form.validate():
        form_data = {
            'nickname' : form.nickname.data,
            'imagen' : request.POST.get("avatar")
        }

        print(form_data)
        redirect("/")

    print(form.errors)
    return template('profile', form=form)
