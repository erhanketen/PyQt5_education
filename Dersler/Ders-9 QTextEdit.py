import sys
from PyQt5.QtWidgets import QWidget,QTextEdit ,QLabel, QPushButton, QVBoxLayout, QApplication

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ders-9 QTextEdit")

        self.yazi_alani = QTextEdit()

        self.temizle = QPushButton("Temizle")

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)

        self.setLayout(v_box)

        self.temizle.clicked.connect(self.click)

        self.show()

    def click(self):
        self.yazi_alani.clear()


app = QApplication(sys.argv)
window = Pencere()
sys.exit(app.exec_())








