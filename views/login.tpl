<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inicio de Sesión</title>
    <link rel="stylesheet" href="/static/css/global.css">
    <link rel="stylesheet" href="/static/css/form.css">
</head>
<body>
    <img src="/static/img/logo.png" alt="logo">
    <h1>Inicie Sesión</h1>

    <form method="POST" action="/login" autocomplete="off">
        <fieldset>
            <div class="edit_input">
                {{ form.email }}
                {{ form.email.label }}
            </div>
            <div class="edit_input">
                {{ form.password }}
                {{ form.password.label }}
            </div>
            <div class="button">
                <a href="/select_profiles">
                    {{ form.btn_continue }}
                </a>
            </div>
        </fieldset>
        <div class="register">
            <p>Si aún no estás registrado,&nbsp</p>
            <a href="/register">
                <input type="button" value="regístrate aquí"/>
            </a>
        </div>

    </form>
</body>
</html>