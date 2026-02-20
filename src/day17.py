# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 11:50:04 2026

@author: divya
"""

import sqlite3
# 1️⃣ Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# 2️⃣ Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

# 3️⃣ Insert sample data
intern_data = [
    (1, "Aisha", "Data Science", 8000),
    (2, "Rahul", "Web Dev", 6000),
    (3, "Sneha", "Data Science", 9000),
    (4, "Arjun", "AI/ML", 10000),
    (5, "Meera", "Web Dev", 7000)
]

cursor.executemany("INSERT OR REPLACE INTO interns VALUES (?, ?, ?, ?)", intern_data)

conn.commit()

# 4️⃣ Query only name and track
cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()

print("Intern Name and Track:")
for row in rows:
    print(row)

# 5️⃣ Close connection
conn.close()