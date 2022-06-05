% include('header.tpl')
    <div id="container-settings">
        <h1 class="title">Configuración de Cuenta</h1>
        <!-- <br>
        <h3>Datos actuales de la Cuenta</h3>
        <br>
            %for index in range(len(rows)):
                <div class="row">
                    %for second_index in range(len(rows[index])-1):
                        <div>
                            {{ fields[second_index] }}
                            %if second_index >= 4:
                                {{ rows[index][second_index+1] }}
                            %else:
                                {{ rows[index][second_index] }}
                        </div>
                    %end
                </div>
            %end
        <br>
        <h3>Modificar datos de la Cuenta</h3>
        <br> -->
        <form method="POST" action="/account_settings">
            <fieldset id="fieldset">
                <div class="input">
                    {{ form.name.label }}
                    {{ form.name }}
                </div>
                <div class="input">
                    {{ form.surname.label }}
                    {{ form.surname }}
                </div>
                <div class="input">
                    {{ form.password.label }}
                    {{ form.password }}
                </div>
                <div class="input">
                    {{ form.password_confirm.label }}
                    {{ form.password_confirm }}
                </div>
                <div class="input">
                    {{ form.phone_number.label }}
                    {{ form.phone_number }}
                </div>
                <div class="input">
                    {{ form.direction.label }}
                    {{ form.direction }}
                </div>
                <div class="input">
                    {{ form.suscription.label }}
                    {{ form.suscription }}
                </div>
            </fieldset>
            <div class="button">
                {{ form.submit }}
                <button class="btn_cancel"><a href="/">Volver</a></button>     
            </div>
        </form>

        <hr class="hr">

        %if rows_profile != []:
        <form action="/account_settings/profile" method="post">
            <h1 class="title">Configuración de Perfiles</h1>
            <div class="avatar">
                %for row_profile in rows_profile:
                    <div>
                        <button id="avatar-btn" type="submit">
                            <img class="profile_image" src="{{ row_profile[3] }}" alt="Avatar">
                        </button>
                        <p>{{ row_profile[2] }}</p>
                        <input type="hidden" name="profile_code" value="{{ row_profile[0] }}">
                    </div>
                %end
            </div>
        </form>
        %end

    % include('nav.tpl')
% include('footer.tpl')
