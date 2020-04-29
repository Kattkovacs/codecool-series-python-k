
starsS = document.querySelectorAll('.fas');
starsR = document.querySelectorAll('.far');

console.log(starsS);

for (let star in starsS) {
    star.addEventListener('mouseenter', function(e){
            e.target.removeClass('fas fa-star');
    });
    star.addEventListener('mouseleave', function(e){
            e.target.addClass('far fa-star');
    })
}
