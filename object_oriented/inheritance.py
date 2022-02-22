#inheritance(kalıtım):miras alma

#Person => name,lastname,age,eat(),run(),drink()
#Student(Person),Teacher(Person)

class Person():
    def __init__(self,fname,lname):
        print("Person Created!")
        self.firstName = fname
        self.lastName = lname
    def whomai(self):
        print("Im a person")
#---------------------------------------
class Student(Person): #persondan kalıtıldı init çalışır
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        print("Student Created!")
    
    def whomai(self):#override
        print("Im a student.")
#------------------------------------------------------
class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch=branch
    
    def whomai(self):
        print(f"I am a {self.branch} teacher.")

#--------------------------------------------------

p1 = Person('zet','ey')
s1 = Student('zuyb','ak')
t1 = Teacher('Zübeyir','Aktekin','Physics')

p1.whomai()
s1.whomai()
t1.whomai()