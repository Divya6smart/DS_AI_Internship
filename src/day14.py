# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:25:17 2026

@author: divya
"""
#task1
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Dataset
df = pd.DataFrame({
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
})

# Label Encoding (Binary)
le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

# One-Hot Encoding (Nominal)
df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print(df)

#task2
# STEP 1 — Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler
# STEP 2 — Create Sample Dataset
data = {
    "Age": [22, 25, 30, 35, 40, 28, 32, 45],
    "Salary": [20000, 25000, 50000, 80000, 120000, 60000, 75000, 150000]
}
df = pd.DataFrame(data)
print("Original Data:\n")
print(df)
# STEP 3 — Standardization (Mean=0, Std=1)
scaler_standard = StandardScaler()
df_standardized = pd.DataFrame(
    scaler_standard.fit_transform(df),
    columns=df.columns
)
# STEP 4 — Normalization (Range 0–1)
scaler_minmax = MinMaxScaler()
df_normalized = pd.DataFrame(
    scaler_minmax.fit_transform(df),
    columns=df.columns
)
# STEP 5 — Plot Histogram BEFORE Scaling
plt.figure()
sns.histplot(df["Salary"], kde=True)
plt.title("Salary Before Scaling")
plt.show()
# STEP 6 — Plot Histogram AFTER Standardization
plt.figure()
sns.histplot(df_standardized["Salary"], kde=True)
plt.title("Salary After Standardization")
plt.show()
# STEP 7 — Plot Histogram AFTER Normalization
plt.figure()
sns.histplot(df_normalized["Salary"], kde=True)
plt.title("Salary After Normalization")
plt.show()

#task3
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Non-linear data (y = x²)
X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y = np.array([1,4,9,16,25,36,49,64,81,100])

# Linear Model
lin = LinearRegression().fit(X, y)
r2_linear = r2_score(y, lin.predict(X))

# Polynomial Model (degree=2)
poly = PolynomialFeatures(2)
X_poly = poly.fit_transform(X)
lin_poly = LinearRegression().fit(X_poly, y)
r2_poly = r2_score(y, lin_poly.predict(X_poly))

print("R² without Polynomial:", r2_linear)
print("R² with Polynomial:", r2_poly)