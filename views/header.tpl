<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Header</title>

    <!-- Fuentes -->

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Display:wght@100;200;300&display=swap"
        rel="stylesheet">

    <!-- Iconos -->

    <link href='https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">

    <!-- Estilos Slick Menu-->
    
    <link rel="stylesheet" href="/static/css/slick/slick.css">
    <link rel="stylesheet" href="/static/css/slick/slick-theme.css">

    <!-- Estilos -->

    <!-- Estilos Globales -->
    
    <link rel="stylesheet" href="/static/css/global/global.css">
    <link rel="stylesheet" href="/static/css/global/global_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/global/global_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos de los Ajustes del Usuario-->
    
    <link rel="stylesheet" href="/static/css/acc_settings/account_settings.css">
    <link rel="stylesheet" href="/static/css/acc_settings/account_settings_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/acc_settings/account_settings_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos de la Página Principal -->

    <link rel="stylesheet" href="/static/css/home/home.css">
    <link rel="stylesheet" href="/static/css/home/home_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/home/home_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos de los Contenidos -->

    <link rel="stylesheet" href="/static/css/content/content.css">
    <link rel="stylesheet" href="/static/css/content/content_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/content/content_desktop.css" media="only screen and (min-width: 992px)">

    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">
</head>

<body>
    %from config.local_storage import local_storage
    <main>
        <header class="header_user">
            <ul class="head">
                <li class="logo_user">
                    <a href="/home">
                        <img src="/static/img/logo.png" alt="logo">
                    </a>
                </li>

                <li class="menu_tablet">
                    <a href="/series">Series</a>
                    <a href="/films">Películas</a>
                </li>

                <li class="menu_desktop">
                    <a href="/search">
                        <i class='bx bx-search-alt-2 search'></i>
                    </a>
                    <div class="dropdown">
                        <img src="{{avatar}}" alt="avatar">
                        <i class='bx bxs-chevron-down arrow'></i>
                        <ul>
                            <li><a href="/select_profile"><i class='bx bxs-user-account'></i>Ir a Perfiles</a></li>
                            <hr>
                            <li><a href="/account_settings"><i class='bx bx-user'></i>Cuenta</a></li>
                            <li><a href="/favorites"><i class='bx bxs-heart'></i>Favoritos</a></li>
                            <li><a href=""><i class='bx bx-history'></i>Historial</a></li>
                            <hr>
                            <li><a onclick="logout()"><i class='bx bx-log-out'></i>Cerrar Sesión</a></li>
                        </ul>
                    </div>

                </li>

            </ul>
        </header>