import sqlite3

con = sqlite3.connect("movies_db")
print("Enter movie year of release, which you want to update: ")
my = input()

print("Enter movie name, which you want to update: ")
mn = input()

print("Enter lead actor, which you want to update: ")
mar = input()



query = "update movies_info set mname='" + mn + "',mactor='" + mar + "' where myear=" + my

con.execute(query)
con.commit()

con.close()

print("Data Updated..")