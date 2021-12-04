import sqlite3

con = sqlite3.connect("movies_db")

cur = con.cursor()

query = "select mactor from movies_info where mname=Venom"
cur.execute(query)
data = cur.fetchall()


for d in data:
    print("Movie name:",d[1])
    print("Lead Actor:",d[2])
    print()


cur.close()
con.close()