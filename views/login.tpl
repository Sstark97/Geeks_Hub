<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Formulario de registro</h1>
    <form method="POST" action="/register">
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
                {{ form.password_confirm.label }}:
                {{ form.password_confirm }}
            </div>
            <div>
                {{ form.accept_rules.label }}:
                {{ form.accept_rules }}
            </div>
            <div>
                {{ form.save }}
            </div>   
            <div>
                {{ form.cancel}}
            </div>    
        </fieldset>
    </form>
</body>
</html>