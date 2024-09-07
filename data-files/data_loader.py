import pandas as pd

# Assuming all .xls files are in the same folder and named appropriately
file_names = ["BeeSpotter1.xls", "BeeSpotter2.xls", "BeeSpotter3.xls", "BeeSpotter4.xls", "BeeSpotter5.xls"]

# Load all Excel files into a list of DataFrames
data_frames = [pd.read_csv(file, sep='\t') for file in file_names]

# Optionally concatenate the DataFrames into one
bee_data = pd.concat(data_frames, ignore_index=True)

# Preview the first few rows
print(bee_data.head())
