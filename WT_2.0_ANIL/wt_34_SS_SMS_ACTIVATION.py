# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_34_SS_SMS_ACTIVATION.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from wt_28_SMS_HISTORY import wt_28_Ui_MainWindow
import datetime
import time
import sqlite3


class wt_34_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 701)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1121, 611))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(40, 40, 451, 51))
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
        self.label_3.setGeometry(QtCore.QRect(460, 60, 221, 31))
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
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(220, 140, 631, 121))
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
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(100, 290, 921, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(70, 340, 1061, 241))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 30, 141, 41))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(160, 30, 141, 41))
        self.radioButton_3.setObjectName("radioButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 40, 531, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(420, 90, 531, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(610, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(330, 90, 81, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(330, 40, 81, 31))
        self.label_6.setObjectName("label_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(780, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 21))
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
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.groupBox_2.setTitle(_translate("MainWindow", "SMS Activation"))
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
        self.radioButton_2.setText(_translate("MainWindow", "Activate"))
        self.radioButton_3.setText(_translate("MainWindow", "Deactivate"))
        self.pushButton_6.setText(_translate("MainWindow", "Reset"))
        self.pushButton_6.setDisabled(True)
        self.label_5.setText(_translate("MainWindow", "API Key:"))
        self.label_6.setText(_translate("MainWindow", "API Url:"))
        self.pushButton_7.setText(_translate("MainWindow", "SMS History"))
        
        self.pushButton.clicked.connect(self.login_page)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.reset_loging)
        self.pushButton_7.clicked.connect(self.open_new_window)
        
     
        self.pushButton_5.clicked.connect(self.save_sms_dtls)
        self.radioButton_3.clicked.connect(self.disable_all)
        self.radioButton_2.clicked.connect(self.enable_all)
        
        
        self.groupBox_2.hide()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
        
        
    def login_page(self):
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PWD FROM SERVICES_MST WHERE SERVICE_NAME = 'WEIGHING_MODE' AND STATUS = 'ACTIVE'") 
        for x in results:  
            if(str(self.lineEdit.text()) == str(x[0])):          
                self.go_ahead_flg="No"
                self.groupBox_2.show()
                self.load_data()
            else:
                self.label_3.setText("Incorrect Password.") 
                self.label_3.show()   
                self.groupBox_2.hide()
                 
        connection.close()    
        
    def reset_loging(self):
        self.lineEdit.setText("")         
        self.label_3.hide()
        self.groupBox_2.hide()

    def load_data(self):
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT SMS_ACTIVATION,SMS_API_URL,SMS_API_KEY   FROM USER_RIGHT_SET")       
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
        
        print("Key :"+str(self.lineEdit_4.text()))
        print("Url :"+str(self.lineEdit_2.text()))
        
        
    def disable_all(self):
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        
    def enable_all(self):
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_4.setEnabled(True) 
        
    def save_sms_dtls(self):        
        #print("Key :"+str(self.lineEdit_4.text()))
        #print("Url :"+str(self.lineEdit_2.text()))
              
        if(self.radioButton_2.isChecked()):
            self.activation="ACTIVE"
        else:
            self.activation="DEACTIVE"
            
     
        connection = sqlite3.connect("wt.db")
        with connection:        
                cursor = connection.cursor()       
                cursor.execute("UPDATE USER_RIGHT_SET SET SMS_ACTIVATION='"+self.activation+"', SMS_API_KEY='"+self.lineEdit_4.text()+"', SMS_API_URL='"+str(self.lineEdit_2.text())+"'")
        connection.commit();
        connection.close()
        self.label_3.setText("Save Successfully.")
        self.label_3.show()
     
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_28_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()   
     
     
     
     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_34_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
