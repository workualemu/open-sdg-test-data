# scripts/clean_data.py

import pandas as pd
import glob

for file in glob.glob("data/*.csv"):
    df = pd.read_csv(file)
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    if "Value" in df.columns:
        df["Value"] = pd.to_numeric(df["Value"], errors="coerce")  # Converts 'NaN' string to real NaN
    df.to_csv(file, index=False)
