import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap


def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 2")

    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("SIMURG TECH.")
    etiket1.move(200,30)

    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QPixmap("../Kaynaklar/Logo.png"))
    etiket2.move(0,40)

    pencere.setGeometry(700,300,500,500)

    pencere.show()

    sys.exit(app.exec_())

Pencere()