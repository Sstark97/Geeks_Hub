"""Archivo de Rutas del Formulario de Registro."""
import sys
from bottle import route, run, template, request, get, post, redirect, static_file, error
from config.config import DATA_BASE
from forms.register_form import RegistrationForm
from models.account import Account
sys.path.append('forms')

@get('/register')
def register():
    """Pagina de inicio de Registro"""
    form = RegistrationForm(request.POST)
    return template('register', form=form)

@post('/register')
def register_process():
    """Procesa el formulario de Registro de Cuentas"""
    form = RegistrationForm(request.POST)
    account = Account(DATA_BASE)
    if form.register.data and form.validate():

        form_data = {
            "Correo" : form.email.data,
            "Nombre" : form.name.data,
            "Apellidos" : form.surname.data,
            "Direccion" : form.direction.data,
            "Contrasena" : form.password.data,
            "Telefono" : form.phone_number.data,
            "Tipo_Suscripcion" : form.suscription.data
        }
        # print(form_data)
        account.insert(form_data)
        redirect('/accounts')
    if form.cancel:
        redirect('/')
    return template('register', form=form)