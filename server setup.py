
import socket 
import threading 


ip = "192.168.100.7"
port = 55554  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((ip, port)) 
server.listen() 

clients = [] 
names = [] 

def send_message(message, client):
    for c in clients:
        if c != client:
            try:
                c.send(message)
            except:
                remove(c)

def remove(client): 
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        client.close()
        name = names[index]
        send_message(f"{name} has left the chat.".encode("utf-8"), None)
        names.remove(name)

def recieve_message(client):
    while True:
        try:
            message = client.recv(1024)
            send_message(message, client)
        except:
            remove(client)
            break


def connect(): 
    while True:
        client, address = server.accept()
        print(f"Connection established with {str(address)}")

        name = client.recv(1024).decode("utf-8")
        names.append(name)
        clients.append(client)


        join_message = f"JOIN:{name} has joined the chat!".encode("utf-8")
        send_message(join_message, None)


        thread = threading.Thread(target=recieve_message, args=(client,))
        thread.start()

print("Server Initiated, Looking For Connections ..........")
connect()
















