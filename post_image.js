var loadingDisplay = document.getElementById('loading');

function postImage(){
    var post_image = document.getElementById('post-image');
    loadingShow();
    post_image.action="http://220.149.232.14/predict";
    post_image.submit();    
}

function loadingShow() {
    loadingDisplay.style.visibility = "visible";
    setTimeout(hidingShow,2000);
}

function hidingShow(){
    loadingDisplay.style.visibility = "hidden";
}


