# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_16_ser_sms_reports.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from cryptography.fernet import Fernet
from PyQt5 import QtCore, QtGui, QtWidgets
from wt_29_SMS_HISTORY_report import wt_29_Ui_MainWindow
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3

class wt_16_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 701)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1121, 611))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.from_time=""
        self.to_time=""
        self.phone_1=""
        self.phone_2=""
        self.phone_3=""
        self.phone_4=""
        self.phone_5=""
        self.status=""
        
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
        self.line.setGeometry(QtCore.QRect(100, 290, 921, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 350, 1061, 241))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 190, 100, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 30, 141, 41))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(260, 30, 141, 41))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(570, 30, 91, 31))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(670, 30, 111, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(830, 30, 91, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(930, 30, 101, 31))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setMaxLength(10)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(670, 90, 111, 31))
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setMaxLength(10)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(930, 90, 101, 31))
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setMaxLength(10)
        self.lineEdit_5.setObjectName("lineEdit_5")
       
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(930, 140, 101, 31))
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setMaxLength(10)
        self.lineEdit_6.setObjectName("lineEdit_6")
        
        
        
        self.lineEdit_6_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6_1.setGeometry(QtCore.QRect(670, 140, 111, 31))
        self.lineEdit_6_1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6_1.setMaxLength(4)
        self.lineEdit_6_1.setObjectName("lineEdit_6_1")
        
        
        
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(580, 190, 100, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_6_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6_1.setGeometry(QtCore.QRect(700, 190, 100, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6_1.setFont(font)
        self.pushButton_6_1.setObjectName("pushButton_6_1")
        
        
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(570, 90, 91, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(830, 90, 91, 31))
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(830, 140, 91, 31))
        self.label_7.setObjectName("label_7")
        
        self.label_7_1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7_1.setGeometry(QtCore.QRect(570, 140, 91, 31))
        self.label_7_1.setObjectName("label_7_1")
        
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(50, 80, 341, 131))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 3, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 1, 4, 1, 1)
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
        self.label_19.setText(_translate("MainWindow", "SMS Reports Setting"))
        self.label_3.setText(_translate("MainWindow", "Incorrect Password."))
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.groupBox_2.setTitle(_translate("MainWindow", "SMS Reports Setting"))
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
        self.radioButton_2.setText(_translate("MainWindow", "Activate"))
        self.radioButton_3.setText(_translate("MainWindow", "Deactivate"))
        self.label.setText(_translate("MainWindow", "Phone No (1):"))
        self.lineEdit_2.setText(_translate("MainWindow", "9773540255"))
        self.label_2.setText(_translate("MainWindow", "Phone No (2):"))
        self.lineEdit_3.setText(_translate("MainWindow", "99434545565"))
        self.lineEdit_4.setText(_translate("MainWindow", "985435435455"))
        self.lineEdit_5.setText(_translate("MainWindow", "9835435555"))
        self.lineEdit_6.setText(_translate("MainWindow", "985452343244"))
        self.pushButton_6.setText(_translate("MainWindow", "Reset"))
        self.pushButton_6_1.setText(_translate("MainWindow", "SMS History"))
        self.label_5.setText(_translate("MainWindow", "Phone No (3):"))
        self.label_6.setText(_translate("MainWindow", "Phone No (4):"))
        self.label_7.setText(_translate("MainWindow", "Phone No (5):"))
        self.label_7_1.setText(_translate("MainWindow", "Min.Wt.(Kg):"))
        self.label_8.setText(_translate("MainWindow", "From Time :"))
        self.label_10.setText(_translate("MainWindow", "HH:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "05"))
        self.comboBox.setItemText(1, _translate("MainWindow", "06"))
        self.comboBox.setItemText(2, _translate("MainWindow", "07"))
        self.comboBox.setItemText(3, _translate("MainWindow", "20"))
        self.comboBox.setItemText(4, _translate("MainWindow", "21"))
        self.comboBox.setItemText(5, _translate("MainWindow", "22"))
        
        self.label_11.setText(_translate("MainWindow", "MI:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "05"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "06"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "07"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "20"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "21"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "22"))
        self.label_9.setText(_translate("MainWindow", "To Time:"))
        self.label_12.setText(_translate("MainWindow", "HH:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "05"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "06"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "07"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "20"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "21"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "22"))
        self.label_13.setText(_translate("MainWindow", "MI:"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "05"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "06"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "07"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "20"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "21"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "22"))
        self.pushButton.clicked.connect(self.login_page)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.reset_loging)
        self.pushButton_6_1.clicked.connect(self.open_new_window)
        
        self.label_3.hide()
        self.groupBox_2.hide()
        
        self.pushButton_5.clicked.connect(self.save_data)
        self.pushButton_6.clicked.connect(self.reset_data)
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def login_page(self):
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PWD,xxx FROM SERVICES_MST WHERE SERVICE_NAME = 'SMS_REPORTS' AND STATUS = 'ACTIVE'") 
        for x in results:
            print("key:"+str(x[1]))
            key=str(x[1])
            val=str(x[0])
            val2=str.encode(val)
            #val2=bytes(x[0],'utf-8')
            #print("pwd:"+str(x[0]))
            d_cipher_suite = Fernet(str(x[1]))
            #print("type:"+str(type(val2)))
            plain_text = d_cipher_suite.decrypt(val2)
            #print("plain_text :"+str(plain_text,'utf-8'))           
            if(str(self.lineEdit.text()) == str(plain_text,'utf-8')):                    
                self.go_ahead_flg="No"
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
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_6_1.setText("")
       
            
    def load_data(self):      
        connection = sqlite3.connect("services.db")
        results=connection.execute("select FROM_TIME ,TO_TIME,PHONE_1,PHONE_2,PHONE_3,PHONE_4,PHONE_5,STATUS from SMS_REPORTS_CONFIG") 
        for x in results:
             self.comboBox.setCurrentText(str(x[0])[0:2])
             self.comboBox_2.setCurrentText(str(x[0])[3:5])
             self.comboBox_3.setCurrentText(str(x[1])[0:2])
             self.comboBox_4.setCurrentText(str(x[1])[3:5])
             self.lineEdit_2.setText(str(x[2]))
             self.lineEdit_3.setText(str(x[3]))
             self.lineEdit_4.setText(str(x[4]))
             self.lineEdit_5.setText(str(x[5]))
             self.lineEdit_6.setText(str(x[6]))
             if(str(x[7]) == 'ACTIVE'):
                 self.radioButton_2.setChecked(True)
                 self.radioButton_3.setChecked(False)
             else:
                 self.radioButton_3.setChecked(True)
                 self.radioButton_2.setChecked(False)
        connection.close()
        self.label_3.hide()
        
        connection = sqlite3.connect("services.db")
        results=connection.execute("select WT_LIMIT FROM DEVICE_CONF") 
        for x in results:
             self.lineEdit_6_1.setText(str(x[0]))
    
    def save_data(self):
        self.from_time=str(self.comboBox.currentText()+":"+self.comboBox.currentText())
        self.to_time=str(self.comboBox_3.currentText()+":"+self.comboBox_4.currentText())
        self.phone_1=str(self.lineEdit_2.text())
        self.phone_2=str(self.lineEdit_3.text())
        self.phone_3=str(self.lineEdit_4.text())
        self.phone_4=str(self.lineEdit_5.text())
        self.phone_5=str(self.lineEdit_6.text())
        if(self.radioButton_2.isChecked()):
              self.status="ACTIVE"
        else:
              self.status="DEACTIVE"
              
        connection = sqlite3.connect("services.db")          
        with connection:        
                cursor = connection.cursor()                    
                cursor.execute("UPDATE SMS_REPORTS_CONFIG SET FROM_TIME='"+str(self.from_time)+"',TO_TIME='"+str(self.to_time)+"',PHONE_1='"+str(self.phone_1)+"',PHONE_2='"+str(self.phone_2)+"',PHONE_3='"+str(self.phone_3)+"',PHONE_4='"+str(self.phone_4)+"',PHONE_5='"+str(self.phone_5)+"',STATUS='"+str(self.status)+"'  WHERE JOB_NAME='DAILY_SMS'")
                cursor.execute("UPDATE DEVICE_CONF set WT_LIMIT='"+str(self.lineEdit_6_1.text())+"'") 
        connection.commit();
        connection.close()
        
        
        
        
        self.label_3.setText("Configuration Saved.") 
        self.label_3.show() 
        
        
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_29_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_16_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
