% include('header.tpl')
        <div class="container_settings">
            <h1 class="title">Configuración de Cuenta</h1>

            % if form.errors:
            <blockquote>
                <ul>
                    % for field, errors in form.errors.items():
                        % for error in errors:
                            <li>{{field}}: {{error}}</li>
                        % end
                    % end
                </ul>
            </blockquote>
            % end

            <form method="POST" action="/account_settings/delete_account">
                <fieldset class="account_settings">
                    <div class="input">
                        {{ form.email }}
                        {{ form.email.label }}
                    </div>
                </fieldset>
                <div class="button">
                    {{ form.delete }}
                    <button class="btn_cancel"><a href="/">Cancelar</a></button>     
                </div>
            </form>

    % include('nav.tpl')

    </main>

    <!-- JQuery -->
    <script src="/static/js/jquery.js"></script>
    <!-- Script de Cerrar Sesión -->
    <script src="/static/js/logout.js"></script>

    <!-- Script para leer el Dark Mode -->
    <script src="/static/js/load_dark_mode.js"></script>
    </body>

    </html>