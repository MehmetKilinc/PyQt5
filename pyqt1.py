import sys
from PyQt5 import QtWidgets
import sqlite3

class pencere(QtWidgets.QWidget):

	def __init__(self):

		super().__init__()

		self.init_ui()

	def init_ui(self):

		self.kullanıcı_Adı = QtWidgets.QLineEdit()
		self.parola = QtWidgets.QLineEdit()
		self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
		self.yazı_alanı = QtWidgets.QLabel()
		self.giriş = QtWidgets.QPushButton("giriş")
		self.yeni = QtWidgets.QPushButton("kullanıcı oluştur")

		vbox = QtWidgets.QVBoxLayout()
		vbox.addWidget(self.kullanıcı_Adı)
		vbox.addWidget(self.parola)
		vbox.addWidget(self.yazı_alanı)
		vbox.addStretch()
		vbox.addWidget(self.giriş)
		vbox.addWidget(self.yeni)
		hbox = QtWidgets.QHBoxLayout()
		hbox.addStretch()
		hbox.addLayout(vbox)
		hbox.addStretch()

		self.setLayout(hbox)

		self.veritaban()

		self.giriş.clicked.connect(self.login)
		self.yeni.clicked.connect(self.yenik)


		self.show()

	def veritaban(self):

		bağlantı = sqlite3.connect("merhaba.db")
		self.cursor = bağlantı.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS uyeler (kullanıcı TEXT , parola TEXT)")

		bağlantı.commit()

	def login(self):

		ad = self.kullanıcı_Adı.text()
		parola = self.parola.text()

		self.cursor.execute("SELECT * FROM uyeler WHERE kullanıcı = ? AND parola = ?",(ad,parola))

		data = self.cursor.fetchall()

		if len(data) == 0:

			self.yazı_alanı.setText("böyle bir kullanıcı bulunamadı")

		else:

			self.yazı_alanı.setText("hoşgeldin " + str(ad))


	def yenik(self):

		bağlantı = sqlite3.connect("merhaba.db")
		self.cursor = bağlantı.cursor()

		ad = self.kullanıcı_Adı.text()
		paro = self.parola.text()

		self.cursor.execute("INSERT INTO uyeler VALUES (?,?)",(ad,paro))
		bağlantı.commit()

		self.cursor.execute("SELECT * FROM uyeler WHERE kullanıcı = ? AND parola = ?",(ad,paro))
		data = self.cursor.fetchall()
		if len(data) == 0:

			self.yazı_alanı.setText("kullanıcı oluşturulurken hata oluştu")

		else:

			self.yazı_alanı.setText("kullanıcı oluşturuldu. oturum açabilirsiniz.")


app = QtWidgets.QApplication(sys.argv)

pencere = pencere()

sys.exit(app.exec_())