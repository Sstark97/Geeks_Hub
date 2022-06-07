<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Creación de Perfil</title>

    <!-- Estilos -->

    <!-- Estilos Globales -->
    
    <link rel="stylesheet" href="/static/css/global/global.css">
    <link rel="stylesheet" href="/static/css/global/global_tablet.css"
        media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/global/global_desktop.css" media="only screen and (min-width: 992px)">

    <!-- Estilos de Formularios -->
    
    <link rel="stylesheet" href="/static/css/form/form.css">
    <link rel="stylesheet" href="/static/css/form/form_tablet.css" media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/form/form_desktop.css" media="only screen and (min-width: 992px)">

</head>
<body>
    <img class="profile_logo" src="/static/img/logo.png" alt="logo">
    <h1>Creación de Perfil</h1>
    <form method="POST" action="/profiles" autocomplete="off">
        <fieldset>
            <div class="edit_input">
                {{ form.nickname }}
                {{ form.nickname.label }}
            </div>    
            <div class="input"><label for="avatar">Avatar</label></div>
            <div class="avatar">
                % cont = 1
                % for avatar in rows:
                <div>
                    <input type="radio" name="avatar" id={{ f"radio{cont}" }} value="{{ avatar }}">
                    <label for={{ f"radio{cont}" }}>
                        <img src="{{ avatar }}" alt={{ f"avatar{cont}" }}>
                    </label>
                </div>
                % cont += 1
                % end 
            </div>
            <div class="button">
                {{ form.btn_continue }}
                <a href="/select_profile">
                    <input type="button" value="Cancelar"/>
                </a>
            </div>    
        </fieldset>
    </form>
</body>
</html>