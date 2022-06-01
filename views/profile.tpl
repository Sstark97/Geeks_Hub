<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Creación de Perfil</title>
    <link rel="stylesheet" href="/static/css/global.css">
    <link rel="stylesheet" href="/static/css/form.css">
</head>
<body>
    <img class="profile_logo" src="/static/img/logo.png" alt="logo">
    <h1>Creación de Perfil</h1>
    <form method="POST" action="/profiles" autocomplete="off">
        <fieldset>
            <div class="input">
                {{ form.nickname.label }}
                {{ form.nickname }}
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
                <a href="/">
                    <input type="button" value="Cancelar"/>
                </a>
            </div>    
        </fieldset>
    </form>
</body>
</html>