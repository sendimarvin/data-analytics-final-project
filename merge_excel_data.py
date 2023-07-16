import pandas as pd

# Path to the Excel workbook
excel_file = "xWater Quality Dataset.xlsx"

# Read the Excel workbook into a dictionary of dataframes, where keys are sheet names
dfs = pd.read_excel(excel_file, sheet_name=None)

# Create an empty consolidated dataframe to store the transformed data
consolidated_df = pd.DataFrame()

# Iterate through each sheet in the workbook
for sheet_name, df in dfs.items():
    # Skip empty sheets that do not have any data
    if df.empty:
        continue

    # Transpose the dataframe to convert columns into rows
    transposed_df = df.transpose()

    # Use the first row as the column headers
    transposed_df.columns = transposed_df.iloc[0]

    # Remove the first row (old column headers)
    transposed_df = transposed_df.iloc[1:]

    # Add a new column to indicate the sheet name
    transposed_df['Sheet'] = sheet_name

    # Ensure unique column names in the transposed dataframe
    transposed_df = transposed_df.loc[:, ~transposed_df.columns.duplicated()]

    # Concatenate the transposed dataframe with the consolidated dataframe
    consolidated_df = pd.concat([consolidated_df, transposed_df], axis=0, ignore_index=True)

# Save the consolidated dataframe to a new sheet in the Excel workbook
with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a') as writer:
    consolidated_df.to_excel(writer, sheet_name='Consolidated', index=False)

print("Consolidation completed. The data has been written to the 'Consolidated' sheet.")
