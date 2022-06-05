% include('header.tpl')
    <div class="back">
        <a href="/home">
            <i class='bx bx-left-arrow-alt icons'></i>
            <p>Volver</p>
        </a>
    </div>
    <main class="content_container">

        <div id="content_title">
            <img src="/{{content.get('Portada')}}" alt="{{content.get('Titulo')}}">
            <div class="title">
                <h3 class="bg_content">{{content.get("Titulo")}}</h3>
                <p>Dirigido por {{content.get("Director")}}</p>
            </div>
        </div>

        <div id="trailer">
            <iframe src="{{content.get('Trailer')}}" title="YouTube video player" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
            </iframe>
        </div>

        <div id="sinopsis">
            <div class="title">
                <h3>Sinopsis</h3>
                <div class="score">
                    <i class='bx bxs-star'></i>
                    <p>{{content.get('Puntuacion_Media')}}</p>
                </div>
            </div>
            <p>{{content.get('Sinopsis')}}</p>
        </div>

        <div id="other_content">
            <div>
                <h4>Duración</h4>
                <p>{{duration}}</p>
            </div>
        </div>

        <div id="content_info">
            <ul>
                %for key, value in content.items():
                    %if key != "Titulo" and key != "Portada" and key != "Trailer" and key != "Sinopsis":
                        <li>
                            <span class="content_info_title">{{key}}:</span>
                            <span class="content_info_value">{{value}}</span>
                        </li>
                    %end
                %end
            </ul>
        </div>

        <div id="sinopsis">
            <span class="content_info_title">Sinopsis:</span>
            <span class="content_info_value">{{content.get("Sinopsis")}}</span>
        </div>

    </main>
</body>
</html>