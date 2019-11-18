var discription_container = document.querySelector('.discription');
var avatar_container = document.getElementById('avatar');
var discription = discription_container.querySelector('h2');

function show_result() {
    
    discription_container.style.height = 300+'px';
    discription.style.fontSize = 3+'em';
    discription.innerText = '가장 닮은 동물은';
    document.querySelector(".input-file-container").style.display = "none";
    document.querySelector(".startBtn-container").style.display = "none";
    document.querySelector(".resultBtn-container").style.display = "block";

    var retryBtn_container = document.querySelector(".retryBtn-container");
    retryBtn_container.querySelector('label').style.display = "block";
    retryBtn_container.style.display = "block";

    avatar_container.src = "images/result_cat.jpg";

}

function show_result_from_detail() {
    document.querySelector(".chart-discription-container").style.display = "none";
    document.querySelector(".animals-container").style.display = "none";
    document.querySelector(".image-discription-container").style.display = "none";
    document.querySelector(".manipulated-images-container").style.display = "none";
    document.querySelector(".result-discription-container").style.display = "none";
    document.querySelector(".backBtn-container").style.display = "none";

    document.querySelector(".avatarWrapper").style.display = "block";
    discription_container.style.display = "block";
    show_result();
}
