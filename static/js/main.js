const shows = document.querySelectorAll('.show-title');

for (let show of shows) {
    show.addEventListener('click', () => {
        if (show.classList.contains('green-highlight')) {
            show.classList.remove('green-highlight');
        } else {
            show.classList.add('green-highlight');
        }
    })
}