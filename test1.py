import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "model": "ROP",
    "features": [25.3, 0.9, 1.2, 3500, 0.55, 1.3, 1.8, 0.35,
                 0.4, 0.6, 10050, 24.8, 24.6, 0.91, 0.89, 1.25]
}

res = requests.post(url, json=data)
print(res.json())
