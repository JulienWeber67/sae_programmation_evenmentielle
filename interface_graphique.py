from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QLineEdit
import sys
import psutil
import socket


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.i = 0
        self.setWindowTitle("QTextEdit")
        self.resize(750, 750)
        self.__test = QLineEdit("commande a entré :")
        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)
        self.zonetext = QTextEdit()
        self.zonetext.setEnabled(False)
        self.__msg = QLineEdit("")
        self.btnPress1 = QPushButton("Add message")
        self.btnPress2 = QPushButton("Clear")
        self.btnPress3 = QPushButton("Register")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.__msg)
        layout.addWidget(self.__test)
        layout.addWidget(self.zonetext)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress3)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def btnPress1_Clicked(self):
        text = self.__msg.text()
        self.textEdit.append(f"From serveur : {text}")

    def btnPress2_Clicked(self):
        self.textEdit.setPlainText("")
        self.zonetext.setPlainText("")

    def btnPress3_Clicked(self):
        text = self.__test.text()
        self.zonetext.append(f"Nouveau texte {text}")

        """text = self.__msg.text()
        self.textEdit.append(f"to serveur {text}")
        message = f"{text}"
        client_socket.send(message.encode())
        print("Message envoyé")"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_()) 