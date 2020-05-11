const ratings = document.querySelectorAll('.rating');

// for(let rating of ratings) {
//     rating.addEventListener('click', ()=> {
//         let genre = rating.previousElementSibling.dataset.genreName;
//         alert(`Genre: ${genre}`);
//     })
// }

for(let rating of ratings) {
    rating.addEventListener('click', (e)=> {
        let genre = e.target.previousElementSibling.dataset.genreName;
        alert(`Genre: ${genre}`);
    })
}