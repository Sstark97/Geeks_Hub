%include('admin_header.tpl')
    <div class="admin_container">
        <h3>Películas mejor valoradas</h3>
        <div class="films_container">
            %for film in films:
                <div class="film_container">
                    %for col in film:
                        %if film.index(col) == 0:
                            <div class="image">
                                <img src="{{col}}" alt="{{film[1]}}">
                            </div>
                        %else:
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
                    %if serie.index(col) == 0:
                        <div class="image">
                            <img src="{{col}}" alt="{{serie[1]}}">
                        </div>
                    %else:
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