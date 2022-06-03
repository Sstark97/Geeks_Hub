%include('admin_header.tpl',title=title)
    <h1 class="title">{{title}}</h1>
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
    <form class="form_container" method="POST" action="{{path}}" enctype="multipart/form-data">
        <fieldset>
            <div class="input">
                {{ form.title.label }}
                {{ form.title }}
            </div>
            <div class="input">
                {{ form.age_rating.label }}
                {{ form.age_rating }}
            </div>
            <div class="input">
                {{ form.GENRES.label }}
                {{ form.GENRES }}
            </div>
            <div class="input">
                {{ form.director.label }}
                {{ form.director }}
            </div>
            <div class="input">
                {{ form.average_score.label }}
                {{ form.average_score }}
            </div>
            <div class="input">
                {{ form.productor.label }}
                {{ form.productor }}
            </div>
            <div class="input">
                {{ form.synopsis.label }}
                {{ form.synopsis }}
            </div>
            <div class="input">
                {{ form.release_date.label }}
                {{ form.release_date }}
            </div>
            <div class="input">
                {{form.cover_page.label}}
                <label class="file" for="cover_page">
                    <span>Selecciona una imagen</span>
                    {{ form.cover_page }}
                </label>
            </div>
            <div class="input">
                {{ form.trailer.label }}
                {{ form.trailer }}
            </div>
            <div class="input">
                {{ form.duration.label }}
                {{ form.duration }}
            </div>
            <div class="button">
                {{ form.submit }}
                <button class="btn_cancel btn_delete"><a href="/admin/films">Cancelar</a></button>     
            </div>     
        </fieldset>
    </form>

    <script src="/static/js/file.js"></script>
</body>
</html>