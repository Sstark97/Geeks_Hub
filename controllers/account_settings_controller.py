"""Archivo de Rutas de la Configuración de Cuentas."""
import sys
from bottle import get, request, template, redirect, post
from models.account import Account
from models.profile import Profile
from config.config import DATA_BASE, ACCOUNT, PROFILE
from config.local_storage import local_storage
sys.path.append('models')
# sys.path.append('forms')

@get('/account_settings')
def account_settings():
    """Página de inicio de Configuración de Cuentas"""
    account = Account(DATA_BASE)
    profile = Profile(DATA_BASE)
    rows = account.select(['*'], {'Correo': local_storage.getItem("email")})
    rows_profile = profile.select(['*'], {'Correo': local_storage.getItem("email")})
    return template('account_settings', rows=rows, rows_profile=rows_profile)

@post('/account_settings')
def account_settings_process():
    """Procesa el formulario de Configuración de Cuentas"""
    account = Account(DATA_BASE)
    profile = Profile(DATA_BASE)

    form_data_account = {
        "Correo" : request.forms.get('email'),
        "Nombre" : request.forms.get('name'),
        "Apellidos" : request.forms.get('surname'),
        "Direccion" : request.forms.get('direction'),
        "Contrasena" : request.forms.get('password'),
        "Telefono" : request.forms.get('phone_number'),
        "Tipo_Suscripcion" : request.forms.get('suscription')
    }

    form_data_profile = {
        "Nickname" : request.forms.get('nickname'),
        "Imagen" : request.forms.get('avatar')
    }

    account.update(form_data_account, {'Correo': local_storage.getItem("email")})
    profile.update(form_data_profile, {'Correo': local_storage.getItem("email")})
    redirect('/account_settings')