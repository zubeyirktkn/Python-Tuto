import mysql.connector

def getProducts():
    connection=mysql.connector.connect(
                host="localhost", 
                user="root",
                password="56295141iP",
                database="node-app"
        )
    cursor=connection.cursor()

    #cursor.execute("Select * From Products Where id=1")#idsi1 olanı al
    #cursor.execute("Select * From Products Where name='zetphone' or price>=3000")
    #cursor.execute("Select name,price From Products")
    #cursor.execute("Select * From Products Where name LIKE '%Samsung%'")
    cursor.execute("Select * From Products Where name LIKE '%Samsung%' and price=1000")

    result=cursor.fetchall()
    #result=cursor.fetchone()
    #print(f"name:{result[0]},price:{result[1]}")
    
    
    for product in result:
            print(f"id:{product[0]},name:{product[1]} ,price:{product[2]}")
            #print(f"name:{product[0]} ,price:{product[1]}")
    
    
def getProductById(id):
    connection=mysql.connector.connect(host="localhost",user="root",password="56295141iP",database="node-app")
    cursor = connection.cursor()

    sql="Select * From Products Where id=%s"
    params=(id,)
    cursor.execute(sql,params)
    result= cursor.fetchone()

    print(f"id:{result[0]},name:{result[1]} ,price:{result[2]}")

getProductById(1)

#getProducts()