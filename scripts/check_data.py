from sdg.open_sdg import open_sdg_check
from sdg.inputs import InputSdmxMl_UnitedNationsApi as uapi

qur = "API QUERY"
print("QUERYYYYYYYYYY: " + qur)
print("Popup: Do something important now.")


uapi_object = uapi(reference_area='800')
qur = uapi_object.get_api_query()
print("QUERYYYYYYYYYY: " + qur)
# Validate the indicators.
validation_successful = open_sdg_check(config='config_data.yml')

# If everything was valid, perform the build.
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
