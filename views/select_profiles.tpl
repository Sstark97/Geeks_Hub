<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selección de Perfil</title>
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
</head>
<body>
    <img class="profile_logo" src="/static/img/logo.png" alt="logo">
    <h1>¿Quién eres?</h1>

    <form action="/select_profile" method="post">
        <div class="form_container">

            <label for="profile">Selecciona un perfil</label>

            <div class="avatar">

            %if rows != []:
                %cont = 0
                %for row in rows:
                    <div>
                        <input type="radio" name="profile_code" id={{ f"profile_code{cont}" }} value="{{ row[0] }}">
                        <label for={{ f"profile_code{cont}" }} >
                            <img class="profile_image" src="{{ row[3] }}" alt="Avatar">
                        </label>
                        <p>{{ row[2] }}</p>
                    </div>
                    %cont += 1
                %end
            %end

            %if len(rows) != 5:
                <div>
                    <a href="/profiles"><img class="profile_image" src="/static/img/avatar/add.png" alt="Añadir"></a>
                    <p>Añadir</p>
                </div>
            %end
            
            </div>
            <button type="submit" class="btn" name="btn_continue">Continuar</button>
        </div>
    </form>
</body>
</html>