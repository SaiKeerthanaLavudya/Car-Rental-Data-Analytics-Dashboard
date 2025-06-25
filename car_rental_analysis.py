import pandas as pd

# Step 1: Load the CSV file (adjust the path if needed)
df = pd.read_csv("car_rental_sample.csv")  # If the file is in same folder

# Step 2: Drop unwanted columns
columns_to_drop = [
    'fuel_type', 'setup_prams', 'tid', 'RunDate', 'average_text',
    'supplier_address', 'supplier_loction_type'
]
df_cleaned = df.drop(columns=columns_to_drop)

# Step 3: Convert date columns to datetime format
df_cleaned['start_date'] = pd.to_datetime(df_cleaned['start_date'])
df_cleaned['return_date'] = pd.to_datetime(df_cleaned['return_date'])

# Step 4: Create new columns
df_cleaned['rental_days'] = (df_cleaned['return_date'] - df_cleaned['start_date']).dt.days
df_cleaned['total_price'] = df_cleaned['price'] + df_cleaned['deposit_price'] + df_cleaned['drive_away_price']

# Step 5: Display sample cleaned data
print(df_cleaned[['city', 'product_name', 'rental_days', 'price', 'total_price']].head())

# Optional: Save cleaned data for dashboard use
df_cleaned.to_csv("cleaned_car_rental.csv", index=False)
