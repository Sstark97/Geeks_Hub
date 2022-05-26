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
                {{ form.nickname.label }}:
                {{ form.nickname }}
            </div>
            <div class="avatar">
                <div>
                    <input type="radio" name="avatar" id="check1" value="/static/img/avatar/avatar1.png">
                    <label for="check1">
                        <img src="/static/img/avatar/avatar1.png" alt="avatar1">
                    </label>
                </div>
                <div>
                    <input type="radio" name="avatar" id="check2" value="/static/img/avatar/avatar2.png">
                    <label for="check2">
                        <img src="/static/img/avatar/avatar2.png" alt="avatar2">
                    </label>
                </div>
                <div>
                    <input type="radio" name="avatar" id="check3" value="/static/img/avatar/avatar3.png">
                    <label for="check3">
                        <img src="/static/img/avatar/avatar3.png" alt="avatar3">
                    </label>
                </div>
                <div>
                    <input type="radio" name="avatar" id="check4" value="/static/img/avatar/avatar4.png">
                    <label for="check4">
                        <img src="/static/img/avatar/avatar4.png" alt="avatar4">
                    </label>
                </div>
                <div>
                    <input type="radio" name="avatar" id="check5" value="/static/img/avatar/avatar5.png">
                    <label for="check5">
                        <img src="/static/img/avatar/avatar5.png" alt="avatar5">
                    </label>
                </div>
                <div>
                    <input type="radio" name="avatar" id="check6" value="/static/img/avatar/avatar6.png">
                    <label for="check6">
                        <img src="/static/img/avatar/avatar6.png" alt="avatar6">
                    </label>
                </div>
                <div>
                    <input type="radio" name="avatar" id="check7" value="/static/img/avatar/avatar7.png">
                    <label for="check7">
                        <img src="/static/img/avatar/avatar7.png" alt="avatar7">
                    </label>
                </div>
                <div>
                    <input type="radio" name="avatar" id="check8" value="/static/img/avatar/avatar8.png">
                    <label for="check8">
                        <img src="/static/img/avatar/avatar8.png" alt="avatar8">
                    </label>
                </div>
                <div>
                    <input type="radio" name="avatar" id="check9" value="/static/img/avatar/avatar9.png">
                    <label for="check9">
                        <img src="/static/img/avatar/avatar9.png" alt="avatar9">
                    </label>
                </div>
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