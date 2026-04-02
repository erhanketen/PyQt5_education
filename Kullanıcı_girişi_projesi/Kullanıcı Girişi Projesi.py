import sys
import DB
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ini_ui()

    def ini_ui(self):
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle("Kullanıcı Girişi")

        kullanıcı_yazı = QtWidgets.QLabel("Kullanıcı Adı:")
        şifre_yazı = QtWidgets.QLabel("Şifre:")

        self.kullanıcı_adı = QtWidgets.QLineEdit()
        self.şifre = QtWidgets.QLineEdit()
        self.şifre.setEchoMode(QtWidgets.QLineEdit.Password)

        self.giris = QtWidgets.QPushButton("Giriş")
        self.kayit_ol = QtWidgets.QPushButton("Kayıt Ol")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addStretch()
        v_box.addWidget(kullanıcı_yazı)
        v_box.addWidget(self.kullanıcı_adı)
        v_box.addWidget(şifre_yazı)
        v_box.addWidget(self.şifre)
        v_box.addWidget(self.kayit_ol)
        v_box.addWidget(self.giris)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.window.setLayout(h_box)

        self.giris.clicked.connect(self.click)
        self.kayit_ol.clicked.connect(self.click)

        self.window.show()

    def click(self):
        sender = self.sender()
        if sender.text() == "Kayıt Ol":
            kayit = DB.DBconnection.veri_bas((self.kullanıcı_adı.text(),self.şifre.text()))
            if kayit == "Bu Kullanıcı Zaten Var!":
                sys.stderr.write("Bu Kullanıcı Zaten Var!")
                sys.stderr.flush()
            else:
                print("kayit oluşturuldu")

        else:
            giris = DB.DBconnection.veri_cek((self.kullanıcı_adı.text(),self.şifre.text()))
            if giris:
                print("Giris Basarili!")
            else:
                print("Giris Basarisiz!")

        DB.DBconnection.baglanti_kes()


app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())





