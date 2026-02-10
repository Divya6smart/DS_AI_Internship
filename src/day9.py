# -*- coding: utf-8 -*-
"""
Created on Wed Feb  11 14:37:25 2026

@author: divya
"""

import pandas as pd

# -------- Products Series --------
products = pd.Series(
    [700, 150, 300],
    index=["Laptop", "Mouse", "Keyboard"]
)

print("Products Series:")
print(products)

print("\nPrice of Laptop:")
print(products["Laptop"])

print("\nFirst two products:")
print(products.iloc[:2])


# -------- Grades Series --------
grades = pd.Series([85, None, 92, 45, None, 78, 55])

print("\nOriginal Grades:")
print(grades)

print("\nMissing values:")
print(grades.isnull())

filled_grades = grades.fillna(0)

print("\nGrades after filling missing values:")
print(filled_grades)

print("\nScores greater than 60:")
print(filled_grades[filled_grades > 60])


# -------- Usernames Series --------
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

cleaned_usernames = usernames.str.strip().str.lower()
contains_a = cleaned_usernames.str.contains('a')

print("\nCleaned Usernames:")
print(cleaned_usernames)

print("\nContains letter 'a':")
print(contains_a)
