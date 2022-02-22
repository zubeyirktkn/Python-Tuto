import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtGui import QPalette,QColor,QIcon

class Color(QWidget):
    def __init__(self,color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(100,100,500,500)
        self.setWindowIcon(QIcon('chess.png'))
        self.setWindowTitle("Chess")

        """
        #vlayout=QtWidgets.QVBoxLayout()#vertical layout
        hlayout1=QtWidgets.QHBoxLayout()
        hlayout1.addWidget(Color("black"))
        hlayout1.addWidget(Color("white"))
        hlayout1.addWidget(Color("black"))
        hlayout1.addWidget(Color("white"))

        vlayout=QtWidgets.QVBoxLayout()
        vlayout.addWidget(Color("black"))
        vlayout.addWidget(Color("white"))
        vlayout.addWidget(Color("black"))
        vlayout.addWidget(Color("white"))
        
        vlayout.addLayout(hlayout1)
        """     
        layout=QtWidgets.QGridLayout()
        layout.setSpacing(0)#boşluk olmasın
        """
        layout.addWidget(Color("black"),0,0)
        layout.addWidget(Color("grey"),0,1)
        layout.addWidget(Color("black"),1,1)
        layout.addWidget(Color("grey"),1,0)
        """
        #satranc board------------------------------------------
        i=0
        j=0
        black="gray"
        white="white"
        for i in range(8):
            for j in range(8):
                if i%2==0 and j%2==0:
                    layout.addWidget(Color(f"{white}"),i,j)
                elif i%2==0 and j%2!=0:
                    layout.addWidget(Color(f"{black}"),i,j)
                elif i%2!=0 and j%2!=0:
                    layout.addWidget(Color(f"{white}"),i,j)
                elif i%2!=0 and j%2==0:
                    layout.addWidget(Color(f"{black}"),i,j)
        #--------------------------------------------------------------

        widget=QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

def app():
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())
app()
