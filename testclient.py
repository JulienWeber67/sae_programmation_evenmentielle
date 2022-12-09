"""connect
while :
    envoi

    reception

    fermeture socket"""

import socket
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QLineEdit
import sys

host = "localhost" # "", "127.0.0.1
port = 10000

print(f"Ouverture de la socket sur le serveur {host} port {port}")
client_socket = socket.socket()
client_socket.connect((host, port))
print("Serveur est connecté")

data = ("")
class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.i = 0
        self.setWindowTitle("QTextEdit")
        self.resize(750, 750)
        self.__test = QLineEdit("")
        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)
        self.textEdit2 = QTextEdit()
        #self.textEdit2.setEnabled(False)
        self.__msg = QLineEdit("")
        self.btnPress1 = QPushButton("Add message")
        self.btnPress2 = QPushButton("Clear")
        self.btnPress3 = QPushButton("Register")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.__msg)
        layout.addWidget(self.__test)
        layout.addWidget(self.textEdit2)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress3)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def btnPress1_Clicked(self):
        text = self.__msg.text()
        self.textEdit.append(f"From serveur : {text}")
        message = input("Message au serveur : ")
        client_socket.send(message.encode())
        print("Message envoyé")

    def btnPress2_Clicked(self):
        self.textEdit.setPlainText("")
        self.textEdit2.setPlainText("")

    def btnPress3_Clicked(self):
        mot = self.__test
        self.textEdit2.append(f"Nouveau texte {mot}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())

while  data != 'disconnect':

    message = input("Message au serveur : ")
    client_socket.send(message.encode())
    print("Message envoyé")

    data = client_socket.recv(1024).decode()
    print(f"Message du serveur : {data}")

# Fermeture de la socket du client
client_socket.close()
print("Socket fermée")
