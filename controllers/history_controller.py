"""Archivo de Rutas de los Historiales."""
import sys
from bottle import get
from models.history import History
from config.config import DATA_BASE
sys.path.append('models')

@get('/history')
def history_index():
    """Página de inicio de los Historiales."""
    historial = History(DATA_BASE)

    # Añadir
    # historial.insert({"Cod_Perfil" : "Perfil13", "Cod_Contenido" : "P004", "Fecha_Visualizacion" : "2022-05-24"})
    # row = historial.select(["*"], {"Cod_Perfil" : "Perfil13"})
    
    # Select perfiles que han visto peliculas
    # row = historial.select(['*'],  {"Cod_Contenido": "P%"})

    # Select de todos los historiales
    row = historial.select(['*'])

    return str(row)
