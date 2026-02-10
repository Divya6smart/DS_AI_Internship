# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 12:44:51 2026

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