import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import time

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,500)
        self.initUI()
        self.tempo=0

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayı 1:")
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.resize(200,32)
        self.txt_sayi1.move(150,30)
        #----------------------------------------------------
        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayı 2:")
        self.lbl_sayi2.move(50,80)
        
        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.resize(200,32)
        self.txt_sayi2.move(150,80)
        #------------------------------------------------------
        self.btn_topla=QtWidgets.QPushButton(self)
        self.btn_topla.setText("+")
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.toplama)

        self.btn_cikar=QtWidgets.QPushButton(self)
        self.btn_cikar.setText("-")
        self.btn_cikar.move(250,130)
        self.btn_cikar.clicked.connect(self.hesapla)

        self.btn_carp=QtWidgets.QPushButton(self)
        self.btn_carp.setText("x")
        self.btn_carp.move(150,170)
        self.btn_carp.clicked.connect(self.hesapla)
        
        self.btn_bol=QtWidgets.QPushButton(self)
        self.btn_bol.setText("/")
        self.btn_bol.move(250,170)
        self.btn_bol.clicked.connect(self.hesapla)

        self.btn_sil=QtWidgets.QPushButton(self)
        self.btn_sil.setText("Temizle")
        self.btn_sil.move(150,200)
        self.btn_sil.resize(60,20)
        self.btn_sil.clicked.connect(self.hesapla)

        #------------------------------------------------------
        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText("Sonuç:")
        self.lbl_sonuc.move(150,230)
        #-------------------------------------------------------
        self.lbl_hata = QtWidgets.QLabel(self)
        self.lbl_hata.setText("")
        self.lbl_hata.move(150,250)
        #-------------------------------------------------------
    def hesapla(self):#sender kullanımı
        sender =self.sender().text()
        if sender=="+":
            self.toplama()
        elif sender=="-":
            self.cikarma()
        elif sender=="x":
            self.carpma()
        elif sender=="/":
            self.bolme()
        elif sender=="Temizle":
            self.sil()
        #-----------------------------------------------------------
    def toplama(self):
        try:
            result=int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
            self.lbl_sonuc.setText("Sonuç:"+str(result))
        except:
            self.hata()
            self.tempo+=1
        finally:
            if self.tempo==0:
                self.lbl_hata.setText("")
            self.tempo=0
        
    def cikarma(self):
        try:
            result=int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
            self.lbl_sonuc.setText("Sonuç:"+str(result))
        except:
            self.hata()
            self.tempo+=1
        finally:
            if self.tempo==0:
                self.lbl_hata.setText("")
            self.tempo=0
        
    def carpma(self):
        try:
            result=int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
            self.lbl_sonuc.setText("Sonuç:"+str(result))
        except:
            self.hata()
            self.tempo+=1
        finally:
            if self.tempo==0:
                self.lbl_hata.setText("")
            self.tempo=0
        
    def bolme(self):
        try:
            result=float(self.txt_sayi1.text()) / float(self.txt_sayi2.text())
            self.lbl_sonuc.setText("Sonuç:"+str(result))
        except:
            self.hata()
            self.tempo+=1
        finally:
            if self.tempo==0:
                self.lbl_hata.setText("")
            self.tempo=0

    def hata(self):
        self.lbl_hata.resize(200,50)
        self.lbl_hata.setText("Yanlış bir değer girdiniz.")

    def sil(self):
        self.lbl_sonuc.setText("Sonuç:")



def app():
    app=QApplication(sys.argv)
    win=MainForm()
    win.show()
    sys.exit(app.exec_())

app()