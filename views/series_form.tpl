%include('admin_header.tpl',title=title)
    <h1>Formulario de Creación de Series</h1>
    % if form.errors:
        <blockquote>
            <p>Hay errores en el formulario:</p>
            <ul>
            % for field, errors in form.errors.items():
                % for error in errors:
                <li>{{field}}: {{error}}</li>
                % end
            % end
            </ul>
        </blockquote>
    % end
    <form method="POST" action="{{path}}" enctype="multipart/form-data">
        <fieldset>
            <div>
                {{ form.season.label }}:
                {{ form.season }}

            </div>
            <div>
                {{ form.title.label }}:
                {{ form.title }}
            </div>
            <div>
                {{ form.age_rating.label }}:
                {{ form.age_rating }}
            </div>
            <div>
                {{ form.genre.label }}:
                {{ form.genre }}
            </div>
            <div>
                {{ form.director.label }}:
                {{ form.director }}
            </div>
            <div>
                {{ form.average_score.label }}:
                {{ form.average_score }}
            </div>
            <div>
                {{ form.productor.label }}:
                {{ form.productor }}
            </div>
            <div>
                {{ form.synopsis.label }}:
                {{ form.synopsis }}
            </div>
            <div>
                {{ form.release_date.label }}:
                {{ form.release_date }}
            </div>
            <div>
                {{ form.cover_page.label }}:
                {{ form.cover_page }}
            </div>
            <div>
                {{ form.trailer.label }}:
                {{ form.trailer }}
            </div>
            <div>
                {{ form.chapters.label }}:
                {{ form.chapters }}
            </div>
            <div>
                {{ form.submit }}
                <button><a href="/admin/series">Cancelar</a></button>      
            </div>
        </fieldset>
    </form>
</body>
</html>