import re
result=""

#re module-------------------------------------------------

str="Zübeyir Zübayir Aktekin : Dünyanın En Boş İnsanı | 22 yaşında"

#re.findall() ilk parametreyi ikinci parametrede arar
#result=re.findall("Zübeyir",str)
#result=len(result)#kaç tane varsa onu yazar

#re.split() ilk parametreyi gördüğünde bölüp diziye eleman yapar
#result=re.split(" ",str)

#re.sub() 3. parametre içindeki 1. parametrelerin hepsini 2. parametreyle değiştirir
#result=re.sub(" ","-",str)#\s de boşluk demek

#re.search()
#result=re.search("Boş",str)
#result=result.span()
#result=result.start()
#result=result.end()


#regular expressions ------------------------------------------------

# result=re.findall("[abc]",str)
# result=re.findall("[sat]",str)
# result=re.findall("[a-e]",str)
# result=re.findall("[0-5]",str)
# result=re.findall("[^abc]",str)#abc dışındaki bütün karakterleri arar
# result=re.findall("[^0-9]",str)#0dan 9a kadar olanlar dışındakileri arar
#****
#result=re.findall("...",str)#kaç nokta koyarsan o kadar haneli elemanlara ayırır 
#result=re.findall("Züb..ir",str)
#****
#result=re.findall("^Züb",str)#z ile başlayan varsa döner
#****
#result=re.findall("aşında$",str)#x$  x ile bitiyor mu
#****
#result=re.findall("Zübe*yir",str)#?
#****
#result=re.findall("Zübe+yir",str)#?
#****
#result=re.findall("Zübe?yir",str)#?
#****
#result=re.findall("Z{2,3}",str)#?
#****
# a|b or
# (a|b|c)xz
#\$a 
#\aZüb karakter stringin başında mı
#yir\Z sonunda mı


print(result)