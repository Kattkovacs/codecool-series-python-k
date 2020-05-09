let addAvgTitle =
    `<p>The average of the selected cards: {{ show['average_rating'] |int }}</p>`;
document.querySelector('#avg-title').innerHTML = addAvgTitle;

const cards = document.querySelectorAll('.card-year');
const avgTitle = document.querySelector('#avg-title');
const highlightedCards = document.querySelectorAll('.highlighted');

for (let card of cards) {
    card.addEventListener('click', (e) => {
        if (card.classList.contains('highlighted')) {
            card.classList.remove('highlighted');
        } else {
            card.classList.add('highlighted');
            document.querySelector('#avg-title').innerHTML =
                `<p>The average of the selected cards: {{ card.children[1].textContent }}</p>`;
            // let cardAvg = card.children[1].textContent;
            // document.querySelector('#avg-title').innerHTML += cardAvg;
        }
    })
}


