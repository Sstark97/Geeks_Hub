<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
</head>
<body>
    <h1>Profile</h1>
    <form method="POST" action="/profiles">
        <fieldset>
            <div>
                {{ form.nickname.label }}:
                {{ form.nickname }}
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