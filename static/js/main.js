let rows = document.querySelectorAll('.row');
console.log(rows);

for (let i of rows) {
    if (i.dataset.older==='older') {
        i.classList.add("highlight");
    }
    i.addEventListener('click', displayAlert);
    }

function displayAlert(e) {
    alert('The name and age of the actor at show release: ' + this.firstElementChild.innerHTML +
        ' ' + this.children[1].innerHTML +
        ' The current age of the show: ' + this.lastElementChild.innerHTML);
}

