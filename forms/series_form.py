"""Formulario de Registro de Series"""
import decimal
from wtforms import Form, StringField, IntegerField, DateField, SubmitField , TextAreaField, SelectField, DecimalField, FileField, validators
from config.local_storage import local_storage
from config.config import GENRES, AGE_RATING, DATA_BASE
from models.series import Series


class SeriesForm(Form):
    """Clase para el formulario de registro de series"""
    title  = StringField('Título', [
                                    validators.InputRequired(), 
                                    validators.Length(min=1, max=50), 
                                ])
    season = IntegerField('N_Temporada', 
                            [validators.DataRequired("El campo es obligatorio"), 
                            validators.NumberRange(min=1, max=100, message="El campo debe ser un número entre 1 y 100")],
                            default=1, 
                        )

    def validate_season(self, season):
        """Función para validar la temporada"""
        serie = Series(DATA_BASE)
        titles = serie.select(["Titulo"], {"Titulo": local_storage.getItem("Titulo"), "N_Temporada": season.data})

        print(local_storage.getItem("Titulo"))

        if len(titles) != 0 and local_storage.getItem("action") != "edit":
            local_storage.removeItem("Titulo")
            raise validators.ValidationError('Ya existe esa temporada')

    
    age_rating = SelectField(label='Calificación', choices=AGE_RATING, validators = [validators.InputRequired()])

    GENRES = SelectField(label='Genero', choices=GENRES, validators = [validators.InputRequired()])

    director = StringField('Director', [ 
                                    validators.InputRequired(),
                                    validators.Length(min=1, max=50),
                                ])

    average_score = DecimalField('Puntuación Media', 
                                rounding=decimal.ROUND_UP,
                                places=2,
                                validators = [
                                    validators.DataRequired("El campo es obligatorio"),
                                    validators.NumberRange(min=1.00, max=5.00, 
                                    message="El campo debe ser un número entre 1.01 y 5.00")
                                ], 
                                default=1.01,
                            )

    productor = StringField('Productor', [ 
                                    validators.InputRequired(),
                                    validators.Length(min=1, max=30),
                                ])

    synopsis = TextAreaField('Sinopsis', [validators.Length(min=10, max=1000)])

    release_date = DateField('Fecha de Publicación',[validators.DataRequired("El campo es obligatorio")],format='%Y-%m-%d')

    cover_page = FileField('Portada', render_kw={'accept':'image/png, image/jpeg', 'class':'inputfile'})

    trailer = StringField('Tráiler', [ 
                                    validators.InputRequired(),
                                    validators.Length(min=6, max=80),
                                ])

    chapters = IntegerField('Capítulos', 
                                [validators.DataRequired("El campo es obligatorio"), 
                                validators.NumberRange(min=1, max=100, message="El campo debe ser un número entre 1 y 100")],
                                default=1, 
                            )
    submit = SubmitField('Guardar')
