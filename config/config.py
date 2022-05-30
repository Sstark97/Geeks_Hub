"""Definicion del enlace a la Base de Datos."""
DATA_BASE = "./config/geeks_hub.db"
# Tablas
SUSCRIPTION = "Suscripcion"
FILM = "Pelicula"
SERIES = "Serie"
ACCOUNT = "Cuenta"
PROFILE = "Perfil"
HISTORY = "Historial"

#Formularios
AGE_RATING = (('', 'Selecciona una Calificación'), ('tp', 'Tp'), ('8', '8'), ('12', '12'), ('16', '16'), ('18', '18'))
GENRE = (('', 'Selecciona un Genéro'), ('Suspense', 'Suspense'), ('Terror', 'Terror'), ('Comedia', 'Comedia'), 
        ('Accion', 'Accion'), ('Drama', 'Drama'), ('Fantasia','Fantasia'), ('Romance','Romance'), ('Aventura', 'Aventura'),
        ('Ciencia Ficcion', 'Ciencia Ficcion'), ('Belico', 'Belico'), ('Musical', 'Musical'), ('Documental', 'Documental'))

#Campos de las tablas
SERIES_FIELDS = ('Cod_Serie', 'N_Temporada', 'Titulo', 'Calificacion_Edad', 'Genero', 'Director', 
'Puntuacion_Media', 'Productor', 'Sinopsis', 'Fecha_Publicacion', 'Portada' ,'Trailer', 'Capitulos')
FILM_FIELDS = ('Cod_Pelicula', 'Titulo', 'Calificacion_Edad', 'Genero', 'Director',
'Puntuacion_Media', 'Productor', 'Sinopsis', 'Fecha_Publicacion', 'Portada', 'Trailer', 'Duracion')
ACCOUNT_FIELDS = ('Correo','Nombre','Apellidos','Direccion','Telefono','Tipo_Suscripcion')
