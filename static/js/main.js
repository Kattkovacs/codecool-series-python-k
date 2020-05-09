let addAvgTitle =
    `<p>The average of the selected cards: </p>
    <p></p>`;
document.querySelector('#avg-title').innerHTML = addAvgTitle;

const cards = document.querySelectorAll('.card-year');
const avgTitle = document.querySelector('#avg-title');
const highlightedCards = document.querySelectorAll('.highlighted');
let counter = 1;

for (let card of cards) {
    card.addEventListener('click', () => {
        if (card.classList.contains('highlighted')) {
            card.classList.remove('highlighted');
        } else {
            card.classList.add('highlighted');
            if (counter===1){
                document.querySelector('#avg-title').lastElementChild.innerHTML = card.children[1].textContent;
                counter ++;
            } else {
                let cardAvg=card.children[1].textContent;
                let pAvg=document.querySelector('#avg-title').lastElementChild.innerHTML;
                let totalAvg = (parseFloat(cardAvg)+parseFloat(pAvg))/2;
                document.querySelector('#avg-title').lastElementChild.innerHTML=parseFloat(totalAvg);
                counter ++;
            }


            // let cardAvg = card.children[1].textContent;
            // document.querySelector('#avg-title').innerHTML += cardAvg;
        }
    })
}


