# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_29_weight_cam3.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from wt_31_weight_cam_2 import wt_31_Ui_MainWindow



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
import numpy as np
import cv2, threading, time
try:
    import queue
except ImportError:
    import Queue as queue
import os,sys,time
import datetime
import time

import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

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
import re

from reportlab.lib import colors
#from reportlab.lib.pagesizes import letter, inch
from reportlab.lib.pagesizes import landscape, letter,inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
from reportlab.pdfgen.canvas import Canvas

import pandas as pd
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from reportlab.rl_settings import showBoundary

import urllib.request
import urllib.parse
import json
import sqlite3


c1_connection = None
c2_connection = None 
c3_connection = None 
c4_connection = None 

connection = sqlite3.connect("wt.db")
results=connection.execute("SELECT IP_ADD,USER_ID,PASSWD,PORT FROM CAMERA_CONF WHERE CAMERA_NO='1'")       
for x in results:        
    c1_connection=str("rtsp://"+str(x[1])+":"+str(x[2])+"@"+str(x[0])+":"+str(x[3]))
                       #"rtsp://admin:31dec2019@192.168.1.21:554"
        #print (" c1_connection :"+str(c1_connection))
connection.close()



connection = sqlite3.connect("wt.db")
results=connection.execute("SELECT IP_ADD,USER_ID,PASSWD,PORT FROM CAMERA_CONF WHERE CAMERA_NO='2'")       
for x in results:        
        c2_connection=str("rtsp://"+str(x[1])+":"+str(x[2])+"@"+str(x[0])+":"+str(x[3]))
                       #"rtsp://admin:31dec2019@192.168.1.21:554"
        #print (" c2_connection :"+str(c2_connection))
connection.close()       



connection = sqlite3.connect("wt.db")
results=connection.execute("SELECT IP_ADD,USER_ID,PASSWD,PORT FROM CAMERA_CONF WHERE CAMERA_NO='3'")       
for x in results:        
     c3_connection=str("rtsp://"+str(x[1])+":"+str(x[2])+"@"+str(x[0])+":"+str(x[3]))
                       #"rtsp://admin:31dec2019@192.168.1.21:554"
        #print (" c3_connection :"+str(c3_connection))
connection.close()


connection = sqlite3.connect("wt.db")
results=connection.execute("SELECT IP_ADD,USER_ID,PASSWD,PORT FROM CAMERA_CONF WHERE CAMERA_NO='4'")       
for x in results:        
        c4_connection=str("rtsp://"+str(x[1])+":"+str(x[2])+"@"+str(x[0])+":"+str(x[3]))
                       #"rtsp://admin:31dec2019@192.168.1.21:554"
        #print (" c4_connection :"+str(c4_connection))
connection.close()
        



class wt_29_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 764)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1341, 711))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.pass_flg="No"
        self.first_wt_flag="Yes"
        
        self.list_type=""
        self.vehicle_no=""
        self.amount=""
        self.party_name=""
        self.supplier_name=""
        self.transport_name=""
        self.materail_name=""
        self.first_wt_mode=""
        self.first_wt_val=""        
        self.net_wt_val=""
        self.weight_type=""
        self.rate=""
        self.serial_id=""
        self.line = ""
        self.first_wt=0
        self.second_wt=0
        self.cap_gross_wt=0
        self.cap_tare_wt=0
        self.IO_error_flg=0
        self.gross_wt=""  
        self.tare_wt=""
        self.net_wt=0
        self.amount=0
        self.re_str = ""
        self.regex = ""
        self.rate= ""
        self.xstr3=""
        self.xstr2=""
        self.xstr4=""
        self.line =""
        self.IO_error_flg=0  
        self.serial_no="00"
        
        self.tot_bags=0
        self.AVG_bag_wt=0
        self.enable_buttons_flag="No"
        self.enable_counter=0
        self.last_value=0
        self.current_value=0
        self.sms_message_str="This is sample sms for the wighing test"
        self.sms_phnoe_no=""
        self.wt_limit="0"
        self.weighing_crosses_min_wt_lim="No"
        
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 670, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(650, 670, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(790, 670, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(760, 490, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 320, 411, 131))
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setProperty("value", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 490, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(230, 490, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(760, 320, 221, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_39 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("")
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_3.addWidget(self.label_39, 0, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("")
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 1, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("")
        self.label_38.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_3.addWidget(self.label_38, 0, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("")
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 1, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_3.addWidget(self.label_34, 3, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 2, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_3.addWidget(self.label_35, 3, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 2, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.frame)
        self.label_40.setGeometry(QtCore.QRect(900, 490, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_40.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(1170, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(1170, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_42 = QtWidgets.QLabel(self.frame)
        self.label_42.setGeometry(QtCore.QRect(1030, 350, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_42.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.label_45 = QtWidgets.QLabel(self.frame)
        self.label_45.setGeometry(QtCore.QRect(1030, 310, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_45.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.frame)
        self.label_46.setGeometry(QtCore.QRect(1180, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(440, 460, 551, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(1040, 440, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(490, 320, 221, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self._2 = QtWidgets.QGridLayout(self.layoutWidget)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setObjectName("_2")
        self.label_36 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("")
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self._2.addWidget(self.label_36, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_37 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("")
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self._2.addWidget(self.label_37, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self._2.addWidget(self.label_23, 1, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self._2.addWidget(self.label_27, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self._2.addWidget(self.label_25, 2, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self._2.addWidget(self.label_28, 2, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self._2.addWidget(self.label_26, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self._2.addWidget(self.label_29, 3, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(490, 490, 82, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(580, 490, 82, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(490, 570, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(730, 570, 221, 31))
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
        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setGeometry(QtCore.QRect(1040, 480, 256, 211))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(100, 250, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(420, 250, 211, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.frame)
        self.label_49.setGeometry(QtCore.QRect(720, 250, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_49.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.label_51 = QtWidgets.QLabel(self.frame)
        self.label_51.setGeometry(QtCore.QRect(1040, 250, 211, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 60, 1231, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget1)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.layoutWidget1)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 0, 1, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.layoutWidget1)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout.addWidget(self.graphicsView_3, 0, 2, 1, 1)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.layoutWidget1)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout.addWidget(self.graphicsView_4, 0, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(190, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(20, 250, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(380, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(470, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(710, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(800, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setGeometry(QtCore.QRect(1010, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setGeometry(QtCore.QRect(1100, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame)
        self.pushButton_20.setGeometry(QtCore.QRect(330, 250, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame)
        self.pushButton_21.setGeometry(QtCore.QRect(640, 250, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame)
        self.pushButton_22.setGeometry(QtCore.QRect(950, 250, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 540, 441, 151))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 30, 411, 101))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(35)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(189, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
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
        self.pushButton_5.setText(_translate("MainWindow", "Next"))
        self.pushButton_6.setText(_translate("MainWindow", "Reset"))
        self.pushButton_7.setText(_translate("MainWindow", "Return"))
        self.label_24.setText(_translate("MainWindow", "Net Weight (Kg) :"))
        self.pushButton_9.setText(_translate("MainWindow", "Capture Gross Weight(Kg) "))
        self.pushButton_10.setText(_translate("MainWindow", "Capture Tare Weight(Kg)"))
        self.label_39.setText(_translate("MainWindow", "--"))
        self.label_31.setText(_translate("MainWindow", "--"))
        self.label_38.setText(_translate("MainWindow", "Second. Wt.Type :"))
        self.label_30.setText(_translate("MainWindow", "Second. Wt. Date :"))
        self.label_34.setText(_translate("MainWindow", "Second. Wt. (Kg) :"))
        self.label_32.setText(_translate("MainWindow", "Second Wt. Time :"))
        self.label_35.setText(_translate("MainWindow", "0"))
        self.label_33.setText(_translate("MainWindow", "--:-- "))
        self.label_40.setText(_translate("MainWindow", "0"))
        self.pushButton_17.setText(_translate("MainWindow", "Get Record"))
        self.label_42.setText(_translate("MainWindow", "Search Slip No:"))
        self.label_45.setText(_translate("MainWindow", "Current Slip No:"))
        self.label_46.setText(_translate("MainWindow", "0"))
        self.label_50.setText(_translate("MainWindow", "First Weight Only"))
        self.label_36.setText(_translate("MainWindow", "First Wt.Type :"))
        self.label_37.setText(_translate("MainWindow", "--"))
        self.label_23.setText(_translate("MainWindow", "First Wt. Date :"))
        self.label_27.setText(_translate("MainWindow", "--"))
        self.label_25.setText(_translate("MainWindow", "First Wt. Time :"))
        self.label_28.setText(_translate("MainWindow", "--:-- "))
        self.label_26.setText(_translate("MainWindow", "First Wt. (Kg) :"))
        self.label_29.setText(_translate("MainWindow", "0"))
        self.radioButton.setText(_translate("MainWindow", "Auto"))
        self.radioButton_2.setText(_translate("MainWindow", "Mannual"))
        self.label_2.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.label_3.setText(_translate("MainWindow", "Saved Successfully !"))
        self.label_3.hide()
       
        self.pushButton_8.setText(_translate("MainWindow", "Start-C1"))
        self.pushButton_11.setText(_translate("MainWindow", "Stop-C1"))
        self.pushButton_12.setText(_translate("MainWindow", "Save"))
        
        self.pushButton_13.setText(_translate("MainWindow", "Start-C2"))
        self.pushButton_14.setText(_translate("MainWindow", "Stop-C2"))
        self.pushButton_20.setText(_translate("MainWindow", "Save"))
        
        
        self.pushButton_15.setText(_translate("MainWindow", "Start-C3"))
        self.pushButton_16.setText(_translate("MainWindow", "Stop-C3"))
        self.pushButton_21.setText(_translate("MainWindow", "Save"))
        
        self.pushButton_18.setText(_translate("MainWindow", "Start-C4"))
        self.pushButton_19.setText(_translate("MainWindow", "Stop-C4")) 
        self.pushButton_22.setText(_translate("MainWindow", "Save"))
        
        self.groupBox.setTitle(_translate("MainWindow", "Vehicle No."))
        #self.lineEdit_5.setText(_translate("MainWindow", "MH43-AW-0302"))
        
        try:
            
            self.thread = QtCore.QThread()
            self.thread.start()
            self.vid = ShowVideo()       
            self.vid.moveToThread(self.thread)  
                  
            
            
            self.thread2 = QtCore.QThread()
            self.thread2.start()
            self.vid2 = ShowVideo2()       
            self.vid2.moveToThread(self.thread2)
                   
            
            self.thread3 = QtCore.QThread()
            self.thread3.start()
            self.vid3 = ShowVideo3()       
            self.vid3.moveToThread(self.thread3)
            self.image_viewer3 = ImageViewer()
            
            self.thread4 = QtCore.QThread()
            self.thread4.start()
            self.vid4 = ShowVideo4()       
            self.vid4.moveToThread(self.thread4)
            self.image_viewer4 = ImageViewer()
           
            self.imagec = QtGui.QImage()
            self.image_viewer = ImageViewer()
            self.image_viewer2 = ImageViewer() 
            self.gridLayout.addWidget(self.image_viewer, 0, 0, 1, 1)
            self.gridLayout.addWidget(self.image_viewer2, 0, 1, 1, 1)
            self.gridLayout.addWidget(self.image_viewer3, 0, 2, 1, 1)
            self.gridLayout.addWidget(self.image_viewer4, 0, 3, 1, 1)
            
            self.vid.VideoSignal.connect(self.image_viewer.setImage)
            self.vid2.VideoSignal.connect(self.image_viewer2.setImage)
            self.vid3.VideoSignal.connect(self.image_viewer3.setImage)
            self.vid4.VideoSignal.connect(self.image_viewer4.setImage)
            
        except BaseException as e:
                print("IO Errors"+str(e))
         
        self.pushButton_7.clicked.connect(MainWindow.close)
        self.lineEdit_5.textChanged.connect(self.text_change_f)
        
        
        #--c1 start ,stop ,save
        self.pushButton_8.clicked.connect(self.vid.startVideo) # start C1 
        self.pushButton_11.clicked.connect(self.stop_vedio_c1)  # stop C1 
        self.pushButton_12.clicked.connect(self.save_img_c1) # save C1
        
        
        
        self.pushButton_13.clicked.connect(self.vid2.startVideo) # start C2 
        self.pushButton_14.clicked.connect(self.stop_vedio_c2)  # stop C2 
        self.pushButton_20.clicked.connect(self.save_img_c2) # save C2       
        
        
               
        self.pushButton_15.clicked.connect(self.vid3.startVideo) # start C3 
        self.pushButton_16.clicked.connect(self.stop_vedio_c3)  # stop C3
        self.pushButton_21.clicked.connect(self.save_img_c3) # save C3 
        
        self.pushButton_18.clicked.connect(self.vid4.startVideo) # start C4
        self.pushButton_19.clicked.connect(self.stop_vedio_c4)  # stop C4 
        self.pushButton_22.clicked.connect(self.save_img_c4) # save C4       
        
        
        self.pushButton_9.clicked.connect(self.gross_wt_onclick)
        self.pushButton_10.clicked.connect(self.tare_wt_onclick)
        self.pushButton_5.clicked.connect(self.open_PPOP_window)
        #self.pushButton_6.clicked.connect(self.start_all_cameras)
        
        self.pushButton_17.clicked.connect(self.call_fetch_slip_via_get)
        self.listWidget_2.doubleClicked.connect(self.call_fetch_slip_via_vehicle)
        self.pushButton_6.clicked.connect(self.reset_fun)
        
        
        self.label_45.hide()
        self.label_46.hide()
        self.load_2nd_wt_vehicles()
        self.timer1=QtCore.QTimer()
        self.timer2=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.start_wt()
      
    
   
        
        
        
        
    
     #################################
    def stop_vedio_c1(self):
        self.vid.run_video = False
        #self.vid.stopVideo()
        #time.sleep(5)
   
    
    def save_img_c1(self):
        print("inside stop camera  C1! ")
        self.vid.VideoSignal.connect(self.copyImageC1)

    def copyImageC1(self,image):
        file_path="./camera_images"
        file_name="CAM1_xxx.jpg"
        if image.isNull():
            print("no imput imgage!")
        else:
            self.imagec = image
            self.imagec.save(str(file_path)+"/"+str(file_name), "JPG")
            print("saved data !!!!")
            self.label_47.setText(str(file_name))
            #self.vid.stopVideo()
            self.vid.run_video = False
            #time.sleep(5)
    
   ############### 
    def stop_vedio_c2(self):
        self.vid2.run_video = False
        #self.vid2.stopVideo()
        #time.sleep(5)
   
    
    def save_img_c2(self):
        print("inside stop camera C2 ! ")
        self.vid2.VideoSignal.connect(self.copyImageC2)

    def copyImageC2(self,image):
        file_path="./camera_images"
        file_name="CAM2_xxx.jpg"
        if image.isNull():
            print("no imput imgage C2!")
        else:    
            self.imagec = image
            self.imagec.save(str(file_path)+"/"+str(file_name), "JPG")
            print("saved data !!!!")
            self.label_48.setText(str(file_name))
            #self.vid2.stopVideo()
            self.vid2.run_video = False
            #time.sleep(5)
            
    
    ##########
    def stop_vedio_c3(self):
        self.vid3.run_video = False
        #self.vid2.stopVideo()
        #time.sleep(5)
   
    
    def save_img_c3(self):
        print("inside stop camera C3 ! ")
        self.vid3.VideoSignal.connect(self.copyImageC3)

    def copyImageC3(self,image):
        file_path="./camera_images"
        file_name="CAM3_xxx.jpg"
        if image.isNull():
            print("no imput imgage C3 !")
        else:    
            self.imagec = image
            self.imagec.save(str(file_path)+"/"+str(file_name), "JPG")
            print("saved data !!!!")
            self.label_49.setText(str(file_name))
            #self.vid2.stopVideo()
            self.vid3.run_video = False
            #time.sleep(5)
            
    
    ##########
    def stop_vedio_c4(self):
        self.vid4.run_video = False
        
   
    
    def save_img_c4(self):
        print("inside stop camera C4 ! ")
        self.vid4.VideoSignal.connect(self.copyImageC4)

    def copyImageC4(self,image):
        file_path="./camera_images"
        file_name="CAM4_xxx.jpg"
        if image.isNull():
            print("no imput imgage C4!")
        else:    
            self.imagec = image
            self.imagec.save(str(file_path)+"/"+str(file_name), "JPG")
            print("saved data !!!!")
            self.label_51.setText(str(file_name))
            #self.vid2.stopVideo()
            self.vid4.run_video = False
            #time.sleep(5)
            
    
    ##########
    
    
    def open_PPOP_window(self):
        self.save_data()        
        if(self.pass_flg=="Yes"):
            #self.thread.join()
            #self.thread_2.join()
            #self.thread_3.join()
            #self.thread_4.join()            
            #self.window = QtWidgets.QMainWindow()
            self.window =MyWindow()
            self.ui=wt_31_Ui_MainWindow()
            self.ui.setupUi(self.window)           
            self.window.show()
    
    def load_2nd_wt_vehicles(self):
        self.listWidget_2.clear()
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT VEHICLE_NO||' - ('||printf(\"%04d\", SERIAL_ID)||')' AS SERIAL_ID FROM WEIGHT_MST WHERE STATUS='FIRST' and (ifnull(round((julianday(CURRENT_TIMESTAMP) - julianday(FIRST_WT_CRTEATED_ON) )),0) < 10) ")       
        for x in results:        
               self.listWidget_2.addItem(str(x[0]))
        connection.close()
        
    def start_wt(self):
        #print("Weight Started ....")
        try:
            self.ser = serial.Serial(
                                port='/dev/ttyUSB0',
                                baudrate=9600,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.05
                            )
        
            self.ser.flush()        
            
            self.line = self.ser.read(20)
            print("o/p:"+str(self.line))
            
            connection = sqlite3.connect("services.db")
            results=connection.execute("select WT_LIMIT FROM DEVICE_CONF")
            for x in results:
                self.wt_limit=str(x[0])        
            connection.close()
         
        
            self.timer2.setInterval(5000)        
            self.timer2.timeout.connect(self.display_lcd_val)
            self.timer2.start(1)
            
        except IOError:
            print("IO Errors")
            self.IO_error_flg=1
        
       
        
    def display_lcd_val(self):
        
        
        #print(" inside display_lcd_val:"+str(self.IO_error_flg))
        if(self.IO_error_flg==0):
            try:
                self.line = self.ser.read(20)
                #print("o/p:"+str(self.line)) 
                if (len(self.line) > 6):
                    #print("o/p:"+str(self.line))
                    self.ser.flush()
                    self.ser.write(b'*D\r')
                    self.xstr3=str(self.line,'utf-8')
                    cnt=int(self.xstr3.find("\x02"))
                    #print("index of \x02 :"+str(cnt))
                    cnt=cnt+2                    
                    self.xstr2=self.xstr3[cnt:(cnt+6)]
                    '''
                    self.xstr3=self.xstr3[2:int(len(self.xstr3)-1)]
                    self.xstr2=self.xstr3.replace("'","")
                    self.xstr2=self.xstr3.replace("\\x02 ","")
                    self.xstr2=self.xstr3.replace("\\x03 ","")  
                    self.xstr2=self.xstr2.replace("\\n","")
                    self.xstr2=self.xstr2.replace("\\r","")
                    self.xstr2=self.xstr2.replace("\\","")
                    self.xstr2=self.xstr2.replace("'","")
                    self.xstr2=self.xstr2.replace("''","")
                    self.xstr2=self.xstr2.replace(" ","")
                    '''
                    self.xstr2=self.xstr2[0:6]
                    try:
                        self.xstr4=int(self.xstr2)
                    except ValueError:                        
                        print("Value Error"+str(self.xstr2))
                        self.xstr4=0
                    #print("Modified String:"+str(self.xstr4))                    
                    self.lcdNumber.setProperty("value", str(self.xstr4))
                    
                    
                    self.last_value=self.current_value
                    self.current_value=int(self.xstr4)
                    if(self.last_value==self.current_value):
                            self.enable_counter=self.enable_counter+1
                            if(self.enable_counter > 15):
                                 self.enable_buttons_flag="Yes"
                                 if(int(self.current_value) > int(self.wt_limit)):
                                          #self.update_device_counter()
                                          self.weighing_crosses_min_wt_lim="Yes"
                            else:
                                 self.enable_buttons_flag="No"
                                 #self.enable_counter=0
                    else:            
                            self.enable_buttons_flag="No"
                            self.enable_counter=0
                    
                    if(int(self.current_value) > int(self.wt_limit)):
                        if(self.enable_buttons_flag=="Yes"):
                            if(str(self.label_46.text()) != "0"):
                                       if(self.label_37.text() == "GROSS"):
                                           self.pushButton_9.setDisabled(True)
                                           self.pushButton_10.setEnabled(True)
                                       else:
                                           self.pushButton_10.setDisabled(True)
                                           self.pushButton_9.setEnabled(True)
                            else:
                                self.pushButton_9.setEnabled(True)
                                self.pushButton_10.setEnabled(True)
                        else:
                            self.pushButton_9.setDisabled(True)
                            self.pushButton_10.setDisabled(True)
                    else:
                            self.pushButton_9.setDisabled(True)
                            self.pushButton_10.setDisabled(True)       
                    
                    if(self.weighing_crosses_min_wt_lim=="Yes" and int(self.current_value) == 0) :
                            self.update_device_counter()
                    
            except IOError:
                print("IO Errors") 
                self.IO_error_flg=1  
          
        
    def update_device_counter(self):
        connection = sqlite3.connect("services.db")          
        with connection:        
             cursor = connection.cursor()                    
             cursor.execute("UPDATE DEVICE_CONF set DEVICE_VEHICAL_COUNTER=DEVICE_VEHICAL_COUNTER+1") 
        connection.commit();
        connection.close()
        self.weighing_crosses_min_wt_lim="No"
        
    def gross_wt_onclick(self):
        #print("self.label_46 : "+str(self.label_46.text()))
        if(str(self.label_46.text()) == "0"):
               self.label_37.setText("GROSS")         
               self.label_27.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
               self.label_28.setText(datetime.datetime.now().strftime("%H:%M"))
               self.label_29.setText(str(self.current_value))
               #self.label_29.setText(str("25"))
               
        else:     
               self.label_39.setText("GROSS")
               self.label_31.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
               self.label_35.setText(str(self.current_value))
               #self.label_35.setText(str("25"))
               self.label_33.setText(datetime.datetime.now().strftime("%H:%M"))
                       
        self.net_wt_calc()
        #self.label_54.setEnabled(True)
        #self.lineEdit_16.setEnabled(True)
    
               
    def tare_wt_onclick(self):       
        if(str(self.label_46.text()) == "0"):
               self.label_37.setText("TARE")         
               self.label_27.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
               self.label_28.setText(datetime.datetime.now().strftime("%H:%M"))
               self.label_29.setText(str(self.current_value))
               #self.label_29.setText(str("25"))
               
        else:      
               self.label_39.setText("TARE")
               self.label_31.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
               self.label_35.setText(str(self.current_value))
               #self.label_35.setText(str("20"))
               self.label_33.setText(datetime.datetime.now().strftime("%H:%M"))         
        self.net_wt_calc()
        #self.label_54.setDisabled(True)
        #self.lineEdit_16.setDisabled(True)
        #self.lineEdit_17.setDisabled(True)
        
        
    def net_wt_calc(self):        
        print(" self.label_29.text : "+str(self.label_29.text()))
        print(" self.label_35.text : "+str(self.label_35.text()))
        self.first_wt=str(self.label_29.text())
        self.second_wt=str(self.label_35.text())
        if(int(self.first_wt) > 0 and  int(self.second_wt) > 0):            
                if(int(self.first_wt) >= int(self.second_wt)):            
                      self.net_wt=(int(self.first_wt)-int(self.second_wt))             
                      self.label_40.setText(str(self.net_wt))
                else:
                      self.net_wt=(int(self.second_wt)-int(self.first_wt))             
                      self.label_40.setText(str(self.net_wt))
    
    def text_change_f(self):        
        string =self.lineEdit_5.text()
        if not (string.isupper()):
               self.lineEdit_5.setText(string.upper())
               
  
       
        
    def device_date(self):     
        self.label_2.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
   
    def save_data(self):        
        self.vehicle_no=str(self.lineEdit_5.text())
        print(" Length is :"+str(len(self.vehicle_no)))
        if(len(self.vehicle_no) >= 10):
            
           # self.party_name=str(self.lineEdit_10.text())
           # self.supplier_name=str(self.lineEdit_11.text()) 
           # self.materail_name=str(self.lineEdit_14.text())
           # self.transport_name=str(self.lineEdit_9.text())
            #self.amount=str(self.label_43.text())
            self.first_wt_mode=self.label_37.text()
            self.first_wt_val=self.label_29.text()
            self.second_wt_mode=self.label_39.text()
            self.second_wt_val=self.label_35.text()  
            self.net_wt_val=str(self.label_40.text())
            #self.rate=str(self.label_43.text())
            #self.sms_phnoe_no=str(self.lineEdit_12.text())
            print("save called")
            if (self.radioButton.isChecked()):
                    self.weight_type="AUTO"
            elif (self.radioButton_2.isChecked()):
                    self.weight_type="MANUAL"
            self.serial_id=0        
            self.serial_id=str(self.label_46.text())
                
        
        if(len(self.vehicle_no) >= 10):
             print("self.label_46.text :"+str(self.label_46.text()))
             if(str(self.label_46.text()) == "0"):
                if(int(self.first_wt_val) > 0):
                            connection = sqlite3.connect("wt.db")
                            with connection:                            
                                cursor = connection.cursor()       
                                print(" First Wt Date :"+str(self.label_27.text())+" First  Wt Time:"+str(self.label_28.text()))
                                cr_date_str=str(self.label_27.text()+" "+str(self.label_28.text())+":00")
                                print("cr_date_str:"+str(cr_date_str))
                                cr_date= datetime.datetime.strptime(cr_date_str, '%Y-%m-%d %H:%M:%S')
                                print("cr_date:"+str(cr_date))                                
                                cursor.execute("INSERT INTO WEIGHT_MST(FIRST_WEIGHT_MODE,FIRST_WEIGHT_VAL,WEIGHT_TYPE,NET_WEIGHT_VAL,VEHICLE_NO,FIRST_WT_CRTEATED_ON,CAM_REC_TYPE) VALUES('"+self.first_wt_mode+"','"+self.first_wt_val+"','"+self.weight_type+"','"+self.net_wt_val+"','"+self.vehicle_no+"','"+str(cr_date)+"','CURRENT')")
                            connection.commit();
                            connection.close()
                            print("Data Inserted !!!!")                            
                            self.label_3.show()
                            self.bkp_f()
                            self.pass_flg="Yes"
                            
                            

             else:
                print(" second weight val :"+str(self.second_wt_val)) 
                if(int(self.second_wt_val) > 0):
                            connection = sqlite3.connect("wt.db")
                            with connection:        
                                cursor = connection.cursor()
                                
                                print(" Second Wt Date :"+str(self.label_31.text())+" SEcond  Wt Time:"+str(self.label_33.text()))
                                cr_date_str_2=str(self.label_31.text()+" "+str(self.label_33.text())+":00")
                                print("cr_date_str_2:"+str(cr_date_str_2))
                                cr_date_2= datetime.datetime.strptime(cr_date_str_2, '%Y-%m-%d %H:%M:%S')
                                print("cr_date_str:"+str(cr_date_2))
                                
                                #print("UPDATE WEIGHT_MST SET SECOND_WT_MODE='"+str(self.second_wt_mode)+"', SECOND_WT_VAL='"+str(self.second_wt_val)+"', NET_WEIGHT_VAL='"+str(self.net_wt_val)+"',SECOND_WT_CREATED_ON=current_timestamp, STATUS='SECOND' , AMOUNT_2='"+str(self.rate)+"', PHONE_NO_2='"+str(self.lineEdit_12.text())+"',SECOND_WT_CREATED_ON='"+cr_date_str_2+"' WHERE SERIAL_ID='"+str(self.label_46.text())+"'")
                                cursor.execute("UPDATE WEIGHT_MST SET SECOND_WT_MODE='"+str(self.second_wt_mode)+"', SECOND_WT_VAL='"+str(self.second_wt_val)+"', NET_WEIGHT_VAL='"+str(self.net_wt_val)+"',SECOND_WT_CREATED_ON=current_timestamp, STATUS='SECOND' , SECOND_WT_CREATED_ON='"+str(cr_date_2)+"', CAM_REC_TYPE='CURRENT' WHERE SERIAL_ID='"+str(self.label_46.text())+"'")
                            connection.commit();
                            connection.close()
                            print("Data Updated !!!!")
                            self.label_3.setText(" Successfully Saved 2nd Wt.")
                            self.label_3.show()
                            self.bkp_f_upd()
                            self.pass_flg="Yes"

                else:
                            self.label_3.setText(" 2nd Wt should be greater than 0.")
                            self.label_3.show()
                            self.pass_flg="No"
                                
                                
        self.load_2nd_wt_vehicles()    
       
    def call_fetch_slip_via_get(self):        
        self.slip_no=str(self.lineEdit_15.text())
        print("Slip No :"+str(self.slip_no))
        self.fetch_slip_data()
        
    def call_fetch_slip_via_vehicle(self):
        v_str=str(self.listWidget_2.currentItem().text())
        self.re_str = str(v_str)                
        self.slip_no= re.search('\(([^)]+)', self.re_str).group(1)
        self.lineEdit_15.setText(str(self.slip_no))
        #self.slip_no=v_str[16:19]
        print("self.slip_no:"+str(self.slip_no))
        self.fetch_slip_data()
        
    
    def fetch_slip_data(self):        
        self.vehicle_no=""
        connection = sqlite3.connect("wt.db")
        print("SELECT SERIAL_ID, PARTY_NAME,SUPPLIER_NAME,TRANSPORT_NAME,MATERIAL_NAME,FIRST_WEIGHT_MODE,FIRST_WEIGHT_VAL,FIRST_WT_CRTEATED_ON ,FIRST_WT_CRTEATED_ON,NET_WEIGHT_VAL,VEHICLE_NO,AMOUNT,TRANSPORT_TYPE,SECOND_WT_MODE,SECOND_WT_VAL,SECOND_WT_CREATED_ON  FROM WEIGHT_MST WHERE SERIAL_ID='"+self.slip_no+"'")
        results=connection.execute("SELECT SERIAL_ID, PARTY_NAME,SUPPLIER_NAME,TRANSPORT_NAME,MATERIAL_NAME,FIRST_WEIGHT_MODE,FIRST_WEIGHT_VAL,FIRST_WT_CRTEATED_ON ,FIRST_WT_CRTEATED_ON,NET_WEIGHT_VAL,VEHICLE_NO,AMOUNT,TRANSPORT_TYPE,IFNULL(SECOND_WT_MODE,'--'),IFNULL(SECOND_WT_VAL,0),IFNULL(SECOND_WT_CREATED_ON,'0'),STATUS FROM WEIGHT_MST WHERE SERIAL_ID='"+self.slip_no+"'")       
        for x in results:        
            self.label_46.setText(str(x[0]).zfill(4))
            self.label_46.show()
            self.label_45.show()            
            self.label_37.setText(str(x[5]))
            
            print ("first wt mode :"+str(x[5]))
            if(str(x[5]) == "GROSS"):
                self.pushButton_9.setDisabled(True)
                self.pushButton_10.setEnabled(True)
                self.pushButton_5.setEnabled(True)
                
            if(str(x[5]) == "TARE"):
                self.pushButton_10.setDisabled(True)
                self.pushButton_9.setEnabled(True)
                self.pushButton_5.setEnabled(True)
            
            print("First Wt date :"+str(x[7]))
            self.label_27.setText(str(x[7])[0:11])
            self.label_28.setText(str(x[7])[11:16])
            self.label_29.setText(str(x[6]))
                
            
          
            self.vehicle_no=(str(x[10])) 
            self.lineEdit_5.setText(str(x[10]))
            self.label_40.setText(str(x[9]))
            #self.label_43.setText(str(x[11]))
            #self.lineEdit_13.setText(str(x[12]))
            self.label_3.hide()
            # second wt data 
            self.label_39.setText(str(x[13]))
            print ("second wt mode :"+str(x[13]))
            if(str(x[13]) == "GROSS"):
                self.pushButton_10.setDisabled(True)
                self.pushButton_9.setEnabled(True)
                
            if(str(x[13]) == "TARE"):
                self.pushButton_9.setDisabled(True)
                self.pushButton_10.setEnabled(True)             
             
                
                
            if(str(x[15]) != "0"):    
                self.label_31.setText(str(x[15])[0:11])
                self.label_33.setText(str(x[15])[11:16])
            else:    
                self.label_31.setText("00")
                self.label_33.setText("00:00")
            
            
            print("second wt:"+str(x[14]))
            self.label_35.setText(str(x[14]))
            print("Status:"+str(x[16]))
            if(str(x[16]) == "SECOND"):
               self.pushButton_9.setDisabled(True)
               self.pushButton_10.setDisabled(True)
               #self.pushButton_5.setDisabled(True)
    
        
        
    def bkp_f(self):
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT MAX(SERIAL_ID) FROM WEIGHT_MST")       
        for x in results:
            self.serial_no=str(x[0])            
        
        print("serial No:"+str(self.serial_no))        
        os.system("pwd")
        os.system("ls -ltr ")
        #os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
        #os.system("mv wt_bkp.db /media/usb")
        #os.system("sudo umount /media/usb")
        os.system("cp ./camera_images/CAM1_xxx.jpg ./camera_images/CAM1_"+str(self.serial_no)+".jpg")
        os.system("cp ./camera_images/CAM2_xxx.jpg ./camera_images/CAM2_"+str(self.serial_no)+".jpg")
        os.system("cp ./camera_images/CAM3_xxx.jpg ./camera_images/CAM3_"+str(self.serial_no)+".jpg")
        os.system("cp ./camera_images/CAM4_xxx.jpg ./camera_images/CAM4_"+str(self.serial_no)+".jpg")
       
        os.system("rm -rf ./camera_images/CAM*xxx.jpg")
        
        
    def bkp_f_upd(self):        
        self.serial_no=str(self.label_46.text())           
        
        print("serial No:"+str(self.serial_no))        
        os.system("pwd")
        os.system("ls -ltr ")
        #os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
        #os.system("mv wt_bkp.db /media/usb")
        #os.system("sudo umount /media/usb")
        os.system("cp ./camera_images/CAM1_xxx.jpg ./camera_images/CAM5_"+str(self.serial_no)+".jpg")
        os.system("cp ./camera_images/CAM2_xxx.jpg ./camera_images/CAM6_"+str(self.serial_no)+".jpg")
        os.system("cp ./camera_images/CAM3_xxx.jpg ./camera_images/CAM7_"+str(self.serial_no)+".jpg")
        os.system("cp ./camera_images/CAM4_xxx.jpg ./camera_images/CAM8_"+str(self.serial_no)+".jpg")
       
        os.system("rm -rf ./camera_images/CAM*xxx.jpg")
    
    def reset_fun(self): 
        self.label_3.hide()
        # First Wt
        self.label_37.setText("--")         
        self.label_27.setText("--")
        self.label_28.setText("--:--")
        self.label_29.setText("0")
        
        #second Wt                      
        self.label_39.setText("--")
        self.label_31.setText("--")
        self.label_35.setText("0")
        self.label_33.setText("--:--")
        
        #.label_53.setText("0")
        self.label_49.setText("")
        self.label_40.setText("0")
        self.label_46.setText("0")
        self.label_46.hide()
        self.label_45.hide()
        
        self.label_47.setText("")
        self.label_48.setText("")
        self.label_49.setText("")
        self.label_51.setText("")
        
        self.pushButton_9.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        
       
 
 # bufferless VideoCapture
class VideoCapture_new:
  def __init__(self, name):
    self.cap = cv2.VideoCapture(name)
    self.q = queue.Queue()
    t = threading.Thread(target=self._reader)
    t.daemon = True
    t.start()

  # read frames as soon as they are available, keeping only most recent one
  def _reader(self):
    while True:
      ret, frame = self.cap.read()
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()   # discard previous (unprocessed) frame
        except Queue.Empty:
          pass
      self.q.put(frame)

  def read(self):
    return self.q.get()
 
 
 
 

class ImageViewer(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)
 
 
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0,4, self.image)
        self.image = QtGui.QImage()
 
    def initUI(self):
        self.setWindowTitle('Test')
 
    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")
 
        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.update()    
    


class ShowVideo(QtCore.QObject): 
    #initiating the built in camera
    global c1_connection
    print (" c1_connection :"+str(c1_connection))
   
    camera = VideoCapture_new(c1_connection)
    
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)    
    run_video = True
    def __init__(self, parent = None):
        super(ShowVideo, self).__init__(parent)
        
        
    @QtCore.pyqtSlot() 
    def startVideo(self):        
        if(self.run_video == True):
                # frame = self.camera.read()
                while (self.run_video):            
                    frame = self.camera.read()                    
                    try:
                            frame = np.array(frame, dtype=np.uint8)
                            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)                    
                            h, w, ch = rgbImage.shape
                            bytesPerLine = ch * w
                            convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                            p = convertToQtFormat.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
                            self.VideoSignal.emit(p)
                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                break
                    except BaseException as e:
                            print("IO Errors"+str(e))
                            print(" length of frame :"+str(frame))
                   
    
    def stopVideo(self):            
            self.run_video = False
            #self.camera.release()
            cv2.destroyAllWindows()
            
   
       
class ShowVideo2(QtCore.QObject): 
    #initiating the built in camera
    global c2_connection
    print (" c2_connection :"+str(c2_connection))
   
    camera = VideoCapture_new(c2_connection)
    
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)    
    run_video = True
    def __init__(self, parent = None):
        super(ShowVideo2, self).__init__(parent)
        
        
    @QtCore.pyqtSlot() 
    def startVideo(self):        
        if(self.run_video == True):
                # frame = self.camera.read()
                while (self.run_video):            
                    frame = self.camera.read()                    
                    try:
                            frame = np.array(frame, dtype=np.uint8)
                            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)                    
                            h, w, ch = rgbImage.shape
                            bytesPerLine = ch * w
                            convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                            p = convertToQtFormat.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
                            self.VideoSignal.emit(p)
                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                break
                    except BaseException as e:
                            print("IO Errors"+str(e))
                            print(" length of frame :"+str(frame))
                   
    
    def stopVideo(self):            
            self.run_video = False
            #self.camera.release()
            cv2.destroyAllWindows()
               

class ShowVideo3(QtCore.QObject): 
    #initiating the built in camera
    global c3_connection
    print (" c3_connection :"+str(c3_connection))
   
    camera = VideoCapture_new(c3_connection)
    
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)    
    run_video = True
    def __init__(self, parent = None):
        super(ShowVideo3, self).__init__(parent)
        
        
    @QtCore.pyqtSlot() 
    def startVideo(self):        
        if(self.run_video == True):
                # frame = self.camera.read()
                while (self.run_video):            
                    frame = self.camera.read()                    
                    try:
                            frame = np.array(frame, dtype=np.uint8)
                            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)                    
                            h, w, ch = rgbImage.shape
                            bytesPerLine = ch * w
                            convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                            p = convertToQtFormat.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
                            self.VideoSignal.emit(p)
                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                break
                    except BaseException as e:
                            print("IO Errors"+str(e))
                            print(" length of frame :"+str(frame))
                   
    
    def stopVideo(self):            
            self.run_video = False
            #self.camera.release()
            cv2.destroyAllWindows()
        
         
          
class ShowVideo4(QtCore.QObject): 
    #initiating the built in camera
    global c4_connection
    print (" c4_connection :"+str(c4_connection))
   
    camera = VideoCapture_new(c4_connection)
    
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)    
    run_video = True
    def __init__(self, parent = None):
        super(ShowVideo4, self).__init__(parent)
        
        
    @QtCore.pyqtSlot() 
    def startVideo(self):        
        if(self.run_video == True):
                # frame = self.camera.read()
                while (self.run_video):            
                    frame = self.camera.read()                    
                    try:
                            frame = np.array(frame, dtype=np.uint8)
                            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)                    
                            h, w, ch = rgbImage.shape
                            bytesPerLine = ch * w
                            convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                            p = convertToQtFormat.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
                            self.VideoSignal.emit(p)
                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                break
                    except BaseException as e:
                            print("IO Errors"+str(e))
                            print(" length of frame :"+str(frame))
                   
    
    def stopVideo(self):            
            self.run_video = False
            #self.camera.release()
            cv2.destroyAllWindows()


class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self,event):               
        event.accept()
        
        print("inside sdfsdf close event") 

            
                   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_29_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
