#dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
#kullanımı: open(dosya_adi,dosya_erişim_modu)
#dosya_erişim_modu=> dosyayı hangi amaçla açtığımız

#"w":(Write) yazma modu.Dosyayı konumda oluşturur.
#dosyayı oluşturup açar içine bir şey yazarsan önceki yazılanlar silinir
#aynı isimli dosya varsa eskisini silip yenisini oluşturur
"""
file=open("C:/users/zubey/desktop/newfile.txt","w")
print(file)
file.close()
file=open("newfile.txt","w",encoding="utf-8")
file.write("Zübeyir Aktekin")
file.close()
"""
#"a":(Append) ekleme.Doya konumda yoksa oluşturur.
"""
file=open("newfile.txt","a",encoding="utf-8")
file.write("Harun aktekin\n")
file.close()
"""

#"x":(create) oluşturma.Dosya zaten varsa hata verir.
"""
file=open("newfile2.txt","x",encoding="utf-8")
file.close()
"""

#"r":(read) okuma.varsayılan.Dosya konumda yoksa hata verir.

file=open("newfile.txt","r")
