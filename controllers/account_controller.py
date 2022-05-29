"""Archivo de Rutas de las Cuentas."""
import sys
from bottle import route, run, template, request, get, post, redirect, static_file, error
from models.account import Account
from forms.register_form import RegistrationForm
from config.config import DATA_BASE
sys.path.append('models')

@get('/accounts')
def account_index():
    """Página de inicio de las Cuentas."""
    cuentas = Account(DATA_BASE)

    # Añadir
    # cuenta.insert({"Correo" : "miriamdaw@gmail.com", "Nombre" : "Miriam", "Apellidos" : "Garcia Rodriguez", "Direccion" : 
    # "C/ Lomo Apolinario", "Contrasena" : "miri135am", "Telefono" : "647893746", "Tipo_Suscripcion" : "Estandar"})
    # row = cuenta.select(["*"], {"Nombre" : "Miriam"})

    # Actualizar
    # cuentas.update({"Correo" : "miriamcorreo@gmail.com"}, {"Nombre" : "Miriam"})

    # Eliminar
    # cuentas.delete({"Nombre" : "Miriam"})
    
    # Select Direccion Avenida (A/)
    # row = cuentas.select(['*'],  {"Direccion": "A/%"})

    # Select de todas las Cuentas
    row = cuentas.select(['*'])
    return str(row)

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
        
    return template('register', form=form)
    