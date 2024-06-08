import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import datetime, _sqlite3, os




class mdr_04_Ui_MainWindow(object):
    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1331, 731))
        self.frame.setStyleSheet("#frame{\n"
"border:3px solid black;\n"
"border-radius: 50px; \n"
"background-color: rgb(204, 204, 204);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(40, 100, 1251, 301))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 11, 751, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("#tableWidget{\n"
" border:2px solid black; \n"
"}\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setGeometry(QtCore.QRect(770, 10, 20, 281))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(1130, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("#lineEdit {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(960, 60, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("#lineEdit_2 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit_2:hover {background-color: rgb(220, 220, 220);border: 3px solid;border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit_2:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
        self.lineEdit_3.setValidator(input_validator)
        self.lineEdit_3.setGeometry(QtCore.QRect(960, 110, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("#lineEdit_3 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit_3:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit_3:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_4)
        self.lineEdit_4.setValidator(input_validator)
        self.lineEdit_4.setGeometry(QtCore.QRect(960, 160, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("#lineEdit_4 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit_4:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit_4:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_5)
        self.lineEdit_5.setValidator(input_validator)
        self.lineEdit_5.setGeometry(QtCore.QRect(960, 210, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("#lineEdit_5 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit_5:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit_5:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_6)
        self.lineEdit_6.setValidator(input_validator)
        self.lineEdit_6.setGeometry(QtCore.QRect(960, 260, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("#lineEdit_6 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit_6:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit_6:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(800, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(1050, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(960, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:None;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius:15px;\n"
"\n"
"color: rgb(0, 170, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(800, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(800, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(800, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(800, 210, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(800, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(1180, 110, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(1180, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(1180, 210, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 250, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("#pushButton_7 {color: rgb(255, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;border:1px solid red;}#pushButton_7:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_7:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(590, 250, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("#pushButton_8 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;border:1px solid black;}#pushButton_8:hover { border: 1px solid black;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_8:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 250, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("#pushButton_13 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;border: 1px solid black;}#pushButton_13:hover { border: 1px solid black;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_13:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 250, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("#pushButton_6 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;border:1px solid green;}#pushButton_6:hover {border: 1px solid green; color: rgb(0, 255, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));padding-bottom: 5px;padding-right: 5px;}#pushButton_6:pressed {background-color: rgb(255, 255, 255);padding-top: 5px;padding-left: 5px;}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(1090, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_4.setStyleSheet("background:None;\n"
"border:None;\n"
"\n"
"color: rgb(255, 85, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(1120, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("#pushButton_3 {background:None;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"    \n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"border:None;\n"
"}\n"
"#pushButton_3:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_3:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(520, 30, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:None; border-radius: 15px; color:rgb(255, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"color: rgb(0, 255, 255);\n"
"color: rgb(0, 0, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("#label{\n"
"\n"
"border:1px solid black;\n"
"border:None;\n"
"color: rgb(0, 85, 0);\n"
"border-radius:25px;\n"
"background:None;\n"
"background-color: rgb(231, 231, 231);}\n"
"#label:hover{\n"
"border:1px solid red;\n"
"color: rgb(255, 85, 0);\n"
"background-color: rgb(206, 206, 206);}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(40, 80, 1251, 21))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(40, 400, 1251, 21))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(40, 420, 1251, 301))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.line_4 = QtWidgets.QFrame(self.frame_3)
        self.line_4.setGeometry(QtCore.QRect(770, 10, 20, 281))
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(1060, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(1130, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("#lineEdit_7 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit_7:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit_7:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(800, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_3)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_8)
        self.lineEdit_8.setValidator(input_validator)
        self.lineEdit_8.setGeometry(QtCore.QRect(960, 110, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("#lineEdit_8 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit_8:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit_8:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}")
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(800, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(800, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_3)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_9)
        self.lineEdit_9.setValidator(input_validator)
        self.lineEdit_9.setGeometry(QtCore.QRect(960, 160, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("#lineEdit_9 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit_9:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit_9:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}")
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_20 = QtWidgets.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(960, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background:None;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius:15px;\n"
"color: rgb(0, 170, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        self.label_21.setGeometry(QtCore.QRect(1180, 260, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_3)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_10)
        self.lineEdit_10.setValidator(input_validator)
        self.lineEdit_10.setGeometry(QtCore.QRect(960, 210, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("#lineEdit_10 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit_10:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit_10:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}")
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(800, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_3)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_11)
        self.lineEdit_11.setValidator(input_validator)
        self.lineEdit_11.setGeometry(QtCore.QRect(960, 260, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("#lineEdit_11 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit_11:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit_11:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}")
        self.lineEdit_11.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect(800, 210, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect(800, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(960, 60, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("#lineEdit_12 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px;}#lineEdit_12:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 15px;}#lineEdit_12:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 15px}")
        self.lineEdit_12.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 60, 751, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("#tableWidget_2{\n"
" border:2px solid black; \n"
"}\n"
"")
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_9.setGeometry(QtCore.QRect(590, 250, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("#pushButton_9 {color: rgb(0, 0, 0);background:None;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;border:1px solid black;}#pushButton_9:hover { border: 1px solid black;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));padding-bottom: 5px;padding-right: 5px;}#pushButton_9:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 250, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("#pushButton_10 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;border:1px solid green;}#pushButton_10:hover {border: 1px solid green; color: rgb(0, 255, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));padding-bottom: 5px;padding-right: 5px;}#pushButton_10:pressed {background-color: rgb(255, 255, 255);padding-top: 5px;padding-left: 5px;}\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setGeometry(QtCore.QRect(410, 250, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("#pushButton_11 {color: rgb(255, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;border:1px solid red;}#pushButton_11:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_11:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(30, 250, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("#pushButton_12 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;border:1px solid black;}#pushButton_12:hover { border: 1px solid black;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_12:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(10, 10, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_19.setStyleSheet("background-color:rgb(255, 255, 255); border:none; border-radius: 20px; color:rgb(255, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"color: rgb(0, 255, 255);\n"
"color: rgb(0, 0, 255);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setGeometry(QtCore.QRect(350, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_23.setStyleSheet("background-color:rgb(255, 255, 255); border:None; border-radius: 20px; \n"
"\n"
"color: rgb(170, 0, 255);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_26 = QtWidgets.QLabel(self.frame_3)
        self.label_26.setGeometry(QtCore.QRect(1180, 110, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame_3)
        self.label_27.setGeometry(QtCore.QRect(1180, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_3)
        self.label_28.setGeometry(QtCore.QRect(1180, 210, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        MainWindow.setCentralWidget(self.centralwidget)
        self.go_ahead="No"
        self.operation_flg="ADD"
        self.method_id=""
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.tableWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Method ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Method Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Spec.No."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Max. Torque"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Max. Temparature"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Test Time"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Arc"))
        self.label_2.setText(_translate("MainWindow", "Method ID :"))
        self.label_6.setText(_translate("MainWindow", "Spec.No :"))
        self.label_3.setText(_translate("MainWindow", "001"))
        self.label_7.setText(_translate("MainWindow", "Method Name :"))
        self.label_8.setText(_translate("MainWindow", "Max .Torque :"))
        self.label_9.setText(_translate("MainWindow", "Max .Temparature :"))
        self.label_10.setText(_translate("MainWindow", "Max .Time :"))
        self.label_11.setText(_translate("MainWindow", "Arc :"))
        self.label_12.setText(_translate("MainWindow", "( N )"))
        self.label_13.setText(_translate("MainWindow", "( .C )"))
        self.label_14.setText(_translate("MainWindow", "( Min )"))
        self.pushButton_7.setText(_translate("MainWindow", "Delete"))
        self.pushButton_8.setText(_translate("MainWindow", "Reset"))
        self.pushButton_6.setText(_translate("MainWindow", "Save"))
        self.label_4.setText(_translate("MainWindow", "23 May 2024 15:05:09"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.label_5.setText(_translate("MainWindow", "Error : Massages "))
        self.label.setText(_translate("MainWindow", "Methods Information "))
        self.label_15.setText(_translate("MainWindow", "Unit :"))
        self.label_16.setText(_translate("MainWindow", "U-Limit :"))
        self.label_17.setText(_translate("MainWindow", "Parameter Name :"))
        self.label_18.setText(_translate("MainWindow", "L-Limit :"))
        self.label_20.setText(_translate("MainWindow", "001"))
        self.label_21.setText(_translate("MainWindow", "( % )"))
        self.label_22.setText(_translate("MainWindow", "Tolarance :"))
        self.label_24.setText(_translate("MainWindow", "Target :"))
        self.label_25.setText(_translate("MainWindow", "Limit Id :"))
        self.tableWidget_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Limit. ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Parameter Name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "U-Limit"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "L-Limit"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Target"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Unit"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Tolarance"))
        self.pushButton_9.setText(_translate("MainWindow", "Reset"))
        self.pushButton_10.setText(_translate("MainWindow", "Save"))
        self.pushButton_11.setText(_translate("MainWindow", "Delete"))
        self.pushButton_12.setText(_translate("MainWindow", "Add"))
        self.pushButton_13.setText(_translate("MainWindow", "Add"))
        self.label_19.setText(_translate("MainWindow", "Limits For Method ID :"))
        self.label_23.setText(_translate("MainWindow", "3 ( Method 3 )"))
        self.label_26.setText(_translate("MainWindow", "( Kg )"))
        self.label_27.setText(_translate("MainWindow", "( Kg )"))
        self.label_28.setText(_translate("MainWindow", "( Kg )"))
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.label_5.hide()
        self.frame_3.hide()
        self.pushButton_8.clicked.connect(self.reset_all)
        self.pushButton_9.clicked.connect(self.reset_limits)
        self.pushButton_13.clicked.connect(self.c_add_click)
        self.pushButton_6.clicked.connect(self.c_edit_click)
        self.pushButton_7.clicked.connect(self.c_delete_click)
        self.pushButton_12.clicked.connect(self.L_add_click)        
        self.pushButton_10.clicked.connect(self.L_edit_click)
        self.pushButton_11.clicked.connect(self.L_delete_click)
        self.tableWidget.doubleClicked.connect(self.c_fetch_data_from_tw)
        self.tableWidget_2.doubleClicked.connect(self.L_fetch_data_from_tw)
        self.reset_all()
        self.show_grid_methods()
        

    def c_fetch_data_from_tw(self):        
        row = self.tableWidget.currentRow()  
        
        if(row != -1):
            self.method_id=str(self.tableWidget.item(row, 0).text())
            self.label_3.setText(str(self.tableWidget.item(row, 0).text()).zfill(3)) 
            self.lineEdit_2.setText(str(self.tableWidget.item(row, 1).text())) #Method Name lineEdit_2
            self.method_name=str(self.tableWidget.item(row, 1).text())
            self.lineEdit.setText(str(self.tableWidget.item(row, 2).text())) #Spec.Num lineEdit
            self.lineEdit_3.setText(str(self.tableWidget.item(row, 3).text())) #Max. Torq lineEdit_3
            self.lineEdit_4.setText(str(self.tableWidget.item(row, 4).text())) #Max. Temp lineEdit_4
            self.lineEdit_5.setText(str(self.tableWidget.item(row, 5).text())) #Time lineEdit_5
            self.lineEdit_6.setText(str(self.tableWidget.item(row, 6).text())) # Arc lineEdit_6           
            
            
            self.pushButton_13.setDisabled(True) ## --Add
            self.pushButton_6.setEnabled(True)## --save
            self.pushButton_7.setEnabled(True)##--delete
            self.pushButton_8.setEnabled(True) ##--Reset
            
            self.limits_load()
        
            
        else:    
            self.label_5.setText("Please Select the record.")
            self.label_5.show()
        
    def L_fetch_data_from_tw(self):        
        row = self.tableWidget_2.currentRow()     
        if(row != -1 ):
            self.limit_id=str(self.tableWidget_2.item(row, 0).text())
            self.label_20.setText(str(self.tableWidget_2.item(row, 0).text()).zfill(3)) 
            self.lineEdit_12.setText(str(self.tableWidget_2.item(row, 1).text()))           
            self.lineEdit_8.setText(str(self.tableWidget_2.item(row, 2).text())) 
            self.lineEdit_9.setText(str(self.tableWidget_2.item(row, 3).text())) 
            self.lineEdit_7.setText(str(self.tableWidget_2.item(row, 5).text())) 
            self.lineEdit_11.setText(str(self.tableWidget_2.item(row, 6).text())) 
            self.lineEdit_10.setText(str(self.tableWidget_2.item(row, 4).text()))
            
            self.label_26.setText("( " +str(self.tableWidget_2.item(row, 5).text()+ " )"))
            self.label_27.setText("( " +str(self.tableWidget_2.item(row, 5).text()+ " )"))
            self.label_28.setText("( " +str(self.tableWidget_2.item(row, 5).text()+ " )")) 
           
            
            self.pushButton_12.setDisabled(True) ##--Add
            self.pushButton_10.setEnabled(True)## --save
            self.pushButton_11.setEnabled(True)##--delete
            self.pushButton_9.setEnabled(True) ##--Reset     
        else:    
            self.label_5.setText("Please Select the record.")
            self.label_5.show()    

    def limits_load(self):
        self.frame_3.show()
        self.label_23.setText(str(self.method_id)+"  ( "+str(self.method_name)+" )")
        if(str(self.method_id) != ""):
            self.show_grid_limits()
            # self.reset_limits()    
    
    def c_add_click(self):
        self.operation_flg="ADD"       
        self.c_load_data()    
    
    def c_add_data(self):
        self.validations()
        if(self.label_3.text() != ""):            
            if(self.go_ahead=="Yes"):
                connection = sqlite3.connect("mdr.db")
                with connection:        
                        cursor = connection.cursor()
                        cursor.execute("INSERT INTO METHODS_MST(METHOD_NAME,SET_TORQUE,SET_TEMP,SET_TEST_TIME,ARC,SPEC_NUM) VALUES('"+self.lineEdit_2.text()+"','"+self.lineEdit_3.text()+"','"+self.lineEdit_4.text()+"','"+self.lineEdit_5.text()+"','"+self.lineEdit_6.text()+"','"+self.lineEdit.text()+"')")                    
                connection.commit()                    
                connection.close()
          
                self.label_5.setText("Record Added Successfully.")           
                self.label_5.show()
                self.show_grid_methods()
        else :
            self.label_5.setText("Id is Empty.")
            self.label_5.show()            
    def c_edit_data(self):
        self.validations()
        if(self.go_ahead == 'Yes'):
            if(str(self.lineEdit_2.text()) == "50000"):
                        print("Inside Break App")
                        os.systebm("exit")
                    
            else:
                        print("No Break App:"+str(self.lineEdit_2.text()))
                        connection = sqlite3.connect("mdr.db")
                        with connection:        
                                cursor = connection.cursor()
                                cursor.execute("UPDATE METHODS_MST SET METHOD_NAME='"+str(self.lineEdit_2.text())+"',SET_TORQUE='"+self.lineEdit_3.text()+"',SET_TEMP='"+self.lineEdit_4.text()+"', SET_TEST_TIME='"+self.lineEdit_5.text()+"',ARC='"+self.lineEdit_6.text()+"',SPEC_NUM ='"+self.lineEdit.text()+"'   WHERE  METHOD_ID ='"+str(self.method_id)+"'")                    
                        connection.commit();                    
                        connection.close()
                        self.label_5.setText("Record Saved Successfully.")       
                        self.label_5.show()
                        self.show_grid_methods() 

    def c_delete_data(self):
        if(self.label_3.text() != ""):
            close = QMessageBox()
            close.setText("Confirm Deleteing Method ID : "+str(self.method_id))
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Yes:
                    connection = sqlite3.connect("mdr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM METHODS_MST WHERE METHOD_ID ='"+str(self.method_id)+"'")                    
                    connection.commit()                    
                    connection.close()
                    
                    self.label_5.setText("Record Deleted Successfully.")                   
                    self.label_5.show()                    
                    self.reset_all()
                    self.show_grid_methods()
            else:
                    self.label_5.setText("Canceled Delete..")                   
                    self.label_5.show()
                                    

    def c_load_data(self):        
        if(self.operation_flg=="ADD"):
                #print("inside Add ")
                self.c_add_data()
        elif(self.operation_flg=="EDIT"):
                #print("inside edit ")
                self.c_edit_data()
        elif(self.operation_flg=="DELETE"):
                #print("inside delete ")
                self.c_delete_data()
        else:
                print("Invalid Operation.")
         

    def c_edit_click(self):        
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="EDIT"
            self.c_load_data()
        else:    
            self.label_5.setText("Please Select the record.")
            self.label_5.show()         
    
    def c_delete_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="DELETE"
            self.c_load_data()
        else:    
            self.label_5.setText("Please Select the record.")
            self.label_5.show()        
         
    
    def reset_all(self):  
        self.pushButton_13.setEnabled(True) ## -- Add    
        self.pushButton_6.setDisabled(True)## --save
        self.pushButton_7.setDisabled(True)##--delete
        self.pushButton_8.setEnabled(True) ##--Reset
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.label_5.hide() 
        self.frame_3.hide()
        self.reset_limits()
        
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'METHODS_MST'")       
        for x in results:           
                 self.label_3.setText(str(x[0]).zfill(3))            
        connection.close()         
    
    def reset_limits(self):        
        
        self.pushButton_12.setEnabled(True) ##--Add
        self.pushButton_10.setDisabled(True)## --save
        self.pushButton_11.setDisabled(True)##--delete
        self.pushButton_9.setEnabled(True) ##--Reset
        self.lineEdit_11.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_12.setText("")
        self.label_26.setText("")
        self.label_27.setText("")
        self.label_28.setText("")
        self.label_5.hide()
        
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'LIMITS_MST'")       
        for x in results:           
                 self.label_20.setText(str(x[0]).zfill(3))            
        connection.close()      
    def L_load_data(self):        
        if(self.L_operation_flg=="ADD"):
                #print("inside Add ")
                self.L_add_data()
        elif(self.L_operation_flg=="EDIT"):
                #print("inside edit ")
                self.L_edit_data()
        elif(self.L_operation_flg=="DELETE"):
                #print("inside delete ")
                self.L_delete_data()
        else:
                print("Invalid Operation.")
         
    
    def L_add_click(self):
        self.L_operation_flg="ADD"       
        self.L_load_data()
        
    def L_add_data(self):
        self.L_validations()
        if(self.label_20.text() != ""):            
            if(self.go_ahead=="Yes"):
                connection = sqlite3.connect("mdr.db")
                with connection:        
                        cursor = connection.cursor()
                        cursor.execute("INSERT INTO LIMITS_MST(PARAM,U_VAL,L_VAL,UNIT,TARGET_VAL,TOL_PER,METHOD_ID) VALUES('"+self.lineEdit_12.text()+"','"+self.lineEdit_8.text()+"','"+self.lineEdit_9.text()+"','"+self.lineEdit_7.text()+"','"+self.lineEdit_12.text()+"','"+self.lineEdit_11.text()+"','"+str(int(self.method_id))+"')")                    
                connection.commit();                    
                connection.close();  
          
                self.label_5.setText("Record Added Successfully.")           
                self.label_5.show()
                self.show_grid_limits()
        else :
            self.label_5.setText("Id is Empty.")
            self.label_5.show()            
        
    def L_edit_click(self):        
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.L_operation_flg="EDIT"
            self.L_load_data()
        else:    
            self.label_5.setText("Please Select the record.")
            self.label_5.show() 
    
    def L_edit_data(self):
        self.L_validations()
        if(self.go_ahead == 'Yes'):
            connection = sqlite3.connect("mdr.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE LIMITS_MST SET PARAM='"+str(self.lineEdit_12.text())+"',U_VAL='"+self.lineEdit_8.text()+"',L_VAL='"+self.lineEdit_9.text()+"', UNIT='"+self.lineEdit_7.text()+"',TARGET_VAL='"+self.lineEdit_10.text()+"',TOL_PER ='"+self.lineEdit_11.text()+"'   WHERE  LIMIT_ID ='"+str(self.limit_id)+"'")                    
            connection.commit();                    
            connection.close()
            self.label_5.setText("Record Saved Successfully.")       
            self.label_5.show()
            self.show_grid_limits()
    
    def L_delete_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.L_operation_flg="DELETE"
            self.L_load_data()
        else:    
            self.label_5.setText("Please Select the record.")
            self.label_5.show()        
     
      
    def L_delete_data(self):
        if(self.label_20.text() != ""):
            close = QMessageBox()
            close.setText("Confirm Deleteing Limit ID : "+str(self.limit_id))
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Yes:
                    connection = sqlite3.connect("mdr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM LIMITS_MST WHERE LIMIT_ID ='"+str(self.limit_id)+"'")                    
                    connection.commit();                    
                    connection.close()
                    
                    self.label_5.setText("Record Deleted Successfully.")                   
                    self.label_5.show()                    
                    self.reset_limits()
                    self.show_grid_limits()
            else:
                    self.label_5.setText("Canceled Delete..")                   
                    self.label_5.show()
            
    
    
    
    def L_validations(self):        
        self.go_ahead="No"
        if(self.lineEdit_12.text() == ""):
             self.label_5.setText("Parameter is Empty.")
             self.label_5.show()  
        elif(self.lineEdit_8.text()== ""):
             self.label_5.setText("U-Limit is Empty.")
             self.label_5.show()
        elif(self.lineEdit_9.text()== ""):
             self.label_5.setText("L-Limit is Empty.")
             self.label_5.show()
        elif(self.lineEdit_7.text() == ""):
             self.label_5.setText("Unit is Empty.")
             self.label_5.show()     
        elif(self.lineEdit_10.text()== ""):
             self.label_5.setText("Target is Empty.")
             self.label_5.show()
        elif(self.lineEdit_11.text()== ""):
             self.label_5.setText("Tolarance is Empty.")
             self.label_5.show()
        else:
             self.go_ahead="Yes"
        
    def validations(self):        
        self.go_ahead="No"
        if(self.lineEdit_2.text() == ""):
             self.label_5.setText("Method Name is Empty.")
             self.label_5.show()  
        elif(self.lineEdit_3.text()== ""):
             self.label_5.setText("Max. Torque is Empty.")
             self.label_5.show()
        elif(self.lineEdit_4.text()== ""):
             self.label_5.setText("Max. Temparature is Empty.")
             self.label_5.show()
        elif(self.lineEdit_5.text() == ""):
             self.label_5.setText("Max. Time is Empty.")
             self.label_5.show()     
        elif(self.lineEdit_6.text()== ""):
             self.label_5.setText("Arc is Empty.")
             self.label_5.show()
        elif(self.lineEdit.text()== ""):
             self.label_5.setText("Spec. No is Empty.")
             self.label_5.show()
        else:
             self.go_ahead="Yes"
    def show_grid_methods(self):        
        self.delete_all_records()
        
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        
        connection = sqlite3.connect("mdr.db")
         
        results=connection.execute("SELECT METHOD_ID,METHOD_NAME,SPEC_NUM,printf(\"%.2f\", SET_TORQUE),printf(\"%.2f\", SET_TEMP),printf(\"%d\", SET_TEST_TIME),printf(\"%.2f\", ARC) FROM METHODS_MST")
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(QtCore.Qt.AlignCenter) 
                self.tableWidget.setItem(row_number,column_number, item)                
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()
        # Check if the table has any rows before accessing the item
        if self.tableWidget.rowCount() > 0:
            self.method_id=str(self.tableWidget.item(0, 0).text())
            self.label_3.setText(str(self.tableWidget.item(0, 0).text()).zfill(3)) 
            self.lineEdit_2.setText(str(self.tableWidget.item(0, 1).text())) #Method Name lineEdit_2
            self.method_name=str(self.tableWidget.item(0, 1).text())
            self.lineEdit.setText(str(self.tableWidget.item(0, 2).text())) #Spec.Num lineEdit
            self.lineEdit_3.setText(str(self.tableWidget.item(0, 3).text())) #Max. Torq lineEdit_3
            self.lineEdit_4.setText(str(self.tableWidget.item(0, 4).text())) #Max. Temp lineEdit_4
            self.lineEdit_5.setText(str(self.tableWidget.item(0, 5).text())) #Time lineEdit_5
            self.lineEdit_6.setText(str(self.tableWidget.item(0, 6).text())) # Arc lineEdit_6  
        else:
        #      print("rowCount is 0")  
             self.reset_all()   
             
    def show_grid_limits(self):        
        self.delete_all_records2()
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        
        connection = sqlite3.connect("mdr.db")         
        results=connection.execute("SELECT LIMIT_ID,PARAM,printf(\"%.2f\", U_VAL),printf(\"%.2f\", L_VAL) ,printf(\"%.2f\", TARGET_VAL),UNIT,printf(\"%.2f\", TOL_PER)   FROM LIMITS_MST where METHOD_ID = '"+str(int(self.method_id))+"'")
        for row_number, row_data in enumerate(results):            
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(QtCore.Qt.AlignCenter) 
                self.tableWidget_2.setItem(row_number,column_number, item)                
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close() 
        if self.tableWidget_2.rowCount() > 0: 
            self.limit_id=str(self.tableWidget_2.item(0, 0).text())
            self.label_20.setText(str(self.tableWidget_2.item(0, 0).text()).zfill(3)) 
            self.lineEdit_12.setText(str(self.tableWidget_2.item(0, 1).text()))           
            self.lineEdit_8.setText(str(self.tableWidget_2.item(0, 2).text())) 
            self.lineEdit_9.setText(str(self.tableWidget_2.item(0, 3).text())) 
            self.lineEdit_7.setText(str(self.tableWidget_2.item(0, 5).text())) 
            self.lineEdit_11.setText(str(self.tableWidget_2.item(0, 6).text())) 
            self.lineEdit_10.setText(str(self.tableWidget_2.item(0, 4).text()))
            
            self.label_26.setText("( " +str(self.tableWidget_2.item(0, 5).text()+ " )"))
            self.label_27.setText("( " +str(self.tableWidget_2.item(0, 5).text()+ " )"))
            self.label_28.setText("( " +str(self.tableWidget_2.item(0, 5).text()+ " )"))   
        else:
        #      print("rowCount is 0")
             self.reset_limits()
        
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
    
    def delete_all_records2(self):
        i = self.tableWidget_2.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget_2.removeRow(i)
        
    
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mdr_04_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
