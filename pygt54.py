import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QHBoxLayout


class pencere(QWidget):

	def __init__(self):

		super().__init__()

		self.init_ui()

	def init_ui(self):

		self.checkbox = QCheckBox("pythonu severmisin ? ")
		self.yazı_alanı = QLabel("")
		self.buton = QPushButton("bana tıkla")

		vbox = QVBoxLayout()
		vbox.addWidget(self.checkbox)
		vbox.addStretch()
		vbox.addWidget(self.yazı_alanı)
		vbox.addWidget(self.buton)
		vbox.addStretch()
		hbox = QHBoxLayout()
		hbox.addStretch()
		hbox.addLayout(vbox)
		hbox.addStretch()
		self.setLayout(hbox)

		self.setWindowTitle("naber")

		self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazı_alanı))

		self.show()

	def click(self , checkbox , yazı_alanı):

		if checkbox:

			yazı_alanı.setText("evet seviyorsun")


		else:

			yazı_alanı.setText("hayır sevmiyorsun")

app = QApplication(sys.argv)

pencere = pencere()

sys.exit(app.exec_())