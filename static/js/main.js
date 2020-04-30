let cards = document.querySelectorAll('.card-show');

for (let card of cards) {
    card.addEventListener('click', changeBackground);
}


function changeBackground(e) {
        let selectedCard = this;
        if (selectedCard.classList.contains('highlighted')) {
            selectedCard.classList.remove('highlighted');
        } else {
            let collectHighs = document.querySelectorAll('.highlighted');
            selectedCard.classList.add('highlighted');
            getAverage();
        }

function getAverage() {
    let highlighteds = document.querySelectorAll('.highlighted');
    let counter = 1;
    if (highlighteds.length===1) {
        let average = selectedCard.querySelector('h1').textContent;
        document.querySelector('#avg').innerHTML = average;

    } else {
        let newAverage = selectedCard.querySelector('h1').textContent;
        counter++;
        let oldAvg = document.querySelector('#avg').innerHTML;
        let newTotal = (parseFloat(newAverage)+parseFloat(oldAvg))/counter;
        document.querySelector('#avg').innerHTML = String(newTotal);
    }
}
}
