# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_02_reports.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5.Qt import QTableWidgetItem
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
import serial,time
from PyQt5.QtCore import QDate
import datetime

from reportlab.lib import colors
#from reportlab.lib.pagesizes import letter, inch
from reportlab.lib.pagesizes import landscape, letter,inch,A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate,Spacer,tables
from reportlab.pdfgen.canvas import Canvas

import pandas as pd
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from reportlab.rl_settings import showBoundary

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from print_popup_report import P_POPUi_MainWindow

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize


from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY 
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
import sqlite3
from reportlab.lib.pagesizes import landscape, letter,inch,A4
from reportlab.lib import colors


class wt_02_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1311, 700))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.from_date=""
        self.to_date=""
        self.v_param_arr=[]
        self.whr_str=""
        self.filter_col_name=""
        self.filter_col_val="" 
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 641))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 49, 119, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(220, 50, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 71, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 100, 119, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 100, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QRadioButton(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 170, 91, 31))
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(130, 170, 161, 31))
        self.comboBox.setObjectName("comboBox")
        self.checkBox_2 = QtWidgets.QRadioButton(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 230, 91, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 230, 161, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.checkBox_3 = QtWidgets.QRadioButton(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 290, 101, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(130, 290, 161, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 450, 101, 31))
        self.checkBox_4.setObjectName("checkBox_4")
        
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 350, 131, 31))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.setText("Collection  Report")
        
        self.label_2_1 = QtWidgets.QLabel(self.groupBox)
        self.label_2_1.setGeometry(QtCore.QRect(10, 375, 181, 31))
        self.label_2_1.setText("Total Amount(Rs):1000")
        self.label_2_1.setObjectName("label_2_1")
        self.label_2_1.hide()
        
        
        
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 510, 81, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 510, 81, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 510, 81, 41))
        self.pushButton_5.setObjectName("pushButton_5")
       
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 590, 81, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_6_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6_1.setGeometry(QtCore.QRect(180, 590, 111, 41))
        self.pushButton_6_1.setObjectName("pushButton_6_1")
        
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(340, 20, 951, 651))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 12, item)
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget_2.setGeometry(QtCore.QRect(360, 140, 296, 183))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.calendarWidget_2.setFont(font)
        self.calendarWidget_2.setGridVisible(True)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(690, 140, 296, 183))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.setHorizontalHeaderLabels(['Serial ID.', ' Vehicle.No ', 'Party Name', 'Supplier Name','Transport Name','Material Name' ,'Gross Wt. Date','Gross Wt.(Kg)','Tare Wt.Date','Tare Wt.(Kg)','Total Amount','Gross Amount','Tare Amount'])        
       
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Reports Parameters"))
        self.label.setText(_translate("MainWindow", "From Date :"))
        self.pushButton.setText(_translate("MainWindow", "Date"))
        self.label_2.setText(_translate("MainWindow", "To  Date :"))
        self.pushButton_2.setText(_translate("MainWindow", "Date"))
        self.checkBox.setText(_translate("MainWindow", "By Party"))
        self.checkBox_2.setText(_translate("MainWindow", "By Supplier"))
        self.checkBox_3.setText(_translate("MainWindow", "By Transport"))
        self.checkBox_4.setText(_translate("MainWindow", "All"))
        self.pushButton_3.setText(_translate("MainWindow", "View"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset"))
        self.pushButton_5.setText(_translate("MainWindow", "Print"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.pushButton_6_1.setText(_translate("MainWindow", "View Report"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Serial ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Party Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Supplier Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Transport Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Material Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Gross Weight Date"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Gross Weight (Kg)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Tare Weight Date"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Tare Weight (Kg)"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Net Weight (Kg)"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Total Amount (Rs)"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Second Weight Amount (Rs)"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "First Weight Amount (Rs)"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "001"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "1"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.calendarWidget.hide()
        self.calendarWidget_2.hide()
        self.pushButton_6.clicked.connect(MainWindow.close)
        
        #self.pushButton_4.clicked.connect(self.anydisk_click)
        self.pushButton.clicked.connect(self.from_dt_onclick)
        self.pushButton_2.clicked.connect(self.to_dt_onclick)
        self.calendarWidget.clicked.connect(self.date_dd_click_from)
        self.calendarWidget_2.clicked.connect(self.date_dd_click_to)               
        
        self.load_data()
        self.checkBox.clicked.connect(self.by_party_onclick)
        self.checkBox_2.clicked.connect(self.by_sup_onclick)
        self.checkBox_3.clicked.connect(self.by_trasport_onclick)
        
        self.checkBox_4.clicked.connect(self.all_onclick)
        self.pushButton_4.clicked.connect(self.load_data)
        self.pushButton_3.clicked.connect(self.list_report_data)
        self.pushButton_5.clicked.connect(self.open_PPOP_window3)
        self.pushButton_6_1.clicked.connect(self.open_PPOP_window4)        
        
        self.delete_all_records()
   
        
        
        
        
    def cr_where_clause(self):
        if(self.checkBox_4.isChecked()):
                self.whr_str=" WHERE strftime('%Y-%m-%d',FIRST_WT_CRTEATED_ON)  between '"+str(self.from_date)+"' and '"+str(self.to_date)+"' limit 50000"
        elif(self.checkBox.isChecked()) :
                self.whr_str=" WHERE strftime('%Y-%m-%d',FIRST_WT_CRTEATED_ON)  between '"+str(self.from_date)+"' and '"+str(self.to_date)+"' AND PARTY_NAME='"+str(self.comboBox.currentText())+"' limit 50000 "
                self.filter_col_name="Party Name"
                self.filter_col_val=str(self.comboBox.currentText())
        elif(self.checkBox_2.isChecked()) :
                self.whr_str=" WHERE strftime('%Y-%m-%d',FIRST_WT_CRTEATED_ON)  between '"+str(self.from_date)+"' and '"+str(self.to_date)+"' AND SUPPLIER_NAME='"+str(self.comboBox_2.currentText())+"'  limit 50000 "
                self.filter_col_name="Supplier Name"
                self.filter_col_val=str(self.comboBox_2.currentText())  
        elif(self.checkBox_3.isChecked()) :
                self.whr_str=" WHERE strftime('%Y-%m-%d',FIRST_WT_CRTEATED_ON)  between '"+str(self.from_date)+"' and '"+str(self.to_date)+"' AND TRANSPORT_NAME='"+str(self.comboBox_3.currentText())+"' limit 50000 "
                self.filter_col_name="Transport Name"
                self.filter_col_val=str(self.comboBox_3.currentText()) 
        elif(self.radioButton_5.isChecked()):
                self.whr_str=" WHERE strftime('%Y-%m-%d',FIRST_WT_CRTEATED_ON)  between '"+str(self.from_date)+"' and '"+str(self.to_date)+"'  limit 50000 "
                self.filter_col_name="collection_report"
                self.filter_col_val=""
            
    def list_report_data(self):
        self.label_2_1.hide()
        self.delete_all_records()
        if not (self.radioButton_5.isChecked()):        
            font = QtGui.QFont()
            font.setPointSize(10)
            self.tableWidget.setFont(font)
            self.tableWidget.setColumnCount(14)
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.tableWidget.setHorizontalHeaderLabels(['Serial ID.', ' Vehicle.No ', 'Party Name', 'Supplier Name','Transport Name','Material Name' ,'Gross Wt. Date','Gross Wt.(Kg)','Tare Wt.Date','Tare Wt.(Kg)','Net Wt. (Kg)','Total Amount','Gross Amount','Tare Amount'])        
           
            connection = sqlite3.connect("wt.db")        
            print ("from_date :"+str(self.from_date)+" to_date :"+str(self.to_date));
            self.cr_where_clause()
            print(" Where clause :"+self.whr_str)
            if(self.whr_str != ""):
                results=connection.execute("SELECT SERIAL_ID_DISPLY,VEHICLE_NO,PARTY_NAME,SUPPLIER_NAME,TRANSPORT_NAME,MATERIAL_NAME,"+
                                       "GROSS_WT_DATE ,GROSS_WT_VAL, TARE_WT_DATE ,TARE_WT_VAL  ,NET_WEIGHT_VAL, (IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT,GROSS_WT_RATE,TARE_WT_RATE FROM WEIGHT_MST_VW "+self.whr_str
                                           )
          
            else:
                results=connection.execute("SELECT printf(\"%04d\", SERIAL_ID) as SERIAL_ID,VEHICLE_NO,PARTY_NAME,SUPPLIER_NAME,TRANSPORT_NAME,MATERIAL_NAME,"+
                                       "GROSS_WT_DATE ,GROSS_WT_VAL, TARE_WT_DATE ,TARE_WT_VAL  ,NET_WEIGHT_VAL, (IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT,GROSS_WT_RATE,TARE_WT_RATE FROM WEIGHT_MST_VW")
            for row_number, row_data in enumerate(results):            
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            connection.close()
             
            print("inside if part ")
        else:
            print("inside else part ")
            font = QtGui.QFont()
            font.setPointSize(10)
            self.tableWidget.setFont(font)
            self.tableWidget.setColumnCount(3)
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.tableWidget.setHorizontalHeaderLabels(['Serial ID.', ' Vehicle.No ', 'Charges (Rs)'])        
            connection = sqlite3.connect("wt.db")
            print ("from_date :"+str(self.from_date)+" to_date :"+str(self.to_date));
            self.cr_where_clause()
            print(" Where clause :"+self.whr_str)
            if(self.whr_str != ""):
                results=connection.execute("SELECT printf(\"%04d\", SERIAL_ID) as SERIAL_ID,VEHICLE_NO, (IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT FROM WEIGHT_MST_VW"+self.whr_str)
            else:
                results=connection.execute("SELECT printf(\"%04d\", SERIAL_ID) as SERIAL_ID,VEHICLE_NO, (IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT FROM WEIGHT_MST_VW")
            for row_number, row_data in enumerate(results):            
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            connection.close()             
            connection = sqlite3.connect("wt.db")
            if(self.whr_str != ""):
                    results=connection.execute("SELECT SUM(TOTAL_AMOUNT) FROM WEIGHT_MST_VW "+str(self.whr_str))
            else: 
                    results=connection.execute("SELECT SUM(TOTAL_AMOUNT) FROM WEIGHT_MST_VW ")
            for x in results:
                    total_amount=str(x[0])
                    self.label_2_1.setText("Total Amount(Rs):"+str(total_amount))
                    self.label_2_1.show()
            connection.close()
            
        self.create_pdf_new() 
           
        
    
    
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)  
    
    def by_party_onclick(self):
        if(self.checkBox.isChecked()):
            self.comboBox.setEnabled(True)
            self.comboBox_2.setDisabled(True)
            self.comboBox_3.setDisabled(True)
            #self.checkBox_2.setDisabled(True)
            #self.checkBox_3.setDisabled(True)  
        if not (self.checkBox.isChecked()):
            self.comboBox.setDisabled(True)
            
    def by_sup_onclick(self):
        if(self.checkBox_2.isChecked()):
            self.comboBox_2.setEnabled(True)
            self.comboBox.setDisabled(True)
            self.comboBox_3.setDisabled(True)
            #self.checkBox.setDisabled(True)
            #self.checkBox_3.setDisabled(True) 
        
        if not (self.checkBox_2.isChecked()):
            self.comboBox_2.setDisabled(True)
            
    
    def by_trasport_onclick(self):
        if(self.checkBox_3.isChecked()):
            self.comboBox_3.setEnabled(True)
            self.comboBox.setDisabled(True)
            self.comboBox_2.setDisabled(True)
            #self.checkBox_2.setDisabled(True)
            #self.checkBox.setDisabled(True) 
        
        if not (self.checkBox_3.isChecked()):
            self.comboBox_3.setDisabled(True)          
            
            
    def all_onclick(self):
        self.label_2_1.hide()
        if(self.checkBox_4.isChecked()):
             self.checkBox.setDisabled(True)
             self.checkBox_2.setDisabled(True)
             self.checkBox_3.setDisabled(True)
             self.checkBox_3.setChecked(True)
             self.radioButton_5.setDisabled(True)
             
        else:
             self.checkBox.setEnabled(True)
             self.checkBox_2.setEnabled(True)
             self.checkBox_3.setEnabled(True)
             self.radioButton_5.setEnabled(True)
        
        self.comboBox_3.setDisabled(True)
        self.comboBox.setDisabled(True)
        self.comboBox_2.setDisabled(True)     
          
             
             
             
    def load_data(self):
        self.label_2_1.hide()
        self.i=0
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT DISTINCT PARTY_NAME FROM WEIGHT_MST where PARTY_NAME not in ('None','')") 
        for x in results:                          
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        
        self.i=0
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT DISTINCT SUPPLIER_NAME FROM WEIGHT_MST where SUPPLIER_NAME not in ('None','')") 
        for x in results:                          
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        
        self.i=0
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT DISTINCT TRANSPORT_NAME FROM WEIGHT_MST where TRANSPORT_NAME not in ('None','')") 
        for x in results:                          
            self.comboBox_3.addItem("")
            self.comboBox_3.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        self.comboBox.setDisabled(True)
        self.checkBox.setDisabled(True)
        self.comboBox_2.setDisabled(True)
        self.checkBox_2.setDisabled(True)
        self.comboBox_3.setDisabled(True)
        self.checkBox_3.setDisabled(True)
        self.checkBox_4.setChecked(True)
        self.radioButton_5.setDisabled(True)
        
        
        self.default_dates()
        self.delete_all_records()
    
    
    def default_dates(self):
        temp_var =QDate.currentDate()
        var_name = temp_var.toPyDate()
        self.from_date=str(var_name)
        self.to_date=str(var_name) 
        self.lineEdit.setText(str(QDate.currentDate().toString()))
        self.lineEdit_2.setText(str(QDate.currentDate().toString())) 
     
    def from_dt_onclick(self):
        self.calendarWidget.show()
        
    def to_dt_onclick(self):
        self.calendarWidget_2.show()
        
    def date_dd_click_from(self):        
        temp_var = self.calendarWidget.selectedDate() 
        var_name = temp_var.toPyDate()        
        self.from_date=str(var_name)        
        self.lineEdit.setText(str(self.calendarWidget.selectedDate().toString()))
        self.calendarWidget.hide()
        #self.lineEdit.show()
        
    def date_dd_click_to(self):        
        temp_var = self.calendarWidget_2.selectedDate() 
        var_name = temp_var.toPyDate()        
        self.to_date=str(var_name)        
        self.lineEdit_2.setText(str(self.calendarWidget_2.selectedDate().toString()))
        self.calendarWidget_2.hide()
        #self.lineEdit_2.show()
        
    def create_pdf_new(self):
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        total_amount="0"
        #styles.add(ParagraphStyle(name="x", fontSize=12, leading = 7, alignment=TA_LEFT))
        #styles.add(ParagraphStyle(name="x2", fontSize=10, leading = 7, alignment=TA_LEFT))
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT COMPANY_NAME,COMPANY_ADDR||' Phone:'||CONTACT_NO FROM USER_RIGHT_SET")
        for x in results:                          
              Title = Paragraph(str(x[0]), styles["Title"])
              ptext = "<font name=Helvetica size=10>"+str(x[1])+" </font>"            
              Title2 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        
        self.cr_where_clause()
        print(" Where clause :"+str(self.whr_str))
        connection = sqlite3.connect("wt.db")
        if(self.whr_str != ""):
                results=connection.execute("SELECT SUM(TOTAL_AMOUNT) FROM WEIGHT_MST_VW "+str(self.whr_str))
        else: 
                results=connection.execute("SELECT SUM(TOTAL_AMOUNT) FROM WEIGHT_MST_VW ")
        for x in results:
                total_amount=str(x[0])
                #self.label_2_1.setText("Total Amount(Rs):"+str(total_amount))
                #self.label_2_1.show()
        connection.close()
        
        if(self.checkBox_4.isChecked()):
                 self.all_flag='ACTIVE'
        else:
                 self.all_flag='DEACTIVE'
                 
        connection = sqlite3.connect("wt.db")          
        with connection:        
             cursor = connection.cursor()                    
             cursor.execute("UPDATE PRINTER_DATA SET REPORT_FROM_DATE='"+str(self.from_date)+"',REPORT_TO_DATE='"+str(self.to_date)+"',ALL_FLAG='"+str(self.all_flag)+"',total_amount='"+str(total_amount)+"',FILTER_COL='"+str(self.filter_col_name)+"',FILTER_COL_VAL='"+str(self.filter_col_val)+"'") 
        connection.commit();
        connection.close()          
                
                
                
        
        if(self.checkBox_4.isChecked()):  ## All data Header infomartion
                summary_data=[["From Date: "+str(self.from_date),"To Date: "+str(self.to_date) , "Total Amount: "+str(total_amount), "Report Date: "+str(datetime.datetime.now().strftime("%d %b %Y %H:%M"))]]
                     
        elif(self.checkBox.isChecked()) :  ## Party NAme                
                summary_data=[["From Date: "+str(self.from_date),"To Date: "+str(self.to_date) , "Total Amount: "+str(total_amount) ,"Report Date: "+str(datetime.datetime.now().strftime("%d %b %Y %H:%M")),"Party Name: "+str(self.comboBox.currentText())]]
        elif(self.checkBox_2.isChecked()) :
                summary_data=[["From Date: "+str(self.from_date),"To Date: "+str(self.to_date) , "Total Amount: "+str(total_amount) ,"Report Date: "+str(datetime.datetime.now().strftime("%d %b %Y %H:%M")),"Supplier Name: "+str(self.comboBox_2.currentText())]]
        elif(self.checkBox_3.isChecked()) :               
                summary_data=[["From Date: "+str(self.from_date),"To Date: "+str(self.to_date) , "Total Amount: "+str(total_amount),"Report Date: "+str(datetime.datetime.now().strftime("%d %b %Y %H:%M")),"Transport Name: "+str(self.comboBox_3.currentText())]]
        elif(self.radioButton_5.isChecked()) :               
                summary_data=[["From Date: "+str(self.from_date),"To Date: "+str(self.to_date) , "Total Amount: "+str(total_amount),"Report Date: "+str(datetime.datetime.now().strftime("%d %b %Y %H:%M"))]]
        else:
                summary_data=[["From Date: "+str(self.from_date),"To Date: "+str(self.to_date) , "Total Amount: "+str(total_amount),"Report Date: "+str(datetime.datetime.now().strftime("%d %b %Y %H:%M"))]]
       
         
        f3=Table(summary_data)
        #f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10)]))       
        
        Elements = [Title,Spacer(1,12),Title2,Spacer(1,12),f3,Spacer(1,12),Spacer(1,12)]
         
        if(str(self.filter_col_name) !="collection_report"):
            childs_data=[]
            childs_data=[['Serial ID.', ' Vehicle.No ','Party Name','Supplier Name','Transport Name','Material Name' ,'Gross Wt. Date','Gross Wt. \n (Kg)','Tare Wt.Date','Tare Wt. \n (Kg)',' Net Wt. \n (Kg)','Total Amount']]
            connection = sqlite3.connect("wt.db")
            
            if(self.whr_str != ""):
                    results=connection.execute("SELECT SERIAL_ID_DISPLY,VEHICLE_NO,PARTY_NAME,SUPPLIER_NAME,TRANSPORT_NAME,MATERIAL_NAME,GROSS_WT_DATE ,GROSS_WT_VAL, TARE_WT_DATE ,TARE_WT_VAL  ,NET_WEIGHT_VAL, (IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT FROM WEIGHT_MST_VW "+str(self.whr_str)) 
            else:
                    results=connection.execute("SELECT SERIAL_ID_DISPLY,VEHICLE_NO,PARTY_NAME,SUPPLIER_NAME,TRANSPORT_NAME,MATERIAL_NAME,GROSS_WT_DATE ,GROSS_WT_VAL, TARE_WT_DATE ,TARE_WT_VAL  ,NET_WEIGHT_VAL, (IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT FROM WEIGHT_MST_VW ") 
       
            for k in results:
                childs_data.append(k)
            connection.close()
        else:
            childs_data=[]
            childs_data=[['Serial ID.', ' Vehicle.No ','Total Amount']]
            connection = sqlite3.connect("wt.db")
            
            if(self.whr_str != ""):
                    results=connection.execute("SELECT SERIAL_ID_DISPLY,VEHICLE_NO,(IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT FROM WEIGHT_MST_VW "+str(self.whr_str)) 
            else:
                    results=connection.execute("SELECT SERIAL_ID_DISPLY,VEHICLE_NO, (IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT FROM WEIGHT_MST_VW ") 
       
            for k in results:
                childs_data.append(k)
            connection.close()
            
            
        f=Table(childs_data)
        f.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
         
        Elements.append(f)
        
        doc = SimpleDocTemplate('./reports/TodaysReport.pdf',pagesize=A4)
        doc.pagesize = landscape(A4)
        doc.build(Elements)
        print("Done")
        self.filter_col_name=""
         
    
    '''    
    def open_PPOP_window3(self):     
        self.create_pdf_new()   
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POPUi_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    '''   
    def open_PPOP_window3(self):
        self.create_pdf_new()  
        os.system("./job_print_report.sh")
       
    def open_PPOP_window4(self):
        self.create_pdf_new() 
        os.system("xpdf ./reports/TodaysReport.pdf")
        
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_02_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
