"""Formulario de Registro de Series"""
from wtforms import Form, StringField, IntegerField, DateField, SubmitField , TextAreaField, SelectField, validators

COUNTRIES = [('', 'Select country'), ('ES', 'Spain'), ('US', 'United States'), ('UK', 'United Kingdom')]


class SeriesForm(Form):
    """Clase para el formulario de registro de series"""
    season = IntegerField('N_Temporada', 
                               [validators.DataRequired("El campo es obligatorio") , 
                               validators.Length(min=1, max=10)], 
                               default=1, 
                            #    render_kw={'class':'myclass'}
                            )
    title  = StringField('Título', [
                                    validators.InputRequired(), 
                                    validators.Length(min=6, max=50), 
                                ])
    # calificacion_edad
    age_rating = SelectField(label='Calificación', choices=COUNTRIES, validators = [validators.InputRequired()])

    genre = SelectField(label='Genero', choices=COUNTRIES, validators = [validators.InputRequired()])

    director = StringField('Director', [ 
                                    validators.InputRequired(),
                                    validators.Length(min=6, max=30),
                                ])

    average_score = IntegerField('Puntuación Media', 
                               [validators.DataRequired("El campo es obligatorio") , validators.Length(min=1, max=5)], 
                               default=1, 
                            #    render_kw={'class':'myclass'}
                            )

    productor = StringField('Productor', [ 
                                    validators.InputRequired(),
                                    validators.Length(min=6, max=30),
                                ])

    synopsis = TextAreaField('Sinopsis', [validators.Length(min=10, max=1000)])

    release_date = DateField('Fecha de Publicación', [validators.DataRequired("El campo es obligatorio")])

    cover_page = StringField('Portada', [ 
                                    validators.InputRequired(),
                                    validators.Length(min=6, max=45),
                                ])

    trailer = StringField('Tráiler', [ 
                                    validators.InputRequired(),
                                    validators.Length(min=6, max=80),
                                ])

    chapters = IntegerField('Capítulos', 
                               [validators.DataRequired("El campo es obligatorio") , validators.Length(min=1, max=5)], 
                               default=1, 
                            #    render_kw={'class':'myclass'}
                            )
    submit = SubmitField('Guardar')
