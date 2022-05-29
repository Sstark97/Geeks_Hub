"""Fichero para el Formulario de Registro"""
from email_validator import EmailNotValidError
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField , validators, DateField, SelectField

class RegistrationForm(Form):
    """Clase que maneja el formulario de Registro"""
    
    name = StringField('Nombre', [validators.InputRequired(), validators.Length(min=1, max=20)])
    surname = StringField('Apellidos', [validators.InputRequired(), validators.Length(min=1, max=25)])
    email = StringField('Correo electrónico', [validators.InputRequired(), validators.Length(min=6, max=60), validators.Email()])
    password = PasswordField('Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('password_confirm', 
                           message='Las contraseñas no coinciden')
        ])
    password_confirm = PasswordField('Repita la contraseña')
    direction = StringField('Dirección', [validators.InputRequired(), validators.Length(min=1, max=70)])
    phone_number = StringField('Teléfono', [validators.InputRequired(), validators.Length(min=1, max=9)])  # 9 dígitos España
    # birth_date = DateField('Fecha de Nacimiento', [validators.DataRequired()])  
    suscription = SelectField("Tipo de Suscripcion", choices=[('Basico', 'Basico'), ('Estandar', 'Estandar'), ('Premium', 'Premium')])  
    
    register = SubmitField('Registrar')
    # cancel = SubmitField('Cancelar')
