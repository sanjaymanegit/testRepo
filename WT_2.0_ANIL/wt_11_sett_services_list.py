# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_11_sett_services_list.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from wt_14_ser_weighing_mode import wt_14_Ui_MainWindow
from wt_15_ser_auto_manual import wt_15_Ui_MainWindow
from wt_16_ser_sms_reports import wt_16_Ui_MainWindow
from wt_21_ser_DAT import wt_21_Ui_MainWindow
from wt_19_ser_factory_reset import wt_19_Ui_MainWindow
from wt_22_ser_WIFI import wt_22_Ui_MainWindow
#from wt_18_ser_database_backup import wt_18_Ui_MainWindow
from wt_35_ser_database_backup import wt_35_Ui_MainWindow
from wt_20_ser_change_password import wt_20_Ui_MainWindow
from wt_17_ser_printer_setup import wt_17_Ui_MainWindow
from wt_30_ser_camera_conf import wt_30_Ui_MainWindow

from wt_24_ur_RATES import wt_24_Ui_MainWindow
from wt_23_ur_COMPANY_INFO import wt_23_Ui_MainWindow
from wt_33_ser_datetime import wt_33_Ui_MainWindow

from wt_34_SS_SMS_ACTIVATION import wt_34_Ui_MainWindow
from wt_36_ser_register import wt_36_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3

class wt_11_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1311, 691))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet("background-color: rgb(255, 239, 242);")
        self.frame.setObjectName("frame")
        self.password_str=""
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 50, 181, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(270, 30, 631, 121))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 141, 31))
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(210, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")        
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")        
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")        
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 50, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 50, 75, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")        
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 170, 1231, 471))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 170, 171, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 70, 171, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 70, 171, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(730, 70, 151, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(920, 70, 281, 61))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 70, 251, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")        
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 170, 241, 61))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setGeometry(QtCore.QRect(530, 170, 171, 61))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setGeometry(QtCore.QRect(730, 170, 151, 61))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setGeometry(QtCore.QRect(920, 170, 281, 61))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setGeometry(QtCore.QRect(320, 270, 171, 61))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14_1.setGeometry(QtCore.QRect(530, 270, 171, 61))
        self.pushButton_14_1.setObjectName("pushButton_14_1")
        
        self.pushButton_14_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14_2.setGeometry(QtCore.QRect(730, 270, 171, 61))
        self.pushButton_14_2.setObjectName("pushButton_14_2")
        
        self.pushButton_14_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14_3.setGeometry(QtCore.QRect(920, 270, 281, 61))
        self.pushButton_14_3.setObjectName("pushButton_14_3")
        
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_15.setGeometry(QtCore.QRect(30, 270, 241, 61))
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(940, 80, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(1060, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
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
        self.label.setText(_translate("MainWindow", "Services List"))
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.groupBox_2.setTitle(_translate("MainWindow", "List"))
        self.pushButton_4.setText(_translate("MainWindow", "Camera Setting"))
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setText(_translate("MainWindow", "Auto/Manual"))
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setText(_translate("MainWindow", "SMS - Reports"))
        self.pushButton_6.setDisabled(True)
        self.pushButton_7.setText(_translate("MainWindow", "DAT"))
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setText(_translate("MainWindow", "Rates Configuration"))
        #self.pushButton_8.setDisabled(True)
        self.pushButton_9.setText(_translate("MainWindow", "Weighing Mode"))
        self.pushButton_9.setDisabled(True)
        self.pushButton_10.setText(_translate("MainWindow", "Company-Information"))
        #self.pushButton_10.setDisabled(True)
        self.pushButton_11.setText(_translate("MainWindow", "Factory Reset"))
        self.pushButton_12.setText(_translate("MainWindow", "Wifi-Setting"))
        self.pushButton_13.setText(_translate("MainWindow", "Database Backup"))
        self.pushButton_14.setText(_translate("MainWindow", "Printer Setup"))
        self.pushButton_15.setText(_translate("MainWindow", "Change Passwords"))
        self.pushButton_14_1.setText(_translate("MainWindow", "Date Setting"))
        self.pushButton_14_2.setText(_translate("MainWindow", "SMS - Activation"))
        self.pushButton_14_3.setText(_translate("MainWindow", "Register"))
        self.pushButton_14_3.hide()
        self.label_2.setText(_translate("MainWindow", "Incorrect Password !!!!"))
        self.label_3.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.pushButton.clicked.connect(self.show_page)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.reset_fun)
        self.pushButton_9.clicked.connect(self.open_new_window)
        self.pushButton_5.clicked.connect(self.open_new_window2)
        self.pushButton_6.clicked.connect(self.open_new_window3)
        self.pushButton_7.clicked.connect(self.open_new_window4)
        self.pushButton_8.clicked.connect(self.open_new_window11)
        self.pushButton_11.clicked.connect(self.open_new_window5)
        self.pushButton_10.clicked.connect(self.open_new_window12)
        self.pushButton_12.clicked.connect(self.open_new_window6)
        self.pushButton_13.clicked.connect(self.open_new_window7)
        self.pushButton_15.clicked.connect(self.open_new_window8)
        self.pushButton_14.clicked.connect(self.open_new_window9)
        self.pushButton_14_1.clicked.connect(self.open_new_window13)
        self.pushButton_14_2.clicked.connect(self.open_new_window14)
        self.pushButton_14_3.clicked.connect(self.open_new_window15)
        self.pushButton_4.clicked.connect(self.open_new_window10)
        
        self.label_2.hide()
        self.groupBox_2.hide()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_3.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
           
     
    def show_page(self):
        connection = sqlite3.connect("wt.db")
        results=connection.execute("select SS_PWD FROM SERIVES_SET")       
        for x in results:        
              self.password_str=str(x[0])
        connection.close()
        
        if(self.password_str == str(self.lineEdit.text())):
            self.groupBox_2.show()
            self.label_2.hide()
            self.register_button()
        else:
            self.label_2.show()
            self.groupBox_2.hide()
    
    
    def register_button(self):
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("services.db")
        results=connection.execute("select DEVICE_SERIAL_NO from DAT_MST") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))
           if(serial_no == str(x[0])):
               #self.go_ahead="Yes"
               self.pushButton_14_3.hide()
           else:
               #self.go_ahead="No"
               self.pushButton_14_3.show()
        
    def getserial(self):
        # Extract serial from cpuinfo file
        cpuserial = "0000000000000000"
        try:
           f = open('/proc/cpuinfo','r')
           for line in f:
                if line[0:6]=='Serial':
                   cpuserial = line[10:26]
           f.close()
        except:
           cpuserial = "ERROR000000000"
        return cpuserial    
       
    def reset_fun(self):
        self.label_2.hide()
        self.groupBox_2.hide()
        self.lineEdit.setText("")
    
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_14_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()   

    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_15_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
     
    def open_new_window3(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_16_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
     
     
    def open_new_window4(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_21_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window5(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_19_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window6(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_22_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window7(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_35_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()   
        
    def open_new_window8(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_20_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window9(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_17_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window10(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_30_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window11(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_24_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def open_new_window12(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_23_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
   
    def open_new_window13(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_33_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window14(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_34_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def open_new_window15(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_36_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()      
            
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_11_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
