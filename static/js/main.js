const episodeSums = document.querySelectorAll('.sum');

for (let row of episodeSums) {
    let episodes = row.dataset.sum;
    if (parseInt(episodes) %2===0){
        row.classList.add('even-sum');
    } else if (parseInt(episodes) %2!==0){
        row.classList.add('odd-sum');
    }
}


