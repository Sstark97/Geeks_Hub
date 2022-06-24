<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Cambio de Perfil">
    <meta name="keywords" content="geeks hub, streaming, películas, series">
    <meta name="author" content="Sara Cabrera, Aitor Santana, Javier Martel"/>
    <meta name="copyright" content="Geeks Hub"/>
    <meta property="og:image" content="/static/img/logo.png">
    <meta property="og:description" content="La mejor plataforma de Streaming para Geeks">
    <meta http-equiv="expires" content="43200"/>

    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">
    <title>Selección de Perfil</title>
    <!-- Estilos -->

    <!-- Estilos Globales -->
    
    <link rel="stylesheet" href="/static/css/global/global.css">
    <link rel="stylesheet" href="/static/css/global/global_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/global/global_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos de Formularios -->
    
    <link rel="stylesheet" href="/static/css/form/form.css">
    <link rel="stylesheet" href="/static/css/form/form_tablet.css" media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/form/form_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos de los Errores -->

    <link rel="stylesheet" href="/static/css/errors/erros.css">
    <link rel="stylesheet" href="/static/css/errors/errors_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/errors/errors_desktop.css" media="only screen and (min-width: 992px)">

</head>
<body>
    <img class="profile_logo" src="/static/img/logo.png" alt="logo">
    <h1>¿Quién eres?</h1>

    <form action="/select_profile" method="post">
        <div class="form_container">

            <label for="profile">Selecciona un perfil</label>
                % if error != "":
                    <blockquote>
                        <ul>
                            <li>{{ error }}</li>
                        </ul>
                    </blockquote>
                % end
            <div class="avatar">

            %if rows != []:
                %cont = 0
                %for row in rows:
                    <div>
                        <input class="hidden" type="radio" name="profile_code" id={{ f"profile_code{cont}" }} value="{{ row[0] }}" tabindex="0">
                        <label for={{ f"profile_code{cont}" }} >
                            <img class="profile_image" src="{{ row[3] }}" alt="Avatar">
                        </label>
                        <p>{{ row[2] }}</p>
                    </div>
                    %cont += 1
                %end
            %end

            %if len(rows) != 5:
                <div>
                    <a href="/profiles"><img class="profile_image" src="/static/img/avatar/add.png" alt="Añadir"></a>
                    <p>Añadir</p>
                </div>
            %end
            
            </div>
            <button type="submit" class="btn" name="btn_continue" onclick="resetDarkMode()">Continuar</button>
        </div>
    </form>

    <script src="/static/js/dark_mode.js"></script>
</body>
</html>