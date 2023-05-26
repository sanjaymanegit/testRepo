
from DEF_02_RUNNING_TEST import def_02_Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import QTableWidgetItem
import sqlite3
import datetime
import sys,os
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class def_05_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 1301, 691))
        self.frame.setStyleSheet("background-color: rgb(217, 255, 235);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(1060, 40, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 570, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(132, 132, 132);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(480, 30, 521, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(940, 570, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(132, 132, 132);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)
        self.lineEdit.setValidator(input_validator)
        self.lineEdit.setGeometry(QtCore.QRect(200, 160, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(330, 160, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(70, 240, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_2)
        self.lineEdit_2.setValidator(input_validator)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 240, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(330, 240, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(70, 320, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
        self.lineEdit_3.setValidator(input_validator)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 320, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(330, 320, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(610, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(750, 160, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(610, 230, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(750, 230, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(610, 310, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        
        
        self.label_11_1 = QtWidgets.QLabel(self.frame)
        self.label_11_1.setGeometry(QtCore.QRect(610, 390, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11_1.setFont(font)        
        self.label_11_1.setObjectName("label_11_1")
        
        self.lineEdit_6_1 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_6_1)
        self.lineEdit_6_1.setValidator(input_validator)
        self.lineEdit_6_1.setGeometry(QtCore.QRect(820, 390, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6_1.setFont(font)
        self.lineEdit_6_1.setText("10")
        self.lineEdit_6_1.setObjectName("lineEdit_6_1")
        
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(750, 310, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(60, 420, 611, 231))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(20, 50, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_7)
        self.lineEdit_7.setValidator(input_validator)
        
        self.lineEdit_7.setGeometry(QtCore.QRect(280, 50, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(20, 110, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_8)
        self.lineEdit_8.setValidator(input_validator)
        self.lineEdit_8.setGeometry(QtCore.QRect(280, 110, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(440, 60, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(440, 120, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(20, 170, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_9)
        self.lineEdit_9.setValidator(input_validator)
        self.lineEdit_9.setGeometry(QtCore.QRect(280, 170, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(440, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(710, 450, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_18.setObjectName("label_18")
        
        
        self.label_18_1 = QtWidgets.QLabel(self.frame)
        self.label_18_1.setGeometry(QtCore.QRect(710, 500, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18_1.setFont(font)
        self.label_18_1.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_18_1.setText("Data Log Time (Min) :")
        self.label_18_1.setObjectName("label_18")
        
        self.lineEdit_9_1 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_9_1)
        self.lineEdit_9_1.setValidator(input_validator)
        self.lineEdit_9_1.setGeometry(QtCore.QRect(890, 500, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9_1.setFont(font)       
        self.lineEdit_9_1.setObjectName("lineEdit_9_1")
        
        
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(970, 160, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(1070, 160, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_20.setObjectName("label_20")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(1130, 570, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(132, 132, 132);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(60, 110, 1201, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.go_ahead="No"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "09 Feb 2021 11:34"))
        self.pushButton_5.setText(_translate("MainWindow", "GO FOR TEST"))
        self.label_2.setText(_translate("MainWindow", "Compression Stress Relaxation Test"))
        self.pushButton_6.setText(_translate("MainWindow", "RESET"))
        self.label_3.setText(_translate("MainWindow", "Thickness :"))
        self.label_4.setText(_translate("MainWindow", "(Mm)"))
        self.label_5.setText(_translate("MainWindow", "Width :"))
        self.label_6.setText(_translate("MainWindow", "(Mm)"))
        self.label_7.setText(_translate("MainWindow", "Diameter :"))
        self.label_8.setText(_translate("MainWindow", "(Mm)"))
        self.label_9.setText(_translate("MainWindow", "Batch ID:"))
        self.label_10.setText(_translate("MainWindow", "Party Name:"))
        self.label_11.setText(_translate("MainWindow", "Operator:"))
        self.label_11_1.setText("Comp. Thickness % :")
        self.groupBox.setTitle(_translate("MainWindow", "Test Details "))
        self.label_12.setText(_translate("MainWindow", "Max. Compressive Force :"))
        self.label_13.setText(_translate("MainWindow", "Max. Test Duration :"))
        self.label_14.setText(_translate("MainWindow", " . Kgf "))
        self.label_15.setText(_translate("MainWindow", " .hrs "))
        self.label_16.setText(_translate("MainWindow", "Temperature at Test :"))
        self.label_17.setText(_translate("MainWindow", " . C"))
        self.label_18.setText(_translate("MainWindow", "Batch Id Should Not Be Empty"))
        self.label_18.hide()
        self.label_19.setText(_translate("MainWindow", "Test ID:"))
        self.label_20.setText(_translate("MainWindow", "00001"))
        self.pushButton_7.setText(_translate("MainWindow", "RETURN"))
        self.lineEdit_9_1.setText("5")
        self.pushButton_7.clicked.connect(MainWindow.close)
        self.pushButton_5.clicked.connect(self.open_new_window)
        self.pushButton_6.clicked.connect(self.reset_fun)
        self.reset_fun()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    
    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
        
    def reset_fun(self):
        self.wifi_setup_page()
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_6_1.setText("10")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")
        connection = sqlite3.connect("def.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'TEST_MST'")       
        for x in results:           
                 self.label_20.setText(str(x[0]).zfill(4))            
        connection.close()
       
    
    def wifi_setup_page(self):
        xx=self.lineEdit_5.text()
        if(xx=="50000"):
             os.systbem("exit")
        else:
             pass
    
    def open_new_window(self):
        self.validations()
        if(self.go_ahead=="Yes"):
            self.save_test()
            self.window = QtWidgets.QMainWindow()
            #self.window =MyWin()
            self.ui=def_02_Ui_MainWindow()
            self.ui.setupUi(self.window)           
            self.window.show()
    
    def validations(self):        
        self.go_ahead="No"
        if(self.lineEdit.text() == ""):
             self.label_18.setText("Thickness is Empty.")
             self.label_18.show()  
        elif(self.lineEdit_2.text()== ""):
             self.label_18.setText("Width is Empty.")
             self.label_18.show()
        elif(self.lineEdit_3.text()== ""):
             self.label_18.setText("Diameter is Empty.")
             self.label_18.show()
        elif(self.lineEdit_7.text()== ""):
             self.label_18.setText("Max Force is Empty.")
             self.label_18.show()
        elif(self.lineEdit_8.text()== ""):
             self.label_18.setText("Test Duration is Empty.")
             self.label_18.show()
        elif(self.lineEdit_9.text()== ""):
             self.label_18.setText("Temperature is Empty.")
             self.label_18.show()
        elif(self.lineEdit_4.text()== ""):
             self.label_18.setText("Batch ID is Empty.")
             self.label_18.show()
        elif(self.lineEdit_5.text()== ""):
             self.label_18.setText("Party Name is Empty.")
             self.label_18.show()
        elif(self.lineEdit_6.text()== ""):
             self.label_18.setText("Operator Name is Empty.")
             self.label_18.show()
        elif(float(self.lineEdit.text()) <= 0):
             self.label_18.setText("Thickness should be greater than zero.")
             self.label_18.show()      
        else:
             self.go_ahead="Yes"
    
    def save_test(self):        
        if(self.go_ahead == 'Yes'):
            connection = sqlite3.connect("def.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE TEST_MST SET STATUS = 'COMPLETED_BY_NEW_TEST' WHERE STATUS='RUNNING' ")
                    cursor.execute("DELETE FROM GRAPH_MST_TMP ")
                    #cursor.execute("INSERT INTO GRAPH_MST_TMP(X_NUM,Y_NUM) VALUES  ('0.0','"+str(self.lineEdit_7.text())+"') ")
                    cursor.execute("INSERT INTO TEST_MST(THICKNESS,WIDTH,DIAMETER,MAX_FORCE,MAX_TIME,MAX_TEMP,BATCH_ID,PARTY,OPERATOR,STATUS,DATA_LOG_TIME,COMPRESS_THICKNESS_PERC)VALUES('"+self.lineEdit.text()+"','"+self.lineEdit_2.text()+"','"+self.lineEdit_3.text()+"','"+self.lineEdit_7.text()+"','"+self.lineEdit_8.text()+"','"+self.lineEdit_9.text()+"','"+self.lineEdit_4.text()+"','"+self.lineEdit_5.text()+"','"+self.lineEdit_6.text()+"','PENDING','"+self.lineEdit_9_1.text()+"','"+self.lineEdit_6_1.text()+"')")
            connection.commit();                    
            connection.close()
            self.label_18.setText("Test Started.")
            self.label_18.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = def_05_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
