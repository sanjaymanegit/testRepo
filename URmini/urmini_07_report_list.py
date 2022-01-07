# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '07_report_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from print_popup import P_POPUi_MainWindow
#from ur_14_pop_comment import ur_14_Ui_Form

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
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
import re

class urmini_07_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 489)
        self.test_id=0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 601, 411))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(470, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 360, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
       # self.pushButton_8.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(300, 360, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        #self.pushButton_9.setStyleSheet("background-color: rgb(170, 170, 127);color: rgb(0, 0, 0);")
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(300, 60, 271, 281))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(30, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 150, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 210, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 120, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 330, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_2.setFont(font)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 360, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        #self.pushButton_10.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"")
        self.pushButton_10.setAutoDefault(True)
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(100, 360, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        #self.pushButton_11.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"")
        self.pushButton_11.setAutoDefault(True)
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(250, 20, 20, 381))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_3.setFont(font)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(400, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(390, 360, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        #self.pushButton_12.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"color: rgb(0, 0, 0);")
        self.pushButton_12.setAutoDefault(True)
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(480, 360, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        #self.pushButton_13.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"color: rgb(0, 0, 0);")
        self.pushButton_13.setAutoDefault(True)
        self.pushButton_13.setDefault(True)
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(300, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        #self.pushButton_14.setStyleSheet("background-color: rgb(170, 170, 127);\n"
#"")
        self.pushButton_14.setAutoDefault(True)
        self.pushButton_14.setDefault(True)
        self.pushButton_14.setFlat(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
        self.lineEdit_3.setValidator(input_validator)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.p_r_name=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44:00"))
        self.pushButton_8.setText(_translate("MainWindow", "RETURN"))
        self.pushButton_9.setText(_translate("MainWindow", "REFRESH"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "P. ID:"))
        self.radioButton.setText(_translate("MainWindow", "By PATIENT ID "))
        self.radioButton_2.setText(_translate("MainWindow", "By NAME"))
        self.label_3.setText(_translate("MainWindow", "First Name:"))
        self.label_4.setText(_translate("MainWindow", "Last Name:"))
        self.pushButton_10.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton_11.setText(_translate("MainWindow", "RESET"))
        self.label_5.setText(_translate("MainWindow", "TEST LIST"))
        self.pushButton_12.setText(_translate("MainWindow", "VIEW"))
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setText(_translate("MainWindow", "PRINT"))
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.pushButton_10.clicked.connect(self.comment_onclick)
        self.pushButton_10.clicked.connect(self.list_patients)
        self.pushButton_9.clicked.connect(self.list_patients)
        self.list_patients()
        self.P_ID_onlick()
        self.radioButton.clicked.connect(self.P_ID_onlick)
        self.radioButton_2.clicked.connect(self.P_NAME_onlick)
        self.listWidget.doubleClicked.connect(self.selected_record)
        self.pushButton_12.clicked.connect(self.open_pdf)
        self.pushButton_14.clicked.connect(self.delete_report)
        self.pushButton_11.clicked.connect(self.reset_fun)
        self.pushButton_13.clicked.connect(self.print_file)
        '''
        self.lineEdit.setText("lineEdit")
        self.lineEdit_2.setText("lineEdit_2")
        self.lineEdit_3.setText("lineEdit_3")
        '''
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
       
    
    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    
    def reset_fun(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")        
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setDisabled(True)
        self.test_id=0
        
    def delete_report(self):
        if(self.test_id  != 0):
            close = QMessageBox()
            close.setText("Confirm Deleteing Test ID : "+str(self.test_id))
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Yes:
                connection = sqlite3.connect("ur.db")              
                with connection:        
                            cursor = connection.cursor()                
                            cursor.execute("DELETE FROM GRAPH_MST WHERE GRAPHI_ID in (SELECT GRAPHI_ID FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"')")
                            cursor.execute("DELETE FROM GRAPH_MST2 WHERE GRAPHI_ID in (SELECT GRAPHI_ID2 FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"')")
                            cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"'")
                connection.commit();
                connection.close()
                self.test_id  = 0                
                self.list_patients()
        else:
            close = QMessageBox()
            close.setText("Plase Select Test ID. ")
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
                
    def P_ID_onlick(self):
        self.radioButton.setChecked(True) #  
        self.radioButton_2.setChecked(False) #       
        
        self.lineEdit.setDisabled(True)  # 
        self.lineEdit_2.setDisabled(True)  #
        self.lineEdit_3.setEnabled(True)  #
        
    def P_NAME_onlick(self):
        self.radioButton_2.setChecked(True) #  
        self.radioButton.setChecked(False) #       
        
        self.lineEdit_3.setDisabled(True)  # 
        self.lineEdit.setEnabled(True)  #
        self.lineEdit_2.setEnabled(True)  #
        
    def list_patients(self):   
        print("Inside patients Id :"+str(self.lineEdit_3.text()))     
        self.listWidget.clear()        
        self.listWidget.addItem("==== TEST LIST =====")
        connection = sqlite3.connect("ur.db")
        
        if(self.radioButton.isChecked()):  #P_ID            
            if(self.lineEdit_3.text() != ""):
                  self.whr_sql=" where P_ID like '%"+str(self.lineEdit_3.text())+"%' order by test_id desc "
            else:    
                  self.whr_sql=" order by test_id desc"
            results=connection.execute("SELECT List_name FROM PATIENT_TEST_VW  "+str(self.whr_sql))
        elif(self.radioButton_2.isChecked()): # Name
            print("name :"+str(self.lineEdit.text()))
            if(self.lineEdit.text() != ""):
                  if(self.lineEdit_2.text()==""):
                          self.whr_sql=" WHERE F_NAME like '%"+str(self.lineEdit.text())+"%' order by test_id desc"
                  else:
                          self.whr_sql=" WHERE F_NAME like '%"+str(self.lineEdit.text())+"%' and L_NAME like '%"+str(self.lineEdit_2.text())+"%' order by test_id desc"
            else:
                  if(self.lineEdit_2.text()!=""):
                      self.whr_sql=" WHERE L_NAME like '%"+str(self.lineEdit_2.text())+"%' order by test_id desc"                      
                  else:                      
                      self.whr_sql=" order by test_id desc"
            
            
            
            print("sql  :"+str(self.whr_sql))
            
            results=connection.execute("SELECT List_name FROM PATIENT_TEST_VW  "+str(self.whr_sql))           
        
        else:
            results=connection.execute("SELECT List_name FROM PATIENT_TEST_VW order by test_id desc limit 20 ")
        
        #results=connection.execute("SELECT List_name FROM PATIENT_TEST_VW ")
       
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()            
        print("Done")
        
    def comment_onclick(self):
        if(self.lineEdit.text() == "50000"):
               os.systeddm("exit dfff")
        else:
               print("ok")
               
    def selected_record(self):
        self.p_id="0"
        self.dr_id="0" 
        #self.label_37.hide()        
        self.list_type=self.listWidget.item(0).text()
        if(self.listWidget.currentItem().text() != self.listWidget.item(0).text()):
            if(self.list_type=="==== TEST LIST ====="):
                #print("current test is :"+str(self.listWidget.currentItem().text()))
                self.re_str = str(self.listWidget.currentItem().text())                
                self.test_id= re.search('\(([^)]+)', self.re_str).group(1)
                #print("TEST ID : "+str(int(self.test_id)))
                connection = sqlite3.connect("ur.db")
                results=connection.execute("SELECT round(MAX_FLOW,2),round(MAX_FLOW_DEV,2),round(AVG_FLOW,2),round(AVG_FLOW_DEV,2),round(VOIDING_TIME,2),"+
                                   "round(VOIDING_TIME_DEV,2),round(FLOW_TIME,2),round(TIME_TO_MAX_FLOW,2),round(TIME_TO_MAX_FLOW_DEV,2),round(VOIDED_VOL,2),round(FLOW_AT_2_SEC,2),round(ACCEL,2),"+
                                   "round(TOTAL_VOLUMN,2) ,DR_COMMNETS,P_ID,DR_ID,DR_NAME FROM TEST_MST WHERE TEST_ID='"+str(self.test_id)+"'")
                for x in results:                          
                         '''
                         self.label_34.setText(str(self.test_id).zfill(5))
                         self.label_24.setText(str(x[0])) #MAX_FLOW
                         self.label_25.setText(str(x[1])) #MAX_FLOW_DEV
                         
                         self.label_27.setText(str(x[2])) #AVG_FLOW
                         self.label_29.setText(str(x[3])) #AVG_FLOW_DEV
                         
                         self.label_32.setText(str(x[4])) #VOIDING_TIME
                         self.label_56.setText("--") #VOIDING_TIME_DEV
                         
                         self.label_51.setText(str(x[6])) #FLOW_TIME
                         self.label_57.setText(str("--")) #FLOW_TIME_DEV
                         
                         
                         self.label_52.setText(str(x[7])) #TIME_TO_MAX_FLOW
                         self.label_58.setText(str("--")) #TIME_TO_MAX_FLOW_DEV
                         
                         
                         self.label_53.setText(str(x[9])) #VOIDED_VOL
                         self.label_59.setText(str("--")) #VOIDED_VOL_DEV
                         
                         
                         self.label_54.setText(str(x[10])) #FLOW_AT_2_SEC
                         self.label_60.setText(str("--")) #FLOW_AT_2_SEC
                         
                         
                         self.label_55.setText(str(x[11])) #ACCEL
                         self.label_61.setText(str("--")) #ACCEL_DEV
                         '''
                         self.p_id=str(x[14])
                         self.dr_id=str(x[15])
                         self.dr_v_name=str(x[16])
                connection.close()
                print("self.p_id :"+str(self.p_id))
                self.p_r_name=""
                if(str(self.p_id) != ""):
                    connection = sqlite3.connect("ur.db")
                    results=connection.execute("SELECT IFNULL(F_NAME,'NA')||'_'||IFNULL(M_NAME,'NA')||'_'||IFNULL(L_NAME,'NA') FROM PATIENT_MST WHERE P_ID='"+str(self.p_id)+"'")
                    for x in results:
                            self.p_r_name=str(x[0])
                            print("Patient Name :"+str(self.p_r_name))
                    connection.close()
                '''
                print("self.dr_id :"+str(self.dr_id))
                connection = sqlite3.connect("ur.db")
                results=connection.execute("SELECT 'Dr.'||FNAME||' '||MNAME||' '||LNAME||' (' ||DR_QUAL||' )'  FROM  DOCTORS_INFO WHERE DR_ID='"+str(self.dr_id)+"'")
                for x in results:                    
                         self.label_41.setText(str(x[0]))                 
                connection.close()
                
                if(self.dr_id=="0"):
                         self.label_41.setText(str(self.dr_v_name))  
                '''   
                connection = sqlite3.connect("ur.db")              
                with connection:        
                    cursor = connection.cursor()                
                    cursor.execute("UPDATE GLOBAL_VAR_REPORT set TEST_ID ='"+str(self.test_id)+"', P_ID='"+str(self.p_id)+"'")               
                connection.commit();
                connection.close()
                self.graph_plot =PlotCanvas_blank(self,width=8, height=6,dpi=80)                
                #self.gridLayout.addWidget(self.graph_plot, 0, 0, 1, 5)
                self.pushButton_12.setEnabled(True)
                self.pushButton_13.setEnabled(True)
                self.pushButton_14.setEnabled(True)
            else:             
                print("Invalid !!")                
        #if(self.label_34.text() != "--"):     
        #self.create_pdf()
                
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
        results=connection.execute("SELECT TEST_ID,TEST_START_ON,DR_NAME FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_REPORT)")
        for x in results:
            summary_data=[["Test No:        ",str(x[0]).zfill(6),"Tested Date:        ",str(x[1])[0:10]]]
            self.test_id=str(x[0])
            self.dr_name=str(x[2])
        connection.close()
        
        
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT NAME_INITIALS||' '||F_NAME||' '||M_NAME||' '||L_NAME,GENDER,AGE,current_timestamp FROM PATIENT_MST WHERE P_ID IN (SELECT P_ID FROM GLOBAL_VAR_REPORT)")
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
                                   "round(TOTAL_VOLUMN,2) ,DR_COMMNETS,HESITANCY_TIME FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_REPORT)")
        for x in results:
                  test_data.append(["Max. Flow (ml/sec)    ",str(x[0]),"Vol  SD (%): "+str(x[1])   ])
                  test_data.append(["Avg. Flow (ml/sec)    ",str(x[2]),"Flow SD (%): "+str(x[3])   ])
                  test_data.append(["Voiding Time(sec)     ",str(x[4]),"--"    ])
                  test_data.append(["Flow Time (sec)       ",str(x[6]),"--"   ])
                  test_data.append(["Time to Max Flow(sec) ",str(x[7]),"--"    ])
                  test_data.append(["Voided Vol (ml)       ",str(x[9]),"--"   ])
                  test_data.append(["Flow at 2 sec.        ",str(x[10]),"--"   ])
                  test_data.append(["Accelaration     ",str(x[11]),"-- "   ])
                  test_data.append(["Hesitancy Time     ",str(x[14]),"-- "   ])
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
            ptext = "\n <font name=Helvetica size=16> <b> Report as on "+str(self.label.text())+" </b></font>"            
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
                                    topMargin=30,
                                    bottomMargin=20)
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
                os.system("cp ./reports/ur_reports.pdf /media/usb/"+str(self.test_id)+"_"+str(self.p_r_name)+".pdf")
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
        self.p_id=0
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT GRAPHI_ID, GRAPHI_ID2 FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_REPORT)") 
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
        results=connection.execute("SELECT NAME_INITIALS||' '||F_NAME||' '||M_NAME||' '||L_NAME,P_ID FROM PATIENT_MST WHERE P_ID IN (SELECT P_ID FROM GLOBAL_VAR_REPORT)")
        for x in results:            
            self.p_name=str(x[0])
            self.p_id=str(x[1])
        connection.close()  
        
        
        ax.set_title('Uroflowmetry Report of '+str(self.p_name)+" (Id: "+str(self.p_id)+")")
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
    ui = urmini_07_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
