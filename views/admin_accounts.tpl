%include('admin_header.tpl',title='Cuentas')
    <table class="account">
    <thead>
        <tr>
            %for field in fields:
                <th>{{field}}</th>
            %end
            <th>Acción</th>
        </tr>
    </thead>
        %for row in rows:
        <tr>
            %for col in row:
            <td>{{ col }}</td>
            %end
            <td id="only_view">
                <form action="/admin/accounts/{{row[0]}}" method="GET">
                    <button class="btn_view" type="submit" name="view">
                        <i class='bx bxs-low-vision icons'></i>
                    </button>
                </form>
            </td>
        </tr>
        %end
    </table>
</body>
</html>