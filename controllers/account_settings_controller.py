"""Archivo de Rutas de la Configuración de Cuentas."""
import sys
from bottle import get, request, template, redirect, post
from models.account import Account
from models.profile import Profile
from forms.account_settings_form import AccountSettingsForm
from forms.profile_form import ProfileForm
from utils.hash_password import hash_password
from config.config import DATA_BASE, ACCOUNT_FIELDS, AVATARS
from config.local_storage import local_storage
sys.path.append('models')
sys.path.append('forms')

@get('/account_settings')
def account_settings():
    """Página de inicio de Configuración de Cuentas"""

    email = local_storage.getItem("email")
    profile_code = local_storage.getItem("profile")

    if profile_code:
        form = AccountSettingsForm(request.POST)
        account = Account(DATA_BASE)
        profile = Profile(DATA_BASE)
        personal_profile = profile.select(['Imagen'], {'Cod_Perfil': profile_code})

        rows = account.select(['*'], {'Correo': email})
        rows_profile = profile.select(['*'], {'Correo': email})

        form.name.data = rows[0][1]
        form.surname.data = rows[0][2]
        form.direction.data = rows[0][3]
        form.phone_number.data = rows[0][5]
        form.suscription.data = rows[0][6]

        return template('account_settings', 
                        title= "Geeks Hub - Cuenta",
                        rows=rows, 
                        rows_profile=rows_profile, 
                        form=form, 
                        fields=ACCOUNT_FIELDS, 
                        avatar=personal_profile[0][0]
                        )

@post('/account_settings')
def account_settings_process():
    """Procesa el formulario de Configuración de Cuentas"""

    form = AccountSettingsForm(request.POST)
    account = Account(DATA_BASE)

    if form.submit.data and form.validate():
        form_data_account = {}

        if form.name.data:
            form_data_account["Nombre"] = form.name.data
        if form.surname.data:
            form_data_account["Apellidos"] = form.surname.data
        if form.direction.data:
            form_data_account["Direccion"] = form.direction.data
        if form.password.data and form.password.data == form.password_confirm.data:
            form_data_account["Contrasena"] = hash_password(form.password.data)
        if form.phone_number.data:
            form_data_account["Telefono"] = form.phone_number.data
        if form.suscription.data and form.suscription.data != '0':
            form_data_account["Tipo_Suscripcion"] = form.suscription.data
        
        account.update(form_data_account, {'Correo': local_storage.getItem("email")})
        redirect('/account_settings')

    account = Account(DATA_BASE)
    profile = Profile(DATA_BASE)
    email = local_storage.getItem("email")
    profile_code = local_storage.getItem("profile")
    personal_profile = profile.select(['Imagen'], {'Cod_Perfil': profile_code})

    rows = account.select(['*'], {'Correo': email})
    rows_profile = profile.select(['*'], {'Correo': email})
    
    return template('account_settings',
                    title= "Geeks Hub - Cuenta", 
                    rows=rows, 
                    rows_profile=rows_profile, 
                    form=form, 
                    fields=ACCOUNT_FIELDS, 
                    avatar=personal_profile[0][0]
                    )
    
@get('/account_settings/profile')
def account_settings_profile():
    """Página de inicio de Configuración de Perfil"""

    if request.GET.get("btn_continue") and request.GET.get("profile_code"):
        form = form = ProfileForm(request.GET) 
        profile = Profile(DATA_BASE)
        
        codigo_perfil = request.GET.get("profile_code")
        rows_profile = profile.select(['*'], {'Cod_Perfil': codigo_perfil})
        form.nickname.data = rows_profile[0][2]
        personal_profile = profile.select(['Imagen'], {'Cod_Perfil': local_storage.getItem("profile")})

        return template(
                        'profile_settings', 
                        rows=AVATARS, 
                        title= "Geeks Hub - Perfil",
                        rows_profile=rows_profile, 
                        form=form, 
                        profile_code=codigo_perfil,
                        avatar=personal_profile[0][0]
                        )
    redirect('/account_settings')

@post('/account_settings/profile')
def account_settings_profile_process():
    """Procesa el formulario de Configuración de Perfil"""

    form = ProfileForm(request.POST)
    profile = Profile(DATA_BASE)

    if form.btn_continue.data and form.validate():
        
        form_data = {}
        if form.nickname.data:
            form_data["Nickname"] = form.nickname.data
        if request.POST.get("avatar"):
            form_data["Imagen"] = request.POST.get("avatar")

        codigo_perfil = request.POST.get("profile_code")
        
        profile.update(form_data, {'Cod_Perfil': codigo_perfil})
        redirect('/account_settings')
