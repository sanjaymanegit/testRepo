# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ur_15_pop_print.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class wt_37_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 270)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(10, 10, 581, 231))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 541, 201))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox)
        reg_ex = QRegExp("[0-9]+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_11)
        self.lineEdit_11.setValidator(input_validator)
        self.lineEdit_11.setGeometry(QtCore.QRect(170, 50, 61, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(420, 50, 111, 31))
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(60, 50, 101, 31))
        self.label_14.setObjectName("label_14")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(280, 50, 111, 31))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(340, 120, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reports"))
        self.groupBox.setTitle(_translate("MainWindow", "Print Slip"))
        self.radioButton_3.setText(_translate("MainWindow", "Plain Paper"))
        self.pushButton_6.setText(_translate("MainWindow", "Close"))
        self.label_14.setText(_translate("MainWindow", "No. Of Copies:"))
        self.pushButton_7.setText(_translate("MainWindow", "Print"))
        self.radioButton_4.setText(_translate("MainWindow", "Pre-Printed"))
        self.label_2.setText(_translate("MainWindow", "Print started."))
        self.label_2.hide()
        self.lineEdit_11.setText("1")
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PRE_PRINT_FLAG, PRINTER_NAME FROM DEVICE_CONF") 
        for x in results:            
            if(str(x[0])=='ACTIVE'):
                    self.radioButton_3.setChecked(False)
                    self.radioButton_4.setChecked(True) #Pre - printed
                    self.radioButton_3.setDisabled(True)
                         
            else:
                    self.radioButton_3.setChecked(True)
                    self.radioButton_4.setChecked(False) #Pre - printed
                    self.radioButton_4.setDisabled(True)
                    
        connection.close()
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_7.clicked.connect(self.print_fun)
   
    def print_fun(self):
        if(self.lineEdit_11.text() != ''):
            if(self.lineEdit_11.text() != ' '):
                 for x in range(int(self.lineEdit_11.text())):
                     #print("printing:"+str(x))
                     os.system("./job_print_recipt.sh")
                     self.label_2.show()
                     self.pushButton_7.setDisabled(True)
            else:
                 print("Space Issued in lineedit_5")
                 self.label_2.hide()
        else:
            print("empty copies")
            self.label_2.hide()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_37_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
