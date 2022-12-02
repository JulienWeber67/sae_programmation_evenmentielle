"""connect
while :
    envoi

    reception

    fermeture socket"""

import socket
import threading

host = "localhost"
port = 10000

print(f"Ouverture de la socket sur le serveur {host} port {port}")
client_socket = socket.socket()
client_socket.connect((host, port))
print("Serveur est connecté")

data = ("")

while  data != 'disconnect':

    message = input("Message au serveur : ")
    client_socket.send(message.encode())
    print("Message envoyé")

    data = client_socket.recv(1024).decode()
    print(f"Message du serveur : {data}")

# Fermeture de la socket du client
client_socket.close()
print("Socket fermée")
