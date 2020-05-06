const cards = document.querySelectorAll('.show-card')

for(let card of cards) {
    card.addEventListener('mouseenter', () => {
    if (card.lastElementChild.innerHTML === 'alive'){
        if (card.classList.contains('light-highlight')) {
            card.classList.remove('light-highlight');
        } else {
        card.classList.add('light-highlight');
        }
    } else {
        if (card.classList.contains('dark-highlight')) {
            card.classList.remove('dark-highlight');
        } else {
            card.classList.add('dark-highlight');
        }
    }

    })

}