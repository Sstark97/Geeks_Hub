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

    <h3>Favoritos</h3>

    <div class="content_list">
        <ul>
            %for favorite in favorites:
                <li>
                    <a href="/">
                        <img src="{{favorite[0]}}" alt="{{favorite[2]}}">
                    </a>
                </li>
            %end
        </ul>
    </div>

    <h3>Top 10</h3>

    <div class="content_list">
        <ul>
            %for top in top_ten:
                <li>
                    <a href="/">
                        <img src="{{top[4]}}" alt="{{top[1]}}">
                    </a>
                </li>
            %end
        </ul>
    </div>

    % include('nav.tpl')
% include('footer.tpl')