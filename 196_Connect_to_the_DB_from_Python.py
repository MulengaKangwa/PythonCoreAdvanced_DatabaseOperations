import mysql.connector

conn =mysql.connector.connect(host="localhost",database="mydbMK",user="root",password="Direwolf19Meng$")

if conn.is_connected():
    print("Connected to mysql db")

cursor = conn.cursor()

cursor.execute('select * from emp')

row = cursor.fetchone()

while row is not None:
    print(row)
    row=cursor.fetchone()

cursor.close()
conn.close()