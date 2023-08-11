
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


class  TY_07_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        #self.frame.setGeometry(QtCore.QRect(30, 20, 1321, 691))
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 709))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(880, 340, 191, 211))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/down.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(500, 1000))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(160, 340, 171, 221))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/up1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(500, 1000))
        self.toolButton_2.setObjectName("toolButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)
        self.lineEdit.setValidator(input_validator)
        self.lineEdit.setGeometry(QtCore.QRect(480, 190, 241, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 170, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 200, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 0, 127);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(470, 340, 261, 221))
        self.toolButton_3.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"background-color: rgb(247, 255, 226);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/stop1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(500, 1000))
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(320, 600, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(255, 231, 254);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(1040, 50, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(255, 231, 254);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(760, 200, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(410, 60, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 85, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.rev_speed_val=0
        
        
        self.speed_val=""
        self.input_speed_val=""
        self.goahead_flag=0
        self.calc_speed=0
        self.command_str=""
        
        self.is_active_modbus='N'
        self.modbus_port=""
        self.non_modbus_port=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Enter Speed :"))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Empty Or Invalid speed !!."))        
        self.pushButton.setText(_translate("MainWindow", "Speed Setup"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.label_3.setText(_translate("MainWindow", "(mm/min) "))
        self.label_4.setText(_translate("MainWindow", "Manual Control of Motor"))
        self.pushButton_2.clicked.connect(MainWindow.close)       
        self.toolButton.clicked.connect(self.r_run)   #down
        self.toolButton_2.clicked.connect(self.f_run) #up
        self.toolButton_3.clicked.connect(self.stop_run)
        self.pushButton.clicked.connect(self.open_new_window)
        
        self.label_2.hide()
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
        self.label_2.show() 
        self.input_speed_val=str(self.lineEdit.text())
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
                 self.label_2.setText("Running with "+str(round(self.display_calc_speed,2))+"% speed of maximum speed :"+str(self.speed_val)+" (mm/min).")
                 self.label_2.show()
                 print("Validation of Speed Successfull")
            else:
                 #print(" not Ok ")
                 #self.label_2.show()
                 self.label_2.setText("Speed Should not more than MAX Speed:"+str(self.speed_val))
                 self.label_2.show()
        else:
            self.label_2.show()
            
        
         
        
        
        
        
        
        
            
            
        
    def r_run(self):
        print("Reverse Run started ....")
        self.validate_speed()

        
        ###################################################################################       
        #####  self.is_active_modbus : this status us detected in validate_speed function.
        #####  self.modbus_port : this status us detected in load_modbus_port function.        
        ###################################################################################
        
        #print("self.is_active_modbus:"+str(self.is_active_modbus)+"  self.modbus_port:"+str(self.modbus_port))
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
                    #print(" write2 :"+str(v))
                    print("Reverse speed : "+str(v)+" is set successfully in the PLC via Modbus.")
                except IOError as e:
                    print("Set Speed Error 02 - Reverse-Write Modbus IO Error -Motor start : "+str(e))
                
        else:
            print("Set Speed Error 01 : Modbus is not active or modbus port is not detected.")
        
        
        ######################################################################       
        #####  
        #####  Above is the setting of speed if PLC is connected
        ###### Reverse Run the Motor Below
        ###### self.command_str : This is detected in validate_speed function
        ######
        #######################################################################
        
        time.sleep(1)
        
        
        try:
           #print("is_active_modbus [Reverse] :"+str(self.is_active_modbus))
           if(self.is_active_modbus == 'Y'):
               #print("rev non modbus port :"+str(self.non_modbus_port))
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
                       #print("non modbus port :"+str(self.non_modbus_port))
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
                print("Reverse command Started.")
           else:
                print("Reverse command not Started. Please Check.")
        except IOError:
            print(print("IO Errors(Reverse): Please check motor connection is active ?")    )  
       
        
    def f_run(self):
        print("Forward Run ....")
        self.validate_speed()
        #self.label_2.hide()
#         self.toolButton.show()
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap("./images/up1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
#         self.toolButton.setIcon(icon)
#         self.toolButton.setIconSize(QtCore.QSize(70, 141))
        ######################################################################       
        #####  self.is_active_modbus : this status us detected in validate_speed function.
        #####  self.modbus_port : this status us detected in load_modbus_port function.
        ###################################################################################
        
        #print("self.is_active_modbus:"+str(self.is_active_modbus)+"  self.modbus_port:"+str(self.modbus_port))
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
                    #print(" write1 :"+str(v))
                    print("Forword speed : "+str(v)+" is set successfully in the PLC via Modbus.")
                except IOError as e:
                    print("Forward-Write Modbus IO Error 02  -Motor start : "+str(e))
                #print("Forward speed : "+str(v))
        else:
            print("Set Speed Error 01 : Modbus is not active or modbus port is not detected.")
        ######################################################################       
        #####  
        #####  Above is the setting of speed if PLC is connected
        ###### Forword Run the Motor Below
        ###### self.command_str : This is detected in validate_speed function
        ######
        #######################################################################
        
        time.sleep(1)
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
                print("Forword command executed. ")
            else:
                print("Forword command not Started. Please Check.")
         
        except IOError:
           print("IO Errors(Forward): Please check motor connection is active ?")    
                
    
    def stop_run(self):
        #print("Forward Run ....")
        self.label_2.hide()
        #self.toolButton.hide()
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
            print("Stop command executed. ")
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

