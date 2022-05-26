"""Archivo de Rutas del Formulario de Registro."""
import sys
from bottle import route, run, template, request, get, post, redirect, static_file, error
from forms.register_form import RegistrationForm
sys.path.append('forms')

@get('/register')
def register():
    form = RegistrationForm(request.POST)
    return template('register', form=form)