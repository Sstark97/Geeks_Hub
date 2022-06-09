"""Formulario de Eliminacion de Contenido"""
from wtforms import Form, SubmitField, EmailField, validators
from config.local_storage import local_storage

class DeleteAccountForm(Form):
    """Clase para el formulario de Eliminación de una Cuenta"""

    email = EmailField('Email', [validators.InputRequired(), validators.Email()])

    def validate_email(self, email):
        """Función para validar el email"""

        if email.data != local_storage.getItem("email"):
            raise validators.ValidationError('El email no coincide')

    delete = SubmitField('delete', render_kw={'value':'Borrar', 'class':'btn btn_delete'})
