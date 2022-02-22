#oop

#class => person(name,surname,birthday,calculateAge())

class Person:
    #pass #dolu gibi göster
    #class attributes
    adress="no info"
    #constructer(yapıcı method) object oluşur oluşmaz çalışır default setting gibi
    def __init__(self,name,year):
        #object attributes
        self.name=name
        self.year=year
        print('init methodu çalıştı!')
    #---------------------------------
    #istance methods
    def intro(self):
        print("Hello There. I am "+ self.name)
    
    def calculateAge(self):
        return 2021-self.year
    


#object (instance) 
p1 = Person('Zet',1999)
p2 = Person('Ali',2000)

#updating
p1.name='ahmet'
p1.adress='mersin'
p2.adress='istanbul'

#accessing object attributes
p1.intro()
p2.intro()

print(f"Adım:{p1.name},Yaşım:{p1.calculateAge()}\nAdım:{p2.name},Yaşım:{p2.calculateAge()}")


