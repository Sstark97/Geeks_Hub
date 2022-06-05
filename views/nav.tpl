%from config.local_storage import local_storage
<nav class="nav_user">
    <ul>
        <li>
            <a href="">
                <i class='bx bxs-home'></i>
            </a>
        </li>
        <li id="serie">
            <a href="">
                <i class='bx bxs-tv' ></i>
            </a>
        </li>
        <li id="movie">
            <a href="">
                <i class='bx bxs-film' ></i>
            </a>
        </li>
        <li>
            <a href="">
                <i class='bx bxs-search-alt-2' ></i>
            </a>
        </li>
        <li>
            <input type="checkbox" id="check">
            <label for="check" class="hamburguer_menu">
                <img src="{{avatar}}" alt="avatar">
            </label>
            <ul class="hamburguer_nav">
                <li><a href="/select_profile"><i class='bx bxs-user-account' ></i>Ir a Perfiles</a></li>
                <hr>
                <li><a href=""><i class='bx bx-user' ></i>Cuenta</a></li>
                <li><a href=""><i class='bx bxs-heart'></i>Favoritos</a></li>
                <li><a href=""><i class='bx bx-history'></i>Historial</a></li>
                <hr>
                <li><a onclick="logout()"><i class='bx bx-log-out' ></i>Cerrar Sesión</a></li>
            </ul>
        </li>
    </ul>
</nav>