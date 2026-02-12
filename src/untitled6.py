# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:15:05 2026

@author: divya
"""

import pandas as pd
import numpy as np

data = {
    'order_id': [101, 102, np.nan, 104, 102, 106, np.nan],
    'Price': ['$100', '$200', '$150', '$300', '$200', '$400', '$150'],
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', 
             '2025-01-04', '2025-01-02', '2025-01-06', '2025-01-03'],
    'Location': [' New York ', 'los angeles', 'Chicago', 
                 'new york', 'los angeles', 'Chicago ', ' chicago']
}

df = pd.DataFrame(data)
# Load dataset (assuming customer_orders.csv exists)
df = pd.read_csv('customer_orders.csv')

# --- 1. Handling Missing Data and Duplicates ---
print("Shape before cleaning:", df.shape)

# Report missing values
print("\nMissing values per column:\n", df.isna().sum())

# Fill missing numerical values with the median
# Example: filling 'order_id' or 'price' if they are numeric
for col in df.select_dtypes(include=np.number).columns:
    df[col].fillna(df[col].median(), inplace=True)

# Remove exact duplicate rows
df = df.drop_duplicates()

print("Shape after cleaning:", df.shape)

# --- 2. Data Type Conversion (Price and Date) ---
# Check initial dtypes
print("\nData types before conversion:\n", df.dtypes)

# Clean and convert Price: Remove '$', convert to float
# Assuming column name is 'Price'
df['Price'] = df['Price'].astype(str).str.replace('$', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'])

# Convert Date: Convert to datetime object
# Assuming column name is 'Date'
df['Date'] = pd.to_datetime(df['Date'])

print("\nData types after conversion:\n", df.dtypes)

# --- 3. Text Normalization (Location) ---
# Clean whitespace and standardize casing
# Assuming column name is 'Location'
df['Location'] = df['Location'].str.strip().str.title()

# Verify unique values
print("\nUnique Locations:\n", df['Location'].unique())