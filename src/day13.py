# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:22:53 2026

@author: divya
"""

# -------------------------------------------------
# STEP 1 — Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
# Make plots look better
sns.set_style("whitegrid")
# STEP 2 — Create Housing Dataset
data = {
    "HouseID": [1,2,3,4,5,6,7,8,9,10],
    "Price": [250000, 300000, 150000, 450000, 500000, 120000, 
              700000, 650000, 200000, 1000000],
    "City": ["Bangalore", "Mumbai", "Delhi", "Mumbai", "Bangalore",
             "Delhi", "Mumbai", "Bangalore", "Delhi", "Mumbai"],
    "Bedrooms": [2,3,2,4,4,1,5,4,2,6]
}
df = pd.DataFrame(data)
# STEP 3 — Inspect Dataset
print("First 5 Rows:\n")
print(df.head())
print("\nDataset Info:\n")
print(df.info())
print("\nStatistical Summary:\n")
print(df.describe())
# -------------------------------------------------
# STEP 4 — Histogram + KDE (Numerical Column: Price)
# -------------------------------------------------
plt.figure()
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
# -------------------------------------------------
# STEP 5 — Calculate Skewness & Kurtosis
# -------------------------------------------------
price_skew = skew(df["Price"])
price_kurt = kurtosis(df["Price"])
print("\nSkewness of Price:", price_skew)
print("Kurtosis of Price:", price_kurt)
# -------------------------------------------------
# STEP 6 — Interpretation Logic
# -------------------------------------------------

if price_skew > 0:
    print("Price distribution is positively skewed (Right Skewed)")
elif price_skew < 0:
    print("Price distribution is negatively skewed (Left Skewed)")
else:
    print("Price distribution is approximately normal")
# -------------------------------------------------
# STEP 7 — Count Plot (Categorical Column: City)
# -------------------------------------------------
plt.figure()
sns.countplot(x="City", data=df)
plt.title("Number of Houses per City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()
# -------------------------------------------------
# STEP 8 — Optional: Apply Log Transformation (if skewed)
# -------------------------------------------------
df["LogPrice"] = np.log(df["Price"])
plt.figure()
sns.histplot(df["LogPrice"], kde=True)
plt.title("Distribution After Log Transformation")
plt.xlabel("Log(Price)")
plt.ylabel("Frequency")
plt.show()
print("\nFinal Dataset with LogPrice:\n")
print(df.head())


#goal2
# STEP 1 — Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
# STEP 2 — Create Housing Dataset
data = {
    "HouseID": [1,2,3,4,5,6,7,8,9,10],
    "Price": [250000, 300000, 150000, 450000, 500000, 
              120000, 700000, 650000, 200000, 1000000],
    "SquareFootage": [800, 1000, 600, 1500, 1800, 
                      500, 2200, 2000, 750, 3000],
    "City": ["Bangalore", "Mumbai", "Delhi", "Mumbai", "Bangalore",
             "Delhi", "Mumbai", "Bangalore", "Delhi", "Mumbai"],
    "Bedrooms": [2,3,2,4,4,1,5,4,2,6]
}
df = pd.DataFrame(data)
# STEP 3 — Inspect Dataset
print("First 5 Rows:\n")
print(df.head())
# STEP 4 — Scatter Plot (Numerical vs Numerical)
# Compare SquareFootage vs Price
plt.figure()
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("Square Footage vs House Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()
# STEP 5 — Boxplot (Categorical vs Numerical)
# Compare City vs Price
plt.figure()
sns.boxplot(x="City", y="Price", data=df)
plt.title("City vs House Price")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()
# STEP 6 — Correlation Value
correlation = df["SquareFootage"].corr(df["Price"])
print("\nCorrelation between SquareFootage and Price:", correlation)
# STEP 7 — Observation
if correlation > 0:
    print("\nObservation: As SquareFootage increases, Price tends to increase.")
elif correlation < 0:
    print("\nObservation: As SquareFootage increases, Price tends to decrease.")
else:
    print("\nObservation: No clear relationship between SquareFootage and Price.")
    

#goal3

# STEP 1 — Import Required Library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


# -------------------------------------------------
# STEP 2 — Create Housing Dataset
# (Added Highly Correlated Variable: SizeInSqMeters)
# -------------------------------------------------

data = {
    "HouseID": [1,2,3,4,5,6,7,8,9,10],
    "Price": [250000, 300000, 150000, 450000, 500000, 
              120000, 700000, 650000, 200000, 1000000],
    "SquareFootage": [800, 1000, 600, 1500, 1800, 
                      500, 2200, 2000, 750, 3000],
    # 1 square meter ≈ 10.76 sq ft (Highly correlated variable)
    "SizeInSqMeters": [74, 93, 56, 139, 167, 
                       46, 204, 186, 70, 279],
    "Bedrooms": [2,3,2,4,4,1,5,4,2,6]
}

df = pd.DataFrame(data)


# -------------------------------------------------
# STEP 3 — Generate Correlation Matrix
# -------------------------------------------------

correlation_matrix = df.corr()

print("Correlation Matrix:\n")
print(correlation_matrix)


# -------------------------------------------------
# STEP 4 — Visualize Using Heatmap
# -------------------------------------------------

plt.figure()
sns.heatmap(correlation_matrix, annot=True)
plt.title("Correlation Matrix Heatmap")
plt.show()


# -------------------------------------------------
# STEP 5 — Identify Highly Correlated Variables (> 0.8)
# -------------------------------------------------

print("\nHighly Correlated Variable Pairs (Correlation > 0.8):\n")

for i in correlation_matrix.columns:
    for j in correlation_matrix.columns:
        if i != j:
            corr_value = correlation_matrix.loc[i, j]
            if abs(corr_value) > 0.8:
                print(f"{i} and {j} --> Correlation: {corr_value}")


# -------------------------------------------------
# STEP 6 — Boxplot to Detect Outliers (Price)
# -------------------------------------------------

plt.figure()
sns.boxplot(y=df["Price"])
plt.title("Boxplot of House Prices")
plt.ylabel("Price")
plt.show()