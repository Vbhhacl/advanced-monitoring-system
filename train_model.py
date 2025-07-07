import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib 
import random

# Generate sample data
data = [random.uniform(50, 90) for _ in range(1000)]
df = pd.DataFrame(data, columns=["temp"])
df.to_csv("temperature_data.csv", index=False)

# Train model
model = IsolationForest(contamination=0.05)
model.fit(df)
joblib.dump(model, "anomaly_model.pkl")
print("Model trained and saved as anomaly_model.pkl")
