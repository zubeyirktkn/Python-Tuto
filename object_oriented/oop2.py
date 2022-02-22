class Circle:
    #class object attribute
    pi=3.14 #her oluşan obje için aynı olması için global değişken gibi oluşur


    def __init__(self,r=1):
        self.yaricap=r

    #methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)

c1=Circle() #r=1
c2= Circle(5) #r=5

print(f"c1:alan={c1.alan_hesapla()},c1:cevre={c1.cevre_hesapla()}\nc2:alan={c2.alan_hesapla()},c2:cevre={c2.cevre_hesapla()}")
