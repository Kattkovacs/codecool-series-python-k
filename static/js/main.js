const medals = document.querySelectorAll('.actor');

for (let medal of medals) {
    medal.addEventListener('click', changeBackground)
}

function changeBackground(e) {
    e.target.classList.add('highlight');
}

