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
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Data
df = pd.DataFrame({
    "Age": [22, 25, 30, 35, 40],
    "Salary": [20000, 50000, 80000, 120000, 200000]
})

# Standardization
std = StandardScaler()
df_std = pd.DataFrame(std.fit_transform(df), columns=df.columns)

# Normalization
mm = MinMaxScaler()
df_mm = pd.DataFrame(mm.fit_transform(df), columns=df.columns)

print("Standardized:\n", df_std)
print("\nNormalized:\n", df_mm)

# Histogram (Salary)
plt.hist(df["Salary"])
plt.title("Original Salary")
plt.show()

plt.hist(df_std["Salary"])
plt.title("Standardized Salary")
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