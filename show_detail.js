function showDetail() {

    document.querySelector('.result').style.display = "none";
    document.querySelector('.detail').style.display = "block";


    google.charts.load('current', { packages: ['corechart', 'bar'] });
    google.charts.setOnLoadCallback(showChart);

    showManipulation();

    var resultDiscriptionContainer = document.querySelector(".result-discription-container");
    resultDiscriptionContainer.style.height = "200px";
    resultDiscriptionContainer.style.margin
    var resultDiscription = resultDiscriptionContainer.querySelector('h2');
    resultDiscription.innerHTML = "결과 상세설명<br>컨테이너 입니다.";


}

function showManipulation() {
    document.getElementById("img1").src = 'images/01.png';
    document.getElementById("img2").src = 'images/02.png';
    document.getElementById("img3").src = 'images/03.png';
    document.getElementById("img4").src = 'images/04.png';

}

function showChart() {
    var dog_prob = Math.round(Number(dog_score) * 100);
    var cat_prob = Math.round(Number(cat_score) * 100);
    var pig_prob = Math.round(Number(pig_score) * 100);

    var data = google.visualization.arrayToDataTable([
        ['string', 'Similarity(%)', { role: 'annotation' }],
        ["", dog_prob, dog_prob + '%'],
        ["", cat_prob, cat_prob + '%'],
        ["", pig_prob, pig_prob + '%'],
        ["", 11, 11 + '%']
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

