"""Fichero para la creación del formulario de inicio"""
from wtforms import Form, StringField, SubmitField , validators
from config.config import DATA_BASE
from models.account import Account

class RemembermeForm(Form):
    """Clase para la realización de Recuperar Contraseña"""
    email = StringField('Correo', [validators.InputRequired(), validators.Length(min=6, max=60), validators.Email()])

    def validate_email(self, email):
        """Función para validar el email"""
        account = Account(DATA_BASE)
        emails = account.select(["Correo"], {"Correo": email.data})

        if len(emails) == 0:
            raise validators.ValidationError('El email no existe')

    btn_continue = SubmitField('Continuar')
