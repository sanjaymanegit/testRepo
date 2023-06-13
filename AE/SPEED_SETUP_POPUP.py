


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


class spped_setup_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 482)
        #MainWindow.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 721, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color: rgb(215, 255, 252);")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)
        self.lineEdit.setValidator(input_validator)
        
        self.lineEdit.setGeometry(QtCore.QRect(240, 120, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 120, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(340, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 200, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_2)
        self.lineEdit_2.setValidator(input_validator)
        
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(340, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(440, 280, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 40, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        #font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 350, 651, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        #self.label_5.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 280, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(560, 196, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 280, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 280, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
        self.lineEdit_3.setValidator(input_validator)
        
        
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(340, 280, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.modbus_status_flag="N"
        self.modbus_port=""
        self.non_modbus_port=""
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Forward.Speed :"))
        self.label_2.setText(_translate("MainWindow", "( mm/min )"))
        self.label_3.setText(_translate("MainWindow", "Reverse.Speed :"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "( mm/min )"))
        self.pushButton.setText(_translate("MainWindow", "Set Speed"))
        self.pushButton_2.setText(_translate("MainWindow", "Check Modbus Connection"))
        self.label_5.setText(_translate("MainWindow", "Click on \"Set Speed\" to setup speed."))
        self.pushButton_3.setText(_translate("MainWindow", "Close"))
        self.label_6.setText(_translate("MainWindow", "Set up Default Speed of Motor :"))
        self.checkBox.setText(_translate("MainWindow", "Modbus isActive ?"))
        self.checkBox.setDisabled(True)
        self.label_7.setText(_translate("MainWindow", "Max.Speed :"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "( mm/min )"))
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.save_data)
        self.pushButton_2.clicked.connect(self.chk_modbus_conn)        
        self.load_data()
        
    def load_data(self):
        connection = sqlite3.connect("tyr.db")
        #results=connection.execute("SELECT MOTOR_TEST_SPEED,MOTOR_MAX_SPEED FROM SETTING_MST")
        results=connection.execute("SELECT NEW_TEST_MOTOR_SPEED,NEW_TEST_MOTOR_REV_SPEED FROM GLOBAL_VAR")
        rows=results.fetchall()  
        self.lineEdit.setText(str(rows[0][0])) #Fr .Speed
        self.lineEdit_2.setText(str(rows[0][1])) #rev.Speed
        #self.lineEdit_3.setText(str(rows[0][2])) #Max.Speed
        connection.close()
        self.load_modbus_port()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT MOTOR_MAX_SPEED,ISACTIVE_MODBUS,MODBUS_PORT,NON_MODBUS_PORT FROM SETTING_MST")        
        rows=results.fetchall()  
        self.lineEdit_3.setText(str(rows[0][0])) #Max.Speed
        self.modbus_status_flag=str(rows[0][1])
        self.modbus_port=str(rows[0][2])
        self.non_modbus_port=str(rows[0][3])        
        connection.close()
        
        self.label_5.setText("Modbus Port: <font color=blue>"+str(self.modbus_port)+" </font>,  Controller Port :<font color=blue>"+str(self.non_modbus_port)+" </font>")
        if(self.modbus_status_flag=='Y'):
              self.checkBox.setChecked(True)
        else:
              self.checkBox.setChecked(False)
        
  
    def save_data(self):
        
        if(self.checkBox.isChecked()):
               self.modbus_status_flag='Y'
        else:
               self.modbus_status_flag='N'
               
        connection = sqlite3.connect("tyr.db")        
        with connection:        
            cursor = connection.cursor()                    
            cursor.execute("UPDATE SETTING_MST SET  MOTOR_TEST_SPEED = '"+self.lineEdit.text()+"',MOTOR_MAX_SPEED='"+self.lineEdit_3.text()+"',ISACTIVE_MODBUS='"+str(self.modbus_status_flag)+"'")
            cursor.execute("UPDATE GLOBAL_VAR SET  NEW_TEST_MOTOR_SPEED = '"+self.lineEdit.text()+"',NEW_TEST_MOTOR_REV_SPEED='"+self.lineEdit_2.text()+"'") 
        connection.commit();
        connection.close() 
        
        self.label_5.setText("Saved Successfully !")
        self.label_5.show()
        
        self.input_speed_val=str(self.lineEdit.text())
        v=float(self.input_speed_val)
        try:
            if(self.modbus_port=="dev/ttyUSB1"):
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
            print(" write2 :"+str(v))
        except IOError as e:
            print("Forward-Write Modbus IO Error -Motor start : "+str(e))
        
        print("Forward speed : "+str(v))
        
        
        self.rev_speed_val=str(self.lineEdit_2.text())
        v=float(self.rev_speed_val)
        try:     
            
            if(self.modbus_port=="dev/ttyUSB1"):
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
            print(" write2 :"+str(v))
        except IOError as e:
            print("Reverse-Write Modbus IO Error -Motor start : "+str(e))
        
        print("Reverse speed : "+str(v))
        
        
    def chk_modbus_conn(self):
        self.input_speed_val=str(self.lineEdit.text())
        v=float(self.input_speed_val)
        try:     
            if(self.modbus_port=="/dev/ttyUSB1"):
                  instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) # port name, slave address (in decimal)
            else:
                  instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # port name, slave address (in decimal)
                  print("self.modbus_port:"+str(self.modbus_port))
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
            print(" write2 :"+str(v))
            self.label_5.setText("Modbus Connection Ok.")
            self.label_5.show()
        except IOError as e:
            print("Forward-Write Modbus IO Error -Motor start : "+str(e))
            self.label_5.setText("ERROR:"+str(e))
            self.label_5.show()
        print("Forward speed : "+str(v))
        
        
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
        
        print("Port Type:"+str(port_type))
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
                   
        print("Port Type2:"+str(port_type)) 
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
                            
                        
                        print("USB0: "+str(self.port)+" non_modbus: "+str(self.non_modbus_port)+" modbus: "+str(self.modbus_port))     
                        
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
    ui = spped_setup_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
