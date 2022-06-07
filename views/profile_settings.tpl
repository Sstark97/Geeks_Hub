% include('header.tpl')

<div class="container_settings">
    <h1 class="title">Configuración de Perfil</h1>
    <form method="POST" action="/account_settings/profile" autocomplete="off">
        <fieldset class="account_settings">
            <div class="input">
                {{ form.nickname }}
                {{ form.nickname.label }}
            </div>
            <h1 class="title">Avatar</h1>
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
                    <input type="button" value="Cancelar" />
                </a>
            </div>
        </fieldset>

    </form>
</div>

% include('nav.tpl')
% include('footer.tpl')