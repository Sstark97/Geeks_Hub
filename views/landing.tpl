<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Página Inicial de la Web">
    <meta name="keywords" content="geeks hub, streaming, películas, series">
    <meta name="author" content="Sara Cabrera, Aitor Santana, Javier Martel"/>
    <meta name="copyright" content="Geeks Hub"/>
    <meta http-equiv="expires" content="43200"/>

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

    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">

</head>

<body>
    <main class="main">
        <section class="background">
            <article class="button_login">
                <a href="/login">
                    <button class="login">Iniciar Sesión</button>
                </a>
            </article>
            <article class="logo">
                <img src="/static/img/logo.png" alt="logo">
                <p>Todas las películas y series que desees, y mucho más.
                    Los mayores éxitos de taquilla, las historias más rompedoras y los clásicos inolvidables que nos han convertido en quienes somos.</p>
            </article>
        </section>
        <section class="content">
            <div class="cuadro"></div>
            <article class="info">
                <h2>Disfruta de Geeks Hub en compañía</h2>
                <ul>
                    <li>Noches de series y películas con GroupWatch. Para invitar o que te inviten a GroupWatch, es necesario tener una suscripción.</li>
                    <li>Disfruta de Geeks Hub en compañía, aunque estéis en diferentes lugares.</li>
                    <li>Visualización simultánea con hasta 6 personas.</li>
                    <li>Pausad, rebobinad y reaccionad juntos</li>
                    <li>Fácil de configurar y compartir.</li>
                </ul>
            </article>
        </section>
        <div class="button_submit">
            <a href="/register">
                <input class="submit" type="button" value="Suscríbete ahora">
            </a>
        </div>
        <section class="devices">
            <article class="television">
                <img src="/static/img/television.png" alt="televisión">
                <h2>TV</h2>
                <p>Televisores LG</p>
                <p>Apple TV</p>
                <p>Samsung</p>
                <p>Dispositivos Android TV</p>
                <p>Amazon Fire TV</p>
            </article>
            <article class="computer">
                <img src="/static/img/computer.png" alt="ordenador">
                <h2>Ordenadores</h2>
                <p>Chrome OS</p>
                <p>MacOS</p>
                <p>Windows PC</p>
            </article>
            <article class="phone">
                <img src="/static/img/phone.png" alt="móvil">
                <h2>Móvil y Tablet</h2>
                <p>Tablets Amazon Fire</p>
                <p>Móviles y Tables Android</p>
                <p>iPhone & iPad</p>
            </article>
            <article class="console">
                <img src="/static/img/console.png" alt="consola">
                <h2>Videoconsolas</h2>
                <p>PS4</p>
                <p>PS5</p>
                <p>Xbox One</p>
                <p>Xbox Series X</p>
                <p>Xbox Series S</p>
            </article>
        </section>
    </main>
    <footer>
% include('footer')