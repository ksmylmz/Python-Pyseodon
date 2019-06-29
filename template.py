import sys

from PyQt5.QtWidgets import QApplication,QMessageBox
from components import *
from PyQt5.Qt import QHBoxLayout,QGridLayout,QPixmap,QPlainTextEdit, QLabel, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import os



class _mainView():
    
    #definitions
    centralwidget = None
    window = None
    bgLabel = None
    mainLayout = None
    menuGrid = None
    console=None,
    searchBox = None
    btnsearchBox = None
    btnMetaTags=None
    btnHtags=None
    btnImgAlt=None
    btnBroken=None
    btnUnfrendly=None
    btnAnalytics=None
    btnMobil=None
    cgkFlash=None
    btnIframe=None
    btnFavico=None
    btnPerformance=None
    checkGzip=None
    btnScriptUnMinify=None
    btnCssUnMinify = None
    btninlineCss = None
    btnKeywords  =None
    logoLabel  =None
    result = None
    line = None
    consolelabel = None
    about = None
    
    clearConsole = None
    app = None
    
     
    def __init__(self):
        
        self.app = QApplication(sys.argv)
        
        c = makeComponets()
        #window    
        self.window = App(50,50,871,658,"Pyseodon Audit")
        
        self.centralwidget = QWidget()
        #self.centralwidget.setObjectName("centralwidget")
        
        ##search Box
        self.searchBox = QLineEdit(self.centralwidget)
        self.searchBox.setGeometry(QtCore.QRect(10, 10, 710, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchBox.setFont(font)
        self.searchBox.setStyleSheet("border-radius : 8%; border:solid 1px #ccc;")
        self.searchBox.setPlaceholderText("enter the scan url")
     
        #searchButton    
        self.btnsearchBox = c.makeBtn("Scan",self.centralwidget)
        self.btnsearchBox.setGeometry(QtCore.QRect(740, 10, 101, 31))
        searcBtnStyle = "color: #FFF; background-color :#C7AFBD;border:solid 1px #FFF; border-radius:5%";
        self.btnsearchBox.setStyleSheet(searcBtnStyle)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnsearchBox.setIcon(icon)   
        
        #backgroundLabel

        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, -20, 871, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.bgLabel.sizePolicy().hasHeightForWidth())
        self.bgLabel.setSizePolicy(sizePolicy)
        self.bgLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bgLabel.setStyleSheet("background:#DDECEF; color:rgb(0, 0, 255);")  
        
        #gridLayout
        self.mainLayout = QtWidgets.QWidget(self.centralwidget)
        self.mainLayout.setGeometry(QtCore.QRect(10, 50, 271, 361))
        
        self.menuGrid = QtWidgets.QGridLayout(self.mainLayout)
        self.menuGrid.setContentsMargins(0, 0, 0, 0)
        
        #btnsStyle       
        btnStyle = "color: #000; background-color :#FDE8D7;"
        btnStyle += "border:solid 1px #000; brder-radius:5%;"
        btnStyle += "padding:8px 16px; brder-radius:5%;"
        
        
        self.btnMetaTags = c.makeBtn("Check Meta Tags",self.mainLayout)
        self.btnMetaTags.setStyleSheet(btnStyle)
        
        self.btnHtags = c.makeBtn("Check H Tags",self.mainLayout)
        self.btnHtags.setStyleSheet(btnStyle)
        
        self.btnImgAlt = c.makeBtn("Check Img Alt",self.mainLayout)
        self.btnImgAlt.setStyleSheet(btnStyle)
        
        self.btnBroken = c.makeBtn("Check Broken Urls",self.mainLayout)
        self.btnBroken.setStyleSheet(btnStyle)
        
        self.btnUnfrendly = c.makeBtn("Check Unfrendly Urls",self.mainLayout)
        self.btnUnfrendly.setStyleSheet(btnStyle)
        
        self.btnAnalytics = c.makeBtn("Check Analytics Tag",self.mainLayout)
        self.btnAnalytics.setStyleSheet(btnStyle)
        
        self.btnMobil = c.makeBtn("Check Responsive",self.mainLayout)
        self.btnMobil.setStyleSheet(btnStyle)
        
        self.cgkFlash = c.makeBtn("Check Flash Tags",self.mainLayout)
        self.cgkFlash.setStyleSheet(btnStyle)

        
        self.btnIframe = c.makeBtn("Check Iframe Tags",self.mainLayout)
        self.btnIframe.setStyleSheet(btnStyle)
        
        self.btnFavico = c.makeBtn("Check Favico",self.mainLayout)
        self.btnFavico.setStyleSheet(btnStyle)
        
        self.btnPerformance = c.makeBtn("Check Performance",self.mainLayout)
        self.btnPerformance.setStyleSheet(btnStyle)
        
        self.checkGzip = c.makeBtn("Check Compression",self.mainLayout)
        self.checkGzip.setStyleSheet(btnStyle)
        
        self.btnScriptUnMinify = c.makeBtn("Check Unminify Js",self.mainLayout)
        self.btnScriptUnMinify.setStyleSheet(btnStyle)
        
        self.btnCssUnMinify = c.makeBtn("Check Unminify Css",self.mainLayout)
        self.btnCssUnMinify.setStyleSheet(btnStyle)
        
        self.btninlineCss = c.makeBtn("Check Inline Css",self.mainLayout)
        self.btninlineCss.setStyleSheet(btnStyle)
        
    
        
        
        #appendLayoutsToMain Layout

        self.menuGrid.addWidget(self.btnPerformance,1,0,1,1)
        self.menuGrid.addWidget(self.btnMetaTags,1,1,1,1)
        self.menuGrid.addWidget(self.btnHtags,2,0,1,1)
        self.menuGrid.addWidget(self.btnImgAlt,2,1,1,1)
        self.menuGrid.addWidget(self.btnBroken,3,0,1,1)
        self.menuGrid.addWidget(self.btnUnfrendly,3,1,1,1)
        self.menuGrid.addWidget(self.btnAnalytics,4,0,1,1)
        self.menuGrid.addWidget(self.btnMobil,4,1,1,1)
        self.menuGrid.addWidget(self.cgkFlash,5,0,1,1)
        self.menuGrid.addWidget(self.btnIframe,5,1,1,1)
        self.menuGrid.addWidget(self.btnFavico,6,0,1,1)
        self.menuGrid.addWidget(self.checkGzip,6,1,1,1)
        self.menuGrid.addWidget(self.btnScriptUnMinify,7,0,1,1)
        self.menuGrid.addWidget(self.btnCssUnMinify,7,1,1,1)
        self.menuGrid.addWidget(self.btninlineCss,8,0,1,1)



        #logolabel
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(580, 60, 281, 301))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("images/poseidon_by_ungartattoo.png"))
        
        #resultlabel 
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(290, 50, 301, 351))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setStyleSheet("color:rgb(85, 0, 127);")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        
        #line
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 430, 851, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 480, 851, 161))
        self.plainTextEdit.setStyleSheet("border:5px solid #ccc; border-radius:5%;")
        
        
        #console
        self.console = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(10, 480, 851, 161))
        self.console.setStyleSheet("border:5px solid #ccc; border-radius:5%;")
        
        
        #consoleLabel
        self.consolelabel = QtWidgets.QLabel(self.centralwidget)
        self.consolelabel.setGeometry(QtCore.QRect(10, 450, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.consolelabel.setFont(font)
        self.consolelabel.setStyleSheet("background-color:#ccc;")
        self.consolelabel.setText(" Console ")
        
        #about
        self.about = QtWidgets.QLabel(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(810, 635, 50, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setUnderline(True)
        self.about.setFont(font)
        self.about.setText("<a href='http://bit.ly/2FG1SK1'> About</a>")
        self.about.setOpenExternalLinks(True)

        
        #clear Consloe
        self.clearConsole = QtWidgets.QToolButton(self.centralwidget)
        self.clearConsole.setGeometry(QtCore.QRect(70, 450, 31, 31))
        self.clearConsole.setMaximumSize(QtCore.QSize(32, 32))
        self.clearConsole.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearConsole.setIcon(icon1)
        self.clearConsole.setIconSize(QtCore.QSize(32, 32))
        
        
        self.bgLabel.raise_()
        self.searchBox.raise_()
        self.btnsearchBox.raise_()
        self.mainLayout.raise_()
        self.logoLabel.raise_()
        self.result.raise_()
        self.line.raise_()
        self.console.raise_()
        self.consolelabel.raise_()
        self.about.raise_()
        self.clearConsole.raise_()




        #self.centralwidget.setLayout(self.mainLayout)
        self.window.setCentralWidget(self.centralwidget)
        


       
    def showWindow(self):
         sys.exit(self.app.exec_())
         
    def setResult(self,text):
        style="<center><div style='width:100%;height:100%;margin:5px;padding-top:5px;font-size:12px'>"
        style+="<b>"+ text+"</b></div></center>"
        self.result.setText(style)
        
    def appendConsole(self,text):
        consoleTex = self.console.toPlainText()
        content  =""
        content  +=consoleTex
        content  +="\n\n"
        content  +=text
        self.console.setPlainText(content)
        
        
    def dialog(self,title,contet):
        msg = QMessageBox()
        msg.setText(contet)
        msg.setWindowTitle(title)            
        msg.exec()
        
    




 
