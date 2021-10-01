from sqlite3.dbapi2 import Cursor
import sys
import sqlite3
from typing import Text
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui

from note_add import Ui_MainWindow
from Kayıt_sayfa import Ui_MainWindow_


class MainForm(QMainWindow):

    def sifre_belirle(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_()
        self.ui.setupUi(self.window)
        self.window.show() 
 
     
    def __init__(self):
# pencere özelleştirmesi yaptığım bölüm
        super(MainForm,self).__init__()
        self.setWindowTitle("Güvenli Not")
        self.setStyleSheet("background-image: url(arka_plan/arkaplan.jpg);")
        self.setGeometry(400,750,400,800)
        self.move(400,100)
        self.setWindowIcon(QtGui.QIcon("arka_plan/icon.png"))
        self.setMaximumHeight(750)
        self.setMaximumWidth(400)
        self.setMinimumHeight(420)
        self.setMinimumWidth(400)
        self.initUI()

    def initUI(self):

#Pencerede içerisinde bulunan arayüz elemanları
        self.resim = QtWidgets.QLabel(self)
        self.resim.move(-40,-70)
        self.resim.resize(490,460)
        self.resim.setStyleSheet("background-image: url(arka_plan/note-icon.png);")
        


        self.sonraki_btn=QtWidgets.QPushButton(self)
        self.sonraki_btn.setText("Giriş")
        self.sonraki_btn.move(100,380)
        self.sonraki_btn.setStyleSheet("border-radius: 5;border : 2px solid white")
        self.sonraki_btn.clicked.connect(self.yenisayfa)
  
        self.sifre_btn=QtWidgets.QPushButton(self)
        self.sifre_btn.setText("Şifre Oluştur")
        self.sifre_btn.move(210,380)
        self.sifre_btn.setStyleSheet("border-radius: 5;border : 2px solid white")
        self.sifre_btn.clicked.connect(self.sifre_belirle)


        self.k_adı= QtWidgets.QLineEdit(self)
        self.k_adı.move(80,425)
        self.k_adı.resize(250,28)
        self.k_adı.setPlaceholderText("Kullanıcı Adı")



        self.sifre_= QtWidgets.QLineEdit(self)
        self.sifre_.move(80,460)
        self.sifre_.resize(250,28)
        self.sifre_.setPlaceholderText("Şifre") 
        self.sifre_.setEchoMode(QtWidgets.QLineEdit.Password)
           
        self.comboBox1 = QtWidgets.QComboBox(self)
        self.comboBox1.setGeometry(QtCore.QRect(10, 570, 151, 31))
        self.comboBox1.addItem(QtGui.QIcon("arka_plan/res.jpg"),"1.Arka Plan")
        self.comboBox1.addItem(QtGui.QIcon("arka_plan/res1.jpg"),"2.Arka Plan")
        self.comboBox1.addItem(QtGui.QIcon("arka_plan/res2.jpg"),"3.Arka Plan")
        self.comboBox1.addItem(QtGui.QIcon("arka_plan/res3.jpg"),"4.Arka Plan")
        self.comboBox1.addItem(QtGui.QIcon("arka_plan/res4.jpg"),"5.Arka Plan")
        self.comboBox1.addItem(QtGui.QIcon("arka_plan/res5.jpg"),"6.Arka Plan")
        self.comboBox1.addItem(QtGui.QIcon("arka_plan/res6.jpg"),"7.Arka Plan")
        self.comboBox1.move(80,580)

        self.arkaplan=QtWidgets.QPushButton(self)
        self.arkaplan.move(240,580)
        self.arkaplan.resize(90,32)
        self.arkaplan.setText("Değiştir")
        self.arkaplan.setStyleSheet("border-radius: 5;border : 2px solid white")
        self.arkaplan.clicked.connect(self.arkaplan_)
   
#Veri tabanı oluşturma bölümü
        self.baglanti = sqlite3.connect("Veri_Tabani.sqlite")
        self.imlec = self.baglanti.cursor()
        self.imlec.execute("""CREATE TABLE IF NOT EXISTS k_bilgi 
        (ID INTEGER PRIMARY KEY,
        _kullaniciadi TEXT,
        _sifre TEXT,
        _isimsoyad TEXT)""")
        self.baglanti.commit()
#Veri tabanından isim ve soyisim verilerini çağıran bölüm
        self.imlec.execute("SELECT _isimsoyad FROM k_bilgi ")
        isim_soyisim = self.imlec.fetchall() 
        metin=""
        metin=isim_soyisim

        self.label =QtWidgets.QLabel(self)
        self.label.move(80,530)
        self.label.resize(250,40)
        self.label.setText("Uygulamaya Hoşgeldiniz \n"+str(metin) )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color: rgb(5, 0, 0);\n"
        "background-color: rgb(220, 220, 220);\n"
        "border-radius: 5;border : 0px solid white;font-size: 10pt")

        
# Arka Planın değişmesini sağlayan bölüm.
    def arkaplan_(self):
        secim=self.comboBox1.currentText()
        
        if secim=="1.Arka Plan":
            self.setStyleSheet("background-image: url(arka_plan/res.jpg);")
        elif secim=="2.Arka Plan":
            self.setStyleSheet("background-image: url(arka_plan/res1.jpg);")
        elif secim=="3.Arka Plan":
            self.setStyleSheet("background-image: url(arka_plan/res2.jpg);")
        elif secim=="4.Arka Plan":
            self.setStyleSheet("background-image: url(arka_plan/res3.jpg);")
        elif secim=="5.Arka Plan":
            self.setStyleSheet("background-image: url(arka_plan/res4.jpg);")
        elif secim=="6.Arka Plan":
            self.setStyleSheet("background-image: url(arka_plan/res5.jpg);")
        elif secim=="7.Arka Plan":
            self.setStyleSheet("background-image: url(arka_plan/res6.jpg);")
        else:
            self.setStyleSheet("background-image: url(arka_plan/res7.jpg);")

#Not ekleme sayfasının açılmasını sağlayan bölüm

    def yenisayfa(self):
        while True:
            kadi = self.k_adı.text()
            sifre = self.sifre_.text()
            self.imlec.execute("SELECT  _kullaniciadi, _sifre FROM k_bilgi")
            veri = self.imlec.fetchall()
            if(kadi,sifre) in veri:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.window)
                self.window.show()
                break
            elif kadi or sifre == "":
                msj= QMessageBox()
                msj.setWindowTitle('Yanliş bilgi')
                msj.setText('Boş alan bırakmayın kullanıcı adı veya şifrenizi kontrol edin.')
                msj.setIcon(QMessageBox.Warning)
                msj.exec_()
                break                 

 
def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()   

