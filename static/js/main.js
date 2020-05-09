const btn = document.querySelector('#btn');

btn.addEventListener('click', ()=>{
    const selectedNumber = document.querySelector('#points').value;
    const shows = document.querySelectorAll('.show-title');
    for (let show of shows) {
        let showSeasonNumber = show.firstElementChild.textContent;
        if (showSeasonNumber<=selectedNumber) {
            show.style.display = 'none';
        }
    }

});