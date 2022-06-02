""" Módulo de Autenticación de Administrador """

def is_authenticated_user(user, password):
    """Función que comprueba si el usuario admin está autenticado"""
    print(user, password)
    if user == "admin" and password=="daw1234":
        return True
    return False
