import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QRadioButton

class pencere(QWidget):

	def __init__(self):

		super().__init__()

		self.init_ui()

	def init_ui(self):

		self.radio_yazısı = QLabel("hangi dili daha çok seviyorsun ? ")
		self.java = QRadioButton("java")
		self.python = QRadioButton("python")
		self.php = QRadioButton("php")

		self.yazı_alanı = QLabel("")

		self.buton = QPushButton("gönder")

		vbox = QVBoxLayout()
		vbox.addWidget(self.radio_yazısı)
		vbox.addWidget(self.java)
		vbox.addWidget(self.python)
		vbox.addWidget(self.php)
		vbox.addStretch()
		vbox.addWidget(self.yazı_alanı)
		vbox.addWidget(self.buton)

		hbox = QHBoxLayout()
		hbox.addStretch()
		hbox.addLayout(vbox)
		hbox.addStretch()

		self.setLayout(hbox)

		self.buton.clicked.connect(lambda : self.click(self.java.isChecked,self.python.isChecked,self.php.isChecked,self.yazı_alanı))



		self.show()

	def click(self,java,python,php,yazı_alanı):

		if java:

			yazı_alanı.setText("java")
		if python:

			yazı_alanı.setText("python")
		if php:

			yazı_alanı.setText("php")

app = QApplication(sys.argv)

pencere = pencere()

sys.exit(app.exec_())