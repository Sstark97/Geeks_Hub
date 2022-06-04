        <footer>
            <ul class="icons">
                <li>
                    <a href="/" target="blank"><i class='bx bxl-facebook-circle'></i></a>
                    <a href="/" target="blank"><i class='bx bxl-twitter'></i></a>
                    <a href="/" target="blank"><i class='bx bxl-instagram-alt'></i></a>
                </li>
            </ul>
            <ul class="menu">
                <li><a href="/">Inicio</a></li>
                <li><a href="/">Contáctanos</a></li>
            </ul>
            <p>©2022 Geeks Hub | Todos los derechos reservados</p>
        </footer>

        <script>
            const element = document.querySelector(".content_list");

            element.addEventListener('wheel', (event) => {
            event.preventDefault();

                element.scrollBy({
                    left: event.deltaY < 0 ? -30 : 30,
                });
            });
        </script>
</body>
</html>
