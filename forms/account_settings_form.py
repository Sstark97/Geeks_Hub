"""Formulario para la Configuración de la Cuenta"""
from email_validator import EmailNotValidError
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField , validators, DateField, SelectField

class AccountSettingsForm(Form):
    """Clase que maneja el formulario de Configuración de Cuentas"""
    name = StringField('Nombre', [
                                    validators.Length(min=1, max=20),
                                ])
    surname = StringField('Apellidos', [
                                    validators.Length(min=1, max=30),
                                ])
    direction = StringField('Dirección', [
                                    validators.Length(min=1, max=30),
                                ])
    password = PasswordField('Contraseña', [
                                    validators.Length(min=1, max=20),
                                ])
    phone_number = StringField('Teléfono', [
                                    validators.Length(min=9, max=9),
                                ])
    suscription = SelectField('Tipo de Suscripción', choices=[('Basico', 'Basico'), ('Estandar', 'Estandar'), ('Premium', 'Premium')])
    submit = SubmitField('Guardar')
    logout = SubmitField('Cerrar Sesión')
