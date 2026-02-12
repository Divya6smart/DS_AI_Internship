# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on thru Feb  12 14:38:47 2026
=======
Created on Mon Feb  10 14:38:47 2026
>>>>>>> 6391c11 (day9)

@author: divya
"""
# STEP 1 — Import pandas 
import pandas as pd 
 
# STEP 2 — Create messy dataset (added Date + messy City + duplicate row) 
data = { 
    "CustomerID": [101,102,103,104,105,106,107,107,108,109], 
    "Name": ["Amit","Sara","John",None,"Priya","David","Meena","Meena","Ali","Riya"], 
    "Age": [25,None,30,22,None,28,35,35,None,26], 
    "City": [" Bangalore","Mumbai ","Delhi",None,"Bangalore","Chennai","Mumbai","Mumbai","Delhi"," Bangalore "], 
    "OrderAmount": [2500,1800,None,2200,3000,None,1500,1500,2700,None], 
    "PaymentMethod": ["UPI","Card","Cash","Card",None,"UPI","Cash","Cash","Card","UPI"], 
    "Date": ["2024-01-05","2024-01-10","2024-02-01","2024-02-05","2024-03-01", 
             "2024-03-05","2024-03-10","2024-03-10","2024-04-01","2024-04-05"] 
} 
 
df = pd.DataFrame(data) 
# STEP 3 — Inspect dataset 
print("First rows:\n", df.head()) 
print("\nDataset info:") 
print(df.info()) 
# STEP 4 — Check missing values 
print("\nMissing values per column:") 
print(df.isna().sum()) 
# STEP 5 — Fill missing values (statistical approach) 
df["Age"] = df["Age"].fillna(df["Age"].mean()) 
df["OrderAmount"] = df["OrderAmount"].fillna(df["OrderAmount"].mean()) 
df["City"] = df["City"].fillna(df["City"].mode()[0]) 
df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0]) 
df["Name"] = df["Name"].fillna("Unknown") 
# STEP 6 — Check data types before conversion 
print("\nData types BEFORE conversion:") 
print(df.dtypes) 
# STEP 7 — Convert data types 
df["Age"] = df["Age"].astype(int) 
df["Date"] = pd.to_datetime(df["Date"]) 
print("\nData types AFTER conversion:") 
print(df.dtypes) 

# ------------------------------------------------- 
# STEP 1 — Import pandas
import pandas as pd

# STEP 2 — Create dataset with messy Location values
data = {
    "Location": [" New York", "new york", "NEW YORK ",
                 "Los Angeles", " los angeles ", "LOS ANGELES"]
}

df = pd.DataFrame(data)

# STEP 3 — Check unique values BEFORE cleaning
print("Unique values BEFORE cleaning:")
print(df["Location"].unique())

# STEP 4 — Remove leading/trailing spaces
df["Location"] = df["Location"].str.strip()

# STEP 5 — Standardize casing (Title Case)
df["Location"] = df["Location"].str.title()

# STEP 6 — Verify cleaning
print("\nUnique values AFTER cleaning:")
print(df["Location"].unique())

# OPTIONAL — Show final dataset
print("\nFinal cleaned dataset:")
print(df)
