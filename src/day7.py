# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 09:12:17 2026

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
run_journal()
# --- Goal 2: Practice Structured Data Storage (CSV) ---
def process_students():
    print("\n--- Filtering Passed Students ---")
    filename = 'students.csv'
    
    # Create the CSV file first for demonstration
    data = [
        ['Name', 'Grade', 'Status'],
        ['Alice', 'A', 'Pass'],
        ['Bob', 'aB', 'Pass'],
        ['charlie', 'F', 'Fail']
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

filename = input("\nEnter filename to open: ")

try:
    with open(filename, "r") as file:
        file.read()
    print("File opened successfully")

except FileNotFoundError:
    print("Oops! That file doesn't exist yet")


