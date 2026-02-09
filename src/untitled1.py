# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:17:59 2026

@author: divya
"""

file = open("content.txt", "w")
file.write("Hello, myself divya.")
file.close()

file = open("content.txt", "r")
content = file.read()
print(content)
file.close()

#create a data.csv file
import csv

with open("new_csv.csv"):
    for row in reader:
    print(row)