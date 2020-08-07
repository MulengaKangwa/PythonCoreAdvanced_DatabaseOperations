import mysql.connector

mydb = mysql.connector.connect(host="localhost",database="mydbMK",user="root",password="Direwolf19Meng$")
import mysql.connector

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
sal = ("30000", "40000")

mycursor.execute(sql, sal)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")