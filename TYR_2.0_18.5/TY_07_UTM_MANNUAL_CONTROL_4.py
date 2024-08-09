
from PyQt5 import QtCore, QtGui, QtWidgets
from SPEED_SETUP_POPUP import spped_setup_Ui_MainWindow
from TY_07_UTM_MANNUAL_CONTROL_2 import TY_07_Ui_MainWindow

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


class TY_07_4_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1349, 726)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1301, 651))
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
        self.label_4.setGeometry(QtCore.QRect(410, 20, 471, 61))
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
        self.frame_2.setGeometry(QtCore.QRect(60, 130, 1201, 481))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(350, 180, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
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
        self.lineEdit.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(255, 231, 254);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 60, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
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
        font.setPointSize(12)
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
        font.setPointSize(12)
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
        self.lineEdit_2.setStyleSheet("color: rgb(0, 170, 0);\n"
"border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"border-radius:20px;\n"
"background-color: rgb(255, 231, 254);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(710, 60, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(530, 280, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
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
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(1030, 60, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
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
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(50, 270, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber.setGeometry(QtCore.QRect(350, 270, 161, 61))
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(40, 370, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber_2.setGeometry(QtCore.QRect(350, 370, 161, 61))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(530, 370, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 300, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(255, 231, 254);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(880, 300, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(255, 231, 254);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(860, 70, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:0px;\n"
"background-color: rgb(255, 231, 254);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setGeometry(QtCore.QRect(980, 0, 20, 161))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(810, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1349, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.IO_error_flg=0
        self.xstr3=""
        self.xstr2=""
        self.xstr4=""
        self.current_value=0
        self.test_guage_mm=""
        self.chck_for_last_rec=1

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Speed Setup"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.label_4.setText(_translate("MainWindow", "Manual Control  - Only Compression"))
        self.label_2.setText(_translate("MainWindow", "Click on Start-Down Button."))
        self.label.setText(_translate("MainWindow", " Speed (Down) :"))
        self.label_3.setText(_translate("MainWindow", "(Mm/min) "))
        self.label_5.setText(_translate("MainWindow", "Displacement :"))
        self.label_6.setText(_translate("MainWindow", "(Mm) "))
        self.label_11.setText(_translate("MainWindow", "(Kgf) "))
        self.pushButton_3.setText(_translate("MainWindow", "Start-DOWN"))
        self.label_7.setText(_translate("MainWindow", "Current Load :"))
        self.label_8.setText(_translate("MainWindow", "Current Displacement :"))
        self.label_12.setText(_translate("MainWindow", "(Mm) "))
        self.pushButton_4.setText(_translate("MainWindow", "Stop Process"))
        self.pushButton_5.setText(_translate("MainWindow", "Mannual Control"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.label_9.setText(_translate("MainWindow", "Load Cell No :"))
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.open_new_window)
        self.pushButton_5.clicked.connect(self.open_new_window5)
        self.pushButton_3.clicked.connect(self.start_down)
        self.pushButton_4.clicked.connect(self.stop_timer)
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT IFNULL(PRE_LOAD,0),IFNULL(MANUAL_CONTROL_TEST_SPEED,0),LOAD_CELL_NO from GLOBAL_VAR") 
        for x in results:                        
                        self.lineEdit_2.setText(str(x[0]))
                        self.lineEdit.setText(str(x[1]))
                        self.comboBox.setCurrentText(str(x[2]))                        
        connection.close()
        
        self.timer2=QtCore.QTimer()
    
    def validate_speed(self):
        self.command_str_speed=""
        self.break_sence="0"
        self.auto_rev_time_off="0"
        if(str(self.lineEdit.text()) == ""):
             self.goahead_flag=0
             self.label_2.setText("Speed is Empty.")
             self.label_2.show()
        elif(str(self.lineEdit_2.text()) == ""):
             self.goahead_flag=0
             self.label_2.setText("Deflection is Empty.")
             self.label_2.show()             
        else:
            self.goahead_flag=1
        
        
        if(self.goahead_flag==1):
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT IFNULL(MOTOR_MAX_SPEED,0),BREAKING_SENCE,AUTO_REV_TIME_OFF from SETTING_MST") 
                    for x in results:
                         self.speed_val=str(x[0])
                         self.break_sence=int(x[1])
                         self.auto_rev_time_off=int(x[2])
                    connection.close()
                    self.goahead_flag=0
                    
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT IFNULL(NEW_TEST_MOTOR_SPEED,0),IFNULL(NEW_TEST_GUAGE_MM,0) from GLOBAL_VAR") 
                    for x in results:
                         self.input_speed_val=str(x[0])
                         self.test_guage_mm=str(x[1])
                    connection.close()
                    
                    if(self.input_speed_val != ""):
                        if(int(self.input_speed_val) <= int(self.speed_val)):
                             #print(" Ok ")
                             self.goahead_flag=1
                             self.calc_speed=(int(self.input_speed_val)/int(self.speed_val))*1000                 
                             #print(" calc Speed : "+str(self.calc_speed))
                             #print(" command: *P"+str(self.calc_speed)+" \r")
                             self.command_str_speed="*P%04d"%self.calc_speed+"_%04d"%self.break_sence+"\r"
                             print("Morot Speed and Breaking speed Command  :"+str(self.command_str_speed))
                        else:
                             print(" not Ok ")
                             
                    else:
                        print(" not Ok ")
        
    
    
    def start_down(self):
        
        self.validate_speed()
        if(self.goahead_flag==1):
                    self.flag=1
                    self.command_str=""                    
                    self.test_guage_mm=float(self.test_guage_mm)
                    connection = sqlite3.connect("tyr.db")              
                    with connection:        
                                cursor = connection.cursor()
                                cursor.execute("UPDATE GLOBAL_VAR SET PRE_LOAD='"+str(self.lineEdit_2.text())+"',LOAD_CELL_NO='"+str(self.comboBox.currentText())+"',MANUAL_CONTROL_TEST_SPEED='"+str(self.lineEdit.text())+"'")
                    connection.commit();
                    connection.close() 
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
                    
                    
                    self.test_type="Compression"
                    if(self.test_type=="Flexural"):
                        self.test_guage_mm=0
                        self.command_str="*G0.00\r"
                    else:
                        self.command_str="*G%.2f"%self.test_guage_mm+"\r"
                        
                    print("Guage Length Command : "+str(self.command_str))
                    
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    #time.sleep(2)
                    #===== Auto Reverse Time Off =====
                    self.ser.flush()
                    self.command_str="*O%04d"%self.auto_rev_time_off+"\r"
                    print("Auto reve. Time off Command : "+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    
                    
                    b = bytes(self.command_str_speed, 'utf-8')
                    self.ser.write(b)
                    print("Speed command:"+str(self.command_str_speed)) 
                    
                    
                    self.load_cell_no=str(self.comboBox.currentText())
                    self.max_length=str(self.lineEdit_2.text())
                    self.max_length=float(self.test_guage_mm)-float(self.max_length)
                    self.max_load=int("09999")
                    
                    if(int(self.load_cell_no) ==1):                                    
                                    self.command_str="*S1C%05d"%self.max_load+" %.1f"%float(self.max_length)+"\r"
                    else:
                                    self.command_str="*S2C%05d"%self.max_load+" %.1f"%float(self.max_length)+"\r"
                                    
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    self.label_2.setText("Compression Started for Deflection:"+str(self.max_length)+" Mm. Load cell No:"+str(self.load_cell_no))               
                    print("Compression command:"+str(self.command_str))                                    
                    self.label_2.show()
                    '''
                    #====================================================
                    self.command_str="*D"
                    print("Tare Command : "+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    #===================================================
                    '''
                    self.load_cell_hi=1
                    self.encoder=2
                    self.line = self.ser.readline(15)
                    print("o/p:"+str(self.line))
                    self.timer2.setInterval(1000)        
                    self.timer2.timeout.connect(self.display_lcd_val)
                    self.timer2.start(1)
                    
                    
                    
        else:
                    print("Invalid......")
                
        
            
            
       
            
            
    def display_lcd_val(self):               
        #print(" inside display_lcd_val:"+str(self.IO_error_flg))
        self.pushButton_2.setDisabled(True)
        self.pushButton_4.setEnabled(True)
        #self.label_2.hide()
        self.label_2.setText("Running.....")       
        self.label_2.show()
        if(self.IO_error_flg==0):
            try:
                self.line = self.ser.readline()
                print("Timer Job o/p:"+str(self.line))
                self.ser.flush()
                self.ser.write(b'*D\r')
            except IOError:
                print("IO Errors")
            
            xstr3=str(self.line)
            xstr3=xstr3[1:int(len(xstr3)-1)]
            xstr2=xstr3.replace("'\\r","")        
            #print("replace3('\r):"+str(xstr2))
            xstr1=xstr2.replace("'","")        
            #print("replace2('):"+str(xstr1))
            xstr=xstr1.replace("\\r","")
            #print("replace1(\r):"+str(xstr))        
            self.buff=xstr.split("_")
            #print("length of array :"+str(len(self.buff)))
            if(int(len(self.buff)) > 8 ):
                #print("length of array :"+str(len(self.buff)))
                self.check_R = re.findall(r"[R]", xstr)
                self.check_S = re.findall("[S]", xstr)
                self.check_OK = re.findall("[OK]", xstr)
                #print("Checkking R Characher :"+str(self.check_R))
                #print("Checkking OK Characher :"+str(len(self.check_OK))) 
                if (len(self.check_R) > 0 and len(self.check_OK) ==0):
                    #print("Running.... :"+str(self.check_R))
                    #print("length(X).... :"+str(self.buff[4]))
                    #print("load(Y)... :"+str(self.buff[1]))
                    #print("Load Cell No... :"+str(self.buff[7]))
                    self.load_cell_hi=str(self.buff[7])
                    #print("Encoder No.. :"+str(self.buff[6]))
                    self.encoder=str(self.buff[6])
                    print(" load_cell No :"+str(self.load_cell_hi)+" self.encoder:"+str(self.encoder))
                    if(self.load_cell_hi==1):              
                        self.q=abs(float(self.buff[0]))
                    else:                        
                        self.q=abs(float(self.buff[1])) #+random.randint(0,50)
                    
                    if(self.encoder==1):
                        self.p=abs(float(self.buff[4])) #
                    else:
                        self.p=abs(float(self.buff[5]))
                    
                    if(self.test_type=="COMPRESS_2"):
                        self.p=int(self.test_guage_mm)-self.p
                        #print("self.p :"+str(self.p))
                    elif(self.test_type=="Flexural"):
                        #self.p=self.p
                        self.p=int(self.test_guage_mm)-self.p
                    else:
                        self.p=int(self.test_guage_mm)-self.p
                    
                    
                    self.lcdNumber_2.setProperty("value", str(self.p))
                    self.lcdNumber.setProperty("value", str(self.q))
                else:
                        
                        ### This is change to process last repcord
                        if(self.chck_for_last_rec==1):
                                self.chck_for_last_rec=0
                                if(str(self.buff[6])=="2"):
                                    self.load_cell_hi=1
                                    self.load_cell_lo=0
                                else:
                                    self.load_cell_hi=0
                                    self.load_cell_lo=1
                                    
                                if(str(self.buff[7])=="2"):
                                    self.extiometer=1
                                    self.encoder=0
                                else:
                                    self.extiometer=0
                                    self.encoder=1
                                
                                if(self.load_cell_hi==1):              
                                    self.q=abs(float(self.buff[1])) #+random.randint(0,50)
                                else:
                                    self.q=abs(float(self.buff[0]))
                                
                                if(self.encoder==1):
                                    self.p=abs(float(self.buff[4])) #
                                else:
                                    self.p=abs(float(self.buff[5]))
                                #print("self.test_typexx: "+str(self.test_type))
                                    
                                self.t=abs(float(self.buff[3]))   
                                    
                                if(self.test_type=="Compression"):
                                    if(int(self.test_guage_mm) > int(self.p)):
                                            self.p=int(self.test_guage_mm)-self.p
                                    else:
                                            self.p=int(self.p)-self.test_guage_mm
                                    #print("self.p :"+str(self.p))
                                elif(self.test_type=="Flexural"):
                                    #self.p=self.p
                                    self.p=int(self.test_guage_mm)-self.p
                                else:
                                    self.p=self.p
              

                                
                                
                               # self.arr_speed.append(float(self.speed))
                                
#                                 self.arr_p.append(float(self.p))
#                                 self.arr_q.append(float(self.q))
#                                 
#         #                         self.t=self.elapsed_time.total_seconds()
#                                 self.t_timestamp=str(self.end_time)
#                                 self.arr_t_timestamp.append(self.t_timestamp)
#                                 self.arr_t.append(float(self.t))
                                
                                print("Last Record.... Timer P:"+str(self.p)+" q:"+str(self.q)+" t:"+str(self.t))
                                self.lcdNumber_2.setProperty("value", str(self.p))
                                self.lcdNumber.setProperty("value", str(self.q))
                      
                        #self.on_ani_stop()
                        self.label_2.setText("Wait....Returning")       
                        self.label_2.show()
                               
                    
            
            
        
    def stop_timer(self):
       if(self.timer2.isActive()):
           self.timer2.stop()
           self.pushButton_2.setEnabled(True)
           self.label_2.setText("Stopped Process...You can close window now.")       
           self.label_2.show()
           
    
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=spped_setup_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window5(self):
        print("ok")
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_07_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_07_4_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
