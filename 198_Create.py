import mysql.connector

conn =mysql.connector.connect(host="localhost",database="mydbMK",user="root",password="Direwolf19Meng$")

if conn.is_connected():
    print("Connected to mysql db")

cursor = conn.cursor()

try:
    cursor.execute("insert into emp values(3,'Abby',30000)")
    conn.commit()
    print("Employee added")
except:
    conn.rollback()

cursor.close()
conn.close()