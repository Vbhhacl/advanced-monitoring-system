# Anomaly Detection Monitoring System

A beginner-friendly machine learning project that simulates real-time anomaly detection using a trained ML model. It also integrates monitoring tools like Prometheus to provide visibility into anomalies in numeric data — ideal for industrial and IoT applications.

---

## 🧩 Features

- Simulates real-time data input (similar to sensor readings).
- Detects anomalies using a trained **Isolation Forest** model.
- Exposes a **Flask-based REST API** for predictions.
- Pushes anomaly scores to a **Prometheus-compatible metrics endpoint**.
- Ready for extension to real-world sensor integration and cloud deployment.

---

## 🧠 Technology Used

| Component          | Description                               |
|-------------------|-------------------------------------------|
| Python            | Core programming language                 |
| Flask             | Backend API for real-time predictions     |
| scikit-learn      | For training and using the ML model       |
| Prometheus Client | For exposing metrics                      |
| joblib            | Saves/loads the trained ML model          |

---

## 📦 File Structure

monitoring-system/
├── anomaly_api.py # Flask API for ML predictions
├── metrics_exporter.py # Sends data and exports metrics
├── anomaly_model.pkl # Pre-trained Isolation Forest model
├── requirements.txt # Python dependencies
└── README.md # Project documentation



## ⚙️ How It Works

1. **ML Model**: The Isolation Forest model is pre-trained to detect outliers in numeric data.
2. **Flask API**: Receives a value and predicts whether it's an anomaly.
3. **Metrics Exporter**: Randomly generates values, queries the API, and updates a Prometheus metric (`anomaly_score`).
4. **Monitoring**: Prometheus scrapes metrics from `http://localhost:8000/metrics`, allowing you to visualize anomaly trends in tools like Grafana.

---

## 📤 Example API Flow

- **Input**:
  ```json
  { "value": 0.95 }
Output:

json
Copy
Edit
{ "anomaly": 0 }
Metric exposed: anomaly_score 0 or 1

📈 Future Enhancements
Integration with real-time sensors (e.g., temperature, vibration).

Deployment with Docker and Kubernetes.

Live dashboards via Grafana.

Cloud API integration for real IoT applications.

🧠 Why This Project Is Unique
Demonstrates real-time prediction instead of offline batch inference.

Combines AI + DevOps Monitoring concepts using Flask and Prometheus.

Simulates a real-world industrial application with minimal hardware.

Beginner-friendly yet extensible to enterprise use cases.

📚 Summary
This project showcases how machine learning can power anomaly detection in a simulated sensor-like environment, with built-in observability through Prometheus. It’s a great stepping stone into intelligent monitoring systems and industrial IoT solutions.
