<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inicio</title>

    <!-- Estilos -->

    <link rel="stylesheet" href="/static/css/global.css">
    <link rel="stylesheet" href="/static/css/landing.css">

    <!-- Iconos -->

    <link href='https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css' rel='stylesheet'>

</head>

<body>
    <div class="main">
        <div class="background">
            <div class="button_login">
                <a href="/login">
                    <button class="login">Iniciar Sesión</button>
                </a>
            </div>
            <div class="logo">
                <img src="/static/img/logo.png" alt="logo">
                <p>Lorem Ipsum es simplemente un texto ficticio de la industria de la impresión y la composición
                    tipográfica. Lorem Ipsum ha sido el texto ficticio estándar de la industria desde el año 1500,
                    cuando un impresor desconocido tomó una galera de tipos y la codificó para hacer un libro de
                    muestras tipográficas. Ha sobrevivido no solo cinco siglos, sino también el salto a la composición
                    tipográfica electrónica, permaneciendo esencialmente sin cambios. Se popularizó en la década de 1960
                    con el lanzamiento de hojas de Letraset que contenían pasajes de Lorem Ipsum y, más recientemente,
                    con software de autoedición como Aldus PageMaker, que incluía versiones de Lorem Ipsum.</p>
            </div>
        </div>
        <div class="content">
            <div class="cuadro"></div>
            <p>Lorem Ipsum es simplemente un texto ficticio de la industria de la impresión y la composición
                tipográfica. Lorem Ipsum ha sido el texto ficticio estándar de la industria desde el año 1500,
                cuando un impresor desconocido tomó una galera de tipos y la codificó para hacer un libro de
                muestras tipográficas. Ha sobrevivido no solo cinco siglos, sino también el salto a la composición
                tipográfica electrónica, permaneciendo esencialmente sin cambios. Se popularizó en la década de 1960
                con el lanzamiento de hojas de Letraset que contenían pasajes de Lorem Ipsum y, más recientemente,
                con software de autoedición como Aldus PageMaker, que incluía versiones de Lorem Ipsum.</p>
        </div>
        <div class="button_submit">
            <a href="/register">
                <input class="submit" type="button" value="Suscríbete ahora">
            </a>
        </div>
        <div class="devices">
            <div class="television">
                <img src="/static/img/television.png" alt="televisión">
                <h2>TV</h2>
                <p>Televisores LG</p>
                <p>Apple TV</p>
                <p>Samsung</p>
                <p>Dispositivos Android TV</p>
                <p>Amazon Fire TV</p>
            </div>
            <div class="computer">
                <img src="/static/img/computer.png" alt="ordenador">
                <h2>Ordenadores</h2>
                <p>Chrome OS</p>
                <p>MacOS</p>
                <p>Windows PC</p>
            </div>
            <div class="phone">
                <img src="/static/img/phone.png" alt="móvil">
                <h2>Móvil y Tablet</h2>
                <p>Tablets Amazon Fire</p>
                <p>Móviles y Tables Android</p>
                <p>iPhone & iPad</p>
            </div>
            <div class="console">
                <img src="/static/img/console.png" alt="consola">
                <h2>Videoconsolas</h2>
                <p>PS4</p>
                <p>PS5</p>
                <p>Xbox One</p>
                <p>Xbox Series X</p>
                <p>Xbox Series S</p>
            </div>
        </div>
    </div>

% include('footer')