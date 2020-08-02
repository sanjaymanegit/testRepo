# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_25_ur_MASTER.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from pop_party import POP_PARTY_Ui_MainWindow
from pop_vehicle_no import POP_vehicle_Ui_MainWindow
from pop_transport import POP_TRANS_Ui_MainWindow
from wt_26_ur_TARE_CONF import wt_26_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3

class wt_25_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1181, 683)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1111, 591))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(160, 60, 521, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(850, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(90, 180, 911, 231))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(70, 90, 111, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 90, 111, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(480, 90, 111, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_11.setGeometry(QtCore.QRect(670, 90, 151, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(490, 460, 111, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1181, 21))
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
        self.label_19.setText(_translate("MainWindow", "Master Information Update"))
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Master Data Modifications"))
        self.pushButton_7.setText(_translate("MainWindow", "Party Data"))
        #self.pushButton_7.setDisabled(True)
        self.pushButton_8.setText(_translate("MainWindow", "Vehicle Nos."))
        self.pushButton_9.setText(_translate("MainWindow", "Transport Data"))
        self.pushButton_11.setText(_translate("MainWindow", "Tare Weights Data"))
        self.pushButton_10.setText(_translate("MainWindow", "Return"))
        self.pushButton_10.clicked.connect(MainWindow.close)
        
        self.pushButton_7.clicked.connect(self.pop_party_window)
        self.pushButton_8.clicked.connect(self.pop_vehicle_window)
        self.pushButton_9.clicked.connect(self.pop_trans_window)
        self.pushButton_11.clicked.connect(self.open_tare_window)
        
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))

    def pop_party_window(self):         
        self.window = QtWidgets.QMainWindow()
        self.ui=POP_PARTY_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def pop_vehicle_window(self):         
        self.window = QtWidgets.QMainWindow()
        self.ui=POP_vehicle_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()     
    
    def pop_trans_window(self):         
        self.window = QtWidgets.QMainWindow()
        self.ui=POP_TRANS_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_tare_window(self):         
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_26_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()          

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_25_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
