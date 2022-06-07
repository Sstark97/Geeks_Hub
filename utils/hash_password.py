"""Archivo donde reside la función que hashea las contraseñas"""
from bcrypt import hashpw, checkpw, gensalt

def hash_password(password):
    """Función que hashea la contraseña"""
    passwd = password.encode()
    sal = gensalt()

    return hashpw(passwd, sal)
    
def check_password(password, hashed_password):
    """Función que comprueba si la contraseña es correcta""" 
    passwd = password.encode()
    hackwd = hashed_password.encode()

    return checkpw(passwd, hackwd)
