import os
import pandas as pd
import glob

data_dir = "data"

# Find all CSV files in the data directory
csv_files = glob.glob(os.path.join(data_dir, "*.csv"))

for file_path in csv_files:
    df = pd.read_csv(file_path)

    # Strip leading/trailing whitespace in all string cells
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Coerce 'Value' column to numeric, converting 'NaN' strings to actual NaN
    if "Value" in df.columns:
        df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

    # Overwrite the original CSV
    df.to_csv(file_path, index=False)

    print(f"Cleaned: {file_path}")
