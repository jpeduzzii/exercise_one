import sqlite3
import pandas as pd
conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()

query = """
    SELECT *
    FROM teams
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

cities = ()
for record in records:
    cities +=(len(record[1]),(record[1]))
# len of city + city is the tuple
print(cities)
