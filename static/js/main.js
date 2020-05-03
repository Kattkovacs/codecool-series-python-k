let allShows = document.querySelectorAll('.all-shows');
let button = document.querySelector('#btn');

button.addEventListener('click', hideShows);

function hideShows() {
    for (let show of allShows) {
        if (show.style.display === 'block') {
            show.style.display = 'none';
        }
    }
}