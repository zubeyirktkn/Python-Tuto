import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication,QMainWindow, QPushButton,QToolTip
from PyQt5 import QtGui

def window(self):
    app=QApplication(sys.argv)
    win =QMainWindow()

    win.setWindowTitle("Chess")
    win.setGeometry(200,200,500,500)
    win.setWindowIcon(QtGui.QIcon('chess.png'))#ikon değişmedi??
    win.setToolTip("MyToolTip")
    
    
    win.show()
    sys.exit(app.exec_())


def UI(self):
    button=QPushButton("Btn",self)
    button.setGeometry(QRect(100,100,111,28))
    button.setIcon(QtGui.QIcon("chess.png"))



window()

