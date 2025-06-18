from sdg.open_sdg import open_sdg_check
import sdg.helpers as helpers
import pandas as pd

# Define a cleaning hook function
def clean_dataframe(df):
    if isinstance(df, pd.DataFrame):
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        if 'Value' in df.columns:
            df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    return df

# Patch the data cleaner globally using sdg.helpers
helpers.clean_data_frame = clean_dataframe

# Run the check with the modified behavior
success = open_sdg_check(config='config_data.yml')

if not success:
    raise Exception('There were validation errors. See output above.')
