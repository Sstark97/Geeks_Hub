"""Archivo de Rutas de las Cuentas."""
import sys
from bottle import get, request, template, redirect, post
from models.account import Account
from config.config import DATA_BASE
from forms.login_form import LoginForm
sys.path.append('models')
sys.path.append('forms')

@get('/accounts')
def account_index():
    """Página de inicio de las Cuentas."""
    cuentas = Account(DATA_BASE)

    # Añadir
    # cuenta.insert({"Correo" : "miriamdaw@gmail.com", "Nombre" : 
    # "Miriam", "Apellidos" : "Garcia Rodriguez", "Direccion" : "C/ Lomo Apolinario", "Contrasena" : "miri135am", "Telefono" : "647893746", "Tipo_Suscripcion" : "Estandar"})
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

@get('/login')
def login():
    """Página para mostrar el formulario"""
    form = LoginForm(request.POST)
    return template('login', form=form)

@post('/login')
def login_process():
    """Página para procesar el formulario"""
    form = LoginForm(request.POST) 
    account = Account(DATA_BASE)
    error = True

    if form.btn_continue.data and form.validate():
        password = account.select(["Contrasena"], {"Correo": form.email.data})

        if password[0][0] == form.password.data:
            error = False

            form_data = {
                'email' : form.email.data,
                'password' : form.password.data,
            }
            with open("./static/file/login.txt", "w", encoding="UTF8") as fichero:
                fichero.write(form.email.data)

            redirect('/')

    if error:

        print(form.errors)
        return template('login', form=form)

    return None
        
