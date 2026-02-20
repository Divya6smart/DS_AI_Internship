# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 12:14:22 2026

@author: divya
"""

import sqlite3

# Connect to database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# -------------------------------
# 1️⃣ FILTER: Data Science interns with stipend > 5000
# -------------------------------
print("Filtered Interns (Data Science & stipend > 5000):")

cursor.execute("""
SELECT name, stipend
FROM interns
WHERE track = 'Data Science' AND stipend > 5000
""")

filtered_rows = cursor.fetchall()
for row in filtered_rows:
    print(row)


# -------------------------------
# 2️⃣ AGGREGATE: Average stipend per track
# -------------------------------
print("\nAverage Stipend Per Track:")

cursor.execute("""
SELECT track, AVG(stipend)
FROM interns
GROUP BY track
""")

avg_rows = cursor.fetchall()
for row in avg_rows:
    print(row)


# -------------------------------
# 3️⃣ COUNT: Number of interns per track
# -------------------------------
print("\nIntern Count Per Track:")

cursor.execute("""
SELECT track, COUNT(*)
FROM interns
GROUP BY track
""")

count_rows = cursor.fetchall()
for row in count_rows:
    print(row)

# Close connection
conn.close()