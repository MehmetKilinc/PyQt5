import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QCheckBox,QRadioButton,QTextEdit



class pencere(QWidget,os):


	def __init__(self):


		super().__init__()

		self.init_ui()

	def init_ui(self):

		self.yazı_alanı = QTextEdit()
		self.temizle = QPushButton("temizle")
		vbox = QVBoxLayout()
		vbox.addWidget(self.yazı_alanı)
		vbox.addWidget(self.temizle)
		hbox = QHBoxLayout()
		hbox.addStretch()
		hbox.addLayout(vbox)
		hbox.addStretch()
		self.setLayout(hbox)

		self.temizle.clicked.connect(self.click)
		self.kaydet.clicked.connect(self.click)

		self.show()

	def click(self):

		

		

		self.yazı_alanı.clear()

		



			







app= QApplication(sys.argv)

pencere = pencere()

sys.exit(app.exec_())