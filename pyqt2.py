import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QHBoxLayout,QVBoxLayout,QCheckBox,QLabel

class pencere(QWidget):

	def __init__(self):

		super().__init__()

		self.init_ui()

	def init_ui(self):

		self.checkbox = QCheckBox("python severmisin ? ")
		self.buton = QPushButton("bana tıkla")
		self.yazı_alanı = QLabel()

		vbox = QVBoxLayout()
		vbox.addWidget(self.checkbox)
		vbox.addStretch()
		vbox.addWidget(self.yazı_alanı)
		vbox.addWidget(self.buton)
		hbox = QHBoxLayout()
		hbox.addStretch()
		hbox.addLayout(vbox)
		hbox.addStretch()

		self.setLayout(hbox)

		self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked , self.yazı_alanı))

		self.show()

	def click(self , checkbox , yazı_alanı):

		if not checkbox:

			yazı_alanı.setText("neden")

		else:

			yazı_alanı.setText("güzel")


app = QApplication(sys.argv)

pencere = pencere()

sys.exit(app.exec_())