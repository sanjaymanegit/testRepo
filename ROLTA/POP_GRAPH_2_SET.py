#from GRAPH_SCALES_ALL import set_two_graphs_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

# from print_test_popup import P_POP_TEST_Ui_MainWindow
# from email_popup_test_report import popup_email_test_Ui_MainWindow
# from email_popup_log_report import popup_email_log_Ui_MainWindow
# from comment_popup_expansion import comment_Ui_MainWindow
# 


from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import random
import serial,time
import array  as arr
import numpy as np

import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

import datetime
import serial
import time

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
from reportlab.pdfgen.canvas import Canvas
#import pandas as pd
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from reportlab.rl_settings import showBoundary

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY 
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import portrait,landscape, letter,inch,A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Line, Drawing


class pop_graph2_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1485, 657)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1451, 601))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(1350, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
#         self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
# "background-color: rgb(0, 180, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        
        
        
        
        self.chke_box = QtWidgets.QCheckBox(self.frame)
        self.chke_box.setGeometry(QtCore.QRect(1280, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.chke_box.setFont(font)
        self.chke_box.setText("Enable")
        self.chke_box.setObjectName("chke_box")
        
        
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 390, 471, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(490, 400, 471, 191))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setItem(0, 2, item)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_3.setGeometry(QtCore.QRect(970, 400, 471, 191))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_3.setItem(0, 2, item)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(120, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setGeometry(QtCore.QRect(610, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setGeometry(QtCore.QRect(1060, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 80, 1431, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 0, 1, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout.addWidget(self.graphicsView_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1485, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.timer3=QtCore.QTimer()
        self.timer4=QtCore.QTimer()
        self.timer5=QtCore.QTimer()
        self.timer6=QtCore.QTimer()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Close"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Trend"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Timestamp"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Pressure"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "233.2"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "22-11-2011 03:44:55"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Trend"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Timestamp"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainWindow", "Expansion"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("MainWindow", "233.2"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("MainWindow", "22-11-2011 03:44:55"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Trend"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Timestamp"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(0, 0)
        item.setText(_translate("MainWindow", "Stress"))
        item = self.tableWidget_3.item(0, 1)
        item.setText(_translate("MainWindow", "233.2"))
        item = self.tableWidget_3.item(0, 2)
        item.setText(_translate("MainWindow", "22-11-2011 03:44:55"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.pushButton_17.setText(_translate("MainWindow", "Pressure Vs  Expansion"))
        self.pushButton_18.setText(_translate("MainWindow", "Strain Vs Stress"))
        self.pushButton_19.setText(_translate("MainWindow", "Stress Vs Time"))
        self.pushButton_4.clicked.connect(MainWindow.close)
        
        self.chke_box.clicked.connect(self.stop_process)
        
        self.start2_test_expansion()
        
    
    def start2_test_expansion(self):
        print("Group2 started")
#         self.pushButton_21.hide()
#         self.pushButton_22.show()
#         self.pushButton_22.setDisabled(True)
    
#         self.validation() 
#         self.disable_all()
#         self.pushButton_9.setEnabled(True)
#         connection = sqlite3.connect("tyr.db")              
#         with connection:
#                             cursor = connection.cursor()                  
#                             cursor.execute("UPDATE GLOBAL_VAR SET D_AV='"+str(self.lineEdit_46.text())+"',T_AV='"+str(self.lineEdit_47.text())+"',NEW_TEST_GUAGE_MM='"+str(self.lineEdit_51.text())+"'")
#                             cursor.execute("DELETE FROM STG_GRAPH_MST ")  
#         connection.commit();
#         connection.close();
        self.goAhead="Yes"
        if(self.goAhead=="Yes"):              
                        
                        self.sc_new =PlotCanvasG2_Auto(self,width=5, height=4, dpi=80)
                        self.gridLayout.addWidget(self.sc_new, 0, 0, 1, 1)
                        
                        self.sc_new_P1 =PlotCanvasG2_Auto_P1(self,width=5, height=4, dpi=80)
                        self.gridLayout.addWidget(self.sc_new_P1, 0, 1, 1, 1)
                        
                        self.sc_new_P2 =PlotCanvasG2_Auto_P2(self,width=5, height=4, dpi=80)
                        self.gridLayout.addWidget(self.sc_new_P2, 0, 2, 1, 1)
                        
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT COUNT(*) FROM STG_GRAPH_MST")
                        rows=results.fetchall()
                        connection.close()
                        if(int(rows[0][0]) > -2 ):
                                        self.timer3.setInterval(1000)        
                                        #self.timer3.timeout.connect(self.show_load_cell_val)
                                        self.timer3.timeout.connect(self.show_grid1_val_P3)
                                        self.timer3.timeout.connect(self.show_grid1_val_P4)
                                        self.timer3.timeout.connect(self.show_grid1_val_P5)
                                        self.timer3.start(1)
                                        self.pushButton_4.setDisabled(True)
                                        
        else:            
                    print("validation Error") 

    def stop_process(self):
        if(self.sc_new.timer1.isActive()):
                self.sc_new.on_ani_stop()
                self.sc_new_P1.on_ani_stop()
                self.sc_new_P2.on_ani_stop()
                if(self.timer3.isActive()): 
                    self.timer3.stop()                    
                    self.pushButton_4.setEnabled(True)
                    self.chke_box.setChecked(True)
                else:
                    print("Process is not running")
                    self.pushButton_4.setEnabled(True)
                    self.chke_box.setChecked(True)
            
    def show_grid1_val_P3(self):        
        self.rev_arr3=[]        
        self.rev_arr4=[]
        self.delete3x_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)      
        self.tableWidget.setHorizontalHeaderLabels(['Parameter','Pressure(MPa)','Expansion (mm)'] )
        #self.z=[123.00,344.4,24.5,45.77,34,565]
       
        self.rev_arr3=self.sc_new.arr_q
        self.rev_arr4=self.sc_new.arr_p
        self.rev_arr3.reverse()
        self.rev_arr4.reverse()
        if(len(self.rev_arr3) > 0):
              for i in range(len(self.rev_arr3)):
                        self.tableWidget.insertRow(i)
                        item = QtWidgets.QTableWidgetItem()        
                        item.setText(str("Pressure vs Expansion"))
                        self.tableWidget.setItem(i,0,item) 
                        item2 = QtWidgets.QTableWidgetItem()        
                        item2.setText(str(self.rev_arr3[i]))
                        self.tableWidget.setItem(i,1,item2)
                        item3 = QtWidgets.QTableWidgetItem()        
                        item3.setText(str(self.rev_arr4[i]))
                        self.tableWidget.setItem(i,2,item3) 
                
                
               
        self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
    def show_grid1_val_P4(self):
        
        self.rev_arr=[]
        self.rev_arr2=[]
        self.delete4_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_2.setFont(font) 
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)      
        self.tableWidget_2.setHorizontalHeaderLabels(['Parameter','Stress(MPa)','Strain (%)'] )
        #self.z=[123.00,344.4,24.5,45.77,34,565]
       
        self.rev_arr=self.sc_new_P1.arr_q_mpa
        self.rev_arr2=self.sc_new_P1.arr_p_strain
        self.rev_arr.reverse()
        self.rev_arr2.reverse()
        if(len(self.rev_arr) > 0):
                for i in range(len(self.rev_arr)):
                        self.tableWidget_2.insertRow(i)
                        item4 = QtWidgets.QTableWidgetItem()        
                        item4.setText(str("Stress Vs Strain"))
                        self.tableWidget_2.setItem(i,0,item4) 
                        item5 = QtWidgets.QTableWidgetItem()        
                        item5.setText(str(self.rev_arr[i]))
                        self.tableWidget_2.setItem(i,1,item5)
                        item6 = QtWidgets.QTableWidgetItem()        
                        item6.setText(str(self.rev_arr2[i]))
                        self.tableWidget_2.setItem(i,2,item6) 
                
                
              
        self.tableWidget_2.resizeColumnsToContents()
        #self.tableWidget_2.resizeRowsToContents()
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            
            
    def show_grid1_val_P5(self):        
        self.rev_arr5=[]
        self.rev_arr6=[]
        self.delete5_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_3.setFont(font) 
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)      
        self.tableWidget_3.setHorizontalHeaderLabels(['Parameter','Stress(MPa)','Time (sec)'] )
        #self.z=[123.00,344.4,24.5,45.77,34,565]
       
        self.rev_arr5=self.sc_new_P2.arr_q_mpa
        self.rev_arr6=self.sc_new_P2.arr_t
        self.rev_arr5.reverse()
        self.rev_arr6.reverse()
        if(len(self.rev_arr5) > 0):
                for i in range(len(self.rev_arr6)):
                        self.tableWidget_3.insertRow(i)
                        item7 = QtWidgets.QTableWidgetItem()        
                        item7.setText(str("Stress Vs Time"))
                        self.tableWidget_3.setItem(i,0,item7) 
                        item8 = QtWidgets.QTableWidgetItem()        
                        item8.setText(str(self.rev_arr5[i]))
                        self.tableWidget_3.setItem(i,1,item8)
                        item9 = QtWidgets.QTableWidgetItem()        
                        item9.setText(str(self.rev_arr6[i]))
                        self.tableWidget_3.setItem(i,2,item9) 
                       
        self.tableWidget_3.resizeColumnsToContents()
        #self.tableWidget_3.resizeRowsToContents()
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
  
    
    def delete3x_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
    
    def delete4_all_records(self):
        i = self.tableWidget_2.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget_2.removeRow(i) 
        
    def delete5_all_records(self):
        i = self.tableWidget_3.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget_3.removeRow(i)       
            


################ GRAPH GROUP 2 ############################

class PlotCanvasG2_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="tyr"
        self.axes.set_xlabel('Expansion (mm)')
        self.axes.set_ylabel('Pressure (MPa)')
        self.axes.grid(which='major', linestyle='-', linewidth='0.50', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.50', color='black')
        
#         self.axes2 = self.axes.twinx()
#         color = 'tab:green'
#         self.axes2.set_ylabel('Time (Sec)', color = color)
#         self.axes2.set_ylim(0,500)
        
        
        
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.q =0
        self.t =170
        self.t_timestamp=""
        self.p_strain=0.0
        self.real_sec=0.0
        
        self.arr_p=[0.0]
        self.arr_q=[0.0]
        self.arr_t=[0.0]
        self.arr_p1=[0.0]
        self.arr_q1=[0.0]
        self.arr_t_timestamp=[""]
        self.arr_key_id=[0.0]
        
        self.x=0
        self.y=0
        #self.ax = self.figure.add_subplot(111) 
        self.xlim=0
        self.ylim=10
        self.line_cnt=0
        self.line_cnt2=0
        self.xlim_update='NO'
        self.ylim_update='NO'
        ##############
        self.buff=[]
        self.ybuff=[]
        self.line=""
        self.yline=""
        self.flag=1
        
        self.check_R=""
        self.check_S=""
        self.IO_error_flg=0
        
        self.timer1=QtCore.QTimer()
       
       
        
        self.speed_val=""
        self.input_speed_val=""
        self.goahead_flag=0
        self.calc_speed=0
        self.command_str=""
        self.save_data_flg=""
        self.load_cell_hi=0
        self.load_cell_lo=0
        self.extiometer=0
        self.encoder=0      
        self.auto_rev_time_off=0
        self.break_sence=0
        self.test_motor_speed=0
        self.test_guage_mm=0
        self.test_type="Tensile"
        self.max_load=0
        self.max_length=0
        self.flexural_max_load=100
        self.q_mpa =0
        self.arr_p_strain=[0.0]
        self.arr_q_mpa=[0.0]
        self.cs_area=0
        self.d_av=0
        self.t_av=0
        self.graph_type=""
        self.elapsed_time=0
        self.elapsed_time_show=0
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.circumference=0
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
   
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
        #self.line_cnt2, = self.axes2.plot([0,0], [0,0], lw=2)
#         connection = sqlite3.connect("tyr.db")              
#         with connection:        
#                 cursor = connection.cursor()                            
#                 cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
#         connection.commit();
#         connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_ID,CURRENT_TIMESTAMP ,GRAPH_TYPE,CIRCUMFARANCE FROM TEST_MST_TMP") 
        for x in results:
                        self.axes.set_title('Sample ID :'+str(x[0])+" Date :"+str(x[1])[0:10]+"")                        
                        self.graph_type=str(x[2])
                        self.axes.set_xlabel('Expansion (mm)')
                        self.axes.set_ylabel('Pressure (MPa)')
                        self.cs_area= 0
                        self.circumference=str(x[3])
        connection.close()
        
        
                   
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,PROOF_TEST_BY,PROOF_MAX_LOAD,PROOF_MAX_LENGTH,TEST_TIME_SEC,D_AV,T_AV from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=float(x[0])             
             self.max_load=int(x[2])
             #self.max_load=100
             self.max_length=float(float(x[0])-float(x[3]))
             self.flex_max_length=float(x[3])
             self.cof_max_length=float(x[4])
             #self.max_load=str(self.max_load).zfill(5)
             #self.max_length=str(int(self.max_length)).zfill(5)
             #self.max_length=float(x[3])
             print("Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
             self.unit_type=str(x[5])
             self.proof_test_by=str(x[6])
             self.proof_max_load=int(str("9999"))
             self.proof_max_length=float(str(x[8]))
             self.test_time_sec=int(str(x[9]))
             self.d_av=float((str(x[10])))
             self.t_av=float((str(x[11])))
             
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:
             #self.axes.set_xlim(0,int(x[0]))
             #self.axes.set_ylim(0,int(x[1]))
             #self.flexural_max_load=int(x[1])
             #self.xlim=int(x[0])
             #self.ylim=int(x[1])
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'PRESSURE_VS_EXPANSION' LIMIT 1") 
        for x in results:
             self.axes.set_xlim(0,float(x[0]))
             self.axes.set_ylim(0,float(x[1]))          
        connection.close()
        
        
        '''
        
        '''
        self.test_guage_mm=609
        self.max_load=0
        self.cof_max_length=100
        #print("434Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
        
        
        try:
            self.ser = serial.Serial(
                        port='/dev/ttyUSB0',
                        baudrate=19200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        xonxoff=False,
                        timeout = 0.05
                    )
          
            self.ser.flush()
            self.ser.write(b'*D\r')
            self.yline = self.ser.readline()
            print("Check for Load Cel o/p:"+str(self.yline))
            ystr3=str(self.yline)
            ystr3=ystr3[1:int(len(ystr3)-1)]
            ystr2=ystr3.replace("'\\r","")        
            #print("replace3('\r):"+str(xstr2))
            ystr1=ystr2.replace("'","")        
            #print("replace2('):"+str(xstr1))
            ystr=ystr1.replace("\\r","")
            #print("replace1(\r):"+str(xstr))        
            self.ybuff=ystr.split("_")
            print("Length of Array :"+str(len(self.ybuff)))
            #==== Guage Length Setting before staret =====
            self.ser.flush()
            
            if(self.test_type=="Flexural"):
                #self.test_guage_mm=0
                #self.command_str="*G0.00\r"
                self.command_str="*G%.2f"%self.test_guage_mm+"\r"
            else:
                self.command_str="*G000.0\r"
                
            print("Guage Length Command : "+str(self.command_str))
            
            b = bytes(self.command_str, 'utf-8')
            self.ser.write(b)
            #time.sleep(2)
            #===== Auto Reverse Time Off =====
            self.ser.flush()
            self.command_str="*O%04d"%self.auto_rev_time_off+"\r"
            print("Auto reve. Time off Command : "+str(self.command_str))
            b = bytes(self.command_str, 'utf-8')
            self.ser.write(b)
            #time.sleep(2)
            #========Motor Speed and Breaking Sence =========            
            self.validate_speed()            
            if(self.goahead_flag==1):
                b = bytes(self.command_str, 'utf-8')
                self.ser.write(b)
            else:   
                self.ser.write(b'*P0050_0010\r')
                
                
            #time.sleep(2)
            #========Final Motor start Command =========
            self.ser.flush()           
                
            if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                        self.ser.write(b'*S2T000.0 000.0\r')
                        print("Start Command :*S2T000.0 000.0\r")
                    else:
                        self.ser.write(b'*S1T000.0 000.0\r')
                        print("Start Command:*S1T000.0 000.0\r")
            else:
                    print("Error :Serial O/P is not getting ")
            
        except IOError:
            #print("IO Errors")
            self.IO_error_flg=1
        
        
        self.timer1.setInterval(1000)     
        self.timer1.timeout.connect(self.update_graph)
        self.timer1.start(1)
   
        self.x1,self.y1 = [],[]
        self.x2,self.y2 = [],[]
        self.lines = []
        lobj = self.axes.plot([],[],lw=2)[0]
        #lobj2 = self.axes2.plot([],[],lw=2)[0]
        
        self.lines.append(lobj)
        #self.lines.append(lobj2)
        self.on_ani_start()
        
        
    def update_graph(self):
        self.end_time = datetime.datetime.now()
        self.elapsed_time=self.end_time-self.start_time
        if(self.IO_error_flg==0):
            '''
           
            '''
            try:
                self.line = self.ser.readline()
                #print("Timer Job o/p:"+str(self.line))
                self.ser.flush()
                self.ser.write(b'*D\r')
            except IOError:
                print("IO Errors")    
                
            xstr3=str(self.line)
            xstr3=xstr3[1:int(len(xstr3)-1)]
            xstr2=xstr3.replace("'\\r","")        
            #print("replace3('\r):"+str(xstr2))
            xstr1=xstr2.replace("'","")        
            #print("replace2('):"+str(xstr1))
            xstr=xstr1.replace("\\r","")
            #print("replace1(\r):"+str(xstr))        
            self.buff=xstr.split("_")
        #print("length of array :"+str(len(self.buff)))
        if(int(len(self.buff)) > 8 ):
            #print("length of array :"+str(len(self.buff)))
            self.check_R = re.findall(r"[R]", xstr)
            self.check_S = re.findall("[S]", xstr)
            self.check_OK = re.findall("[OK]", xstr)
            #print("Checkking R Characher :"+str(self.check_R))
            #print("Checkking OK Characher :"+str(len(self.check_OK))) 
            if (len(self.check_R) > 0 and len(self.check_OK) ==0):
                
                
                if(str(self.buff[6])=="2"):
                    self.load_cell_hi=1
                    self.load_cell_lo=0
                else:
                    self.load_cell_hi=0
                    self.load_cell_lo=1
                    
                if(str(self.buff[7])=="2"):
                    self.extiometer=1
                    self.encoder=0
                else:
                    self.extiometer=0
                    self.encoder=1
                
                if(self.load_cell_hi==1):              
                    self.q=abs(float(self.buff[1])) #+random.randint(0,50)
                else:
                    self.q=abs(float(self.buff[0]))
                
                if(self.encoder==1):
                    self.p=abs(float(self.buff[4])) #
                else:
                    self.p=abs(float(self.buff[5]))
                
                if(self.test_type=="Compress"):
                    self.p=int(self.test_guage_mm)-self.p
                    #print("self.p :"+str(self.p))
                elif(self.test_type=="Flexural"):
                    #self.p=self.p
                    self.p=int(self.test_guage_mm)-self.p
                else:
                    self.p=self.p
                    #self.p=int(self.test_guage_mm)-self.p
                    #self.p=self.p
                '''
                self.r=170.00
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                self.arr_t.append(float(self.t))
                '''
                
                
                #self.q=abs(float(self.buff[1])) #fix val
                #self.t=abs(float(self.buff[3]))
                self.t=float(self.elapsed_time.seconds)
                #self.p=abs(float(self.buff[4])) #fix val
                #self.p_strain=(float(self.p)*100/float(20.00))
                #self.arr_p_strain.append(float(self.p)*100/float(20.00))
                if(int(self.circumference) > 0):
                     self.p_strain=(float(self.p)/float(self.circumference))*100
                else:
                     self.p_strain=0
                     
                self.arr_p_strain.append(float(self.p_strain))  
                if(float(self.t_av) > 0.0):
                        self.q_mpa=float(((float(self.q)* float(self.d_av))/(2*float(self.t_av))))
                else:
                        self.q_mpa=0.0
                
                self.arr_q_mpa.append(float(self.q_mpa)) 
                self.arr_t.append(float(self.t))
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                
                
                self.t_mod=int(self.t) % 60 
                self.t_timestamp=str(self.end_time)
                self.arr_t_timestamp.append(str(int(int(self.t)/3600)).zfill(2)+":"+str(int(int(self.t)/60)).zfill(2)+":"+str(int(int(self.t_mod))).zfill(2))
                self.real_sec=float(self.t)                
                self.arr_key_id.append(float(self.real_sec))
                
                print(" [G2 P0 ] P:"+str(self.p)+" q:"+str(self.q)+" t:"+str(self.t))
                

                
                
                if(int(self.q) > int(self.ylim)):
                    self.ylim=(int(self.q)+100)
                    self.ylim_update='YES'                   
                   
                              
                if(self.p > self.xlim):
                   self.xlim=(int(self.p)+100)
                   self.xlim_update='YES'                   
                #time.sleep(1)
                self.save_data_flg="No"
            else:                
               
                self.save_data_flg="Yes"
                self.on_ani_stop()
            
                   
    def plot_grah_only(self,i):
        '''
        self.x1.append(self.p)
        self.y1.append(self.q)
        self.x2.append(self.p)
        self.y2.append(self.t)

        self.xlist = [self.x1, self.x2]
        self.ylist = [self.y1, self.y2]
        #for index in range(0,1):
        for lnum,line in enumerate(self.lines):
            line.set_data(self.xlist[lnum], self.ylist[lnum]) # set data for each line separately.
        return self.lines
        '''
        self.line_cnt.set_data(self.arr_p,self.arr_q)       
        return [self.line_cnt]
        #return self.line_cnt,
    
   
        
    def on_ani_stop(self):
        self.on_stop()
        if self.playing:
            self.ani._stop()
        else:
             pass
            
    def on_stop(self):
        if(self.timer1.isActive()): 
           self.timer1.stop()
           
#    def init(self):
#        self.line_cnt.set_data([], [])
#        return self.line_cnt,



    def init(self):
        for line in self.lines:
            line.set_data([],[])
        return self.lines
   

    def on_ani_start(self):        
        if self.playing:
            pass
        else:
            self.playing = True
            self.ani = animation.FuncAnimation(
                self.figure,
                self.plot_grah_only,init_func=self.init
                ,blit=True
                ,interval=10
                    )
            
            print("Done1")
            
    
    
    def validate_speed(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT IFNULL(MOTOR_MAX_SPEED,0) from SETTING_MST") 
        for x in results:
             self.speed_val=str(x[0])
        connection.close()
        self.goahead_flag=0
        '''        
        '''
        self.input_speed_val=100
        if(self.input_speed_val != ""):
            if(int(self.input_speed_val) <= int(self.speed_val)):
                 #print(" Ok ")
                 self.goahead_flag=1
                 self.calc_speed=(int(self.input_speed_val)/int(self.speed_val))*1000                 
                 
                 self.command_str="*P%04d"%self.calc_speed+"_%04d"%self.break_sence+"\r"
                 print("Morot Speed and Breaking speed Command  :"+str(self.command_str))
            else:
                 print(" not Ok ")
                 
        else:
            print(" not Ok  ")  ### End of G2
            

class PlotCanvasG2_Auto_P1(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="tyr"
#         self.axes.set_xlabel('Expansion (mm)')
#         self.axes.set_ylabel('Pressure (MPa)')
        self.axes.grid(which='major', linestyle='-', linewidth='0.50', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.50', color='black')
        
#         self.axes2 = self.axes.twinx()
#         color = 'tab:green'
#         self.axes2.set_ylabel('Time (Sec)', color = color)
#         self.axes2.set_ylim(0,500)
        
        
        
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.p_strain=0
        self.q =0
        self.t =170
        
        self.arr_p=[0.0]
        self.arr_q=[0.0]
        self.arr_t=[0.0]
        self.arr_p1=[0.0]
        self.arr_q1=[0.0]
        self.x=0
        self.y=0
        #self.ax = self.figure.add_subplot(111) 
        self.xlim=0
        self.ylim=10
        self.line_cnt=0
        self.line_cnt2=0
        self.xlim_update='NO'
        self.ylim_update='NO'
        ##############
        self.buff=[]
        self.ybuff=[]
        self.line=""
        self.yline=""
        self.flag=1
        
        self.check_R=""
        self.check_S=""
        self.IO_error_flg=0
        
        self.timer1=QtCore.QTimer()
       
       
        
        self.speed_val=""
        self.input_speed_val=""
        self.goahead_flag=0
        self.calc_speed=0
        self.command_str=""
        self.save_data_flg=""
        self.load_cell_hi=0
        self.load_cell_lo=0
        self.extiometer=0
        self.encoder=0      
        self.auto_rev_time_off=0
        self.break_sence=0
        self.test_motor_speed=0
        self.test_guage_mm=0
        self.test_type="Tensile"
        self.max_load=0
        self.max_length=0
        self.flexural_max_load=100
        self.q_mpa =0
        self.arr_p_strain=[0.0]
        self.arr_q_mpa=[0.0]
        self.cs_area=0
        self.d_av=0
        self.t_av=0
        self.graph_type=""
        self.elapsed_time=0
        self.elapsed_time_show=0
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.circumference="0"
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
   
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
        #self.line_cnt2, = self.axes2.plot([0,0], [0,0], lw=2)
#         connection = sqlite3.connect("tyr.db")              
#         with connection:        
#                 cursor = connection.cursor()                            
#                 cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
#         connection.commit();
#         connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_ID,CURRENT_TIMESTAMP ,GRAPH_TYPE,CIRCUMFARANCE FROM TEST_MST_TMP") 
        for x in results:
                        self.axes.set_title('Sample ID :'+str(x[0])+" Date :"+str(x[1])[0:10]+"")                        
                        self.graph_type=str(x[2])
                        self.axes.set_xlabel('Strain (%)')
                        self.axes.set_ylabel('Stress (MPa)')
                        self.cs_area= 0
                        self.circumference=str(x[3])
        connection.close()
        
        
                   
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,PROOF_TEST_BY,PROOF_MAX_LOAD,PROOF_MAX_LENGTH,TEST_TIME_SEC,D_AV,T_AV from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=float(x[0])             
             self.max_load=int(x[2])
             #self.max_load=100
             self.max_length=float(float(x[0])-float(x[3]))
             self.flex_max_length=float(x[3])
             self.cof_max_length=float(x[4])
             #self.max_load=str(self.max_load).zfill(5)
             #self.max_length=str(int(self.max_length)).zfill(5)
             #self.max_length=float(x[3])
             print("Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
             self.unit_type=str(x[5])
             self.proof_test_by=str(x[6])
             self.proof_max_load=int(str("9999"))
             self.proof_max_length=float(str(x[8]))
             self.test_time_sec=int(str(x[9]))
             self.d_av=float((str(x[10])))
             self.t_av=float((str(x[11])))
             
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:
             #self.axes.set_xlim(0,int(x[0]))
             #self.axes.set_ylim(0,int(x[1]))
             #self.flexural_max_load=int(x[1])
             #self.xlim=int(x[0])
             #self.ylim=int(x[1])
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'STRESS_VS_STRAIN' LIMIT 1") 
        for x in results:
             self.axes.set_xlim(0,float(x[0]))
             self.axes.set_ylim(0,float(x[1]))          
        connection.close()
        
        
        '''
        
        '''
        self.test_guage_mm=609
        self.max_load=0
        self.cof_max_length=100
        print("434Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
        try:
            self.ser = serial.Serial(
                            port='/dev/ttyUSB0',
                            baudrate=19200,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            xonxoff=False,
                            timeout = 0.05
                        )
        except IOError:
                 self.ser=""
                 self.IO_error_flg=1
        '''
       
        
        '''
        self.timer1.setInterval(1000)     
        self.timer1.timeout.connect(self.update_graph)
        self.timer1.start(1)
   
        self.x1,self.y1 = [],[]
        self.x2,self.y2 = [],[]
        self.lines = []
        lobj = self.axes.plot([],[],lw=2)[0]
        #lobj2 = self.axes2.plot([],[],lw=2)[0]
        
        self.lines.append(lobj)
        #self.lines.append(lobj2)
        self.on_ani_start()
        
        
    def update_graph(self):
        self.end_time = datetime.datetime.now()
        self.elapsed_time=self.end_time-self.start_time
        if(self.IO_error_flg==0):
            '''
           
            '''
            try:
                self.line = self.ser.readline()
                print("Timer Job o/p:"+str(self.line))
                self.ser.flush()
                self.ser.write(b'*D\r')
            except IOError:
                print("IO Errors")    
                
            xstr3=str(self.line)
            xstr3=xstr3[1:int(len(xstr3)-1)]
            xstr2=xstr3.replace("'\\r","")        
            #print("replace3('\r):"+str(xstr2))
            xstr1=xstr2.replace("'","")        
            #print("replace2('):"+str(xstr1))
            xstr=xstr1.replace("\\r","")
            #print("replace1(\r):"+str(xstr))        
            self.buff=xstr.split("_")
        #print("length of array :"+str(len(self.buff)))
        if(int(len(self.buff)) > 8 ):
            #print("length of array :"+str(len(self.buff)))
            self.check_R = re.findall(r"[R]", xstr)
            self.check_S = re.findall("[S]", xstr)
            self.check_OK = re.findall("[OK]", xstr)
            #print("Checkking R Characher :"+str(self.check_R))
            #print("Checkking OK Characher :"+str(len(self.check_OK))) 
            if (len(self.check_R) > 0 and len(self.check_OK) ==0):
                
                
                if(str(self.buff[6])=="2"):
                    self.load_cell_hi=1
                    self.load_cell_lo=0
                else:
                    self.load_cell_hi=0
                    self.load_cell_lo=1
                    
                if(str(self.buff[7])=="2"):
                    self.extiometer=1
                    self.encoder=0
                else:
                    self.extiometer=0
                    self.encoder=1
                
                if(self.load_cell_hi==1):              
                    self.q=abs(float(self.buff[1])) #+random.randint(0,50)
                else:
                    self.q=abs(float(self.buff[0]))
                
                if(self.encoder==1):
                    self.p=abs(float(self.buff[4])) #
                else:
                    self.p=abs(float(self.buff[5]))
                
                if(self.test_type=="Compress"):
                    self.p=int(self.test_guage_mm)-self.p
                    #print("self.p :"+str(self.p))
                elif(self.test_type=="Flexural"):
                    #self.p=self.p
                    self.p=int(self.test_guage_mm)-self.p
                else:
                    self.p=self.p
                    #self.p=int(self.test_guage_mm)-self.p
                    #self.p=self.p
                '''
                self.r=170.00
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                self.arr_t.append(float(self.t))
                '''
                
                
                #self.q=abs(float(self.buff[1])) #fix val
                #self.t=abs(float(self.buff[3]))
                self.t=float(self.elapsed_time.seconds)
                
                #self.p=abs(float(self.buff[4])) #fix val
                
                #self.p_strain=float(float(self.p)*100/float(20.00))
                #self.arr_p_strain.append(float(self.p)*100/float(20.00))
                if(int(self.circumference) > 0):
                     self.p_strain=(float(self.p)/float(self.circumference))*100
                else:
                     self.p_strain=0
                     
                self.arr_p_strain.append(float(self.p_strain))
                if(float(self.t_av) > 0.0):
                        self.q_mpa=float(((float(self.q)* float(self.d_av))/(2*float(self.t_av))))
                else:
                        self.q_mpa=0.0
                
                self.arr_q_mpa.append(float(self.q_mpa)) 
                self.arr_t.append(float(self.t))
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                #print(" Timer P:"+str(self.p)+" q:"+str(self.q)+" t:"+str(self.t))
                print(" [G2 P1 ] arr_p_strain:"+str(self.p_strain)+" q_mpa:"+str(self.q_mpa)+" t:"+str(self.t))
                


                if(int(self.q) > int(self.ylim)):
                    self.ylim=(int(self.q)+100)
                    self.ylim_update='YES'                   
                   
                              
                if(self.p > self.xlim):
                   self.xlim=(int(self.p)+100)
                   self.xlim_update='YES'                   
                #time.sleep(1)
                self.save_data_flg="No"
            else:                
               
                self.save_data_flg="Yes"
                self.on_ani_stop()
            
                   
    def plot_grah_only(self,i):
        ''''
        self.x1.append(self.p)
        self.y1.append(self.q_mpa)
        self.x2.append(self.p)
        self.y2.append(self.t)

        self.xlist = [self.x1, self.x2]
        self.ylist = [self.y1, self.y2]
        #for index in range(0,1):
        for lnum,line in enumerate(self.lines):
            line.set_data(self.xlist[lnum], self.ylist[lnum]) # set data for each line separately.
        return self.lines
        '''

        self.line_cnt.set_data(self.arr_p_strain,self.arr_q_mpa)       
        return [self.line_cnt]
        #return self.line_cnt,
    
   
        
    def on_ani_stop(self):
        self.on_stop()
        if self.playing:
            self.ani._stop()
        else:
             pass
            
    def on_stop(self):
        if(self.timer1.isActive()): 
           self.timer1.stop()
           
#    def init(self):
#        self.line_cnt.set_data([], [])
#        return self.line_cnt,



    def init(self):
        for line in self.lines:
            line.set_data([],[])
        return self.lines
   

    def on_ani_start(self):        
        if self.playing:
            pass
        else:
            self.playing = True
            self.ani = animation.FuncAnimation(
                self.figure,
                self.plot_grah_only,init_func=self.init
                ,blit=True
                ,interval=10
                    )
            
            print("Done1")
            
    
    
    def validate_speed(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT IFNULL(MOTOR_MAX_SPEED,0) from SETTING_MST") 
        for x in results:
             self.speed_val=str(x[0])
        connection.close()
        self.goahead_flag=0
        '''        
        '''
        self.input_speed_val=100
        if(self.input_speed_val != ""):
            if(int(self.input_speed_val) <= int(self.speed_val)):
                 #print(" Ok ")
                 self.goahead_flag=1
                 self.calc_speed=(int(self.input_speed_val)/int(self.speed_val))*1000                 
                 
                 self.command_str="*P%04d"%self.calc_speed+"_%04d"%self.break_sence+"\r"
                 print("Morot Speed and Breaking speed Command  :"+str(self.command_str))
            else:
                 print(" not Ok ")
                 
        else:
            print(" not Ok ") ### End G2 Auto P1
            
            
   


class PlotCanvasG2_Auto_P2(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="tyr"
        self.axes.set_xlabel('Expansion (mm)')
        self.axes.set_ylabel('Pressure (MPa)')
        self.axes.grid(which='major', linestyle='-', linewidth='0.50', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.50', color='black')
        
#         self.axes2 = self.axes.twinx()
#         color = 'tab:green'
#         self.axes2.set_ylabel('Time (Sec)', color = color)
#         self.axes2.set_ylim(0,500)
        
        
        
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.p_strain=0
        self.q =0
        self.t =170
        
        self.arr_p=[0.0]
        self.arr_q=[0.0]
        self.arr_t=[0.0]
        self.arr_p1=[0.0]
        self.arr_q1=[0.0]
        self.x=0
        self.y=0
        #self.ax = self.figure.add_subplot(111) 
        self.xlim=0
        self.ylim=10
        self.line_cnt=0
        self.line_cnt2=0
        self.xlim_update='NO'
        self.ylim_update='NO'
        ##############
        self.buff=[]
        self.ybuff=[]
        self.line=""
        self.yline=""
        self.flag=1
        
        self.check_R=""
        self.check_S=""
        self.IO_error_flg=0
        
        self.timer1=QtCore.QTimer()
       
       
        
        self.speed_val=""
        self.input_speed_val=""
        self.goahead_flag=0
        self.calc_speed=0
        self.command_str=""
        self.save_data_flg=""
        self.load_cell_hi=0
        self.load_cell_lo=0
        self.extiometer=0
        self.encoder=0      
        self.auto_rev_time_off=0
        self.break_sence=0
        self.test_motor_speed=0
        self.test_guage_mm=0
        self.test_type="Tensile"
        self.max_load=0
        self.max_length=0
        self.flexural_max_load=100
        self.q_mpa =0
        self.arr_p_strain=[0.0]
        self.arr_q_mpa=[0.0]
        self.cs_area=0
        self.d_av=0
        self.t_av=0
        self.graph_type=""
        self.elapsed_time=0
        self.elapsed_time_show=0
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
   
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
        #self.line_cnt2, = self.axes2.plot([0,0], [0,0], lw=2)
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                cursor = connection.cursor()                            
                cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
        connection.commit();
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_ID,CURRENT_TIMESTAMP ,GRAPH_TYPE FROM TEST_MST_TMP") 
        for x in results:
                        self.axes.set_title('Sample ID :'+str(x[0])+" Date :"+str(x[1])[0:10]+"")                        
                        self.graph_type=str(x[2])
                        self.axes.set_xlabel('Time (Sec)')
                        self.axes.set_ylabel('Stress (MPa)')
                        self.cs_area= 0
        connection.close()
        
        
                   
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,PROOF_TEST_BY,PROOF_MAX_LOAD,PROOF_MAX_LENGTH,TEST_TIME_SEC,D_AV,T_AV from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=float(x[0])             
             self.max_load=int(x[2])
             #self.max_load=100
             self.max_length=float(float(x[0])-float(x[3]))
             self.flex_max_length=float(x[3])
             self.cof_max_length=float(x[4])
             #self.max_load=str(self.max_load).zfill(5)
             #self.max_length=str(int(self.max_length)).zfill(5)
             #self.max_length=float(x[3])
             print("Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
             self.unit_type=str(x[5])
             self.proof_test_by=str(x[6])
             self.proof_max_load=int(str("9999"))
             self.proof_max_length=float(str(x[8]))
             self.test_time_sec=int(str(x[9]))
             self.d_av=float((str(x[10])))
             self.t_av=float((str(x[11])))
             
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:
             #self.axes.set_xlim(0,int(x[0]))
             #self.axes.set_ylim(0,int(x[1]))
             #self.flexural_max_load=int(x[1])
             #self.xlim=int(x[0])
             #self.ylim=int(x[1])
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'STRESS_VS_TIME' LIMIT 1") 
        for x in results:
             self.axes.set_xlim(0,float(x[0]))
             self.axes.set_ylim(0,float(x[1]))          
        connection.close()
        
        
        '''
        
        '''
        self.test_guage_mm=609
        self.max_load=0
        self.cof_max_length=100
        #print("434Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
        try:
            self.ser = serial.Serial(
                            port='/dev/ttyUSB0',
                            baudrate=19200,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            xonxoff=False,
                            timeout = 0.05
                        )
        except IOError:
                 self.ser=""
                 self.IO_error_flg=1
        
        '''
       
        
        '''
        self.timer1.setInterval(1000)     
        self.timer1.timeout.connect(self.update_graph)
        self.timer1.start(1)
   
        self.x1,self.y1 = [],[]
        self.x2,self.y2 = [],[]
        self.lines = []
        lobj = self.axes.plot([],[],lw=2)[0]
        #lobj2 = self.axes2.plot([],[],lw=2)[0]
        
        self.lines.append(lobj)
        #self.lines.append(lobj2)
        self.on_ani_start()
        
        
    def update_graph(self):
        self.end_time = datetime.datetime.now()
        self.elapsed_time=self.end_time-self.start_time
        if(self.IO_error_flg==0):
            '''
           
            '''
            try:
                self.line = self.ser.readline()
                #print("Timer Job o/p:"+str(self.line))
                self.ser.flush()
                self.ser.write(b'*D\r')
            except IOError:
                print("IO Errors")    
                
            xstr3=str(self.line)
            xstr3=xstr3[1:int(len(xstr3)-1)]
            xstr2=xstr3.replace("'\\r","")        
            #print("replace3('\r):"+str(xstr2))
            xstr1=xstr2.replace("'","")        
            #print("replace2('):"+str(xstr1))
            xstr=xstr1.replace("\\r","")
            #print("replace1(\r):"+str(xstr))        
            self.buff=xstr.split("_")
        #print("length of array :"+str(len(self.buff)))
        if(int(len(self.buff)) > 8 ):
            #print("length of array :"+str(len(self.buff)))
            self.check_R = re.findall(r"[R]", xstr)
            self.check_S = re.findall("[S]", xstr)
            self.check_OK = re.findall("[OK]", xstr)
            #print("Checkking R Characher :"+str(self.check_R))
            #print("Checkking OK Characher :"+str(len(self.check_OK))) 
            if (len(self.check_R) > 0 and len(self.check_OK) ==0):
                
                
                if(str(self.buff[6])=="2"):
                    self.load_cell_hi=1
                    self.load_cell_lo=0
                else:
                    self.load_cell_hi=0
                    self.load_cell_lo=1
                    
                if(str(self.buff[7])=="2"):
                    self.extiometer=1
                    self.encoder=0
                else:
                    self.extiometer=0
                    self.encoder=1
                
                if(self.load_cell_hi==1):              
                    self.q=abs(float(self.buff[1])) #+random.randint(0,50)
                else:
                    self.q=abs(float(self.buff[0]))
                
                if(self.encoder==1):
                    self.p=abs(float(self.buff[4])) #
                else:
                    self.p=abs(float(self.buff[5]))
                
                if(self.test_type=="Compress"):
                    self.p=int(self.test_guage_mm)-self.p
                    #print("self.p :"+str(self.p))
                elif(self.test_type=="Flexural"):
                    #self.p=self.p
                    self.p=int(self.test_guage_mm)-self.p
                else:
                    self.p=self.p
                    #self.p=int(self.test_guage_mm)-self.p
                    #self.p=self.p
                '''
                self.r=170.00
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                self.arr_t.append(float(self.t))
                '''
                
                
                #self.q=abs(float(self.buff[1])) #fix val
                #self.t=abs(float(self.buff[3]))
                self.t=float(self.elapsed_time.seconds)
                #self.p=abs(float(self.buff[4])) #fix val
                self.p_strain=float(float(self.p)*100/float(20.00))
                self.arr_p_strain.append(float(self.p)*100/float(20.00))
                
                if(float(self.t_av) > 0.0):
                        self.q_mpa=float(((float(self.q)* float(self.d_av))/(2*float(self.t_av))))
                else:
                        self.q_mpa=0.0
                
                self.arr_q_mpa.append(float(self.q_mpa)) 
                self.arr_t.append(float(self.t))
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                print(" [G2 P2] P:"+str(self.p)+" q:"+str(self.q)+" t:"+str(self.t))
                

                if(int(self.q) > int(self.ylim)):
                    self.ylim=(int(self.q)+100)
                    self.ylim_update='YES'                   
                   
                              
                if(self.p > self.xlim):
                   self.xlim=(int(self.p)+100)
                   self.xlim_update='YES'                   
                #time.sleep(1)
                self.save_data_flg="No"
            else:                
               
                self.save_data_flg="Yes"
                self.on_ani_stop()
            
                   
    def plot_grah_only(self,i):
        '''
        self.x1.append(self.t)
        self.y1.append(self.q_mpa)
        self.x2.append(self.t)
        self.y2.append(self.t)

        self.xlist = [self.x1, self.x2]
        self.ylist = [self.y1, self.y2]
        #for index in range(0,1):
        for lnum,line in enumerate(self.lines):
            line.set_data(self.xlist[lnum], self.ylist[lnum]) # set data for each line separately.
        return self.lines
        '''

        self.line_cnt.set_data(self.arr_t,self.arr_q_mpa)       
        return [self.line_cnt]
         #return self.line_cnt,
    
   
        
    def on_ani_stop(self):
        self.on_stop()
        if self.playing:
            self.ani._stop()
        else:
             pass
            
    def on_stop(self):
        if(self.timer1.isActive()): 
           self.timer1.stop()
           
#    def init(self):
#        self.line_cnt.set_data([], [])
#        return self.line_cnt,



    def init(self):
        for line in self.lines:
            line.set_data([],[])
        return self.lines
   

    def on_ani_start(self):        
        if self.playing:
            pass
        else:
            self.playing = True
            self.ani = animation.FuncAnimation(
                self.figure,
                self.plot_grah_only,init_func=self.init
                ,blit=True
                ,interval=10
                    )
            
            print("Done1")
            
    
    
    def validate_speed(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT IFNULL(MOTOR_MAX_SPEED,0) from SETTING_MST") 
        for x in results:
             self.speed_val=str(x[0])
        connection.close()
        self.goahead_flag=0
        '''        
        '''
        self.input_speed_val=100
        if(self.input_speed_val != ""):
            if(int(self.input_speed_val) <= int(self.speed_val)):
                 #print(" Ok ")
                 self.goahead_flag=1
                 self.calc_speed=(int(self.input_speed_val)/int(self.speed_val))*1000                 
                 
                 self.command_str="*P%04d"%self.calc_speed+"_%04d"%self.break_sence+"\r"
                 print("Morot Speed and Breaking speed Command  :"+str(self.command_str))
            else:
                 print(" not Ok ")
                 
        else:
            print(" not Ok ")
            

            











if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = pop_graph2_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
