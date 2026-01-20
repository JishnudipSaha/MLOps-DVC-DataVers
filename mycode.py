import pandas as pd
import os

# Create a sample data frame with column names.
data = {"Name": ["Jishnu", "Aritra", "Prateek"],
        "Age":[21,20,21],
        "City": ["Belgharia", "Barasat", "Kota"]}
df = pd.DataFrame(data=data)

# # Adding new row to df for V2
# new_row_loc = {"Name": "V2", "Age": 20, "City": "City1"}
# df.loc[len(df.index)] = new_row_loc

# # Adding new row to df for V3
# new_row_loc2 = {"Name": "V3", "Age": 22, "City": "City2"}
# df.loc[len(df.index)] = new_row_loc2

# Ensure the "data" directory exist at root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Saving the dataframe to CSV file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")