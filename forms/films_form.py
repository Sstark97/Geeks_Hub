"""Formulario de Registro de Peliculas"""
import decimal
from wtforms import Form, StringField, IntegerField, DateField, SubmitField , TextAreaField, SelectField, DecimalField, FileField, validators
from config.config import GENRES, AGE_RATING

class FilmsForm(Form):
    """Clase para el formulario de registro de peliculas"""
    title  = StringField('Título', [
                                    validators.InputRequired(), 
                                    validators.Length(min=1, max=100)
                                    ])

    age_rating = SelectField(label='Calificación', choices=AGE_RATING, validators = [validators.InputRequired()])

    GENRES = SelectField(label='Genero', choices=GENRES, validators = [
                                                                        validators.InputRequired()
                                                                        ])

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
                                default=1.01
                            )

    productor = StringField('Productor', [ 
                                        validators.InputRequired(),
                                        validators.Length(min=1, max=30)
                                        ])

    synopsis = TextAreaField('Sinopsis', [validators.Length(min=10, max=1000)])

    release_date = DateField('Fecha de Publicación',[
                                                    validators.DataRequired("El campo es obligatorio"
                                                    )], format='%Y-%m-%d')

    cover_page = FileField('Portada', render_kw={'accept':'image/png, image/jpeg', 'class':'inputfile'})

    trailer = StringField('Tráiler', [ 
                                    validators.InputRequired(),
                                    validators.Length(min=6, max=80)
                                    ])

    duration = IntegerField('Duración', [
                                        validators.DataRequired("El campo es obligatorio"), 
                                        validators.NumberRange(min=60, max=200, message="El campo debe ser un número entre 6 y 200")
                                        ], default=60)
    submit = SubmitField('Guardar')
