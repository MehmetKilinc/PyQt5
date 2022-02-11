import sys
from PyQt5.QtWidgets import QPushButton,QLabel,QFileDialog,QWidget,QApplication,QTextEdit,QHBoxLayout,QVBoxLayout
import os


class pencere(QWidget):

	def __init__(self):

		super().__init__()

		self.init_ui()

	def init_ui(self):

		self.yazı_alanı = QTextEdit()
		self.temizle = QPushButton("temizle")
		self.aç = QPushButton("aç")
		self.kaydet = QPushButton("kaydet")

		hbox = QHBoxLayout()
		hbox.addWidget(self.temizle)
		hbox.addWidget(self.aç)
		hbox.addWidget(self.kaydet)
		vbox  =QVBoxLayout()
		vbox.addWidget(self.yazı_alanı)
		vbox.addLayout(hbox)
		self.setLayout(vbox)

		self.temizle.clicked.connect(self.yaziyi_temizle)
		self.aç.clicked.connect(self.dosya_ac)
		self.kaydet.clicked.connect(self.dosya_kaydet)




		self.show()

	def yaziyi_temizle(self):
		self.yazı_alanı.clear()
	def dosya_ac(self):
		
		dosya_ismi = QFileDialog.getOpenFileName(self,"dosya aç",os.getenv("HOME"))
		print(dosya_ismi)

	def dosya_kaydet(self):
		pass



app = QApplication(sys.argv)

pencere = pencere()

sys.exit(app.exec_())