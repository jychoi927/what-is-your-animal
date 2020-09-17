import requests

# resp = requests.post("http://127.0.0.1:5000/predict", files={"file": open('./cat.jpg', 'rb')})
resp = requests.post("http://220.149.232.14/predict", files={"file": open('./human_0001.jpg', 'rb')})

print(resp.json())
