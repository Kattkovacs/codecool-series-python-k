const titles = document.querySelectorAll('.random-colorize');


for (let title of titles) {
    title.addEventListener('mouseenter', (e) => {
        let random = '#'+(0x1000000+(Math.random())*0xffffff).toString(16).substr(1,6);
        e.target.style.backgroundColor = random;
    })
}