%include('admin_header.tpl',title='Cuenta')
    <p><b>Los datos de la cuenta seleccionada son los siguientes: </b></p>
    <table border="1">
        <tr>
            <th>Correo</th>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th>Dirección</th>
            <th>Contraseña</th>
            <th>Teléfono</th>
            <th>Tipo Suscripción</th>
        </tr>
        %for row in rows:
        <tr>
            %for col in row:
            <td>{{ col }}</td>
            %end
        </tr>
        %end
    </table>

    <br>

    <button><a href="/admin/accounts">Volver atrás</a></button>

</body>
</html>