<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{content[0][2]}}</title>
</head>
<body>
    <h2>{{content[0][2]}}</h2>
    <button><a href="/admin/{{content_type}}">Volver</a></button>
    <table border="1">
        <tr>
            %for field in fields:
                <th>{{field}}</th>
            %end
        </tr>

        %for row in content:
        <tr>
            %for col in row:
                %if row.index(col) == img_col:
                    <td>
                        <img src="{{col}}" width="300px" height="100%"/>
                    </td>
                %else:
                    <td>{{col}}</td>
                %end
            %end
        </tr>
        %end
    </table>
    
</body>
</html>