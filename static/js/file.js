const inputs = document.querySelectorAll( '.inputfile' );
const label = document.querySelector( 'span' );

inputs.forEach( input => {
    input.addEventListener( 'change', e => {
        var fileName = '';
        if ( input.files && input.files.length === 1 ) {
            label.innerText = input.files[0].name;
        } else {
            label.innerText = 'Selecciona una imagen';
        }
    });
});
    