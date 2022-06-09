"""Fichero para la creación del formulario de inicio"""
from wtforms import Form, StringField, PasswordField, SubmitField , validators
from config.config import DATA_BASE
from config.local_storage import local_storage
from utils.hash_password import check_password
from models.account import Account

class LoginForm(Form):
    """Clase para la realización del formulario de inicio"""
    email = StringField('Correo', [
                                    validators.InputRequired(), 
                                    validators.Length(min=6, max=60), 
                                    validators.Email(message="El email no es válido")
                                    ])
    password = PasswordField('Contraseña', [
                                            validators.DataRequired()
                                            ])

    def validate_email(self, email):
        """Función para validar el email"""
        account = Account(DATA_BASE)
        emails = account.select(["Correo"], {"Correo": email.data})

        if len(emails) == 0:
            raise validators.ValidationError('El email no existe')

    def validate_password(self, password):
        """Función para validar la contraseña"""
        account = Account(DATA_BASE)
        correo = local_storage.getItem("email")
        passwd = account.select(["Contrasena"], {"Correo": correo})

        if len(passwd) > 0:

            if not check_password(password.data, passwd[0][0]):
                raise validators.ValidationError('La contraseña es incorrecta')

    btn_continue = SubmitField('Continuar')
