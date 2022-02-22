#value type parameters
# def changeName(n):
#     n='zet'

# name = 'zubeyir'

# changeName(name)
# print(name)

#list(reference type) parameters
# def change(n):
#     n[0]='istanbul'

# sehirler= ['ankara','izmir']
# change(sehirler)
# print(sehirler)

#parametre sınırı olmaması için * tuple list parametre girilebilir
# def add(*params):
#     return sum(params)

# print(add(20,10,20,40,80))

#parametre sınırı yok ancak veri tipleri farklı ise ** dictinary parametre verilir
def displayUser(**args):
    for key,value in args.items():
        print("{} is {} ".format(key,value))


displayUser(name='zet',age=22,city='mersin')

def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
