"""Formulario para la Configuración de la Cuenta"""
from wtforms import Form, StringField, PasswordField, SubmitField , validators, SelectField
from config.config import SUSCRIPTIONS

class AccountSettingsForm(Form):
    """Clase que maneja el formulario de Configuración de Cuentas"""
    name = StringField('Nombre', [
                                    validators.Length(min=1, max=20),
                                ])
    surname = StringField('Apellidos', [
                                    validators.Length(min=1, max=30)
                                ])
    direction = StringField('Dirección', [
                                    validators.Length(min=1, max=30)
                                ])
    password = PasswordField('Contraseña', [
                                    validators.Length(max=20),
                                    validators.EqualTo('password_confirm', 
                                    message='Las contraseñas no coinciden')
                                ])
    password_confirm = PasswordField('Repita la contraseña', [validators.Length(max=20)])

    phone_number = StringField('Teléfono', [validators.Length(min=9, max=9,
                                                message="Debe introducir un número de 9 dígitos"),
                                                validators.regexp('[0-9]+', message="El número debe contener solo digitos")])
    
    suscription = SelectField('Tipo de Suscripción', choices=SUSCRIPTIONS)
    submit = SubmitField('Guardar', render_kw={'id':'form-submit'})
