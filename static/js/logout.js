const logout = () => {
    $.ajax({
        url: '/logout',
        type: 'POST',
        success: function(data) {
            window.location.href = '/';
        }
    });

    if(localStorage.getItem('theme') == 'light') {
        localStorage.setItem('theme', 'dark');
    }
};