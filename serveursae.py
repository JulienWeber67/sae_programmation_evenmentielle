
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
import psutil
import platform
import pyautogui
import os
import csv

msgclient =''
message =""
while message != "kill":

    host = "0.0.0.0" # "", "127.0.0.1
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

            with open('testing.csv', 'w', newline='') as csvfile:
                fieldnames = ['port', 'machine']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerow({'port': port, 'machine': address})

            if message == "commande":
                value = pyautogui.prompt("Enter Shell Command")
                stream = os.popen(value)
                out = stream.read()
                pyautogui.alert(out)

            if message == "OS" :
                i = platform.system()
                k = platform.release()
                u = platform.platform()

                reply = f"nom:{i},version :{k},platform :{u}"
                conn.send(reply.encode())

            if message == "RAM":
                reply = f"'ram total : {psutil.virtual_memory()[0] } 'bits'"
                conn.send(reply.encode())
                reply = f"'ram utilisé :{psutil.virtual_memory()[3]} 'bits' "
                conn.send(reply.encode())
                reply = f"'ram restant : {psutil.virtual_memory()[4]} 'bits'"
                conn.send(reply.encode())

            if message == "name" :
                reply = f"'hostname : {socket.gethostname()}"
                conn.send(reply.encode())

            if message == "CPU" :
                reply = f"'The CPU usage is: {psutil.cpu_percent(4)}'%'"
                conn.send(reply.encode())

            if message == "ip" :
                reply = f"address ip : {address}"
                conn.send(reply.encode())

            if message != "OS" and message != "RAM" and message != "name" and message != "CPU" and message != "ip" :
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
    if message == "reset":
        print("rebooting")
        message = ""
