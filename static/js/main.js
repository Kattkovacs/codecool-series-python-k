const button = document.querySelector('#btn');
const rows = document.querySelectorAll('.row');


button.addEventListener('click', () => {
    let counter = 0;
    for (let row of rows) {
        if (counter%3===0) {
            row.style.background='red';
        }
        counter += 1;
    }
});