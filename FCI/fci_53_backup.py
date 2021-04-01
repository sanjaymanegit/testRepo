# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_53_backup.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3
from PyQt5.Qt import QTableWidgetItem

class fci_53_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 711))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(870, 30, 261, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(990, 100, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 150, 4);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_7.setGeometry(QtCore.QRect(590, 590, 711, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_44 = QtWidgets.QLabel(self.groupBox_7)
        self.label_44.setGeometry(QtCore.QRect(40, 20, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(300, 90, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);")
        #self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(650, 100, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 150, 4);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(820, 100, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 150, 4);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(10, 180, 1301, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(40, 610, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(209, 8, 45);\n"
"color: rgb(255, 255, 0);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(490, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(244, 244, 0);\n"
"background-color: rgb(170, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(170, 610, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 150, 4);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(30, 270, 421, 71))
        self.frame_5.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 85, 0);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(3)
        self.frame_5.setObjectName("frame_5")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_4.setGeometry(QtCore.QRect(220, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(30, 460, 411, 81))
        self.frame_3.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 85, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(110, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(230, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 20, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")       
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(40, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 400, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(300, 610, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 150, 4);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(590, 270, 691, 291))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        '''
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        '''
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        #item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(600, 220, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1396, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.backup_job_status=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00 "))
        self.pushButton_9.setText(_translate("MainWindow", "RETURN"))
        self.groupBox_7.setTitle(_translate("MainWindow", " MESSAGE"))
        self.label_44.setText(_translate("MainWindow", "Invalid Password"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD :"))
        self.pushButton_10.setText(_translate("MainWindow", "SHOW"))
        self.pushButton_11.setText(_translate("MainWindow", "CLEAR"))
        self.pushButton_12.setText(_translate("MainWindow", "SAVE"))
        self.label_9.setText(_translate("MainWindow", "BACKUP"))
        self.pushButton_13.setText(_translate("MainWindow", "LOG"))
        self.radioButton_3.setText(_translate("MainWindow", "ACTIVE"))
        self.radioButton_4.setText(_translate("MainWindow", "INACTIVE"))
        self.i=0        
        for x in range(24):            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        self.label_6.setText(_translate("MainWindow", "MI:"))
        self.i=0        
        for x in range(60):            
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        self.comboBox.setCurrentText("18")
        self.comboBox_2.setCurrentText("00")
        self.comboBox.setDisabled(True)
        self.comboBox_2.setDisabled(True)
        self.label_5.setText(_translate("MainWindow", "HH:"))
        self.label_8.setText(_translate("MainWindow", "STATUS"))
        self.label_7.setText(_translate("MainWindow", "TIME"))
        self.pushButton_14.setText(_translate("MainWindow", "TAKE BACKUP"))
        self.tableWidget.setSortingEnabled(True)
        '''
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        '''
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BACKUP DATE"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MODE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "FILE NAME"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1212"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("MainWindow", "BACKUP HISTORY"))
        self.pushButton_9.clicked.connect(MainWindow.close)
        self.pushButton_11.clicked.connect(self.reset_loging)
        self.pushButton_10.clicked.connect(self.login_page)
        self.pushButton_13.clicked.connect(self.list_report_data)
        self.pushButton_14.clicked.connect(self.backup_process)
        self.pushButton_12.clicked.connect(self.save_data)
        self.reset_loging()
        
        #self.list_report_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)      
        
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    
    def login_page(self):        
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PWD,xxx FROM SERVICES_MST WHERE SERVICE_NAME = 'BACKUP' AND STATUS = 'ACTIVE'") 
        for x in results:
            val=str(x[0])           
        connection.close()
        print("pwd:"+self.lineEdit.text()+" db val:"+str(val))
        if(str(self.lineEdit.text()) == str(val)):
                self.show_all()
                self.list_report_data()
                self.groupBox_7.hide()
        else:
                self.groupBox_7.show()
                self.label_44.show()
                self.label_44.setText("INCORRECT PASSWORD.")
                #self.reset_loging()
               
    
    def reset_loging(self):
        self.lineEdit.setText("")
        self.frame_3.hide()
        self.frame_5.hide()
        self.tableWidget.hide()
        self.groupBox_7.hide()
        self.label_5.hide()
        self.label_8.hide()
        self.label_7.hide()
        self.pushButton_14.hide()
        self.pushButton_12.hide()
        self.pushButton_13.hide()
        self.label_10.hide()
        
    def show_all(self):        
        self.frame_3.show()
        self.frame_5.show()
        self.tableWidget.show()
        self.groupBox_7.show()
        self.label_5.show()
        self.label_8.show()
        self.label_7.show()
        self.pushButton_14.show()
        self.pushButton_12.show()
        self.pushButton_13.show()
        self.label_10.show()
        #self.list_report_data()
        connection = sqlite3.connect("fci.db")
        results=connection.execute("SELECT BACKUP_JOB_STATUS ,BACKUP_JOB_HH,BACKUP_JOB_MI FROM GLOBAL_VAR") 
        for x in results:            
            self.backup_job_status=str(x[0])
            if(self.backup_job_status=="ACTIVE"):
                self.radioButton_3.setChecked(True)
                self.radioButton_4.setChecked(False)
            else:
                self.radioButton_3.setChecked(False)
                self.radioButton_4.setChecked(True)
            self.comboBox.setCurrentText(str(x[1]))
            self.comboBox_2.setCurrentText(str(x[2]))
        connection.close()
        
    def save_data(self):
        if(self.radioButton_3.isChecked()):
            self.backup_job_status="ACTIVE"
        else:
            self.backup_job_status="INACTIVE"
        
        connection = sqlite3.connect("fci.db")          
        with connection:        
                    cursor = connection.cursor()                    
                    cursor.execute("UPDATE GLOBAL_VAR SET BACKUP_JOB_STATUS='"+str(self.backup_job_status)+"',BACKUP_JOB_HH='"+self.comboBox.currentText()+"',BACKUP_JOB_MI='"+self.comboBox_2.currentText()+"'")                    
        connection.commit();
        connection.close()
        self.groupBox_7.show()
        self.label_44.show()
        self.label_44.setText("SAVED SUCCESSFULLY.")
    
    def backup_process(self):
        self.groupBox_7.show()       
        self.label_44.setText("STARTED BACKUP")
        self.label_44.show()
        time.sleep(1)
        self.bkp_f()
        
       
    def bkp_f(self):        
        #print("inside backup ")
        date_str=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                try:
                    os.system("cp fci.db fci_bkp"+str(date_str)+".db")
                    os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                    os.system("mv fci_bkp"+str(date_str)+".db /media/usb")
                    os.system("sudo umount /media/usb")
                    connection = sqlite3.connect("services.db")          
                    with connection:        
                        cursor = connection.cursor()                    
                        cursor.execute("INSERT INTO ZBACKUP_HIST(BACKUP_TYPE,FILE_NAME,PATH,STATUS,BACKUP_ON) VALUES ('Manual','fci_bkp"+str(date_str)+".db','/media/usb','Completed',CURRENT_TIMESTAMP)")                    
                    connection.commit();
                    connection.close()
                    self.list_report_data()
                    self.groupBox_7.show()       
                    self.label_44.show()
                    self.label_44.setText("BACKUP COMPLETED.")
                   
                   
                #self.label_9.setText("fci_bkp"+str(date_str)+".db")
                #self.label_44.show()
                #self.label_44.setText("wt_bkp"+str(date_str)+".db")
                except:
                    self.label_44.show()
                    self.label_44.setText("OS ERROR.")
               
        else:
             #print("Please connect usb storage device")
             self.groupBox_7.show()       
             self.label_44.show()
             self.label_44.setText("PLEASE CONNECT USB DEVICE.")
             
    def get_usb_storage_id(self):
        os.system("rm -rf lsusb_data_db_bkp.txt")  
        product_id = "ERROR"
        os.system("lsusb >> lsusb_data_db_bkp.txt")
        try:
           f = open('lsusb_data_db_bkp.txt','r')
           for line in f:
               cnt=0                
               cnt=int(line.find("SanDisk"))
               if cnt > 0 :                   
                   product_id = line[28:33]
                   product_id = "0x"+str(product_id)
           f.close()
        except:
           product_id = "ERROR"
           self.label_44.show()
           self.label_44.setText("USB ERROR.")             
        return product_id
    
    
    def list_report_data(self):
        self.groupBox_7.hide()
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget.setHorizontalHeaderLabels(['BACKUP DATE', 'MODE', 'FILE NAME'])               
        connection = sqlite3.connect("services.db")  
        results=connection.execute("select BACKUP_ON,BACKUP_TYPE, FILE_NAME  FROM ZBACKUP_HIST order by BACKUP_ON desc ")            
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close() 
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)      



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_53_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())