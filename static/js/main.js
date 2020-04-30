let cards = document.querySelectorAll('.card-show');

for (let card of cards) {
    card.addEventListener('click', changeBackground);
}


function changeBackground(e) {
        let selectedCard = e.target.parentElement;
        if (selectedCard.classList.contains('highlighted')) {
            selectedCard.classList.remove('highlighted');
        } else {
            selectedCard.classList.add('highlighted');
            let collectHighs = document.querySelectorAll('.highlighted');
            if (collectHighs.length===1){

                let oneHighChild = document.querySelector('.avg');
                document.querySelector('#avg').innerHTML = oneHighChild.text;
            } else {
                for (let high of collectHighs) {
                    let highChild = document.querySelector('.avg');
                    document.querySelector('#avg').innerHTML = highChild.text;
                }
            }
        }
}



//     .children;
// document.querySelector('#avg').innerHTML = collectHighs;