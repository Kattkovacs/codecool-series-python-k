const cards = document.querySelectorAll('.show-card');
const overviews = document.querySelectorAll('.overview');


function getOverview() {
    for (let card of cards) {
        card.addEventListener('mouseenter', function () {
            card.firstElementChild.classList.add('highlight');
        });
        card.addEventListener('mouseleave', function () {
            if (card.firstElementChild.classList.contains('highlight')) {
                card.firstElementChild.classList.remove('highlight');
            }
        })
    }
}

getOverview();