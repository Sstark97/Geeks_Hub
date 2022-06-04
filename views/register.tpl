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
                <div class="edit_input">
                    {{ form.name }}
                    {{ form.name.label }}
                </div>
                <div class="edit_input">
                    {{ form.surname }}
                    {{ form.surname.label }}
                </div>
            </div>

            <div class="contain">
                <div class="edit_input">
                    {{ form.email }}
                    {{ form.email.label }}
                </div>
                <div class="edit_input">
                    {{ form.direction }}
                    {{ form.direction.label }}
                </div>
            </div>

            <div class="contain">
                <div class="edit_input">
                    {{ form.password }}
                    {{ form.password.label }}
                </div>
                <div class="edit_input">
                    {{ form.password_confirm }}
                    {{ form.password_confirm.label }}
                </div>
            </div>

            <div class="contain phone">
                <div class="edit_input">
                    {{ form.phone_number }}
                    {{ form.phone_number.label }}
                </div>
            </div>

            <div class="suscription">
                % cont = 1
                %for suscription in rows:
                    <div class="box">
                        <input type="radio" name="new_suscription" id={{ f"radio{cont}" }} value="{{ suscription[0] }}">
                        <label for={{ f"radio{cont}" }}>
                            <div class="{{suscription[0]}}">
                                <h1>{{suscription[0]}}</h1>
                            </div>
                            <p>Precio: {{suscription[1]}}</p>
                            <p>Calidad: {{suscription[2]}}</p>
                            <p>Número de dispositivos: {{suscription[3]}}</p>
                        </label>
                    </div>
                % cont += 1
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
