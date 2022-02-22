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


def getProducts():
    connection=mysql.connector.connect(
                host="localhost", 
                user="root",
                password="56295141iP",
                database="node-app"
        )
    cursor=connection.cursor()

    #cursor.execute("Select * From Products")#tüm kolonları al
    cursor.execute("Select name,price From Products")
    
    #result=cursor.fetchall()
    result=cursor.fetchone()
    print(f"name:{result[0]},price:{result[1]}")
    """
    for product in result:
            #print(f"name:{product[1]} ,price:{product[2]}")
            print(f"name:{product[0]} ,price:{product[1]}")
    """








getProducts()
