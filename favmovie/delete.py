import sqlite3

con = sqlite3.connect("movies_db")

print("Enter Movie year, which you want to delete: ")
my = input()

query = "delete from movies_info where myear=" + my

con.execute(query)
con.commit()

con.close()
print("Data deleted..")