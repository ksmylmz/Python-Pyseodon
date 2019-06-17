from PyQt5.QtWidgets import  QWidget,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.uic.Compiler.qtproxies import QtGui
from components import *
from PyQt5.Qt import QHBoxLayout,QGridLayout
from PyQt5.Qt import QLabel


class App(QWidget):

    def __init__(self,left,top,width,heigth,title):
        super().__init__()
        self.title = title
        self.left = left
        self.top = top
        self.width = width
        self.height = heigth
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)         
        #self.setWindowIcon(QtGui.QIcon('images/f8e1cc1e5ffca73092a340fa648ef8a2.png'))  
        self.show()
        
        
class makeComponets():
    
    def makeLabel(self,title):
        label = QLabel(title)
        return label
    
    def makeBtn(self,title):
        btn = QPushButton(title)
        return btn
        
        
