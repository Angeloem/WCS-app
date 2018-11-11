# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:43:01 2018

@author: Emanuel Sanga

This app is maintained by WCS class , more like a repository...

for more information,find us on github.com
"""
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classwork import App
from classwork import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class test(QMainWindow):
	global details
	def __init__(self , parent = None):
		super(test , self).__init__(parent = parent)
		
		self.loader()
	def loader(self):		
		widget = QWidget()
		self.setCentralWidget(widget)
		
		#layouts
		self.layout = QFormLayout()
		self.descriLayout = QVBoxLayout()
		self.buttonLayout = QHBoxLayout()
		
		#QFormLayout dealz
		self.name = QLabel('name')
		items = ['male' , 'female' , 'none']
		self.sexchooser = QComboBox()
		for item in items:
			self.sexchooser.addItem(item)
		
		self.age = QLabel('age')
		self.optcourse = QLabel('Opted Course')
		self.nameEdit = QLineEdit()
		#self.nameEdit.editingFinished()
		self.nameEdit.setPlaceholderText('enter name here')
		self.coursEdit = QLineEdit()
		self.coursEdit.setPlaceholderText('Mt || Ph || St')
		self.sexLabel = QLabel('sex')	
		#age selector
		self.ageSelector = QComboBox()
		for x in range(18 , 40):
			self.ageSelector.addItem(str(x))
		self.descriptor = QPlainTextEdit()
		
		self.descriptor.setPlaceholderText('describe yourself here')
		self.descriptor.setUndoRedoEnabled(True)
		self.layout.addRow(self.name , self.nameEdit)
		self.layout.addRow(self.optcourse , self.coursEdit)
		self.layout.addRow(QLabel('sex') , self.sexchooser)
		self.layout.addRow(QLabel('Age') , self.ageSelector)
		
		#phot dealz
		self.Browse = QPushButton('Browse')
		self.Browse.clicked.connect(self.browser)
		
		self.layout.addRow(QLabel('Profile Picture') , self.Browse)
		
		#buttons dealz
		self.SubmitButton = QPushButton('&Submit')
		self.SubmitButton.clicked.connect(self.detailer)
		self.cancelButton = QPushButton("Can&cel")
		self.cancelButton.clicked.connect(self.close)
		self.buttonLayout.addWidget(self.SubmitButton)
		self.buttonLayout.addWidget(self.cancelButton)
		
		self.descriLayout.addLayout(self.layout)
		self.descriLayout.addWidget(self.descriptor)
		self.descriLayout.addLayout(self.buttonLayout)
		
		self.show()
		widget.setLayout(self.descriLayout)
		self.setMinimumSize(300 , 350)
		self.setMaximumSize(300 , 350)
		self.setWindowTitle('DETAILS')
	def detailer(self):
		name = self.nameEdit.text()
		age = self.ageSelector.currentText()
		sex = self.sexchooser.currentText()
		opted = self.coursEdit.text()
		text = self.descriptor.toPlainText()
		
		details = [name , age , sex , opted , text]
		with open('textfiles/detailer.txt' , 'w') as e:
			for detail in details:
				e.write(detail+'\n')
		print(details.pop(2))
		self.Api = App()
		if self.descriptor.toPlainText():
			self.Api.texte.insertPlainText(sex + ' with ' +age + ' years of age and ' + text)
		else:
			self.Api.texte.insertPlainText(sex + ' with ' +age + ' years of age ')
		self.close()
	def browser(self):
		self.files = QFileDialog.getOpenFileName(self , 'Open File' , '/home/lightemaxt3' , 'Image Files(*.jpg , *.gif , *.png)')
		pimp = self.files[0]
		with open('textfiles/directory.txt' , 'w') as directory:
			directory.write(pimp)
if __name__ == '__main__':
	import sys
	import os
	app = QApplication(sys.argv)
	ex = test()
	sys.exit(app.exec_())

