"""
def cube():
    for i in range(5):
        yield i ** 3#üretilip siliniyor tek kullanımlık 
        #bu return gibi değil fonksiyon bir iterable obje döndürüyor
#generator = cube()#generatore iterable objeyi atıp

#iterator=iter(generator)#iterator değişkenine generatorden oluşan iteratoru atıp
#aslında buna da gerek yok generator bir iterator oluşturuyor

iterator = cube()
"""
"""
print(next(iterator))#üzerinde gezinebiliyoruz
print(next(iterator))#bu işlem bellekte yer kaplamıyor
print(next(iterator))
"""
"""
for i in cube():
    print(i)
"""
liste = [i**3 for i in range(5)]#generator değil liste oluşur
generator = (i**3 for i in range(5))#listeye generator atar
print(liste)
print(next(generator))