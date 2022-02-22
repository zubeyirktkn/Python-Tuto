liste =["1","2","5a","10b","abc","10","50"]

#liste elemanları içindeki sayısal değerleri bulunuz
'''
for i in liste:
    try:
        result=int(i)
        print(result)
    except ValueError:
        continue
'''

#kullanıcı 'q' girmedikçe alınan her inputun sayı olduğundan emin olun
"""
while True:
    try:
        number=input("Bir sayı girin:")
        if(number=="q"):
            break
        else:
            int(number)
    except Exception as ex:
        print("Sayı girmediniz.Sayı girdiğinizden emin olun!")
"""    


#girilen parola içinde türkçe karakter hatası verin
"""
def checkPassword(parola):

    turkce_karakterler = "şçğüıŞ"
    

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("parola türkçe karakter içeremez.")
        else:
            pass

parola = input("parola:")

try:
    checkPassword(parola)
except Exception as ex:
    print("Türkçe karakter içeremez!")
"""

#faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin

def factoriel(number):
    
    try:
        if number<1:
            raise ValueError("Negatif sayı!")
        elif(number==1):
            return 1
        else:
            return number*(factoriel(number-1))
    except Exception as ex:
        print("Wrong input!")

print(factoriel(-5))
