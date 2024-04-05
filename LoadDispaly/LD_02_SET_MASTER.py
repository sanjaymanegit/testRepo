# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LD_02_SET_MASTER.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from TY_09_register import TY_09_Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import wmi
import datetime
import time

class Ui_SetMaster(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 951, 461))
        self.frame.setStyleSheet("border: 3px solid black;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"border-radius: 30px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(230, 20, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border:2px solid black;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));\n"
"border-radius: 25px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(90, 80, 801, 271))
        self.frame_2.setStyleSheet("background-color: rgb(255, 196, 197);\n"
"border: 2px solid black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:None;")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(220, 30, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(241, 255, 239);\n"
"border:1px solid black;\n"
"border-radius: 12px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:None;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 110, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(241, 255, 239);\n"
"border:1px solid black;\n"
"border-radius: 12px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:None;")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 190, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(241, 255, 239);\n"
"border:1px solid black;\n"
"border-radius: 12px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(370, 190, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border:None;")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        
        
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 380, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(39, 255, 118);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(200, 380, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(740, 380, 151, 51))
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
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(90, 380, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid black;\n"
"border-radius: 12px;")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Master Data Set"))
        self.label_3.setText(_translate("MainWindow", "Company Name:"))
        self.label_4.setText(_translate("MainWindow", "Unit No:"))
        self.label_5.setText(_translate("MainWindow", "Length (Default) :"))
        self.label_6.setText(_translate("MainWindow", "(mm.)"))
        self.pushButton_7.setText(_translate("MainWindow", "Register"))
        self.pushButton_6.setText(_translate("MainWindow", "Save"))
        self.pushButton_5.setText(_translate("MainWindow", "Close"))
        self.label_47.setText(_translate("MainWindow", "Enter the field"))
        self.label_47.hide()
        # self.reset_lineEdit()
        self.pushButton_6.clicked.connect(self.update_master)
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.pushButton_7.clicked.connect(self.open_register)
        self.register_button()
        self.load_data()


    def open_register(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_09_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show() 
        
    def register_button(self):
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("LD.db")
        results=connection.execute("select DEVICE_SERIAL_NO from GLOBAL_VAR") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))
           if(serial_no == str(x[0])):
               #self.go_ahead="Yes"
               self.pushButton_7.hide()
           else:
               #self.go_ahead="No"
               self.pushButton_7.show()
        connection.close()
        
    def getserial(self):
        # Extract serial from cpuinfo file
        cpuserial = "0000000000000000"
        try:
           c = wmi.WMI()
           hddSerialNumber = c.Win32_PhysicalMedia()[0].wmi_property('SerialNumber').value.strip()
           cpuserial=hddSerialNumber
           #print("Serial No xxx: "+str(cpuserial))
        except:
           cpuserial = "ERROR000000000"
        return cpuserial    
        
    def load_data(self):
        connection = sqlite3.connect("LD.db")  
        results = connection.execute("SELECT COMPANY_NAME, UNIT_NO, LENGTH FROM MASTER_DATA LIMIT 1")
        
        for x in results:
             self.lineEdit.setText(str(x[0]))
             self.lineEdit_2.setText(str(x[1]))
             self.lineEdit_3.setText(str(x[2]))
             
        connection.close()
             
        
    def update_master(self):
        self.company_name = str(self.lineEdit.text())
        self.unit_no = str(self.lineEdit_2.text())
        self.length = str(self.lineEdit_3.text())
        if (self.company_name != "" and self.unit_no != ""):
                connection = sqlite3.connect("LD.db")
                cursor = connection.cursor()
                cursor.execute("UPDATE MASTER_DATA SET COMPANY_NAME = ?, UNIT_NO = ?, LENGTH = ?", (self.company_name, self.unit_no, self.length)) 

                #cursor.execute("UPDATE MASTER_DATA SET COMPANY_NAME ='"+str(self.company_name)+"', UNIT_NO = '"+str(self.unit_no)+"', LENGTH = '"+str(self.length)+"'")
                connection.commit()
                connection.close()
                
                self.label_47.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 0);\n"
"border:1px solid black;\n"
"border-radius: 12px;")
                self.label_47.setText("Data added successfully!")
                self.label_47.show()
                
                
        elif (self.company_name == ""):
             self.label_47.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);\n"
"border:1px solid black;\n"
"border-radius: 12px;")
             self.label_47.setText("Please enter the Company Name")
             self.label_47.show()
              
        elif (self.unit_no == ""):
             self.label_47.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);\n"
"border:1px solid black;\n"
"border-radius: 12px;")
             self.label_47.setText("Please enter the Unit No")
             self.label_47.show()
                       
     


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SetMaster()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
