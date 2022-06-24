<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">
    <meta name="description" content="Página para logearse en la Web">
    <meta name="keywords" content="geeks hub, streaming, películas, series">
    <meta name="author" content="Sara Cabrera, Aitor Santana, Javier Martel"/>
    <meta name="copyright" content="Geeks Hub"/>
    <meta property="og:image" content="/static/img/logo.png">
    <meta property="og:description" content="La mejor plataforma de Streaming para Geeks">
    <title>{{title}}</title>
    <!-- Estilos -->

    <!-- Estilos Globales -->

    <link rel="stylesheet" href="/static/css/global/global.css">
    <link rel="stylesheet" href="/static/css/global/global_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/global/global_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos de Formularios -->

    <link rel="stylesheet" href="/static/css/form/form.css">
    <link rel="stylesheet" href="/static/css/form/form_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/form/form_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos de los Errores -->

    <link rel="stylesheet" href="/static/css/errors/erros.css">
    <link rel="stylesheet" href="/static/css/errors/errors_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/errors/errors_desktop.css" media="only screen and (min-width: 992px)">

</head>

<body>
    <img src="/static/img/logo.png" alt="logo">
    <h1>{{title}}</h1>
    %if message != '':
        <p class="mensaje">{{message}}</p>
    %end

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

    <form method="POST" action="{{path}}" autocomplete="off">
        <fieldset>
            <div class="edit_input">
                {{ form.email }}
                {{ form.email.label }}
            </div>
            %if path == '/login':
                <div class="edit_input">
                    {{ form.password }}
                    {{ form.password.label }}
                </div>
            %end
            <div class="button">
                <a href="{{action}}" tabindex="-1">
                    {{ form.btn_continue }}
                </a>
            </div>
        </fieldset>

        %if path == '/login':
            <div class="links">
                <p>Si aún no estás registrado,&nbsp</p>
                <a href="/register" tabindex="-1">
                    <input type="button" value="regístrate aquí" />
                </a>
            </div>

            <div class="links">
                <p>¿Has olvidado tu contraseña?&nbsp</p>
                <a href="/change_password" tabindex="-1">
                    <input type="button" value="Haz click aquí" />
                </a>
            </div>
        %end

    </form>
</body>

</html>