
var loadingDisplay = document.getElementById('loading');
//loadingDisplay.style.visibility = "hidden";
function loadingShow() {

    loadingDisplay.style.visibility = "visible";
    setTimeout(hidingShow,2000);
    setTimeout(movePage,2002);
    /*
    const Url = 'http://220.149.232.14/predict';
    $.ajax({
        url: Url,
        contentType: false,
        processData: false,
        dataType: "json",
        type: "POST",
        data: js,
        success: function(result){
            console.log(result)
        }
    })
    */
}

function hidingShow(){
    loadingDisplay.style.visibility = "hidden";
}

function movePage(){
    location.href="result.html";
}

