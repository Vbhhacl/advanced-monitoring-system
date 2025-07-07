
from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Gauge
import joblib

app = Flask(__name__)

# Load model
try:
    model = joblib.load("anomaly_model.pkl")
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    exit(1)

# Prometheus metric
anomaly_score = Gauge('anomaly_score', 'Anomaly score by ML model')

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        value = data["value"]
    except Exception:
        return jsonify({"error": "Missing or invalid 'value' in JSON body"}), 400

    try:
        prediction = model.predict([[value]])[0]
        is_anomaly = int(prediction == -1)
        anomaly_score.set(is_anomaly)
        return jsonify({"anomaly": is_anomaly})
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

if __name__ == '__main__':
    start_http_server(5001)
    app.run(port=5000, debug=True)
