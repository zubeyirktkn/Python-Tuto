#girilen sayının asal olup olmadığını kontrol eden uygulama

num=int(input("Number="))
i=2
isPrime=0
while i<=num//2:
    if(num%i==0):
        print(f"{num} is not prime because it can be diveded by {i}.")
        isPrime+=1
        break
    i+=1
if(isPrime==0):
    print(f"{num} is a prime number!")
