

from SPEED_SETUP_POPUP import spped_setup_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
import serial,time
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

import sqlite3
import re
import datetime
import time
import os,sys

import minimalmodbus
#from minimalmodbus import BYTEORDER_LITTLE_SWAP
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
minimalmodbus.BYTEORDER_BIG= 0
minimalmodbus.BYTEORDER_LITTLE= 1


class TY_07_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        MainWindow.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 60, 1230, 661))
        self.frame.setStyleSheet("")
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.frame.setObjectName("frame")
        self.speed_val=""
        self.input_speed_val=""
        self.goahead_flag=0
        self.calc_speed=0
        self.command_str=""
        self.modbus_port=""
        self.non_modbus_port=""
        
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(430, 40, 351, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(180, 150, 831, 311))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        #self.groupBox_3.setStyleSheet("background-color: rgb(214, 253, 204);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(150, 90, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        
        
        self.label_9_1 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9_1.setGeometry(QtCore.QRect(150, 40, 471, 31))
        self.label_9_1.setStyleSheet("color: rgb(0, 85, 255);")
        font = QtGui.QFont()
        
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        self.label_9_1.setFont(font)
        self.label_9_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9_1.setObjectName("label_9_1")
        
        
        
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        #reg_ex = QRegExp("\d+")
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_7)
        self.lineEdit_7.setValidator(input_validator)
        
        self.lineEdit_7.setMaxLength(7)
        self.lineEdit_7.setGeometry(QtCore.QRect(330, 90, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_14.setGeometry(QtCore.QRect(630, 190, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        
        self.pushButton_14_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14_1.setGeometry(QtCore.QRect(20, 35, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_14_1.setFont(font)       
        self.pushButton_14_1.setObjectName("pushButton_14_1")
        
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(250, 310, 70, 97))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/up1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(70, 141))
        self.toolButton.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.toolButton.setObjectName("toolButton")
        self.toolButton.hide()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.rev_speed_val=0
        self.is_active_modbus='N'

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "UTM Mannual Control"))
        self.label_9.setText(_translate("MainWindow", "Motor Speed (RPM) :"))
        self.label_9_1.setText(_translate("MainWindow", "Empty Or Invalid speed"))
        self.pushButton_5.setText(_translate("MainWindow", "Forward"))
        self.pushButton_2.setText(_translate("MainWindow", "Reverse"))
        self.pushButton_6.setText(_translate("MainWindow", "Stop"))
        self.pushButton_14.setText(_translate("MainWindow", "Return"))
        self.pushButton_14_1.setText("Setup Motor Speed.")
        self.pushButton_14.clicked.connect(MainWindow.close)       
        self.pushButton_2.clicked.connect(self.r_run)
        self.pushButton_5.clicked.connect(self.f_run)
        self.pushButton_6.clicked.connect(self.stop_run)
        self.pushButton_14_1.clicked.connect(self.open_new_window)
        
        self.label_9_1.hide()
        self.load_modbus_port()
        
    def validate_speed(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT IFNULL(MOTOR_MAX_SPEED,0),ISACTIVE_MODBUS from SETTING_MST") 
        for x in results:
             self.speed_val=str(x[0])
             self.is_active_modbus=str(x[1])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT IFNULL(NEW_TEST_MOTOR_REV_SPEED,0) from GLOBAL_VAR") 
        for x in results:
             self.rev_speed_val=str(x[0])
        connection.close()
        
        
        
        
        self.goahead_flag=0
        self.label_9_1.show() 
        self.input_speed_val=str(self.lineEdit_7.text())
        if(self.input_speed_val != ""):
            if(float(self.input_speed_val) <= float(self.speed_val)):
                 #print(" Ok ")
                 self.goahead_flag=1
                 self.calc_speed=(float(self.input_speed_val)/int(self.speed_val))*1000                 
                 #print(" calc Speed : "+str(self.calc_speed))
                 #print(" command: *P"+str(self.calc_speed)+"\r")
                 self.command_str="*P%04d"%self.calc_speed+"\r"
                 #self.command_str="*P50.00\r"
                 #print("xcxcx :"+str(self.command_str))
                 self.display_calc_speed=float(self.calc_speed)/10
                 self.label_9_1.setText("Running with "+str(round(self.display_calc_speed,2))+"% speed of maximum speed ("+str(self.speed_val)+" rpm).")
                 self.label_9_1.show()
                 #print("ok-done")
            else:
                 #print(" not Ok ")
                 #self.label_9_1.show()
                 self.label_9_1.setText("Speed Should not more than MAX Speed:"+str(self.speed_val))
                 self.label_9_1.show()
        else:
            self.label_9_1.show()
            
        
         
        
        
        
        
        
        
            
            
        
    def r_run(self):
        #print("Reverse Run ....")
        self.validate_speed()
        #self.label_9_1.hide()
        self.toolButton.show()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/down.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(70, 141))
        try:
           print("rev is_active_modbus :"+str(self.is_active_modbus))
           if(self.is_active_modbus == 'Y'):
               print("rev non modbus port :"+str(self.non_modbus_port))
               if(self.non_modbus_port=="/dev/ttyUSB0"):
                       self.ser = serial.Serial(
                            port='/dev/ttyUSB0',
                            baudrate=19200,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            xonxoff=False,
                            timeout = 0.25
                        )
                       print("non modbus port :"+str(self.non_modbus_port))
               else:
                        self.ser = serial.Serial(
                            port='/dev/ttyUSB1',
                            baudrate=19200,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            xonxoff=False,
                            timeout = 0.25
                        )
           else:
               self.ser = serial.Serial(
                            port='/dev/ttyUSB0',
                            baudrate=19200,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            xonxoff=False,
                            timeout = 0.25
                        )
           self.ser.flush()
           if(self.goahead_flag==1):
                b = bytes(self.command_str, 'utf-8')
                self.ser.write(b)
                self.ser.write(b'*R\r')
           else:
                print("No go Ahead !!!!!")
           
           
        except IOError:
            print("IO Errors")    
        #time.sleep(1)
        if(self.is_active_modbus == 'Y' and self.modbus_port != ""): 
                v=float(self.input_speed_val)
                try:
                    if(self.modbus_port=="/dev/ttyUSB1"):
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) # port name, slave address (in decimal)
                    else:
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # port name, slave address (in decimal)
                    instrument.serial.timeout = 1
                    instrument.serial.baudrate = 9600
                    
                    v=v*40
                    if(float(v) < 1 ):
                        v=1.0
                    elif(float(v)== 1 ):
                        v=1.0
                    else:
                        v=round(v,0)
                    
                    instrument.write_register(4096,v,0) ###self.input_speed_val RPM
                    instrument.write_register(4097,0,0) ###self.input_speed_val RPM
                    print(" write2 :"+str(v))
                except IOError as e:
                    print("Reverse-Write Modbus IO Error -Motor start : "+str(e))
                
                print("Reverse speed : "+str(v))
        
    def f_run(self):
        print("Forward Run ....")
        self.validate_speed()
        #self.label_9_1.hide()
        self.toolButton.show()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/up1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(70, 141))
        try:
            if(self.is_active_modbus == 'Y'): 
                       if(self.non_modbus_port=="/dev/ttyUSB0"):
                               self.ser = serial.Serial(
                                    port='/dev/ttyUSB0',
                                    baudrate=19200,
                                    bytesize=serial.EIGHTBITS,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    xonxoff=False,
                                    timeout = 0.25
                                )
                       else:
                               self.ser = serial.Serial(
                                    port='/dev/ttyUSB1',
                                    baudrate=19200,
                                    bytesize=serial.EIGHTBITS,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    xonxoff=False,
                                    timeout = 0.25
                                )
            else:
                       self.ser = serial.Serial(
                                    port='/dev/ttyUSB0',
                                    baudrate=19200,
                                    bytesize=serial.EIGHTBITS,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    xonxoff=False,
                                    timeout = 0.25
                                )  
            if(self.goahead_flag==1):               
                b = bytes(self.command_str, 'utf-8')
                self.ser.write(b)
                self.ser.write(b'*F\r')
            else:
                print("No go Ahead !!!!!")
          
           #time.sleep(1)
        except IOError:
           print("IO Errors")     
        
        if(self.is_active_modbus == 'Y' and self.modbus_port != ""): 
                v=float(self.input_speed_val)
                try:     
                    if(self.modbus_port=="/dev/ttyUSB1"):
                                    instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) # port name, slave address (in decimal)
                    else:
                                    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # port name, slave address (in decimal)
                    instrument.serial.timeout = 1
                    instrument.serial.baudrate = 9600
                    
                    v=v*40
                    if(float(v) < 1 ):
                        v=1.0
                    elif(float(v)== 1 ):
                        v=1.0
                    else:
                        v=round(v,0)
                        
                    instrument.write_register(4098,v,0) ###self.input_speed_val RPM
                    instrument.write_register(4099,0,0) ###self.input_speed_val RPM
                    print(" write1 :"+str(v))
                except IOError as e:
                    print("Forward-Write Modbus IO Error -Motor start : "+str(e))
                print("Forward speed : "+str(v))
    
    def stop_run(self):
        #print("Forward Run ....")
        self.label_9_1.hide()
        self.toolButton.hide()
        try:
            if(self.is_active_modbus == 'Y'):            
                   if(self.non_modbus_port=="/dev/ttyUSB0"):
                           self.ser = serial.Serial(
                                port='/dev/ttyUSB0',
                                baudrate=19200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.25
                            )
                   else:
                          self.ser = serial.Serial(
                                port='/dev/ttyUSB1',
                                baudrate=19200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.25
                            )
            else:
                          self.ser = serial.Serial(
                                port='/dev/ttyUSB0',
                                baudrate=19200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.25
                            )
           
            self.ser.write(b'*Q\r')
           #time.sleep(1)
        except IOError:
           print("IO Errors")
           
    
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=spped_setup_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    
    def get_USB_0_DEVICE(self):
        os.system("rm -rf lsusb_USB0.txt")
        port_type="ERROR"
        
        ### Check for Controller #######
        os.system("udevadm info /dev/ttyUSB0 | grep PL2303 >> lsusb_USB0.txt")
        try:
           f = open('lsusb_USB0.txt','r')
           for line in f:
               cnt=0                
               cnt=int(line.find("PL2303")) ## For controller Port
               if cnt > 0 :
                    port_type="C"
               else:
                    port_type="ERROR"  
                   
           f.close()
        except:          
             port_type="ERROR"     
        
        
        if(port_type == "ERROR"):
        
                #### Check For Modbus ########
                os.system("udevadm info /dev/ttyUSB0 | grep Future >> lsusb_USB0.txt")
                try:
                   f = open('lsusb_USB0.txt','r')
                   for line in f:
                       cnt=0                
                       cnt=int(line.find("Future")) ## For controller Port
                       if cnt > 0 :
                            port_type="M"
                       else:
                            port_type="ERROR"     
                   f.close()
                except:          
                      port_type="ERROR"
                   
         
        return port_type
    
    
    def get_USB_1_DEVICE(self):
        os.system("rm -rf lsusb_USB1.txt")
        port_type="ERROR"
        
        ### Check for Controller #######
        os.system("udevadm info /dev/ttyUSB1 | grep PL2303 >> lsusb_USB1.txt")
        try:
           f = open('lsusb_USB1.txt','r')
           for line in f:
               cnt=0                
               cnt=int(line.find("PL2303")) ## For controller Port
               if cnt > 0 :
                    port_type="C"
               else:
                    port_type="ERROR"  
                   
           f.close()
        except:          
             port_type="ERROR"     
        
        
        if(port_type == "ERROR"):
        
                #### Check For Modbus ########
                os.system("udevadm info /dev/ttyUSB1 | grep Future >> lsusb_USB1.txt")
                try:
                   f = open('lsusb_USB1.txt','r')
                   for line in f:
                       cnt=0                
                       cnt=int(line.find("Future")) ## For controller Port
                       if cnt > 0 :
                            port_type="M"
                       else:
                            port_type="ERROR"     
                   f.close()
                except:          
                      port_type="ERROR"
                   
         
        return port_type
    
        
    def load_modbus_port(self):
        self.modbus_port=""
        self.non_modbus_port=""
        self.port=""        
        connection = sqlite3.connect("tyr.db") 
        results=connection.execute("SELECT ISACTIVE_MODBUS FROM SETTING_MST") 
        for x in results:
                   if(str(x[0]) == 'Y'):                       
                        self.port=self.get_USB_0_DEVICE()
                        print("USB0: "+str(self.port))
                        if(self.port == "C"):
                             self.non_modbus_port="/dev/ttyUSB0"
                        elif(self.port == "M"):
                             self.modbus_port="/dev/ttyUSB0"
                        else:                             
                             print("Error 468")  
                            
                        
                        print("USB0: "+str(self.port)+" non_modbus: "+(self.non_modbus_port))     
                        
                        self.port=self.get_USB_1_DEVICE()
                        
                        if(self.port == "C"):
                             self.non_modbus_port="/dev/ttyUSB1"
                        elif(self.port == "M"):
                             self.modbus_port="/dev/ttyUSB1"
                        else:
                             print("Error 480")        
                   else:
                         print("Modbus Flag :"+str(x[0]))                       
        connection.close()
        
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE SETTING_MST SET MODBUS_PORT='"+str(self.modbus_port)+"',NON_MODBUS_PORT='"+str(self.non_modbus_port)+"'")            
        connection.commit();

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_07_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
