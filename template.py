import sys

from PyQt5.QtWidgets import QApplication
from components import *
from PyQt5.Qt import QHBoxLayout,QGridLayout,QPixmap,QPlainTextEdit, QLabel, QLineEdit
from PyQt5 import QtGui
import os


class _mainView():
    window = None
    mainLayout = None
    result = None
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
    clearConsole = None
    app = None
     
    def __init__(self):
        
        self.app = QApplication(sys.argv)
            
        self.window = App(100,100,900,500,"Pyseodon Audit")
        
        c = makeComponets()
        
        self.mainLayout = QGridLayout()
        
        self.searchBox = QLineEdit("")
        self.searchBox.setPlaceholderText("search url")
        font = QtGui.QFont("Times", 15, QtGui.QFont.Bold)
        self.searchBox.setFont(font)
        
        
        self.result = QLabel("")
        self.result.setOpenExternalLinks(True)
        
        self.console =QPlainTextEdit("")
        
        
        self.btnsearchBox = c.makeBtn("Scan")
        self.btnMetaTags = c.makeBtn("Check Meta Tags")
        self.btnHtags = c.makeBtn("Check H Tags")
        self.btnImgAlt = c.makeBtn("Check Img Alt")
        self.btnBroken = c.makeBtn("Check Broken Urls")
        self.btnUnfrendly = c.makeBtn("Check Unfrendly Urls")
        self.btnAnalytics = c.makeBtn("Check Analytics Tag")
        self.btnMobil = c.makeBtn("Check Responsive View")
        self.cgkFlash = c.makeBtn("Check Flash Tags")
        self.btnIframe = c.makeBtn("Check Iframe Tags")
        self.btnFavico = c.makeBtn("Check Favico")
        self.btnPerformance = c.makeBtn("Check Performance")
        self.checkGzip = c.makeBtn("Check Compression")
        self.btnScriptUnMinify = c.makeBtn("Check Unminify Js")
        self.btnCssUnMinify = c.makeBtn("Check Unminify Css")
        self.btninlineCss = c.makeBtn("Check Inline Css")
        self.clearConsole = c.makeBtn("Clear Console")
        

        
    
        
    
        #appendLayoutsToMain Layout
        self.mainLayout.addWidget(self.searchBox,0,0,1,8)
        self.mainLayout.addWidget(self.btnsearchBox,0,8,1,2)
        self.mainLayout.addWidget(self.btnPerformance,1,0,1,1)
        self.mainLayout.addWidget(self.btnMetaTags,1,1,1,1)
        self.mainLayout.addWidget(self.btnHtags,2,0,1,1)
        self.mainLayout.addWidget(self.btnImgAlt,2,1,1,1)
        self.mainLayout.addWidget(self.btnBroken,3,0,1,1)
        self.mainLayout.addWidget(self.btnUnfrendly,3,1,1,1)
        self.mainLayout.addWidget(self.btnAnalytics,4,0,1,1)
        self.mainLayout.addWidget(self.btnMobil,4,1,1,1)
        self.mainLayout.addWidget(self.cgkFlash,5,0,1,1)
        self.mainLayout.addWidget(self.btnIframe,5,1,1,1)
        self.mainLayout.addWidget(self.btnFavico,6,0,1,1)
        self.mainLayout.addWidget(self.checkGzip,6,1,1,1)
        self.mainLayout.addWidget(self.btnScriptUnMinify,7,0,1,1)
        self.mainLayout.addWidget(self.btnCssUnMinify,7,1,1,1)
        self.mainLayout.addWidget(self.btninlineCss,8,0,1,1)
        self.mainLayout.addWidget(self.clearConsole,8,1,1,1)
        self.mainLayout.addWidget(self.result,0,2,7,1)
        self.mainLayout.addWidget(self.console,9,0,1,10)
     
        
        #setMainLayout
        self.window.setLayout(self.mainLayout)
       
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
    




 
