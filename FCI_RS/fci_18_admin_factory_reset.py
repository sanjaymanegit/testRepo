# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_19_ser_factory_reset.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3

class fci_18_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 711))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
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
        self.label_3.setGeometry(QtCore.QRect(460, 60, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(230, 130, 631, 131))
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
        self.line.setGeometry(QtCore.QRect(110, 280, 921, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 320, 661, 241))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(180, 30, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(120, 40, 141, 41))
        self.radioButton.setObjectName("radioButton")
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 40, 141, 41))
        self.radioButton_2.setObjectName("radioButton_2")
        
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(120, 90, 141, 41))
        self.checkBox.setObjectName("checkBox")
        
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(280, 90, 141, 41))
        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(450, 90, 141, 41))       
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        
        
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(300, 40, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)        
        self.label_6.setFont(font)       
        self.label_6.setObjectName("label_6")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)        
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 46, 125, 31))               
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.device_location="SITE"
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_19.setText(_translate("MainWindow", "Factory Reset"))
        self.label_3.setText(_translate("MainWindow", "Incorrect Password."))
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Factory Reset"))
        self.pushButton_5.setText(_translate("MainWindow", "FORMAT"))
        self.label_5.setText(_translate("MainWindow", "Done."))
        self.label_6.setText(_translate("MainWindow", "Device. Id:"))
        self.label_5.hide()
        self.checkBox.setText(_translate("MainWindow", "Weighing Data"))
        self.checkBox_2.setText(_translate("MainWindow", "Set Default Data"))
        self.checkBox_3.setText(_translate("MainWindow", "Master Data Only"))
        self.lineEdit_2.setReadOnly(True)
        self.radioButton.setText("Site")
        self.radioButton.setChecked(True)
        self.radioButton_2.setText("Storage")
        self.radioButton.hide()
        self.radioButton_2.hide()
        ## default to all 
        self.pushButton.clicked.connect(self.login_page)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.label_3.hide()        
        self.groupBox_2.hide()
        self.pushButton_2.clicked.connect(self.reset_loging)
        
        self.pushButton_5.clicked.connect(self.clean_data)
        
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
        
    def login_page(self):
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PWD FROM SERVICES_MST WHERE SERVICE_NAME = 'FACTORY_RESET' AND STATUS = 'ACTIVE'") 
        for x in results:  
            if(str(self.lineEdit.text()) == str(x[0])):          
                self.go_ahead_flg="No"
                self.groupBox_2.show()                
            else:
                self.label_3.show()   
                self.groupBox_2.hide()
                 
        connection.close()
        
        connection = sqlite3.connect("fci.db")
        results=connection.execute("SELECT DEVICE_ID,DEVICE_LOCATION_TYPE FROM GLOBAL_VAR") 
        for x in results:
                self.lineEdit_2.setText(str(x[0]))
                if(str(x[1]) =='SITE'):
                    self.radioButton.setChecked(True)
                    self.radioButton_2.setChecked(False)
                else:
                    self.radioButton.setChecked(False)
                    self.radioButton_2.setChecked(True)
                    
        connection.close()
    
    def reset_loging(self):
        self.lineEdit.setText("")
        self.label_3.hide()
        self.groupBox_2.hide()
        
        
    def clean_data(self):
        close = QMessageBox()
        close.setText(" <font color=blue>           !!!    WARNING     !!! </font> <br> <br>  <font color=red> YOUR ALL DATA WILL BE PERMANANTALY LOST </font> ")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:
                if(self.checkBox.isChecked()):
                    connection = sqlite3.connect("fci.db")          
                    with connection:        
                                cursor = connection.cursor()                    
                                cursor.execute(" DELETE FROM WEIGHT_MST")
                                cursor.execute(" DELETE FROM BATCH_MST")
                                cursor.execute(" DELETE FROM AUDIT_MST")
                                cursor.execute(" DELETE FROM API_LOGS")
                                cursor.execute(" DELETE FROM SLOTS_MST")                        
                                cursor.execute(" DELETE FROM BATCH_STORAGE_LOSS")
                                cursor.execute(" DELETE FROM ISSUE_QUANTITY_DTLS")
                                cursor.execute(" DELETE FROM ISSUE_MST")                                
                                cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('WEIGHT_MST','BATCH_MST','AUDIT_MST','API_LOGS','SLOTS_MST','BATCH_STORAGE_LOSS','ISSUE_QUANTITY_DTLS','ISSUE_MST')")
                                
                    connection.commit();
                    connection.close()
                    self.label_3.setText("Factory-reset completed successfully.") 
                    self.label_3.show()
                
                if(self.checkBox_2.isChecked()):            
                    connection = sqlite3.connect("services.db")          
                    with connection:        
                                cursor = connection.cursor()                    
                                cursor.execute("UPDATE SERVICES_MST SET PWD='ss12345' WHERE SERVICE_NAME='SERVICE_USER_PWD' ")
                                cursor.execute("UPDATE SERVICES_MST SET PWD='12345' WHERE SERVICE_NAME='BUSINESS_USER_PWD'")
                                cursor.execute("UPDATE SERVICES_MST SET PWD='1000' WHERE SERVICE_NAME='CHANGE_PASSWORDS'")                                
                    connection.commit();
                    connection.close()
                    self.label_3.setText("Factory-reset completed successfully.") 
                    self.label_3.show()
                    
                if(self.checkBox_3.isChecked()):            
                    connection = sqlite3.connect("fci.db")          
                    with connection:        
                                cursor = connection.cursor()
                                cursor.execute("DELETE FROM MATERIAL_TYPES")
                                cursor.execute("DELETE FROM CONTRACTOR_MST")
                                cursor.execute("DELETE FROM STORAGE_DETAILS")
                                cursor.execute("DELETE FROM USERS_MST where USER_ID > 1")
                                cursor.execute("DELETE FROM CALIBRATION_LOG")
                                cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('MATERIAL_TYPES','CONTRACTOR_MST','STORAGE_DETAILS','CALIBRATION_LOG')")
                                cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=2 WHERE name in ('USERS_MST')")
                    connection.commit();
                    connection.close()
                    self.label_3.setText("Factory-reset completed successfully.") 
                    self.label_3.show()
                    
                    
                if(self.radioButton.isChecked()):
                    self.device_location="SITE"
                elif(self.radioButton_2.isChecked()):
                    self.device_location="STORAGE"
                    
                connection = sqlite3.connect("fci.db")          
                with connection:        
                                cursor = connection.cursor()
                                cursor.execute("UPDATE GLOBAL_VAR SET DEVICE_LOCATION_TYPE='"+str(self.device_location)+"',DEVICE_ID='"+self.lineEdit_2.text()+"' ")
                                self.label_3.setText("Factory-reset completed successfully.") 
                                self.label_3.show()
                connection.commit();
                connection.close()
                
                self.log_audit("Factory Reset","Factory Reset Done")
        else:
                self.label_3.setText("Cancled Factory Reset.") 
                self.label_3.show() 
    
    def log_audit(self,event_name,desc_str):        
        connection = sqlite3.connect("fci.db")
        with connection:        
            cursor = connection.cursor()       
            cursor.execute("INSERT INTO AUDIT_MST(AUDIT_TYPE,MESSAGE) VALUES(?,?)",(event_name,desc_str))
            cursor.execute("UPDATE AUDIT_MST SET USER_ID = (SELECT LOGIN_USER_ID FROM GLOBAL_VAR) WHERE USER_ID IS NULL")            
        connection.commit();
        connection.close()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_18_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
