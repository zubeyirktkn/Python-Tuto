"""
with open("newfile.txt","r+",encoding="utf-8") as file:#r+ modu hem okutur hem yazar
    file.seek(20)
    file.write("deneme")
"""
#sayfa sonunda güncelleme append
"""
with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("\nZeynep Aktekin")
"""
#sayfa başında güncelleme
"""
with open("newfile.txt","r+",encoding="utf-8") as file:#dosyayı r+da açtık
    content=file.read()#içeriği contente kopyaladık
    content="Rukiye Aktekin\n"+content#contentin başına ekleme yaptık
    file.seek(0)#cursoru başa getirdik dosyanın içinde
    file.write(content)#dosyanın başından contenti yazdık aslında content
    #içerikten uzun olduğu için içerik komple silinip yerine content yazıldı gibi düşünebiliriz
"""

#sayfa ortasında güncelleme
with open("newfile.txt","r+",encoding="utf-8") as file:
    liste=file.readlines()#listeye dönüştürülen fileı liste değişkenine attık.Dosya içeriği aynı!
    liste.insert(1,"Kübra Aktekin\n")#listeye 1 indexli elemandan önce verilen içeriği sokuşturduk.Dosya içeriği değişmedi hala!
    file.seek(0)#dosya içinde cursoru dosyanın başına aldık
    file.writelines(liste)#dosyanın içine write lines ile listeyi yazdık


with open("newfile.txt","r+",encoding="utf-8") as file:
    print(file.read())