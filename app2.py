import pandas as pd
import requests
import time

# Load your CSV
df = pd.read_csv("WLC_MUD_LOG_INTERPOLATED.csv")

# Pick the 16 required columns (you might want to confirm the names later)
FEATURE_COLUMNS = [
    'ROP', 'DXC', 'DEXM', 'ROPA', 'U', 'LTHDIGITAL',
    'FRACTUREGRADNT', 'BDTI', 'KREV', 'BDDI', 'Unnamed: 0',
    'ROP_rm3', 'ROP_rm10', 'DXC_rm3', 'DXC_rm10', 'BDTI_rm3'
]

# Ensure only rows with all values present
df = df.dropna(subset=FEATURE_COLUMNS)

# Loop through each row and send prediction
for _, row in df.iterrows():
    payload = {
        "model": "ROP",
        "features": [float(row[col]) for col in FEATURE_COLUMNS]
    }

    try:
        res = requests.post("http://127.0.0.1:5000/predict", json=payload)
        print(res.json())
    except Exception as e:
        print("Request failed:", e)

    time.sleep(0.5)  # optional: slow down so Grafana can keep up
