

from PyQt5 import QtCore, QtGui, QtWidgets
from TY_12_TEST_LIST import TY_12_LIST_Ui_MainWindow
#from TY_00_TEST_TYPES import TY_00_T_Ui_MainWindow
from TY_03_REPORTS import TY_03_Ui_MainWindow
from TY_04_SETTING import TY_04_Ui_MainWindow
from TY_05_SPECIMEN_2 import TY_05_Ui_MainWindow
from TY_07_UTM_MANNUAL_CONTROL import TY_07_Ui_MainWindow
from TY_18_TEST_TYPE_REPORTS import TY_18_TEST_TYPE_REPORTS_Ui

import sqlite3
import datetime

import time
from PyQt5.QtCore import QDate
import sys,os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 70, 1161, 631))
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        
        self.frame.setObjectName("frame")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 310, 191, 181))
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/motor5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(200, 160))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 310, 201, 181))
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/sample.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(200, 160))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(100, 50, 201, 181))
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/test.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(200, 160))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 50, 191, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/report3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(200, 160))
        self.pushButton_2.setObjectName("pushButton_2")
        
        
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(760, 310, 201, 181))
        self.pushButton_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QtCore.QSize(200, 160))
        self.pushButton_3.setObjectName("pushButton_3")
        
        
        
        self.pushButton_3_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3_1.setGeometry(QtCore.QRect(730, 50, 410, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3_1.setFont(font)
        self.pushButton_3_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3_1.setIcon(icon2)
        self.pushButton_3_1.setIconSize(QtCore.QSize(400, 460))
        self.pushButton_3_1.setObjectName("pushButton_3_1")
        
        
        
        
        
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(830, 420, 191, 181))
        self.label_3.setText("Setting")
        self.label_3.setObjectName("label_3")
        
        self.label_3_1 = QtWidgets.QLabel(self.frame)
        self.label_3_1.setGeometry(QtCore.QRect(530, 420, 191, 181))
        self.label_3_1.setText("Motor")
        self.label_3_1.setObjectName("label_3_1")
        
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(810, 550, 90, 26))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)        
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("Shutdown")
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(910, 550, 90, 26))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)        
        self.pushButton_7.setFont(font)
        self.pushButton_7.setText("Reboot")
        self.pushButton_7.setObjectName("pushButton_7")
        
       
        self.label_4_1 = QtWidgets.QLabel(self.frame)
        self.label_4_1.setGeometry(QtCore.QRect(810, 590, 361, 126))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        #font.setBold(False)
        #font.setWeight(75)
        self.label_4_1.setFont(font)
        #self.label_4_1.setStyleSheet("color: rgb(0, 0, 255);color: rgb(170, 0, 0);")
        self.label_4_1.setAlignment(QtCore.Qt.AlignLeft)
        self.label_4_1.setObjectName("label_4_1")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reports"))
        self.pushButton.clicked.connect(self.open_new_window)
        self.pushButton_2.clicked.connect(self.open_new_window2)
        self.pushButton_3.clicked.connect(self.open_new_window3)
        self.pushButton_4.clicked.connect(self.open_new_window4)
        self.pushButton_5.clicked.connect(self.open_new_window5)
        
        self.pushButton_6.clicked.connect(self.shutdown_system)
        self.pushButton_7.clicked.connect(self.reboot_system)
        self.anydesk_open()
     
    def shutdown_system(self):
        os.system("sudo shutdown -P 0")
        
    def reboot_system(self):
        os.system("sudo reboot")
    
    def anydesk_open(self):
        self.anydesk_id =0
        os.system("rm -rf anydes_id_f.txt")
        os.system("anydesk --get-alias>> anydes_id_f.txt")
        f = open('anydes_id_f.txt','r')
        for line in f:                 
                    self.anydesk_id = line[0:29]
        print("self.anydesk_id:"+str(self.anydesk_id))
        self.label_4_1.setText("<font color=blue> AnyDesk ID: </font> "+str(self.anydesk_id))
        f.close()
        
    def open_new_window(self):        
        f = open("/var/local/devid", "r")
        dev_id=f.read()
        f.close()
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select DEVICE_SERIAL_NO from GLOBAL_REPORTS_PARAM") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))
           if(serial_no == str(x[0])):
               self.go_ahead="Yes"
           else:
               self.go_ahead="No"
        connection.close()
        if(self.go_ahead=="Yes"):  
            if(str(dev_id)[0:11]=='201910:0003'):
                self.window = QtWidgets.QMainWindow()
                self.ui=TY_12_LIST_Ui_MainWindow()
                self.ui.setupUi(self.window)           
                self.window.show()        
            else:
                print("dev id :"+str(dev_id)[0:11])   
        else:
           print("Device Invalid :"+str(serial_no))
        
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_18_TEST_TYPE_REPORTS_Ui()
        self.ui.setupUi(self.window)           
        self.window.show()        
        
    def open_new_window3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_04_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_05_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def open_new_window5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_07_Ui_MainWindow()
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
