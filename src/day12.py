# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:44:34 2026

@author: divya
"""

import matplotlib.pyplot as plt

# Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

# Scatter plot
plt.scatter(study_hours, scores)

# Labels and title
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Hours vs Exam Scores")

# Display plot
plt.show()

import matplotlib.pyplot as plt

# ----- Subplot 1: Bar Chart -----
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# ----- Subplot 2: Line Plot -----
months = [1, 2, 3, 4, 5]
revenue = [200, 350, 300, 500, 650]

plt.subplot(1, 2, 2)
plt.plot(months, revenue)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

# Adjust layout
plt.tight_layout()

# Display dashboard
plt.show()

