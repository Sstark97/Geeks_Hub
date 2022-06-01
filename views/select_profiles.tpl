<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selección de Perfil</title>
    <link rel="stylesheet" href="/static/css/global.css">
    <link rel="stylesheet" href="/static/css/form.css">
</head>
<body>
    <img class="profile_logo" src="/static/img/logo.png" alt="logo">
    <h1>¿Quién eres?</h1>

    <form action="/select_profile" method="post">
        <div class="form_container">

            <label for="profile">Selecciona un perfil</label>

            <div class="avatar">
            %for row in rows:
                <div>
                    <img class="profile_image" src="{{ row[3] }}" alt="Avatar">
                    <p>{{ row[2] }}</p>
                </div>
            %end
                <div>
                    <a href="/profiles"><img class="profile_image" src="/static/img/avatar/add.png" alt="Añadir"></a>
                    <p>Añadir</p>
                </div>
            </div>
            <div class="button">
                <a href="/">
                    <input id="btn_select" name="btn_select" type="submit" value="Seleccionar">
                </a>
            </div>
        </div>
    </form>
</body>
</html>