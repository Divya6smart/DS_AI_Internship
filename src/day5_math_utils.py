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