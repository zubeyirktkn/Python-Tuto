import mysql.connector
from mysql.connector import connection

mydb=mysql.connector.connect(
    host="localhost",    #192.23.45.56
    user="root",
    password="56295141iP",
    database="mydatabase"
)

mycursor=mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW DATABASES")
#mycursor.execute("CREATE DATABASE mydatabase")

