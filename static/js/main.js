const actors = document.querySelectorAll('.actor');

for (let actor of actors) {
    if (actor.firstElementChild.textContent==='older') {
        actor.classList.add('highlight');
    }
    actor.addEventListener('click', () =>{
        let alert1 ='Age of the person at show release: ';
        let alert2 = actor.lastElementChild.textContent;
        let alert3 = ' the shows current age is: ';
        let alert4 = 2020-actor.children[1].textContent;
        alert(alert1+alert2+alert3+alert4)
    })
}

