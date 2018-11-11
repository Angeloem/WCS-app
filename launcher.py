# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:43:01 2018

@author: Emanuel Sanga

This app is maintained by WCS class , more like a repository...

for more information,find us on github.com
"""
from details import test
from classwork import App
from PyQt5.QtWidgets import *
import sys
app = QApplication(sys.argv)
with open('textfiles/detailer.txt' , 'r') as directory:
	if 	directory.readlines() == '':
		testApp = test()
	elif directory.read(4) == '':
		testApp = test()
	else:
		appApp = App()
sys.exit(app.exec_())
