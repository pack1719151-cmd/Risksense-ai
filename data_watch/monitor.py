import pandas as pd

def detect_basic_risks(csv_path):
    df = pd.read_csv(csv_path)
    risks = []

    avg_sales = df["sales"].mean()

    for _, row in df.iterrows():
        if row["sales"] > avg_sales * 3:
            risks.append({
                "type": "ANOMALY",
                "message": f"Unusual sales spike detected on {row['date']} (₹{row['sales']})"
            })

        if row["returns"] > row["sales"] * 0.1:
            risks.append({
                "type": "PROCESS_RISK",
                "message": f"High returns ratio on {row['date']}"
            })

    return risks

