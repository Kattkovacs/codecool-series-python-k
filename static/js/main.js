const actors = document.querySelectorAll('.actor');
const shows = document.querySelectorAll('.show');

for (let actor of actors) {
    actor.addEventListener('mouseenter', highlightShow);
}

function highlightShow(e) {
    for (let show of shows) {
        if (e.target.dataset.actorShowId == show.dataset.showId) {
            show.classList.add('highlighted');
        }
    }
}

