from threading import Thread
import sys
import socket
import platform

def Send(client):
    while True:
        msg = input()
        msg = msg.encode("utf-8")
        client.send(msg)

def Reception(client):
    while True:
        request_client = client.recv(500)
        request_client = request_client.decode('utf-8')
        print(request_client)
        if request_client == "kill":
            print("SERVER IS DEAD, Please press enter and start the server later")
            sys.exit()
        if not request_client : #Client disconnect
            print("CLOSE connexion")
            break


Host = "localhost"
Port = 18000

#Création du socket

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((Host,Port))
socket.listen(1)

client, ip = socket.accept()
print("Le client d'ip",ip,"s'est connecté")

envoi = Thread(target=Send,args=[client])
reception = Thread(target=Reception,args=[client])

envoi.start()
reception.start()

reception.join()

client.close()
socket.close()

