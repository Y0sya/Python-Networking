import socket
import threading

HOST='10.26.203.44'
PORT=55555

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
nickname=input("Nickname")

def recieve():
    while True:
        try:
            message=client.recv(1024).decode('utf-8')
            if message=="NICKNAME":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("ERROR")
            client.close()
            break

def write():
    while True:
        message=(nickname+input(''))

recieve_thread=threading.Thread(target=recieve)
recieve_thread.start

write_thread=threading.Thread(target=write)
write_thread.start
