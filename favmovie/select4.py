import sqlite3

con = sqlite3.connect("movies_db")

query = "select * from movies_info"

cur = con.cursor()
cur.execute(query)

while True:
    data = cur.fetchone()
    if data !=None:
        print(data)
    else:
        break

cur.close()
con.close()