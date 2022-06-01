"""Formulario de Eliminacion de Contenido"""
from wtforms import Form, SubmitField 

class DeleteContentForm(Form):
    """Clase para el formulario de Eliminación de contenido"""

    delete = SubmitField('delete', render_kw={'value':'Borrar', 'class':'btn btn_delete'})
    cancel = SubmitField('cancel', render_kw={'value':'Cancelar', 'class':'btn btn_view'})
