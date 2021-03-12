# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TY_08_TEST_CONF.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3


class TY_08_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 701)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 40, 1100, 625))
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
        self.label_3.setGeometry(QtCore.QRect(450, 50, 221, 31))
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
        self.groupBox.setGeometry(QtCore.QRect(230, 120, 631, 121))
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
        self.line.setGeometry(QtCore.QRect(20, 270, 1071, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 320, 1051, 261))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(80, 90, 131, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(340, 90, 171, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(620, 90, 141, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(850, 90, 141, 31))
        self.checkBox_4.setObjectName("checkBox_4")
        
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setGeometry(QtCore.QRect(80, 120, 141, 31))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_6.setGeometry(QtCore.QRect(340, 120, 141, 31))
        self.checkBox_6.setObjectName("checkBox_6")
        
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
        self.label_19.setText(_translate("MainWindow", "Test Configuration"))
        self.label_3.setText(_translate("MainWindow", "Incorrect Password."))
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Test Configuration"))
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
        self.checkBox.setText(_translate("MainWindow", "Tensile Test"))
        self.checkBox_2.setText(_translate("MainWindow", "Compression Test"))
        self.checkBox_3.setText(_translate("MainWindow", "Tear Test"))
        self.checkBox_4.setText(_translate("MainWindow", "Flexural Test"))
        self.checkBox_5.setText(_translate("MainWindow", "QLSS"))
        self.checkBox_6.setText(_translate("MainWindow", "ILSS"))
        
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.login_page)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.reset_loging)
        
        self.label_3.hide()
        self.groupBox_2.hide()
        
        self.pushButton_5.clicked.connect(self.save_data)
        self.load_data()
          
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
     

    def login_page(self):
         if(str(self.lineEdit.text()) == 'singhisking'):          
                self.go_ahead_flg="No"
                self.groupBox_2.show()
                self.load_data()
         else:
                self.label_3.setText("Incorrect Password.") 
                self.label_3.show()   
                self.groupBox_2.hide()
                 
          
        
    def reset_loging(self):
        self.lineEdit.setText("")         
        self.label_3.hide()
        self.groupBox_2.hide()
    
    def load_data(self):      
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TENSILE_TEST_FLG,COMPRESS_TEST_FLG,TARE_TEST_FLG,flexural_test,QLSS_TEST,ILSS_TEST FROM GLOBAL_VAR") 
        for x in results:            
            if(str(x[0])=='ACTIVE'):
                self.checkBox.setChecked(True)
            else:
                self.checkBox.setChecked(False)
                
            if(str(x[1])=='ACTIVE'):
                self.checkBox_2.setChecked(True)
            else:
                self.checkBox_2.setChecked(False)    
                
            if(str(x[2])=='ACTIVE'):
                self.checkBox_3.setChecked(True)
            else:
                self.checkBox_3.setChecked(False)
                
            if(str(x[3])=='ACTIVE'):
                self.checkBox_4.setChecked(True)
            else:
                self.checkBox_4.setChecked(False)
            
            if(str(x[4])=='ACTIVE'):
                self.checkBox_5.setChecked(True)
            else:
                self.checkBox_5.setChecked(False)
            
            if(str(x[5])=='ACTIVE'):
                self.checkBox_6.setChecked(True)
            else:
                self.checkBox_6.setChecked(False) 
                
        connection.close()
        self.label_3.hide() 
     
    def save_data(self):        
        if(self.checkBox.isChecked()):
            self.tensile_flg='ACTIVE'
        else:
            self.tensile_flg='DEACTIVE'
        
        if(self.checkBox_2.isChecked()):
            self.compress_flg='ACTIVE'
        else:
            self.compress_flg='DEACTIVE'
            
        if(self.checkBox_3.isChecked()):
            self.tare_flag='ACTIVE'
        else:
            self.tare_flag='DEACTIVE'    
        
        if(self.checkBox_4.isChecked()):
            self.flx_flag='ACTIVE'
        else:
            self.flx_flag='DEACTIVE'
        
        if(self.checkBox_5.isChecked()):
            self.qlss_flag='ACTIVE'
        else:
            self.qlss_flag='DEACTIVE'    
        
        if(self.checkBox_6.isChecked()):
            self.ilss_flag='ACTIVE'
        else:
            self.ilss_flag='DEACTIVE'
            
        connection = sqlite3.connect("tyr.db")          
        with connection:        
                cursor = connection.cursor()                    
                cursor.execute("UPDATE GLOBAL_VAR SET TENSILE_TEST_FLG = '"+str(self.tensile_flg)+"',COMPRESS_TEST_FLG='"+str(self.compress_flg)+"',TARE_TEST_FLG='"+str(self.tare_flag)+"' , flexural_test='"+str(self.flx_flag)+"',QLSS_TEST='"+str(self.qlss_flag)+"',ILSS_TEST='"+str(self.ilss_flag)+"'") 
        connection.commit();
        connection.close()
        self.label_3.setText("Configuration Saved.") 
        self.label_3.show()   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_08_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
