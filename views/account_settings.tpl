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
            <div class="input">
                {{ form.name.label }}
                {{ form.name }}
            </div>
            <div class="input">
                {{ form.surname.label }}
                {{ form.surname }}
            </div>
            <div class="input">
                {{ form.direction.label }}
                {{ form.direction }}
            </div>
            <div class="input">
                {{ form.password.label }}
                {{ form.password }}
            </div>
            <div class="input">
                {{ form.phone_number.label }}
                {{ form.phone_number }}
            </div>
            <div class="input">
                {{ form.suscription.label }}
                {{ form.suscription }}
            </div>
            <div class="button">
                {{ form.submit }}
                <button class="btn_cancel"><a href="/">Volver</a></button>     
            </div>
        </form>

        <h1 class="title">Cerrar Sesión</h3>
        <form method="POST" action="/account_settings">
            <div class="button">
                {{ form.logout }}
            </div>
        </form>
    </div>

    % include('nav.tpl')
% include('footer.tpl')