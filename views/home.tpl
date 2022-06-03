% include('header.tpl')

    <div class="slider">
        <ul>
            % for content in slider:
                <li>
                    <a href="/">
                        % path = ""
                        %if content[0].find("S") != -1:
                            % path += content[4].replace("series","carrousel")
                        %else:
                            %path += content[4].replace("movies","carrousel")
                        %end
                        <h2>{{content[1]}}</h2>
                        <img src="/{{path}}" alt="{{content[1]}}">
                    </a>
                </li>
            % end
        </ul>
    </div>

    <h3>Favoritos</h3>

    <div class="content_list">
        %for favorite in favorites:
                <img src="{{favorite[0]}}" alt="{{favorite[2]}}">
        %end
    </div>

    <h3>Top 10</h3>

    <div class="content_list">
        %for top in top_ten:
            <img src="{{top[4]}}" alt="{{top[1]}}">
        %end
    </div>

    % include('nav.tpl')
% include('footer.tpl')