import sqlite3

con = sqlite3.connect("movies_db")

#  Insert Data
print("Enter Movie Name: ")
mn = input()

print("Enter lead actor: ")
mar = input()

print("Enter lead actress: ")
mas = input()

print("Enter movie director: ")
md = input()

print("Enter movie release year: ")
my = input()

query = "insert into movies_info(myear,mname,mactor,mactress,mdirector) values (" + my + ",'" + mn + "','" + mar + "','" + mas + "','" + md + "')"

con.execute(query)
con.commit()

con.close()

print("Data Saved...")
