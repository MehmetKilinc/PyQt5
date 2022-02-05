import sys
from PyQt5 import QtWidgets
import sqlite3


class pencere():

	def __init__(self):

		super().__init__()

		self.init_ui()


	def bağlantı_oluştur(self):

		bağlantı = sqlite3.connect("database.db")

		self.cursor = bağlantı.cursor()

		self.cursor.execute("CREATE TABLE IF NOT EXISTS üyeler (kullanıcı_adı TEXT , parola TEXT)")

		bağlantı.commit()

	def init_ui(self):

		self.kullanıcı_adı = QtWidgets.QLineEdit()
		self.parola = QtWidgets.QLineEdit()
		self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
		self.clear = QtWidgets.QPushButton("temizle")
		self.giriş = QtWidgets.QPushButton("giriş yap")
		self.yazı_alanı = QtWidgets.QLabel("")

		vbox = QtWidgets.QVBoxLayout()
		vbox.addWidget(self.kullanıcı_adı)
		vbox.addWidget(self.parola)
		vbox.addWidget(self.yazı_alanı)
		vbox.addStretch()
		vbox.addWidget(self.clear)
		vbox.addWidget(self.giriş)

		hbox = QtWidgets.QHBoxLayout()
		hbox.addStretch()
		hbox.addLayout(vbox)
		hbox.addStretch()

		self.setLayout(hbox)

		self.setWindowTitle("kullanıcı girişi")

		self.giriş.clicked.connect(self.login)
		self.clear.clicked.connect(self.login)

		self.show()

	def login():

		sender = self.sender()

		if sender.text() == "giriş":

			ad = self.kullanıcı_adı.text()
			şifre = self.parola.text()

			self.cursor.execute("SELECT * FROM üyeler WHERE kullanıcı_adı = ? AND parola = ?",(ad,şifre))

			data = self.cursor.fetchall()

			if len(data) == 0:

				self.yazı_alanı.setText("kullanıcı bulunamadı")

			else:

				self.yazı_alanı.setText("hoşgeldiniz" + str(ad))

		else:

			self.kullanıcı_adı.clear()
			self.parola.clear()

app = QtWidgets.QApplication(sys.argv)

pencere = pencere()

sys.exit(app.exec_())