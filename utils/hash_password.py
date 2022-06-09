"""Archivo donde reside la función que hashea las contraseñas"""
from bcrypt import hashpw, checkpw, gensalt

def hash_password(password):
    """Función que hashea la contraseña"""
    passwd = password.encode()
    sal = gensalt()
    hashed_password = hashed_password.encode() if isinstance(hashed_password, str) else hashed_password

    return hashpw(passwd, sal)
    
def check_password(password, hashed_password):
    """Función que comprueba si la contraseña es correcta""" 
    passwd = password.encode()
    hashed_password = hashed_password.encode() if isinstance(hashed_password, str) else hashed_password

    return checkpw(passwd, hashed_password)
