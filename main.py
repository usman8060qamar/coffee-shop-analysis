import pandas as pd

# Load the dataset
input_file = 'Coffee Shop Sales.xlsx'  # Path to your input Excel file
output_file = 'Cleaned_Coffee_Shop_Sales.xlsx'  # Path for the cleaned output file

# Read the Excel file
df = pd.read_excel(input_file)

# Display initial data info
print("Initial Data Info:")
print(df.info())
print("\nInitial Data Sample:")
print(df.head())

# Data Cleaning Steps

# 1. Remove duplicates
df.drop_duplicates(subset=['transaction_id'], keep='first', inplace=True)

# 2. Check for missing values and handle them
missing_values = df.isnull().sum()
print("\nMissing Values Before Cleaning:")
print(missing_values)

# Fill missing values or drop rows/columns as needed
df.dropna(subset=['transaction_qty', 'unit_price', 'product_id'], inplace=True)

# 3. Ensure data types are consistent
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Convert transaction_time to string and then to timedelta
df['transaction_time'] = pd.to_datetime(df['transaction_time'], format='%H:%M:%S').dt.time
df['transaction_time'] = pd.to_timedelta(df['transaction_time'].astype(str))

# 4. Reset index after cleaning
df.reset_index(drop=True, inplace=True)

# Display cleaned data info
print("\nCleaned Data Info:")
print(df.info())
print("\nCleaned Data Sample:")
print(df.head())

# Export the cleaned dataframe to a new Excel file
df.to_excel(output_file, index=False)

print(f"\nCleaned data exported to {output_file}")