from AE_REPORTS_TENSILE_03 import AE_03_Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton


import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem
import datetime
import random
import serial,time
import array  as arr
import numpy as np


class AE_02_SP_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 769)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 10, 1321, 691))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(720, 50, 601, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(1150, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 620, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(570, 620, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_8.setStyleSheet("background-color: rgb(148, 255, 166);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(420, 500, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(710, 0, 20, 691))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(220, 10, 200, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 60, 651, 241))
        self.frame_2.setStyleSheet("background-color: rgb(255, 240, 220);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(150, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(330, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_11.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(460, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(20, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(150, 100, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(20, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 160, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(380, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setGeometry(QtCore.QRect(490, 160, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 310, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(30, 360, 351, 121))
        self.frame_3.setStyleSheet("background-color: rgb(255, 238, 244);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(10, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_4.setGeometry(QtCore.QRect(120, 40, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 490, 121, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(30, 550, 341, 101))
        self.frame_5.setStyleSheet("background-color: rgb(255, 238, 244);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(10, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_6.setGeometry(QtCore.QRect(120, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(420, 360, 261, 121))
        self.frame_6.setStyleSheet("background-color: rgb(255, 238, 244);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        self.label_20.setGeometry(QtCore.QRect(30, 40, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(350, 70, 351, 101))
        self.frame_7.setStyleSheet("background-color: rgb(255, 238, 244);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setLineWidth(2)
        self.frame_7.setObjectName("frame_7")
        self.label_21 = QtWidgets.QLabel(self.frame_7)
        self.label_21.setGeometry(QtCore.QRect(10, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame_7)
        self.comboBox_8.setGeometry(QtCore.QRect(110, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setObjectName("comboBox_8")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_17.setGeometry(QtCore.QRect(120, 40, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(470, 310, 181, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(700, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(1030, 10, 91, 41))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(410, 550, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_10.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(730, 70, 581, 611))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        
        
        
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(770, 230, 312, 183))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget_2.setGeometry(QtCore.QRect(770, 440, 312, 183))
        self.calendarWidget_2.setGridVisible(True)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.from_dt=""
        self.to_dt=""
        self.party_name=""
        self.specimen_name=""
        self.unit_type=""
                  
#         self.kg_to_lb=float(2.20462)
#         self.mm_to_inch=float(0.0393701)
#         self.kg_to_Newton=float(9.81)
#         self.kgCm2_toMPA=float(0.0980665)
        
        self.test_ids=[]
        self.length=""
        self.test_id=""
        self.test_id_type=""
        self.email_flg="N"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Search Report"))
        self.label_47.setText(_translate("MainWindow", "05 Aug 2020 14:23:00"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.pushButton_8.setText(_translate("MainWindow", "Search"))
        self.label_48.setText(_translate("MainWindow", " ")) #message ..................
        self.radioButton.setText(_translate("MainWindow", "By Date Range [Tensile Test] "))
        self.pushButton_9.setText(_translate("MainWindow", "From Date :"))
        self.pushButton_11.setText(_translate("MainWindow", "To Date.:"))
        self.label_14.setText(_translate("MainWindow", "Party Name:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MRF"))
        self.comboBox.setItemText(1, _translate("MainWindow", "NISHIGANDHA Polymer"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.label_15.setText(_translate("MainWindow", "Batch.Id:"))
        self.label_16.setText(_translate("MainWindow", "Job Name:"))
        self.radioButton_2.setText(_translate("MainWindow", "By Party Name "))
        self.label_17.setText(_translate("MainWindow", "Party Name:"))
        self.radioButton_3.setText(_translate("MainWindow", "By Batch Id."))
        self.label_19.setText(_translate("MainWindow", "Batch ID:"))
        self.label_20.setText(_translate("MainWindow", "Test ID:"))
        self.label_21.setText(_translate("MainWindow", "Party Name:"))
        self.radioButton_4.setText(_translate("MainWindow", "By Test ID / Serial No :"))
        self.label_11.setText(_translate("MainWindow", "Double Click on record to see detail report"))
        self.checkBox.setText(_translate("MainWindow", "Select All"))
        self.checkBox.hide()
        self.pushButton_10.setText(_translate("MainWindow", " Delete "))

        
        #### Default setting ######
        self.calendarWidget.hide()
        self.calendarWidget_2.hide()
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        
        self.frame_2.setEnabled(True)
        self.frame_3.setDisabled(True)
        self.frame_5.setDisabled(True)
        self.frame_6.setDisabled(True)
        
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_16.setReadOnly(True)
        self.pushButton_11.setDisabled(True)
        
        
        
        #self.pushButton_10.setDisabled(True)
        
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.radioButton.clicked.connect(self.date_range_radiobutt_on_click)
        self.radioButton_2.clicked.connect(self.party_radiobutt_on_click)
        self.radioButton_3.clicked.connect(self.batch_radiobutt_on_click)
        self.radioButton_4.clicked.connect(self.jobname_radiobutt_on_click)
       
        self.lineEdit_15.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.lineEdit_16.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        
        self.pushButton_9.clicked.connect(self.from_on_click1)
        self.pushButton_11.clicked.connect(self.to_on_click2)
        self.calendarWidget.clicked.connect(self.calendar1_on_click)
        self.calendarWidget_2.clicked.connect(self.calendar2_on_click)
        
        self.comboBox.currentTextChanged.connect(self.load_batchids_1)
        self.comboBox_2.currentTextChanged.connect(self.load_jobname_1)
        
        self.pushButton_8.clicked.connect(self.list_tests)
        
        self.tableWidget.doubleClicked.connect(self.open_doubleClick_report)
        self.pushButton_10.clicked.connect(self.delete_tests)
        
        
        
        
        self.load_party_names_1()
        self.load_party_names_2()
        
        self.load_batchids_2()
        
        self.list_tests()
        
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        
    def device_date(self):     
        self.label_47.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))  
        
     
    def date_range_radiobutt_on_click(self):
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        
        self.frame_2.setEnabled(True)
        self.frame_3.setDisabled(True)
        self.frame_5.setDisabled(True)
        self.frame_6.setDisabled(True)
    
    def party_radiobutt_on_click(self):
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(True)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        
        self.frame_2.setDisabled(True)
        self.frame_3.setEnabled(True)
        self.frame_5.setDisabled(True)
        self.frame_6.setDisabled(True)
        
    def batch_radiobutt_on_click(self):
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(True)
        self.radioButton_4.setChecked(False)
        
        self.frame_2.setDisabled(True)
        self.frame_3.setDisabled(True)
        self.frame_5.setEnabled(True)
        self.frame_6.setDisabled(True)

    def jobname_radiobutt_on_click(self):
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(True)
        
        self.frame_2.setDisabled(True)
        self.frame_3.setDisabled(True)
        self.frame_5.setDisabled(True)
        self.frame_6.setEnabled(True)
        
    def from_on_click1(self):
        self.calendarWidget.show()
    
    def to_on_click2(self):
        self.calendarWidget_2.show()
        
    def calendar1_on_click(self):
        temp_var = self.calendarWidget.selectedDate() 
        var_name = temp_var.toPyDate()        
        #self.from_dt=str(var_name)
        self.lineEdit_15.setText(str(self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)))
        self.calendarWidget.hide()
        self.pushButton_11.setEnabled(True)
        
    
    def calendar2_on_click(self):
        temp_var = self.calendarWidget_2.selectedDate() 
        var_name = temp_var.toPyDate()        
        #self.to_dt=str(var_name)
        self.lineEdit_16.setText(str(self.calendarWidget_2.selectedDate().toString(QtCore.Qt.ISODate)))
        self.calendarWidget_2.hide()
        self.load_party_names_1()
        
    def load_party_names_1(self):
        self.i=0
        self.comboBox.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT PARTY_NAME FROM TEST_MST WHERE TEST_TYPE='Tensile'") 
        for x in results:            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str(x[0]))           
            self.i=self.i+1
        connection.close()
    
    def load_party_names_2(self):
        self.i=0
        self.comboBox_4.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT PARTY_NAME FROM TEST_MST WHERE TEST_TYPE='Tensile'") 
        for x in results:            
            self.comboBox_4.addItem("")
            self.comboBox_4.setItemText(self.i,str(x[0]))           
            self.i=self.i+1
        connection.close()
        
    def load_batchids_1(self):
        self.j=0
        self.comboBox_2.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT BATCH_ID FROM TEST_MST WHERE TEST_TYPE='Tensile' and PARTY_NAME='"+str(self.comboBox.currentText())+"'")
        #print("SELECT DISTINCT BATCH_ID FROM TEST_MST WHERE TEST_TYPE='Tensile' and PARTY_NAME='"+str(self.comboBox.currentText())+"'") 
        
        for x in results:            
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(self.j,str(x[0]))           
            self.j=self.j+1
        connection.close()
        
    def load_batchids_2(self):
        self.j=0
        self.comboBox_6.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT BATCH_ID FROM TEST_MST WHERE TEST_TYPE='Tensile' and PARTY_NAME='"+str(self.comboBox.currentText())+"'")
          
        for x in results:            
            self.comboBox_6.addItem("")
            self.comboBox_6.setItemText(self.j,str(x[0]))           
            self.j=self.j+1
        connection.close()
        
    def load_jobname_1(self):
        self.k=0
        self.comboBox_3.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT JOB_NAME FROM TEST_MST WHERE TEST_TYPE='Tensile' and PARTY_NAME='"+str(self.comboBox.currentText())+"' AND BATCH_ID = '"+str(self.comboBox_2.currentText())+"'")         
        #print("SELECT DISTINCT JOB_NAME FROM TEST_MST WHERE TEST_TYPE='Tensile' and PARTY_NAME='"+str(self.comboBox.currentText())+"' AND BATCH_ID = '"+str(self.comboBox_2.currentText())+"'")         
        for x in results:            
            self.comboBox_3.addItem("")
            self.comboBox_3.setItemText(self.k,str(x[0]))         
            self.k=self.k+1
        connection.close()
        
    def list_tests(self):
        
        #self.pushButton_14_1.setEnabled(True)
        self.from_dt=self.lineEdit_15.text()
        self.to_dt=self.lineEdit_16.text()
        #self.party_name=str(self.comboBox_3.currentText())
        #self.specimen_name=str(self.comboBox_4.currentText())
        #self.unit_type=str(self.comboBox_5.currentText())
        
        print("frm:"+str(self.from_dt)+"   to:"+str(self.to_dt))
        self.specimen_shape=""
        
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
       
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 200)
        self.tableWidget.setColumnWidth(6, 200)
       
        
        self.tableWidget.setHorizontalHeaderLabels(['Test ID.','CreatedOn','Party Name','Spec.Counts','Batch ID.','Spec.Name','Comments'])
        
         
        connection = sqlite3.connect("tyr.db")
        if(self.radioButton.isChecked()):
                print("date Range -select")
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' and B.TEST_TYPE='Tensile' and  B.PARTY_NAME = '"+str(self.comboBox.currentText())+"' and B.BATCH_ID = '"+str(self.comboBox_2.currentText())+"' and B.JOB_NAME='"+str(self.comboBox_3.currentText())+"'")                        
        elif(self.radioButton_2.isChecked()):
                print("by party name -select")
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.TEST_TYPE='Tensile' and  B.PARTY_NAME = '"+str(self.comboBox.currentText())+"' ")                        
        elif(self.radioButton_3.isChecked()):
                print("by batch id -select")
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.TEST_TYPE='Tensile' and  B.BATCH_ID = '"+str(self.comboBox_6.currentText())+"' ")                        
        elif(self.radioButton_4.isChecked()):
                if(self.lineEdit_17.text() != ""):
                    print("by Test Id / Serial No -select")
                    results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.TEST_TYPE='Tensile' and  B.TEST_ID='"+str(self.lineEdit_17.text())+"' ")                        
                else:
                    results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.TEST_TYPE='Tensile'")                        
            
        else:
                print("by else part-select")
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' and B.TEST_TYPE='Tensile' and  B.PARTY_NAME = '"+str(self.comboBox.currentText())+"' and B.BATCH_ID = '"+str(self.comboBox_2.currentText())+"' and B.JOB_NAME='"+str(self.comboBox_3.currentText())+"'")                        
      
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if(int(column_number) == 0):
                    #print("data-column_number :"+str(column_number))
                    item = QtWidgets.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(QtCore.Qt.Unchecked)
                    item.setText(str(data))
                    self.tableWidget.setItem(row_number,column_number,item)
                    #self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                else:
                    self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                #self.lineEdit.setText("")
        connection.close()   
        self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.label_48.setText("")                   
        self.label_48.show()
        connection = sqlite3.connect("tyr.db")          
        with connection:        
                cursor = connection.cursor()
                #cursor.execute("UPDATE GLOBAL_VAR SET SR_FROM_DT='"+str(self.from_dt)+"', SR_TO_DT='"+str(self.to_dt)+"', SR_PARTY_NAME='"+str(self.party_name)+"',SR_SPECIMENT_NAME='"+str(self.specimen_name)+"'")
                cursor.execute("DELETE FROM TEST_IDS")
                if(self.radioButton.isChecked()):
                                  cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,B.TEST_TYPE  FROM TEST_MST B  where B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' and TEST_TYPE='Tensile' and  B.PARTY_NAME = '"+str(self.comboBox.currentText())+"' and B.BATCH_ID = '"+str(self.comboBox_2.currentText())+"' and B.JOB_NAME='"+str(self.comboBox_3.currentText())+"'") 
                elif(self.radioButton_2.isChecked()): # party Name
                                  cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,B.TEST_TYPE  FROM TEST_MST B  where TEST_TYPE='Tensile' and  B.PARTY_NAME = '"+str(self.comboBox.currentText())+"' ") 
                elif(self.radioButton_3.isChecked()): #batch id
                                  cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,B.TEST_TYPE  FROM TEST_MST B  where TEST_TYPE='Tensile' and  B.BATCH_ID = '"+str(self.comboBox_2.currentText())+"' ") 
                elif(self.radioButton_4.isChecked()): #test id
                             if(self.lineEdit_17.text() != ""):
                                  cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,B.TEST_TYPE  FROM TEST_MST B  where TEST_TYPE='Tensile' and  and B.TEST_ID='"+str(self.comboBox_3.currentText())+"'") 
                             else:
                                  cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,B.TEST_TYPE  FROM TEST_MST B  where TEST_TYPE='Tensile' and  and B.TEST_ID='"+str(self.comboBox_3.currentText())+"'") 
                       
                else:
                                  cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,B.TEST_TYPE  FROM TEST_MST B  where B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' and TEST_TYPE='Tensile' and  B.PARTY_NAME = '"+str(self.comboBox.currentText())+"' and B.BATCH_ID = '"+str(self.comboBox_2.currentText())+"' and B.JOB_NAME='"+str(self.comboBox_3.currentText())+"'") 
               
                    
        connection.commit();
        connection.close()
        
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1            
            self.tableWidget.removeRow(i)
    
    
    def open_doubleClick_report(self):
        row = self.tableWidget.currentRow()
        if(row != -1 ):
            self.test_id=(self.tableWidget.item(row, 0).text() )
            print(" test_id :"+str(self.test_id))        
        
            connection = sqlite3.connect("tyr.db")
            with connection:        
                  cursor = connection.cursor()                                        
                  cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID = '"+str(self.test_id)+"'")              
            connection.commit();
            connection.close() 
        
        self.window = QtWidgets.QMainWindow()
        self.ui=AE_03_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def delete_tests(self):
        close = QMessageBox()
        close.setText("Confirm Deleteing TEST ID.")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE from GRAPH_MST WHERE GRAPH_ID in (SELECT GRAPH_ID FROM  CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM TEST_IDS))") 
                            cursor.execute("DELETE FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM TEST_IDS)")  
                            cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM TEST_IDS)")
                            print(" Few Test Deleted.")
                           
                    connection.commit();                    
                    connection.close()                    
                    self.label_48.setText("Record Deleted Successfully.")                   
                    self.label_48.show()
                    
        
    
    def del_uncheked(self):
        i = self.tableWidget.rowCount()       
        while (i > 0):
            i=i-1
            item = self.tableWidget.item(i, 0)
            #print("test id  :"+str(item.text()))
            currentState = item.checkState()
            if(currentState == QtCore.Qt.Checked):
                    print("Checked test ID:"+str(item.text()))
                    connection = sqlite3.connect("tyr.db")          
                    with connection:        
                            cursor = connection.cursor()                            
                            cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,B.TEST_TYPE  FROM TEST_MST B WHERE B.TEST_ID='"+str(item.text())+"' AND B.TEST_ID NOT IN (SELECT TEST_ID FROM TEST_IDS)") 
                    connection.commit();
                    connection.close()                    
            else:
                    print("Un-Checked test ID:"+str(item.text()))
                    connection = sqlite3.connect("tyr.db")          
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM TEST_IDS WHERE TEST_ID = '"+str(item.text())+"'")                             
                    connection.commit();
                    connection.close()
       
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AE_02_SP_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
