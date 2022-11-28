"""import platform

i=platform.system()
k=platform.release()
u=platform.platform()

print(f"nom:{i},version :{k},platform :{u}")"""

"""import socket
import sys
while True:

    port = 18000
    host = "localhost"
    server_socket = socket.socket()
    server_socket.bind((host,port))
    print(f"attente du client sur le port {port} depuis la machine {host}")
    server_socket.listen(1)
    while True:
        conn, address = server_socket.accept()
        data = conn.recv(1024).decode()
        reply = input()
        conn.send(reply.encode())
        print(data)
    if data == "bye":
        reply3 = "arretclient"
        data = conn.recv(1024).decode()
        conn.send(reply3.encode())
        print("Le client s'est arrêté")
     if data == "arret":
        conn.close()
        print("Le client et le serveur se sont arrêté")"""



