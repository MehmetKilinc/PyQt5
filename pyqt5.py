import sys
from PyQt5 import QtWidgets

class pencere(QtWidgets.QWidget):

	def __init__(self):

		super().__init__()

		self.init_ui()

	def init_ui(self):

		self.yazı_alanı = QtWidgets.QLabel("bana henüz tıklanmadı")
		self.buton = QtWidgets.QPushButton("bana tıkla")
		self.sayı = 0

		vbox = QtWidgets.QVBoxLayout()
		vbox.addWidget(self.buton)
		vbox.addWidget(self.yazı_alanı)
		vbox.addStretch()


		hbox = QtWidgets.QHBoxLayout()
		hbox.addStretch()
		hbox.addLayout(vbox)
		hbox.addStretch()

		self.setLayout(hbox)

		self.buton.clicked.connect(self.click)

		self.show()

	def click(self):

		self.sayı += 1
		self.yazı_alanı.setText("bana " + str(self.sayı) + "kere tıklandı")


app = QtWidgets.QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())
