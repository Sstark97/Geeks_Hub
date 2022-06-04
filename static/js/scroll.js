const element = document.querySelectorAll(".content_list");

element.forEach(content => {
    content.addEventListener('wheel', (event) => {
        event.preventDefault();

        content.scrollBy({
            left: event.deltaY < 0 ? -40 : 40,
        });
    });
});