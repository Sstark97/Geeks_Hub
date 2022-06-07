% include('header.tpl')
        <div class="container_settings">
            <h1 class="title">Configuración de Cuenta</h1>

            % if form.errors:
            <blockquote>
                <p>Hay errores en el formulario:</p>
                <ul>
                    % for field, errors in form.errors.items():
                    % for error in errors:
                    <li>{{field}}: {{error}}</li>
                    % end
                    % end
                </ul>
            </blockquote>
            % end

            <form method="POST" action="/account_settings">
                <fieldset class="account_settings">
                    <div class="input">
                        {{ form.name }}
                        {{ form.name.label }}
                    </div>
                    <div class="input">
                        {{ form.surname }}
                        {{ form.surname.label }}
                    </div>
                    <div class="input">
                        {{ form.password }}
                        {{ form.password.label }}
                    </div>
                    <div class="input">
                        {{ form.password_confirm }}
                        {{ form.password_confirm.label }}
                    </div>
                    <div class="input">
                        {{ form.phone_number }}
                        {{ form.phone_number.label }}
                    </div>
                    <div class="input">
                        {{ form.direction }}
                        {{ form.direction.label }}
                    </div>
                    <div class="selector">
                        {{ form.suscription }}
                        {{ form.suscription.label }}
                    </div>
                </fieldset>
                <div class="button">
                    {{ form.submit }}
                    <button class="btn_cancel"><a href="/">Cancelar</a></button>     
                </div>
            </form>

            <hr class="hr">

            %if rows_profile != []:
            <form action="/account_settings/profile" method="get">
                <h1 class="title">Configuración de Perfiles</h1>
                <div class="avatar">
                    %cont = 0
                    %for row_profile in rows_profile:
                        <div class="div-avatar">
                            <input type="radio" name="profile_code" id={{ f"profile_code{cont}" }} value="{{ row_profile[0] }}">
                            <label for={{ f"profile_code{cont}" }} class="lbl_img">
                                <img class="profile_image" src="{{ row_profile[3] }}" alt="Avatar">
                            </label>
                            <p>{{ row_profile[2] }}</p>
                        </div>
                        %cont += 1
                    %end
                </div>
                <div class="button">
                    <input type="submit" class="profile_submit" name="btn_continue" value="Continuar">
                </div>
            </form>
            %end

        % include('nav.tpl')
        
        </main>
        
        <!-- JQuery -->
        <script src="/static/js/jquery.js"></script>
        <!-- Script de Cerrar Sesión -->
        <script src="/static/js/logout.js"></script>
    </body>
</html>
