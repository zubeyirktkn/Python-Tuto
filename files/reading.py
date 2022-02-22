file=open("newfile.txt","r",encoding="utf-8")

#for ile okuma************************************
"""
for i in file:
    print(i,end="")
"""
#*********************************************
#read() fonksiyonu parametre vermezsen tüm dosyayı okur 
"""
print("içerik 1")
content1 = file.read()
print(content1)

print("içerik 2")
file=open("newfile.txt","r",encoding="utf-8")
content2=file.read()
print(content2)
"""

"""
content=file.read(5)#parametre alırsa 5 byte okur 5 karakter yani
content=file.read(2)#kaldığı yerden devam ediyor
print(content)
"""
#readline() fonksiyonu 1 satır okur *************************
"""
print(file.readline())
print(file.readline())
"""
#readlines() ********************************
"""
liste=file.readlines()
print(liste[0])
print(liste[1])
"""
#********************************************
#dosya içeriğini düzeltip tekar yapıyorum
"""
file=open("newfile.txt","w",encoding="utf-8")
file.write("Zübeyir Aktekin\nHarun Aktekin\nÖmer Aktekin")
"""
file=open("newfile.txt","r",encoding="utf-8")

#content=file.read()
#content=file.readline(5)
content=file.readlines()#her satırı listenin 1 elemanı olacak şekilde listeler

print(content[0])

file.close()