"""Fichero para la creación del formulario de inicio"""
from atexit import register
from email_validator import EmailNotValidError
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField , validators

class LoginForm(Form):
    """Clase para la realización del formulario de inicio"""
    email = StringField('Email Address', [validators.InputRequired(), validators.Length(min=6, max=60), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired()])
    btn_continue = SubmitField('Continuar')
