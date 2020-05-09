const rates = document.querySelectorAll('.rating');

for (let rate of rates) {
    rate.addEventListener('click', (e) => {
        let rateNow = e.target.textContent;
        let newRate = parseFloat(rateNow)+ 0.1;
        e.target.textContent=newRate.toFixed(1);
    });
    rate.addEventListener('contextmenu', (e) => {
        e.preventDefault();
        let rateNow = e.target.textContent;
        let newRate = parseFloat(rateNow)-0.1;
        e.target.textContent=newRate.toFixed(1);
    })
}
