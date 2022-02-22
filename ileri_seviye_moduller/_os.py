import os
import datetime

result=os.name#işletim sistemi adı

#dizin değiştirme-------------------------------------------------
#os.chdir("C:\\")#bulunduğun dizini değiştir
#os.chdir("../../..")#.. arttıkça 1 dizin dışarı çıkılır

#klasör oluşturma----------------------------------------------------
#os.mkdir("newDirectory")#bulunduğun patha klasör oluşturur
#os.makedirs("C:\\newdirectory/yeniklasör")#c içine nd içine yk oluşturur
#os.rename("first_name","newname")#isim değiştirme
#os.rmdir("dirname")#alt dizini yoksa siler
#os.removedirs("klasöradı/klasöradı")#çoklu klasör silme

#listeleme------------------------------------------------------
#result=os.listdir()
#result=os.listdir("C:\\")
"""
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)
"""

#dizin öğrenme---------------------------------------------------
#result=os.getcwd()#aktif dosyanın path bilgisi


#result=os.stat("date.py")
#result=result.st_size/1024
#result=datetime.datetime.fromtimestamp(result.st_ctime)#oluşturulma
#result=datetime.datetime.fromtimestamp(result.st_atime)#acces son erişilme
#result=datetime.datetime.fromtimestamp(result.st_mtime)#modified date

#os.system("notepad.exe")

result=os.path.abspath("_os.py")#tam konum öğrenme
result=os.path.dirname("C:/Users/zubey/Desktop/python_temelleri/ileri_seviye_moduller/_os.py")#dizin ismi
result=os.path.dirname(os.path.abspath("_os.py"))#dizin adı elde etme
result=os.path.exists("_os.py")
result=os.path.isdir("C:/Users/zubey/Desktop/python_temelleri/ileri_seviye_moduller/_os.py")
result=os.path.isfile("C:/Users/zubey/Desktop/python_temelleri/ileri_seviye_moduller/_os.py")
result=os.path.join("C:\\","deneme","deneme1")
result=os.path.split("C:\\deneme")
result=os.path.splitext("_os.py")
result=result[0]#_os

print(result)
