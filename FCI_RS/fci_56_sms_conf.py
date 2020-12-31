# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_27_ur_SMS.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from wt_28_SMS_HISTORY import wt_28_Ui_MainWindow
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3

class fci_56_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 769)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 711))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(40, 40, 321, 51))
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
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(440, 60, 221, 31))
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
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(830, 20, 221, 31))
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
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 130, 1061, 371))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 300, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 60, 141, 41))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(580, 60, 111, 41))
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 130, 531, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 190, 531, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 300, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(190, 180, 81, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(190, 120, 81, 31))
        self.label_6.setObjectName("label_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(600, 300, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1187, 21))
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
        self.label_19.setText(_translate("MainWindow", "SMS Activation"))
        self.label_3.setText(_translate("MainWindow", "Incorrect Password."))
        self.label_3.hide()
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.groupBox_2.setTitle(_translate("MainWindow", "SMS Activation"))
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
        self.radioButton_2.setText(_translate("MainWindow", "Activate"))
        self.radioButton_3.setText(_translate("MainWindow", "Deactivate"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.label_5.setText(_translate("MainWindow", "API Url:"))
        self.label_6.setText(_translate("MainWindow", "API Key:"))
        self.pushButton_7.setText(_translate("MainWindow", "SMS History"))
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.load_data()
        self.pushButton_5.clicked.connect(self.save_sms_dtls)
        self.radioButton_3.clicked.connect(self.disable_all)
        self.radioButton_2.clicked.connect(self.enable_all)
        #self.pushButton_7.clicked.connect(self.open_new_window)
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))

    def disable_all(self):
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        
    def enable_all(self):
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        
    def save_sms_dtls(self):
        
        print("Key :"+str(self.lineEdit_2.text()))
        print("Url :"+str(self.lineEdit_4.text()))
              
        if(self.radioButton_2.isChecked()):
            self.activation="ACTIVE"
        else:
            self.activation="DEACTIVE"
            
        
        connection = sqlite3.connect("fci.db")
        with connection:        
                cursor = connection.cursor()       
                cursor.execute("UPDATE GLOBAL_VAR SET SMS_ACTIVATION='"+self.activation+"', SMS_API_KEY='"+self.lineEdit_2.text()+"', SMS_API_URL='"+str(self.lineEdit_4.text())+"'")
        connection.commit();
        connection.close()
        self.label_3.setText("Save Successfully.")
        self.label_3.show()
        
    def load_data(self):
        connection = sqlite3.connect("fci.db")
        results=connection.execute("SELECT SMS_ACTIVATION,SMS_API_KEY , SMS_API_URL FROM GLOBAL_VAR")       
        for x in results:
              self.activation=(str(x[0]))
              if(str(self.activation) == "ACTIVE"):
                  self.radioButton_2.setChecked(True)
                  self.radioButton_3.setChecked(False)
              else:
                  self.radioButton_3.setChecked(True)
                  self.radioButton_2.setChecked(False)
                  self.disable_all()
                  
              self.lineEdit_2.setText(str(x[1])) 
              self.lineEdit_4.setText(str(x[2]))
        connection.close()
        
        print("Key :"+str(self.lineEdit_2.text()))
        print("Url :"+str(self.lineEdit_4.text()))

     

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_56_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

