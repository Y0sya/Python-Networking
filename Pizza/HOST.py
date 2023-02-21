import socket
import threading

HOST='10.26.203.44'
PORT=55555

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

#clients=[]
#user_type=[]

clients={}
prompts=["USERNAME","PASSWORD","TYPE"]
orders=[]
def driver_orders(client):
    for order in orders:
        client.send(order.encode('utf-8'))
    client.recv(1024)
def customer_menu():
    print("ORDERS SIR")

def handle(client):
    while True:
        try:
            if clients[client][3]=="driver":
                driver_orders(client)
            elif clients[client][3]=="customer":
                customer_menu(client)
            else:
                client.send("Error, try again. Connection closing".encode('utf-8'))
                client.close()
                break
        except:
            print(f"{clients[client][1]} has left.")
            clients.remove(client)
            client.close()
            break
#'''
def obtain_credentials(client, credential, clients):
    client.send(credential.encode('utf-8'))
    clients[client].append(client.recv(1024).decode('utf-8'))
    
def new_connection():
    while True:
        client, address=server.accept()
        clients[client]=[]
        clients[client].append(address)
        print(f"Connected to {address}.")
        for prompt in prompts:
            obtain_credentials(client, prompt, clients)
        print(clients)
        client.send("Connected to server".encode('utf-8'))
        print(f"{clients[client][0]} connected as {clients[client][1]}, with password {clients[client][2]}, and of type {clients[client][3]}")
        thread=threading.Thread(target=handle, args=(client,))
        thread.start()
    
new_connection()