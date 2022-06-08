<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inicio</title>

    <!-- Estilos -->

    <!-- Estilos Globales -->
    
    <link rel="stylesheet" href="/static/css/global/global.css">
    <link rel="stylesheet" href="/static/css/global/global_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/global/global_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos de la Landing Page -->

    <link rel="stylesheet" href="/static/css/landing/landing.css">
    <link rel="stylesheet" href="/static/css/landing/landing_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/landing/landing_desktop.css" media="only screen and (min-width: 992px)">

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
                <p>Todas las películas y series que desees, y mucho más.
                    Los mayores éxitos de taquilla, las historias más rompedoras y los clásicos inolvidables que nos han convertido en quienes somos.</p>
            </div>
        </div>
        <div class="content">
            <div class="cuadro"></div>
            <div class="info">
                <h2>Disfruta de Geeks Hub en compañía</h2>
                <ul>
                    <li>Noches de series y películas con GroupWatch. Para invitar o que te inviten a GroupWatch, es necesario tener una suscripción.</li>
                    <li>Disfruta de Geeks Hub en compañía, aunque estéis en diferentes lugares.</li>
                    <li>Visualización simultánea con hasta 6 personas.</li>
                    <li>Pausad, rebobinad y reaccionad juntos</li>
                    <li>Fácil de configurar y compartir.</li>
                </ul>
            </div>
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