from mysql.connector import connection
import mysql.connector

def insertProduct(name,price,imageUrl,description):        
        connection=mysql.connector.connect(
                host="localhost", 
                user="root",
                password="56295141iP",
                database="node-app"
                )

        cursor = connection.cursor()

        sql="INSERT INTO Products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
        values=(name,price,imageUrl,description)
        cursor.execute(sql,values)

        try:
                connection.commit()#sorguyu databasee gönder
                print(f"{cursor.rowcount} tane kayıt eklendi")
                print(f"Son eklenen kayıtın idsi:{cursor.lastrowid}")
        except mysql.connector.Error as err:
                print("hata",err)
        finally:
                connection.close()
                print("database bağlantısı kesildi")



def insertProducts(list):        
        connection=mysql.connector.connect(
                host="localhost", 
                user="root",
                password="56295141iP",
                database="node-app"
                )

        cursor = connection.cursor()

        sql="INSERT INTO Products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
        values=list
        cursor.executemany(sql,values)

        try:
                connection.commit()#sorguyu databasee gönder
                print(f"{cursor.rowcount} tane kayıt eklendi")
                print(f"Son eklenen kayıtın idsi:{cursor.lastrowid}")
        except mysql.connector.Error as err:
                print("hata",err)
        finally:
                connection.close()
                print("database bağlantısı kesildi")


list=[]
while True:
        name=input("ürün adı:")
        price=float(input("ürün fiyatı:"))
        imageUrl=input("ürün fotoğrafı:")
        description=input("ürün açıklaması:")
        
        list.append((name,price,imageUrl,description))

        result=input("Devam etmek istiyor musunuz?(e/h)")
        if result=="h":
                print("Kayıtlarınız veritabanına iletildi.")
                print(list)
                insertProducts(list)
                break
        else:
                continue
#insertProduct(name,price,imageUrl,description)