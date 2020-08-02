# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'wt_01_main.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from wt_02_reports import wt_02_Ui_MainWindow
#from wt_13_wighing_mode import wt_13_Ui_MainWindow
from wt_04_weight_1 import wt_04_1_Ui_MainWindow
from wt_10_setting_menu import wt_10_Ui_MainWindow
from wt_05_dup_recipt import wt_05_Ui_MainWindow
import sqlite3
import datetime

import time
from PyQt5.QtCore import QDate
import sys,os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 40, 1280, 640))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet("background-color: rgb(255, 239, 242);")
        self.frame.setObjectName("frame")
        self.go_ahead="No"
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(100, 390, 181, 151))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 390, 181, 151))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(960, 390, 181, 151))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 390, 181, 151))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")        
       
       
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(1050, 20, 221, 31))
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
        
        
        
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 70, 401, 251))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)        
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("comp_name.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(601, 261))        
        self.pushButton_5.setObjectName("pushButton_5")
        
        
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(810, 560, 90, 26))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)        
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("Shutdown")
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(910, 560, 90, 26))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)        
        self.pushButton_7.setFont(font)
        self.pushButton_7.setText("Reboot")
        self.pushButton_7.setObjectName("pushButton_7")
        
       
        self.label_4_1 = QtWidgets.QLabel(self.frame)
        self.label_4_1.setGeometry(QtCore.QRect(1000, 560, 161, 26))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        #font.setBold(False)
        #font.setWeight(75)
        self.label_4_1.setFont(font)
        #self.label_4_1.setStyleSheet("color: rgb(0, 0, 255);color: rgb(170, 0, 0);")
        self.label_4_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4_1.setObjectName("label_4_1")
        
        
        
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
        self.pushButton.setText(_translate("MainWindow", "Weighing"))
        self.pushButton_2.setText(_translate("MainWindow", "Reports"))
        self.pushButton_3.setText(_translate("MainWindow", "Setting"))
        self.pushButton_4.setText(_translate("MainWindow", "Recipt"))
        #self.pushButton_5.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.pushButton.clicked.connect(self.open_new_window)
        self.pushButton_2.clicked.connect(self.open_new_window2)
        self.pushButton_3.clicked.connect(self.open_new_window4)
        self.pushButton_4.clicked.connect(self.open_new_window5)
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        self.pushButton_6.clicked.connect(self.shutdown_system)
        self.pushButton_7.clicked.connect(self.reboot_system)
        self.anydesk_open()
     
    def shutdown_system(self):
        os.system("sudo shutdown -P 0")
        
    def reboot_system(self):
        os.system("sudo reboot")
    
    def anydesk_open(self):
        self.anydesk_id =0
        os.system("anydesk --get-id >> anydes_id_f.txt")
        f = open('anydes_id_f.txt','r')
        for line in f:                 
                    self.anydesk_id = line[0:9]
        print("self.anydesk_id:"+str(self.anydesk_id))
        self.label_4_1.setText("AnyDesk ID:"+str(self.anydesk_id))
        f.close()
        
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))

    def open_new_window(self):                
        f = open("/var/local/devid", "r")
        dev_id=f.read()
        f.close()
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("services.db")
        results=connection.execute("select DEVICE_SERIAL_NO from DAT_MST") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))
           if(serial_no == str(x[0])):
               self.go_ahead="Yes"
           else:
               self.go_ahead="No"
               
        if(self.go_ahead=="Yes"):       
            if(dev_id=='201910:0003'):            
                connection = sqlite3.connect("services.db")
                results=connection.execute("select DAT_STR from DAT_MST") 
                for x in results:
                    #print("DATE Str :"+str(x[0]))
                    DAT_DT=datetime.datetime.strptime(str(x[0]),"%Y-%m-%d").date()
                    CURR_DT=datetime.date.today()                
                    
                    #print("date dt :"+str(DAT_DT))
                    #print("curr dt :"+str(CURR_DT))                
                    if(DAT_DT > CURR_DT):        
                            self.window = QtWidgets.QMainWindow()
                            self.ui=wt_04_1_Ui_MainWindow()
                            self.ui.setupUi(self.window)           
                            self.window.show()        
                    else:
                        print("DAT date problem.")
                connection.close()         
            else:
                print("dev id :"+str(dev_id))
        else:
           print("Device Invalid :"+str(serial_no))
       
            
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_02_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()   
        
    
    def open_new_window4(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_10_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()     
    
    def open_new_window5(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_05_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
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
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
