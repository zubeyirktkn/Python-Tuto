def square(num):
    return num**2

isimLambda=lambda num:num**2

numbers=[1,2,3,4]

result=list(map(square,numbers))#map numberstaki elemanları sıra sıra squaree gönderir
for i in result:
    print(i)

result=list(map(lambda num:num**3,numbers))#lambda ifadesi fonksiyon görevi görür

print(isimLambda(3))
print(result)