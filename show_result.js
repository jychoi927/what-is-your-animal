var discripton_container = document.querySelector('.discription');
var postsns_container = document.querySelector('.post-sns');

function show_result() {
    var discription = discripton_container.querySelector('h2');
    discription.style.fontSize = 3+'em';
    discription.innerText = '본인과 가장 닮은 동물은';
    document.querySelector(".input-file-container").style.display = "none";
    document.querySelector(".startBtn-container").style.display = "none";

    postsns_container.style.visibility = "visible";

}

  

