# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:45:02 2026

@author: divya
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

# Create datasets
heights = np.random.normal(165, 7, 1000)          # Normal
incomes = np.random.exponential(50000, 1000)     # Right-Skewed
scores = 100 - np.random.exponential(10, 1000)   # Left-Skewed

df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

def analyze(column):
    mean = df[column].mean()
    median = df[column].median()
    
    sns.histplot(df[column], kde=True)
    plt.title(column)
    plt.axvline(mean, linestyle='--', label="Mean")
    plt.axvline(median, linestyle='-', label="Median")
    plt.legend()
    plt.show()
    
    print(column, "| Mean:", round(mean,2), "| Median:", round(median,2))
    print("-"*40)

analyze("Heights")
analyze("Incomes")
analyze("Scores")

#task2
import pandas as pd
import numpy as np

# Sample dataset
data = {"Marks": [45, 50, 55, 60, 65, 70, 75, 200]}
df = pd.DataFrame(data)

# Step 1 — Calculate Mean and Standard Deviation
mu = df["Marks"].mean()
sigma = df["Marks"].std()

# Step 2 — Create Z-Score column
df["z_score"] = (df["Marks"] - mu) / sigma

# Step 3 — Identify Outliers (|Z| > 3)
outliers = df[np.abs(df["z_score"]) > 3]

print("Mean (μ):", round(mu,2))
print("Standard Deviation (σ):", round(sigma,2))
print("\nData with Z-Score:\n", df)
print("\nOutliers:\n", outliers)

#task3
import numpy as np
import pandas as pd

np.random.seed(42)

# Step 1 — Create heavily skewed data (Income-like)
data = np.random.exponential(scale=50000, size=10000)

# Step 2 — Take 1000 samples of size 30 and store means
sample_means = []

for i in range(1000):
    sample = np.random.choice(data, size=30)
    sample_means.append(np.mean(sample))

# Step 3 — Plot distribution of sample means
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.show()