

from MDR_03_SYSTEM import mdr_03_Ui_MainWindow
from MDR_04_METHODS import mdr_04_Ui_MainWindow

from register import reg_Ui_MainWindow
from email_setup import email_setup_Ui_MainWindow
from date_time_setup import datetime_set_Ui_MainWindow
from callibration_process import calibration_Ui_MainWindow
from factory_reset import factory_reset_Ui_MainWindow



from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3


class mdr_02_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 40, 1261, 671))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 261, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 390, 261, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(390, 20, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 85, 127);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 610, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(0, 85, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 610, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(0, 85, 127);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(430, 610, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(420, 90, 321, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 240, 261, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(830, 90, 321, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(830, 240, 321, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(830, 390, 321, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(420, 240, 321, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(420, 390, 321, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 610, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(0, 85, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1150, 630, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(0, 85, 127);")
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Methods"))
        self.pushButton_4.setText(_translate("MainWindow", "System"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45 "))
        self.pushButton_2.setText(_translate("MainWindow", "Shutdown"))
        self.pushButton_5.setText(_translate("MainWindow", "Reboot"))
        self.label_21.setText(_translate("MainWindow", "AnyDesk Id: 456533323"))
        self.pushButton_7.setText(_translate("MainWindow", "Email-Setup"))
        self.pushButton_8.setText(_translate("MainWindow", "Graph Setup"))
        self.pushButton_8.setDisabled(True)
        self.pushButton_10.setText(_translate("MainWindow", "Torque-Calibration"))
        self.pushButton_11.setText(_translate("MainWindow", "Temp1-Calibration"))
        self.pushButton_11.setDisabled(True)
        self.pushButton_12.setText(_translate("MainWindow", "Temp2-Calibration"))
        self.pushButton_12.setDisabled(True)
        self.pushButton_9.setText(_translate("MainWindow", "Date-Time Setup"))
        self.pushButton_13.setText(_translate("MainWindow", "Factory Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.pushButton_6.setText(_translate("MainWindow", "Register"))
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.register_button()
        self.pushButton_2.clicked.connect(self.shutdown_system)
        self.pushButton_5.clicked.connect(self.reboot_system)
        self.pushButton_6.clicked.connect(self.open_new_window)
        self.pushButton_7.clicked.connect(self.open_email_setup_window)
        self.pushButton_9.clicked.connect(self.open_datetime_setup_window)
        self.pushButton_10.clicked.connect(self.open_callibration_window)
        self.pushButton_13.clicked.connect(self.open_factoryReset_window)
        self.pushButton_4.clicked.connect(self.open_system_window)
        self.pushButton.clicked.connect(self.open_methods_window)
        
        self.anydesk_open()
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
       
    
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=reg_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_email_setup_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=email_setup_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_datetime_setup_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=datetime_set_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_callibration_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=calibration_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_factoryReset_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=factory_reset_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_methods_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=mdr_04_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_system_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=mdr_03_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show() 
        
    def register_button(self):
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("select DEVICE_SERIAL_NO from GLOBAL_VAR") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))
           if(serial_no == str(x[0])):
               #self.go_ahead="Yes"
               self.pushButton_6.hide()
           else:
               #self.go_ahead="No"
               self.pushButton_6.show()
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
        self.label_21.setText("<font color=blue> AnyDesk ID: </font> "+str(self.anydesk_id))
        f.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mdr_02_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
