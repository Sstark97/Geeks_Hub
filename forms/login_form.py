"""Fichero para la creación del formulario de inicio"""
from wtforms import Form, StringField, PasswordField, SubmitField , validators

class LoginForm(Form):
    """Clase para la realización del formulario de inicio"""
    email = StringField('Correo', [validators.InputRequired(), validators.Length(min=6, max=60), validators.Email()])
    password = PasswordField('Contraseña', [
        validators.DataRequired()])
    btn_continue = SubmitField('Continuar')
