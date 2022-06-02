"""Formulario de Registro de Series"""
import decimal
from wtforms import Form, StringField, IntegerField, DateField, SubmitField , TextAreaField, SelectField, DecimalField, FileField, validators
from config.config import GENRE, AGE_RATING

class SeriesForm(Form):
    """Clase para el formulario de registro de series"""
    season = IntegerField('N_Temporada', 
                               [validators.DataRequired("El campo es obligatorio"), 
                                validators.NumberRange(min=1, max=100, message="El campo debe ser un número entre 1 y 100")],
                                default=1, 
                            #    render_kw={'class':'myclass'}
                            )
    title  = StringField('Título', [
                                    validators.InputRequired(), 
                                    validators.Length(min=6, max=50), 
                                ])
    # calificacion_edad
    age_rating = SelectField(label='Calificación', choices=AGE_RATING, validators = [validators.InputRequired()])

    genre = SelectField(label='Genero', choices=GENRE, validators = [validators.InputRequired()])

    director = StringField('Director', [ 
                                    validators.InputRequired(),
                                    validators.Length(min=6, max=30),
                                ])

    average_score = DecimalField('Puntuación Media', 
                                rounding=decimal.ROUND_UP,
                                places=2,
                                validators = [validators.DataRequired("El campo es obligatorio")], 
                                default=1.01,
                            #    render_kw={'class':'myclass'}
                            )

    productor = StringField('Productor', [ 
                                    validators.InputRequired(),
                                    validators.Length(min=6, max=30),
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
                            #    render_kw={'class':'myclass'}
                            )
    submit = SubmitField('Guardar')
