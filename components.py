from PyQt5.QtWidgets import  QWidget,QPushButton,QMessageBox,QDialog
from PyQt5.QtGui import QIcon
from PyQt5.uic.Compiler.qtproxies import QtGui
from components import *
from PyQt5.Qt import QHBoxLayout,QGridLayout
from PyQt5.Qt import QLabel,QMainWindow



class App(QMainWindow):

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
        self.setWindowIcon(QIcon('images/logo.png'))  
        self.show()
        
        
class makeComponets():
    
    def makeLabel(self,title=""):
        label = QLabel(title)
        return label
    
    def makeBtn(self,title="",parent=None):
        btn = QPushButton(title,parent)
        return btn
    
    

        
        
        
