# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_29_stacks.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from fci_30_batch_pop import fci_30_Ui_MainWindow
from fci_31_issue_pop import fci_31_Ui_MainWindow
import sqlite3
import re
import datetime
import time

class fci_29_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1311, 701))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(1130, 10, 161, 31))
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
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(370, 650, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 650, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(430, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setGeometry(QtCore.QRect(430, 40, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(30, 40, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(810, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_7.setEnabled(False)
        self.groupBox_7.setGeometry(QtCore.QRect(810, 50, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_9.setGeometry(QtCore.QRect(30, 30, 181, 31))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(1160, 80, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 150, 1251, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 50, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_8.setGeometry(QtCore.QRect(30, 30, 221, 31))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(830, 640, 351, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 210, 241, 441))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)        
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(290, 160, 20, 521))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(320, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("")
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(330, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("")
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(330, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("")
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(330, 350, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("")
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(330, 400, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("")
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(310, 440, 151, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(490, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(20, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(490, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(490, 300, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.frame)
        self.label_49.setGeometry(QtCore.QRect(490, 350, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_49.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(490, 400, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(310, 500, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.label_51 = QtWidgets.QLabel(self.frame)
        self.label_51.setGeometry(QtCore.QRect(490, 450, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.frame)
        self.label_52.setGeometry(QtCore.QRect(490, 500, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_52.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_52.setObjectName("label_52")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(770, 210, 401, 231))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_31 = QtWidgets.QLabel(self.groupBox)
        self.label_31.setGeometry(QtCore.QRect(20, 50, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("")
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        self.label_34.setGeometry(QtCore.QRect(10, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("")
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 100, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(180, 170, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(530, 650, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(770, 450, 71, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(780, 500, 401, 91))
        self.textEdit.setObjectName("textEdit")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(310, 560, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("")
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.label_53 = QtWidgets.QLabel(self.frame)
        self.label_53.setGeometry(QtCore.QRect(490, 560, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_53.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_53.setObjectName("label_53")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
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
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00 "))
        self.pushButton_7.setText(_translate("MainWindow", "Batch Details"))
        self.pushButton_8.setText(_translate("MainWindow", "Return"))
        self.radioButton_3.setText(_translate("MainWindow", "Batch ID."))
        self.groupBox_5.setTitle(_translate("MainWindow", "."))
        self.comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox.setItemText(1, _translate("MainWindow", "R0002"))
        self.radioButton_4.setText(_translate("MainWindow", "Issue ID."))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "ISSUE_0002"))
        self.pushButton_9.setText(_translate("MainWindow", "Search "))
        self.radioButton_5.setText(_translate("MainWindow", "Materials"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "Rice (4001)"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "Paddy(300)"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "Wheat (5001)"))
        self.label_24.setText(_translate("MainWindow", "Message: Successfully Ssaved .sdfsdfsdf"))
        self.label_24.hide()
        self.label_25.setText(_translate("MainWindow", "Rec. No.:"))
        self.label_26.setText(_translate("MainWindow", "Slot.Id.:"))
        self.label_27.setText(_translate("MainWindow", "Material Name:"))
        self.label_28.setText(_translate("MainWindow", "Batch Id."))
        self.label_29.setText(_translate("MainWindow", "Issue.Id."))
        self.label_29.hide()
        self.label_30.setText(_translate("MainWindow", "Current Bags.Count:"))
        self.label_32.setText(_translate("MainWindow", "00045"))
        self.label_21.setText(_translate("MainWindow", "Slots List:"))
        self.label_47.setText(_translate("MainWindow", "SL0001"))
        self.label_48.setText(_translate("MainWindow", "Wheat(5001)"))
        self.label_49.setText(_translate("MainWindow", "R0001"))
        self.label_50.setText(_translate("MainWindow", "ISSUE_0001"))
        self.label_50.hide()
        self.label_33.setText(_translate("MainWindow", "Current Net.Wt(Ton):"))
        self.label_51.setText(_translate("MainWindow", "5400"))
        self.label_52.setText(_translate("MainWindow", "2345.997"))
        self.groupBox.setTitle(_translate("MainWindow", "Set Depo Loss"))
        self.label_31.setText(_translate("MainWindow", "Lost  Bags.Count:"))
        self.label_34.setText(_translate("MainWindow", "Lost  Net. Wt(Ton):"))
        self.pushButton_11.setText(_translate("MainWindow", "Save"))
        self.pushButton_10.setText(_translate("MainWindow", "Issue Details"))
        self.pushButton_10.setDisabled(True)
        self.label_35.setText(_translate("MainWindow", "Remark:"))
        self.label_36.setText(_translate("MainWindow", "Last Updated On :"))
        self.label_53.setText(_translate("MainWindow", "2020-09-20 12:33:44"))
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.pushButton_7.clicked.connect(self.open_new_window)
        self.pushButton_10.clicked.connect(self.open_new_window2)
        self.listWidget.doubleClicked.connect(self.selected_record)
        
        
        
        self.list_slots()
        
    
    
    
          
    def list_slots(self):        
        self.listWidget.clear()        
        self.listWidget.addItem("==== Slots =====")
        connection = sqlite3.connect("fci.db")
        if(self.radioButton_3.isChecked()):  #batch id           
            results=connection.execute("SELECT SLOT_ID||'-'||MATERAIL_NAME||'-'||REC_ID FROM SLOTS_BATCH_MST ")
        elif(self.radioButton_4.isChecked()): # issue id                 
            results=connection.execute("SELECT SLOT_ID||'-'||MATERAIL_NAME||'-'||REC_ID  FROM SLOTS_BATCH_MST")           
        elif(self.radioButton_5.isChecked()):  # #Material    
                       
            results=connection.execute("SELECT SLOT_ID||'-'||MATERAIL_NAME||'-'||REC_ID FROM SLOTS_BATCH_MST")
        else:
            results=connection.execute("SELECT SLOT_ID||'-'||MATERAIL_NAME||'-'||REC_ID  FROM SLOTS_BATCH_MST")
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()
    
    def selected_record(self):
         self.list_type=self.listWidget.item(0).text()
         if(self.listWidget.currentItem().text() != self.listWidget.item(0).text()):
            if(self.list_type=="==== Slots ====="):
                #print("current test is :"+str(self.listWidget.currentItem().text()))
                self.slot_id = str(self.listWidget.currentItem().text())               
                arr_item=str(self.slot_id).split("-")
                
                self.rec_id=str(arr_item[2])
                print("rec: "+str(self.rec_id))
                connection = sqlite3.connect("fci.db")               
                
                results=connection.execute("SELECT SLOT_ID,BATCH_ID,MATERAIL_NAME,LOADED_BAGS_CNT,LOADED_NET_WT,IFNULL(DL_BAGS,0),IFNULL(DL_NET_WT,0),IFNULL(UPDATED_ON,CREATED_ON) as LAST_DT  FROM SLOTS_BATCH_MST where REC_ID ='"+str(self.rec_id)+"'")
                for x in results:
                    self.label_32.setText(str(self.rec_id).zfill(4))
                    self.label_47.setText(str(x[0]))
                    self.label_49.setText(str(x[1]))
                    self.label_48.setText(str(x[2]))
                    self.label_51.setText(str(x[3]))
                    self.label_52.setText(str(x[4]))
                    self.lineEdit_6.setText(str(x[5]))
                    self.lineEdit_7.setText(str(x[6]))
                    self.label_53.setText(str(x[7]))
                connection.close()
                connection = sqlite3.connect("fci.db")
                with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET BATCH_ID_POP = '"+str(self.label_49.text())+"'" )                    
                connection.commit();                    
                connection.close()
                
                
            else:             
                print("Invalid !!")
        
    
    
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_30_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_31_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_29_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())