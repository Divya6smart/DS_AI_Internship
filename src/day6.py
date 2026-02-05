# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 18:22:38 2026

@author: divya
"""

import csv
import os

# --- Goal 1: Understanding 'w' vs 'a' (Append) ---
def run_journal():
    print("--- Daily Journal ---")
    name = input("Enter your name: ")
    goal = input("Enter your Daily Goal: ")
    
    # Using 'a' (append) to add to the end of the file
    with open("journal.txt", "a") as file:
        file.write(f"Name: {name}, Goal: {goal}\n")
    print("Goal saved to journal.txt!")

# Run this 3 times to see the effect
# Note: After running 3 times, journal.txt will have 3 lines.
# If you change "a" to "w", it will only have the last entry.
run_journal()

# --- Goal 2: Practice Structured Data Storage (CSV) ---
def process_students():
    print("\n--- Filtering Passed Students ---")
    filename = 'students.csv'
    
    # Create the CSV file first for demonstration
    data = [
        ['Name', 'Grade', 'Status'],
        ['Alice', 'A', 'Pass'],
        ['Bob', 'B', 'Pass'],
        ['Charlie', 'F', 'Fail']
    ]
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    # Read the CSV and filter for Passed students
    print("Students who passed:")
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Status'] == 'Pass':
                print(row['Name'])

# Execute the CSV processing
process_students()