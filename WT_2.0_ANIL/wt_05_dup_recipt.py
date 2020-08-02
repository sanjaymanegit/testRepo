# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_05_dup_recipt1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import re
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter,inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
from reportlab.pdfgen.canvas import Canvas
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class wt_05_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 766)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1311, 701))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.whr_sql=""
        self.serial_id=0
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 50, 171, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 30, 131, 31))        
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1110, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 630, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(280, 170, 571, 301))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(20, 200, 531, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 230, 521, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout.addWidget(self.label_23)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 50, 521, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 1, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 1, 3, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 50, 381, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 30, 151, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 30, 61, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setGeometry(QtCore.QRect(170, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(20, 140, 1271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 170, 241, 511))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(880, 170, 411, 301))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(130, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(10, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(130, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_4)
        self.label_26.setGeometry(QtCore.QRect(10, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        self.label_27.setGeometry(QtCore.QRect(130, 110, 241, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label_28.setGeometry(QtCore.QRect(10, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox_4)
        self.label_29.setGeometry(QtCore.QRect(130, 160, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_31 = QtWidgets.QLabel(self.groupBox_4)
        self.label_31.setGeometry(QtCore.QRect(10, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.groupBox_4)
        self.label_32.setGeometry(QtCore.QRect(130, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.label_35 = QtWidgets.QLabel(self.groupBox_4)
        self.label_35.setGeometry(QtCore.QRect(10, 250, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.groupBox_4)
        self.label_36.setGeometry(QtCore.QRect(130, 250, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setGeometry(QtCore.QRect(280, 490, 571, 111))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_5)
        reg_ex = QRegExp("[0-9]+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_5)
        self.lineEdit_5.setValidator(input_validator)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 40, 41, 41))
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setGeometry(QtCore.QRect(80, 40, 81, 31))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 40, 101, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(980, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_6.setGeometry(QtCore.QRect(880, 500, 411, 101))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_11.setGeometry(QtCore.QRect(140, 40, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_8.setGeometry(QtCore.QRect(20, 40, 91, 41))
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(450, 630, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(1110, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_7.setGeometry(QtCore.QRect(640, 610, 651, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_34 = QtWidgets.QLabel(self.groupBox_7)
        self.label_34.setGeometry(QtCore.QRect(80, 20, 521, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(920, 110, 371, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_8.setGeometry(QtCore.QRect(680, 50, 221, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 181, 31))
        self.comboBox.setObjectName("comboBox")        
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(360, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_5.setEnabled(True)
        self.radioButton_5.setGeometry(QtCore.QRect(680, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setObjectName("radioButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Serial. No."))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_8.setText(_translate("MainWindow", "View"))
        self.groupBox.setTitle(_translate("MainWindow", "Weight Details"))
        self.label_12.setText(_translate("MainWindow", "Net Weight (Kg) :"))
        self.label_17.setText(_translate("MainWindow", "          00"))
        self.label_22.setText(_translate("MainWindow", "Total (Rs):"))
        self.label_23.setText(_translate("MainWindow", "000.00"))
        self.label_10.setText(_translate("MainWindow", "Gross Weight (Kg) : "))
        self.label_15.setText(_translate("MainWindow", "        00"))
        self.label_18.setText(_translate("MainWindow", "Date(Gross)   :"))
        self.label_20.setText(_translate("MainWindow", "--"))
        self.label_11.setText(_translate("MainWindow", "Tare Weight (Kg) :"))
        self.label_16.setText(_translate("MainWindow", "        00"))
        self.label_19.setText(_translate("MainWindow", "Date(Tare)   :"))
        self.label_21.setText(_translate("MainWindow", "--"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Vehical No."))
        self.label_30.setText(_translate("MainWindow", "No.Days Before :"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("MainWindow", "Details."))
        self.label_24.setText(_translate("MainWindow", "--"))
        self.label_13.setText(_translate("MainWindow", "Vehical No.:"))
        self.label_14.setText(_translate("MainWindow", "Serial No:"))
        self.label_25.setText(_translate("MainWindow", "--"))
        self.label_26.setText(_translate("MainWindow", "Party Name:"))
        self.label_27.setText(_translate("MainWindow", "------"))
        self.label_28.setText(_translate("MainWindow", "Driver (IN/OUT) :"))
        self.label_29.setText(_translate("MainWindow", "--"))
        self.label_31.setText(_translate("MainWindow", "Weighing Method :"))
        self.label_32.setText(_translate("MainWindow", "--"))
        self.label_35.setText(_translate("MainWindow", "Operator Name :"))
        self.label_36.setText(_translate("MainWindow", "----"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Print Copies"))
        self.pushButton_7.setText(_translate("MainWindow", "Print"))
        self.lineEdit_5.setText(_translate("MainWindow", "1"))
        self.lineEdit_5.setMaxLength(1)
        self.radioButton.setText(_translate("MainWindow", "Pre-Print"))
        self.radioButton_2.setText(_translate("MainWindow", "Plain Paper"))
        self.radioButton_2.setDisabled(True)
        self.pushButton_9.setText(_translate("MainWindow", "Search"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Tare Weight(Kg)"))
        self.pushButton_11.setText(_translate("MainWindow", "Mannual Update Tare Weight"))
        self.lineEdit_8.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setText(_translate("MainWindow", "Cancle Serial No."))
        self.label_33.setText(_translate("MainWindow", "31 Jan 2020 12:13:14"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Remark :"))
        self.label_34.setText(_translate("MainWindow", "--"))
        self.label_37.setText(_translate("MainWindow", " Please use last 4 digit of vehical number in case no record."))
        self.groupBox_8.setTitle(_translate("MainWindow", "Party Name"))
        #self.comboBox.setItemText(0, _translate("MainWindow", "Party 1"))
        self.radioButton_3.setText(_translate("MainWindow", "Search by serial Number"))
        self.radioButton_4.setText(_translate("MainWindow", "Search by Vehical Number"))
        self.radioButton_5.setText(_translate("MainWindow", "Search by Party Name"))
        
        self.radioButton_3.clicked.connect(self.serial_no_onlick)
        self.radioButton_4.clicked.connect(self.vehical_onlick)
        self.radioButton_5.clicked.connect(self.party_onlick)
        self.pushButton_9.clicked.connect(self.list_vehicles)
        self.listWidget.doubleClicked.connect(self.selected_record)
        self.pushButton_7.clicked.connect(self.open_PPOP_window3)
        self.pushButton_8.clicked.connect(self.open_PPOP_window4)
        self.pushButton_12.clicked.connect(self.cancle_serial_no)
        self.pushButton_11.clicked.connect(self.mannual_update_tare)
        
        self.load_data()
        self.list_vehicles()
        '''
        self.lineEdit_2.setText("serial No")
        self.lineEdit_4.setText("vehical No")
        self.lineEdit_5.setText("print copies")
        self.lineEdit_6.setText("days")
        self.lineEdit_8.setText("tare wt")
        '''
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_33.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
        
    def load_data(self):
        self.radioButton_4.setChecked(True) #vehical No
        self.radioButton_3.setChecked(False) # Party 
        self.radioButton_5.setChecked(False) # Serial No 
        self.groupBox_8.setDisabled(True)  # Party Name
        self.groupBox_2.setDisabled(True)  # serial No
        self.groupBox_3.setEnabled(True)  #vehical No
        
        self.i=0
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT distinct PARTY_NAME FROM WEIGHT_MST WHERE PARTY_NAME not in ('','None')") 
        for x in results:            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str(x[0]))
            self.i=self.i+1
        connection.close()
        
        if(self.label_25.text() == "--"):
            self.pushButton_7.setDisabled(True)
            self.pushButton_8.setDisabled(True)
    
    def cancle_serial_no(self):
        if(self.label_25.text() != "--"):            
            connection = sqlite3.connect("wt.db")
            with connection:                            
                cursor = connection.cursor()
                cursor.execute("UPDATE WEIGHT_MST SET CANCLE_STATUS='Cancled',AMOUNT_2=0,AMOUNT=0 WHERE SERIAL_ID='"+str(self.label_25.text())+"'")
            connection.commit();
            connection.close()
            self.label_37.setText("Serial No: "+str(self.label_25.text())+" is cancled.")
            self.label_37.show()
        else:   
            self.label_37.setText("Please select the record.")
            self.label_37.show() 
            
    def mannual_update_tare(self):
        print("insider mannual tare "+str(self.label_25.text()))
        
        if(self.label_25.text() != "--"):            
            if(self.lineEdit_8.text() != "0"):
                        connection = sqlite3.connect("wt.db")
                        print("SELECT FIRST_WEIGHT_MODE WEIGHT_MST WHERE SERIAL_ID='"+str(int(self.label_25.text()))+"'")
                        results=connection.execute("SELECT FIRST_WEIGHT_MODE FROM WEIGHT_MST WHERE SERIAL_ID='"+str(int(self.label_25.text()))+"'") 
                        for x in results:            
                            self.firs_wt_mode=str(x[0])
                        connection.close()
                        print("self.firs_wt_mode :"+str(self.firs_wt_mode))
                        connection = sqlite3.connect("wt.db")
                        with connection:                
                            second_wt_dt=str(datetime.datetime.now().strftime("%Y-%m-%d"))
                            second_wt_time=str(datetime.datetime.now().strftime("%H:%M"))
                            cr_date_str_2=str(second_wt_dt+" "+str( second_wt_time)+":00")
                            #print("cr_date_str_2:"+str(cr_date_str_2))
                            cr_date_2= datetime.datetime.strptime(cr_date_str_2, '%Y-%m-%d %H:%M:%S')
                            #print("cr_date_str:"+str(cr_date_2))            
                            cursor = connection.cursor()
                            if(self.firs_wt_mode=='GROSS'):                             
                                  #print("UPDATE WEIGHT_MST SET SECOND_WT_MODE='TARE', SECOND_WT_VAL='"+str(self.lineEdit_8.text())+"',SECOND_WT_CREATED_ON='"+str(cr_date_2)+"'  WHERE SERIAL_ID='"+str(int(self.label_25.text()))+"'")
                                  cursor.execute("UPDATE WEIGHT_MST SET SECOND_WT_MODE='TARE', SECOND_WT_VAL='"+str(self.lineEdit_8.text())+"',SECOND_WT_CREATED_ON='"+str(cr_date_2)+"' ,status='SECOND'  WHERE SERIAL_ID='"+str(int(self.label_25.text()))+"'")
                            elif(self.firs_wt_mode=='TARE'):
                                  #print("UPDATE WEIGHT_MST SET  FIRST_WEIGHT_VAL='"+str(self.lineEdit_8.text())+"',FIRST_WT_CRTEATED_ON='"+str(cr_date_2)+"'  WHERE SERIAL_ID='"+str(int(self.label_25.text()))+"'")
                                  cursor.execute("UPDATE WEIGHT_MST SET  FIRST_WEIGHT_VAL='"+str(self.lineEdit_8.text())+"',FIRST_WT_CRTEATED_ON='"+str(cr_date_2)+"'  WHERE SERIAL_ID='"+str(int(self.label_25.text()))+"'")                                                                      
                            cursor.execute("UPDATE WEIGHT_MST SET NET_WEIGHT_VAL= (case WHEN FIRST_WEIGHT_VAL > SECOND_WT_VAL THEN  FIRST_WEIGHT_VAL-SECOND_WT_VAL WHEN FIRST_WEIGHT_VAL < SECOND_WT_VAL THEN  SECOND_WT_VAL-FIRST_WEIGHT_VAL ELSE NET_WEIGHT_VAL END)     WHERE SERIAL_ID='"+str(int(self.label_25.text()))+"'")
                        connection.commit();
                        connection.close()
                        self.selected_record()    
                        self.label_37.setText("Tare wt is updated for Serial No: "+str(self.label_25.text())+".")
                        self.label_37.show()
            else:            
                        self.label_37.setText("Tare wt should greate than 0.")
                        self.label_37.show()
        else:   
            self.label_37.setText("Please select the record.")
            self.label_37.show() 
        
                    
            
            
            
    def selected_record(self): 
        self.label_37.hide()
        
        self.list_type=self.listWidget.item(0).text()
        if(self.listWidget.currentItem().text() != self.listWidget.item(0).text()):
            if(self.list_type=="==== Weighing List ====="):
                #print("current test is :"+str(self.listWidget.currentItem().text()))
                self.re_str = str(self.listWidget.currentItem().text())                
                self.serial_id= re.search('\(([^)]+)', self.re_str).group(1)
                #print("SErial ID : "+str(int(self.serial_id)))
                connection = sqlite3.connect("wt.db")
                #print("SELECT SERIAL_ID_DISPLY,VEHICLE_NO,PARTY_NAME,SUPPLIER_NAME,TRANSPORT_NAME,MATERIAL_NAME,"+
                #                   "GROSS_WT_DATE ,GROSS_WT_VAL, TARE_WT_DATE , TARE_WT_VAL ,IFNULL(NET_WEIGHT_VAL,0),(IFNULL(GROSS_WT_RATE,0)+IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT,"+
                #                   "GROSS_WT_RATE,TARE_WT_RATE FROM WEIGHT_MST_VW where SERIAL_ID = '"+str(int(self.serial_id))+"'")
                
                results=connection.execute("SELECT SERIAL_ID_DISPLY,VEHICLE_NO,PARTY_NAME,SUPPLIER_NAME,TRANSPORT_NAME,MATERIAL_NAME,"+
                                   "GROSS_WT_DATE ,GROSS_WT_VAL, TARE_WT_DATE , TARE_WT_VAL ,IFNULL(NET_WEIGHT_VAL,0),(IFNULL(GROSS_WT_RATE,0)+IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT,"+
                                   "GROSS_WT_RATE,TARE_WT_RATE,FPRM_NO,REMARK,RECEIPT_CNT,MANNUAL_INS_FLG,DRIVER_IN_OUT,CANCLE_STATUS,OPERATOR_NAME,STATUS FROM WEIGHT_MST_VW where SERIAL_ID = '"+str(int(self.serial_id))+"'")
                for x in results:                          
                    self.label_17.setText("<font color=blue>"+str(x[10])+"</font>")  #Net Weight (Kg)
                    self.label_23.setText(str(x[11]))  #Total (Rs)
                    self.label_15.setText("<font color=blue>"+str(x[7])+"</font>")  #Gross Weight (Kg)
                    if(str(x[6]) != "None"):
                            self.label_20.setText("<font color=blue>"+str(x[6][0:10])+"</font>       Time: <font color=blue>"+ str(x[6][11:16]) +"</font> ")  #Rate (Gross):
                    else:
                            self.label_20.setText("<font color=blue> None </font>               Time: <font color=blue> None </font> ")  #Rate (Tare):
                    self.label_16.setText("<font color=blue>"+str(x[9])+"</font>")  #Tare Weight (Kg)
                    print("TARE DATE :"+str(x[8]))
                    if(str(x[8]) != "None"):
                            self.label_21.setText("<font color=blue>"+str(x[8][0:10])+"</font>       Time: <font color=blue>"+ str(x[8][11:16]) +"</font> ")  #Rate (Tare):
                    else:
                            self.label_21.setText("<font color=blue> None </font>               Time: <font color=blue> None </font> ")  #Rate (Tare):
                    self.label_25.setText(str(x[0])) #Serial No
                    self.label_24.setText(str(x[1])) # Vehicle No
                    self.label_27.setText(str(x[2])) # Party Name 
                    self.label_29.setText(str(x[18])) #  Driver IN OUT
                    self.label_36.setText(str(x[20])) #  Operator Name
                    self.label_32.setText(str(x[17])) #  Auto/mannual
                    self.label_34.setText(str(x[15])) #  Remark
                    
                    if(str(x[21]) =='SECOND'):
                         self.groupBox_6.setDisabled(True)
                    else:
                         self.groupBox_6.setEnabled(True)     
                    
                    self.strg="Gross Weight (Kg) :\n"
                    self.label_10.setText(str(self.strg))
                    self.label_11.setText("Tare Weight (Kg) :\n")
                connection.close()
                connection = sqlite3.connect("wt.db")          
                with connection:        
                         cursor = connection.cursor()                    
                         cursor.execute("UPDATE PRINTER_DATA SET SERIAL_ID='"+str(int(self.label_25.text()))+"'") 
                connection.commit();
                connection.close()  
                
            else:             
                print("Invalid !!")    
        if(self.label_25.text() != "--"):
            self.pushButton_7.setEnabled(True)
            self.pushButton_8.setEnabled(True)
            
    def vehical_onlick(self):        
        self.radioButton_4.setChecked(True) #vehical No
        self.radioButton_3.setChecked(False) # Party 
        self.radioButton_5.setChecked(False) # Serial No 
        self.groupBox_8.setDisabled(True)  # Party Name
        self.groupBox_2.setDisabled(True)  # serial No
        self.groupBox_3.setEnabled(True)  #vehical No
        
    def party_onlick(self):
        self.radioButton_4.setChecked(False) #vehical No
        self.radioButton_5.setChecked(True) # Party 
        self.radioButton_3.setChecked(False) # Serial No 
        self.groupBox_8.setEnabled(True)  # Party Name
        self.groupBox_2.setDisabled(True)  # serial No
        self.groupBox_3.setDisabled(True)  #vehical No
            
    def serial_no_onlick(self):
        self.radioButton_4.setChecked(False) #vehical No
        self.radioButton_5.setChecked(False) # Party 
        self.radioButton_3.setChecked(True) # Serial No 
        self.groupBox_8.setDisabled(True)  # Party Name
        self.groupBox_2.setEnabled(True)  # serial No
        self.groupBox_3.setDisabled(True)  #vehical No            
         
    def list_vehicles(self):        
        self.listWidget.clear()        
        self.listWidget.addItem("==== Weighing List =====")
        connection = sqlite3.connect("wt.db")
        if(self.radioButton_4.isChecked()):  #vehical No            
            if(self.lineEdit_4.text() != ""):
                  self.whr_sql=" and VEHICLE_NO like '%"+str(self.lineEdit_4.text())+"%' order by serial_id desc "
            else:    
                  self.whr_sql=" order by serial_id desc"
            results=connection.execute("SELECT VEHICLE_NO||' - ('||printf(\"%04d\", SERIAL_ID)||')'||' -'||PARTY_NAME AS SERIAL_ID FROM WEIGHT_MST WHERE (ifnull(round((julianday(CURRENT_TIMESTAMP) - julianday(FIRST_WT_CRTEATED_ON) )),0) < 365)  "+str(self.whr_sql))
        elif(self.radioButton_5.isChecked()): # Party
            if(self.comboBox.currentText() != ""):
                  self.whr_sql=" and PARTY_NAME like '%"+str(self.comboBox.currentText())+"%'  order by serial_id desc"
            else:    
                  self.whr_sql=" order by serial_id desc"
            results=connection.execute("SELECT VEHICLE_NO||' - ('||printf(\"%04d\", SERIAL_ID)||')'||' -'||PARTY_NAME AS SERIAL_ID FROM WEIGHT_MST WHERE (ifnull(round((julianday(CURRENT_TIMESTAMP) - julianday(FIRST_WT_CRTEATED_ON) )),0) < 365) "+str(self.whr_sql))           
        elif(self.radioButton_3.isChecked()):  # Serial No
            if(self.lineEdit_2.text() != ""):
                  self.whr_sql=" and SERIAL_ID like '%"+str(self.lineEdit_2.text())+"%' order by serial_id desc "
            else:    
                  self.whr_sql=" order by serial_id desc"             
            results=connection.execute("SELECT VEHICLE_NO||' - ('||printf(\"%04d\", SERIAL_ID)||')'||' -'||PARTY_NAME AS SERIAL_ID FROM WEIGHT_MST WHERE (ifnull(round((julianday(CURRENT_TIMESTAMP) - julianday(FIRST_WT_CRTEATED_ON) )),0) < 365) "+str(self.whr_sql))
        else:
            results=connection.execute("SELECT VEHICLE_NO||' - ('||printf(\"%04d\", SERIAL_ID)||')'||' -'||PARTY_NAME AS SERIAL_ID FROM WEIGHT_MST WHERE (ifnull(round((julianday(CURRENT_TIMESTAMP) - julianday(FIRST_WT_CRTEATED_ON) )),0) < 365) order by serial_id desc ")
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close() 

    def open_PPOP_window3(self):
        if(self.lineEdit_5.text() != ''):
            if(self.lineEdit_5.text() != ' '):                    
                 for x in range(int(self.lineEdit_5.text())):
                     print("printing:"+str(x))
                     os.system("./job_print_recipt.sh")
            else:
                 print("Space Issued in lineedit_5")
        else:
            print("empty copies")
    
    def open_PPOP_window4(self):
        self.create_pdf()
        os.system("xpdf ./reports/duplicateSlip.pdf")
    
    def create_pdf(self):
        self.first_wt=""
        self.first_wt_date=""
        self.first_wr_time=""
        self.second_wt=""
        self.second_wt_date=""
        self.second_wt_time=""
        self.first_wt_mode=""
        self.second_wt_mode=""
        self.address=""
        
        if(self.label_25.text()=="--"):
              self.serial_id=0
        self.serial_id=self.label_25.text()
        print("self.serial_id :"+str(self.serial_id))
        if (self.serial_id=="0"):
            connection = sqlite3.connect("wt.db")       
            results=connection.execute("SELECT MAX(SERIAL_ID) FROM WEIGHT_MST_VW")
            for x in results:
                 self.serial_id=str(x[0])
            
            connection.close()
        
        connection = sqlite3.connect("wt.db")          
        with connection:        
             cursor = connection.cursor()                    
             cursor.execute("UPDATE PRINTER_DATA SET SERIAL_ID='"+str(self.serial_id)+"'") 
        connection.commit();
        connection.close()   
        
        data= [['           Weight Type          ','          Date           ','      Time     ','        Weight(Kg)          ']]
        
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT SERIAL_ID,VEHICLE_NO,FIRST_WEIGHT_VAL,FIRST_WT_CRTEATED_ON,SECOND_WT_VAL,SECOND_WT_CREATED_ON,"+
                                           "NET_WEIGHT_VAL ,(AMOUNT+AMOUNT_2) as CHARGES,PARTY_NAME,SUPPLIER_NAME,FIRST_WEIGHT_MODE,SECOND_WT_MODE,MATERIAL_NAME FROM WEIGHT_MST WHERE SERIAL_ID in (SELECT SERIAL_ID from PRINTER_DATA)") 
      
               
        for x in results:
               self.first_wt=str(x[2])
               self.first_wt_date=str(x[3])
               self.first_wr_time=str(x[3])
               self.second_wt=str(x[4])
               self.second_wt_date=str(x[5])
               self.second_wt_time=str(x[5])
               self.first_wt_mode=str(x[10])
               self.second_wt_mode=str(x[11])
        connection.close()
        data.append([str(self.first_wt_mode)+" Weight",str(self.first_wt_date[0:10]),str(self.first_wt_date[11:16]),str(self.first_wt)])        
        data.append([str(self.second_wt_mode)+" Weight",str(self.second_wt_date[0:10]),str(self.second_wt_date[11:16]),str(self.second_wt)])
        
        
        
        c = Canvas("./reports/duplicateSlip.pdf")
        #c.setPageSize( landscape(letter) )
        #############################
        c.setFont('Helvetica', 12 )
        PAGE_HEIGHT = letter[1]
        PAGE_WIDTH = letter[0]
        
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT COMPANY_NAME,COMPANY_ADDR||'(Phone:'||CONTACT_NO||')'  FROM USER_RIGHT_SET")
        for x in results:
              c.drawString(170,810,str(str(x[0])))             
              self.address=str(str(x[1]))
        connection.close()
        
        c.setFont('Helvetica', 10 )
        c.drawString(120,790,str(self.address[0:76]))
        c.drawString(150,770,str(self.address[76:200]))
        
        c.line( 0.5*inch, PAGE_HEIGHT-( 0.45*inch ), PAGE_WIDTH-( 0.5*inch ), PAGE_HEIGHT-( 0.45*inch ) )
        ###################################################
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT SERIAL_ID_DISPLY,current_timestamp as dt,PARTY_NAME,SUPPLIER_NAME,MATERIAL_NAME,TRANSPORT_NAME,"+
                                           "GROSS_WT_DATE,TARE_WT_DATE,(IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOT_AMOUNT,GROSS_WT_VAL,TARE_WT_VAL,NET_WEIGHT_VAL,VEHICLE_NO,FPRM_NO,REMARK,MANNUAL_INS_FLG,OPERATOR_NAME,DRIVER_IN_OUT FROM WEIGHT_MST_VW WHERE SERIAL_ID ='"+str(self.serial_id)+"' ") 
        
        
        for x in results:
                c.setFont('Helvetica',10)
                c.drawString(50,740,"Serial ID: "+str(x[0]))
                #c.drawString(250,740,"Date : "+str(x[1]))
                c.drawString(250,740,"Vehical No : "+str(x[12]))       
                c.drawString(50,710,"Party Name: "+str(x[2]))                
                c.drawString(250,710,"Container No.: "+str(x[13]))
                
                c.drawString(50,680," Material Name : "+str(x[4]))
                c.drawString(250,680," Remark : "+str(x[14]))   
                
                c.drawString(50,650," Type : "+str(x[15]))
                c.drawString(250,650," Driver : "+str(x[17]))
                #c.drawString(250,680," "+str(x[4]))
                
               
                
                c.drawString(250,550,"Operator    : "+str(x[16]))
                c.drawString(250,530,"Net Wt(Kg)    : "+str(x[11]))
                c.drawString(250,510,"Total Amount(Rs): "+str(x[8]))
                c.line(0.5*inch,490,580,490)
        
        connection.close()
        
        ##############################################
        c.setFont('Helvetica',10)        
        f = Table(data)        
        f.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black), ('FONT', (0, 0), (-1, -1), "Helvetica", 10)]))
        width = 200
        height_1 = 400
        f.wrapOn(c, width, height_1)
        x = 40
        y = 580
        f.drawOn(c, x, y)        
        ############################################
        
        c.showPage()
        c.save()                    
    
        
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_05_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
