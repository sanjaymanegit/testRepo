# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_37_update_record.ui'
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

class wt_37_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 766)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1311, 701))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 50, 171, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 40, 131, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        #self.lineEdit_2.setText("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1110, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(380, 640, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 50, 381, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 30, 151, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        #self.lineEdit_4.setText("lineEdit_4")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(20, 140, 1271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 170, 341, 511))
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
        self.groupBox_4.setGeometry(QtCore.QRect(370, 170, 411, 421))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
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
        self.label_25.setGeometry(QtCore.QRect(120, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_4)
        self.label_26.setGeometry(QtCore.QRect(10, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label_28.setGeometry(QtCore.QRect(10, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_31 = QtWidgets.QLabel(self.groupBox_4)
        self.label_31.setGeometry(QtCore.QRect(10, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_35 = QtWidgets.QLabel(self.groupBox_4)
        self.label_35.setGeometry(QtCore.QRect(10, 200, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 70, 151, 31))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText("lineEdit_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(120, 120, 261, 31))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setText("lineEdit_7")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_6.setEnabled(True)
        self.radioButton_6.setGeometry(QtCore.QRect(130, 160, 51, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setChecked(False)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_7.setEnabled(True)
        self.radioButton_7.setGeometry(QtCore.QRect(200, 160, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setChecked(True)
        self.radioButton_7.setObjectName("radioButton_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 270, 151, 31))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setText("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(120, 210, 261, 31))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setText("lineEdit_9")
        
        self.label_32 = QtWidgets.QLabel(self.groupBox_4)
        self.label_32.setGeometry(QtCore.QRect(10, 330, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 330, 261, 31))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setText("lineEdit_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(980, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(510, 640, 91, 41))
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
        self.comboBox.addItem("")
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
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_6.setGeometry(QtCore.QRect(800, 170, 491, 301))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        self.label_17.setGeometry(QtCore.QRect(10, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_40 = QtWidgets.QLabel(self.groupBox_6)
        self.label_40.setGeometry(QtCore.QRect(10, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_14.setGeometry(QtCore.QRect(150, 40, 121, 31))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setText("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_15.setGeometry(QtCore.QRect(150, 100, 301, 31))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.setText("lineEdit_15")
        self.line = QtWidgets.QFrame(self.groupBox_6)
        self.line.setGeometry(QtCore.QRect(30, 140, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_16.setGeometry(QtCore.QRect(150, 230, 301, 31))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_16.setText("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_17.setGeometry(QtCore.QRect(150, 170, 121, 31))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_17.setText("lineEdit_17")
        self.label_41 = QtWidgets.QLabel(self.groupBox_6)
        self.label_41.setGeometry(QtCore.QRect(10, 230, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.label_18 = QtWidgets.QLabel(self.groupBox_6)
        self.label_18.setGeometry(QtCore.QRect(10, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 40, 151, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_3.setGeometry(QtCore.QRect(300, 170, 151, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(640, 640, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.driver=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Serial. No."))
        self.pushButton_6.setText(_translate("MainWindow", "Retrun"))
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_8.setText(_translate("MainWindow", "Save"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Vehical No."))
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
        self.label_13.setText(_translate("MainWindow", "Vehical No.:"))
        self.label_14.setText(_translate("MainWindow", "Serial No:"))
        self.label_25.setText(_translate("MainWindow", "00123"))
        self.label_26.setText(_translate("MainWindow", "Party Name:"))
        self.label_28.setText(_translate("MainWindow", "Driver (IN/OUT) :"))
        self.label_31.setText(_translate("MainWindow", "Charges (Rs) :"))
        self.label_35.setText(_translate("MainWindow", "Container No."))
        self.radioButton_6.setText(_translate("MainWindow", " IN"))
        self.radioButton_7.setText(_translate("MainWindow", " OUT"))
        self.label_32.setText(_translate("MainWindow", "Remark :"))
        self.pushButton_9.setText(_translate("MainWindow", "Search"))
        self.pushButton_12.setText(_translate("MainWindow", "Delete"))
        self.label_33.setText(_translate("MainWindow", "31 Jan 2020 12:13:14"))
        self.label_37.setText(_translate("MainWindow", " Please use last 4 digit of vehical number in case no record found."))
        self.groupBox_8.setTitle(_translate("MainWindow", "Party Name"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Party 1"))
        self.radioButton_3.setText(_translate("MainWindow", "Search by serial Number"))
        self.radioButton_4.setText(_translate("MainWindow", "Search by Vehical Number"))
        self.radioButton_5.setText(_translate("MainWindow", "Search by Party Name"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Weight Details"))
        self.label_17.setText(_translate("MainWindow", "First Wt(Kg).:"))
        self.label_40.setText(_translate("MainWindow", "First Wt. Date:"))
        self.label_41.setText(_translate("MainWindow", "Second Wt. Date:"))
        self.label_18.setText(_translate("MainWindow", "Second. Wt(Kg).:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "GROSS"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "TARE"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "None"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "GROSS"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "TARE"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "None"))
        self.pushButton_13.setText(_translate("MainWindow", "Print"))
        self.lineEdit_15.setDisabled(True)
        self.lineEdit_16.setDisabled(True)
        self.comboBox_2.setCurrentText("GROSS")
        self.comboBox_3.setCurrentText("TARE")
        self.radioButton_3.clicked.connect(self.serial_no_onlick)
        self.radioButton_4.clicked.connect(self.vehical_onlick)
        self.radioButton_5.clicked.connect(self.party_onlick)
        self.pushButton_9.clicked.connect(self.list_vehicles)
        self.pushButton_8.clicked.connect(self.update_record)
        self.pushButton_13.clicked.connect(self.print_recipt)
        self.pushButton_12.clicked.connect(self.delete_record)
        
        self.listWidget.doubleClicked.connect(self.selected_record)
        
        self.groupBox_4.hide()
        self.groupBox_6.hide()
        
        self.load_data()
        self.list_vehicles()
        
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
            
    def list_vehicles(self):        
        self.listWidget.clear()        
        self.listWidget.addItem("==== Weighing List =====")
        connection = sqlite3.connect("wt.db")
        if(self.radioButton_4.isChecked()):  #vehical No            
            if(self.lineEdit_4.text() != ""):
                  self.whr_sql=" and VEHICLE_NO like '%"+str(self.lineEdit_4.text())+"%' order by serial_id desc "
            else:    
                  self.whr_sql=" order by serial_id desc"
            results=connection.execute("SELECT VEHICLE_NO||' - ('||printf(\"%04d\", SERIAL_ID)||')' AS SERIAL_ID FROM WEIGHT_MST WHERE (ifnull(round((julianday(CURRENT_TIMESTAMP) - julianday(FIRST_WT_CRTEATED_ON) )),0) < 365)  "+str(self.whr_sql))
        elif(self.radioButton_5.isChecked()): # Party
            if(self.comboBox.currentText() != ""):
                  self.whr_sql=" and PARTY_NAME like '%"+str(self.comboBox.currentText())+"%'  order by serial_id desc"
            else:    
                  self.whr_sql=" order by serial_id desc"
            
            print("PArty :"+str(self.comboBox.currentText()))
            print(" wheresql :"+str(self.whr_sql))      
            results=connection.execute("SELECT VEHICLE_NO||' - ('||printf(\"%04d\", SERIAL_ID)||')' AS SERIAL_ID FROM WEIGHT_MST WHERE (ifnull(round((julianday(CURRENT_TIMESTAMP) - julianday(FIRST_WT_CRTEATED_ON) )),0) < 365) "+str(self.whr_sql))           
        elif(self.radioButton_3.isChecked()):  # Serial No
            if(self.lineEdit_2.text() != ""):
                  self.whr_sql=" and SERIAL_ID like '%"+str(self.lineEdit_2.text())+"%' order by serial_id desc "
            else:    
                  self.whr_sql=" order by serial_id desc"             
            results=connection.execute("SELECT VEHICLE_NO||' - ('||printf(\"%04d\", SERIAL_ID)||')'  AS SERIAL_ID FROM WEIGHT_MST WHERE (ifnull(round((julianday(CURRENT_TIMESTAMP) - julianday(FIRST_WT_CRTEATED_ON) )),0) < 365) "+str(self.whr_sql))
        else:
            results=connection.execute("SELECT VEHICLE_NO||' - ('||printf(\"%04d\", SERIAL_ID)||')'  AS SERIAL_ID FROM WEIGHT_MST WHERE (ifnull(round((julianday(CURRENT_TIMESTAMP) - julianday(FIRST_WT_CRTEATED_ON) )),0) < 365) order by serial_id desc ")
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()
       
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
        
            
    def selected_record(self): 
        self.label_37.hide()
        self.groupBox_4.show()
        self.groupBox_6.show()
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
                                   "GROSS_WT_RATE,TARE_WT_RATE,FPRM_NO,REMARK,RECEIPT_CNT,MANNUAL_INS_FLG,DRIVER_IN_OUT,CANCLE_STATUS,OPERATOR_NAME,STATUS,FIRST_WEIGHT_MODE,FIRST_WEIGHT_VAL,FIRST_WT_CRTEATED_ON,SECOND_WT_MODE,SECOND_WT_VAL,SECOND_WT_CREATED_ON FROM WEIGHT_MST_VW where SERIAL_ID = '"+str(int(self.serial_id))+"'")
                for x in results:                    
                    print("ok")
                    self.label_25.setText(str(x[0])) #Serial No
                    self.lineEdit_5.setText(str(x[1])) #Vehical No
                    self.lineEdit_7.setText(str(x[2])) # Party Name
                    self.lineEdit_9.setText(str(x[14])) #Container No
                    self.lineEdit_8.setText(str(x[11])) #Charges
                    self.lineEdit_10.setText(str(x[15])) # Remark
                    self.lineEdit_14.setText(str(x[23])) #First Wt
                    self.lineEdit_17.setText(str(x[26])) #Second Wt
                    self.lineEdit_15.setText(str(x[24]))  #First Wt Date
                    self.lineEdit_16.setText(str(x[27])) # Second WT Date
                    self.driver=str(x[18])
                    if(str(str(x[18])) != "OUT"):
                            self.radioButton_6.setChecked(True)
                    else:
                            self.radioButton_7.setChecked(True)
                       
                    if(str(x[22]) == "GROSS"):
                             self.comboBox_2.setCurrentText("GROSS")
                    elif(str(x[22]) == "TARE"):
                             self.comboBox_2.setCurrentText("TARE")
                    else:
                             self.comboBox_2.setCurrentText("None")
                    
                    if(str(x[25]) == "GROSS"):
                             self.comboBox_3.setCurrentText("GROSS")
                    elif(str(x[25]) == "TARE"):
                             self.comboBox_3.setCurrentText("TARE")
                    else:
                             self.comboBox_3.setCurrentText("None")
                             
                          
                connection.close()
                connection = sqlite3.connect("wt.db")          
                with connection:        
                         cursor = connection.cursor()                    
                         cursor.execute("UPDATE PRINTER_DATA SET SERIAL_ID='"+str(int(self.label_25.text()))+"'") 
                connection.commit();
                connection.close()  
                
            else:             
                print("Invalid !!")
                
    def update_record(self):
            self.label_37.show()
            if(self.radioButton_6.isChecked()):
                   self.driver="IN"
            elif(self.radioButton_7.isChecked()):
                  self.driver="OUT"
            else:
                   self.driver=""
            #print("UPDATE WEIGHT_MST SET VEHICLE_NO="+str(self.lineEdit_5.text())+",PARTY_NAME="+str(self.lineEdit_7.text())+",FPRM_NO="+str(self.lineEdit_9.text())+",REMARK="+str(self.lineEdit_10.text())+",FIRST_WEIGHT_MODE="+self.comboBox_2.currentText()+",FIRST_WEIGHT_VAL="+str(self.lineEdit_14.text())+",SECOND_WT_MODE="+self.comboBox_3.currentText()+",SECOND_WT_VAL="+str(self.lineEdit_17.text())+"    WHERE SERIAL_ID='"+str(int(self.label_25.text()))+"'")       
            connection = sqlite3.connect("wt.db")          
            with connection:        
                         cursor = connection.cursor()                    
                         cursor.execute("UPDATE WEIGHT_MST SET VEHICLE_NO='"+str(self.lineEdit_5.text())+"',PARTY_NAME='"+str(self.lineEdit_7.text())+"',DRIVER_IN_OUT='"+str(self.driver)+"',FPRM_NO='"+str(self.lineEdit_9.text())+"',REMARK='"+str(self.lineEdit_10.text())+"',FIRST_WEIGHT_MODE='"+self.comboBox_2.currentText()+"',FIRST_WEIGHT_VAL='"+str(self.lineEdit_14.text())+"',SECOND_WT_MODE='"+self.comboBox_3.currentText()+"',SECOND_WT_VAL='"+str(self.lineEdit_17.text())+"',AMOUNT='"+str(self.lineEdit_8.text())+"',AMOUNT_2='0'    WHERE SERIAL_ID='"+str(int(self.label_25.text()))+"'") 
            connection.commit();
            connection.close()
            print("Record updated"+str(int(self.label_25.text())))
            self.label_37.setText("Saved Successfully.")
            
    def print_recipt(self):
            os.system("./job_print_recipt.sh")
    
    def delete_record(self):
           self.label_37.show()
           connection = sqlite3.connect("wt.db")          
           with connection:        
                         cursor = connection.cursor()                    
                         cursor.execute("DELETE FROM  WEIGHT_MST WHERE SERIAL_ID='"+str(int(self.label_25.text()))+"'") 
           connection.commit();
           connection.close()
           self.list_vehicles()
           self.label_37.setText("Deleted  Successfully.")
        
        
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_37_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
