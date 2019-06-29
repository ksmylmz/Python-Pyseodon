# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_template.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 658)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.searchBox = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBox.setGeometry(QtCore.QRect(10, 10, 710, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchBox.setFont(font)
        self.searchBox.setStyleSheet("border-radius : 8%;\n"
"border:solid 1px #ccc;")
        self.searchBox.setObjectName("searchBox")
        self.btnsearchBox = QtWidgets.QPushButton(self.centralwidget)
        self.btnsearchBox.setGeometry(QtCore.QRect(740, 10, 101, 31))
        self.btnsearchBox.setStyleSheet("    color: #FFF;\n"
"    background-color :#C7AFBD;\n"
"    border:solid 1px #FFF;\n"
"   border-radius:5%;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnsearchBox.setIcon(icon)
        self.btnsearchBox.setObjectName("btnsearchBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 871, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("background:#DDECEF;\n"
"color:rgb(0, 0, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 271, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.menuGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.menuGrid.setContentsMargins(0, 0, 0, 0)
        self.menuGrid.setObjectName("menuGrid")
        self.btnsearchBox_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_11.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_11.setObjectName("btnsearchBox_11")
        self.menuGrid.addWidget(self.btnsearchBox_11, 4, 0, 1, 1)
        self.btnsearchBox_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_14.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_14.setObjectName("btnsearchBox_14")
        self.menuGrid.addWidget(self.btnsearchBox_14, 6, 0, 1, 1)
        self.btnsearchBox_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_6.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_6.setObjectName("btnsearchBox_6")
        self.menuGrid.addWidget(self.btnsearchBox_6, 3, 1, 1, 1)
        self.btnsearchBox_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_5.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_5.setObjectName("btnsearchBox_5")
        self.menuGrid.addWidget(self.btnsearchBox_5, 2, 0, 1, 1)
        self.btnsearchBox_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_8.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_8.setObjectName("btnsearchBox_8")
        self.menuGrid.addWidget(self.btnsearchBox_8, 1, 0, 1, 1)
        self.btnsearchBox_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_15.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_15.setObjectName("btnsearchBox_15")
        self.menuGrid.addWidget(self.btnsearchBox_15, 6, 1, 1, 1)
        self.btnsearchBox_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_4.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_4.setObjectName("btnsearchBox_4")
        self.menuGrid.addWidget(self.btnsearchBox_4, 2, 1, 1, 1)
        self.btnsearchBox_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_13.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_13.setObjectName("btnsearchBox_13")
        self.menuGrid.addWidget(self.btnsearchBox_13, 5, 1, 1, 1)
        self.btnsearchBox_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_9.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_9.setObjectName("btnsearchBox_9")
        self.menuGrid.addWidget(self.btnsearchBox_9, 1, 1, 1, 1)
        self.btnsearchBox_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_7.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_7.setObjectName("btnsearchBox_7")
        self.menuGrid.addWidget(self.btnsearchBox_7, 3, 0, 1, 1)
        self.btnsearchBox_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_3.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_3.setObjectName("btnsearchBox_3")
        self.menuGrid.addWidget(self.btnsearchBox_3, 0, 1, 1, 1)
        self.btnsearchBox_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_2.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_2.setObjectName("btnsearchBox_2")
        self.menuGrid.addWidget(self.btnsearchBox_2, 0, 0, 1, 1)
        self.btnsearchBox_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_12.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_12.setObjectName("btnsearchBox_12")
        self.menuGrid.addWidget(self.btnsearchBox_12, 5, 0, 1, 1)
        self.btnsearchBox_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_10.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_10.setObjectName("btnsearchBox_10")
        self.menuGrid.addWidget(self.btnsearchBox_10, 4, 1, 1, 1)
        self.btnsearchBox_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_16.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_16.setObjectName("btnsearchBox_16")
        self.menuGrid.addWidget(self.btnsearchBox_16, 7, 0, 1, 1)
        self.btnsearchBox_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnsearchBox_17.setStyleSheet("    color: #000;\n"
"    background-color :#FDE8D7;\n"
"    border:solid 1px #000;\n"
"   border-radius:5%;\n"
"padding:8px 16px;\n"
"\n"
"font: 75 10pt \"Arial\";")
        self.btnsearchBox_17.setObjectName("btnsearchBox_17")
        self.menuGrid.addWidget(self.btnsearchBox_17, 7, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 60, 281, 301))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../images/poseidon_by_ungartattoo.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 50, 301, 351))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(85, 0, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 430, 851, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 480, 851, 161))
        self.plainTextEdit.setStyleSheet("border:5px solid #ccc;\n"
"border-radius:5%;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 450, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:#ccc;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(820, 440, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(70, 450, 31, 31))
        self.toolButton.setMaximumSize(QtCore.QSize(32, 32))
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(32, 32))
        self.toolButton.setObjectName("toolButton")
        self.label.raise_()
        self.searchBox.raise_()
        self.btnsearchBox.raise_()
        self.gridLayoutWidget.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.plainTextEdit.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.toolButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchBox.setPlaceholderText(_translate("MainWindow", "input the scan url"))
        self.btnsearchBox.setText(_translate("MainWindow", "Scan"))
        self.btnsearchBox_11.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_14.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_6.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_5.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_8.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_15.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_4.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_13.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_9.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_7.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_3.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_2.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_12.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_10.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_16.setText(_translate("MainWindow", "chk"))
        self.btnsearchBox_17.setText(_translate("MainWindow", "chk"))
        self.label_3.setText(_translate("MainWindow", "result"))
        self.label_4.setText(_translate("MainWindow", " Console "))
        self.label_5.setText(_translate("MainWindow", "About"))


