% include('header.tpl')

    <div class="slider">
        <ul>
            % for content in slider:
                <li>
                    <a href="/">
                        <h2>{{content[1]}}</h2>
                        <img src="/{{content[4]}}" alt="{{content[1]}}">
                    </a>
                </li>
            % end
        </ul>
    </div>

    <div class="">

    </div>

    % include('nav.tpl')
% include('footer.tpl')