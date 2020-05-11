const actors = document.querySelectorAll('.actor');

for (let actor of actors) {
    actor.addEventListener('click', (e) =>{
        let nameOfActor = actor.dataset.actorName;
        let input = document.createElement('INPUT');
        input.placeholder=nameOfActor;
        // actor.style.visibility='hidden';
        e.target.parentElement.replaceChild(input, actor);

    })
}