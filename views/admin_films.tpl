<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin/{{title}}</title>
</head>
<body>

    <p><b>Las {{title}} actuales son las siguientes:</b></p>
    <table border="1">
        <tr>
            <th>{{cod}}</th>
            <th>{{content_title}}</th>
            <th>{{content_third_row}}</th>
            <th colspan="3">Acciones</th>
        </tr>
        %for row in rows:
        <tr>
            %for col in row:
            <td>{{col}}</td>
            %end
            <td>
                <form action="/edit/{{row[0]}}" method="GET">
                    <input type="submit" name="save" value="Editar">
                </form>
            </td>
            <td>
                <form action="/delete/{{row[0]}}" method="GET">
                    <input type="submit" name="delete" value="Borrar">
                </form>
            </td>
        </tr>
        %end
    </table>
    
</body>
</html>