const logout = () => {
    $.ajax({
        url: '/logout',
        type: 'POST',
        success: function(data) {
            window.location.href = '/';
        }
    });
};