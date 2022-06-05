"""Archivo de Rutas de la Configuración de Cuentas."""
import sys
from bottle import get, request, template, redirect, post
from models.account import Account
from models.profile import Profile
from forms.account_settings_form import AccountSettingsForm
from config.config import DATA_BASE, ACCOUNT_FIELDS
from config.local_storage import local_storage
sys.path.append('models')
sys.path.append('forms')

@get('/account_settings')
def account_settings():
    """Página de inicio de Configuración de Cuentas"""
    print(local_storage.getItem("email"))
    print(local_storage.getItem("profile"))
    form = AccountSettingsForm(request.POST)
    account = Account(DATA_BASE)
    profile = Profile(DATA_BASE)
    rows = account.select(['*'], {'Correo': local_storage.getItem("email")})
    rows_profile = profile.select(['*'], {'Correo': local_storage.getItem("email")})

    form.name.data = rows[0][1]
    form.surname.data = rows[0][2]
    form.direction.data = rows[0][3]
    form.phone_number.data = rows[0][5]
    form.suscription.data = rows[0][6]

    return template('account_settings', rows=rows, rows_profile=rows_profile, form=form, fields=ACCOUNT_FIELDS)

@post('/account_settings')
def account_settings_process():
    """Procesa el formulario de Configuración de Cuentas"""
    form = AccountSettingsForm(request.POST)
    account = Account(DATA_BASE)
    profile = Profile(DATA_BASE)

    if form.submit.data:
        form_data_account = {}

        if form.name.data:
            form_data_account["Nombre"] = form.name.data
        if form.surname.data:
            form_data_account["Apellidos"] = form.surname.data
        if form.direction.data:
            form_data_account["Direccion"] = form.direction.data
        if form.password.data and form.password.data == form.password_confirm.data:
            form_data_account["Contrasena"] = form.password.data
        if form.phone_number.data:
            form_data_account["Telefono"] = form.phone_number.data
        if form.suscription.data and form.suscription.data != '0':
            form_data_account["Tipo_Suscripcion"] = form.suscription.data
        
        # form_data_profile = {
        #     "Nickname" : request.forms.get('nickname'),
        #     "Imagen" : request.forms.get('avatar')
        # }
        print(form_data_account)
        account.update(form_data_account, {'Correo': local_storage.getItem("email")})
        # profile.update(form_data_profile, {'Correo': local_storage.getItem("email")})
        redirect('/account_settings')
    