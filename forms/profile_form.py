"""Fichero para la creación de un nuevo perfil"""
from wtforms import Form, StringField, SubmitField , validators

class ProfileForm(Form):
    """Clase para la realización del formulario de creación de perfil"""
    nickname = StringField('Nickname', [validators.InputRequired(), 
                                        validators.Length(min=1, max=20)], render_kw={'class':'form-label'})

    btn_continue = SubmitField('Continuar')
    cancel = SubmitField('Cancelar')
