let stars = document.querySelectorAll('i');

for (let star of stars) {
    star.addEventListener('mouseenter', starHoverHandler);
}
for (let star of stars) {
    star.addEventListener('mouseleave', starLeaveHandler);
}

function starHoverHandler(e) {
    let starId = e.target.dataset.starId;
    let row = e.target.parentNode;
    let rowStars = row.querySelectorAll('i');
    for (let star of rowStars) {
        if (star.dataset.starId <= starId) {
            star.className = "fas fa-star";
        } else {
            star.className = "far fa-star";
        }
    }
}

function starLeaveHandler(e) {
    let row = e.target.parentNode;
    let rowStars = row.querySelectorAll('i');
    for (let star of rowStars) {
        if(row.dataset.showRating-1 >= star.dataset.starId) {
            star.className = "fas fa-star";
        } else {
            star.className = "far fa-star";
        }
    }
}