% include('header.tpl')

<div id="container">
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

    <section class="content_list">
        %for favorite in favorites:
            <a href="/">
                <img src="{{favorite[0]}}" alt="{{favorite[2]}}">
                <div class="video">
                    <div class="caja"></div>
                    <!-- <iframe src="{{favorite[1]}}" frameborder="0"></iframe> -->
                </div>
            </a>
        %end
    </section>

    <h3>Top 10</h3>

    <section class="content_list">
        %for top in top_ten:
        <a href="/">
            <img src="{{top[4]}}" alt="{{top[1]}}">
            <div class="video">
                <div class="caja"></div>
                <!-- <iframe src="{{top[5]}}" frameborder="0"></iframe> -->
            </div>
        </a>
        %end
    </section>    

    %for key, value in all_content.items():

    <h3>{{key}}</h3>

    <section class="content_list">
        %for content_genre in value:
        <a href="/">
            <img src="{{content_genre[4]}}" alt="{{content_genre[1]}}">
            <div class="video">
                <!-- <iframe src="{{content_genre[5]}}" frameborder="0"></iframe> -->
            </div>
        </a>
        %end
    </section>    
    %end
</div>

    % include('nav.tpl')
% include('footer.tpl')