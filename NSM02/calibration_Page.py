

from loadcelll_status import loadcell_status_Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3
import serial

class calibration_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 40, 710, 411))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(530, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(40, 140, 321, 231))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_11.setAutoDefault(True)
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(30, 50, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setLineWidth(3)
        self.textEdit.setObjectName("textEdit")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(390, 140, 291, 231))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(130, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_12.setAutoDefault(True)
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 50, 221, 111))
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_2.setLineWidth(3)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(310, 90, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(190, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_10.setAutoDefault(True)
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(10, 60, 691, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(340, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_13.setAutoDefault(True)
        self.pushButton_13.setDefault(True)
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label_4.setText(_translate("MainWindow", "Calibration."))
        self.pushButton_8.setText(_translate("MainWindow", "OK"))
        self.pushButton_11.setText(_translate("MainWindow", "NEXT"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; vertical-align:sub;\">Put Empty Bicker/Pot</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; vertical-align:sub;\"> on Base and Click on</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; vertical-align:sub;\"> OK button.And Procced </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; vertical-align:sub;\">for Next Step.</span></p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "OK"))
        self.pushButton_12.setText(_translate("MainWindow", "VERIFY"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">Fill Bicker with 1 Liter Water</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\"> and Then Click on OK Button.</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Current Weight is : 1000 Kg."))
        self.pushButton_10.setText(_translate("MainWindow", "Return"))
        self.pushButton_13.setText(_translate("MainWindow", "LoadCell"))
        self.pushButton_10.clicked.connect(MainWindow.close)
        
        
        self.pushButton_8.setDisabled(True)
        self.pushButton_9.setDisabled(True)
        self.pushButton_11.setDisabled(True)
        self.pushButton_12.setDisabled(True)
        self.frame_2.setDisabled(True)
        self.frame_3.setDisabled(True)
        #self.pushButton_8.setDisabled(True)
        self.pushButton_7.clicked.connect(self.start_calibration)
        self.pushButton_13.clicked.connect(self.open_new_window)
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
            self.label_5.setText("Calibration is Done succefully,verify." )  
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
        self.ui=loadcell_status_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = calibration_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
