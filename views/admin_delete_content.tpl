%include('admin_header.tpl',title=title)
    <form class="delete_form" action="/admin/{{uri}}/delete/{{cod}}" method="POST">
      <div>
        <h2>{{content_title[0]}}</h2>
        <p>Hac click para confirmar que deseas eliminar la {{content}} </p>
      </div>
      <div class="btn_group">{{form.delete}}{{form.cancel}}</div>
    </form>   
</body>
</html>