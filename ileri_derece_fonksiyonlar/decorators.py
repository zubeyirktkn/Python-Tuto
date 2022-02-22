"""
def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator#sayhelloyu decoratore gönderir
def sayHello(name):
    print("Hello "+name)

sayHello("ali")
"""
import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)

        func(*args,**kwargs)

        finish=time.time()
        print(func.__name__+" fonksiyonunun çalışma süresi:"+str(finish-start))
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))


usalma(2,3)
faktoriyel(4)