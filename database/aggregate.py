import mysql.connector

def getProductInfo():
    connection=mysql.connector.connect(host="localhost",user="root",password="56295141iP",database="node-app")
    cursor = connection.cursor()

    #sql="Select COUNT(*) From Products"#sayısını çevirir
    #sql="Select AVG(Price) From Products"#ortalamasını çevirir
    #sql="Select SUM(Price) From Products"
    #sql="Select MIN(Price) From Products"
    #sql="Select MAX(Price) From Products"
    sql="Select Name From Products Where Price=(Select MAX(Price) From Products)"
    
    cursor.execute(sql)
    result= cursor.fetchone()

    print(f"result: {result[0]}")


getProductInfo()