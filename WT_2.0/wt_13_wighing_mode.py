# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_13_wighing_mode.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from wt_32_public_weighing import wt_32_Ui_MainWindow


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
from wt_04_weight_1 import wt_04_1_Ui_MainWindow
import sqlite3


class wt_13_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 40, 1261, 641))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet("background-color: rgb(255, 239, 242);")
        self.frame.setObjectName("frame")
        
        self.camera_active_flg="DEACTIVE"
        
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 270, 341, 151))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 270, 251, 151))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        
        
        
        self.pushButton_5_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5_1.setGeometry(QtCore.QRect(520, 550, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)       
        self.pushButton_5_1.setFont(font)
        self.pushButton_5_1.setObjectName("pushButton_5_1")
        
        
        
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 270, 241, 151))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(380, 110, 431, 91))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(480, 30, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
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
        self.pushButton.setText(_translate("MainWindow", "Regular Weighing"))
        self.pushButton_2.setText(_translate("MainWindow", "Public Weighing"))
        self.pushButton_3.setText(_translate("MainWindow", "Multi Weighing"))
        self.pushButton_5_1.setText(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", "Weighing"))
        self.label_2.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        
        self.pushButton_5_1.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.open_new_window3)
        
        
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT DISTINCT STATUS FROM CAMERA_CONF WHERE STATUS='ACTIVE'")       
        for x in results:
            self.camera_active_flg=str(x[0])        
        connection.close()        

        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT WEIGHING_PUBLIC_FLG,WEIGHING_MODE_FLG FROM SERIVES_SET")       
        for x in results:
              if(str(x[0]) =="ACTIVE"):                  
                  self.pushButton_2.setEnabled(True)
                  self.pushButton_2.clicked.connect(self.open_new_window3)
              else:
                  self.pushButton_2.setDisabled(True)
                  
              if(str(x[1]) =="ACTIVE"):
                  if(self.camera_active_flg=='ACTIVE'):
                      self.pushButton.setEnabled(True)
                      self.pushButton.clicked.connect(self.open_new_window4)
                  else:                      
                      self.pushButton.setEnabled(True)
                      self.pushButton.clicked.connect(self.open_new_window2)
              else:
                  self.pushButton.setDisabled(True)   
                  
        connection.close()

        self.pushButton_3.setDisabled(True)
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_2.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
           
   
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_04_1_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_32_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()        
        
    def open_new_window4(self):
        from wt_29_weight_cam import wt_29_Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_29_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()                     
               
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_13_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
