from typing import final
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

updateProduct(3,"ZetPhone4",7500)
getProducts()