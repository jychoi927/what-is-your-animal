var startBtnContainer = document.querySelector('.startBtn-container');

var loadFile = function (event) {
    var reader = new FileReader();

    if (event.target.files[0] !== undefined) {
        reader.onload = function () {
            var output = document.getElementById('avatar');
            output.src = reader.result;
        };

        reader.readAsDataURL(event.target.files[0]);
        var startBtn = startBtnContainer.querySelector('label');
        startBtn.style.padding = "14px 45px";
        startBtn.innerText = '닮은 동물 찾기';
    }
    else {
        var output = document.getElementById('avatar');
        var startBtn = startBtnContainer.querySelector('label');

            output.src = "https://s3-us-west-2.amazonaws.com/s.cdpn.io/20625/avatar-bg.png";
            startBtn.style.padding = '';
            startBtn.innerText = '';
    }
};