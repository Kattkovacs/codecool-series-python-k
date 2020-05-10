const actors = document.querySelectorAll('.actor');

for (let actor of actors) {
    actor.addEventListener('mouseenter', ()=>{
        if (actor.lastElementChild.textContent==='dead'){
            actor.classList.add('dead');
        } else if (actor.lastElementChild.textContent==='alive'){
            actor.classList.add('alive');
        }
    })
}