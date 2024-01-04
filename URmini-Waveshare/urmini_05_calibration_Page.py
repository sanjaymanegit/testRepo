
from urmini_19_loadcelll_status import urmini_19_Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3
import serial


class urmini_05_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 601, 421))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(440, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        #self.pushButton_7.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"color: rgb(0, 0, 0);")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        
        self.pushButton_7_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7_1.setGeometry(QtCore.QRect(300, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7_1.setFont(font)
        #self.pushButton_7.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"color: rgb(0, 0, 0);")
        self.pushButton_7_1.setAutoDefault(True)
        self.pushButton_7_1.setDefault(True)
        self.pushButton_7_1.setFlat(False)
        self.pushButton_7_1.setObjectName("pushButton_7_1")
        
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 170, 261, 211))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 170, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        #self.pushButton_8.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"color: rgb(0, 0, 0);")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(140, 170, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        #self.pushButton_11.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"color: rgb(0, 0, 0);")
        self.pushButton_11.setAutoDefault(True)
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(30, 25, 201, 141))
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setLineWidth(3)
        self.textEdit.setObjectName("textEdit")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(330, 170, 241, 211))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 170, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        #self.pushButton_9.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"color: rgb(0, 0, 0);")
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(130, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        #self.pushButton_12.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"color: rgb(0, 0, 0);")
        self.pushButton_12.setAutoDefault(True)
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 30, 181, 121))
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_2.setLineWidth(3)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(190, 120, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(200, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        #self.pushButton_10.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"color: rgb(0, 0, 0);")
        self.pushButton_10.setAutoDefault(True)
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 90, 521, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 21))
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
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44:09"))
        self.pushButton_7.setText(_translate("MainWindow", "Start Calibration"))
        self.pushButton_7_1.setText(_translate("MainWindow", "Check LoadCell"))
        self.label_4.setText(_translate("MainWindow", "CALIBRATION"))
        self.pushButton_8.setText(_translate("MainWindow", "OK"))
        self.pushButton_11.setText(_translate("MainWindow", "NEXT"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; vertical-align:sub;\">Put Empty Beaker/Pot on Base and Click on OK button.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; vertical-align:sub;\">And Procced for Next Step.</span></p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "OK"))
        self.pushButton_12.setText(_translate("MainWindow", "VERIFY"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; vertical-align:sub;\">Fill Beaker with 1 Liter Water and Then Click on OK Button.</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", ""))
        self.pushButton_10.setText(_translate("MainWindow", "RETURN"))
        
        self.pushButton_10.clicked.connect(MainWindow.close)
        
        
        self.pushButton_8.setDisabled(True)
        self.pushButton_9.setDisabled(True)
        self.pushButton_11.setDisabled(True)
        self.pushButton_12.setDisabled(True)
        self.frame_2.setDisabled(True)
        self.frame_3.setDisabled(True)
        #self.pushButton_8.setDisabled(True)
        self.pushButton_7.clicked.connect(self.start_calibration)
        self.pushButton_7_1.clicked.connect(self.open_new_window)
        self.pushButton_8.clicked.connect(self.step1_ok)
        self.pushButton_11.clicked.connect(self.step1_next)
        self.pushButton_9.clicked.connect(self.step2_ok)
        self.pushButton_12.clicked.connect(self.step2_verify)
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
    
    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def start_calibration(self):
        self.label_5.show()
        self.pushButton_11.setDisabled(True)
        self.frame_2.setEnabled(True)
        self.frame_3.setDisabled(True)
        self.label_5.setText("Procced for Step1")  
        self.label_5.show()
        self.pushButton_8.setEnabled(True)
        self.pushButton_11.setDisabled(True)
    
    def step1_ok(self):
        self.pushButton_11.setEnabled(True)
        self.pushButton_8.setDisabled(True)
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
            b = bytes('Z', 'utf-8')
            self.ser.write(b)
            print("Step1 OK done")
        except IOError:
            print("IO Errors")
            self.label_5.setText("IO Errors" )  
            self.label_5.show()
            
    def step1_next(self):
        self.frame_3.setEnabled(True)
        self.frame_2.setDisabled(True)        
        self.label_5.setText("Procced for Step2")  
        self.label_5.show()
        self.pushButton_9.setEnabled(True)
        self.pushButton_12.setDisabled(True)
    
    def step2_ok(self):
        self.pushButton_12.setEnabled(True)
        self.pushButton_9.setDisabled(True)
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
            b = bytes('C', 'utf-8')
            self.ser.write(b)           
            time.sleep(1)
            self.label_5.setText("Calibration is Done succefully , Please verify." )  
            self.label_5.show()            
        except IOError:
            print("IO Errors")
            self.label_5.setText("IO Errors" )  
            self.label_5.show()
        
    def step2_verify(self):
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
              
            self.line = self.ser.readline()                      
            print("o/p:"+str(self.line))
            self.xstr0=str(self.line,'utf-8')
            self.xstr1=self.xstr0.replace("\r","")
            self.xstr2=self.xstr1.replace("\n","")
            self.buff=self.xstr2.split("_")
            if(len(self.buff) > 2):
                self.label_5.setText("Current Weight is : "+str(self.buff[0])+" kg." )  
                self.label_5.show()
            
        except IOError:
            print("IO Errors")
            self.label_5.setText("IO Errors" )  
            self.label_5.show()
    
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=urmini_19_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = urmini_05_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
