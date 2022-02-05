import sys
from PyQt5 import QtWidgets

class pencere(QtWidgets.QWidget):

	def __init__(self):

		super().__init__()

		self.init_ui()

	def init_ui(self):

		self.yazı_alanı = QtWidgets.QLineEdit()
		self.temizle = QtWidgets.QPushButton("temizle")
		self.yazdır = QtWidgets.QPushButton("yazdır")


		vbox = QtWidgets.QVBoxLayout()
		vbox.addWidget(self.yazı_alanı)
		vbox.addWidget(self.temizle)
		vbox.addWidget(self.yazdır)
		vbox.addStretch()

		hbox = QtWidgets.QHBoxLayout()
		hbox.addStretch()
		hbox.addLayout(vbox)
		hbox.addStretch()

		self.setLayout(hbox)

		self.temizle.clicked.connect(self.click)
		self.yazdır.clicked.connect(self.click)

		self.show()

	def click(self):

		sender = self.sender()

		if sender.text() == "temizle":

			self.yazı_alanı.clear()

		else:

			print(self.yazı_alanı.text())




app = QtWidgets.QApplication(sys.argv)

pencere = pencere()

sys.exit(app.exec_())