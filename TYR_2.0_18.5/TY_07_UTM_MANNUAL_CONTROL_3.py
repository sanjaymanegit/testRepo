from PyQt5 import QtCore, QtGui, QtWidgets
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
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 709))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 201, 51))
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
        self.pushButton_2.setGeometry(QtCore.QRect(1030, 30, 201, 51))
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
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(480, 20, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 85, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(60, 110, 1201, 481))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_2.setGeometry(QtCore.QRect(270, 280, 121, 141))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/up1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(500, 1000))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame_2)
        self.toolButton_3.setGeometry(QtCore.QRect(470, 280, 201, 141))
        self.toolButton_3.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"background-color: rgb(247, 255, 226);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/stop1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setIconSize(QtCore.QSize(500, 1000))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton = QtWidgets.QToolButton(self.frame_2)
        self.toolButton.setGeometry(QtCore.QRect(750, 280, 131, 141))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/down.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(500, 1000))
        self.toolButton.setObjectName("toolButton")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(260, 190, 611, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)
        self.lineEdit.setValidator(input_validator)
        self.lineEdit.setGeometry(QtCore.QRect(140, 50, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)        
        self.lineEdit.setStyleSheet("color: rgb(0, 170, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 60, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 0, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(280, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(410, 60, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_2)
        self.lineEdit_2.setValidator(input_validator)
        self.lineEdit_2.setGeometry(QtCore.QRect(580, 50, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(0, 170, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(710, 60, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(280, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(760, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(520, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
        self.lineEdit_3.setValidator(input_validator)
        self.lineEdit_3.setGeometry(QtCore.QRect(960, 50, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(0, 170, 0);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(1090, 60, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(840, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(0, 140, 1201, 41))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(383, 0, 20, 161))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setGeometry(QtCore.QRect(790, 0, 20, 161))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(60, 620, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 620, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 620, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(255, 231, 254);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(680, 620, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
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
        self.follow_me_active=0
        self.follow_me_inactive=0
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Speed Setup"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.label_4.setText(_translate("MainWindow", "Manual Control "))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Running with 40 % speed of maximum speed 500 ( mm/min)"))
        self.label.setText(_translate("MainWindow", " Speed :"))
        self.label_3.setText(_translate("MainWindow", "(mm/min) "))
        self.label_5.setText(_translate("MainWindow", "Load cell No :"))
        self.label_6.setText(_translate("MainWindow", "(mm) "))
        self.label_6.hide()
        self.label_7.setText(_translate("MainWindow", "(UP) "))
        self.label_8.setText(_translate("MainWindow", "(DOWN) "))
        self.label_9.setText(_translate("MainWindow", "(STOP) "))
        self.label_11.setText(_translate("MainWindow", "(Kg) "))
        self.label_12.setText(_translate("MainWindow", "Pre.Load:"))
        self.radioButton.setText(_translate("MainWindow", "Tensile"))
        self.radioButton_2.setText(_translate("MainWindow", "Compress"))
        self.pushButton_3.setText(_translate("MainWindow", "Set Pre Load"))
        self.label_10.setText(_translate("MainWindow", ""))
        self.pushButton_2.clicked.connect(MainWindow.close)       
        self.toolButton.clicked.connect(self.r_run)   #down
        self.toolButton_2.clicked.connect(self.f_run) #up
        self.toolButton_3.clicked.connect(self.stop_run)
        self.pushButton.clicked.connect(self.open_new_window)
        self.pushButton_3.clicked.connect(self.set_pre_load)
        #self.lineEdit_3.setDisabled(True)
        #self.lineEdit_2.setDisabled(True)
        #self.lineEdit.setDisabled(True)
        #self.pushButton_3.setDisabled(True)
        #self.radioButton.setDisabled(True)
        #self.radioButton_2.setDisabled(True)
        self.pre_load="0"
        self.label_2.hide()
        self.load_modbus_port()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT IFNULL(PRE_LOAD,0),IFNULL(LOAD_CELL_NO,2),TEST_MODE,IFNULL(MANUAL_CONTROL_TEST_SPEED,0) from GLOBAL_VAR") 
        for x in results:
                        self.pre_load=float(x[0])
                        self.lineEdit_3.setText(str(x[0]))
                        self.load_cell_no=str(x[1])
                        self.lineEdit_2.setText(str(x[1]))
                        self.test_mode=str(x[2])
                        self.lineEdit.setText(str(x[3]))
        connection.close()
        print(" self.load_cell_no : "+str(self.load_cell_no))
        #self.lineEdit_2.setText("1")
    
    def set_pre_load(self):
        self.flag=0
        self.command_str=""
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET PRE_LOAD='"+str(self.lineEdit_3.text())+"',LOAD_CELL_NO='"+str(self.lineEdit_2.text())+"',MANUAL_CONTROL_TEST_SPEED='"+str(self.lineEdit.text())+"'")
        connection.commit();
        connection.close()
        if(self.radioButton.isChecked()):                        
                        self.flag=1                        
        elif(self.radioButton_2.isChecked()):                        
                        self.flag=0                         
        else:
                        print(" invalid flag")
                    
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
        self.load_cell_no=str(self.lineEdit_2.text())
        self.pre_load=str(self.lineEdit_3.text())
        self.pre_load=float(self.pre_load)
        if(int(self.flag) == 1):
                if(int(self.load_cell_no)==1):
                        self.command_str="S1H%05d"%self.pre_load+"\r"
                       
                else:
                        self.command_str="S2H%05d"%self.pre_load+"\r"
                        
                        
                b = bytes(self.command_str, 'utf-8')
                self.ser.write(b)
                self.label_2.setText("Pre Load :"+str(self.lineEdit_3.text())+" Kg. Load cell No:"+str(self.load_cell_no)+" Test Mode:Tensile")
                print("Tensile With Pre Load Started. command: "+str(self.command_str))
        else:
                if(int(self.load_cell_no) ==1):
                        self.command_str="S1J%05d"%self.pre_load+"\r"
                       
                else:
                        self.command_str="S2J%05d"%self.pre_load+"\r"
                b = bytes(self.command_str, 'utf-8')
                self.ser.write(b)
                self.label_2.setText("Pre Load :"+str(self.lineEdit_3.text())+" Kg. Load cell No:"+str(self.load_cell_no)+" Test Mode:Compression")               
                print("Compress With Pre Load Started. command: "+str(self.command_str))
                
                            
        self.label_2.show()   
        
        
        
    
    def validate_speed(self):
        if(str(self.lineEdit.text()) == ""):
             self.goahead_flag=0
             self.label_2.setText("Speed is Empty.")
             self.label_2.show()
#         elif(str(self.lineEdit_2.text()) == ""):
#              self.goahead_flag=0
#              self.label_2.setText("Displacement is Empty.")
#              self.label_2.show()
#         elif(str(self.lineEdit_3.text()) == ""):
#              self.goahead_flag=0
#              self.label_2.setText("Load is Empty.")
#              self.label_2.show()
        else:
            self.goahead_flag=1
        
        
        if(self.goahead_flag==1):
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
