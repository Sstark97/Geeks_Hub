%include('admin_header.tpl',title='Cuenta')
    <div class="back">
        <a href="/admin/{{content_type}}">
            <i class='bx bx-left-arrow-alt icons'></i>
            <p>Volver</p>
        </a>
    </div>
    <table class="{{class_content}}">
        <thead>
            <tr>
                <th>Correo</th>
                <th>Nombre</th>
                <th>Apellidos</th>
                <th>Dirección</th>
                <th>Teléfono</th>
                <th>Tipo Suscripción</th>
                <th>Número de Perfiles</th>
            </tr>
        </thead>
        %for row in rows:
        <tr>
            %for col in row:
                %if row.index(col) != 4:
                <td>{{ col }}</td>
                %end
            %end
            <td>{{num_profiles}}</td>
        </tr>
        %end
    </table>

</body>
</html>