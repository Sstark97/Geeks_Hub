"""Archivo de inicio de la aplicación."""
from operator import ge
from bottle import get, run, template, static_file, error
from controllers.film_controller import *
from controllers.series_controller import *
from controllers.suscription_controller import *
from controllers.account_controller import *
from controllers.profile_controller import *
from controllers.history_controller import *
from controllers.favorites_controller import * 
from controllers.admin_controller import *
from controllers.account_settings_controller import *
from controllers.home_controller import *
from controllers.search_controller import *

@get('/')
def index():
    """Página de inicio de la aplicación."""
    user = local_storage.getItem("profile")
    if not user:
        return template('landing.tpl')
        
    redirect("/home")
    return None

@get('/correo')
def email_index():
    """Página de inicio de la aplicación."""
    return static_file('register_email.html', root='./static/html')

@error(404)
def not_found_page(error1):
    """Página de Error 404."""
    return static_file('/html/404.html', root='static')
@error(500)
def server_error_page(error2):
    """Página de Error 500."""
    return static_file('/html/500.html', root='static')

@get("/static/<filepath:path>")
def html(filepath):
    """Servicio de archivos estáticos."""
    return static_file(filepath, root = "./static")

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
    
