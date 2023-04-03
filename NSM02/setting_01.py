from register import register_Ui_MainWindow
from loadcelll_status import loadcell_status_Ui_MainWindow
from date_time_set import date_time_set_Ui_MainWindow
from graph_scales import graph_scales_Ui_MainWindow
from factory_reset import factory_reset_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3

class B_01_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 40, 730, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 160, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(252, 210, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 160, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(119, 170, 125);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 290, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(151, 151, 176);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 160, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(188, 125, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 290, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(144, 151, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 290, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 152, 183);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./images/nms.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 100, 691, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(590, 20, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
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
        self.pushButton.setText(_translate("MainWindow", "Load cell"))
        self.pushButton_2.setText(_translate("MainWindow", "Factory Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "BreakApp"))
        self.pushButton_4.setText(_translate("MainWindow", "Graph Scale"))
        self.pushButton_5.setText(_translate("MainWindow", "DateTime"))
        self.pushButton_6.setText(_translate("MainWindow", "Register"))
        self.label_2.setText(_translate("MainWindow", "28 Mar 2023 3:12:24"))
        self.pushButton_7.setText(_translate("MainWindow", "Return"))
        self.pushButton_7.clicked.connect(MainWindow.close)
        self.pushButton_6.clicked.connect(self.open_win_reg)
        self.pushButton.clicked.connect(self.open_win_loadcell)
        self.pushButton_5.clicked.connect(self.open_win_date_time)
        self.pushButton_4.clicked.connect(self.open_win_graph_scales)
        self.pushButton_2.clicked.connect(self.open_win_factory_reset)
        self.pushButton_3.clicked.connect(self.break_app)
        self.register_button()
    
    def open_win_reg(self):       
        self.window = QtWidgets.QMainWindow()        
        self.ui=register_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_win_loadcell(self):       
        self.window = QtWidgets.QMainWindow()        
        self.ui=loadcell_status_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_win_date_time(self):       
        self.window = QtWidgets.QMainWindow()        
        self.ui=date_time_set_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_win_graph_scales(self):       
        self.window = QtWidgets.QMainWindow()        
        self.ui=graph_scales_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_win_factory_reset(self):       
        self.window = QtWidgets.QMainWindow()        
        self.ui=factory_reset_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    
    def register_button(self):
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("services.db")
        results=connection.execute("select DEVICE_SERIAL_NO from DAT_MST") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))
           if(serial_no == str(x[0])):
               #self.go_ahead="Yes"
               self.pushButton_6.hide()
           else:
               #self.go_ahead="No"
               self.pushButton_6.show()
        connection.close()
    
    def getserial(self):
        # Extract serial from cpuinfo file
        cpuserial = "0000000000000000"
        try:
           f = open('/proc/cpuinfo','r')
           for line in f:
                if line[0:6]=='Serial':
                   cpuserial = line[10:26]
           f.close()
        except:
           cpuserial = "ERROR000000000"
        return cpuserial

    def break_app(self):
        close = QMessageBox()
        close.setText("Confirm Again to Break !!")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:
                os.systbem("edxit")
        else:
                print("Not break application....")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = B_01_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
