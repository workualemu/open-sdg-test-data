from sdg.open_sdg import open_sdg_check
from sdg.inputs import InputSdmxMl_UnitedNationsApi
import pandas as pd

# Patch the get_indicator method to clean SDMX-fetched data
original_get_indicator = InputSdmxMl_UnitedNationsApi.get_indicator

def patched_get_indicator(self, *args, **kwargs):
    indicator = original_get_indicator(self, *args, **kwargs)

    # Clean the DataFrame
    df = indicator['data']
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    if 'Value' in df.columns:
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    indicator['data'] = df

    return indicator

InputSdmxMl_UnitedNationsApi.get_indicator = patched_get_indicator

# Run the check
validation_successful = open_sdg_check(config='config_data.yml')

# Optional: fail the script if validation fails
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
