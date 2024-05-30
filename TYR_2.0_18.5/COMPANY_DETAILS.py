
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap
import datetime, sqlite3, shutil, os


class CompanyDetails(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1164, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1121, 621))
        self.frame.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border: 2px solid black;\n"
"border-radius:50px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 40, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("#label{\n"
"\n"
"border:1px solid red;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:25px;\n"
"background:None;\n"
"background-color: rgb(206, 206, 206);}\n"
"#label:hover{\n"
"border:1px solid black;\n"
"color: rgb(255, 85, 0);\n"
"background-color: rgb(231, 231, 231);}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(820, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:None;\n"
"border:None;\n"
"\n"
"color: rgb(255, 85, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(500, 50, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 85, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 120, 1041, 16))
        self.label_6.setStyleSheet("background:None;\n"
"border-radius:8px;\n"
"background-color: rgb(91, 91, 91);\n"
"border:None;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 60, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("#pushButton_3 {background:None;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"    \n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
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
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(70, 160, 981, 241))
        self.frame_2.setStyleSheet("background:None;\n"
"background-color: rgb(243, 243, 243);\n"
"border: 1px solid;\n"
"border-radius:20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(190, 70, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("#textEdit {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px;}#textEdit:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 20px;}#textEdit:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px}")
        self.textEdit.setObjectName("textEdit")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(20, 200, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(190, 10, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        #self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);")
        self.lineEdit.setStyleSheet("#lineEdit {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px;}#lineEdit:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 20px;}#lineEdit:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px}")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(30, 70, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 190, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("#lineEdit_4 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px;}#lineEdit_4:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 20px;}#lineEdit_4:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px}")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 70, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_2:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_2:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(690, 40, 221, 161))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self.label_2.setStyleSheet("border:1px solid;\n"
"border-radius:0px;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/win 10/Desktop/qt designer/python_company_logo.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(910, 560, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("#pushButton_10 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_10:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_10:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(910, 480, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("#pushButton_7 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_7:hover { border: 1px solid green;color: rgb(0, 255, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_7:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(70, 430, 381, 171))
        self.frame_3.setStyleSheet("background:None;\n"
"background-color: rgb(243, 243, 243);\n"
"border: 1px solid;\n"
"border-radius:20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(20, 50, 171, 21))
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
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)        
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("#lineEdit_5 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px;}#lineEdit_5:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 0px;}#lineEdit_5:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px;}")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(20, 100, 161, 21))
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
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("#lineEdit_6 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px;}#lineEdit_6:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 0px;}#lineEdit_6:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px}")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(280, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(280, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(480, 490, 381, 111))
        self.frame_4.setStyleSheet("background:None;\n"
"background-color: rgb(243, 243, 243);\n"
"border: 1px solid;\n"
"border-radius:20px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("#lineEdit_3 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px;}#lineEdit_3:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 0px;}#lineEdit_3:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px}")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 121, 20))
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
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(270, 20, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 81, 20))
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("#lineEdit_2 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px;}#lineEdit_2:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 0px;}#lineEdit_2:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(270, 70, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(750, 430, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("border:None;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(480, 440, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(640, 430, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("border:None;")
        self.radioButton.setObjectName("radioButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Company Details"))
        self.label_4.setText(_translate("MainWindow", "23 May 2024 15:05:09"))
        self.label_5.setText(_translate("MainWindow", "Error : Massages "))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.label_10.setText(_translate("MainWindow", "Contact No :"))
        self.label_3.setText(_translate("MainWindow", "Company Name :"))
        self.label_11.setText(_translate("MainWindow", "Address :"))
        self.pushButton_2.setText(_translate("MainWindow", "Add\n"
"Logo"))
        self.pushButton_10.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_7.setText(_translate("MainWindow", "Save"))
        self.label_12.setText(_translate("MainWindow", "Auto. Reverse. Time :"))
        self.label_13.setText(_translate("MainWindow", "Breaking Sence :"))
        self.label_14.setText(_translate("MainWindow", "(Sec.)"))
        self.label_15.setText(_translate("MainWindow", "(Kg.)"))
        self.label_8.setText(_translate("MainWindow", "Dispalcement :"))
        self.label_17.setText(_translate("MainWindow", "(X-Axis)"))
        self.label_7.setText(_translate("MainWindow", "Load :"))
        self.label_16.setText(_translate("MainWindow", "(Y-Axis)"))
        self.radioButton_2.setText(_translate("MainWindow", "Auto Scale"))
        self.label_9.setText(_translate("MainWindow", "Graph Ploting :"))
        self.radioButton.setText(_translate("MainWindow", "Manual"))
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)  
        self.timer1.start(1)      
        self.timer1.timeout.connect(self.device_date)
        self.label_5.hide()
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.browse_image)
        self.load_data()
        self.pushButton_7.clicked.connect(self.save_data)
        self.pushButton_10.clicked.connect(self.load_data)
        self.radioButton_2.clicked.connect(self.graphScale)
        self.radioButton.clicked.connect(self.graphScale)

    def load_data(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT COMPANY_NAME,ADDRESS1,PHONE_NO,AUTO_REV_TIME_OFF,MOTOR_TEST_SPEED,MOTOR_MAX_SPEED,BREAKING_SENCE,GRAPH_SCALE_CELL_1,GRAPH_SCALE_CELL_2,GRAPH_SCALE_TYPE,PHONE_NO,NEW_DATE,GRAPH_SCALE_TYPE  FROM SETTING_MST")
        rows=results.fetchall()  
        self.lineEdit.setText(rows[0][0]) #COMPANY_NAME
        self.textEdit.setText(str(rows[0][1])) #ADDRESS1
        self.lineEdit_4.setText(str(rows[0][2])) #PHONE_NO
        self.lineEdit_5.setText(str(rows[0][3])) #AUTO_REV_TIME_OFF
        self.lineEdit_6.setText(str(rows[0][6])) #BREAKING_SENCE
        self.lineEdit_2.setText(str(rows[0][7])) #GRAPH_SCALE_CELL_1
        self.lineEdit_3.setText(str(rows[0][8])) #GRAPH_SCALE_CELL_2
        if(rows[0][12]== 'AUTO'):
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            self.lineEdit_2.setDisabled(True)
            self.lineEdit_3.setDisabled(True)
            
        else:    
            self.radioButton.setChecked(True)
            self.radioButton_2.setChecked(False)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            
        connection.close()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT COM_LOGO FROM GLOBAL_VAR")              
        
        for x in results:
                pixmap = QPixmap(x[0]) 
        connection.commit()                    
        connection.close() 
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True) 
    def save_data(self):
        if(self.radioButton_2.isChecked()):
            self.graphscal_type="AUTO"
        else:    
            self.graphscal_type="MANNUAL"
        connection = sqlite3.connect("tyr.db")        
        with connection:        
            cursor = connection.cursor()                    
            cursor.execute("UPDATE SETTING_MST SET COMPANY_NAME = '"+self.lineEdit.text()+"',ADDRESS1='"+self.textEdit.toPlainText()+"',AUTO_REV_TIME_OFF='"+self.lineEdit_5.text()+"', BREAKING_SENCE='"+self.lineEdit_6.text()+"',GRAPH_SCALE_CELL_1='"+self.lineEdit_2.text()+"',GRAPH_SCALE_CELL_2='"+self.lineEdit_3.text()+"',GRAPH_SCALE_TYPE='"+str(self.graphscal_type)+"',PHONE_NO='"+self.lineEdit_4.text()+"'") 
        connection.commit()
        connection.close() 
        self.label_5.setText("Saved Successfully !")
        self.label_5.show()   
    def graphScale(self):
        if(self.radioButton_2.isChecked()):
            self.graphscal_type="AUTO"
            self.lineEdit_2.setDisabled(True)
            self.lineEdit_3.setDisabled(True)
        else:    
            self.graphscal_type="MANNUAL"
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
        
    def device_date(self):
        self.label_4.setText(datetime.datetime.now().strftime("%d %B %Y %H:%M:%S"))    
    def browse_image(self):
        # Open a file dialog to select an image file
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', './logo-images', 'Image Files (*.png *.jpg *.jpeg *.bmp)', options=options)
        
        if file_name:
        #     print("file name :",file_name)
            # Load and set the image to the label
            pixmap = QPixmap(file_name)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            self.label_5.setText("Image Uploaded Successfully....")
            self.label_5.show()
        #     os.makedirs("./logo-images", exist_ok=True)
        # #     try: 
            base_name = os.path.basename(file_name)
        #     print("base name :", base_name)
            destination_path = os.path.join("./logo-images", base_name)
        #     print("destination_path name :",destination_path)
        #         with open(file_name, "rb") as fsrc, open(destination_path, "wb") as fdst:

        #                 shutil.copyfileobj(fsrc, fdst)
        #     except shutil.SameFileError:
        #                 print("Source and destination are the same file.")
        #     except PermissionError:
        #                 print("Permission denied. Check write permissions.")
            
            connection = sqlite3.connect("tyr.db")
            with connection:        
                        cursor = connection.cursor()
                        cursor.execute("UPDATE GLOBAL_VAR SET COM_LOGO = '"+str(destination_path)+"' ")                    
            connection.commit()                   
            connection.close()        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CompanyDetails()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
