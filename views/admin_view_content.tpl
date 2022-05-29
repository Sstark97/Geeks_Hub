%include('admin_header.tpl',title=title)
    <h2>{{title}}</h2>
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