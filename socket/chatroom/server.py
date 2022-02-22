import threading
import socket
 
host=socket.gethostbyname(socket.gethostname())
port=55555
 
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
server.bind((host,port))#client ile bağlantı
server.listen()#dinleme

clients=[]
nicknames=[]

def broadcast(msg):
    for client in clients:
        client.send(msg)#mesaj gönderme

def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast(f"{nickname} left the chat.".encode("ascii"))        
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client,address=server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode("ascii"))
        nickname=client.recv(1024).decode("ascii")#recv
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat!.".encode("ascii"))
        client.send("Connected to server!".encode("ascii"))

        thread=threading.Thread(target=handle,args=(client,))
        thread.start()

print("Server is listening...")
receive()