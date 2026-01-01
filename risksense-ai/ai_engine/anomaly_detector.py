# anomaly_detector.py
# Detects anomalies using AI models
import pandas as pd
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, contamination=0.05):
        self.model = IsolationForest(
            n_estimators=100,
            contamination=contamination,
            random_state=42
        )

    def detect(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        data = df[columns]
        self.model.fit(data)

        df["anomaly_score"] = self.model.decision_function(data)
        df["is_anomaly"] = self.model.predict(data) == -1
        return df
    def get_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[df["is_anomaly"]]
    def summary(self, df: pd.DataFrame) -> dict:
        total = len(df)
        anomalies = df["is_anomaly"].sum()
        return {
            "total_records": total,
            "anomalies_detected": anomalies,
            "anomaly_percentage": (anomalies / total) * 100 if total > 0 else 0
        }
        