<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/global.css">
    <link rel="stylesheet" href="/static/css/admin.css">
    <title>Administración</title>
</head>
<body>
    <head>
        <nav>
            <div>
                <a href="/admin/films">Películas</a>
            </div>
            <div>
                <a href="/admin/series">Series</a>
            </div>
        </nav>
    </head>
    <h2>Zona de Administración</h2>

    <div class="admin_container">
        <h3>Películas mejor valoradas</h3>
        <div class="films_container">
            %for film in films:
                <div class="film_container">
                %for col in film:
                    %if film.index(col) == 0:
                        <div class="film_image">
                            <img src="{{col}}" alt="{{film[1]}}">
                        </div>
                    %else:
                        <div class="film_info">
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
                        <div class="film_image">
                            <img src="{{col}}" alt="{{film[1]}}">
                        </div>
                    %else:
                        <div class="film_info">
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