import socket
import threading
from typing import Collection
 
nickname=input("Choose a nickname:")

host=socket.gethostbyname(socket.gethostname())#socket.gethostbyname(socket.gethostname())
port=55555

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
client.connect((host,port))

def receive():
    while True:
        try:
            message=client.recv(1024).decode("ascii")#burada türkçe karakter hatasını kontrol et
            if message=="NICK":
                client.send(nickname.encode("ascii"))
                
            else:
                print(message)
        except:
            print("An error occured!") 
            client.close()#burada clientı kapattıysak bile yeniden açmamız lazım veya türkçe karakter hatası için ayrı bir exception tanımlanması lazım
            break

def write():
    while True:
        message=f"{nickname}:{input('')}"
        client.send(message.encode("ascii"))

#multi threading yapısı
receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()
