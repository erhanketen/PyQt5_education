import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 3")

    pencere.setGeometry(700,300,500,500)

    buton = QtWidgets.QPushButton(pencere)
    buton.setText("PUSH IT!")
    buton.move(87,120)

    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("SA WORLD")
    etiket.move(100,100)

    pencere.show()

    sys.exit(app.exec_())

Pencere()



