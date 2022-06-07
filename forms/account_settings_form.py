"""Formulario para la Configuración de la Cuenta"""
from wtforms import Form, StringField, PasswordField, SubmitField , validators, SelectField

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
                                    validators.Length(min=1, max=20),
                                    validators.EqualTo('password_confirm', 
                                    message='Las contraseñas no coinciden')
                                ])
    password_confirm = PasswordField('Repita la contraseña')
    phone_number = StringField('Teléfono', [
                                    validators.Length(min=9, max=9),
                                ])
    suscription = SelectField('Tipo de Suscripción', choices=[('Basico', 'Basico'), ('Estandar', 'Estandar'), ('Premium', 'Premium')])
    submit = SubmitField('Guardar', render_kw={'id':'form-submit'})
