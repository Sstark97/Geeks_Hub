<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inicio de Sesión</title>
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

</head>
<body>
    <img src="/static/img/logo.png" alt="logo">
    <h1>Inicie Sesión</h1>

    <form method="POST" action="/login" autocomplete="off">
        <fieldset>
            <div class="edit_input">
                {{ form.email }}
                {{ form.email.label }}
            </div>
            <div class="edit_input">
                {{ form.password }}
                {{ form.password.label }}
            </div>
            <div class="button">
                <a href="/select_profiles">
                    {{ form.btn_continue }}
                </a>
            </div>
        </fieldset>
        <div class="register">
            <p>Si aún no estás registrado,&nbsp</p>
            <a href="/register">
                <input type="button" value="regístrate aquí"/>
            </a>
        </div>

    </form>
</body>
</html>