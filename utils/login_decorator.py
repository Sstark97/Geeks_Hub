"""Decorador que verifica que un usuario este logeado"""
from bottle import redirect
from config.local_storage import local_storage

def login_required(func):
    """Decorador que verifica que un usuario este logeado"""
    def wrapper(*args, **kwargs):
        """Decorador que verifica que un usuario este logeado"""
        user = local_storage.getItem("email")
        user_profile = local_storage.getItem("profile")

        if not user:
            return redirect("/login")
        if not user_profile:
            return redirect("/select_profile")
        return func(*args, **kwargs)

    return wrapper

def is_login(func):
    """Decorador que verifica que un usuario este logeado"""
    def wrapper(*args, **kwargs):
        """Decorador que verifica que un usuario este logeado"""
        user = local_storage.getItem("email")

        if user:
            return redirect("/home")
        return func(*args, **kwargs)

    return wrapper
