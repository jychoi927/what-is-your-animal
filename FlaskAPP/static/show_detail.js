
function showDetail() {

    document.querySelector('.result').style.display = "none";
    document.querySelector('.detail').style.display = "block";


    google.charts.load('current', { packages: ['corechart', 'bar'] });
    google.charts.setOnLoadCallback(showChart);

    showManipulation();
    var resultAnimal = label[0];
    if(resultAnimal == "dog"){resultAnimal = "'강아지' ";}
    else if(resultAnimal == "cat"){resultAnimal = "'고양이' ";}
    else if(resultAnimal == "pig"){resultAnimal = "'돼지' ";}
    else if(resultAnimal == "bear"){resultAnimal = "'곰' ";}
    var resultDiscriptionContainer = document.querySelector(".result-discription-container");
    resultDiscriptionContainer.style.height = "200px";
    resultDiscriptionContainer.style.margin
    var resultDiscription = resultDiscriptionContainer.querySelector('h2');
    var resultText = "사진과 동물의 합성 사진이 자연스러울수록<br>더 높은 점수가 나오는 알고리즘입니다.<br>해당 사진과 가장 자연스럽게 합성된 동물은<br>";
    var resultText = resultText + resultAnimal + "입니다.";
    resultDiscription.innerHTML = resultText;

}

function showManipulation() {
    document.getElementById("img1").src = 'static/cache/human+animal_img0.png?nocache='+Math.floor(Math.random() * 1000);
    document.getElementById("img2").src = 'static/cache/human+animal_img1.png?nocache='+Math.floor(Math.random() * 1000);
    document.getElementById("img3").src = 'static/cache/human+animal_img2.png?nocache='+Math.floor(Math.random() * 1000);
    document.getElementById("img4").src = 'static/cache/human+animal_img3.png?nocache='+Math.floor(Math.random() * 1000);    
}

function showChart() {
    var dog_prob = Math.round(Number(dog_score) * 100);
    var cat_prob = Math.round(Number(cat_score) * 100);
    var pig_prob = Math.round(Number(pig_score) * 100);
    var bear_prob = Math.round(Number(bear_score) * 100);

    var data = google.visualization.arrayToDataTable([
        ['string', 'Similarity(%)', { role: 'annotation' }],
        ["", dog_prob, dog_prob + '%'],
        ["", cat_prob, cat_prob + '%'],
        ["", pig_prob, pig_prob + '%'],
        ["", bear_prob, bear_prob + '%']
    ]);

    var options = {
        chartArea: { width: '100%', height: '90%' },
        hAxis: {
            minValue: 0,
            maxValue: 100
        },

        vAxis: {
        },
        backgroundColor: '#f8f8f8',
        allowHtml: true,
        animation: {
            duration: 1000,
            easing: 'in',
            startup: true
        }

    };

    var chart = new google.visualization.BarChart(document.querySelector('.chart'));

    chart.draw(data, google.charts.Bar.convertOptions(options));
}
