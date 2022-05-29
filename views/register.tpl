<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>

    <h1>Formulario de registro</h1>
    % if form.errors:
    <blockquote>
        <p>Hay errores en el formulario: </p>
        <ul>
        % for field, errors in form.errors.items():
            % for error in errors:
            <li>{{field}}: {{error}}</li>
            % end
        % end
        </ul>
    </blockquote>
    % end

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
                <button style="width:70px">
                    <a href="/" style="text-decoration:none; color:black">Cancelar</a>
                </button>
            </div>       
        </fieldset>
    </form>
</body>
</html>
