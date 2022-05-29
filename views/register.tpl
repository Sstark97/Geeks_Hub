<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <form method="POST" action="/register">
        <fieldset>
            <div>
                {{ form.name.label }}:
                {{ form.name }}
            </div>
            <div>
                {{ form.surname.label }}:
                {{ form.surname }}
            </div>
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
                {{ form.direction.label }}:
                {{ form.direction }}
            </div>
            <div>
                {{ form.phone_number.label }}:
                {{ form.phone_number }}
            </div>
            <div>
                {{ form.suscription.label }}:
                {{ form.suscription }}
            </div>
            <div>
                {{ form.register }}
            </div>       
            <div>
                {{ form.cancel }}
            </div>       
        </fieldset>
    </form>
</body>
</html>
