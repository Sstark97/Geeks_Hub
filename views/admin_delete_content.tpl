%include('admin_header.tpl',title=title)
    <p>Borrar {{content}} con Codigo = {{cod}}</p>
    <form action="/admin/{{uri}}/delete/{{cod}}" method="POST">
      <p>Hac click para confirmar que deseas eliminar la {{content}}: </p>
      <p><b>{{content_title[0]}}</b></p>
      <div>{{form.delete}}{{form.cancel}}</div>
    </form>   
</body>
</html>