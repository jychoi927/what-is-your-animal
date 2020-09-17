var discription_container = document.querySelector('.discription');
var result_avatar_container = document.getElementById('result-avatar');

function showResult() {
    document.querySelector('.detail').style.display = "none";
    document.querySelector('.result').style.display = "block";
}

function getResult() {

    var result_animal = label[0];
    img_url = "static/images/result_" + result_animal + ".jpg";
    result_avatar_container.src = img_url;
}

getResult();
