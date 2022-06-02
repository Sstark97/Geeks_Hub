<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selección de Perfil</title>
    <link rel="stylesheet" href="/static/css/global.css">
    <link rel="stylesheet" href="/static/css/form.css">
    <!-- Iconos -->
    <link href='https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
    <img class="profile_logo" src="/static/img/logo.png" alt="logo">
    <h1>¿Quién eres?</h1>

    <form action="/select_profile" method="post">
        <div class="form_container">

            <label for="profile">Selecciona un perfil</label>

            <div class="avatar">

            %if rows != []:
                %for row in rows:
                    <div>
                        <button id="avatar-btn" type="submit">
                            <img class="profile_image" src="{{ row[3] }}" alt="Avatar">
                        </button>
                        <p>{{ row[2] }}</p>
                        <input type="hidden" name="profile_code" value="{{ row[0] }}">
                    </div>
                %end
            %end

            %if len(rows) != 5:
                <div>
                    <!-- <a href="/profiles" class="a-icon"><i class='bx bx-plus icon-select'></i></a> -->
                    <a href="/profiles"><img class="profile_image" src="/static/img/avatar/add.png" alt="Añadir"></a>
                    <p>Añadir</p>
                </div>
            %end
            
            </div>
        </div>
    </form>
</body>
</html>