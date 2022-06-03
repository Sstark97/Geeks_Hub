"""Archivo de Rutas de la paǵina Home."""
import sys
from bottle import get, template
from models.profile import Profile
from models.film import Film
from models.series import Series
from models.favorites import Favorites
from models.history import History
from config.config import DATA_BASE
sys.path.append('models')

@get('/home')
def home_index():



    return template("home")