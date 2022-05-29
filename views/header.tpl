<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Header</title>

    <!-- Fuentes -->

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Display:wght@100;200;300&display=swap" rel="stylesheet">
    
    <!-- Iconos -->

    <link href='https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css' rel='stylesheet'>

    <!-- Estilos -->

    <link rel="stylesheet" href="/static/css/global.css">
</head>
<body>
    <main>
        <header>
            <ul class="head">

                <li class="logo">
                    <a href="">
                        <img src="/static/img/logo.png" alt="logo">
                    </a>
                </li>

                <li class="menu_tablet">
                    <a href="">Series</a>
                    <a href="">Películas</a>
                </li>

                <li class="menu_desktop">
                    <a href="">
                        <i class='bx bx-search-alt-2 search'></i>
                    </a>
                    <div class="dropdown">
                        <i class='bx bxs-user-circle user'></i>
                        <ul>
                            <li><a href=""><i class='bx bxs-user-account' ></i>Ir a Perfiles</a></li>
                            <hr>
                            <li><a href=""><i class='bx bx-user' ></i>Cuenta</a></li>
                            <li><a href=""><i class='bx bxs-heart'></i>Favoritos</a></li>
                            <li><a href=""><i class='bx bx-history'></i>Historial</a></li>
                            <hr>
                            <li><a href=""><i class='bx bx-log-out' ></i>Cerrar Sesión</a></li>
                        </ul>
                    </div>

                </li>

            </ul>
        </header>
