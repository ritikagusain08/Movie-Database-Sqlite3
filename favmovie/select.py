import sqlite3

con = sqlite3.connect("movies_db")

cur = con.cursor()

query = "select * from movies_info"
cur.execute(query)
data = cur.fetchall()

print("Type of data is : ", type(data))
print("\n")

for d in data:
    print("Year of release:", d[0])
    print("Movie name:",d[1])
    print("Lead Actor:",d[2])
    print("Lead Actress:",d[3])
    print("Movie Director:",d[4])
    print()


cur.close()
con.close()