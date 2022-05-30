<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
    <link rel="stylesheet" href="/static/css/profile.css">
</head>
<body>
    <h1>Profile</h1>
    <form method="POST" action="/profiles">
        <fieldset>
            <div class="nickname">
                {{ form.nickname.label }}
                {{ form.nickname }}
            </div>      
            <div class="avatar">
                % cont = 1
                % for avatar in rows:
                <div>
                    <input type="radio" name="avatar" id={{ f"radio{cont}" }} value="{{ avatar }}">
                    <label for={{ f"radio{cont}" }}>
                        <img src="{{ avatar }}" alt={{ f"avatar{cont}" }}>
                    </label>
                </div>
                % cont += 1
                % end 
            </div>
            <div>
                {{ form.btn_continue }}
            </div>   
            <div>
                {{ form.cancel}}
            </div>    
        </fieldset>
    </form>
</body>
</html>