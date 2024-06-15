

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import datetime, sqlite3, functools
from PyQt5.QtGui import QPixmap

class ConfigurTest(object):
    def setupUi(self, MainWindow):
        self.test_type_id = ""
        self.list_type = ""
        self.operation_flg = ""
        self.rec_count = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 1341, 751))
        self.frame.setStyleSheet("border:3px solid black;\n"
"background-color: rgb(204, 204, 204);\n"
"border-radius:60px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(490, 20, 331, 51))
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
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(960, 110, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_5.setStyleSheet("background:None; border:1px solid black; border-radius: 12px; color: rgb(0, 85, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(1140, 50, 131, 41))
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
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(1110, 20, 181, 21))
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
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 160, 1281, 16))
        self.label_6.setStyleSheet("background:None;\n"
"border-radius:8px;\n"
"background-color: rgb(91, 91, 91);\n"
"border:None;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(230, 100, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("#lineEdit {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px;}#lineEdit:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 0px;}#lineEdit:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px}")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
#         self.label_2 = QtWidgets.QLabel(self.frame)
#         self.label_2.setGeometry(QtCore.QRect(40, 30, 101, 101))
#         self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
#         self.label_2.setStyleSheet("border:1px solid;\n"
# "border-radius:opx;")
#         self.label_2.setText("")
#         self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(560, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton:hover {border: 1px solid green; color: rgb(0, 255, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));padding-bottom: 5px;padding-right: 5px;}#pushButton:pressed {background-color: rgb(255, 255, 255);padding-top: 5px;padding-left: 5px;}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("#pushButton_2 {color: rgb(255, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_2:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_2:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(255, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 180, 1321, 561))
        self.frame_2.setStyleSheet("border:2px solid;\n"
"border-radius:20px;\n"
"border-bottom-left-radius: 60px;\n"
"border-bottom-right-radius: 60px;\n"
"border:None;\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(280, 10, 16, 541))
        self.label_7.setStyleSheet("background:None;\n"
"border-radius:8px;\n"
"background-color: rgb(91, 91, 91);\n"
"border:None;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(1020, 10, 16, 541))
        self.label_8.setStyleSheet("background:None;\n"
"border-radius:8px;\n"
"background-color: rgb(91, 91, 91);\n"
"border:None;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 241, 491))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        # font.setBold(False)
        # font.setUnderline(False)
        # font.setWeight(25)
        self.listWidget.setFont(font)
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setStyleSheet("border:2px solid;\n"
"border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.listWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setObjectName("listWidget")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(320, 10, 681, 541))
        self.frame_3.setStyleSheet("border:2px solid;\n"
"border-radius:20px;\n"
"background-color: rgb(220, 220, 220);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 131, 41))
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 70, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("#lineEdit_2 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px;}#lineEdit_2:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 20px;}#lineEdit_2:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(10, 250, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 250, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("#lineEdit_3 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px;}#lineEdit_3:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 20px;}#lineEdit_3:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px}")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(10, 340, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 430, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("#pushButton_4 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_4:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_4:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 430, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("#pushButton_6 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_6:hover {border: 1px solid green; color: rgb(0, 255, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));padding-bottom: 5px;padding-right: 5px;}#pushButton_6:pressed {background-color: rgb(255, 255, 255);padding-top: 5px;padding-left: 5px;}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 430, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("#pushButton_7 {color: rgb(255, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_7:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_7:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 490, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("#pushButton_9 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_9:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_9:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 131, 41))
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
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(210, 20, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(255, 0, 0);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(460, 40, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 0);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(440, 70, 211, 311))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("#textEdit {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px;}#textEdit:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 20px;}#textEdit:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px}")
        self.textEdit.setObjectName("textEdit")
        self.label_20 = QtWidgets.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(10, 170, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(255, 0, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(160, 170, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.comboBox.setFont(font)
        #self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("#comboBox {background:None;color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px;}#comboBox:hover {border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 0px;}#comboBox:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 0px}")
        #self.comboBox.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 340, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("#lineEdit_4 {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px;}#lineEdit_4:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 20px;}#lineEdit_4:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px}")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8.setGeometry(QtCore.QRect(470, 430, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("#pushButton_8 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_8:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_8:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(1050, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 0, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_2)
        self.listWidget_2.setGeometry(QtCore.QRect(1060, 60, 241, 491))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.listWidget_2.setFont(font)
        self.listWidget_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget_2.setStyleSheet("border:2px solid;\n"
"border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.listWidget_2.setTextElideMode(QtCore.Qt.ElideRight)
        self.listWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_2.setObjectName("listWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Configure Test"))
        self.label_5.setText(_translate("MainWindow", "Error : Massages "))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.label_4.setText(_translate("MainWindow", "23 May 2024 15:05:09"))
        self.pushButton.setText(_translate("MainWindow", "Procced"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.label_3.setText(_translate("MainWindow", "Password :"))
        self.label_11.setText(_translate("MainWindow", "Test Name :"))
        self.label_12.setText(_translate("MainWindow", "Image File :"))
        self.label_13.setText(_translate("MainWindow", "File Path :"))
        self.pushButton_4.setText(_translate("MainWindow", "Add"))
        self.pushButton_6.setText(_translate("MainWindow", "Save"))
        self.pushButton_7.setText(_translate("MainWindow", "Delete"))
        self.pushButton_9.setText(_translate("MainWindow", "Set Default Test"))
        self.label_17.setText(_translate("MainWindow", "Serial. No. :"))
        self.label_18.setText(_translate("MainWindow", "1"))
        self.label_19.setText(_translate("MainWindow", "Test Description :"))
        self.label_20.setText(_translate("MainWindow", "Active :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Y"))
        self.comboBox.setItemText(1, _translate("MainWindow", "N"))
        self.pushButton_8.setText(_translate("MainWindow", "Refresh"))
        self.label_9.setText(_translate("MainWindow", "Test Type List (All) :"))
        self.label_10.setText(_translate("MainWindow", "Test Type List (Active) :"))
#         self.timer1=QtCore.QTimer()
#         self.timer1.setInterval(1000)  
#         self.timer1.start(1)      
#         self.timer1.timeout.connect(self.device_date)
        self.pushButton_4.hide()
        self.frame_2.hide()
        self.label_5.hide()
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.check_pass)
        self.pushButton_2.clicked.connect(self.reset_field)
        self.listWidget.clicked.connect(functools.partial(self.selected_record, "All"))
        self.listWidget_2.clicked.connect(functools.partial(self.selected_record, "Active"))
        self.pushButton_4.clicked.connect(self.s_add_click)
        self.pushButton_6.clicked.connect(self.s_edit_click) 
        self.pushButton_7.clicked.connect(self.s_delete_click)
        self.pushButton_8.clicked.connect(functools.partial(self.selected_record, "Refresh"))
        self.pushButton_9.clicked.connect(self.set_default_test)
        self.device_date()
         

    def set_default_test(self):
        connection = sqlite3.connect("tyr.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE TEST_TYPE_MST SET ACTIVE_Y_N = 'Y' WHERE TEST_TYPE_ID IN ('1', '2', '3', '4')")
        cursor.execute("UPDATE TEST_TYPE_MST SET ACTIVE_Y_N = 'N' WHERE TEST_TYPE_ID NOT IN ('1', '2', '3', '4')")
        connection.commit()              
        connection.close()
        self.load_data()
        
    def check_pass(self):
        password = str("singhisking")
        # password = str("1")
        if (password == str(self.lineEdit.text())):
            self.frame_2.show()
            self.load_data()
            self.label_5.hide()
        else:
            self.frame_2.hide()
            self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(255, 0, 0);")
        #     self.label_5.setStyleSheet("background:None; border:None; color:rgb(255, 0, 0);")
            self.label_5.setText("Incorrect Password")
            self.label_5.show()
            

    def load_data(self):
        self.listWidget.clear() 
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  TEST_TYPE_NAME ||'-'||TEST_TYPE_ID FROM TEST_TYPE_MST order by TEST_TYPE_ID ") 
        for x in results:
            self.listWidget.addItem(str(x[0]))
            self.rec_count=self.rec_count+1
        connection.close()
        if(int(self.rec_count) > 0):
            self.listWidget.setCurrentRow(0)
            self.selected_record("All")
        self.Active_test()    
    def Active_test(self):
        self.listWidget_2.clear()
        connection = sqlite3.connect("tyr.db")
        results =connection.execute("SELECT TEST_TYPE_NAME ||'-'||TEST_TYPE_ID, ACTIVE_Y_N FROM TEST_TYPE_MST") 
        for x in results:
            if (str(x[1]) == "Y"):
                self.listWidget_2.addItem(str(x[0]))
                self.rec_count=self.rec_count+1
        connection.close() 
         
    def s_edit_click(self):
        row = self.listWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="EDIT"
            self.s_load_data()
        else: 
            self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(0, 0, 255);")   
            self.label_5.setText("Please Select the record.")
            self.label_5.show() 

    def s_edit_data(self):
        if(self.label_18.text() != ""):
            self.validate_ip()
            if(str(self.go_ahead )== 'Yes'):
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("UPDATE TEST_TYPE_MST SET TEST_TYPE_NAME='"+self.lineEdit_2.text()+"',TEST_TYPE_DTLS='"+self.textEdit.toPlainText()+"',TEST_TYPE_IMG_FILE='"+self.lineEdit_3.text()+"',TEST_TYPE_PATH='"+self.lineEdit_4.text()+"',ACTIVE_Y_N='"+self.comboBox.currentText()+"' WHERE  TEST_TYPE_ID ='"+str(self.test_type_id)+"'")                    
                    connection.commit()                    
                    connection.close()
                    self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(0, 85, 0);")
                    self.label_5.setText("Record Saved Successfully.")                    
                    self.label_5.show()
                    self.Active_test()
        else:
             print("label_18 is empty.......")                        
    def s_add_click(self):
        self.operation_flg="ADD"       
        self.s_load_data()  
    def s_load_data(self):        
        if(self.operation_flg=="ADD"):
                #print("inside Add ")
                self.s_add_data()
        elif(self.operation_flg=="EDIT"):
                #print("inside edit ")
                self.s_edit_data()
        elif(self.operation_flg=="DELETE"):
                #print("inside delete ")
                self.s_delete_data()
        else:
                print("Invalid Operation.") 
    def s_add_data(self):
        if(self.label_18.text() != ""):
            self.validate_ip()
            if(str(self.go_ahead )== 'Yes'):
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("INSERT INTO TEST_TYPE_MST(TEST_TYPE_NAME,TEST_TYPE_DTLS,TEST_TYPE_IMG_FILE,TEST_TYPE_PATH,ACTIVE_Y_N) VALUES ('"+self.lineEdit_2.text()+"','"+self.textEdit.toPlainText()+"','"+self.lineEdit_3.text()+"','"+self.lineEdit_4.text()+"','"+self.comboBox.currentText()+"')")                    
                    connection.commit();                    
                    connection.close()
                    self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(0, 85, 0);")
                    self.label_5.setText("Record Added Successfully.")                   
                    self.label_5.show()
                    self.load_data()
        else :
            self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(255, 0, 0);")
            self.label_5.setText("Id is Empty.")
            self.label_5.show() 

    def s_delete_click(self):
        row = self.listWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="DELETE"
            self.s_load_data()
        else: 
            self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(0, 0, 255);")   
            self.label_5.setText("Please Select the record.")
            self.label_5.show()        
     
      
    def s_delete_data(self):        
        if(self.label_18.text() != ""):
            close = QMessageBox()
            close.setText("Confirm Deleteing Test TYPE ID : "+str(self.test_type_id))
            close.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Ok:
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM TEST_TYPE_MST WHERE TEST_TYPE_ID ='"+str(self.test_type_id)+"'")
                            #cursor.execute("DELETE FROM TEST_TYPE_MST where 1=1") 
                    connection.commit()                 
                    connection.close() 
                    self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(0, 85, 0);")           
                    self.label_5.setText("Record Deleted Successfully.")
                    self.label_5.show()            
                    self.load_data()
            else:
                    self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(255, 0, 0);")
                    self.label_5.setText("Canceled Delete..")                   
                    self.label_5.show()            

    def selected_record(self, list_name):
        self.test_type_id=""
        
        #self.pushButton_15.setText("")
        
        # self.list_type=self.listWidget_2.currentItem().text()
        connection = sqlite3.connect("tyr.db")
        if (list_name == "All"):
                self.list_type=self.listWidget.currentItem().text()
                results=connection.execute("SELECT  TEST_TYPE_NAME,TEST_TYPE_DTLS,TEST_TYPE_IMG_FILE,ACTIVE_Y_N,TEST_TYPE_ID FROM TEST_TYPE_MST WHERE  TEST_TYPE_NAME ||'-'||TEST_TYPE_ID = '"+str(self.list_type)+"'")
        elif (list_name == "Active"):
             self.list_type=self.listWidget_2.currentItem().text()
             results=connection.execute("SELECT  TEST_TYPE_NAME,TEST_TYPE_DTLS,TEST_TYPE_IMG_FILE,ACTIVE_Y_N,TEST_TYPE_ID FROM TEST_TYPE_MST WHERE  TEST_TYPE_NAME ||'-'||TEST_TYPE_ID = '"+str(self.list_type)+"'")
        else:
             self.label_5.hide()
             results=connection.execute("SELECT  TEST_TYPE_NAME,TEST_TYPE_DTLS,TEST_TYPE_IMG_FILE,ACTIVE_Y_N,TEST_TYPE_ID FROM TEST_TYPE_MST WHERE  TEST_TYPE_NAME ||'-'||TEST_TYPE_ID = '"+str(self.list_type)+"'")
                  
        for x in results:                    
                   self.lineEdit_2.setText(str(x[0])) #Test Name
                   self.textEdit.setText(str(x[1])) #TEST DETAILS
                   self.lineEdit_3.setText(str(x[2])) # image File Name
                   self.lineEdit_4.setText("images/") #image file path
                   self.label_18.setText(str(x[4]))
                   print("see yes or no : ", x[3])
                   if(str(x[3]) == 'Y'):
                       self.comboBox.setCurrentIndex(0) 
                #        self.listWidget_2.clear()
                #        self.listWidget_2.addItem(str(x[0]))
                       
                   else:
                       self.comboBox.setCurrentIndex(1)
                   #print("Active Flag : "+str(x[3]))
                   self.test_type_id=str(x[4])
                #    self.label_24.hide()
                   
                   self.pushButton_4.setDisabled(True) #add
                   self.pushButton_6.setEnabled(True)  #save
                   self.pushButton_7.setEnabled(True) #delete           
                   self.pushButton_8.setEnabled(True) #reset
                       
        connection.close()

    def reset_field(self):
        self.lineEdit.setText("")
        self.frame_2.hide()    
        self.label_5.hide()

    def device_date(self):
        self.label_4.setText(datetime.datetime.now().strftime("%d %B %Y %H:%M:%S"))
        
    def validate_ip(self):
        self.go_ahead = "No"
        if(self.lineEdit_2.text() == ""):
             self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(0, 0, 255);")
             self.label_5.setText("Test Name is Empty.")
             self.label_5.show()  
        elif(self.lineEdit_3.text()== ""):
             self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(0, 0, 255);")
             self.label_5.setText("Image File Name is Empty.")
             self.label_5.show() 
        elif(self.lineEdit_4.text()== ""):
             self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(0, 0, 255);")
             self.label_5.setText("Path is Empty.")
             self.label_5.show()
        elif(self.textEdit.toPlainText()== ""):
             self.label_5.setStyleSheet("background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color:rgb(0, 0, 255);")
             self.label_5.setText("Description is Empty.")
             self.label_5.show()        
        else:
             self.go_ahead="Yes"
             

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ConfigurTest()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())