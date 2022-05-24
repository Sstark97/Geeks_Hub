"""Archivo de inicio de la aplicación."""
import sys
from bottle import get, run, template, static_file
from models.film import Film
from config.config import DATA_BASE
sys.path.append('models')

@get('/')
def index():
    """Página de inicio de la aplicación."""
    
    return template('index.tpl')

@get("/static/<filepath:path>")
def html(filepath):
    """Servicio de archivos estáticos."""
    return static_file(filepath, root = "./static")

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
