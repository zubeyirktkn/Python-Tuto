def hanoi(n,x,y,z):
    
    if (n==1):
        
        print(f"Diski {x}'tan {z}'a taşıyın.")
        
    else:
        hanoi(n-1,x,z,y)
        """
        n=3 =>
            hanoi(2,x,z,y)//1.çubuktan 2.çubuğa taşır
                hanoi(1,x,z,y)//ekranda xten yye yani 1den 2ye yazar 
        """
        hanoi(1,x,y,z)
        hanoi(n-1,y,x,z)


x="1. çubuk"
y="2. çubuk"
z="3. çubuk"
n=int(input("Kaç adet disk vardır:"))

hanoi(n,x,y,z)