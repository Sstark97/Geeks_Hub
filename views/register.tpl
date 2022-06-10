<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Página para registrarse en la Web">
    <meta name="keywords" content="geeks hub, streaming, películas, series">
    <meta name="author" content="Sara Cabrera, Aitor Santana, Javier Martel"/>
    <meta name="copyright" content="Geeks Hub"/>
    <meta http-equiv="expires" content="43200"/>

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
    
    <!-- Estilos de los Errores -->
    
    <link rel="stylesheet" href="/static/css/errors/erros.css">
    <link rel="stylesheet" href="/static/css/errors/errors_tablet.css"
    media="only screen and (min-width: 768px) and (max-width: 992px)">
    <link rel="stylesheet" href="/static/css/errors/errors_desktop.css" media="only screen and (min-width: 992px)">
    
    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">

    <title>Registro</title>

</head>
<body>
    <img src="/static/img/logo.png" alt="logo">
    <h1>Formulario de registro</h1>
    % if len(error) > 0:
    <blockquote>
        <ul>
            <li>{{error}}</li>
        </ul>
    </blockquote>   
    % end
    
    % if form.errors:
    <blockquote>
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
                        <input class="hidden" type="radio" name="new_suscription" id={{ f"radio{cont}" }} value="{{ suscription[0]}}" tabindex="0">
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
                <a href="/profiles" tabindex="-1">
                    {{ form.register }}
                </a>
            </div>         
        </fieldset>
    </form>
</body>
</html>
