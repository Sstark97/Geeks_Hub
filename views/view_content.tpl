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
                % if content_type == "series":
                    <h3 class="bg_content">{{content.get("Titulo")}} T{{content.get("N_Temporada")}}</h3>
                % else:
                    <h3 class="bg_content">{{content.get("Titulo")}}</h3>
                % end
                <p>Dirigido por {{content.get("Director")}}</p>
            </div>
        </div>

        <div id="trailer">
            <iframe src="{{content.get('Trailer')}}" title="YouTube video player" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
            </iframe>
        </div>

        <div id="buttons">
            %cod = content.get("Cod_Contenido")
            <form method="POST" action="{{ f'/{content_type}/{cod}' }}">
                %if favorite:
                    <button type="submit" name="favorite_btn" value="favorite_action"><i class="bi bi-heart-fill heart"></i></button>
                %else:
                    <button type="submit" name="favorite_btn" value="favorite_action"><i class="bi bi-heart heart"></i></button>
                %end
            </form>

            <form method="POST" action="{{ f'/{content_type}/{cod}' }}">
                %if history:
                    <button type="submit" name="history_btn" value="history_action"><i class="bi bi-eye-fill eye"></i></button>
                %else:
                    <button type="submit" name="history_btn" value="history_action"><i class="bi bi-eye eye"></i></button>
                %end
            </form>

        </div>

        % if content_type == "series":
            <div id="seasons">
                <select name="seasons" id="select_seasons" required onchange="abrirPopUp(this)">
                    <option value="{{cod}}">Seleccione temporada</option>
                    % cont = 1
                    % for season in seasons:
                        <option value="{{season}}">Temporada {{cont}}</option>
                        % cont += 1
                    % end
                </select>
            </div>
        % end

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
            % if content_type == "films":
                <div>
                    <h4>Duración</h4>
                    <p>{{duration}}</p>
                </div>
            % else:
                <div>
                    <h4>Capítulos</h4>
                    <p>{{content.get('Capitulos')}}</p>
                </div>
            % end
            <div>
                <h4>Estreno</h4>
                <p>{{content.get('Fecha_Publicacion')}}</p>
            </div>
            <div>
                <h4>Género</h4>
                <p>{{content.get('Genero')}}</p>
            </div>
            <div>
                <h4>Calificación</h4>
                <p>{{content.get('Calificacion_Edad')}}</p>
            </div>
        </div>
    </main>
    % include('nav.tpl')
    <footer style="display: none;">
%include("footer.tpl")