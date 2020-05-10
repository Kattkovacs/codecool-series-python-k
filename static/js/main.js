// import {dataHandler} from "./data-handler.js";

let allShows = document.querySelectorAll('.all-shows');
let button = document.querySelector('#btn');

button.addEventListener('click', hideShows);

function hideShows() {
    for (let show of allShows) {
        if (show.style.display === 'block') {
            show.style.display = 'none';
        }
    }
}


// JSON fetch

// document.querySelector('#highest-season-number').addEventListener('click', ()=>{
//     const seasonNumber = document.querySelector('#select-seasons').value;
//     dataHandler.api_post('/highest-season-number', seasonNumber, highestSeasonNumberCallback)
// });
//
// function highestSeasonNumberCallback(data) {
//     // data -> query result
//     const displayArea = document.querySelector("#shows")
//     // displayArea.innerHTML <= iterate on data and put here
// }
