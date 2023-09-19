
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


class  AE_MANUAL_CONTROL_Ui_MainWindow(object):
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
        font.setPointSize(26)
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
        font.setPointSize(26)
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
        self.test_method=1 #Tensile
        self.load_cell_no=1 #Get Load Cell No
        self.test_speed=0#This is Test Speed. 
        self.test_id=-99
        self.login_user_role="Manual Contol Log"
        self.cycle_num=0
        self.max_speed=1
        self.per_test_speed=0       
        
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
        #self.pushButton.hide()
        self.pushButton_2.setText(_translate("MainWindow", "Return"))
        self.label_3.setText(_translate("MainWindow", "(mm/min) "))
        self.label_4.setText(_translate("MainWindow", "Manual Control of Motor"))
        self.pushButton_2.clicked.connect(MainWindow.close)       
        self.toolButton.clicked.connect(self.down_run)   #down
        self.toolButton_2.clicked.connect(self.up_run) #up
        self.toolButton_3.clicked.connect(self.stop_run)
        self.pushButton.clicked.connect(self.open_new_window)        
        self.label_2.hide()
    
    def record_modbus_logs(self,test_id,cycle_num,set_or_get,log_str,user_name):
        connection = sqlite3.connect("tyr.db")
        with connection:        
            cursor = connection.cursor()
            print("INSERT INTO MODBUS_LOGS(TEST_ID,CYCLE_NUM,SET_OR_GET,LOG_STR,USER_NAME) VALUES(?,?,?,?,?)",(test_id,cycle_num,set_or_get,log_str,user_name))
            cursor.execute("INSERT INTO MODBUS_LOGS(TEST_ID,CYCLE_NUM,SET_OR_GET,LOG_STR,USER_NAME) VALUES(?,?,?,?,?)",(test_id,cycle_num,set_or_get,log_str,user_name))                         
        connection.commit();
        connection.close()
        
    def down_run(self): ## Down Direction
        if(str(self.lineEdit.text()) == ""):
                    self.label_2.setText("Speed is Empty")
                    self.label_2.show()
        else:
                    self.label_2.hide()                    
                    self.max_speed=1
                    self.per_test_speed=0
                    self.test_speed=float(str(self.lineEdit.text()))
                    #self.test_speed=int(float(self.test_speed))
                    
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT  MOTOR_MAX_SPEED FROM SETTING_MST LIMIT 1") 
                    for x in results:            
                        self.max_speed=int(x[0])                        
                    connection.close()
                    
                    self.per_test_speed=((float(self.test_speed)/float(self.max_speed))*100)
                    
                    print("Reverse Run started ....Speed :"+str(self.test_speed))
                        
                    try:
                            #instrument = minimalmodbus.Instrument('/dev/ttyACM0', 7,debug = True) # port name, slave address (in decimal)                   
                            self.instrument = minimalmodbus.Instrument('/dev/ttyACM0', 7) # port name, slave address (in decimal)
                            self.instrument.serial.timeout = 1
                            self.instrument.serial.baudrate = 115200
                            #time.sleep(5)
                            self.IO_error_flg=0
                    except IOError as e:
                            print("IO Errors- Connection to Modbus......:"+str(e))
                            self.IO_error_flg=1
                            self.label_2.setText("IO Error.")
                            self.label_2.show()
                    
                    if(self.IO_error_flg==0):                            
                            #Set Down Speed . Check For IO Error.
                            try:
                                            print("\n\n\n\n##### SET : rev test_speed ######")
                                            #self.instrument.write_register(REGISTER, NEW_VALUE, DECIMALS, functioncode=6, signed=True)
                                            self.instrument.write_register(11,int(self.per_test_speed),0,6)                                            
                                            #self.instrument.write_register(6,0,0)
                                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET test_speed :"+str(self.per_test_speed),self.login_user_role)
                                            #time.sleep(5)
                            except IOError as e:
                                            print("Ignore-Modbus Error- self.test_speed.:"+str(e))
                                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET test_speed :"+str(self.per_test_speed),self.login_user_role)
                                            time.sleep(5)
                                        
                            ####### Write in Coil Register.- Activate DOWN BIT ############
                            try:
                                                 #write_bit(registeraddress: int, value: int, functioncode: int = 5) → None[source]   
                                                 print("\n\n\n\n##### SET :COIL start_bit ######")
                                                 self.instrument.write_bit(3,1,5)                    
                                                 self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET DOWN BIT :1",self.login_user_role)
                                                 self.label_2.setText("Motor Started (Down) .......speed :"+str(self.lineEdit.text()))
                                                 self.label_2.show()
                                                  #time.sleep(5)
                            except IOError as e:
                                                 print("Ignore-Modbus Error- SET COIL DOWN BIT ..:"+str(e))
                                                 self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET COIL DOWN BIT : 1",self.login_user_role)
                                                 self.IO_error_flg=1 
                            #Start Motor DOWN Side .
                            
                    else:
                                    print("Modbus Error ......")   
           
       
        
    def up_run(self):    # Up Direction         
        if(str(self.lineEdit.text()) == ""):
                    self.label_2.setText("Speed is Empty")
                    self.label_2.show()
        else:
                    print("Up Run ....")
                    self.label_2.hide()                    
                    self.max_speed=1
                    self.per_test_speed=0
                    self.test_speed=float(str(self.lineEdit.text()))
                   
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT  MOTOR_MAX_SPEED FROM SETTING_MST LIMIT 1") 
                    for x in results:            
                        self.max_speed=int(x[0])                        
                    connection.close()                    
                    self.per_test_speed=((float(self.test_speed)/float(self.max_speed))*100)*100 
                    
                    print("Reverse Run started ....Speed :"+str(self.test_speed))
                    
                    try:
                            #instrument = minimalmodbus.Instrument('/dev/ttyACM0', 7,debug = True) # port name, slave address (in decimal)                   
                            self.instrument = minimalmodbus.Instrument('/dev/ttyACM0', 7) # port name, slave address (in decimal)
                            self.instrument.serial.timeout = 1
                            self.instrument.serial.baudrate = 115200
                            #time.sleep(5)
                            self.IO_error_flg=0
                    except IOError as e:
                            print("IO Errors- Connection to Modbus......:"+str(e))
                            self.IO_error_flg=1
                            self.label_2.setText("IO Error.")
                            self.label_2.show()
                    
                    if(self.IO_error_flg==0):                            
                            #Set Forwoard Speed . Check For IO Error.
                            try:
                                            print("\n\n\n\n##### SET : test_speed ######")
                                            #self.instrument.write_register(REGISTER, NEW_VALUE, DECIMALS, functioncode=6, signed=True)
                                            self.instrument.write_register(10,int(self.per_test_speed),0,6)
                                            #self.instrument.write_register(6,0,0)
                                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET test_speed :"+str(self.per_test_speed),self.login_user_role)
                                            #time.sleep(5)
                            except IOError as e:
                                            print("Ignore-Modbus Error- self.test_speed.:"+str(e))
                                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET test_speed :"+str(self.per_test_speed),self.login_user_role)
                                            time.sleep(5)
                                        
                            
                            
                            ####### Start Test-Write in Coil Register. ############
                            try:
                                            #write_bit(registeraddress: int, value: int, functioncode: int = 5) → None[source]   
                                            print("\n\n\n\n##### SET :COIL UP BIT 1  ######")
                                            self.instrument.write_bit(2,1,5)                    
                                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET COIL UP BIT  :1",self.login_user_role)
                                            self.label_2.setText("Motor Started (UP) .......speed :"+str(self.lineEdit.text()))
                                            self.label_2.show()
                                             #time.sleep(5)
                            except IOError as e:
                                            print("Ignore-Modbus Error- SET COIL UP BIT ..:"+str(e))
                                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET COIL UP BIT  :"+str(self.start_bit),self.login_user_role)
                                            self.IO_error_flg=1
                                           
                    
                    else:
                                    print("Modbus Error ......") 
                      
    
    def stop_run(self):
        print("Stop Run ....")
        self.label_2.hide()
        
        #Stop Motor.
        try:
                #instrument = minimalmodbus.Instrument('/dev/ttyACM0', 7,debug = True) # port name, slave address (in decimal)                   
                self.instrument = minimalmodbus.Instrument('/dev/ttyACM0', 7) # port name, slave address (in decimal)
                self.instrument.serial.timeout = 1
                self.instrument.serial.baudrate = 115200
                #time.sleep(5)
                self.IO_error_flg=0
        except IOError as e:
                print("IO Errors- Connection to Modbus......:"+str(e))
                self.IO_error_flg=1
                self.label_2.setText("IO Error.")
                self.label_2.show()
        if(self.IO_error_flg==0):                    
                ####### Start Test-Write in Coil Register. ############
                try:
                       #write_bit(registeraddress: int, value: int, functioncode: int = 5) → None[source]   
                       print("\n\n\n\n##### SET :COIL stop  ######")
                       self.instrument.write_bit(1,1,5)                    
                       self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET Test Stop Bit :1",self.login_user_role)
                       self.label_2.setText("Motor Stopped.")
                       self.label_2.show()
                       #time.sleep(5)
                except IOError as e:
                       print("Ignore-Modbus Error- SET COIL start_bit..:"+str(e))
                       self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET start_bit :"+str(self.start_bit),self.login_user_role)
                       self.IO_error_flg=1 
                
        else:
                       print("Modbus Error ......")   
           
       
           
    
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=spped_setup_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    
   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AE_MANUAL_CONTROL_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
