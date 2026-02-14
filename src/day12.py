# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:44:34 2026

@author: divya
"""

# scatter_plot.py

import matplotlib.pyplot as plt

# Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

# Create scatter plot
plt.scatter(study_hours, scores)

# Add labels and title
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Hours vs Exam Scores")

# Show plot
plt.show()

# dashboard.py

import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line plot (monthly sales trend example)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
monthly_sales = [200, 250, 300, 350, 400]

# Create figure

# First subplot (Bar Chart)
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Second subplot (Line Plot)
plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display
plt.show()

