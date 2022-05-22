"""Archivo de inicio de la aplicación."""
from bottle import get, run, template

@get('/')
def index():
    """Página de inicio de la aplicación."""
    return template('index.tpl')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
