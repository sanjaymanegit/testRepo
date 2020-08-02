# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_30_ser_camera_conf.ui'
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

class wt_30_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1174, 759)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1121, 681))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(40, 40, 451, 51))
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
        self.label_3.setGeometry(QtCore.QRect(460, 60, 221, 31))
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
        self.groupBox.setGeometry(QtCore.QRect(220, 140, 631, 121))
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
        self.line.setGeometry(QtCore.QRect(90, 280, 921, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 310, 1031, 341))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(340, 20, 91, 41))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(480, 20, 111, 41))
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 290, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(150, 70, 701, 191))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 6, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 7, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 6, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 1, 7, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_13.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_12.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 2, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 4, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 2, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 6, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_14.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 2, 7, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_17.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout.addWidget(self.lineEdit_17, 3, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 3, 2, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_16.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 3, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 3, 4, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_15.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 3, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 6, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_18.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout.addWidget(self.lineEdit_18, 3, 7, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1174, 21))
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
        self.label_19.setText(_translate("MainWindow", "IP Camera Configuration"))
        self.label_3.setText(_translate("MainWindow", "Incorrect Password."))
        self.label_3.hide()
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.groupBox_2.setTitle(_translate("MainWindow", "IP Camera Configuration"))
        self.radioButton_2.setText(_translate("MainWindow", "Activate"))
        self.radioButton_3.setText(_translate("MainWindow", "Deactivate"))
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
        self.pushButton_6.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "Camera-1 IP :"))
        #self.lineEdit_8.setText(_translate("MainWindow", "192.168.1.20"))
        self.label_8.setText(_translate("MainWindow", "User Id:"))
        #self.lineEdit_9.setText(_translate("MainWindow", "admin"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        #self.lineEdit_3.setText(_translate("MainWindow", "31dec2019"))
        self.label_5.setText(_translate("MainWindow", "Port :"))
        #self.lineEdit_4.setText(_translate("MainWindow", "554"))
        self.label_6.setText(_translate("MainWindow", "Camera2- IP :"))
        #self.lineEdit_10.setText(_translate("MainWindow", "192.168.1.20"))
        self.label_9.setText(_translate("MainWindow", "User Id:"))
        #self.lineEdit_11.setText(_translate("MainWindow", "admin"))
        self.label_7.setText(_translate("MainWindow", "Password:"))
        #self.lineEdit_5.setText(_translate("MainWindow", "31dec2019"))
        self.label_10.setText(_translate("MainWindow", "Port :"))
        #self.lineEdit_6.setText(_translate("MainWindow", "554"))
        self.label_11.setText(_translate("MainWindow", "Camera3- IP :"))
        #self.lineEdit_13.setText(_translate("MainWindow", "192.168.1.20"))
        self.label_13.setText(_translate("MainWindow", "User Id:"))
        #self.lineEdit_12.setText(_translate("MainWindow", "admin"))
        self.label_14.setText(_translate("MainWindow", "Password:"))
        #self.lineEdit_7.setText(_translate("MainWindow", "31dec2019"))
        self.label_12.setText(_translate("MainWindow", "Port :"))
        #self.lineEdit_14.setText(_translate("MainWindow", "554"))
        self.label_15.setText(_translate("MainWindow", "Camera4- IP :"))
        #self.lineEdit_17.setText(_translate("MainWindow", "192.168.1.20"))
        self.label_17.setText(_translate("MainWindow", "User Id:"))
        #self.lineEdit_16.setText(_translate("MainWindow", "admin"))
        self.label_18.setText(_translate("MainWindow", "Password:"))
        #self.lineEdit_15.setText(_translate("MainWindow", "31dec2019"))
        self.label_16.setText(_translate("MainWindow", "Port :"))
        #self.lineEdit_18.setText(_translate("MainWindow", "554"))
        self.pushButton.clicked.connect(self.login_page)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.reset_loging)
        self.pushButton_5.clicked.connect(self.save_data)
        self.pushButton_6.clicked.connect(self.reset_data)
        self.radioButton_2.clicked.connect(self.enable_disable)
        self.radioButton_3.clicked.connect(self.enable_disable)
        self.groupBox_2.hide()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
 
    def enable_disable(self):
        if(self.radioButton_2.isChecked()):
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_5.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
            self.lineEdit_7.setEnabled(True)
            self.lineEdit_8.setEnabled(True)
            self.lineEdit_9.setEnabled(True)
            self.lineEdit_10.setEnabled(True)
            self.lineEdit_11.setEnabled(True)
            self.lineEdit_12.setEnabled(True)
            self.lineEdit_13.setEnabled(True)
            self.lineEdit_14.setEnabled(True)
            self.lineEdit_15.setEnabled(True)
            self.lineEdit_16.setEnabled(True)
            self.lineEdit_17.setEnabled(True)        
        else:
            self.lineEdit_3.setDisabled(True)
            self.lineEdit_4.setDisabled(True)
            self.lineEdit_5.setDisabled(True)
            self.lineEdit_6.setDisabled(True)
            self.lineEdit_7.setDisabled(True)
            self.lineEdit_8.setDisabled(True)
            self.lineEdit_9.setDisabled(True)
            self.lineEdit_10.setDisabled(True)
            self.lineEdit_11.setDisabled(True)
            self.lineEdit_12.setDisabled(True)
            self.lineEdit_13.setDisabled(True)
            self.lineEdit_14.setDisabled(True)
            self.lineEdit_15.setDisabled(True)
            self.lineEdit_16.setDisabled(True)
            self.lineEdit_17.setDisabled(True)
        
 
    def login_page(self):
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PWD FROM SERVICES_MST WHERE SERVICE_NAME = 'WEIGHING_MODE' AND STATUS = 'ACTIVE'") 
        for x in results:  
            if(str(self.lineEdit.text()) == str(x[0])):
                self.groupBox_2.show()
                self.load_data()
            else:
                self.label_3.setText("Incorrect Password.") 
                self.label_3.show()   
                self.groupBox_2.hide()
                 
        connection.close()    
        
    def reset_loging(self):
        self.lineEdit.setText("")         
        self.label_3.hide()
        self.groupBox_2.hide()
        
    def reset_data(self):        
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")
        self.lineEdit_12.setText("")
        self.lineEdit_13.setText("")
        self.lineEdit_14.setText("")
        self.lineEdit_15.setText("")
        self.lineEdit_16.setText("")
        self.lineEdit_17.setText("")
        
        
        
        
        
    def load_data(self):        
        connection = sqlite3.connect("wt.db")
        results=connection.execute("select distinct STATUS from CAMERA_CONF LIMIT 1") 
        for x in results:
             if(str(x[0]) == 'ACTIVE'):
                  self.radioButton_2.setChecked(True)
                  self.radioButton_3.setChecked(False)                  
             else:
                  self.radioButton_3.setChecked(True)
                  self.radioButton_2.setChecked(False)                  
             
        self.enable_disable()        
        connection = sqlite3.connect("wt.db")
        results=connection.execute("select CAMERA_NO,IP_ADD,USER_ID,PASSWD,PORT from CAMERA_CONF order by CAMERA_NO asc") 
        for x in results:
             #print("CAMERA_NO :"+str(x[0]))
             if(int(x[0]) == 1):
                 #print("CAMERA_NO xxx:"+str(x[4]))
                 self.lineEdit_8.setText(str(x[1]))     #c1 ip
                 self.lineEdit_9.setText(str(x[2]))     #c1 user id
                 self.lineEdit_3.setText(str(x[3]))     #c1 paasword
                 self.lineEdit_4.setText(str(x[4]))     #c1 port
             elif(int(x[0]) == 2):
                 self.lineEdit_10.setText(str(x[1]))     #c2 ip
                 self.lineEdit_11.setText(str(x[2]))     #c2 user id
                 self.lineEdit_5.setText(str(x[3]))     #c2 paasword
                 self.lineEdit_6.setText(str(x[4]))     #c2 port
             elif(int(x[0]) == 3):
                 self.lineEdit_13.setText(str(x[1]))     #c3 ip
                 self.lineEdit_12.setText(str(x[2]))     #c3 user id
                 self.lineEdit_7.setText(str(x[3]))     #c3 paasword
                 self.lineEdit_14.setText(str(x[4]))     #c3 port
             elif(int(x[0]) == 4):
                 self.lineEdit_17.setText(str(x[1]))     #c4 ip
                 self.lineEdit_16.setText(str(x[2]))     #c4 user id
                 self.lineEdit_15.setText(str(x[3]))     #c4 paasword
                 self.lineEdit_18.setText(str(x[4]))     #c4 port  
                                  
        connection.close()
        self.label_3.hide()     
     
     
    def save_data(self):        
        self.c1_ip=str(self.lineEdit_8.text())
        self.c2_ip=str(self.lineEdit_10.text())
        self.c3_ip=str(self.lineEdit_13.text())
        self.c4_ip=str(self.lineEdit_17.text()) 
        if(self.radioButton_2.isChecked()):
              self.status="ACTIVE"
        else:
              self.status="DEACTIVE"
       
        if(str(self.c1_ip) != ""):     
            connection = sqlite3.connect("wt.db")          
            with connection:        
                    cursor = connection.cursor()                    
                    cursor.execute("UPDATE CAMERA_CONF SET IP_ADD='"+str(self.lineEdit_8.text())+"',USER_ID='"+str(self.lineEdit_9.text())+"',PASSWD='"+str(self.lineEdit_3.text())+"',PORT='"+str(self.lineEdit_4.text())+"',STATUS='"+str(self.status)+"'  WHERE CAMERA_NO='1'")
                    
            connection.commit();
            connection.close()
            
        if(str(self.c2_ip) != ""):     
            connection = sqlite3.connect("wt.db")          
            with connection:        
                    cursor = connection.cursor()                    
                    cursor.execute("UPDATE CAMERA_CONF SET IP_ADD='"+str(self.lineEdit_10.text())+"',USER_ID='"+str(self.lineEdit_11.text())+"',PASSWD='"+str(self.lineEdit_5.text())+"',PORT='"+str(self.lineEdit_6.text())+"',STATUS='"+str(self.status)+"'  WHERE CAMERA_NO='2'")
                    
            connection.commit();
            connection.close()
            
        if(str(self.c3_ip) != ""):     
            connection = sqlite3.connect("wt.db")          
            with connection:        
                    cursor = connection.cursor()                    
                    cursor.execute("UPDATE CAMERA_CONF SET IP_ADD='"+str(self.lineEdit_13.text())+"',USER_ID='"+str(self.lineEdit_12.text())+"',PASSWD='"+str(self.lineEdit_7.text())+"',PORT='"+str(self.lineEdit_14.text())+"',STATUS='"+str(self.status)+"'  WHERE CAMERA_NO='3'")
                    
            connection.commit();
            connection.close()
            
        if(str(self.c4_ip) != ""):     
            connection = sqlite3.connect("wt.db")          
            with connection:        
                    cursor = connection.cursor()                    
                    cursor.execute("UPDATE CAMERA_CONF SET IP_ADD='"+str(self.lineEdit_17.text())+"',USER_ID='"+str(self.lineEdit_16.text())+"',PASSWD='"+str(self.lineEdit_15.text())+"',PORT='"+str(self.lineEdit_18.text())+"',STATUS='"+str(self.status)+"'  WHERE CAMERA_NO='4'")
                    
            connection.commit();
            connection.close()
        
        
        
        
        self.label_3.setText("Configuration Saved.") 
        self.label_3.show() 
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_30_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
