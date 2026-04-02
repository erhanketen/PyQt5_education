import sys
from PyQt5.QtWidgets import QWidget , QApplication, QCheckBox, QLabel, QPushButton, QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("Python Sevion?")
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("TIKLA")

        v_box = QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("CheckBox")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi_alani))

        self.show()

    def click(self,checkbox,yazi_alani):
        if checkbox:
            yazi_alani.setText("EVET SEVİON!")
        else:
            yazi_alani.setText("SEN HAYIRDIR LAN GARDEEEŞ!")

app = QApplication(sys.argv)

window = Pencere()

sys.exit(app.exec_())








