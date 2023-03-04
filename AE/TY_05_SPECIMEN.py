

from specimen_bakup import specimen_bkp_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import QTableWidgetItem
import sqlite3
import datetime
import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class TY_05_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1291, 709))
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color: rgb(215, 255, 252);")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 30, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 85, 127);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(1100, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 610, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 610, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 611, 551))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(13, item)
        
        
        
        
        
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 6, item)
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(510, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(690, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        
        self.label_22.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(690, 340, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(690, 400, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(1150, 340, 101, 31))
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)
        self.lineEdit.setValidator(input_validator)
        font = QtGui.QFont()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)        
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
        self.lineEdit_3.setValidator(input_validator)        
        self.lineEdit_3.setGeometry(QtCore.QRect(820, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(950, 610, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(1070, 610, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        
        
        self.pushButton_5_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5_1.setGeometry(QtCore.QRect(1070, 45, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5_1.setFont(font)
        self.pushButton_5_1.setObjectName("pushButton_5_1")
        
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(1120, 105, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(1020, 340, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(1120, 165, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(1030, 105, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(810, 220, 131, 31))
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_4)
        self.lineEdit_4.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(985, 210, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setGeometry(QtCore.QRect(1120, 220, 61, 31))
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_10)
        self.lineEdit_10.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_38 = QtWidgets.QLabel(self.frame)
        self.label_38.setGeometry(QtCore.QRect(1000, 460, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_38.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_11)
        self.lineEdit_11.setValidator(input_validator)
        self.lineEdit_11.setGeometry(QtCore.QRect(1150, 460, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(1180, 610, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_12.setGeometry(QtCore.QRect(810, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(820, 340, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(1010, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_6)
        self.lineEdit_6.setValidator(input_validator)
        self.lineEdit_6.setGeometry(QtCore.QRect(1150, 400, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(690, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_8)
        self.lineEdit_8.setValidator(input_validator)
        self.lineEdit_8.setGeometry(QtCore.QRect(820, 460, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(690, 520, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_13)
        self.lineEdit_13.setValidator(input_validator)
        self.lineEdit_13.setGeometry(QtCore.QRect(820, 520, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(1010, 520, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_14)
        self.lineEdit_14.setValidator(input_validator)
        self.lineEdit_14.setGeometry(QtCore.QRect(1150, 520, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(990, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(690, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        
        self.label_35_1 = QtWidgets.QLabel(self.frame)
        self.label_35_1.setGeometry(QtCore.QRect(690, 260, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_35_1.setFont(font)
        self.label_35_1.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_35_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35_1.setObjectName("label_35_1")
        
        
        self.lineEdit_4_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4_1.setGeometry(QtCore.QRect(810, 260, 131, 31))
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_4_1)
        self.lineEdit_4_1.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4_1.setFont(font)
        self.lineEdit_4_1.setObjectName("lineEdit_4_1")
        
        
        
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(680, 290, 601, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(690, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(810, 90, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.go_ahead="No"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Specimen Information"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00"))
        self.pushButton_2.setText(_translate("MainWindow", "Add"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.pushButton_5_1.setText("Backup/Recovery")
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Spec.ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Spec. Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Spec. Shape"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Party"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Guage.Length(Mm)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Specifications"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Test.Speed"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_21.setText(_translate("MainWindow", "Please select the record to Edit."))
        self.label_22.setText(_translate("MainWindow", "Spec.Name :"))
        self.label_24.setText(_translate("MainWindow", "Spec.Shape:"))
        self.label_25.setText(_translate("MainWindow", "Thickness(Mm):"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.lineEdit_3.setText(_translate("MainWindow", "1"))
        self.pushButton_4.setText(_translate("MainWindow", "Delete"))
        self.pushButton_5.setText(_translate("MainWindow", "Reset"))
        self.lineEdit_7.setText(_translate("MainWindow", "party"))
        self.label_31.setText(_translate("MainWindow", "Pre. Load:"))
        self.lineEdit_9.setText(_translate("MainWindow", "secifsns"))
        self.label_33.setText(_translate("MainWindow", "Party:"))
        self.lineEdit_4.setText(_translate("MainWindow", "0.2"))
        self.label_34.setText(_translate("MainWindow", "Guage(Mm):"))
        self.lineEdit_10.setText(_translate("MainWindow", "0.177"))
        self.label_38.setText(_translate("MainWindow", "Outer.Diameter :"))
        self.lineEdit_11.setText(_translate("MainWindow", "4"))
        self.pushButton_9.setText(_translate("MainWindow", "Return"))
        self.lineEdit_12.setText(_translate("MainWindow", "sec name"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Rectangle"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Pipe"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Cylindrical"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "DirectValue"))
        self.label_27.setText(_translate("MainWindow", "Width(Mm):"))
        self.lineEdit_6.setText(_translate("MainWindow", "2"))
        self.label_29.setText(_translate("MainWindow", "Inner.Diameter"))
        self.lineEdit_8.setText(_translate("MainWindow", "3"))
        self.label_30.setText(_translate("MainWindow", "Diameter :"))
        self.lineEdit_13.setText(_translate("MainWindow", "5"))
        self.label_32.setText(_translate("MainWindow", "CS.Area(Mm2):"))
        self.lineEdit_14.setText(_translate("MainWindow", "6"))
        self.label_26.setText(_translate("MainWindow", "Specification:"))
        self.label_35.setText(_translate("MainWindow", "Test Speed. :"))
        self.label_23.setText(_translate("MainWindow", "Spec.ID:"))
        self.label_2.setText(_translate("MainWindow", "0001"))
        self.lineEdit_4_1.setText("")
        self.label_35_1.setText("Rev.Test Speed:")
        self.pushButton_9.clicked.connect(MainWindow.close)
        
        self.comboBox_2.currentTextChanged.connect(self.specimen_diamentions)
        self.lineEdit_3.textChanged.connect(self.width_onchange)
        self.lineEdit_6.textChanged.connect(self.width_onchange)
        self.lineEdit_13.textChanged.connect(self.diameter_onchange)
        self.lineEdit_8.textChanged.connect(self.out_diameter_onchange)
        self.lineEdit_11.textChanged.connect(self.out_diameter_onchange)
        self.specimen_diamentions()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        self.c_select_all_data()
        self.c_rest_fun()
        self.tableWidget.doubleClicked.connect(self.c_fetch_data_from_tw)
        self.pushButton_2.clicked.connect(self.c_add_click) 
        self.pushButton_3.clicked.connect(self.c_edit_click)       
        self.pushButton_4.clicked.connect(self.c_delete_click)
        self.pushButton_5.clicked.connect(self.c_rest_fun)
        self.pushButton_5_1.clicked.connect(self.open_new_window)
       
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
       
    
    def specimen_diamentions(self):              
        if (self.comboBox_2.currentText() == 'Rectangle'):     
           self.shape="Rectangle"
           self.lineEdit_3.setEnabled(True)    #Thickness 
           self.lineEdit_6.setEnabled(True)    #width       
           self.lineEdit_8.setDisabled(True)   # inn diam
           self.lineEdit_11.setDisabled(True)  # out diameter
           self.lineEdit_13.setDisabled(True)   # diameter
           self.lineEdit_14.setDisabled(True)  #cs area
        elif  (self.comboBox_2.currentText() == 'Cylindrical'):     
           self.shape="Cylindrical"
           self.lineEdit_3.setDisabled(True)    #Thickness 
           self.lineEdit_6.setDisabled(True)    #width       
           self.lineEdit_8.setDisabled(True)   # inn diam
           self.lineEdit_11.setDisabled(True)  # out diameter
           self.lineEdit_13.setEnabled(True)   # diameter
           self.lineEdit_14.setDisabled(True)  #cs area
        elif  (self.comboBox_2.currentText() == 'Pipe'):     
           self.shape="Pipe"
           self.lineEdit_3.setDisabled(True)    #Thickness 
           self.lineEdit_6.setDisabled(True)    #width       
           self.lineEdit_8.setEnabled(True)   # inn diam
           self.lineEdit_11.setEnabled(True)  # out diameter
           self.lineEdit_13.setDisabled(True)   # diameter
           self.lineEdit_14.setDisabled(True)  #cs area      
        elif  (self.comboBox_2.currentText() == 'DirectValue'):     
           self.shape="Direct Value"
           self.lineEdit_3.setDisabled(True)    #Thickness 
           self.lineEdit_6.setDisabled(True)    #width       
           self.lineEdit_8.setDisabled(True)   # inn diam
           self.lineEdit_11.setDisabled(True)  # out diameter
           self.lineEdit_13.setDisabled(True)   # diameter
           self.lineEdit_14.setEnabled(True)  #cs area  
    
    def width_onchange(self):
        if(str(self.lineEdit_3.text()) != ""):
            if(str(self.lineEdit_6.text()) != ""):
                    self.thickness=str(self.lineEdit_3.text())
                    self.width=str(self.lineEdit_6.text())
                    try:
                        self.cs_area=(float(self.thickness)) * (float(self.width))                    
                        self.lineEdit_14.setText(str(round(self.cs_area,2)))
                    except ValueError:
                        self.lineEdit_14.setText("")
                        self.lineEdit_3.setText("")
                        self.lineEdit_6.setText("")
            else:
                    self.lineEdit_14.setText("")
                    self.lineEdit_6.setText("")
        else:
            self.lineEdit_14.setText("")
            self.lineEdit_3.setText("")
            
    def diameter_onchange(self):
        if(str(self.lineEdit_13.text()) != ""):
            self.diameter=str(self.lineEdit_13.text())
            try:
                self.cs_area=(float(self.diameter)*float(self.diameter)*3.14)/4 
                self.lineEdit_14.setText(str(round(self.cs_area,2)))
            except ValueError:
                self.lineEdit_14.setText("")
                self.lineEdit_13.setText("")
        else:
            self.lineEdit_14.setText("")
            self.lineEdit_13.setText("")
            
      
    def out_diameter_onchange(self):
        if(str(self.lineEdit_8.text()) != ""):
            if(str(self.lineEdit_11.text()) != ""):
                self.inn_diamter=str(self.lineEdit_8.text())
                self.out_diameter=str(self.lineEdit_11.text())
                try:
                    self.cs_area=((float(self.out_diameter)*float(self.out_diameter)*3.14)/4)-((float(self.inn_diamter)*float(self.inn_diamter)*3.14)/4) 
                    self.lineEdit_14.setText(str(round(self.cs_area,2)))
                except ValueError:
                    self.lineEdit_14.setText("")
                    self.lineEdit_11.setText("")
                    self.lineEdit_8.setText("")
                    
            else:
                    self.lineEdit_14.setText("")
                    self.lineEdit_11.setText("")
        else: 
            self.lineEdit_14.setText("")
            self.lineEdit_8.setText("")
    
    
    
    #Contractors            
    def c_fetch_data_from_tw(self):        
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.dr_id=str(self.tableWidget.item(row, 0).text())
            self.label_2.setText(str(self.tableWidget.item(row, 0).text()).zfill(3)) 
            self.lineEdit_12.setText(str(self.tableWidget.item(row, 1).text())) #spec. name
            self.comboBox_2.setCurrentText(str(self.tableWidget.item(row, 2).text())) #shape
            self.lineEdit_7.setText(str(self.tableWidget.item(row, 3).text())) #party
            self.lineEdit_9.setText(str(self.tableWidget.item(row, 4).text())) #specifications
            self.lineEdit_4.setText(str(self.tableWidget.item(row, 5).text())) # test speed
            self.lineEdit_10.setText(str(self.tableWidget.item(row, 6).text())) #guage length
            
            self.lineEdit.setText(str(self.tableWidget.item(row, 7).text())) #pre load
            self.lineEdit_3.setText(str(self.tableWidget.item(row, 8).text())) #thickness
            self.lineEdit_6.setText(str(self.tableWidget.item(row, 9).text())) #width
            
            self.lineEdit_8.setText(str(self.tableWidget.item(row, 10).text())) #inneer diamerte
            self.lineEdit_11.setText(str(self.tableWidget.item(row, 11).text())) # out diameter
            self.lineEdit_13.setText(str(self.tableWidget.item(row, 12).text())) # diameter
            self.lineEdit_14.setText(str(self.tableWidget.item(row, 13).text())) # cs area
            self.lineEdit_4_1.setText(str(self.tableWidget.item(row, 14).text())) # rev.Test Speed
           
           
            
            self.pushButton_2.setDisabled(True) #add
            self.pushButton_3.setEnabled(True)  #save
            self.pushButton_4.setEnabled(True) #delete           
            #self.pushButton_5.setEnabled(True) #reset
            
        else:    
            self.label_2.setText("Please Select the record.")
            self.label_2.show()
            
           
    def c_rest_fun(self):
        self.label_2.setText("")
        self.lineEdit_12.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_7.setText("")
       
        self.lineEdit_4.setText("")
        self.lineEdit_10.setText("")
            
        self.lineEdit.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_6.setText("")
            
        self.lineEdit_8.setText("")
        self.lineEdit_11.setText("")
        self.lineEdit_13.setText("")
        self.lineEdit_14.setText("")
        
        self.pushButton_2.setEnabled(True) #add
        self.pushButton_3.setDisabled(True)  #save
        self.pushButton_4.setDisabled(True) #delete           
        self.pushButton_5.setEnabled(True) #reset
        
        self.label_21.hide()
        self.c_select_all_data()
        self.label_2.setText("01")
  
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'SPECIMEN_MST'")       
        for x in results:           
                 self.label_2.setText(str(x[0]).zfill(3))            
        connection.close()         
            
   
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
         
    def c_add_click(self):
        self.operation_flg="ADD"       
        self.c_load_data()
        
    def c_add_data(self):
        self.validations()
        if(self.label_2.text() != ""):            
            if(self.go_ahead=="Yes"):
                connection = sqlite3.connect("tyr.db")
                with connection:        
                        cursor = connection.cursor()
                        cursor.execute("INSERT INTO SPECIMEN_MST(SPECIMEN_NAME,SPECIMEN_SPECS,SHAPE,PARTY_NAME,MOTOR_SPEED,GUAGE_LENGTH_MM ,PRE_LOAD ,THICKNESS, WIDTH , IN_DIAMETER_MM ,OUTER_DIAMETER_MM, DIAMETER ,C_A_AREA,REV_MOTOR_SPEED) VALUES('"+self.lineEdit_12.text()+"','"+self.lineEdit_9.text()+"','"+self.comboBox_2.currentText()+"','"+self.lineEdit_7.text()+"','"+self.lineEdit_4.text()+"','"+self.lineEdit_10.text()+"','"+self.lineEdit.text()+"','"+self.lineEdit_3.text()+"','"+self.lineEdit_6.text()+"','"+self.lineEdit_8.text()+"','"+self.lineEdit_11.text()+"','"+self.lineEdit_13.text()+"','"+self.lineEdit_14.text()+"','"+self.lineEdit_4_1.text()+"')")                    
                connection.commit();                    
                connection.close()  
          
                self.label_21.setText("Record Added Successfully.")           
                self.label_21.show()
        else :
            self.label_21.setText("Id is Empty.")
            self.label_21.show()
            
        self.c_select_all_data()
    
    def c_edit_click(self):        
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="EDIT"
            self.c_load_data()
        else:    
            self.label_21.setText("Please Select the record.")
            self.label_21.show() 
    
    def c_edit_data(self):
        self.validations()
        if(self.label_2.text() != "" and self.go_ahead == 'Yes'):
            connection = sqlite3.connect("tyr.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE SPECIMEN_MST SET SPECIMEN_NAME='"+str(self.lineEdit_12.text())+"',SPECIMEN_SPECS='"+self.lineEdit_9.text()+"',SHAPE='"+self.comboBox_2.currentText()+"', PARTY_NAME='"+self.lineEdit_7.text()+"',MOTOR_SPEED='"+self.lineEdit_4.text()+"',GUAGE_LENGTH_MM ='"+self.lineEdit_10.text()+"',PRE_LOAD='"+self.lineEdit.text()+"' ,THICKNESS='"+self.lineEdit_3.text()+"', WIDTH='"+self.lineEdit_6.text()+"' , IN_DIAMETER_MM='"+self.lineEdit_8.text()+"' ,OUTER_DIAMETER_MM='"+self.lineEdit_11.text()+"', DIAMETER='"+self.lineEdit_13.text()+"' ,C_A_AREA='"+self.lineEdit_14.text()+"',REV_MOTOR_SPEED='"+self.lineEdit_4_1.text()+"'   WHERE  SPECIMEN_ID ='"+str(self.dr_id)+"'")                    
            connection.commit();                    
            connection.close()
            self.label_21.setText("Record Saved Successfully.")       
            self.label_21.show()
            self.c_select_all_data()
    
    def validations(self):        
        self.go_ahead="No"
        if(self.lineEdit_12.text() == ""):
             self.label_21.setText("Spec. Name is Empty.")
             self.label_21.show()  
        elif(self.lineEdit_7.text()== ""):
             self.label_21.setText("Party is Empty.")
             self.label_21.show()
        elif(self.lineEdit_10.text()== ""):
             self.label_21.setText("Guage length is Empty.")
             self.label_21.show()
        elif(float(self.lineEdit_10.text()) <= 0):
             self.label_21.setText("Guage length Should not Zero.")
             self.label_21.show()
        elif(self.lineEdit_4.text() == ""):
             self.label_21.setText("Test Speed Should not null.")
             self.label_21.show() 
        elif(float(self.lineEdit_4.text()) <= 0):
             self.label_21.setText("Test Speed Should not Zero.")
             self.label_21.show()
        elif(self.lineEdit_4_1.text() == ""):
             self.label_21.setText("Rev.Test Speed Should not null.")
             self.label_21.show() 
        elif(float(self.lineEdit_4_1.text()) <= 0):
             self.label_21.setText("Rev.Test Speed Should not Zero.")
             self.label_21.show() 
        elif(self.lineEdit_14.text()== ""):
             self.label_21.setText("CS.Area is Empty.")
             self.label_21.show()  
        elif(float(self.lineEdit_14.text()) <= 0):
             self.label_21.setText("CS.Area should be greater than zero.")
             self.label_21.show()      
        else:
             self.go_ahead="Yes"
        
    def c_delete_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="DELETE"
            self.c_load_data()
        else:    
            self.label_21.setText("Please Select the record.")
            self.label_21.show()        
     
      
    def c_delete_data(self):
        if(self.label_2.text() != ""):
            close = QMessageBox()
            close.setText("Confirm Deleteing Specimen ID : "+str(self.dr_id))
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM SPECIMEN_MST WHERE SPECIMEN_ID ='"+str(self.dr_id)+"'")                    
                    connection.commit();                    
                    connection.close()
                    
                    self.label_21.setText("Record Deleted Successfully.")
                   
                    self.label_21.show()
                    
                    self.c_select_all_data()
            else:
                    self.label_21.setText("Canceled Delete..")
                   
                    self.label_21.show()
            
         
    def c_select_all_data(self):     
        self.c_delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(15)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)      
        self.tableWidget.setHorizontalHeaderLabels(['Spec.Id.','Spec.Name', 'Shape',' Party Name ','Specifications','Test Speed',' Guage(Mm)  ','Pre Load','Thickness','Width','Inner Diameter','Outer Diameter','Diameter ','CS Area','Rev.Test Speed'] )       
           
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select SPECIMEN_ID ,SPECIMEN_NAME ,SHAPE,PARTY_NAME ,SPECIMEN_SPECS,MOTOR_SPEED,GUAGE_LENGTH_MM ,PRE_LOAD ,THICKNESS, WIDTH , IN_DIAMETER_MM ,OUTER_DIAMETER_MM, DIAMETER ,C_A_AREA,REV_MOTOR_SPEED  FROM SPECIMEN_MST")                        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))                
        connection.close()   
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
    
    def c_delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)           
  
    def open_new_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=specimen_bkp_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_05_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
