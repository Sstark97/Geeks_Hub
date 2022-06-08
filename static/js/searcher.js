$(document).ready(function () {
    $('.input input').on('keyup', function () {
        const value = $(this).val().toLowerCase();

        $('.content_search a img').filter(function () {
            if (! $(this).attr('alt').toLowerCase().includes(value)) {
                $(this).parent().hide();
            } else {
                $(this).parent().show();
            }
        });

    });
});