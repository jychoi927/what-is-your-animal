function retry(){
    change_discription();
    change_button();
}

function change_discription(){
    discription_container.style.height = 400+'px';
    discription.style.fontSize = 1.8+'em';
    discription.innerHTML = '\'너의얼굴은\'은 딥 러닝을 사용하여<br>얼굴과 가장 닮은 동물을 찾아내는 웹 어플리케이션 입니다.<br>여러분의 얼굴이 어떤 동물과 닮았는지 궁금하신가요?<br>';
}

function change_button(){
    document.querySelector(".resultBtn-container").style.display = "none";
    document.querySelector(".retryBtn-container").style.display = "none";


    var output = document.getElementById('avatar');
    output.src = "https://s3-us-west-2.amazonaws.com/s.cdpn.io/20625/avatar-bg.png";

    document.querySelector(".input-file-container").style.display = "block";
    document.querySelector(".startBtn-container").style.display = "none";
    

    
}

