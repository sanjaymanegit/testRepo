# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_10_setting_menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from wt_11_sett_services_list import wt_11_Ui_MainWindow
from wt_12_sett_user_rights import wt_12_Ui_MainWindow
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os

class wt_10_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 40, 1261, 651))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet("background-color: rgb(255, 239, 242);")
        self.frame.setObjectName("frame")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 210, 391, 251))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(720, 210, 421, 261))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        
        
        self.pushButton_5_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5_1.setGeometry(QtCore.QRect(520, 550, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)       
        self.pushButton_5_1.setFont(font)
        self.pushButton_5_1.setObjectName("pushButton_5_1")
        
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(410, 60, 291, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 0, 127);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(1050, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
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
        self.pushButton_4.setText(_translate("MainWindow", "Services"))
        self.pushButton_5.setText(_translate("MainWindow", "User Rights"))
        self.pushButton_5_1.setText(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", "Setting"))
        self.label_2.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.pushButton_4.clicked.connect(self.open_new_window)
        self.pushButton_5.clicked.connect(self.open_new_window2)
        self.pushButton_5_1.clicked.connect(MainWindow.close)
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_2.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
   
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_11_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_12_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_10_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
