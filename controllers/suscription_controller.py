"""Archivo de Rutas de la Suscripcion."""
import sys
from bottle import get
from models.suscription import Suscription
from config.config import DATA_BASE
sys.path.append('models')

@get('/suscriptions')
def index():
    """Página de inicio de las Suscripciones."""
    suscripciones = Suscription(DATA_BASE)

    row = suscripciones.select(['*'], {'Tipo_Suscripcion': 'Basico', 'Precio': '8.99'})
    
    return str(row)