"""Archivo de Rutas de la Suscripcion."""
import sys
from bottle import get, template
from models.suscription import Suscription
from config.config import DATA_BASE
sys.path.append('models')

@get('/suscription')
def index():
    """Página de inicio de la aplicación."""
    suscripciones = Suscription(DATA_BASE)

    row = suscripciones.select(['*'], {'Tipo_Suscripcion': 'Basico', 'Precio': '8.99', 'Calidad_Videos': 'HD'})
    
    return template('index.tpl')