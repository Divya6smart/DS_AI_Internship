# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 14:35:16 2026

@author: divya
"""
# =====================================
# Student Performance Analysis
# =====================================

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 2. Load Dataset
# Dataset: StudentsPerformance.csv
df = pd.read_csv("StudentsPerformance.csv")

# 3. Basic Info
print(df.head())
print(df.info())

# 4. Feature Engineering
# Create average score
df["average_score"] = (
    df["math score"] +
   df["reading score"] +
    df["writing score"]
) / 3

# Create performance label (Pass = 1, Fail = 0)
df["pass"] = df["average_score"].apply(lambda x: 1 if x >= 50 else 0)

# 5. Exploratory Data Analysis

# Gender vs Average Score
plt.figure(figsize=(6,4))
sns.boxplot(x="gender", y="average_score", data=df)
plt.title("Gender vs Average Score")
plt.show()

# Test preparation vs Performance
plt.figure(figsize=(6,4))
sns.countplot(x="test preparation course", hue="pass", data=df)
plt.title("Test Preparation vs Pass/Fail")
plt.show()

# Parental education impact
plt.figure(figsize=(8,4))
sns.barplot(x="parental level of education", y="average_score", data=df)
plt.xticks(rotation=45)
plt.title("Parental Education vs Average Score")
plt.show()

# 6. Encode Categorical Data
df_encoded = pd.get_dummies(df, drop_first=True)

# 7. Features & Target
X = df_encoded.drop(["pass"], axis=1)
y = df_encoded["pass"]

# 8. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 9. Model Training
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 10. Prediction
y_pred = model.predict(X_test)

# 11. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))