$(document).ready(function () {
    $('.input input').on('keyup', function () {
        const value = $(this).val().toLowerCase();

        if (value !== "") {
            $('.content_search a img').filter(function () {
                if ($(this).attr('alt').toLowerCase().indexOf(value) > -1) {
                    $(this).toggle($(this).attr('alt').toLowerCase().indexOf(value) > -1);
                } else {
                    $(this).parent().hide();
                }
            });

        } else {
            $('.content_search a').show();
        }
    });
});