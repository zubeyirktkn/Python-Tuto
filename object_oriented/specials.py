myList = [1,2,3]
myString = "my string"

# print(len(myList))
# print(len(myString))


class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("Movie object has created!")
    
    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Movie has deleted.")
        

m1=Movie('My Movie',"Zubeyir",120)


print(str(myList))
print(str(m1))

print(len(myString))
print(len(m1))

#del m1 #object siler ,kullanılmadığında silinir object
