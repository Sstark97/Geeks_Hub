""" Módulo de Autenticación de Administrador """
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def is_authenticated_user(user, password):
    """Función que comprueba si el usuario admin está autenticado"""

    return user == getenv('ADMIN_USER') and password== getenv('ADMIN_PASSWORD')
