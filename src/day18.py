# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 12:14:22 2026

@author: divya
"""
#task1
# STEP 1 — Import libraries
import sqlite3
import pandas as pd

# STEP 2 — Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("interns.db")
cursor = conn.cursor()

# STEP 3 — Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    intern_id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# STEP 4 — Insert sample data
sample_data = [
    (1, "Asha", "Data Science", 6000),
    (2, "Ravi", "Web Development", 4000),
    (3, "Kiran", "Data Science", 7500),
    (4, "Meena", "Cyber Security", 5500),
    (5, "Arjun", "Data Science", 4500),
    (6, "Neha", "Web Development", 6500)
]

cursor.executemany("INSERT OR REPLACE INTO interns VALUES (?, ?, ?, ?)", sample_data)
conn.commit()

# -------------------------------
# QUERY 1 — FILTER
# -------------------------------
query_filter = """
SELECT * FROM interns
WHERE track = 'Data Science'
AND stipend > 5000;
"""

df_filter = pd.read_sql_query(query_filter, conn)
print("Filtered Data (Data Science & stipend > 5000):")
print(df_filter)

# -------------------------------
# QUERY 2 — AGGREGATE (AVG)
# -------------------------------
query_avg = """
SELECT track, AVG(stipend) AS avg_stipend
FROM interns
GROUP BY track;
"""

df_avg = pd.read_sql_query(query_avg, conn)
print("\nAverage Stipend per Track:")
print(df_avg)

# -------------------------------
# QUERY 3 — COUNT
# -------------------------------
query_count = """
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track;
"""

df_count = pd.read_sql_query(query_count, conn)
print("\nTotal Interns per Track:")
print(df_count)

# STEP 5 — Close connection
conn.close()

#task2
import sqlite3
import pandas as pd

# Connect
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# Create tables
cur.execute("CREATE TABLE interns(id INT, name TEXT, track TEXT)")
cur.execute("CREATE TABLE mentors(id INT, mentor_name TEXT, track TEXT)")

# Insert data
cur.executemany("INSERT INTO interns VALUES (?, ?, ?)", [
    (1, "Asha", "Data Science"),
    (2, "Ravi", "Web Dev")
])

cur.executemany("INSERT INTO mentors VALUES (?, ?, ?)", [
    (1, "Dr Rao", "Data Science"),
    (2, "Mr Sharma", "Web Dev")
])

# INNER JOIN
query = """
SELECT i.name, i.track, m.mentor_name
FROM interns i
INNER JOIN mentors m
ON i.track = m.track
"""

df = pd.read_sql_query(query, conn)
print(df)

conn.close()
