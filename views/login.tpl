<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>

    <link rel="stylesheet" href="/static/css/form.css">
</head>
<body>
    <img src="/static/img/logo.png" alt="logo">
    <h1>Inicie Sesión</h1>
    <form method="POST" action="/login" autocomplete="off">
        <fieldset>
            <div class="input">
                {{ form.email.label }}
                {{ form.email }}
            </div>
            <div class="input">
                {{ form.password.label }}
                {{ form.password }}
            </div>
            <div class="button">
                {{ form.btn_continue }}
            </div>
        </fieldset>
        <a class="register" href="/">
            <p>Si aún no estás registrado,&nbsp</p>
            <input type="button" value="regístrate aquí"/>
        </a>
    </form>
</body>
</html>