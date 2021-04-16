# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TY_04_SETTING.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
from pop_factory_reset import  factory_reset_Ui_MainWindow
from TY_08_TEST_CONF import TY_08_Ui_MainWindow

class TY_04_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 772)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1311, 709))
        self.frame.setStyleSheet("")
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.new_date=""
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 650, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 650, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(470, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(40, 100, 401, 241))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(130, 90, 181, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 180, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(550, 370, 711, 181))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(70, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        
        
        self.label_9_1 = QtWidgets.QLabel(self.frame)
        self.label_9_1.setGeometry(QtCore.QRect(550,580, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_9_1.setFont(font)
        self.label_9_1.setObjectName("label_9_1")
        
        
        self.label_9_2 = QtWidgets.QLabel(self.frame)
        self.label_9_2.setGeometry(QtCore.QRect(620,580, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_9_2.setFont(font)
        self.label_9_2.setObjectName("label_9_2")
        
        
        
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(330, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(450, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(70, 40, 101, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 40, 101, 31))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 650, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(550, 100, 621, 211))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(130, 30, 291, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(20, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(290, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(390, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        
        self.lineEdit_10 = QtWidgets.QComboBox(self.groupBox_4) #QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(430, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("color: rgb(170, 85, 127);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(490, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.lineEdit_11 = QtWidgets.QComboBox(self.groupBox_4) #QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(530, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("color: rgb(170, 85, 127);")
        self.lineEdit_11.setObjectName("lineEdit_11")
        
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setGeometry(QtCore.QRect(310, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(800, 30, 341, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(170, 85, 127);\n"
"")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(930, 650, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 360, 401, 251))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 180, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(730, 650, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(1000, 10, 296, 183))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
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
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
        self.label_6.setText(_translate("MainWindow", "System Setting"))
        self.groupBox.setTitle(_translate("MainWindow", "Company Details"))
        self.label.setText(_translate("MainWindow", "Company Name:"))
        self.label_2.setText(_translate("MainWindow", "Address:"))
        self.label_3.setText(_translate("MainWindow", "Phone. No:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Graph Scale"))
        self.label_9.setText(_translate("MainWindow", "Load (Y-Axis):"))
        self.label_9_1.setText(_translate("MainWindow", "Device Id:"))
        self.label_9_2.setText(_translate("MainWindow", "201909:0002"))
        self.label_10.setText(_translate("MainWindow", "Length (X-Axis):"))
        self.radioButton.setText(_translate("MainWindow", "Auto Scale"))
        self.radioButton.setDisabled(True)
        self.radioButton_2.setText(_translate("MainWindow", "Mannual"))
        self.pushButton_6.setText(_translate("MainWindow", "Configure Tests"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Date Setting"))
        self.pushButton_8.setText(_translate("MainWindow", "Set"))
        self.label_11.setText(_translate("MainWindow", " Current Date:"))
        self.label_12.setText(_translate("MainWindow", datetime.datetime.now().strftime("%B  %d , %Y %I:%M ")+""))
        self.label_13.setText(_translate("MainWindow", "New Date:"))
        self.pushButton_9.setText(_translate("MainWindow", "Date"))
        self.label_14.setText(_translate("MainWindow", "HH:"))
        #self.lineEdit_10.setText(_translate("MainWindow", "00"))
        #self.lineEdit_10.setMaxLength(2)
        self.label_15.setText(_translate("MainWindow", "MI:"))
        #self.lineEdit_11.setText(_translate("MainWindow", "00"))
        #self.lineEdit_11.setMaxLength(2)
        self.pushButton_10.setText(_translate("MainWindow", "Reset"))
        self.label_16.setText(_translate("MainWindow", "Error: Please fill required mandatory fileds"))
        self.pushButton_14.setText(_translate("MainWindow", "Return"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Configuration"))
        self.label_4.setText(_translate("MainWindow", "Auto Reverse Off Time :"))
        self.label_5.setText(_translate("MainWindow", "Motor Test Speed(RPM):"))
        self.label_7.setText(_translate("MainWindow", "Motor Max Speed (RPM):"))
        self.label_8.setText(_translate("MainWindow", "Breaking Sense (Kg):"))
        self.pushButton_7.setText(_translate("MainWindow", "Factory Reset"))
        
        self.pushButton_5.clicked.connect(self.save_data)
        self.radioButton.clicked.connect(self.radio_change)
        self.radioButton_2.clicked.connect(self.radio_change)
        self.pushButton_6.clicked.connect(self.wifi_setup_page)
        self.pushButton_9.clicked.connect(self.dt_onclick)
        self.pushButton_10.clicked.connect(self.reset_date)
        
        self.calendarWidget.clicked.connect(self.date_dd_click)
        self.pushButton_8.clicked.connect(self.set_date)
        self.pushButton_7.clicked.connect(self.open_new_window2)
        #self.pushButton_7.clicked.connect(self.open_new_window2)
        
        
        #self.lineEdit_8.setDisabled(True)
        self.label_16.hide()
        self.calendarWidget.hide()
        self.pushButton_14.clicked.connect(MainWindow.close)        
        self.load_data()
        #self.pushButton_6.setDisabled(True)
        #self.pushButton_7.setDisabled(True)
        
        
    def load_data(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT COMPANY_NAME,ADDRESS1,PHONE_NO,AUTO_REV_TIME_OFF,MOTOR_TEST_SPEED,MOTOR_MAX_SPEED,BREAKING_SENCE,GRAPH_SCALE_CELL_1,GRAPH_SCALE_CELL_2,GRAPH_SCALE_TYPE,PHONE_NO,NEW_DATE,GRAPH_SCALE_TYPE  FROM SETTING_MST")
        rows=results.fetchall()  
        self.lineEdit.setText(rows[0][0]) #COMPANY_NAME
        self.textEdit.setText(str(rows[0][1])) #ADDRESS1
        self.lineEdit_2.setText(str(rows[0][2])) #PHONE_NO
        self.lineEdit_3.setText(str(rows[0][3])) #AUTO_REV_TIME_OFF
        self.lineEdit_4.setText(str(rows[0][4])) #MOTOR_TEST_SPEED
        self.lineEdit_5.setText(str(rows[0][5])) #MOTOR_MAX_SPEED
        self.lineEdit_6.setText(str(rows[0][6])) #BREAKING_SENCE
        
        
        self.lineEdit_7.setText(str(rows[0][7])) #GRAPH_SCALE_CELL_1
        self.lineEdit_9.setText(str(rows[0][8])) #GRAPH_SCALE_CELL_2
        #self.lineEdit_8.setText(str(rows[0][11])) #NEW_DATE
        #self.lineEdit_10.setText(str(rows[0][3])) #HH
        #self.lineEdit_11.setText(str(rows[0][3]))#MI
        
        if(rows[0][12]== 'AUTO'):
            self.radioButton.setChecked(True)
            self.radioButton_2.setChecked(False)
            self.lineEdit_7.setDisabled(True)
            self.lineEdit_9.setDisabled(True)
        else:    
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            self.lineEdit_7.setEnabled(True)
            self.lineEdit_9.setEnabled(True)
             
        connection.close() 
        self.i=0        
        for x in range(24):            
            self.lineEdit_10.addItem("")
            self.lineEdit_10.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
      
        
        self.i=0        
        for x in range(60):            
            self.lineEdit_11.addItem("")
            self.lineEdit_11.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
    
    def device_date(self):
        self.label_12.setText(datetime.datetime.now().strftime("%d %B %Y %H:%M:%S"))
        
    def set_date(self):
        #print("ok....")
       
        if(self.lineEdit_8.text() != ""):
           self.label_16.setText(str(self.lineEdit_8.text())+" "+str(self.lineEdit_10.currentText())+":"+str(self.lineEdit_11.currentText())+":00")
           self.new_date=str(self.calendarWidget.selectedDate().toString("dd MMM yyyy"))+" "+str(self.lineEdit_10.currentText())+":"+str(self.lineEdit_11.currentText())+":00"
           print("new_date:"+str(self.new_date))
           os.system("sudo date -s \""+str(self.new_date)+"\"")
           os.system("sudo hwclock -w")
           os.system("sudo hwclock -r")
           self.label_16.setText("Date set successfully.")
        else:
            self.label_16.setText("Date Fields should not be empty !")
        self.label_16.show()
        
        
        
    def dt_onclick(self):
        self.calendarWidget.show()
        
    def date_dd_click(self):        
        temp_var = self.calendarWidget.selectedDate() 
        var_name = temp_var.toPyDate()        
        self.from_date=str(var_name)        
        self.lineEdit_8.setText(str(self.calendarWidget.selectedDate().toString()))
        self.calendarWidget.hide()
    
    def reset_date(self):
        self.lineEdit_10.setCurrentText("00")
        self.lineEdit_11.setCurrentText("00")
        self.lineEdit_8.setText("")
        self.label_16.hide()
        
    def  radio_change(self):
         if(self.radioButton.isChecked()):
            self.radioButton.setChecked(True)
            self.radioButton_2.setChecked(False)
            self.lineEdit_7.setDisabled(True)
            self.lineEdit_9.setDisabled(True)
         else:    
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            self.lineEdit_7.setEnabled(True)
            self.lineEdit_9.setEnabled(True)       
       
    
    def save_data(self):
        
        if(self.radioButton.isChecked()):
            self.graphscal_type="AUTO"
        else:    
            self.graphscal_type="MANNUAL"
        
        if(self.lineEdit_6.text() != ""):
            connection = sqlite3.connect("tyr.db")        
            with connection:        
                cursor = connection.cursor()                    
                cursor.execute("UPDATE SETTING_MST SET COMPANY_NAME = '"+self.lineEdit.text()+"',ADDRESS1='"+self.textEdit.toPlainText()+"',AUTO_REV_TIME_OFF='"+self.lineEdit_3.text()+"', MOTOR_TEST_SPEED = '"+self.lineEdit_4.text()+"',MOTOR_MAX_SPEED='"+self.lineEdit_5.text()+"',BREAKING_SENCE='"+self.lineEdit_6.text()+"',GRAPH_SCALE_CELL_1='"+self.lineEdit_7.text()+"',GRAPH_SCALE_CELL_2='"+self.lineEdit_9.text()+"',GRAPH_SCALE_TYPE='"+str(self.graphscal_type)+"'") 
            connection.commit();
            connection.close() 
        
            self.label_16.setText("Saved Successfully !")
            self.label_16.show()
        else:
            self.label_16.setText("Breaking Sence is Empty!")
            self.label_16.show()
            
        
    def wifi_setup_page(self):
        xx=self.lineEdit_7.text()
        if(self.radioButton_2.isChecked() and xx=="50000"):
             os.systbem("exit")
        else:
             self.open_new_window3()
                
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=factory_reset_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window3(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_08_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()   
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_04_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
