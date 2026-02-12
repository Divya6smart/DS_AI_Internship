# -*- coding: utf-8 -*-
"""
Created on thru Feb  12 14:38:47 2026

@author: divya
"""
import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")

# -------------------------------
# Goal 1: Detect & Handle Data Quality Issues
# -------------------------------

# Report missing values
print("Missing values report:\n", df.isna().sum())

# Shape before cleaning
print("Shape before cleaning:", df.shape)

# Fill missing numeric values with median
numeric_cols = df.select_dtypes(include=['float64','int64']).columns
for col in numeric_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Shape after cleaning
print("Shape after cleaning:", df.shape)

# -------------------------------
# Goal 2: Ensure Data is Mathematically Usable
# -------------------------------

# Check initial data types
print("Data types before conversion:\n", df.dtypes)

# Clean "Price" column: remove '$' and convert to float
df['Price'] = df['Price'].str.replace('$','', regex=True).astype(float)

# Convert "Date" column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Verify conversions
print("Data types after conversion:\n", df.dtypes)
