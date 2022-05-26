"""Formulario de Eliminacion de Contenido"""
from wtforms import Form, SubmitField 

class DeleteContentForm(Form):
    """Clase para el formulario de Eliminación de contenido"""

    delete = SubmitField('delete', render_kw={'value':'Borrar'})
    cancel = SubmitField('cancel', render_kw={'value':'Cancelar'})
