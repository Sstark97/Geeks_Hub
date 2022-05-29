%include('admin_header.tpl',title=title)
    <p><b>Las {{title}} actuales son las siguientes:</b></p>
    <button><a href="/admin/{{content}}/new">Añadir una {{str.capitalize(title)}}</a></button>
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
                <form action="/admin/{{content}}/edit/{{row[0]}}" method="GET">
                    <input type="submit" name="save" value="Editar">
                </form>
            </td>
            <td>
                <form action="/admin/{{content}}/delete/{{row[0]}}" method="GET">
                    <input type="submit" name="delete" value="Borrar">
                </form>
            </td>
            <td>
                <form action="/admin/{{content}}/{{row[0]}}" method="GET">
                    <input type="submit" name="view" value="Ver">
                </form>
            </td>
        </tr>
        %end
    </table>
    
</body>
</html>