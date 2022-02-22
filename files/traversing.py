#file = open("newfile2.txt","w",encoding="utf-8")
#file.write("0123456789abcçdefgğhıijklmnoöprsştuüvyz")

with open("newfile2.txt","r",encoding="utf-8") as file:
    content=file.read()
    print(content)

    file.seek(10)#cursorun yerini değiştir
    print(file.tell())#cursorun yerini öğren
    
    content2=file.read()
    print(content2)
