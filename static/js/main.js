const ratings = document.querySelectorAll('.rating');

for(let rating of ratings) {
    rating.addEventListener('click', ()=> {
        let genre = rating.previousElementSibling.dataset.genreName;
        alert(genre);
    })
}