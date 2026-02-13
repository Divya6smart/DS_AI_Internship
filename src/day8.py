# -*- coding: utf-8 -*-
"""
Created on Wed Feb  10 12:44:51 2026

@author: divya
"""

import numpy as np

# Create a 5x3 array of random student scores (50–100)
scores = np.random.randint(50, 101, size=(5, 3))

# Calculate column-wise mean (subject-wise mean)
subject_mean = scores.mean(axis=0)

# Subtract mean using broadcasting
centered_scores = scores - subject_mean

# Output
print("Original Scores:\n", scores)
print("\nSubject-wise Mean:\n", subject_mean)
print("\nCentered Scores (After Normalization):\n", centered_scores)
<<<<<<< HEAD
=======

# Task 2: Reshaping & Transposing
# -------------------------------

# Create 1D array of values from 0 to 23
data = np.arange(24)

# Reshape into (4, 3, 2)
reshaped_data = data.reshape(4, 3, 2)

# Transpose to (4, 2, 3)
final_data = reshaped_data.transpose(0, 2, 1)

print("\nFinal Shape:", final_data.shape)
print("\nFinal Array:\n", final_data)
>>>>>>> 6391c11 (day9)
