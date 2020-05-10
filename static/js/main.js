let trailerButtons = document.querySelectorAll('.trailer');

for (let button of trailerButtons) {
    button.addEventListener('click', trailerButtonHandler);
    }

function trailerButtonHandler(e) {
    let trailerId = e.target.dataset.trailerUrl;
    window.open(trailerId,'_blank', 'height=1000, width= 1000')
}
