# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ur_03_ADMIN_MENU.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ur_04_ADMIN_ORG import ur_04_Ui_MainWindow
from ur_05_ADMIN_USERS import ur_05_Ui_MainWindow
from ur_08_factory_reset import ur_08_Ui_MainWindow
from ur_10_datetime import ur_10_Ui_MainWindow
from ur_09_change_password import ur_09_Ui_MainWindow
from ur_11_register import ur_11_Ui_MainWindow
#from ur_12_admin_reports import ur_12_Ui_MainWindow
from ur_13_calibration import ur_13_Ui_MainWindow
import datetime
import sqlite3
import sys,os


class ur_03_A_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 711))
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(490, 40, 281, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(1110, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(140, 160, 271, 71))
        self.toolButton_3.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.frame)
        self.toolButton_4.setGeometry(QtCore.QRect(530, 160, 271, 71))
        self.toolButton_4.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.frame)
        #self.toolButton_5.setEnabled(False)
        self.toolButton_5.setGeometry(QtCore.QRect(910, 160, 271, 71))
        self.toolButton_5.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_5.setFont(font)
        self.toolButton_5.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.frame)
        #self.toolButton_6.setEnabled(False)
        self.toolButton_6.setGeometry(QtCore.QRect(140, 280, 271, 71))
        self.toolButton_6.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_6.setFont(font)
        self.toolButton_6.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_11 = QtWidgets.QToolButton(self.frame)
        #self.toolButton_11.setEnabled(False)
        self.toolButton_11.setGeometry(QtCore.QRect(530, 280, 271, 71))
        self.toolButton_11.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_11.setFont(font)
        self.toolButton_11.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_11.setObjectName("toolButton_11")
        self.toolButton_12 = QtWidgets.QToolButton(self.frame)
        #self.toolButton_12.setEnabled(False)
        self.toolButton_12.setGeometry(QtCore.QRect(910, 280, 271, 71))
        self.toolButton_12.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_12.setFont(font)
        self.toolButton_12.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_12.setObjectName("toolButton_12")
        self.toolButton_13 = QtWidgets.QToolButton(self.frame)
        #self.toolButton_13.setEnabled(False)
        self.toolButton_13.setGeometry(QtCore.QRect(910, 520, 271, 71))
        self.toolButton_13.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_13.setFont(font)
        self.toolButton_13.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_13.setObjectName("toolButton_13")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(10, 620, 101, 71))
        self.toolButton.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/backword1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(100, 100))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_14 = QtWidgets.QToolButton(self.frame)
        self.toolButton_14.setEnabled(False)
        self.toolButton_14.setGeometry(QtCore.QRect(530, 400, 271, 71))
        self.toolButton_14.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_14.setFont(font)
        self.toolButton_14.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_14.setObjectName("toolButton_14")
        self.toolButton_15 = QtWidgets.QToolButton(self.frame)
        self.toolButton_15.setEnabled(False)
        self.toolButton_15.setGeometry(QtCore.QRect(140, 400, 271, 71))
        self.toolButton_15.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_15.setFont(font)
        self.toolButton_15.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_15.setObjectName("toolButton_15")
        self.toolButton_16 = QtWidgets.QToolButton(self.frame)
        self.toolButton_16.setEnabled(False)
        self.toolButton_16.setGeometry(QtCore.QRect(910, 400, 271, 71))
        self.toolButton_16.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_16.setFont(font)
        self.toolButton_16.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_16.setObjectName("toolButton_16")
        self.toolButton_17 = QtWidgets.QToolButton(self.frame)
        self.toolButton_17.setEnabled(False)
        self.toolButton_17.setGeometry(QtCore.QRect(140, 520, 271, 71))
        self.toolButton_17.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_17.setFont(font)
        self.toolButton_17.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_17.setObjectName("toolButton_17")
        self.toolButton_18 = QtWidgets.QToolButton(self.frame)
        #self.toolButton_18.setEnabled(False)
        self.toolButton_18.setGeometry(QtCore.QRect(530, 520, 271, 71))
        self.toolButton_18.setStyleSheet("background-color: rgb(255, 220, 212);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.toolButton_18.setFont(font)
        self.toolButton_18.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_18.setObjectName("toolButton_18")
        
        
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(990, 10, 90, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)        
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("Shutdown")
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(890, 10, 90, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)        
        self.pushButton_7.setFont(font)
        self.pushButton_7.setText("Reboot")
        self.pushButton_7.setObjectName("pushButton_7")
        
        self.label_4_1 = QtWidgets.QLabel(self.frame)
        self.label_4_1.setGeometry(QtCore.QRect(1050, 650, 161, 26))
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
        self.label_31.setText(_translate("MainWindow", "Administration"))
        self.label_30.setText(_translate("MainWindow", "16 JAN 2020 12:14:15"))
        self.toolButton_3.setText(_translate("MainWindow", "Organisation Details"))
        self.toolButton_4.setText(_translate("MainWindow", "Doctors Details"))
        self.toolButton_5.setText(_translate("MainWindow", "Factory Reset"))
        self.toolButton_6.setText(_translate("MainWindow", "Calibrations"))
        self.toolButton_11.setText(_translate("MainWindow", "Date Time Setting"))
        self.toolButton_12.setText(_translate("MainWindow", "Change Passwords"))
        self.toolButton_13.setText(_translate("MainWindow", "Register Device"))
        self.toolButton_14.setText(_translate("MainWindow", "Wifi Setting"))
        self.toolButton_15.setText(_translate("MainWindow", "Printer Setting"))
        self.toolButton_16.setText(_translate("MainWindow", "Data Backup"))
        self.toolButton_17.setText(_translate("MainWindow", "SMS Configuration"))
        self.toolButton_18.setText(_translate("MainWindow", "System Reports"))
        self.toolButton_18.setDisabled(True)
        self.toolButton.clicked.connect(MainWindow.close)
        self.toolButton_3.clicked.connect(self.open_new_window)
        self.toolButton_4.clicked.connect(self.open_new_window2)
        self.toolButton_5.clicked.connect(self.open_new_window3)
        self.toolButton_11.clicked.connect(self.open_new_window4)
        self.toolButton_12.clicked.connect(self.open_new_window5)
        self.toolButton_13.clicked.connect(self.open_new_window6)
        #self.toolButton_18.clicked.connect(self.open_new_window7)
        self.toolButton_6.clicked.connect(self.open_new_window8)
        
        self.pushButton_6.clicked.connect(self.shutdown_system)
        self.pushButton_7.clicked.connect(self.reboot_system)
        self.anydesk_open()        
        self.register_button()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        
    
    def device_date(self):     
        self.label_30.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
     
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
        
    def register_button(self):
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("services.db")
        results=connection.execute("select DEVICE_SERIAL_NO from DAT_MST") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))
           if(serial_no == str(x[0])):
               #self.go_ahead="Yes"
               self.toolButton_13.hide()
           else:
               #self.go_ahead="No"
               self.toolButton_13.show()
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

    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()      
        self.ui=ur_04_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()      
        self.ui=ur_05_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window3(self):       
        self.window = QtWidgets.QMainWindow()      
        self.ui=ur_08_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window4(self):       
        self.window = QtWidgets.QMainWindow()      
        self.ui=ur_10_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window5(self):       
        self.window = QtWidgets.QMainWindow()      
        self.ui=ur_09_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window6(self):       
        self.window = QtWidgets.QMainWindow()      
        self.ui=ur_11_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
   
    
    def open_new_window8(self):       
        self.window = QtWidgets.QMainWindow()      
        self.ui=ur_13_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show() 
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ur_03_A_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
