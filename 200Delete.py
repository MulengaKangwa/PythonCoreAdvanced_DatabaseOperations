import mysql.connector

def delete(id):
    conn =mysql.connector.connect(host="localhost",database="mydbMK",user="root",password="Direwolf19Meng$")

    if conn.is_connected():
        print("Connected to mysql db")
        cursor = conn.cursor()
        str = "delete from emp where id='%d'"
        args=(id)
        try:
            cursor.execute(str % args)
            conn.commit()
            print("Employee Delete")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

empid = int(input('Enter Emp Id:'))
delete(empid)