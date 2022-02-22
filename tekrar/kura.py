#girilen id no lar için kura çekip bi numara seçecek bir uygulama
#kura uygulamasını geliştirip sadece girilen sayılardan kura çekilebilir
#üzerine düşün class yapısını nerede kullanabileceğini düşün
from os import system
import random

def menu():
    print("*"*30+"KURA UYGULAMASINA HOŞGELDİNİZ"+"*"*30)
    while True:
        print("1)Kişileri gir.\n2)Kişi çıkar.\n3)Kura çek.\n4)Çıkış.")
        choice=input()
        if int(choice)==1:
            kisiGir()
        elif int(choice)==2:
            kisiCikar()
        elif int(choice)==3:
            kuraCek()
        elif int(choice)==4:
            break
        else:
            print("Yanlış girdi.")


def kisiGir():
    while True:
        kisi=input("İsim Soyisim:")
        kisiID=input("Id:")

        with open("kisiler.txt","a",encoding="utf-8") as file:
            file.write(kisi+":"+kisiID+"\n")
        
        choice=input("Menuye dönmek için -1 girin devam etmek için rastgele bir girdi!:")
        if choice=="-1":
            break
        else:
            continue
        

def kisiCikar():#kişi çıkarırken işaretli bölgeyi yapamdım
    pass
    """
    while True:
        name=input(("Çıkarılacak kişinin isim soyisim:"))
        id=input("Çıkarılacak kişinin id:")

        with open("kisiler.txt","r+",encoding="utf-8") as file:
            liste=file.readlines()
            x=f"{name}:{id}"#buradan----------
            print(liste[0]) 
            print(x)
            #liste=liste.remove(x)
            #file.writelines(liste)#buraya-----
        choice=int(input("Çıkmak için -1 devam etmek için rastgele girdi!:"))
        try:
            if choice==-1:
                break
            else:
                continue
        except Exception:
            print("Yanlış")
"""

def kuraCek():
    with open("kisiler.txt","r",encoding="utf-8") as file:
        liste=file.readlines()
        result=random.randint(0,len(liste)-1)
        print(f"Kazanan:{liste[result]}")

menu()

