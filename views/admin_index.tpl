<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/admin.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    <link href='https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css' rel='stylesheet'>
    <title>Administración</title>
</head>
<body>
    <header>
        <input type="checkbox">
        <i class='bx bx-menu'></i>
        <i class='bx bx-x'></i>
        <nav>
            <ul>
                <li>
                    <a href="/admin/films">Películas</a>
                </li>
                <li>
                    <a href="/admin/series">Series</a>
                </li>
            </ul>
        </nav>
    </header>

    <div class="logo">
        <img src="/static/img/logo.png" alt="logo">
    </div>

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