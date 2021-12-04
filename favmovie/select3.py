import sqlite3

con = sqlite3.connect("movies_db")

query = "select * from movies_info"

cur = con.cursor()
cur.execute(query)

data1 = cur.fetchone()
print(data1)

data2 = cur.fetchone()
print(data2)

cur.close()
con.close()