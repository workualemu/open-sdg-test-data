from sdg.open_sdg import open_sdg_check
# from sdg.inputs import InputSdmxMl_UnitedNationsApi as uapi

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main Tkinter window

messagebox.showinfo("Info", "This is a popup message!")

# uapi_object = uapi(reference_area='800')
# qur = uapi_object.get_api_query()
# print(f"QUERYYYYYYYYYY: {qur}")
# Validate the indicators.
validation_successful = open_sdg_check(config='config_data.yml')

# If everything was valid, perform the build.
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
