from mysql.connector import connection
import mysql.connector
import datetime


def insertStudents(list):
    connection=mysql.connector.connect(
    host="localhost",    #192.23.45.56
    user="root",
    password="56295141iP",
    database="schooldb"
    )
    mycursor=connection.cursor()#cursor oluşturduk bağlantıyı kurduk

    sql="INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) Values(%s,%s,%s,%s,%s)"

    values=list

    mycursor.executemany(sql,list)#execute ile sql komutuna liste değerlerini yolladık listeyi içeriğini kullanıcıdan alacağız

    try:
        connection.commit()# executemany ve execute commitle çalışmasını tamamlar


    except  mysql.connector.Error as err:
        print(err)

    finally:
        connection.close()

ogrenciler=[
    ("101","Ahmet","Yılmaz",datetime.datetime(2005,5,17),"E"),
    ("102","Ali","Can",datetime.datetime(2005,6,17),"E"),
    ("103","Canan","Tan",datetime.datetime(2005,7,7),"K"),
    ("104","Ayşe","Taner",datetime.datetime(2005,9,23),"K"),
    ("105","Bahadır","Toksöz",datetime.datetime(2004,7,27),"E"),
    ("106","Ali","Cenk",datetime.datetime(2003,8,25),"E")

]

insertStudents(ogrenciler)

"""
while True:
    StudentNumber=input("Öğrenci numarası:")
    Name=input("Öğrenci Adı:")
    Surname=input("Öğrenci soyadı:")
    Birthdate=datetime(input("Öğrenci doğum tarihi:"))
    Gender=input("Öğrenci cinsiyeti:")
    
    list.append((StudentNumber,Name,Surname,Birthdate,Gender))

    result=input("Girişe devam etmek ister misiniz(e/h):")
    if result=="h":
        insertStudents(list)
        print("Kayıtlarınız veritabanına iletildi.")        
        break
    elif result=="e":
        continue
    else:
        print("yanlış giriş yaptınız e veya h yazınız şimdilik kayıt işlemine devam edilecek:")
"""
