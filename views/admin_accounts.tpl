<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin/Accounts</title>
</head>
<body>
    
    <p><b>Las cuentas actuales son las siguientes:</b></p>
    <table border="1">
        <tr>
            <th>Correo</th>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th>Dirección</th>
            <th>Contraseña</th>
            <th>Teléfono</th>
            <th>Tipo Suscripción</th>
            <th>Acción</th>
        </tr>
        %for row in rows:
        <tr>
            %for col in row:
            <td>{{ col }}</td>
            %end
            <td>
                <form action="" method="GET">
                    <input type="submit" name="view" value="Mostrar">
                </form>
            </td>
        </tr>
        %end
    </table>

    <br>

    <button><a href="../register">Registrar una cuenta nueva</a></button>

</body>
</html>