%include('admin_header.tpl',title=title)
    <a class="back" href="/admin/{{content_type}}">
        <i class='bx bx-left-arrow-alt icons'></i>
        <p>Volver</p>
    </a>
    <main class="content_container">

        <div id="content_title">
            <h3 class="bg_content">{{content.get("Titulo")}}</h3>
        </div>

        <div class="image">
            <img src="/{{content.get('Portada')}}" alt="{{content.get('Titulo')}}">
            <iframe src="{{content.get('Trailer')}}" title="YouTube video player" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
            </iframe>
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