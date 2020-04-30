showCards=document.querySelectorAll('.card');

for (let card of showCards) {
    card.addEventListener('click', function () {
        let showOverview=document.querySelectorAll('.overview');
        if (showOverview.style.display === 'none') {
            showOverview.style.display = 'block';
        } else {
            showOverview.style.display = 'none';
        }
    })
}
