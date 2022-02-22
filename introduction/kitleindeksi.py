kilo=float(input("Kilonuz="))
boy=float(input("Boyunuz(cm)="))

vki=kilo/(boy**2)

print(f"Vücut kitle indeksiniz {vki}.")

saglikDurumu=(vki<=25) and (vki>20)

if(saglikDurumu==1):
    print("Sağlıklısınız.")
else:
    print("Sağlıksızsınız.")