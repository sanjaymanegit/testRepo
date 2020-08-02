# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_12_sett_user_rights.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from wt_37_update_record import wt_37_Ui_MainWindow
from wt_23_ur_COMPANY_INFO import wt_23_Ui_MainWindow
from wt_25_ur_MASTER import wt_25_Ui_MainWindow
from wt_27_ur_SMS import wt_27_Ui_MainWindow
from pop_datetime import DATE_Ui_MainWindow


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3

class wt_12_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1321, 711))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 50, 181, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(270, 10, 631, 111))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 141, 31))
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(210, 50, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 50, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 50, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 150, 1221, 521))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 70, 301, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_6_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6_1.setGeometry(QtCore.QRect(830, 70, 301, 61))
        self.pushButton_6_1.setObjectName("pushButton_6")
        
        
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 70, 261, 61))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setGeometry(QtCore.QRect(90, 200, 261, 61))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setGeometry(QtCore.QRect(430, 200, 261, 61))
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(930, 40, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(1080, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
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
        self.label.setText(_translate("MainWindow", "User Rights"))
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.groupBox_2.setTitle(_translate("MainWindow", "List"))
        self.pushButton_6.setText(_translate("MainWindow", "SMS - Activation"))
        self.pushButton_6_1.setText(_translate("MainWindow", "Company Information"))
        self.pushButton_9.setText(_translate("MainWindow", "Master Data Update"))
        self.pushButton_13.setText(_translate("MainWindow", "Update / Delete Record"))
        self.pushButton_14.setText(_translate("MainWindow", "Date Time Setting"))
        self.label_2.setText(_translate("MainWindow", "Incorrect Password !!!!"))
        self.label_3.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.pushButton.clicked.connect(self.show_page)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.reset_fun)
        self.label_2.hide()
        self.groupBox_2.hide()
        self.pushButton_9.clicked.connect(self.open_new_window3)
        self.pushButton_6.clicked.connect(self.open_new_window5)
        self.pushButton_6.hide()
        self.pushButton_6_1.clicked.connect(self.open_new_window2)
        self.pushButton_6_1.hide()
        self.pushButton_13.clicked.connect(self.open_new_window)
        #self.pushButton_13.hide()
        self.pushButton_14.clicked.connect(self.open_new_window4)
        self.pushButton_14.hide()
       
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_3.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
           
        
    def show_page(self):
        connection = sqlite3.connect("wt.db")
        results=connection.execute("select UR_PWD from USER_RIGHT_SET")       
        for x in results:        
              self.password_str=str(x[0])
        connection.close()
        
        if(self.password_str == str(self.lineEdit.text())):
            self.groupBox_2.show()
            self.label_2.hide()
        else:
            self.label_2.show()
            self.groupBox_2.hide()
        
    def reset_fun(self):
        self.label_2.hide()
        self.groupBox_2.hide()
        self.lineEdit.setText("")
    
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_37_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_23_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window3(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_25_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window4(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=DATE_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window5(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_27_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_12_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
