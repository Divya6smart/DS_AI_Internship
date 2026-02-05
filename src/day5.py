# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 18:13:33 2026

@author: divya
"""

# ---------- Day 5 : Functions Module ----------

def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def power(base, exp):
    return base ** exp

def average(numbers_list):
    return sum(numbers_list) / len(numbers_list)

# ---------- Main Program ----------

# Rectangle calculation
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area, perimeter = calc_rectangle(length, width)
print(f"Rectangle -> Area: {area}, Perimeter: {perimeter}")

# Power and Average
print("2^10 =", power(2, 10))
nums = [10, 20, 30, 40]
print("Average of", nums, "is", average(nums))