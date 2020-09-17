from flask import Flask, request, render_template
from flask_cors import CORS

from transfer_network.inference_end_to_end import get_prediction

app = Flask(__name__)
CORS(app)


@app.route('/')
def idx():
    return render_template('index.html')


@app.route('/main')
def idx_main():
    return render_template('main.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # we will get the file from the request
        file = request.files['file']
        # convert that to bytes
        img_bytes = file.read()
        class_name, cat_ssim, dog_ssim, pig_ssim, bear_ssim = get_prediction(image_bytes=img_bytes)

        label = class_name
        cat_score = (cat_ssim / (cat_ssim + dog_ssim + pig_ssim + bear_ssim))
        dog_score = (dog_ssim / (cat_ssim + dog_ssim + pig_ssim + bear_ssim))
        pig_score = (pig_ssim / (cat_ssim + dog_ssim + pig_ssim + bear_ssim))
        bear_score = (bear_ssim / (cat_ssim + dog_ssim + pig_ssim + bear_ssim))

        # response.headers.add('Access-Control-Allow-Origin', '*')
        return render_template('result.html', label=label, cat_score=cat_score, dog_score=dog_score, pig_score=pig_score, bear_score=bear_score)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
