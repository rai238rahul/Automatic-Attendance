

import sqlite3
conn=sqlite3.connect("students.db")


cmd="SELECT * FROM STUDENTS"
cursor=conn.execute(cmd)
for row in cursor:
    print(row)		 
print("Table created succesfully")

conn.commit()
conn.close()
