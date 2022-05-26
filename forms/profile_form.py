"""Fichero para la creación de un nuevo perfil"""
from atexit import register
from email_validator import EmailNotValidError
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField , validators

class ProfileForm(Form):
    """Clase para la realización del formulario de creación de perfil"""
    nickname = StringField('Nickname', [validators.InputRequired(), validators.Length(min=6, max=20)])
    # image = ¿?
    btn_continue = SubmitField('Continuar')
    cancel = SubmitField('Cancelar')
