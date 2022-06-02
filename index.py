"""Archivo de inicio de la aplicación."""
from bottle import get, run, template, static_file, auth_basic
from controllers.film_controller import *
from controllers.series_controller import *
from controllers.suscription_controller import *
from controllers.account_controller import *
from controllers.profile_controller import *
from controllers.history_controller import *
from controllers.admin_controller import *


@get('/')
def index():
    """Página de inicio de la aplicación."""

    return template('landing.tpl')

@get('/404')
def about():
    """Página de prueba"""
    return static_file('/html/404.html', root='static')

@get("/static/<filepath:path>")
def html(filepath):
    """Servicio de archivos estáticos."""
    return static_file(filepath, root = "./static")

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
    
