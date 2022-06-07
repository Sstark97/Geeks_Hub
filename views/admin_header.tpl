<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    <link href='https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css' rel='stylesheet'>

    <!-- Estilos -->

    <!-- Estilos Globales -->

    <link rel="stylesheet" href="/static/css/global/global.css">
    <link rel="stylesheet" href="/static/css/global/global_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/global/global_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos Admin -->

    <link rel="stylesheet" href="/static/css/admin/admin.css">
    <link rel="stylesheet" href="/static/css/admin/admin_tables_mobile.css" media="only screen and (max-width: 536px)">
    <link rel="stylesheet" href="/static/css/admin/admin_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px) ">
    <link rel="stylesheet" href="/static/css/admin/admin_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos de los Formularios-->

    <link rel="stylesheet" href="/static/css/admin_forms/admin_forms.css">
    <link rel="stylesheet" href="/static/css/admin_forms/admin_forms_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/admin_forms/admin_forms_desktop.css"
        media="only screen and (min-width: 992px)">

    <!-- Estilos de la Vista Detalle de Contenido-->
    
    <link rel="stylesheet" href="/static/css/admin_content/admin_content.css">
    <link rel="stylesheet" href="/static/css/admin_content/admin_content_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/admin_content/admin_content_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos de los Errores -->

    <link rel="stylesheet" href="/static/css/errors/erros.css">
    <link rel="stylesheet" href="/static/css/errors/errors_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/errors/errors_desktop.css" media="only screen and (min-width: 992px)">


    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">
    <title>{{title}}</title>
</head>

<body>
    <header>
        <input type="checkbox">
        <i class='bx bx-menu'></i>
        <i class='bx bx-x'></i>
        <nav>
            <ul>
                <li class="logo_nav">
                    <a href="/admin">
                        <img src="/static/img/logo.png" alt="logo">
                    </a>
                </li>
                <li>
                    <a href="/admin/films">Películas</a>
                </li>
                <li>
                    <a href="/admin/series">Series</a>
                </li>
                <li>
                    <a href="/admin/accounts">Cuentas</a>
                </li>
            </ul>
        </nav>
    </header>

    <div class="logo">
        <a href="/admin">
            <img src="/static/img/logo.png" alt="logo">
        </a>
    </div>