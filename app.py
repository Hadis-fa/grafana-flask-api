from flask import Flask, request, jsonify
from prometheus_client import Gauge, generate_latest
from datetime import datetime
import random  # Replace with your model
import time

app = Flask(__name__)

# Define Prometheus metrics
actual_wob = Gauge('actual_wob', 'Actual WOB value')
predicted_wob = Gauge('predicted_wob', 'Predicted WOB value')
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get("features")

    if not features or len(features) != 16:
        return jsonify({"error": "model expects 16 features"}), 400

    # Simulate prediction (replace with actual ML model call)
    predicted = sum(features) / len(features)
    actual = features[0]  # or simulate it separately

    # Set metrics
    actual_wob.set(actual)
    predicted_wob.set(predicted)

    # Include timestamp
    return jsonify({
        "time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "actual": actual,
        "predicted": predicted
    })

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
