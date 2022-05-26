"""Fichero para la creación del formulario de inicio"""
from email_validator import EmailNotValidError
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField , validators

class LoginForm(Form):
    """Clase para la realización del formulario de inicio"""
    email = StringField('Email Address', [validators.InputRequired(), validators.Length(min=6, max=60), validators.Email()])
    accept_rules = BooleanField('Acepto las reglas del sitio', [validators.InputRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('password_confirm', 
                        message='Las contraseñas no coinciden')
        ])
    btn_continue = SubmitField('Continuar')
    cancel = SubmitField('Cancelar')
