# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ur_13_calibration.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3
import serial

class ur_13_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 701)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1181, 631))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(30, 20, 231, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(420, 20, 221, 41))
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
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(250, 90, 631, 121))
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 50, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 50, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(830, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 230, 1121, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 320, 1131, 271))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(290, 30, 311, 161))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_8.setGeometry(QtCore.QRect(170, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(50, 30, 241, 61))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(640, 30, 341, 151))
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_9.setGeometry(QtCore.QRect(40, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_10.setGeometry(QtCore.QRect(160, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 241, 61))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setGeometry(QtCore.QRect(50, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 571, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 21))
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
        self.label_19.setText(_translate("MainWindow", "Calibration"))
        self.label_3.setText(_translate("MainWindow", "Incorrect Password."))
        self.label_3.hide()
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Calibration Process"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Step 1"))
        self.pushButton_7.setText(_translate("MainWindow", "OK"))
        self.pushButton_8.setText(_translate("MainWindow", "NEXT"))
        self.label.setText(_translate("MainWindow", " Put empty Bicker/Pot on base  \n"+" and Click on Ok Button.\n"+" And Procced for Next step"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Step 2"))
        self.pushButton_9.setText(_translate("MainWindow", "OK"))
        self.pushButton_10.setText(_translate("MainWindow", "Verify"))
        self.label_2.setText(_translate("MainWindow", "  Fill Bicker with 1 liter Water \n"+" and then click on Ok button"))
        self.pushButton_11.setText(_translate("MainWindow", "Start Callibration"))
        self.label_5.setText(_translate("MainWindow", "Calibration Process Started."))
        self.label_5.hide()
        self.pushButton.clicked.connect(self.login_page)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.reset_login)
        self.pushButton_11.clicked.connect(self.start_calibration)
        self.pushButton_7.clicked.connect(self.step1_ok)
        self.pushButton_8.clicked.connect(self.step1_next)
        self.pushButton_9.clicked.connect(self.step2_ok)
        self.pushButton_10.clicked.connect(self.step2_verify)
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.timer1.stop()
        self.groupBox_2.hide()
        self.groupBox_5.setDisabled(True)
        self.groupBox_6.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def reset_login(self):
        self.label_3.hide()
        self.lineEdit.setText("")
        
    def login_page(self):
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PWD FROM SERVICES_MST WHERE SERVICE_NAME = 'CALIBRATION' AND STATUS = 'ACTIVE'") 
        for x in results:  
            if(str(self.lineEdit.text()) == str(x[0])):          
                self.go_ahead_flg="No"
                self.groupBox_2.show()
                #self.load_data()
            else:
                self.label_3.show()   
                self.groupBox_2.hide()
                 
        connection.close()
    
    def start_calibration(self):
        self.label_5.show()
        self.pushButton_11.setDisabled(True)
        self.groupBox_5.setEnabled(True)
        self.label_5.setText("Procced for Step1")  
        self.label_5.show()
        
        
    def step1_ok(self):
        self.pushButton_8.setEnabled(True)
        self.pushButton_7.setDisabled(True)
        try:
            self.ser = serial.Serial(
                                port='/dev/ttyAMA0',
                                baudrate=115200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.05
                            )
        
            self.ser.flush()
            b = bytes('Z', 'utf-8')
            self.ser.write(b)            
        except IOError:
            print("IO Errors")
            self.label_5.setText("IO Errors" )  
            self.label_5.show()
            
    def step1_next(self):
        self.groupBox_6.setEnabled(True)
        self.groupBox_5.setDisabled(True)        
        self.label_5.setText("Procced for Step2")  
        self.label_5.show()   
     
    def step2_ok(self):
        self.pushButton_10.setEnabled(True)
        self.pushButton_9.setDisabled(True)
        try:
            self.ser = serial.Serial(
                                port='/dev/ttyAMA0',
                                baudrate=115200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.05
                            )
        
            self.ser.flush()
            b = bytes('C', 'utf-8')
            self.ser.write(b)           
            time.sleep(1)
            self.label_5.setText("Calibration is Done succefully , Please verify." )  
            self.label_5.show()            
        except IOError:
            print("IO Errors")
            self.label_5.setText("IO Errors" )  
            self.label_5.show()
        
    def step2_verify(self):
        try:
            self.ser = serial.Serial(
                                port='/dev/ttyAMA0',
                                baudrate=115200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.05
                            )        
              
            self.line = self.ser.readline()                      
            print("o/p:"+str(self.line))
            self.xstr0=str(self.line,'utf-8')
            self.xstr1=self.xstr0.replace("\r","")
            self.xstr2=self.xstr1.replace("\n","")
            self.buff=self.xstr2.split("_")
            if(len(self.buff) > 2):
                self.label_5.setText("Current Weight is : "+str(self.buff[0])+" kg." )  
                self.label_5.show()
            else:
                self.label_5.setText("O/P :"+str(self.line))  
                self.label_5.show()
        except IOError:
            print("IO Errors")
            self.label_5.setText("IO Errors" )  
            self.label_5.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ur_13_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
