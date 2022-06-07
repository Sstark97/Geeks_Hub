"""Archivo donde reside la función que hashea las contraseñas"""
from bcrypt import hashpw, checkpw, gensalt

def hash_password(password):
    """Función que hashea la contraseña"""
    return hashpw(password.encode('utf-8'), gensalt())
    
def check_password(password, hashed_password):
    """Función que comprueba si la contraseña es correcta"""
    return checkpw(password.encode('utf-8'), hashed_password)
    