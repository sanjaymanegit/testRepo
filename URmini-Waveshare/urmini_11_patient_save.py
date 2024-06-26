
from print_popup import P_POPUi_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
import datetime
import sqlite3
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY 
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import portrait,landscape, letter,inch,A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Line, Drawing

import datetime
import serial,time
import array  as arr
import numpy as np
import sqlite3
import sys
import os

class Urmini_11_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 981, 571))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(710, 160, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 40, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 480, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setDefault(True)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 480, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 85, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(520, 480, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(50, 40, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)
        self.lineEdit.setValidator(input_validator)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 113, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(600, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(40, 109, 911, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(800, 50, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(140, 150, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(270, 150, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(140, 210, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_8.setObjectName("label_8")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(270, 210, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(380, 210, 82, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(710, 330, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(850, 330, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(140, 380, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_12.setObjectName("label_12")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 380, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(170, 255, 255);\n color: rgb(0, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(550, 40, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(140, 270, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_13.setObjectName("label_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 270, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(490, 270, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(710, 270, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(710, 480, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_6)
        self.lineEdit_6.setValidator(input_validator)
        self.lineEdit_6.setGeometry(QtCore.QRect(770, 330, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        
        
        self.label_34_1 = QtWidgets.QLabel(self.frame)
        self.label_34_1.setGeometry(QtCore.QRect(270, 320, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_34_1.setFont(font)
        #self.label_34_1.setText("Error:255 fdgdfg dfgdfg ")
        self.label_34_1.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_34_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34_1.setObjectName("label_34_1")
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.graph_plot=""
        self.save_type="New"
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44:09"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.pushButton_5.setText(_translate("MainWindow", "View"))
        self.pushButton_6.setText(_translate("MainWindow", "Save"))
        self.pushButton_7.setText(_translate("MainWindow", "Print"))
        self.label_5.setText(_translate("MainWindow", "Patient ID:"))
        self.label_6.setText(_translate("MainWindow", "Created On:"))
        self.label_2.setText(_translate("MainWindow", "08 Feb 2021 11:44:09"))
        self.label_7.setText(_translate("MainWindow", "Patient ID:"))
        self.label_3.setText(_translate("MainWindow", "0001"))
        self.label_8.setText(_translate("MainWindow", "Gender:"))
        self.radioButton.setText(_translate("MainWindow", "Male"))
        self.radioButton_2.setText(_translate("MainWindow", "Female"))
        self.label_10.setText(_translate("MainWindow", "Age:"))
        self.label_11.setText(_translate("MainWindow", "Yrs."))
        self.label_12.setText(_translate("MainWindow", "Doctors :"))
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Default-Unknown"))
        
        self.pushButton_8.setText(_translate("MainWindow", "Return"))
        self.label_13.setText(_translate("MainWindow", "Name :"))
        self.pushButton_9.setText(_translate("MainWindow", "Reset"))
        self.lineEdit_6.setText(_translate("MainWindow", "0"))
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.pushButton_6.clicked.connect(self.open_new_window)
        self.load_data()
        #self.pushButton_4.clicked.connect(self.DOB_on_click)
        #self.calendarWidget.clicked.connect(self.calendar_on_click)
        #self.calendarWidget.clicked.connect(self.calendar_on_click)
        self.pushButton_9.clicked.connect(self.reset_fun)
        self.pushButton_2.clicked.connect(self.search_data)
        self.pushButton_5.clicked.connect(self.open_pdf)
        self.pushButton_7.clicked.connect(self.print_file)  
        
       
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)

    def device_date(self):     
        self.label_2.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
       
    def search_data(self):
        self.dr_id=""
        self.pcnt=0
        self.pushButton_5.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        if(self.lineEdit.text() != ""):
            connection = sqlite3.connect("ur.db")
            results=connection.execute("SELECT NAME_INITIALS,F_NAME,M_NAME,L_NAME,GENDER,AGE,DOB_STR,P_ID,CREATED_ON FROM PATIENT_MST WHERE P_ID = '"+str(int(self.lineEdit.text()))+"'") 
            for x in results:
                self.lineEdit_3.setText(str(x[1]))
                self.lineEdit_4.setText(str(x[2]))
                self.lineEdit_5.setText(str(x[3]))
                self.lineEdit_6.setText(str(x[5]))
                #self.lineEdit_2.setText(str(x[6]))
                self.label_3.setText(str(x[7]).zfill(7))
                self.pcnt=self.pcnt+1
                self.save_type="Exisitng"
                self.label.setText(str(x[8]))
                #self.label.setText("")
            connection.close()
        if(int(self.pcnt) == 0):
            #self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
        
    
    
   
        
    
    def reset_fun(self):
        self.lineEdit.setText(" ")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("0")
        #self.label_34_1.setText("")
        #self.lineEdit_2.setText(str(QDate.currentDate().toString(QtCore.Qt.ISODate)))
        self.pushButton_5.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        
        
    def load_data(self):
        connection = sqlite3.connect("ur.db")
        results=connection.execute("select seq+1 from sqlite_sequence where name = 'PATIENT_MST'")
        for x in results:           
                 self.label_3.setText(str(x[0]).zfill(7))
                 self.p_id=str(x[0])
        
        connection.close()
        print("Inside load_data")
        self.comboBox_2.clear
        self.i=1
        self.dr_id_arr=["None"]
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT 'Dr.'||fname||' '||mname||' '||lname||'('||DR_QUAL||')',DR_ID FROM DOCTORS_INFO") 
        for x in results:            
            self.comboBox_2.addItem("")
            self.dr_id_arr.append(str(x[1]))
            self.comboBox_2.setItemText(self.i,str(x[0]))
            self.i=self.i+1
        connection.close()
        #self.lineEdit_2.setText(str(QDate.currentDate().toString(QtCore.Qt.ISODate)))
        self.pushButton_5.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        
    def open_new_window(self):
        #self.label_34_1.hide()        
        if(self.lineEdit_3.text()==""):
               self.label_34_1.setText("Error: First Name should not empty")
               self.label_34_1.show()
        elif(self.lineEdit_6.text()==""):
               self.label_34_1.setText("Error: Age should not empty")
               self.label_34_1.show()
        elif(self.lineEdit_5.text()==""):
               self.label_34_1.setText("Error: Last Name should not empty")
               self.label_34_1.show()
        elif(str(self.lineEdit_6.text()) == "0"):
               self.label_34_1.setText("Error: Age Should be greater than 0")
               self.label_34_1.show()       
        else:
            print("okk");
            self.save_data()        
           
            
    
    def save_data(self):
        
        if(self.lineEdit_3.text() != "" and  self.lineEdit_5.text() != ""):
                #print(" self.save_type :"+str(self.save_type))
                self.intials=""
                self.f_name=self.lineEdit_3.text()
                self.m_name=self.lineEdit_4.text()
                self.l_name=self.lineEdit_5.text()
                self.p_id=str(int(self.label_3.text()))
                if(self.radioButton_2.isChecked()):
                    self.gender="Female"
                else:
                    self.gender="Male"
                    
                self.age=self.lineEdit_6.text()
                self.dob_str=""
                self.last_test_id=""
                
                if(self.save_type == "New"):
                            connection = sqlite3.connect("ur.db")              
                            with connection:        
                                  cursor = connection.cursor()                                
                                  cursor.execute("insert INTO PATIENT_MST (NAME_INITIALS,F_NAME,M_NAME,L_NAME,GENDER,AGE,DOB_STR,LAST_TEST_ID,CREATED_ON) VALUES ('"+self.intials+"','"+self.f_name+"','"+self.m_name+"','"+self.l_name+"','"+self.gender+"','"+self.age+"','"+self.dob_str+"','"+self.last_test_id+"',current_timestamp)")                                
                            connection.commit();
                            connection.close()
                else:           
                            connection = sqlite3.connect("ur.db")              
                            with connection:        
                                  cursor = connection.cursor()                                
                                  cursor.execute("UPDATE PATIENT_MST SET NAME_INITIALS='"+self.intials+"',F_NAME='"+self.f_name+"',M_NAME='"+self.m_name+"',L_NAME='"+self.l_name+"',GENDER='"+self.gender+"',AGE='"+self.age+"',DOB_STR='"+self.dob_str+"',LAST_TEST_ID='"+self.last_test_id+"' where P_ID='"+str(self.p_id)+"'")
                            connection.commit();
                            connection.close()     
                                
               
                connection = sqlite3.connect("ur.db")              
                with connection:        
                        cursor = connection.cursor()
                        cursor.execute("UPDATE GLOBAL_VAR_TEST SET   p_id='"+str(self.label_3.text())+"', DR_NAME='"+str(self.comboBox_2.currentText())+"'")                          
                connection.commit();
                connection.close()
                 
                ## load test_mst 
                ## load graph_mst ,graph_mst2 tables
                ##UPDATE graph_mst , graph_mst2, test_mst for graphi_id
                connection = sqlite3.connect("ur.db")              
                with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("INSERT INTO TEST_MST(DR_NAME,TEST_START_ON,TEST_END_ON,ELAPSED_TIME,MAX_FLOW,MAX_FLOW_DEV,"+
                                       "AVG_FLOW,AVG_FLOW_DEV,VOIDING_TIME,VOIDING_TIME_DEV,FLOW_TIME,TIME_TO_MAX_FLOW,TIME_TO_MAX_FLOW_DEV,"+
                                       "VOIDED_VOL,FLOW_AT_2_SEC,ACCEL,VOLUMN_TIME_X,VOLUMN_TIME_Y,FLOW_TIME_X,FLOW_TIME_Y,TOTAL_VOLUMN,P_ID,HESITANCY_TIME) "+
                                       "SELECT DR_NAME,TEST_START_ON,TEST_END_ON,ELAPSED_TIME,MAX_FLOW,MAX_FLOW_DEV,AVG_FLOW,AVG_FLOW_DEV,VOIDING_TIME,"+
                                       "VOIDING_TIME_DEV,FLOW_TIME,TIME_TO_MAX_FLOW,TIME_TO_MAX_FLOW_DEV,VOIDED_VOL,FLOW_AT_2_SEC,ACCEL,VOLUMN_TIME_X,"+
                                       "VOLUMN_TIME_Y,FLOW_TIME_X,FLOW_TIME_Y,TOTAL_VOLUMN,P_ID,HESITANCY_TIME FROM GLOBAL_VAR_TEST")
                connection.commit();
                connection.close()
                print("TEST_MST - Populated.")
                connection = sqlite3.connect("ur.db")              
                with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM) SELECT X_NUM,Y_NUM FROM GRAPH_MST_TMP")
                        cursor.execute("INSERT INTO GRAPH_MST2(X_NUM,Y_NUM) SELECT X_NUM,Y_NUM FROM GRAPH_MST_TMP2")
                        cursor.execute("UPDATE PATIENT_MST SET LAST_TEST_ID = (SELECT MAX(TEST_ID) FROM TEST_MST) WHERE LAST_TEST_ID IS NULL")
                connection.commit();
                connection.close()
                print("GRAPH_MST,GRAPH_MST2 - Populated.") 
                 
                connection = sqlite3.connect("ur.db")
                results=connection.execute("SELECT IFNULL(max(GRAPHI_ID),0)+1 FROM GRAPH_MST") 
                for x in results:
                    self.graph_id=str(x[0])                   
                connection.close()
                connection = sqlite3.connect("ur.db")
                results=connection.execute("SELECT IFNULL(max(GRAPHI_ID),0)+1 FROM GRAPH_MST2") 
                for x in results:
                    self.graph_id2=str(x[0])
                connection.close()
                #print("item index :"+str(self.comboBox_2.currentIndex()))
                print("item data :"+str(self.comboBox_2.itemData(0)))
                #print("item text :"+str(self.comboBox_2.currentIndex()))
                
                self.dr_id=0
                self.dr_name=""              
                #print(" array :"+str(self.dr_id_arr))
                #print("self.comboBox_2.currentIndex :"+str(self.comboBox_2.currentIndex()))
                self.dr_id=str(self.dr_id_arr[self.comboBox_2.currentIndex()])
                self.dr_name=self.comboBox_2.currentText()
                #print("self.dr_id :"+str(self.dr_id))
                connection = sqlite3.connect("ur.db")              
                with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("UPDATE GRAPH_MST SET GRAPHI_ID='"+str(self.graph_id)+"' WHERE GRAPHI_ID IS NULL")
                        cursor.execute("UPDATE GRAPH_MST2 SET GRAPHI_ID='"+str(self.graph_id2)+"' WHERE GRAPHI_ID IS NULL")
                        cursor.execute("UPDATE TEST_MST SET GRAPHI_ID='"+str(self.graph_id)+"',  GRAPHI_ID2='"+str(self.graph_id2)+"', DR_ID='"+str(self.dr_id)+"', DR_NAME='"+self.dr_name+"' WHERE TEST_ID  in (SELECT MAX(TEST_ID) FROM TEST_MST)")
                connection.commit();
                connection.close()
                
                print("GRAPH_MST,GRAPH_MST2,TEST_MST - updated with graph id :"+str(self.graph_id)+" graph id 2:"+str(self.graph_id2)) 
                print("data saved")
                self.label_34_1.setText("Test Saved Successfully.")
                self.label_34_1.show()
                self.graph_plot =PlotCanvas_blank(self,width=8, height=6,dpi=80)
                self.pushButton_5.setEnabled(True)
                self.pushButton_7.setEnabled(True)
        else:
                print(" Names are required.")
                
    
    def create_pdf(self):
        y=300
        Elements=[]        
        self.dr_name=""
        self.test_id=""
        self.remark=""
        self.p_name=""
        self.report_date=""
        summary_data=[]
        test_data=[]
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT TEST_ID,TEST_START_ON,DR_NAME FROM TEST_MST ORDER BY TEST_ID DESC LIMIT 1 ")
        for x in results:
            summary_data=[["Test No:        ",str(x[0]).zfill(6),"Tested Date:        ",str(x[1])[0:10]]]
            self.test_id=str(x[0])
            self.dr_name=str(x[2])
        connection.close()
        
        
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT NAME_INITIALS||' '||F_NAME||' '||M_NAME||' '||L_NAME,GENDER,AGE,current_timestamp FROM PATIENT_MST WHERE P_ID IN (SELECT P_ID FROM GLOBAL_VAR_TEST)")
        for x in results:
            summary_data.append(["Patient Name : ",str(x[0]),"Age: ",str(x[2])])
            self.p_name=str(x[0])
            summary_data.append(["Doctors Name:",str(self.dr_name),"Gender:",str(x[1])])
            #summary_data.append(["Report Date: ",str(x[3])[0:10],"",""])
            self.report_date=str(x[3])[0:16]
        
        connection.close()
        test_data=[["  Parameters      ","        Value      ","          Standard Deviation %                   "]]
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT round(MAX_FLOW,2),round(MAX_FLOW_DEV,2),round(AVG_FLOW,2),round(AVG_FLOW_DEV,2),round(VOIDING_TIME,2),"+
                                   "round(VOIDING_TIME_DEV,2),round(FLOW_TIME,2),round(TIME_TO_MAX_FLOW,2),round(TIME_TO_MAX_FLOW_DEV,2),round(VOIDED_VOL,2),round(FLOW_AT_2_SEC,2),round(ACCEL,2),"+
                                   "round(TOTAL_VOLUMN,2) ,DR_COMMNETS,HESITANCY_TIME FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_TEST)")
        for x in results:
                  '''
                  test_data.append(["Max. Flow (ml/sec)    ",str(x[0]),"Vol  SD (%): "+str(x[1])   ])
                  test_data.append(["Avg. Flow (ml/sec)    ",str(x[2]),"Flow SD (%): "+str(x[3])   ])
                  test_data.append(["Voiding Time(sec)     ",str(x[4]),"--"    ])
                  test_data.append(["Flow Time (sec)       ",str(x[6]),"--"   ])
                  test_data.append(["Time to Max Flow(sec) ",str(x[7]),"--"    ])
                  test_data.append(["Voided Vol (ml)       ",str(x[9]),"--"   ])
                  test_data.append(["Flow at 2 sec.        ",str(x[10]),"--"   ])
                  test_data.append(["Accelaration     ",str(x[11]),"-- "   ])
                  test_data.append(["Hesitancy Time (sec)    ",str(x[14]),"-- "   ])
                  self.remark="xxxx"
                  '''
                  
                  test_data.append(["Voided Vol (ml)    ",str(x[9]),"Vol  SD (%): "+str(x[1])   ])
                  test_data.append(["Max. Flow (ml/sec)    ",str(x[0]),"Flow SD (%): "+str(x[3])   ])
                  test_data.append(["Avg. Flow (ml/sec)     ",str(x[2]),"--"    ])
                  test_data.append(["Flow Time (sec)       ",str(x[6]),"--"   ])
                  test_data.append(["Voiding Time(sec)  ",str(x[4]),"--"    ])
                  test_data.append(["Time to Max Flow(sec)      ",str(x[7]),"--"   ])
                  test_data.append(["Flow at 2 sec.        ",str(x[10]),"--"   ])
                  test_data.append(["Accelaration     ",str(x[11]),"-- "   ])
                  test_data.append(["Hesitancy Time (sec)  ",str(x[14]),"-- "   ])
                  self.remark="xxxx"
                  
        connection.close()
        
        
        
        
        
        
        
        
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        
        connection = sqlite3.connect("ur.db")
        results=connection.execute("select UPPER(ORG_NAME),ORG_ADDR from OTER_INFO") 
        for x in results:
            ptext = "<font name=Helvetica size=14>"+str(x[0])+" </font>"   
            Title = Paragraph(str(ptext), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
            ptext = "\n <font name=Helvetica size=16> <b> Report as on "+str(self.label_2.text())+" </b></font>"            
            Title3 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        
        line=Paragraph("           ___________________________________________________________________________________________", styles["Normal"])
        spaceline=Paragraph("  \n", styles["Normal"])
        blank=Paragraph(" --------------------------------------------------------------------------------------------------------------------------------------------------     \n", styles["Normal"])
        ptext = "<font name=Helvetica size=10>         Remark : </font>"           
           
        comments = Paragraph(str(ptext)+" ------------------------------------------------------------------------------------------------------------------------------- -\n", styles["Normal"])
        
        footer_2= Paragraph("\n Ark medico software division", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
       
        
        if(len(summary_data) > 0):
            f3=Table(summary_data)
            f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10)]))       
            
            f4=Table(test_data)
            f4.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
            
            report_gr_img="last_graph.png"        
            pdf_img= Image(report_gr_img, 7 * inch, 5 * inch)
            
            
            Elements=[Title3,Title,Title2,line,Spacer(1,12),Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f4,Spacer(1,12),comments,blank,footer_2,Spacer(1,12)]
            
            
            
            doc = SimpleDocTemplate('./reports/ur_reports.pdf', rightMargin=10,
                                    leftMargin=30,
                                    topMargin=10,
                                    bottomMargin=10)
            doc.build(Elements)
        #print("Done")

    def print_file(self):        
        self.create_pdf()
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POPUi_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def open_pdf(self):
        self.create_pdf()
        os.system("xpdf ./reports/ur_reports.pdf") 
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                os.system("cp ./reports/ur_reports.pdf /media/usb/ur_reports_"+str(self.test_id)+".pdf")
                os.system("sudo umount /media/usb")
        else:
             print("Please connect usb storage device")

    def get_usb_storage_id(self):
        os.system("rm -rf lsusb_data.txt")  
        product_id = "ERROR"
        os.system("lsusb >> lsusb_data.txt")
        try:
           f = open('lsusb_data.txt','r')
           for line in f:
               cnt=0                
               cnt=int(line.find("SanDisk"))
               if cnt > 0 :                   
                   product_id = line[28:33]
                   product_id = "0x"+str(product_id)
           f.close()
        except:
           product_id = "ERROR"
        return product_id
        
class PlotCanvas_blank(FigureCanvas):
    def __init__(self, parent=None, width=5, height=2, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(211)        
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot_graph()        
        
    def plot_graph(self):
        self.graph_id="0"
        self.graph_id2="0"
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT GRAPHI_ID, GRAPHI_ID2 FROM TEST_MST ORDER BY TEST_ID DESC LIMIT 1") 
        for x in results:
            self.graph_id=str(x[0])
            self.graph_id2=str(x[1])
        connection.close()
        
        self.x=[0.0]
        self.y=[0.0]
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE GRAPHI_ID='"+str(self.graph_id)+"'")
        for k in results:        
                self.x.append(k[0])
                self.y.append(k[1])
        connection.close()
       
        ax = self.figure.add_subplot(212)
        #ax.set_facecolor('#CCFFFF')
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.2', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.2', color='black')
        
        connection = sqlite3.connect("ur.db")       
        results=connection.execute("SELECT VOLUMN_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS FROM OTER_INFO")
        rows=results.fetchall()
        if(len(rows) == 0 ):
                ax.set_xlim(0,0)
                ax.set_ylim(0,0)
        else:
                ax.set_xlim(0,int(rows[0][1]))
                ax.set_ylim(0,int(rows[0][0]))
        connection.close()
        
        #ax.set_xlim(0,10)
        #ax.set_ylim(0,100)
       
        ax.plot(self.x,self.y,'#04756A')
        ax.set_ylabel('Volumn (ml)')
        ax.set_xlabel('Time (sec)')
        
       
        
        self.x1=[0.0]
        self.y1=[0.0]
        
        ax = self.figure.add_subplot(211)
        self.p_name=""
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT NAME_INITIALS||' '||F_NAME||' '||M_NAME||' '||L_NAME,GENDER,AGE,current_timestamp FROM PATIENT_MST WHERE P_ID IN (SELECT P_ID FROM GLOBAL_VAR_TEST)")
        for x in results:            
            self.p_name=str(x[0])
        connection.close()  
        
        
        ax.set_title('Uroflowmetry Report of '+str(self.p_name))
        #ax.set_facecolor('#CCFFFF')
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.2', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.2', color='black')
        
        
        connection = sqlite3.connect("ur.db")       
        results=connection.execute("SELECT FLOW_TIME_Y_AXIS,FLOW_TIME_X_AXIS FROM OTER_INFO")        
        for x in results:
                ax.set_xlim(0,int(x[1]))
                ax.set_ylim(0,int(x[0]))
        connection.close()
        
        #ax.set_xlim(0,10)
        #ax.set_ylim(0,1000)
        
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST2 WHERE  GRAPHI_ID='"+str(self.graph_id2)+"'")
        for k in results:        
                self.x1.append(k[0])
                self.y1.append(k[1])
        connection.close()
              
        ax.plot(self.x1,self.y1,'#04756A')
        ax.set_ylabel('Flow (ml/sec)')
        ax.set_xlabel('Time (sec)')
        
        
        self.figure.savefig('last_graph.png',dpi=80)
        self.draw()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Urmini_11_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
