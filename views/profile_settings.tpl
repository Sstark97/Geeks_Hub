% include('header.tpl')

    <div class="container-settings">
        <h1 class="title">Configuración de Perfil</h1>
        <form method="POST" action="/account_settings/profile" autocomplete="off">
                <div class="input">
                    {{ form.nickname.label }}
                    {{ form.nickname }}
                </div>    
                <div class="input"><label for="avatar">Avatar</label></div>
                <div class="avatar">
                    % cont = 1
                    % for avatar_profile in rows:
                    <div>
                        <input type="radio" name="avatar" id={{ f"radio{cont}" }} value="{{ avatar_profile }}">
                        <label for={{ f"radio{cont}" }}>
                            <img src="{{ avatar_profile }}" alt={{ f"avatar_profile{cont}" }}>
                        </label>
                    </div>
                    % cont += 1
                    % end 
                </div>
                <input type="hidden" name="profile_code" value="{{ profile_code }}">
                <div class="button">
                    {{ form.btn_continue }}
                    <a href="/account_settings">
                        <input type="button" value="Cancelar"/>
                    </a>
                </div>    
        </form>
    </div>

    % include('nav.tpl')
% include('footer.tpl')
