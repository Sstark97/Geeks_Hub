"""Fichero para el modelo Profile."""
from models.model import Model
from config.config import PROFILE

class Profile(Model):
    """Clase que maneja la Tabla Perfil."""
    def __init__(self, db_name):
        super().__init__(db_name)
        self._table_name = PROFILE

    def code_generator(self):
        """Genera un código único para el Perfil."""
        conn = self._connect()
        cursor = conn.cursor()
        query = 'SELECT COUNT(Perfil.Cod_Perfil) + 1 FROM Perfil'
        cursor.execute(query)
        contador = cursor.fetchone()[0]
        cod_perfil = ""

        if contador < 10:
                cod_perfil = f"PR00{contador}"
        elif contador < 100:
                cod_perfil = f"PR0{contador}"
        elif contador < 1000:
                cod_perfil = f"PR{contador}"
                
        cursor.close()
        conn.close()
        return cod_perfil
        