"""Archivo de Rutas de las Cuentas."""
import sys
from localStoragePy import localStoragePy
from bottle import get, request, template, redirect, post
from models.account import Account
from forms.register_form import RegistrationForm
from forms.login_form import LoginForm
from config.config import DATA_BASE, ACCOUNT_FIELDS
sys.path.append('models')
sys.path.append('forms')

@get('/admin/accounts')
def admin_accounts():
    """Página de inicio de las Cuentas para Administradores."""
    cuenta = Account(DATA_BASE)
    rows = cuenta.select(list(ACCOUNT_FIELDS))

    return template('admin_accounts', rows=rows, fields=ACCOUNT_FIELDS)

@get('/admin/accounts/<email>')
def admin_accounts_view(email):
    """Página de visualización de una Cuenta para Administradores."""
    cuenta = Account(DATA_BASE)
    rows = cuenta.select(['*'], {'Correo': email})

    return template('admin_view_account', rows=rows)

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
        
        account.insert(form_data)
        redirect('/profiles')
        
    return template('register', form=form)

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

            with open("./static/file/login.txt", "w", encoding="UTF8") as fichero:
                fichero.write(form.email.data)

            redirect('/select_profiles')

    if error:

        return template('login', form=form)

    return None
