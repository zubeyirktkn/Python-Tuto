#identity operator: is

x=y=[1,2,3]

z=[1,2,3]

print(x==y)#içerdiği değerler aynı
print(x==z)#içerdiği değerler aynı

print(x is y) #adresler aynı
print(x is z) #false adresler aynı değil
print(x is not z)#true gelir adresler farklı

#membership operator: in

x=['apple','banana']
print('banana' in x) #true
print('strawberry' not in x) # true