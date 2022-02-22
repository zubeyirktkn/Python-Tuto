from mysql import connector
import mysql.connector
from mysql.connector import connection
from mysql.connector import errors
from mysql.connector.errors import Error
from mysql.connector.fabric import connect

#connection=connection=mysql.connector.connect(host="localhost",user="root",password="56295141iP",database="node-app")
def getProducts():
    connection=mysql.connector.connect(host="localhost",user="root",password="56295141iP",database="node-app")
    cursor=connection.cursor()
    sql="Select name,price from Products "
    cursor.execute(sql)
    results=cursor.fetchall()

    for result in results:
        print(f"{result[0]} {result[1]}")


def updateProduct(id,name,price):
    connection=mysql.connector.connect(host="localhost",user="root",password="56295141iP",database="node-app")
    cursor=connection.cursor()

    sql="Update Products Set name=%s,price=%s where id=%s"
    params=(name,price,id)

    cursor.execute(sql,params)

    try:
        connection.commit()#sorguyu databasee gönder
        print(f"{cursor.rowcount} tane kayıt güncellendi")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database bağlantısı kesildi")


def deleteProduct(id):
    connection=mysql.connector.connect(host="localhost",user="root",password="56295141iP",database="node-app")
    cursor=connection.cursor()

    sql="delete from Products where id=%s"
    #sql="delete from products where name like '%Hua%'"
    params=(id,)

    cursor.execute(sql,params)

    try:
        connection.commit()#sorguyu database'e gönder
        print(f"{cursor.rowcount} tane kayıt silindi")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database bağlantısı kesildi")


#deleteProduct(7)
updateProduct(1,"ZetPhone2",9000)
getProducts()