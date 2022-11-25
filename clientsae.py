from threading import Thread
import socket
import platform

def Sending(socket):
    while True :
        msg = input()
        msg = msg.encode('utf-8')
        if msg == 'disconnect':
            print('close')
            break
        socket.send(msg)


def Reception(socket):
    while True:
        requete_server = socket.recv(500)
        requete_server = requete_server.decode("utf-8")
        if not requete_server : #Server disconnect
            print("CLOSE connexion")
            break
        if requete_server == 'disconnect' :
            print('closing')
            break
        print(requete_server)

Host = "localhost"
Port = 18000

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((Host,Port))

envoi = Thread(target=Sending,args=[socket])
reception = Thread(target=Reception,args=[socket])

envoi.start()
reception.start()