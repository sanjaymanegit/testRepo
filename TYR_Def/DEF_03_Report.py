# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '03_Report.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from print_popup import P_POPUi_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
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


class def_03_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 1321, 691))
        self.frame_2.setStyleSheet("background-color: rgb(217, 255, 235);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(1080, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(590, 70, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 138, 144);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(790, 70, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 138, 144);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(20, 150, 1291, 21))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(800, 600, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 138, 144);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_12.setGeometry(QtCore.QRect(990, 70, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 138, 144);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(780, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(920, 380, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(1060, 380, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(1170, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(780, 310, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_2)
        self.label_25.setGeometry(QtCore.QRect(780, 260, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(920, 260, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_26 = QtWidgets.QLabel(self.frame_2)
        self.label_26.setGeometry(QtCore.QRect(1100, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(920, 310, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_27 = QtWidgets.QLabel(self.frame_2)
        self.label_27.setGeometry(QtCore.QRect(780, 210, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(920, 210, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(1060, 480, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(1060, 430, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setGeometry(QtCore.QRect(780, 480, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(920, 480, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(920, 430, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_20 = QtWidgets.QLabel(self.frame_2)
        self.label_20.setGeometry(QtCore.QRect(780, 430, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_13.setGeometry(QtCore.QRect(960, 600, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 138, 144);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_14.setGeometry(QtCore.QRect(1120, 600, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(255, 138, 144);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(30, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setGeometry(QtCore.QRect(360, 80, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_22 = QtWidgets.QLabel(self.frame_2)
        self.label_22.setGeometry(QtCore.QRect(240, 80, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_22.setObjectName("label_22")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(30, 180, 721, 491))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.test_id=""
        self.delete_all_flg=1
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "09 Feb 2021 11:34"))
        self.pushButton_9.setText(_translate("MainWindow", "GET REPORT"))
        self.pushButton_10.setText(_translate("MainWindow", "RESET"))
        
        self.pushButton_11.setText(_translate("MainWindow", "PRINT"))
        self.pushButton_12.setText(_translate("MainWindow", "RETURN"))
        self.label_13.setText(_translate("MainWindow", "Thickness :"))
        self.label_15.setText(_translate("MainWindow", "(Mm)"))
        self.label_23.setText(_translate("MainWindow", ""))
        self.label_24.setText(_translate("MainWindow", "Operator:"))
        self.label_25.setText(_translate("MainWindow", "Party Name:"))
        self.label_26.setText(_translate("MainWindow", "Test ID:"))
        self.label_27.setText(_translate("MainWindow", "Batch ID:"))
        self.label_17.setText(_translate("MainWindow", "(Mm)"))
        self.label_18.setText(_translate("MainWindow", "(Mm)"))
        self.label_19.setText(_translate("MainWindow", "Diameter :"))
        self.label_20.setText(_translate("MainWindow", "Width :"))
        self.pushButton_13.setText(_translate("MainWindow", "VIEW"))
        self.pushButton_14.setText(_translate("MainWindow", "DELETE"))
        self.radioButton.setText(_translate("MainWindow", "TEST ID "))
        self.radioButton_2.setText(_translate("MainWindow", "BATCH ID"))
        
        self.label_22.setText(_translate("MainWindow", "OR"))
        self.label_21.setText(_translate("MainWindow", "PRINT STARTED ...."))
        self.pushButton_12.clicked.connect(MainWindow.close)
        self.radioButton.clicked.connect(self.test_onlick)
        self.radioButton_2.clicked.connect(self.batch_onlick)
        self.pushButton_9.clicked.connect(self.load_test_data)
        self.pushButton_14.clicked.connect(self.delete_test)
        self.pushButton_10.clicked.connect(self.reset_fun)
        self.pushButton_13.clicked.connect(self.open_pdf)
        self.pushButton_11.clicked.connect(self.print_file) 
        
        
        self.load_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    
    def device_date(self):     
        self.label_9.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    
    def test_onlick(self):
        self.radioButton.setChecked(True)
        self.comboBox_2.setEnabled(True)
        self.comboBox_3.setDisabled(True)
    
    def batch_onlick(self):
        self.radioButton_2.setChecked(True)
        self.comboBox_2.setDisabled(True)
        self.comboBox_3.setEnabled(True)
    
    def load_data(self):
        self.comboBox_2.clear()
        self.i=0
        connection = sqlite3.connect("def.db")
        results=connection.execute("select TEST_ID FROM TEST_MST WHERE STATUS != 'RUNNING' ORDER BY TEST_ID DESC") 
        for x in results:
            self.comboBox_2.addItem(str(x[0]),self.i)
            self.comboBox_2.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        
        self.comboBox_3.clear()
        self.i=0
        connection = sqlite3.connect("def.db")
        results=connection.execute("select BATCH_ID FROM TEST_MST WHERE STATUS != 'RUNNING' ORDER BY TEST_ID DESC") 
        for x in results:
            self.comboBox_3.addItem(str(x[0]),self.i)
            self.comboBox_3.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        #self.frame_2.hide()
        self.test_onlick()
        self.label_21.hide()
                           
       
        
    def load_test_data(self):
        self.test_id=str(self.comboBox_2.currentText())
        if(self.comboBox_2.currentText() != ""):
            connection = sqlite3.connect("def.db")              
            with connection:        
                    cursor = connection.cursor()                
                    cursor.execute("UPDATE GLOBAL_VAR_TEST SET TEST_ID = '"+str(self.comboBox_2.currentText())+"'")               
            connection.commit();
            connection.close()
        
            connection = sqlite3.connect("def.db")        
            if(self.radioButton.isChecked()):
                 results=connection.execute("select TEST_ID,THICKNESS,PARTY,OPERATOR,BATCH_ID,DIAMETER,WIDTH FROM TEST_MST WHERE TEST_ID = '"+self.comboBox_2.currentText()+"'")             
            else:
                 results=connection.execute("select TEST_ID,THICKNESS,PARTY,OPERATOR,BATCH_ID,DIAMETER,WIDTH FROM TEST_MST WHERE BATCH_ID = '"+self.comboBox_3.currentText()+"'") 
                
            for x in results:
                self.label_23.setText(str(x[0]).zfill(4)) #test d
                '''
                self.lineEdit_4.setText("lineEdit_4") #hickness
                self.lineEdit_10.setText("lineEdit_10") # prty  name
                self.lineEdit_11.setText("lineEdit_11") # operator
                self.lineEdit_12.setText("lineEdit_12") #batch id
                self.lineEdit_7.setText("lineEdit_7") #diameter 
                self.lineEdit_8.setText("lineEdit_8")  #width
                '''
                self.lineEdit_4.setText(str(x[1])) #hickness
                self.lineEdit_10.setText(str(x[2])) # prty  name
                self.lineEdit_11.setText(str(x[3])) # operator
                self.lineEdit_12.setText(str(x[4])) #batch id
                self.lineEdit_7.setText(str(x[5])) #diameter 
                self.lineEdit_8.setText(str(x[6]))  #width
                
            connection.close()
            self.graph_plot =PlotCanvas_blank(self,width=8, height=6,dpi=80)    
            self.gridLayout.addWidget(self.graph_plot, 0, 0, 1, 1) 
    
    def reset_fun(self):
        self.label_23.setText("")
        self.lineEdit_4.setText("") #hickness
        self.lineEdit_10.setText("") # prty  name
        self.lineEdit_11.setText("") # operator
        self.lineEdit_12.setText("") #batch id
        self.lineEdit_7.setText("") #diameter 
        self.lineEdit_8.setText("")  #width
        #self.wifi_setup_page()
        
        
    
                    
        
        
        
    def delete_test(self):
        if(self.label_23.text() != ""):
            close = QMessageBox()
            close.setText("Confirm Deleteing Test ID : "+str(int(self.label_23.text())))
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Yes:
                    #print("DELETE FROM GRAPH_MST WHERE GRAPH_ID in (SELECT GRAPHI_ID FROM TEST_MST WHERE TEST_ID='"+str(int(self.label_23.text()))+"')")
                    connection = sqlite3.connect("def.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM GRAPH_MST WHERE GRAPHI_ID in (SELECT GRAPHI_ID FROM TEST_MST WHERE TEST_ID='"+str(int(self.label_23.text()))+"')")  
                            cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID ='"+str(int(self.label_23.text()))+"'")                    
                    connection.commit();                    
                    connection.close()
                    self.load_data()
                    self.label_21.setText("Deleted Test :"+str(int(self.label_23.text())))
                    self.label_21.show()
                    
                    connection = sqlite3.connect("def.db")        
            
                    results=connection.execute("SELECT COUNT(*) FROM TEST_MST")
                    for x in results:
                        if(int(x[0])==0):
                            self.delete_all_flg=0
                        else:
                            self.delete_all_flg=1
                    connection.close()
                    
                    if(self.delete_all_flg==0):
                        connection = sqlite3.connect("def.db")
                        with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM GRAPH_MST")
                            cursor.execute("DELETE FROM TEST_MST")
                            cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('TEST_MST','GRAPH_MST')")
                        connection.commit();                    
                        connection.close()
                    else:
                        pass
                                
            else:
                pass
        else:
             pass
            
    def print_file(self):
        if(self.label_23.text() != ""):
            self.create_pdf()
            self.window = QtWidgets.QMainWindow()
            self.ui=P_POPUi_MainWindow()
            self.ui.setupUi(self.window)           
            self.window.show()
        else:
             pass
        
        
    def open_pdf(self):
        if(self.label_23.text() != ""):
            self.create_pdf()
            os.system("xpdf ./reports/stech_reports.pdf") 
            product_id=self.get_usb_storage_id()
            if(product_id != "ERROR"):
                    os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                    os.system("cp ./reports/ur_reports.pdf /media/usb/stech_reports"+str(self.test_id)+".pdf")
                    os.system("sudo umount /media/usb")
            else:
                 print("Please connect usb storage device")
        else:
             pass

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

            
    def create_pdf(self):
        y=300
        Elements=[]        
       
        self.test_id=""
        self.remark=""
        self.p_name=""
        self.test_date=""
        summary_data=[]
        self.test_data=[]
        self.test_data.append(["Duration(Hrs)","Load Retention(%)"])
        
        self.test_count=0
        self.max_load=0
        self.per_load=0
        self.per_10=0
        self.mod=1
        
        
        self.ptext1 = ""
           
        self.ptext2 = ""
            
        self.ptext3 = ""            
            
        self.footer_2_str= ""
        
        connection = sqlite3.connect("def.db")        
        results=connection.execute("SELECT TEST_ID,TEST_START_ON,BATCH_ID,THICKNESS,WIDTH,DIAMETER,PARTY,OPERATOR,MAX_TEMP,CURRENT_TIMESTAMP,COMPRESS_THICKNESS_PERC FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_TEST)")
        for x in results:
            summary_data=[["Test No:        ",str(x[0]).zfill(6),"Tested Date:        ",str(x[1])[0:10]]]
            summary_data.append(["Batch Id : ",str(x[2]),"Thickness(Mm): ",str(x[3])])
            summary_data.append(["Width(Mm): ",str(x[4]),"Diameter(Mm): ",str(x[5])])
            summary_data.append(["Party: ",str(x[6]),"Operator: ",str(x[7])])
            summary_data.append(["Temparature(C): ",str(x[8]),"Report Date: ",str(x[9])[0:10]])
            summary_data.append(["Comp.Thickness(%): ",str(x[10])])
            self.test_id=str(x[0])
            self.test_date=str(x[1])            
        connection.close()
        
        connection = sqlite3.connect("def.db")
        results=connection.execute("SELECT GRAPHI_ID  FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_TEST)") 
        for x in results:
            self.graph_id=str(x[0])            
        connection.close()
        
        connection = sqlite3.connect("def.db")
        results=connection.execute("SELECT count(REC_ID),max(Y_NUM) FROM GRAPH_MST WHERE GRAPHI_ID='"+str(self.graph_id)+"'")
        for x in results:
                self.test_count=int(x[0])
                self.per_10=int(int(self.test_count)/10)
                print("record count:"+str(self.test_count)+" self.per_10:"+str(self.per_10))
                self.max_load=str(x[1])                         
        connection.close()
        
        connection = sqlite3.connect("def.db")
        results=connection.execute("SELECT Y_NUM,printf(\"%.4f\", X_NUM),REC_ID FROM GRAPH_MST WHERE GRAPHI_ID='"+str(self.graph_id)+"'")
        for k in results:
               if(float(k[1]) == 0):
                   self.per_load=1*100
                   self.test_data.append([str(float(k[1])),str(int(self.per_load))+str("% ")])               
               else:
                    if(int(self.per_10) > 0):
                        self.mod=int(k[2]) % int(self.per_10)
                    else:
                        self.mod=0
                    if(int(self.mod) == 0):
                            self.per_load=float(int(k[0])/float(self.max_load))*100
                            self.test_data.append([str(float(k[1])),str(int(self.per_load))+str("% ")])
                            #print("load :"+str(k[0])+ " Duration :"+str(k[1]))
        connection.close()
       
        
        
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        
        connection = sqlite3.connect("def.db")        
        results=connection.execute("SELECT  PRINTER_HEATER_TITLE, PRINTER_HEADER ,  PRINTER_FOOTER FROM GLOBAL_VAR_TEST")
        for x in results:
            self.ptext1 = "<font name=Helvetica size=14> "+str(x[0])+"  </font>"
           
            self.ptext2 = "<font name=Helvetica size=11> "+str(x[1])+" </font>"
            
            self.ptext3 = "\n <font name=Helvetica size=16> <b> Compression Stress Relaxation Test </b></font>"            
            
            self.footer_2_str= str(x[2])
        
        connection.close()
        
       
        Title = Paragraph(str(self.ptext1), styles["Title"])
        
        Title2 = Paragraph(str(self.ptext2), styles["Title"])
        Title3 = Paragraph(str(self.ptext3), styles["Title"])
        footer_2= Paragraph("\n "+str(self.footer_2_str)+"", styles["Normal"])
        
        
        
          
        
                   
        
        
        
            
        #comments = Paragraph(str(ptext)+" ------------------------------------------------------------------------------------------------------------------------------- -\n", styles["Normal"])
        
        
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
       
        
          
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10)]))       
        
        f4=Table(self.test_data)
        f4.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10)]))       
        
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 7 * inch, 5 * inch)
        
        
        Elements=[Title3,Title,Title2,Spacer(1,12),Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f4,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        
        
        doc = SimpleDocTemplate('./reports/stech_reports.pdf', rightMargin=10,
                                leftMargin=30,
                                topMargin=30,
                                bottomMargin=20)
        doc.build(Elements)
        #print("Done")
            
class PlotCanvas_blank(FigureCanvas):
    def __init__(self, parent=None, width=5, height=2, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)        
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
        connection = sqlite3.connect("def.db")
        results=connection.execute("SELECT GRAPHI_ID  FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_TEST)") 
        for x in results:
            self.graph_id=str(x[0])            
        connection.close()
        
        self.x=[]
        self.y=[]
        self.test_id=0
        self.test_count=0
        self.max_load=0
        self.per_10=0
        self.mod=1
        self.add_10_per_load=0
        '''
        connection = sqlite3.connect("def.db")
        results=connection.execute("SELECT Y_NUM,X_NUM,REC_ID FROM GRAPH_MST WHERE GRAPHI_ID='"+str(self.graph_id)+"'")
        for k in results:        
                self.y.append(k[0])
                self.x.append(k[1])                
        connection.close()
        '''
        connection = sqlite3.connect("def.db")
        results=connection.execute("SELECT count(REC_ID),max(Y_NUM) FROM GRAPH_MST WHERE GRAPHI_ID='"+str(self.graph_id)+"'")
        for x in results:
                self.test_count=int(x[0])
                self.per_10=int(int(self.test_count)/10)
                print("record count:"+str(self.test_count)+" self.per_10:"+str(self.per_10)+" graph_id:"+str(self.graph_id))
                self.max_load=str(x[1])                         
        connection.close()
        
        connection = sqlite3.connect("def.db")
        results=connection.execute("SELECT Y_NUM,printf(\"%.4f\", X_NUM),REC_ID FROM GRAPH_MST WHERE GRAPHI_ID='"+str(self.graph_id)+"'")
        for k in results:
               if(float(k[1]) == 0):
                   self.y.append(float(k[0]))
                   self.x.append(float(k[1]))               
               else:
                if(int(self.per_10) > 0):
                    self.mod=int(k[2]) % int(self.per_10)
                else:
                    self.mod=0
                print("per_10:"+str(self.per_10)+" mod:"+str(self.mod))
                if(int(self.mod) == 0):
                        self.y.append(float(k[0]))
                        self.x.append(float(k[1])) 
                        #self.test_data.append([float(k[1]),int(k[0])])
                        print("load :"+str(k[0])+ " Duration :"+str(k[1]))
        connection.close()
        
        
        
        
        ax = self.figure.add_subplot(111)
        #ax.set_facecolor('#CCFFFF')
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.2', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.2', color='black')
        
        self.test_count=0
        connection = sqlite3.connect("def.db")
        results=connection.execute("SELECT count(*) TEST_MST")
        for k in results:        
                self.test_count=str(k[0])              
        connection.close()
        
        if(int(self.test_count) > 0):
                connection = sqlite3.connect("def.db")
                results=connection.execute("SELECT MAX_FORCE,MAX_TIME,TEST_ID FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_TEST)")
                for k in results:
                        self.add_10_per_load=float(str(k[0]))*0.1
                        self.add_10_per_load=self.add_10_per_load+float(str(k[0]))
                        self.axes.set_ylim(0,float(str(self.add_10_per_load)))
                        self.axes.set_xlim(0,float(str(k[1])))
                        self.test_id=str(k[2])
                connection.close()
        else:        
                self.axes.set_xlim(0,500)
                self.axes.set_ylim(0,500)
        
       
       
        #ax.plot(self.x,self.y,'#04756A')
        ax.plot(self.x,self.y)
        ax.set_ylabel('FORCE (kgf)')
        ax.set_xlabel('DURATION (hrs)')
        ax.set_title('Report of Test Id:'+str(self.test_id))
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.2', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.2', color='black')        
        
        self.figure.savefig('last_graph.png',dpi=80)
        self.draw()  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = def_03_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
