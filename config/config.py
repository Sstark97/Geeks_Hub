"""Definicion del enlace a la Base de Datos."""
DATA_BASE = "./config/geeks_hub.db"
# Tablas
SUSCRIPTION = "Suscripcion"
FILM = "Pelicula"
SERIES = "Serie"
ACCOUNT = "Cuenta"
PROFILE = "Perfil"
HISTORY = "Historial"
FAVORITES = "Favoritos"
FAVORITES_CONTENT = "Contenido_Favorito"

#Formularios
AGE_RATING = (('', 'Selecciona una Calificación'), ('tp', 'Tp'), ('8', '8'), ('12', '12'), ('16', '16'), ('18', '18'))
GENRES = (('', 'Selecciona un Genéro'), ('Suspense', 'Suspense'), ('Terror', 'Terror'), ('Comedia', 'Comedia'), 
        ('Accion', 'Accion'), ('Drama', 'Drama'), ('Fantasia','Fantasia'), ('Romance','Romance'), ('Aventura', 'Aventura'),
        ('Ciencia Ficcion', 'Ciencia Ficcion'), ('Belico', 'Belico'), ('Musical', 'Musical'), ('Documental', 'Documental'))

#Campos de las tablas
SERIES_FIELDS = ('Cod_Serie', 'N_Temporada', 'Titulo', 'Calificacion_Edad', 'Genero', 'Director', 
'Puntuacion_Media', 'Productor', 'Sinopsis', 'Fecha_Publicacion', 'Portada' ,'Trailer', 'Capitulos')

FILM_FIELDS = ('Calificacion_Edad', 'Genero', 'Director',
'Puntuacion_Media', 'Productor', 'Sinopsis', 'Fecha_Publicacion', 'Duracion')

ACCOUNT_FIELDS = ('Correo','Nombre','Apellidos','Direccion','Telefono','Tipo_Suscripcion')

GENRES_FIELDS = ('Suspense', 'Terror', 'Comedia', 'Accion', 'Drama', 'Fantasia', 'Romance', 'Aventura', 'Ciencia Ficcion', 'Belico', 'Musical', 'Documental')

AVATARS = ("/static/img/avatar/avatar1.png", "/static/img/avatar/avatar2.png", "/static/img/avatar/avatar3.png", 
"/static/img/avatar/avatar4.png", "/static/img/avatar/avatar5.png", "/static/img/avatar/avatar6.png", 
"/static/img/avatar/avatar7.png", "/static/img/avatar/avatar8.png", "/static/img/avatar/avatar9.png")
