
import json
import os

class User:#user classı sayesinde her oluşturulan user için aynı özellikleri tutan bir yerimiz oluyor
    def __init__(self,username,password,email):#User sınıfına ait bi obje üretildiğinde init çalışır ve obje üretilirken girdiğiniz biligleri sınıf içindeki bilgilere eşitler

        self.username=username
        self.password=password
        self.email=email

#repository**************************************************************
class UserRepository:#repository objesi oluşturarak kullanıcıların işlemlerini tutan bir sınıfımız oluyor her kullanıcı için ayrı ayrı bu işlemleri yapmak yerine 1 sınıf sayesinde her kullanıcı için login logout vb işlemlere ulaşabiliyoruz

    def __init__(self):#repostiroy objesi oluşturulunca ilk çalışan init methodudur ve ve gerekli liste  ve objeleri ve fonksiyonları barındıırır
        self.users = []#users kullanıcıları tutan bir liste ileride dosyaya listeden yazmak için kullanılır
        self.isLoggedIn = False#güncel giriş yapılma bilgisini tutar 
        self.currentUser = {}#güncel giriş yapan kişinin bilgisini tutar

        #load users from .json file
        self.loadUsers()#json dosyasına yazılan bilgileri json dosyasından okuyup uygulamamızdaki bir listeye atar gerekince kullanmak için
    #---------------------------------
    def loadUsers(self):
        if os.path.exists("users.json"):#dosya var mı yok mu kontrol ediliyor eğer varsa ife giriliyor
            with open("users.json","r",encoding="utf-8") as file:#dosya okuma modunda açılıyor 
                users = json.load(file)#dosyadaki bilgiler load formülüyle alınıp users nesnesine veriliyor türüne bakman lazım type() ile..
                for user in users:#users üzerinden bütün json dosyasındaki kişileri geziyor sıra sıra
                    user=json.loads(user)#bunları usera erişilebilir bilgi olarak yüklüyor burası olmasa userin içinde obje bulunuyor
                    newUser = User(username=user["username"],password=user["password"],email=user["email"])#burada newUser'a dict yapısına dönüştürülen json fileın bilgileri çekilir
                    self.users.append(newUser)#bu sınıfın içindeki yani UserRep  içindeki usersa yeni kullanıcı bilgilerini appendle ekler 
            print(self.users)

    #---------------------------------
    def register(self,user:User):#User classı türünde bir user objesi alınır parametre olaarak
        self.users.append(user)#bu sınıfın yani UserRepo sınıfının içindeki users listesine user nesnesini ekler
        self.saveToFile()#dosyaya kaydet fonksiyonu içinde bu bilgiler json dosyasına yazılır
        print("User registered!")
    #----------------------------------
    def login(self,username,password):#kullanıcı adı ve şifre parametreleriyle giriş yapma methodu çağırılır
        
        for user in self.users:#user aracılığıyla users listesindeki kullanıcılar tek tek gezilir
            if user.username==username and user.password==password:#eğer kullanıcı adı ve şifre aynı olan bir kullanıcıya denk gelinirse true döner ife girilir
                self.isLoggedIn=True#birisinin giriş yaptığı bilgisi True yapılır
                self.currentUser=user#user kişisi currentUsera atanır
                print("Logged in!")
                break
        
    def logout(user):#çıkış yapma
        repository.isLoggedIn = False#login biligisi falsea çekilir
        repository.currentUser={}#şimdiki kullanıcı biligisi silinir
        print("Logged out!")
        
    def identity(self):
        if self.isLoggedIn :
            print(f"username:{self.currentUser.username}")
        else:
            print("Didnt log in!")
    
    #----------------------------------
    def saveToFile(self):
        list=[]

        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open("users.json","w") as file:
            json.dump(list,file)
    #----------------------------------

repository = UserRepository()#döngü içinde tanımlamamaya dikkat et sürekli tanımlanırsa sıfırlanır 

#iskelet*********************************************************************

while True:
    print("Menü".center(50,"*"))
    secim=input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nChoice:")
    
    if secim == "5":
        break
    else:
        if secim=="1":#register
            username=input("Username:")
            password=input("Password:")
            email=input("Email:")

            user= User(username=username,password=password,email=email)
            repository.register(user)

        elif secim=="2":
            #login
            if repository.isLoggedIn:
                print("Already Logged In!")
            else:
                username=input("username:")
                password=input("password:")
            
                repository.login(username,password)
        elif secim=="3":
            #logout
            repository.logout()
        elif secim=="4":
            #identity show
            repository.identity()
        else:
            print("Yanlış seçim!")
