"""Fichero para el Formulario de Registro"""
from wtforms import Form, StringField, PasswordField, SubmitField, validators


class RegistrationForm(Form):
    """Clase que maneja el formulario de Registro"""

    name = StringField(
        'Nombre', [validators.InputRequired(), validators.Length(min=1, max=20)])
    surname = StringField(
        'Apellidos', [validators.InputRequired(), validators.Length(min=1, max=30)])
    email = StringField('Correo electrónico', [validators.InputRequired(), validators.Length(min=6, max=60),
                                               validators.Email(message="Debe introducir un email válido")])

    password = PasswordField('Contraseña', [
        validators.Length(min=1, max=20),
        validators.DataRequired(),
        validators.EqualTo('password_confirm',
                           message='Las contraseñas no coinciden')
    ])
    password_confirm = PasswordField('Repita la contraseña')
    direction = StringField(
        'Dirección', [validators.InputRequired(), validators.Length(min=1, max=70)])
    phone_number = StringField('Teléfono', [validators.InputRequired(), validators.Length(min=9, max=9,
                                                message="Debe introducir un número de 9 dígitos"),
                                                validators.regexp('[0-9]+', message="El número debe contener solo digitos")]) 

    register = SubmitField('Registrar')
