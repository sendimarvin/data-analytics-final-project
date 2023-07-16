import pandas as pd

def merge_sheets(input_file, output_file, column_mapping):
    # Read all sheets into a dictionary of DataFrames
    sheets_dict = pd.read_excel(input_file, sheet_name=None)
    
    # Merge the DataFrames and apply column mapping
    merged_df = pd.concat(sheets_dict.values())
    merged_df = apply_column_mapping(merged_df, column_mapping)
    
    # Write the merged DataFrame to a new Excel file
    merged_df.to_excel(output_file, index=False)
    
    print("Merging completed successfully.")

def apply_column_mapping(df, column_mapping):
    merged_df = df.copy()
    for mapping in column_mapping:
        merged_column = mapping[0]
        sheet_columns = mapping[1:]
        
        for sheet_column in sheet_columns:
            if sheet_column in df.columns:
                merged_df[merged_column] = df[sheet_column].astype(str)
                break
    
    merged_df.drop(set(df.columns) - set(merged_df.columns), axis=1, inplace=True)
    return merged_df

# Provide the input file name, output file name, and column mapping
input_file = 'Water Quality Dataset - trans - test.xlsx'  # Replace with your input file name
output_file = 'output.xlsx'  # Replace with your desired output file name

# Define the column mapping as a list of lists
column_mapping = [['Subcounty', 'Subcounty', 'Sub county'], ['Y', 'y1', 'Y2']]  # Replace with your desired column mapping

# Call the merge_sheets function
merge_sheets(input_file, output_file, column_mapping)