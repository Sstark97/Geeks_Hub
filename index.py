"""Archivo de inicio de la aplicación."""
import os
from bottle import get, run, template, static_file, error
from utils.login_decorator import is_login
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
@is_login
def index():
    """Página de inicio de la aplicación."""
    
    return template('landing.tpl')


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
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

    
