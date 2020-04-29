cards = document.querySelectorAll('.header').parentElement;


for (let card of cards) {
    card.addEventListener('click', changeBackground)
}

function changeBackground(e) {
    let selectedCard = e.target.parentElement;
    selectedCard.classList.add('highlighted');
}
