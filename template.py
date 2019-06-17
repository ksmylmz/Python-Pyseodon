import sys

from PyQt5.QtWidgets import QApplication
from components import *
from PyQt5.Qt import QHBoxLayout,QGridLayout



class _mainView():
    window = None
    mainLayout = None
    result = None
    btnMetaTags=None,
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
    app = None
     
    def __init__(self):
        
        self.app = QApplication(sys.argv)
            
        self.window = App(100,100,900,500,"Pyseodon Audit")
        
        c = makeComponets()
        
        self.mainLayout = QGridLayout()
        
        self.result = QLabel("")
        
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
        self.btnScriptUnMinify = c.makeBtn("Check Unminify Script")
        self.btnCssUnMinify = c.makeBtn("Check Unminify Script")

        
    
        
    
        #appendLayoutsToMain Layout
        self.mainLayout.addWidget(self.btnPerformance,0,0,1,1)
        self.mainLayout.addWidget(self.btnMetaTags,0,1,1,1)
        self.mainLayout.addWidget(self.btnHtags,1,0,1,1)
        self.mainLayout.addWidget(self.btnImgAlt,1,1,1,1)
        self.mainLayout.addWidget(self.btnBroken,2,0,1,1)
        self.mainLayout.addWidget(self.btnUnfrendly,2,1,1,1)
        self.mainLayout.addWidget(self.btnAnalytics,3,0,1,1)
        self.mainLayout.addWidget(self.btnMobil,3,1,1,1)
        self.mainLayout.addWidget(self.cgkFlash,4,0,1,1)
        self.mainLayout.addWidget(self.btnIframe,4,1,1,1)
        self.mainLayout.addWidget(self.btnFavico,5,0,1,1)
        self.mainLayout.addWidget(self.checkGzip,5,1,1,1)
        self.mainLayout.addWidget(self.btnScriptUnMinify,6,0,1,1)
        self.mainLayout.addWidget(self.btnCssUnMinify,6,1,1,1)
        self.mainLayout.addWidget(self.result,0,2,7,1)
     
        
        #setMainLayout
        self.window.setLayout(self.mainLayout)
       
    def showWindow(self):
         sys.exit(self.app.exec_())
         
    def setResult(self,text):
        style="<center><div style='width:100%;height:100%;margin:5px;padding-top:5px;font-size:12px'>"
        style+="<b>"+ text+"</b></div></center>"
        self.result.setText(style)
 
