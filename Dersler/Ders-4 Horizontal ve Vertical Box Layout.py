import sys
from PyQt5 import QtWidgets

def pencere():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("PyQt5 Ders 4")
    window.setGeometry(700,300,500,500)

    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    """
    h_box = QtWidgets.QHBoxLayout()

    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()

    v_box.addStretch()
    v_box.addWidget(okay)
    v_box.addWidget(cancel)

    window.setLayout(h_box)
    window.setLayout(v_box)
    """
    h_box = QtWidgets.QHBoxLayout()

    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box = QtWidgets.QVBoxLayout()

    v_box.addStretch()
    v_box.addLayout(h_box)

    window.setLayout(v_box)

    window.show()

    sys.exit(app.exec_())

pencere()



