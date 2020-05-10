const rows = document.querySelectorAll('.row');

for (let row of rows) {
    row.addEventListener('click', ()=> {
        row.style.visibility = 'hidden';
    })
}