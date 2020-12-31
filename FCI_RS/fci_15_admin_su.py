# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_15_admin_su.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from fci_20_wifi import fci_20_Ui_MainWindow
from fci_24_su_register import fci_24_Ui_MainWindow
from fci_18_admin_factory_reset import fci_18_Ui_MainWindow
from fci_22_su_API_config import fci_22_Ui_MainWindow
from fci_23_su_datetime import fci_23_Ui_MainWindow
from fci_16_admin_printer_setup import fci_16_Ui_MainWindow
from fci_36_calibration_login import fci_36_Ui_MainWindow
from fci_43_admin_maintns import fci_43_Ui_MainWindow
from fci_19_admin_change_password import fci_19_Ui_MainWindow
from fci_53_backup import fci_53_Ui_MainWindow
from fci_54_recovery import fci_54_Ui_MainWindow
from fci_56_sms_conf import fci_56_Ui_MainWindow
from cryptography.fernet import Fernet

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import sqlite3


class fci_15_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 782)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1311, 711))
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
         
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 50, 201, 81))
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 50, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 50, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 155, 1231, 528))
        '''
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        '''
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setGeometry(QtCore.QRect(110, 80, 221, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setGeometry(QtCore.QRect(460, 190, 221, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setGeometry(QtCore.QRect(790, 80, 281, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setGeometry(QtCore.QRect(450, 80, 231, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_15.setGeometry(QtCore.QRect(790, 190, 281, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_16.setGeometry(QtCore.QRect(110, 190, 221, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_17.setGeometry(QtCore.QRect(110, 310, 221, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_18.setGeometry(QtCore.QRect(460, 310, 221, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_19.setGeometry(QtCore.QRect(790, 420, 221, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_20.setGeometry(QtCore.QRect(110, 420, 221, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_21.setGeometry(QtCore.QRect(460, 420, 221, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_22.setGeometry(QtCore.QRect(790, 310, 281, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")       
        
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(940, 80, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(1050, 10, 221, 31))
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
        self.label.setText(_translate("MainWindow", " Service User :"))
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.pushButton_11.setText(_translate("MainWindow", "Factory Reset"))
        self.pushButton_12.setText(_translate("MainWindow", "Wifi-Setting"))
        self.pushButton_13.setText(_translate("MainWindow", "Maintaince"))
        #self.pushButton_13.setDisabled(True)
        self.pushButton_14.setText(_translate("MainWindow", "Printer Setup"))
        #self.pushButton_14.setDisabled(True)
        self.pushButton_15.setText(_translate("MainWindow", "Change Passwords"))
        #self.pushButton_15.setDisabled(True)
        self.pushButton_16.setText(_translate("MainWindow", "Date/Time Set"))
        self.pushButton_17.setText(_translate("MainWindow", "API Config"))
        self.pushButton_18.setText(_translate("MainWindow", "Callibration"))
        #self.pushButton_18.setDisabled(True)
        self.pushButton_19.setText(_translate("MainWindow", "Register"))
        self.pushButton_19.hide()
        self.pushButton_20.setText(_translate("MainWindow", "Backup"))
        self.pushButton_21.setText(_translate("MainWindow", "Recovery"))
        self.pushButton_22.setText(_translate("MainWindow", "SMS"))
        
        self.label_2.setText(_translate("MainWindow", "Incorrect Password !!!!"))
        self.label_3.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))        
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.startx()



    def startx(self):
        self.pushButton.clicked.connect(self.show_page)
        self.pushButton_12.clicked.connect(self.open_new_window2)
        self.pushButton_19.clicked.connect(self.open_new_window3)
        self.pushButton_11.clicked.connect(self.open_new_window4)
        self.pushButton_17.clicked.connect(self.open_new_window5)
        self.pushButton_16.clicked.connect(self.open_new_window6)
        self.pushButton_14.clicked.connect(self.open_new_window7)
        self.pushButton_18.clicked.connect(self.open_new_window8)
        self.pushButton_13.clicked.connect(self.open_new_window9)
        self.pushButton_15.clicked.connect(self.open_new_window10)
        self.pushButton_20.clicked.connect(self.open_new_window11)
        self.pushButton_21.clicked.connect(self.open_new_window12)
        self.pushButton_22.clicked.connect(self.open_new_window13)
        self.pushButton_2.clicked.connect(self.reset_fun)
        
        
        self.label_2.hide()
        self.groupBox_2.hide()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
    
        
    def device_date(self):     
        self.label_3.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def show_page(self):
        connection = sqlite3.connect("services.db")
        results=connection.execute("select PWD FROM SERVICES_MST WHERE SERVICE_NAME='SERVICE_USER_PWD'")       
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
        results=connection.execute("select DEVICE_SERIAL_NO,PRINTER_MAC_ADDR,RANDOM_NUM from DAT_MST") 
        for x in results:
           if(str(x[1]) != ""):
               d_cipher_suite = Fernet(str(x[1]))           
               plain_text = d_cipher_suite.decrypt(str.encode(x[2]))
               #print("Serial Id :"+str(serial_no)+"  Decripted serial No :"+str(plain_text,'utf-8'))  
           if(serial_no == str(plain_text,'utf-8')):               
               self.pushButton_19.hide()
           else:               
               self.pushButton_19.show()
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
               
    def reset_fun(self):
        self.label_2.hide()
        self.groupBox_2.hide()
        self.lineEdit.setText("")
    
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_20_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window3(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_24_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window4(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_18_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window5(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_22_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
   
    def open_new_window6(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_23_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window7(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_16_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window8(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_36_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()

    def open_new_window9(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_43_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window10(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_19_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window11(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_53_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window12(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_54_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window13(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=fci_56_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_15_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
