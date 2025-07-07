import time
import random
import requests
from prometheus_client import start_http_server, Gauge

anomaly_score = Gauge('anomaly_score', 'Anomaly score by ML model')

def get_prediction(value):
    url = "http://127.0.0.1:5000/predict"
    payload = { "value": value }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Got response: {result}")
            return result.get("anomaly", 0)
        else:
            print(f"🔍 Status code: {response.status_code}")
            print(f"📦 Raw response: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None

if __name__ == '__main__':
    print("🚀 Prometheus exporter running at http://localhost:8000/metrics")
    start_http_server(8000)

    while True:
        value = random.uniform(-2, 4)  # simulate random input
        print(f"📨 Sending value: {value}")
        prediction = get_prediction(value)

        if prediction is not None:
            anomaly_score.set(prediction)
        else:
            print("⚠️ No valid prediction received.")
        
        time.sleep(5)
