const actors = document.querySelectorAll('.actor');

for (let actor of actors) {
    if (actor.dataset.older === 'older') {
        actor.classList.add('highlight');
    }
    actor.addEventListener('click', () => {
        let alert2 = actor.dataset.age;
        let alert4 = 2020 - actor.dataset.year;
        alert(`Age of the person at show release: ${alert2} 
        the shows current age is: ${alert4}`)
    })
}

