var startBtnContainer = document.querySelector('.startBtn-container');
var base64result;

var loadFile = function (event) {
    var reader = new FileReader();

    if (event.target.files[0] !== undefined) {
        reader.onload = function () {
            //base64result = reader.result.split(',')[1];
            base64result = reader.result;
            console.log(base64result);
            var byteArray = base64ToByteArray(base64result);
            console.log(byteArray);

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

function base64ToByteArray(base64String) {
    try {            
        var sliceSize = 1024;
        var byteCharacters = atob(base64String);
        var bytesLength = byteCharacters.length;
        var slicesCount = Math.ceil(bytesLength / sliceSize);
        var byteArrays = new Array(slicesCount);

        for (var sliceIndex = 0; sliceIndex < slicesCount; ++sliceIndex) {
            var begin = sliceIndex * sliceSize;
            var end = Math.min(begin + sliceSize, bytesLength);

            var bytes = new Array(end - begin);
            for (var offset = begin, i = 0; offset < end; ++i, ++offset) {
                bytes[i] = byteCharacters[offset].charCodeAt(0);
            }
            byteArrays[sliceIndex] = new Uint8Array(bytes);
        }
        return byteArrays;
    } catch (e) {
        console.log("Couldn't convert to byte array: " + e);
        return undefined;
    }
}


