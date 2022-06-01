%include('admin_header.tpl',title=title)
    <div class="create">
        <a href="/admin/{{content}}/new">Añadir una {{str.capitalize(title)[0:len(title) - 1]}}</a>
    </div>
    <table class="{{class_content}}">
        <thead>
            <tr>
                <th>{{cod}}</th>
                <th>{{content_title}}</th>
                <th>{{content_third_row}}</th>
                <th colspan="3">Acciones</th>
            </tr>
        </thead>
        %for row in rows:
        <tr>
            %for col in row:
            <td>{{col}}</td>
            %end
            <td class="td_flex">
                <form action="/admin/{{content}}/{{row[0]}}" method="GET">
                    <button class="btn_view" type="submit" name="view">
                        <i class='bx bxs-low-vision icons' ></i>
                    </button>
                </form>
                <form action="/admin/{{content}}/edit/{{row[0]}}" method="GET">
                    <button class="btn_edit" type="submit" name="save">
                        <i class='bx bxs-edit-alt icons'></i>
                    </button>
                </form>
                <form action="/admin/{{content}}/delete/{{row[0]}}" method="GET">
                    <button class="btn_delete" type="submit" name="delete">
                        <i class='bx bxs-trash icons'></i>
                    </button>
                </form>
            </td>
        </tr>
        %end
    </table>
    
</body>
</html>