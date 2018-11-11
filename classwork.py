# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:43:01 2018

@author: Emanuel Sanga

This app is maintained by WCS class , more like a repository...

for more information,find us on github.com
"""
import os , random
import time
import numpy as numpy
from matplotlib.backends.backend_qt5 import FigureManagerQT as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as pie
import pandas as pd
import seaborn as sea
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class App(QMainWindow):
    def __init__(self , parent = None):
        super(App , self).__init__(parent = parent)
        self.setWindowIcon(QIcon('/home/lightemaxt3/Desktop/classey/icons/main.png'))
        self.appLayout = QHBoxLayout(self)
        self.StatusBar = self.statusBar()
        self.StatusBar.showMessage('ready')
        self.show()
        self.setStyleSheet('background-color:lightgrey')   
        self.infoLoader() 
        self.actionCreator()
        self.menuCreator()
        self.Toolbar()
        self.mainFrame = QFrame(self)
        self.mainFrame.setFrameShadow(QFrame.Sunken)
        self.mainFrame.setFrameShape(QFrame.Panel)
        self.setCentralWidget(self.mainFrame)
        
        self.mainFrameLayout = QHBoxLayout()
        self.leftFrame = QFrame()
        self.leftFrame.setFrameShadow(QFrame.Sunken)
        self.leftFrame.setFrameShape(QFrame.Panel)
        self.leftFrame.setMinimumWidth(300)
        self.leftFrame.setMaximumWidth(300)
        self.leftLayout = QVBoxLayout()
        self.leftFrame.setLayout(self.leftLayout)
        self.LeftImageLabel = QLabel()
        self.leftFrameLoader()
        
		
        self.middleFrame = QFrame()
        self.middleFrame.setFrameShadow(QFrame.Raised)
        self.middleFrame.setFrameShape(QFrame.StyledPanel)
        self.midoLayout = QVBoxLayout()
        self.middleFrame.setMinimumWidth(200)
        self.middleFrameLoader()
        self.rightFrame = QFrame()
        self.rightFrame.setFrameShadow(QFrame.Sunken)
        self.rightFrame.setFrameShape(QFrame.Panel)
        self.rightFrame.setMinimumWidth(350)
        self.rightFrame.setMaximumWidth(350)
        
        self.splitter = QSplitter()
        self.splitter.resize(500 , 500)
        self.splitter.insertWidget(0 , self.leftFrame)
        self.splitter.insertWidget(1 , self.middleFrame)
        self.splitter.insertWidget(2 , self.rightFrame)
        self.splitter.setCollapsible(0 , False)
        self.splitter.setCollapsible(1 , False)
        self.splitter.setCollapsible(2 , False) 
        self.splitter.setSizes([40 , 60 , 30])
        self.mainFrameLayout.addWidget(self.splitter)
        #self.mainFrameLayout.addWidget(self.rightFrame)     
        
        self.mainFrame.setLayout(self.mainFrameLayout)
        ##RIGHT FRAME DEALZ
        self.texte = QPlainTextEdit()
        self.texte.setReadOnly(True)
        self.texte.setPlaceholderText('description down here')
        text = '<b><u>your description</b></u>'
        text1 = 'Emanuel\'s description here'
        font = QFont('Arial' , 25)
        font1 = QFont('Arial' , 10)
        
        self.rightLayout = QVBoxLayout()        
        self.Label = QLabel()
        self.Label.setText(text)
        self.Label.setFont(font)
        self.Label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        #detailz
        file = open('textfiles/detailer.txt' , 'r')
        self.name = QLabel('<b>'+file.readline()+'</b>')
        self.name.mousePressEvent = self.Profile
        self.rightFramic()
        self.btnn = QLabel('<b>name:  </b>')
        self.descriptor = QLabel('<b>down</b>')
        self.descipt = QLabel('<b>Description:</b>')
        
        self.detailz = QFormLayout()
        
        self.detailz.addRow(self.btnn , self.name)
        self.detailz.addRow(self.descipt , self.descriptor)
        self.rightLayout.addWidget(self.Label)        
        self.rightLayout.addLayout(self.detailz)
        self.rightLayout.addWidget(self.texte)
        self.rightFrame.setLayout(self.rightLayout)
        self.rightLayout.addStretch()
        
        #imagelabel
        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        with open('textfiles/directory.txt' , 'r') as directory:
            roughText = directory.read()
            pimp = roughText
            self.directoryOfImage = str(pimp)
            self.profilePic = QPixmap(self.directoryOfImage)
            self.scaledProfilePic = self.profilePic.scaled(330 , 350) 
            self.imageLabel.setPixmap(self.scaledProfilePic)       
        self.rightLayout.addWidget(self.imageLabel)
        file.close()
        #window configz
        self.setLayout(self.appLayout)
        self.setMinimumSize(1200, 700)
        self.setMaximumSize(1200 , 700)
    def showImages(self):
        image = QPixmap('media/ret.png')
        self.bishaf = image.scaled(300 , 400)
        self.LeftImageLabel.setPixmap(self.bishaf)
    def leftFrameLoader(self):
        self.showImages()
        self.leftFrame.setStyleSheet('padding:0px 0px 0px 0px;background-color:khaki;')
        self.leftLayout.addStretch()
        self.leftLayout.addWidget(QLabel('<a href="nowhere"><B><center>GALLERY</center></B></a>'))
        self.picLayout = QHBoxLayout()	
        image1 = QPixmap('media/1.jpg').scaled(40 , 60)
        image2 = QPixmap('media/2.jpg').scaled(40 , 60)
        image3 = QPixmap('media/3.jpg').scaled(40 , 60)
        image4 = QPixmap('media/4.jpg').scaled(40 , 60)
        image5 = QPixmap('media/5.jpg').scaled(40 , 60)
        label = QLabel()
        label.setPixmap(image1)
        #label.onMouseEvent
        label1 = QLabel()
        label1.setPixmap(image2)
        label2 = QLabel()
        label2.setPixmap(image3)
        label3 = QLabel()
        label3.setPixmap(image4)
        label4 = QLabel()
        label4.setPixmap(image5)

        self.picLayout.addWidget(label)
        self.picLayout.addWidget(label1)
        self.picLayout.addWidget(label2)
        self.picLayout.addWidget(label3)
        self.picLayout.addWidget(label4)
        self.leftLayout.addLayout(self.picLayout)
        self.leftLayout.addWidget(self.LeftImageLabel)
    def rightFramic(self):	
        def printer(self):
            self.setWindowTitle('WCS')	
        printer(self)
    def Profile(self , event):
        pass
    def Project(self):
        pass
    def Job(self):
        pass
    def codeViewer(self):
        pass
    def Append(self):
        pass
    def infoedit(self):
        pass
    def configure(self):
        pass
    def prospectus(self):
        pass
    def timetable(self):
        pass
    def picz(self):
        pass
    def mapper(self):
        pass
    def Administration(self):
        pass
    def Onecourse(self):
        self.middleFrame.focusWidget()
        text = 'on first year,we had the following courses'
        self.newMiddleLayout = QVBoxLayout()
        self.middleFrame.setLayout(self.newMiddleLayout)
        self.label = QLabel('gf')
        self.newMiddleLayout.addWidget(self.label)
    def St1(self):
        pass
    def Ph1(self):
        pass
    def Mt1(self):
        pass
    def Twocourse(self):
        pass
    def St2(self):
        pass
    def Mt2(self):
        pass
    def Ph2(self):
        pass
    def Threecourse(self):
        pass
    def St3(self):
        pass
    def Mt3(self):
        pass
    def Ph3(self):
        pass
    def divCourse(self):
        pass
    def classRatio(self):
        list = {'male':[59] , 'female':[9]}
        claData = pd.DataFrame(list , index = ['students'])
        graph = sea.distplot(claData['male'] , kde = False)
        containerLabel = QLabel(graph)
        self.midoLayout.addWidget(containerLabel)
        print(claData.head())
    def Ages(self):
        pass
    def Leaders(self):
        pass
    def WhatsApp(self):
        pass
    def ClassRoleDivision(self):
        pass
    def classPartners(self):
        pass
    def ApplicationManagement(self):
        pass
    def AppCoders(self):
        pass
    def AppLanguage(self):
        pass
    def crContacts(self):
        pass
    def MemberContacts(self):
        pass
    def infoLoader(self):
        pass
    def actionCreator(self):
        #filemenu
        self.myProfile = QAction('My &Profile' , self , shortcut = 'Ctrl + P' , 
                                 statusTip = 'Enter your profile' , triggered = self.Profile)
        
        self.myProject = QAction('&My Project' , self , shortcut = 'Ctrl + Alt + P',
                                 statusTip = "view your saved project" , triggered = self.Project)
        self.jobAdvisor = QAction('&Job Advisor' , self , shortcut = 'Ctrl + J' ,
                                  statusTip = 'job searching and carreer fitting' ,
                                  triggered = self.Job)
        self.codeView = QAction('View &Code' , self , shortcut = 'Alt +C',
                                statusTip = 'View this app\'s code' , triggered = self.codeViewer)
        self.codeAppend = QAction('Add &Ur Stuffs' , self ,shortcut = 'Shift + A' ,
                                  statusTip = 'add your own components to the app code' , 
                                  triggered = self.Append)
        self.quitter = QAction('Quit' , self , shortcut = 'Alt + E' , 
                               statusTip = 'quit the app' , triggered = self.close)
        #edit menu
        self.userProfile = QAction('&Info Edit' , self , shortcut = 'Ctrl + I' , 
                                   statusTip = 'Edit Profile Info' , triggered = self.infoedit)
        self.configApp = QAction('Co&nfigure' , self , shortcut = 'Alt + S' , 
                                 statusTip = 'configure app' , triggered = self.configure)
        #Udsm menu
        self.prosp = QAction('P&rospectus' , self , shortcut = 'Ctrl + R' , 
                             statusTip = 'View the prospectus' , triggered = self.prospectus)
        self.ttable = QAction('&TimeTable' ,self , checkable=True, shortcut = "Ctrl + T" , 
                              statusTip = 'view semester\'s timetable' , triggered = self.timetable)
        self.pic = QAction('Varsity Gallery' , self , shortcut = 'Alt + P' ,
                           statusTip = 'some of the varsities picz' , triggered = self.picz)
        self.map = QAction('Map map' , self , shortcut = 'Ctrl + M' , 
                           statusTip = 'View the University Map' , triggered = self.mapper)
        self.Administratos = QAction('&Administration' , self , shortcut = 'Ctrl + Alt + A' , 
                                     statusTip = 'View the Varsity Administration' , 
                                     triggered = self.Administration)
        #courses menu
            #year1 submenu
        self.All1 = QAction('All' , self , shortcut = 'Ctrl + l' , 
                            statusTip = 'Year One ALL courses' , triggered = self.Onecourse)
                #optional/selective subjects submenu
        self.St1 = QAction('St1' , self , statusTip = 'st first year' , 
                           triggered = self.St1)
        self.Mt1 = QAction('Mt1' , self , statusTip = 'Mt first year' , 
                           triggered = self.Mt1)
        self.Ph1 = QAction('Ph1' , self , statusTip = 'Ph first year' , 
                           triggered = self.Ph1)
            #year2 submenu
        self.All2 = QAction('All' , self , statusTip = 'Year two ALL courses' , 
                            triggered = self.Twocourse)
                #optional year two
        self.St2 = QAction('St2' , self , statusTip = 'St second year' , 
                           triggered = self.St2)
        self.Mt2 = QAction('Mt2' , self , statusTip = 'Mt second year' , 
                           triggered = self.Mt2)
        self.Ph2 = QAction('Ph2' , self , statusTip = 'Ph second year' , 
                           triggered = self.Ph2)
            #year3 submenu
        self.All3 = QAction('All' , self , statusTip = 'Year Three ALL courses' , 
                           triggered = self.Threecourse)
                #optional year three
        self.St3 = QAction('St3' , self , statusTip = 'st Third year' , 
                           triggered = self.St3)
        self.Mt3 = QAction('Mt3' , self , statusTip = 'Mt Third year' , 
                           triggered = self.Mt3)
        self.Ph3 = QAction('Ph3' , self , statusTip = 'Ph Third year' , 
                           triggered = self.Ph3)
        
        #About us Submenu
        self.divCourse = QAction("&Course Division" , self , shortcut = 'Ctrl +Alt+ D' , 
                                 statusTip = 'How many have taken what' ,
                                 triggered = self.divCourse)
        self.Ratio = QAction("&Ratio" , self , shortcut = 'Ctrl + D' , 
                                 statusTip = 'Ladies Vs Gents ratio.. Boys not included' ,
                                 triggered = self.classRatio)
        self.ageRange = QAction("&Ages" , self , shortcut = 'Ctrl+ Shift + D' , 
                                 statusTip = 'kids vs oldies like Emanuel Sanga' ,
                                 triggered = self.Ages)
        self.leaders = QAction('&Leaders' ,self , shortcut = 'Alt + L' ,
                               statusTip = 'leaderz and their positions' , triggered = self.Leaders)
        self.watsap = QAction('&WhatsApp' , self , shortcut = 'Alt + W' , 
                              statusTip = 'WhatsApp chat link' , triggered = self.WhatsApp)
        self.division = QAction('&Division' , self , shortcut = 'Alt + Z' , 
                              statusTip = 'Roles division in our class' , 
                              triggered = self.ClassRoleDivision)
        self.partners = QAction('Our &Partners' , self , shortcut = 'Shift + W' , 
                              statusTip = 'DepartMental Friends' , triggered = self.classPartners)
        self.management = QAction('&Management' , self  , statusTip = 'Application Management' ,
                                  triggered = self.ApplicationManagement)
        self.coder = QAction('Coders' , self  , statusTip = 'People Responsible for coding' ,
                                  triggered = self.AppCoders)
        self.language = QAction('Language' , self  , statusTip = 'Coding Language Used' ,
                                  triggered = self.AppLanguage)
        self.supporters = QAction('&Supporters' , self  , statusTip = 'People Who Make it work' ,
                                  triggered = self.AppCoders)
        
        #Help Menu
        self.cr = QAction('&Cr\'z Contacts' , self , shortcut = 'Ctrl + Alt + C',
                          statusTip = 'Cr\'z basic contact information' ,
                          triggered = self.crContacts)
        self.memberContact = QAction('Our C&ontacts' , self  , statusTip = 'Our Class\'Social Center' ,
                                  triggered = self.MemberContacts)
    def menuCreator(self):
        self.fileMenu = self.menuBar().addMenu('&File')
        self.fileMenu.addAction(self.myProfile)
        self.fileMenu.addAction(self.myProject)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.jobAdvisor)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.codeView)
        self.fileMenu.addAction(self.codeAppend)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitter)
        
        self.editMenu = self.menuBar().addMenu('E&dit')
        self.editMenu.addAction(self.userProfile)
        self.editMenu.addAction(self.configApp)
        
        self.udsmMenu = self.menuBar().addMenu('&Udsm')
        self.udsmMenu.addAction(self.prosp)
        self.udsmMenu.addAction(self.ttable)
        
        self.Overview = self.udsmMenu.addMenu('P&icz')
        self.Overview.addAction(self.pic)
        self.Overview.addAction(self.map)
        self.Overview.addAction(self.Administratos)
        
        
        self.courseMenu = self.menuBar().addMenu('&Courses')
        self.Year1 = self.courseMenu.addMenu("&First Year")
        self.Year1.addAction(self.All1)
        self.Selective1 = self.Year1.addMenu('&Opti0nal Courses')
        self.Selective1.addAction(self.St1)
        self.Selective1.addAction(self.Mt1)
        self.Selective1.addAction(self.Ph1)
        
        self.Year2 =self.courseMenu.addMenu('&Second Year')
        self.Year2.addAction(self.All2)
        self.Selective2 = self.Year2.addMenu('&Opti0nal Courses')
        self.Selective2.addAction(self.St2)
        self.Selective2.addAction(self.Mt2)
        self.Selective2.addAction(self.Ph2)
        
        self.Year3 = self.courseMenu.addMenu('&Third year')
        self.Year3.addAction(self.All3)
        self.Selective3 = self.Year3.addMenu('&Opti0nal Courses')
        self.Selective3.addAction(self.St3)
        self.Selective3.addAction(self.Mt3)
        self.Selective3.addAction(self.Ph3)
        
        
        self.aboutMenu = self.menuBar().addMenu('About &Us')
        self.ourClass = self.aboutMenu.addMenu('Our Class')
        self.ourClass.addAction(self.divCourse)
        self.ourClass.addAction(self.Ratio)
        self.ourClass.addAction(self.ageRange)
        
        self.aboutMenu.addAction(self.leaders)
        
        self.chatlink = self.aboutMenu.addMenu('Chatting Links')
        self.chatlink.addAction(self.watsap)
                       
        self.aboutMenu.addAction(self.division)
        self.aboutMenu.addAction(self.partners)
        
        self.wcsApp = self.aboutMenu.addMenu('Mor&e')
        self.wcsApp.addAction(self.management)
        self.wcsApp.addAction(self.coder)
        self.wcsApp.addAction(self.language)
        self.wcsApp.addAction(self.supporters)
        
        
        self.helpMenu = self.menuBar().addMenu('&Need Help?')
        self.helpMenu.addAction(self.cr)
        self.helpMenu.addAction(self.memberContact)


    def middleFrameLoader(self):
        classey = '/codes/classey/simplepage.html'
        
        self.webLabel = QLabel('WCS web')
        self.webDisplay = QTextEdit()
        self.webDisplay.setHtml(classey)
        self.webDisplay.setReadOnly(True)
        self.webDisplay.setStyleSheet('padding:0px 0px 0px 0px')
        self.midoLayout.addWidget(self.webLabel)
        self.midoLayout.addWidget(self.webDisplay)
        self.middleFrame.setLayout(self.midoLayout)
    def Toolbar(self):
        self.toolbar = self.addToolBar("WorkSpace")
        self.toolbar.setMovable(False)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolbar.setIconSize(QSize(40 , 60))
        
        self.profile = QAction(QIcon('icons/profile.png') , 'profile' , self , statusTip = 'your profile' )
        self.course = QAction(QIcon('icons/courses.png') , 'Courses' , self)
        self.prospectus = QAction(QIcon('icons/prosp.png') , 'Prospectus' , self)
        self.geeks = QAction(QIcon('icons/geek.jpg') , 'Geeks' , self)
        self.importer = QAction(QIcon('icons/import.png') , 'Import' , self)
        
        
        #self.profile.triggered.connect(lambda : self.Profile)
        #self.course.triggered.connect(self.divCourse)
        #self.prospectus.triggered.connect(self.prosp)
        #self.geeks.triggered.connect(self.coder)
        #self.importer.triggered.connect(self.infoedit)
        
        self.toolbar.addAction(self.profile)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.course)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.prospectus)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.geeks)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.importer)
        pass
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
