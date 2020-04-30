let showCards=document.querySelectorAll('.card-shows');

for (let card of showCards) {
    card.addEventListener('click', function () {
        let showOverview=card.querySelector('.overview');
        if (showOverview.style.display === 'none' || showOverview.style.display === '') {
            showOverview.style.display = 'block';
        } else {
            showOverview.style.display = 'none';
        }
    })
}
