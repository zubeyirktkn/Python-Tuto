"""
def greeting(name="there"):
    print("hello "+name)

greeting("ali")


sayHello = greeting #adresslerini aynı yapar

print(sayHello)
print(greeting)

del sayHello #say hello definition silinir 
#print(sayHello)#hata verir
print(greeting)
"""
"""
#encapsulation
def outer(num1):
    print("outer")
    def inner_increment(num1):#yalnızca outer fonksiyonunda çalışır
        print("inner")
        return num1+1

    num2=inner_increment(num1)
    print(num1,":",num2)
outer(10)
"""
def fact(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer!")
    if not number >=0:
        raise ValueError("number must be zero or positive!")
    def inner_fact(number):
        if number <=1:
            return 1
        return number* inner_fact(number-1)
    
    return inner_fact(number)
try:
    print(fact("a"))
except Exception as ex:
    print(ex)