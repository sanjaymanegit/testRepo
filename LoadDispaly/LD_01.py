# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LD_01.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from LD_03_CONFIRM_PRINT import Ui_Confirm_Print
from LD_02_SET_MASTER import Ui_SetMaster
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
import time
import serial


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1144, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 50, 1061, 561))
        self.frame.setStyleSheet("border: 3px solid black;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"border-radius: 30px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 30, 991, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(130, 130, 801, 261))
        self.frame_2.setStyleSheet("background-color: rgb(255, 196, 197);\n"
"border: 2px solid black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:none;")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(140, 20, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 255);\n"
"border:none;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border:none;")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber.setGeometry(QtCore.QRect(320, 90, 391, 131))
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setStyleSheet("color: rgb(0, 170, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(3)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(720, 180, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border:none;")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_26 = QtWidgets.QLabel(self.frame_2)
        self.label_26.setGeometry(QtCore.QRect(20, 90, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(0, 0, 0);\n"
"border:none;")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_30 = QtWidgets.QLabel(self.frame_2)
        self.label_30.setGeometry(QtCore.QRect(140, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(0, 0, 255);\n"
"border:none;")
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_39 = QtWidgets.QLabel(self.frame_2)
        self.label_39.setGeometry(QtCore.QRect(140, 140, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(0, 0, 255);\n"
"border:none;")
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_47 = QtWidgets.QLabel(self.frame_2)
        self.label_47.setGeometry(QtCore.QRect(320, 20, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(170, 0, 255);\n"
"border:none;")
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.checkbox = QtWidgets.QCheckBox(self.frame_2)
        self.checkbox.setGeometry(QtCore.QRect(20, 190, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkbox.setFont(font)
        self.checkbox.setStyleSheet("border:none;")
        # self.checkbox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.checkbox.setObjectName("checkbox")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(140, 190, 91, 51))
        self.lineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(241, 255, 239);\n"
"border:1px solid black;\n"
"border-radius: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(250, 190, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border:none;")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 460, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(850, 460, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setDefault(True)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 460, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(231, 154, 115);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(580, 460, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.ld_flag="No"
        self.capacity_flag="No"
        self.off_position_flag="No"
        self.flag="No"
        self.ser =""
        self.line =""                   
       
        self.xstr0=""
        self.xstr1=""
        self.xstr2=""
        self.buff=[]
        
        self.IO_error_flg=0
        self.xstr3=""
        self.xstr2=""
        self.xstr4=""
        self.current_value=0
        self.green_counter=0
        
        self.last_value=0
        self.current_value=0
        self.enable_buttons_flag="No"
        self.enable_counter=0
        self.weighing_crosses_min_wt_lim="No"
        self.weighing_crosses_max_wt_lim="No"
        self.wt_min_limit=0
        self.wt_max_limit=0      
        self.c1_count=0
        
        self.ld_set=0
        self.mod_val=0
        
        self.last_display_val=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Delta Electronics Pvt. Ltd"))
        self.label_3.setText(_translate("MainWindow", "Unit No:"))
        self.label_4.setText(_translate("MainWindow", "002"))
        self.label_6.setText(_translate("MainWindow", "Time:"))
        self.label_15.setText(_translate("MainWindow", "Kg."))
        self.label_26.setText(_translate("MainWindow", "Date :"))
        self.label_30.setText(_translate("MainWindow", "05 Aug 2020"))
        self.label_39.setText(_translate("MainWindow", "14:30"))
        self.label_47.setText(_translate("MainWindow", "Gross Weight:"))
        self.checkbox.setText(_translate("MainWindow", "Length :"))
        self.label_16.setText(_translate("MainWindow", "(mm.)"))
        self.pushButton_2.setText(_translate("MainWindow", "Set Master Info"))
        self.pushButton_5.setText(_translate("MainWindow", "Exit"))
        self.pushButton_7.setText(_translate("MainWindow", "Print"))
        self.pushButton_6.setText(_translate("MainWindow", "Refresh"))
        self.load_data()
        self.pushButton_2.clicked.connect(self.set_master)
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.pushButton_6.clicked.connect(self.refresh)
        self.timer = QtCore.QTimer()
        self.timer.start(1)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.dateAndTime)
        self.checkbox.stateChanged.connect(self.length_checked)
        self.pushButton_7.clicked.connect(self.confirm_print)
        self.timer2=QtCore.QTimer()
        self.start_wt()   

    def length_checked(self, state):
        
        if state == 2:   # 2 corresponds to checked state
            self.lineEdit.setEnabled(True)
        else:
            self.lineEdit.setEnabled(False)  

        

    def dateAndTime(self):
        self.label_39.setText(datetime.datetime.now().strftime("%H : %M"))
        self.label_30.setText(datetime.datetime.now().strftime("%d %b %Y"))
    def refresh(self):
        connection = sqlite3.connect("LD.db")

        results = connection.execute("SELECT COMPANY_NAME, UNIT_NO, LENGTH FROM MASTER_DATA")

        for x in results:
            self.label.setText(x[0])
            self.label_4.setText(x[1])
            self.lineEdit.setText(x[2])
        # print(self.label, self.label_4, self.lineEdit, " after refresh")     
        

    def confirm_print(self):
        self.company_name = str(self.label.text())
        self.unit_no = str(self.label_4.text())
        self.date = str(self.label_30.text())
        self.time = str(self.label_39.text())
        self.length = str(self.lineEdit.text())
        self.gross_weigth = str(self.lcdNumber.value())
        print(self.gross_weigth, "gross ")
        connection =sqlite3.connect("LD.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO REPORTS (COMPANY_NAME, UNIT_NO, GROSS_WT, DATE_RC, TIME_RC, LENGTH, STATUS) VALUES (?, ?, ?, ?, ?, ?, 'CONFIRM TO PRINT')", (self.company_name, self.unit_no, self.gross_weigth, self.date, self.time, self.length))

        #cursor.execute("INSERT INTO REPORTS ( COMPANY_NAME = ?, UNIT_NO = ?, GROSS_WT = ?, DATE_RC = ?, TIME_RC = ?, LENGTH = ?, STATUS = 'CONFIRM TO PRINT' )", (self.company_name, self.unit_no, self.gross_weigth, self.date, self.time, self.length))
        #self.query = "UPDATE REPORTS SET COMPANY_NAME = ?, UNIT_NO = ?, GROSS_WT = ?, DATE_RC = ?, TIME_RC = ?, LENGTH = ?, STATUS = 'CONFIRM TO PRINT' "
        #cursor.execute("UPDATE REPORTS SET COMPANY_NAME = ?, UNIT_NO = ?, GROSS_WT = ?, DATE_RC = ?, TIME_RC = ?, LENGTH = ?, STATUS = 'CONFIRM TO PRINT' ", (self.company_name, self.unit_no, self.gross_weigth, self.date, self.time, self.length))
        connection.commit()
        connection.close()
        self.open_confirm_print_page()
    
    def set_master(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SetMaster()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_confirm_print_page(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Confirm_Print()
        self.ui.setupUi(self.window)
        self.window.show()   
    
    def load_data(self):
        connection = sqlite3.connect("LD.db")
        results = connection.execute("SELECT COMPANY_NAME, UNIT_NO, LENGTH FROM MASTER_DATA")
        for x in results:
            self.label.setText(str(x[0]))
            self.label_4.setText(str(x[1]))
            self.lineEdit.setText(str(x[2]))



    def start_wt(self):
        #print("Weight Started ....")
        try:
            self.ser = serial.Serial(
                                port='/dev/ttyAMA0',
                                baudrate=115200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.05
                            )
        
            self.ser.flush()       
            
            
            self.line = self.ser.readline(15)
            print("o/p:"+str(self.line))
             
            self.timer2.setInterval(1000)        
            self.timer2.timeout.connect(self.display_lcd_val)
            self.timer2.start(1)
            
            
        except IOError:
            print("IO Errors-load cell connections error")
            self.IO_error_flg=1
            self.groupBox_7.show()
            self.label_2.show()
            self.label_2.setText("LOAD CELL CONNECTION ERROR.")
            
            
    def display_lcd_val(self):               
        #print(" inside display_lcd_val:"+str(self.IO_error_flg))
        #self.label_2.hide()
        if(self.green_counter > 0):
                #self.pushButton_9.setStyleSheet("background-color: rgb(0, 170, 0);")
                #self.lcdNumber_2.setStyleSheet("color: rgb(255, 255, 0);\n background-color: rgb(0, 0, 0);")               
                self.green_counter=self.green_counter-1
        else:
                self.green_counter=0
                #self.pushButton_9.setStyleSheet("background-color: rgb(170, 0, 0);")
        if(self.IO_error_flg==0):
            try:
                self.line = self.ser.readline()
                print(" raw o/p:"+str(self.line))
                print("self.line:"+str(self.line,'utf-8'))
                self.xstr0=str(self.line,'utf-8')
                self.xstr1=self.xstr0.replace("\r","")
                self.xstr2=self.xstr1.replace("\n","")
                self.buff=self.xstr2.split("_")
                self.last_value=self.current_value 
                if(len(self.buff)> 1):
                       # if(str(self.buff[3]) == 'R'): 
                                self.xstr2=str(self.buff[0])
                                try:
                                     self.xstr4=int(self.xstr2)
                                except ValueError:                        
                                    print("Value Error"+str(self.xstr2))
                                    self.xstr4=0
                                    self.c1_count=0
                                self.c1_count=str(self.buff[1])
                                #self.lcdNumber_2.setProperty("value", str(self.xstr4))
                                self.lcdNumber.setProperty("value", str(self.xstr4)) 
                                #self.lcdNumber.setProperty("value", str(self.c1_count))
                                #print("self.c1_count :"+str(self.c1_count)+" Weight : "+str(self.xstr4))
                               
                    
            except IOError:
                print("IO Errors : Data Read Error") 
                self.IO_error_flg=1                
                self.label_2.show()
                self.label_2.setText("IO Errors .")
        
    def stop_timer(self):
       if(self.timer2.isActive()):
           self.timer2.stop()           



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
