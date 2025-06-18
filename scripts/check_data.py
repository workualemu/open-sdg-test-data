from sdg.open_sdg import open_sdg_check
import pandas as pd

# Monkeypatch InputBase.get_data_frame to clean each CSV-like input
from sdg.inputs import InputBase

original_get_data_frame = InputBase.get_data_frame

def patched_get_data_frame(self, *args, **kwargs):
    df = original_get_data_frame(self, *args, **kwargs)
    if isinstance(df, pd.DataFrame):
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        if 'Value' in df.columns:
            df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    return df

InputBase.get_data_frame = patched_get_data_frame

# Now run the check
success = open_sdg_check(config='config_data.yml')

if not success:
    raise Exception('There were validation errors. See output above.')
