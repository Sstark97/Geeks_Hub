<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Página para cambiar la contraseña">
    <meta name="keywords" content="geeks hub, streaming, películas, series">
    <meta name="author" content="Sara Cabrera, Aitor Santana, Javier Martel"/>
    <meta name="copyright" content="Geeks Hub"/>
    <meta property="og:image" content="/static/img/logo.png">
    <meta property="og:description" content="La mejor plataforma de Streaming para Geeks">
    <meta http-equiv="expires" content="43200"/>
    
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
    
    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">

    <title>Cambiar la Contraseña</title>

</head>
<body>
    <img src="/static/img/logo.png" alt="logo">
    <h1>Restablezca la contraseña</h1>

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

    <form method="POST" action="/change_password_process" autocomplete="off">
        <fieldset>

            <div class="edit_input">
                {{form.code}}
                {{form.code.label}}
            </div>
            
            <div class="contain">
                <div class="edit_input">
                    {{ form.password }}
                    {{ form.password.label }}
                </div>
                <div class="edit_input">
                    {{ form.password_confirm }}
                    {{ form.password_confirm.label }}
                </div>
            </div>

            <div class="button">
                {{ form.btn_continue }}
            </div>         
        </fieldset>
    </form>
</body>
</html>
