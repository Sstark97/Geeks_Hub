%from config.local_storage import local_storage
<nav class="nav_user">
    <ul class="ul_user">
        <li>
            <a href="/home" aria-label="Inicio">
                <i class='bx bxs-home'></i>
            </a>
        </li>
        <li id="serie">
            <a href="/series" aria-label="Series">
                <i class='bx bxs-tv' ></i>
            </a>
        </li>
        <li id="movie">
            <a href="/films" aria-label="Películas">
                <i class='bx bxs-film' ></i>
            </a>
        </li>
        <li>
            <a href="/search" aria-label="Buscador">
                <i class='bx bxs-search-alt-2' ></i>
            </a>
        </li>
        <li>
            <input type="checkbox" id="check">
            <label for="check" class="hamburguer_menu">
                <img src="{{avatar}}" alt="avatar">
            </label>
            <ul class="hamburguer_nav">
                <li><a href="/select_profile" aria-label="Perfiles"><i class='bx bxs-user-account' ></i>Ir a Perfiles</a></li>
                <li class="hr"><hr></li>
                <li><a href="/account_settings" aria-label="Cuenta"><i class='bx bx-user' ></i>Cuenta</a></li>
                <li><a href="/favorites" aria-label="Favoritos"><i class='bx bxs-heart'></i>Favoritos</a></li>
                <li><a href="/history" aria-label="Historial"><i class='bx bx-history'></i>Historial</a></li>
                <li class="hr"><hr></li>
                <li><a onclick="logout()" aria-label="Cerrar Sesión"><i class='bx bx-log-out' ></i>Cerrar Sesión</a></li>
            </ul>
        </li>
    </ul>
</nav>