"""Archivo de Rutas de las Cuentas."""
import sys
from bottle import route, run, template, request, get, post, redirect, static_file, error
from models.account import Account
from forms.register_form import RegistrationForm
from config.config import DATA_BASE
sys.path.append('models')

@get('/admin/accounts')
def admin_accounts():
    """Página de inicio de las Cuentas para Administradores."""
    cuenta = Account(DATA_BASE)
    rows = cuenta.select(["*"])

    return template('admin_accounts', rows=rows)

@get('/accounts')
def account_index():
    """Página de inicio de las Cuentas."""
    cuentas = Account(DATA_BASE)
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
    