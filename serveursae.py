
"""while msgclient != 'kill':
#ouverture socket

while msgclient != 'kill' and msgclient != 'reset' :
#accept

while msgclient != "disconnect" and msgclient != "kill" and msgclient != "rest":
#reception
if msgclient !=  "disconnect":
#envoi
else: #envoi de disconnect

fermeture client

fermeture serveur"""

import socket
import threading

msgclient =''
message =""
while message != "kill":

    host = "localhost" # "", "127.0.0.1
    port = 10000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)

    while message != 'kill' and message != 'reset' :

        print('En attente du client')
        conn, address = server_socket.accept()
        print(f'Client connecté {address}')

        while message != "disconnect" and message != "kill" and message != "reset":

            # Réception du message du client
            msgclient = conn.recv(1024) # message en by
            message = msgclient.decode()
            print(f"Message du client : {message}")

            #if message != "disconnect":
                # J'envoie un message
            reply = input("Saisir un message : ")
            conn.send(reply.encode())
            print(f"Message {reply} envoyé")

            #else:

            #reply = "disconect"
            #conn.send(reply.encode())

        # Fermeture
        conn.close()
        print("Fermeture de la socket client")
        if message == "disconnect":
            message = ""
    server_socket.close()
    print("Fermeture de la socket serveur")
    print("rebooting")
    if message == "reset":
        message = ""
