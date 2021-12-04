import sqlite3

con = sqlite3.connect("movies_db")

query = "select * from movies_info"

cur = con.cursor()
cur.execute(query)

data = cur.fetchmany(2)
print(data)

cur.close()
con.close()