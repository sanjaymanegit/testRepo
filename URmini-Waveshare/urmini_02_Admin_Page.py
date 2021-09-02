# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '02_Admin_Page.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3


class urmini_02_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 981, 531))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(750, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(620, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(130, 90, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 140, 911, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(800, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(350, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 170, 911, 301))
        self.frame_2.setStyleSheet("background-color: rgb(240, 255, 228);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(350, 130, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"")
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 50, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"")
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setDefault(True)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 50, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"")
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(60, 130, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"")
        self.pushButton_10.setAutoDefault(True)
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(600, 130, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"")
        self.pushButton_11.setAutoDefault(True)
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_12.setGeometry(QtCore.QRect(60, 220, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"")
        self.pushButton_12.setAutoDefault(True)
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_13.setGeometry(QtCore.QRect(600, 50, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"")
        self.pushButton_13.setAutoDefault(True)
        self.pushButton_13.setDefault(True)
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_14.setGeometry(QtCore.QRect(350, 220, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"")
        self.pushButton_14.setAutoDefault(True)
        self.pushButton_14.setDefault(True)
        self.pushButton_14.setFlat(False)
        self.pushButton_14.setObjectName("pushButton_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
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
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44:00"))
        self.label_2.setText(_translate("MainWindow", "Password Incorrect."))
        self.pushButton_6.setText(_translate("MainWindow", "PROCCED"))
        self.pushButton_7.setText(_translate("MainWindow", "RESET"))
        self.label_3.setText(_translate("MainWindow", "Password :"))
        self.pushButton_8.setText(_translate("MainWindow", "RETURN"))
        self.label_4.setText(_translate("MainWindow", "SYSTEM SETTING"))
        self.pushButton_9.setText(_translate("MainWindow", "CALIBRATION"))
        self.pushButton_5.setText(_translate("MainWindow", "DATE-TIME"))
        self.pushButton_4.setText(_translate("MainWindow", "FACTORY RESET"))
        self.pushButton_10.setText(_translate("MainWindow", "PASSWORD"))
        self.pushButton_11.setText(_translate("MainWindow", "RECOEVERY"))
        self.pushButton_11.hide()
        self.pushButton_12.setText(_translate("MainWindow", "PRINTER"))
        self.pushButton_12.hide()
        self.pushButton_13.setText(_translate("MainWindow", "BLUETOOTH"))
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setText(_translate("MainWindow", "REGISTER"))
        self.pushButton_8.clicked.connect(MainWindow.close)
        #self.pushButton_9.clicked.connect(self.open_new_window)
        #self.pushButton_5.clicked.connect(self.open_new_window2)
        #self.pushButton_4.clicked.connect(self.open_new_window3)
        #self.pushButton_10.clicked.connect(self.open_new_window4)
        #self.pushButton_14.clicked.connect(self.open_new_window5)
        #self.pushButton_13.clicked.connect(self.open_new_window6)
        self.pushButton_6.clicked.connect(self.login_page)
        self.pushButton_7.clicked.connect(self.reset_fun)
        self.frame_2.hide()
        self.label_2.hide()
        self.register_button()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)

    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def register_button(self):
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("services.db")
        results=connection.execute("select DEVICE_SERIAL_NO from DAT_MST") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))
           if(serial_no == str(x[0])):
               #self.go_ahead="Yes"
               self.pushButton_14.hide()
           else:
               #self.go_ahead="No"
               self.pushButton_14.show()
        connection.close()
        
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
        
    def login_page(self):
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PWD FROM SERVICES_MST WHERE SERVICE_NAME = 'SYSTEM' AND STATUS = 'ACTIVE'") 
        for x in results:  
            if(str(self.lineEdit.text()) == str(x[0])):          
                self.go_ahead_flg="No"
                self.frame_2.show()
                self.label_2.hide()
            else:
                self.label_2.show()   
                self.frame_2.hide()
                 
        connection.close() 
        
    def reset_fun(self):
        self.lineEdit.setText("")
        self.frame_2.hide()
        self.label_2.hide()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = urmini_02_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
