"""Archivo de Rutas de las Cuentas."""
import sys
from bottle import get, request, template, redirect, post, auth_basic
from utils.admin_auth import is_authenticated_user
from utils.email_register import send_register_email
from utils.hash_password import hash_password, check_password
from models.account import Account
from models.suscription import Suscription
from forms.register_form import RegistrationForm
from forms.login_form import LoginForm
from config.config import DATA_BASE, ACCOUNT_FIELDS
from config.local_storage import local_storage
sys.path.append('models')
sys.path.append('forms')

@get('/admin/accounts')
@auth_basic(is_authenticated_user)
def admin_accounts():
    """Página de inicio de las Cuentas para Administradores."""

    cuenta = Account(DATA_BASE)
    rows = cuenta.select(list(ACCOUNT_FIELDS))

    return template('admin_accounts', rows=rows, fields=ACCOUNT_FIELDS)

@get('/admin/accounts/<email>')
@auth_basic(is_authenticated_user)
def admin_accounts_view(email):
    """Página de visualización de una Cuenta para Administradores."""

    cuenta = Account(DATA_BASE)
    rows = cuenta.select(['*'], {'Correo': email})
    profiles = cuenta.n_profiles(['Cod_Perfil'], {'Correo': email})[0][0]

    return template(
                    'admin_view_account', 
                    rows=rows, 
                    num_profiles=profiles, 
                    content_type="accounts", 
                    class_content="cuenta"
                    )

@get('/register')
def register():
    """Pagina de inicio de Registro"""

    user = local_storage.getItem("profile")
    if not user:

        form = RegistrationForm(request.POST)
        suscriptions_data = Suscription(DATA_BASE)
        suscriptions = suscriptions_data.select(["*"])

        return template('register', form=form, error="", rows=suscriptions)
    redirect("/home")
    return None

@post('/register')
def register_process():
    """Procesa el formulario de Registro de Cuentas"""
    form = RegistrationForm(request.POST)
    account = Account(DATA_BASE)
    error=""
    
    if request.POST.get('new_suscription') != "":
        error = "Seleccione una Suscripción"
    elif form.register.data and form.validate() and error == "":
        password = hash_password(form.password.data)

        form_data = {
            "Correo" : form.email.data,
            "Nombre" : form.name.data,
            "Apellidos" : form.surname.data,
            "Direccion" : form.direction.data,
            "Contrasena" : password,
            "Telefono" : form.phone_number.data,
            "Tipo_Suscripcion" : request.POST.get("new_suscription")
        }
        
        account.insert(form_data)
        local_storage.setItem("email",form.email.data)
        send_register_email(form.email.data)
        redirect('/profiles')

    suscriptions_data = Suscription(DATA_BASE)
    suscriptions = suscriptions_data.select(["*"])
        
    return template('register', rows=suscriptions, error=error, form=form)

@get('/login')
def login():
    """Página para mostrar el formulario"""

    user = local_storage.getItem("profile")
    if not user:

        form = LoginForm(request.POST)
        return template('login', form=form)
    
    redirect("/home")
    return None

@post('/login')
def login_process():
    """Página para procesar el formulario"""

    form = LoginForm(request.POST) 
    account = Account(DATA_BASE)
    error = True

    local_storage.setItem("email", form.email.data)

    if form.btn_continue.data and form.validate():
        password = account.select(["Contrasena"], {"Correo": form.email.data})

        if check_password(form.password.data, password[0][0]):
            error = False
            redirect('/select_profile')

    if error:
        return template('login', form=form)

    return None

@post('/logout')
def logout():
    """Página para cerrar la sesión"""
    
    local_storage.clear()
