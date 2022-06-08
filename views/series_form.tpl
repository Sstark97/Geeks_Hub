%include('admin_header.tpl',title=title)
    <h1 class="title">{{title}}</h1>
    % if len(error) > 0:
        <blockquote>
            <ul>
                <li>{{error}}</li>
            </ul>
        </blockquote>
    % end

    % if form.errors:
    <blockquote>
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
            <div class="edit_input">
                {{ form.season }}
                {{ form.season.label }}
            </div>
            <div class="edit_input">
                {{ form.title }}
                {{ form.title.label }}
            </div>
            <div class="input">
                {{ form.age_rating }}
                {{ form.age_rating.label }}
            </div>
            <div class="input">
                {{ form.GENRES }}
                {{ form.GENRES.label }}
            </div>
            <div class="edit_input">
                {{ form.director }}
                {{ form.director.label }}
            </div>
            <div class="edit_input">
                {{ form.average_score }}
                {{ form.average_score.label }}
            </div>
            <div class="edit_input">
                {{ form.productor }}
                {{ form.productor.label }}
            </div>
            <div class="date_input">
                {{ form.release_date }}
                {{ form.release_date.label }}
            </div>
            <div class="file_input">
                <label class="file" for="cover_page">
                    <span>Selecciona una imagen</span>
                    {{ form.cover_page }}
                </label>
                <p>Portada</p>
            </div>
            <div class="edit_input">
                {{ form.trailer }}
                {{ form.trailer.label }}
            </div>
            <div class="edit_input">
                {{ form.chapters }}
                {{ form.chapters.label }}
            </div>
            <div class="textarea_input">
                {{ form.synopsis }}
                {{ form.synopsis.label }}
            </div>
            <div class="button">
                {{ form.submit }}
                <button class="btn_cancel btn_delete"><a href="/admin/series">Cancelar</a></button>     
            </div>     
        </fieldset>
    </form>

    <script src="/static/js/file.js"></script>
</body>
</html