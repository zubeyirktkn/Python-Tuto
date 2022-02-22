import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()

        self.setWindowTitle("Chess")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon('icon.ico'))#ikon değişmedi??
        self.setToolTip("MyToolTip")
        self.initUI()

    def clicked(self):
        self.lbl_result.setText("Ad:"+self.txt_name.text()+"\nSoyad:"+self.txt_surname.text())
  
    def initUI(self):
        self.lbl_name=QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız:")
        self.lbl_name.move(50,50)

        self.txt_name=QtWidgets.QLineEdit(self)
        self.txt_name.move(110,50)

        self.lbl_surname=QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız:")
        self.lbl_surname.move(50,90)

        self.txt_surname=QtWidgets.QLineEdit(self)
        self.txt_surname.move(110,90)   

        self.btn_save=QtWidgets.QPushButton(self)
        self.btn_save.setText("KAYDET")
        self.btn_save.setGeometry(110,130,60,20)
        self.btn_save.clicked.connect(self.clicked) 
        

        self.lbl_result=QtWidgets.QLabel(self)
        self.lbl_result.move(110,150)



def window():
    app=QApplication(sys.argv)
    win =MyWindow()
    win.show()#pencereyi göster
    sys.exit(app.exec_())#pencereyi kapat X e basınca

window()

"""
def window():
    app=QApplication(sys.argv)
    win =QMainWindow()

    #title boyut icon ve tooltip setting------------------------
    win.setWindowTitle("Chess")
    win.setGeometry(200,200,500,500)
    win.setWindowIcon(QIcon('icon.ico'))#ikon değişmedi??
    win.setToolTip("MyToolTip")
    #----------------------------------------------------------------
    #name label-----------------------------
    lbl_name=QtWidgets.QLabel(win)
    lbl_name.setText("Adınız:")
    lbl_name.move(50,50)
    #---------------------------------------
    #name input kutusu------------------------------
    txt_name=QtWidgets.QLineEdit(win)
    txt_name.move(110,50)
    #-----------------------------------------------
    #surname label -----------------------------
    lbl_surname=QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadınız:")
    lbl_surname.move(50,90)
    #-------------------------------------------
    #surname input-------------------------
    txt_surname=QtWidgets.QLineEdit(win)
    txt_surname.move(110,90)
    #--------------------------------------
    #tıklama fonksiyonu buton için---------------
    def clicked(self):
        print("Butona tıklandı.\nİsim: "+txt_name.text()+"\nSoyisim: "+txt_surname.text())
    #--------------------------------------------
    #button özellikleri konumu text--------------
    btn_save=QtWidgets.QPushButton(win)
    #btn_save.move(110,130)
    btn_save.setText("KAYDET")
    btn_save.setGeometry(110,130,60,20)
    btn_save.clicked.connect(clicked)
    #---------------------------------------------

    win.show()#pencereyi göster
    sys.exit(app.exec_())#pencereyi kapat X e basınca

window()#fonksiyon çağrısı
"""

#QLabel
#QComboBox
#QCheckBox
#QRadioButton
#QPushButton
#QTableWidget
#QLineEdit
#QSlider
#QProgressBar