#value type
x=5
y=25

x=y #x =25

y=10 # y= 10 x değişmez

print(x,y) # x= 25, y=10

#reference type

a =["apple","banana"]
b=["apple","banana"]
a=b # a ve b eşitlendikten sonra adresleri aynı oluyor
b[0]="grape"

print(a,b)