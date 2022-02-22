message='hello there.my name is ali veli'

message = message.upper()#tüm harfleri büyült
message=message.title()#başharfleri büyüt
message= message.strip()#baştaki boşluk sil
message = message.split() # boşluklardan böl parametre olarak verilen karakterden de bölebilir
message = message.find('ali') #searcg for the index of the first char of the parameter
message = message.replace('ali','mal') #yer değiştir
message=message.center(100) # paramtere büyüklüğünde alan oluşturup ortaya stringinizi koyar



print(message)