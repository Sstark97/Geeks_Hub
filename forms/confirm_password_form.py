"""Fichero para la creación del formulario de cambiar contraseña"""
from wtforms import Form, StringField, PasswordField, SubmitField , validators
from config.local_storage import local_storage

class ConfirmForm(Form):
    """Clase para la realización del formulario de inicio"""

    code = StringField('Código', [validators.InputRequired(), validators.Length(min=4, max=4)])

    def validate_code(self, code):
        """Función para validar el código"""
        code_now = local_storage.getItem("code")
        if code.data != code_now:
            raise validators.ValidationError('El código es incorrecto')

    password = PasswordField('Contraseña', [
                                            validators.Length(min=1, max=20),
                                            validators.DataRequired(),
                                            validators.EqualTo('password_confirm',
                                            message='Las contraseñas no coinciden')
                                            ])
    password_confirm = PasswordField('Repita la contraseña')

    btn_continue = SubmitField('Continuar')
