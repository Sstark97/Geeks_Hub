<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST" action="/login">
        <fieldset>
            <div>
                {{ form.email.label }}:
                {{ form.email }}
            </div>
            <div>
                {{ form.password.label }}:
                {{ form.password }}
            </div>
            <div>
                {{ form.btn_continue }}
            </div>   
            <div>
                {{ form.cancel}}
            </div>    
        </fieldset>
        <a href="/">
            <input type="button" value="Registrate aquí"/>
        </a>
    </form>
</body>
</html>