"""Archivo de Rutas de las Cuentas."""
import sys
from random import randint
from bottle import get, request, template, redirect, post, auth_basic
from utils.admin_auth import is_authenticated_user
from utils.email_register import send_register_email, send_change_password
from utils.hash_password import hash_password, check_password
from models.account import Account
from models.suscription import Suscription
from forms.register_form import RegistrationForm
from forms.confirm_password_form import ConfirmForm
from forms.login_form import LoginForm
from forms.rememberme_form import RemembermeForm
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

    print(request.POST.get('new_suscription'))
    
    if request.POST.get('new_suscription') == None:
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
        return template('login', form=form, title="Inicia Sesión", path="/login", action="/select_profile",message="")
    
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
        return template('login', form=form, title="Inicia Sesión", path="/login", action="/select_profile",message="")

    return None

@get('/change_password')
def change_password():
    """Página para cambiar la contraseña"""

    user = local_storage.getItem("profile")
    if not user:
            
        form = RemembermeForm(request.POST)
        return template('login', form=form, title="Introduce el Correo", path="/change_password", action="/change_password",message="")

    redirect("/home")
    return None

@post('/change_password')
def change_password_process():
    """Página para procesar el formulario"""

    form = RemembermeForm(request.POST) 

    if form.btn_continue.data and form.validate():
        local_storage.setItem("email", form.email.data)
        code = randint(1000, 9999)
        
        local_storage.setItem("code", code)

        send_change_password(form.email.data, code)

        return template('login', form=form, title="Introduce el Correo", path="/change_password", action="/change_password",
        message="Revisa el Correo")
    
    return template('login', form=form, title="Introduce el Correo", path="/change_password", action="/change_password", message="")

@get('/change_password_process')
def change_password_confirm():
    """ Página para procesar el cambio de contraseña """
    
    user = local_storage.getItem("profile")
    if not user:
        form = ConfirmForm(request.POST)
        return template('confirm_change_password', form=form)

    redirect("/home")
    return None


@post('/logout')
def logout():
    """Página para cerrar la sesión"""
    
    local_storage.clear()
