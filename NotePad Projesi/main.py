import sys
from PyQt5.QtCore import QTimer
from funcs import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel, QLineEdit, QHBoxLayout, \
    QAction, QMainWindow, QFileDialog, QMessageBox, qApp
from PyQt5.QtGui import QFont

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("NotePad Program")
        self.setGeometry(550,300,800,600)

        self.title = QLabel("Başlık:")
        self.text = QLabel("Not:")
        self.files = QLabel("Notlar:")
        self.mesaje = QLabel("")
        self.search_text =QLabel("Arama:")
        self.search_results = QLabel("")

        self.save_button = QPushButton("KAYDET")
        self.open_button = QPushButton("AÇ")
        self.delete_button = QPushButton("SİL")
        self.close_button = QPushButton("KAPAT")
        self.search_button = QPushButton("ARA")

        self.save_button.setShortcut("Ctrl+S")
        self.open_button.setShortcut("Ctrl+O")
        self.close_button.setShortcut("Ctrl+Q")
        self.delete_button.setShortcut("Ctrl+D")

        self.title_space = QLineEdit()
        self.serach_space = QLineEdit()
        self.text_space = QTextEdit()

        font2 = QFont("Segoe UI", 9)
        self.setFont(font2)

        v_box = QVBoxLayout()

        v_box.addWidget(self.title)
        v_box.addWidget(self.title_space)
        v_box.addWidget(self.text)
        v_box.addWidget(self.text_space)
        v_box.addWidget(self.mesaje)
        v_box.addWidget(self.save_button)
        v_box.addWidget(self.open_button)
        v_box.addWidget(self.close_button)
        v_box.addWidget(self.delete_button)

        h_box = QHBoxLayout()

        h_box.addWidget(self.serach_space, stretch=6)
        h_box.addWidget(self.search_button, stretch=1)

        v2_box = QVBoxLayout()

        v2_box.addWidget(self.search_text)
        v2_box.addLayout(h_box)
        v2_box.addWidget(self.files)
        v2_box.addWidget(self.search_results)
        v2_box.addStretch()


        h2_box = QHBoxLayout()

        h2_box.addLayout(v2_box,1)
        h2_box.addLayout(v_box,2)

        central_widget = QWidget()
        central_widget.setLayout(h2_box)
        self.setCentralWidget(central_widget)

        self.save_button.clicked.connect(self.save)
        self.open_button.clicked.connect(self.open)
        self.close_button.clicked.connect(self.close)
        self.delete_button.clicked.connect(self.delete)
        self.search_button.clicked.connect(self.search)

        menubar = self.menuBar()

        file_menu = menubar.addMenu("Dosya")

        open_file_action = QAction("Dosya Aç", self)
        open_file_action.setShortcut("Ctrl+I")

        export_file_action = QAction("Dışarı Aktar", self)
        export_file_action.setShortcut("Ctrl+E")

        exit_program_action = QAction("Çıkış", self)
        exit_program_action.setShortcut("Ctrl+Shift+Q")

        file_menu.addAction(open_file_action)
        file_menu.addAction(export_file_action)
        file_menu.addAction(exit_program_action)

        open_file_action.triggered.connect(self.open_file)
        export_file_action.triggered.connect(self.export_file)
        exit_program_action.triggered.connect(self.exit_program)

        self.list_notes()

        self.show()

    def list_notes(self):
        self.notes_list = search_note("all")
        self.search_results.setText(self.notes_list)
        return

    def save(self):
        _new_title = self.title_space.text()
        _new_content = self.text_space.toPlainText()

        if isTitleEmpty(_new_title):
            gen = untiled_generator()
            untiled = next(gen)
            note.save_note(untiled, _new_content)

            self.title_space.setText(untiled)

            self.list_notes()

            self.mesaje.setText("Not '{}' Olarak Kaydedildi".format(untiled))
            QTimer.singleShot(2000,lambda: self.mesaje.setText(""))
            return

        note.save_note(_new_title,_new_content)

        self.list_notes()

        self.mesaje.setText("{} Notu Kaydedildi".format(_new_title))
        QTimer.singleShot(2000,lambda: self.mesaje.setText(""))

    def open(self):
        _title = self.title_space.text()

        if isTitleEmpty(_title):
            self.mesaje.setText("Başlık Kısmı Boş")
            QTimer.singleShot(2000,lambda: self.mesaje.setText(""))
            return

        openner = note.show_note(_title)

        if openner == "Dosya Bulunamadı":
            self.mesaje.setText("Dosya Bulunamadı")
            QTimer.singleShot(2000, lambda: self.mesaje.setText(""))
            return

        self.title_space.setText(note.note_title)
        self.text_space.setText(note.note_content)

        self.mesaje.setText("{} Notu Açıldı".format(_title))
        QTimer.singleShot(2000,lambda: self.mesaje.setText(""))

    def close(self):
        _title = self.title_space.text()

        if isTitleEmpty(_title):
            self.mesaje.setText("Başlık Kısmı Boş")
            QTimer.singleShot(2000,lambda: self.mesaje.setText(""))
            return

        msg = QMessageBox()
        msg.setWindowTitle("Onay")
        msg.setText("Kaydetmediğiniz Veriler Kaybolacaktır.\nDosya Kapatılsın mı?")

        yes_button = msg.addButton("Evet", QMessageBox.YesRole)
        no_button = msg.addButton("Hayır", QMessageBox.NoRole)
        msg.exec_()

        if msg.clickedButton() == yes_button:
            note.close_note()
        elif msg.clickedButton() == no_button:
            return

        self.title_space.clear()
        self.text_space.clear()

        self.mesaje.setText("{} Notu Kapatıldı".format(_title))
        QTimer.singleShot(2000,lambda: self.mesaje.setText(""))

    def delete(self):
        _title = self.title_space.text()

        if isTitleEmpty(_title):
            self.mesaje.setText("Başlık Kısmı Boş")
            QTimer.singleShot(2000,lambda: self.mesaje.setText(""))
            return

        msg = QMessageBox()
        msg.setWindowTitle("Onay")
        msg.setText("Dosyanın Silinmesine Emin misiniz?")

        yes_button = msg.addButton("Evet", QMessageBox.YesRole)
        no_button = msg.addButton("Hayır", QMessageBox.NoRole)
        msg.exec_()

        if msg.clickedButton() == yes_button:
            deleter = note.delete_note(_title)
        elif msg.clickedButton() == no_button:
            return

        if deleter == "Dosya Bulunamadı":
            self.mesaje.setText("Dosya Bulunamadı")
            QTimer.singleShot(2000,lambda: self.mesaje.setText(""))

        self.title_space.clear()
        self.text_space.clear()

        self.list_notes()

        self.mesaje.setText("{} Notu Silindi".format(_title))
        QTimer.singleShot(2000,lambda: self.mesaje.setText(""))

    def search(self):
        the_search = self.serach_space.text()

        if not isTitleEmpty(the_search):
            _notes_list = search_note(the_search)
            self.search_results.setText(_notes_list)
        else:
            self.list_notes()

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, "Open File")
        if not file_path:
            return
        importer = import_file(file_path)
        if not importer:
            self.mesaje.setText("Bu İsimde Bir Notunuz Bulunmaktadır, Lütfen Çakışmayı Çözün.")
            QTimer.singleShot(2000, lambda: self.mesaje.setText(""))
        else:
            self.title_space.setText(importer)
            self.open()
            self.mesaje.setText("İçeri Aktarıldı")
            QTimer.singleShot(2000, lambda: self.mesaje.setText(""))

        self.list_notes()

    def export_file(self):
        file_path = QFileDialog.getSaveFileName(self, "Save File")
        if not file_path:
            return
        _title = self.title_space.text()

        export_file(_title,file_path)

        self.mesaje.setText("Dışarı Aktarıldı")
        QTimer.singleShot(2000, lambda: self.mesaje.setText(""))

        self.list_notes()

    def exit_program(self):
        msg = QMessageBox()
        msg.setWindowTitle("Onay")
        msg.setText("Kaydedilmeyen Veri Kaybolacaktır.\nProgram Kapatılsın mı?")

        yes_button = msg.addButton("Evet", QMessageBox.YesRole)
        no_button = msg.addButton("Hayır", QMessageBox.NoRole)
        msg.exec_()

        if msg.clickedButton() == yes_button:
            qApp.quit()
        elif msg.clickedButton() == no_button:
            return


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

