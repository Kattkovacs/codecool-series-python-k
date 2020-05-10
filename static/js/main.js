const actors = document.querySelectorAll('.actor');

for (let actor of actors) {
    actor.addEventListener('click', ()=> {
        if (actor.firstElementChild.dataset.birth) {
            let birthDate = actor.firstElementChild.dataset.birth;

            let dateNow = new Date();
            let yearNow = dateNow.getFullYear();
            alert(parseInt(yearNow) - parseInt(birthDate.substring(0, 4)));
        }
    })
}