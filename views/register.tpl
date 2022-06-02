<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>

    <!-- Estilos -->

    <link rel="stylesheet" href="/static/css/global.css">
    <link rel="stylesheet" href="/static/css/form.css">
</head>
<body>
    <img src="/static/img/logo.png" alt="logo">
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

    <form method="POST" action="/register" autocomplete="off">
        <fieldset>
            <div class="contain">
                <div class="input">
                    {{ form.name.label }}
                    {{ form.name }}
                </div>
                <div class="input">
                    {{ form.surname.label }}
                    {{ form.surname }}
                </div>
            </div>

            <div class="contain">
                <div class="input">
                    {{ form.email.label }}
                    {{ form.email }}
                </div>
                <div class="input">
                    {{ form.direction.label }}
                    {{ form.direction }}
                </div>
            </div>

            <div class="contain">
                <div class="input">
                    {{ form.password.label }}
                    {{ form.password }}
                </div>
                <div class="input">
                    {{ form.password_confirm.label }}
                    {{ form.password_confirm }}
                </div>
            </div>

            <div class="contain">
                <div class="input">
                    {{ form.phone_number.label }}
                    {{ form.phone_number }}
                </div>
            </div>

            <div class="suscription">
                %for suscription in suscriptions:
                    <div class="box">
                        <div class="info">
                            <div class="{{suscription[0]}}">
                                <h1>{{suscription[0]}}</h1>
                            </div>
                            <p>Precio: {{suscription[1]}}</p>
                            <p>Calidad: {{suscription[2]}}</p>
                            <p>Número de dispositivos: {{suscription[3]}}</p>
                        </div>
                    </div>
                %end
            </div>

            <div class="button">
                <a href="/profiles">
                    {{ form.register }}
                </a>
            </div>         
        </fieldset>
    </form>
</body>
</html>
