%include('admin_header.tpl',title='Administración')
    <div class="admin_container">
        <h3>Películas mejor valoradas</h3>
        <div class="films_container">
            %for film in films:
                <div class="film_container">
                    %for col in film:
                        %if film.index(col) == 1:
                            <div class="image">
                                <a href="admin/films/{{film[0]}}">
                                    <img src="{{col}}" alt="{{film[1]}}">
                                </a>
                            </div>
                        %elif film.index(col) == 2:
                            <div class="info">
                                <p>{{col}}</p>
                            </div>
                        %end
                    %end
                </div>
            %end
        </div>

        <h3>Series mejor valoradas</h3>
        <div class="series_container">
            %for serie in series:
                <div class="serie_container">
                %for col in serie:
                    %if serie.index(col) == 1:
                        <div class="image">
                            <a href="admin/series/{{serie[0]}}">
                                <img src="{{col}}" alt="{{serie[0]}}">
                            </a>
                        </div>
                    %elif serie.index(col) == 2:
                        <div class="info">
                            <p>{{col}}</p>
                        </div>
                    %end
                %end
                </div>
            %end
        </div>
    </div>
</body>
</html>