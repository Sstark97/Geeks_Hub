%include('header.tpl')
    <div class="div_search">
        <div class="input">
            <input type="text" name="search" placeholder="Buscar...">
        </div>
        <section class="content_search">
            %for row in rows_content:
                %if row[3] == 0 or row[3] == 1:
                    %if row[3] == 0:
                        <a href={{ f"/films/{row[0]}" }}>
                            <img src="{{row[4]}}" alt="{{row[1]}}">
                        </a>
                    %else:
                        <a href={{ f"/series/{row[0]}" }}>
                            <img src="{{row[4]}}" alt="{{row[1]}}">
                        </a>
                    %end
                %end
            %end
        </section>
    </div>

% include('nav.tpl')
    
    <footer style="display: none;">
% include('footer.tpl')