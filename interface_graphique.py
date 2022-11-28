import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QVBoxLayout

while True :
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            widget = QWidget()
            self.setCentralWidget(widget)
            grid = QGridLayout()
            widget.setLayout(grid)
            lab = QLabel("Chat client-serveur")
            self.__text = QLineEdit("")
            ok = QPushButton("send")
            quit = QPushButton("Quitter")
            self.__list =[]
            test = QLabel(f"{list}")
            self.__nom = QLabel("")
            layout = QVBoxLayout()
            grid.addWidget(lab, 0, 0)
            grid.addWidget(self.__text, 1, 0)
            grid.addWidget(ok, 2, 0)
            grid.addWidget(quit, 2, 1)
            grid.addWidget(self.__nom, 3, 0)
            grid.addWidget(test,0,2,1,1)
            grid.addWidget(layout, 4,0)

            ok.clicked.connect(self.__actionOk)
            quit.clicked.connect(self.__actionQuitter)
            self.setWindowTitle("Une première fenêtre")
        def __actionOk(self):
            msg = self.__text.text()
            self.__nom.setText(f"from srv: {msg}")
            self.__list.append(msg)

        def __actionQuitter(self):
            QCoreApplication.exit(0)

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec()