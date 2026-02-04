# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 11:06:52 2026

@author: divya
"""

# PART 1: Inventory Management (Lists)

print("PART 1: Inventory Management")

inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print("Current Inventory:", inventory)

inventory.append("Eggs")
inventory.remove("Bananas")
inventory.sort()

print("Final Updated Inventory:", inventory)
print()

# PART 2: Temperature Readings (Indexing & Slicing)

print("PART 2: Temperature Readings")

temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])

afternoon_peak = temperatures[3:6]
print("Afternoon Peak Readings:", afternoon_peak)

last_3_hours = temperatures[-3:]
print("Last 3 Hours Readings:", last_3_hours)
print()

# PART 3: Screen Resolution (Tuples & Immutability)

print("PART 3: Tuple Immutability")

screen_res = (1920, 1080)
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")

# screen_res[0] = 1280   # TypeError: Tuples cannot be modified

print("Tuples cannot be modified!")