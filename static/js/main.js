let showTable = document.querySelectorAll('.show-length tr');
let actorsTable = document.querySelectorAll ('.actors tr');

for (let row of showTable) {
    row.addEventListener('mouseover', highlightActorRow);
    }
for (let row of showTable) {
    row.addEventListener('mouseleave', removeHighlightActorRow);
}

for (let row of actorsTable) {
    row.addEventListener('mouseover', highlightShowTableRow);
}

for (let row of actorsTable) {
    row.addEventListener('mouseleave', removeHighlightShowTableRow);
}

function highlightActorRow(e) {
    for (let row of actorsTable) {
        if (row.dataset.showId === e.target.parentNode.dataset.showId) {
            row.classList.add('highlighted');
        }
    }
}

function removeHighlightActorRow() {
    for (let row of actorsTable) {
            row.classList.remove('highlighted');
        }
    }

function highlightShowTableRow(e) {
    for (let row of showTable) {
        if (row.dataset.showId === e.target.parentNode.dataset.showId) {
            row.classList.add('highlighted');
        }
    }
}

function removeHighlightShowTableRow() {
    for (let row of showTable) {
        row.classList.remove('highlighted');
    }
}