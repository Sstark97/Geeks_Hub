<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
</head>
<body>
    <p>Borrar {{content}} con Codigo = {{cod}}</p>
    <form action="/admin/{{str.lower(content)}}s/delete/{{cod}}" method="POST">
      <p>Hac click para confirmar que deseas eliminar la {{content}}: </p>
      <p><b>{{content_title[0]}}</b></p>
      <div>{{form.delete}}{{form.cancel}}</div>
    </form>   
</body>
</html>