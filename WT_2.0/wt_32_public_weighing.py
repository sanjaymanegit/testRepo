# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_32_public_weighing.ui'
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
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from wt_37_pop_print import wt_37_Ui_MainWindow

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

class wt_32_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 764)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1331, 711))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
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
        
        
        self.tot_bags=0
        self.AVG_bag_wt=0
        self.enable_buttons_flag="No"
        self.enable_counter=0
        self.last_value=0
        self.current_value=0
        self.sms_message_str="This is sample sms for the wighing test"
        self.sms_phnoe_no=""
        self.sms_phnoe_no_2=""
        self.sms_phnoe_no_3=""
        self.wt_limit="0"
        self.weighing_crosses_min_wt_lim="No"
        self.wt_type=""
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 660, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 660, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(680, 660, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(280, 590, 121, 31))
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
        self.lcdNumber.setGeometry(QtCore.QRect(10, 150, 471, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.display("000000")
        #self.lcdNumber.setProperty("value", 0)
        #self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(280, 360, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(280, 420, 221, 131))
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
        self.label_35 = QtWidgets.QLineEdit(self.layoutWidget_2)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.label_35)
        self.label_35.setValidator(input_validator)
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
        self.label_40.setGeometry(QtCore.QRect(420, 590, 91, 31))
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
        self.pushButton_17.setGeometry(QtCore.QRect(1170, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(1170, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_15.setFont(font)       
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_42 = QtWidgets.QLabel(self.frame)
        self.label_42.setGeometry(QtCore.QRect(1030, 240, 131, 31))
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
        self.label_45.setGeometry(QtCore.QRect(1030, 190, 131, 31))
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
        self.label_46.setGeometry(QtCore.QRect(1180, 190, 91, 31))
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
        self.line.setGeometry(QtCore.QRect(10, 570, 501, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(1030, 350, 151, 41))
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
        self.layoutWidget.setGeometry(QtCore.QRect(20, 420, 221, 131))
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
        self.label_29 = QtWidgets.QLineEdit(self.layoutWidget)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.label_29)
        self.label_29.setValidator(input_validator)
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
        self.radioButton.setGeometry(QtCore.QRect(520, 360, 82, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        #self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(610, 360, 82, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(540, 40, 181, 31))
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
        self.label_3.setGeometry(QtCore.QRect(980, 50, 321, 31))
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
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(1030, 400, 256, 211))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(510, 140, 491, 171))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 40, 411, 101))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(35)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setMaxLength(12)
        self.lineEdit_5.setStyleSheet("background-color: rgb(189, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(550, 470, 120, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_41 = QtWidgets.QLabel(self.frame)
        self.label_41.setGeometry(QtCore.QRect(540, 410, 120, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(670, 410, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("color: rgb(0, 0, 255);")
        self.lineEdit_13.setDisabled(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(670, 470, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_12)
        self.lineEdit_12.setValidator(input_validator)
        self.lineEdit_12.setGeometry(QtCore.QRect(670, 530, 95, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setText("")        
        self.lineEdit_12.setObjectName("lineEdit_12")
        
        self.lineEdit_12_1 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_12_1)
        self.lineEdit_12_1.setValidator(input_validator)
        self.lineEdit_12_1.setGeometry(QtCore.QRect(770, 530, 95, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_12_1.setFont(font)
        self.lineEdit_12_1.setText("")
        self.lineEdit_12_1.setObjectName("lineEdit_12_1")
        
        self.lineEdit_12_2 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_12_2)
        self.lineEdit_12_2.setValidator(input_validator)
        self.lineEdit_12_2.setGeometry(QtCore.QRect(870, 530, 95, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_12_2.setFont(font)
        self.lineEdit_12_2.setText("")
        self.lineEdit_12_2.setObjectName("lineEdit_12_2")
        
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(560, 530, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_44 = QtWidgets.QLabel(self.frame)
        self.label_44.setGeometry(QtCore.QRect(560, 600, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.label_43 = QtWidgets.QLabel(self.frame)
        self.label_43.setGeometry(QtCore.QRect(670, 600, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_43.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(840, 660, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        
        
        
        self.pushButton_7_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7_1.setGeometry(QtCore.QRect(990, 660, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7_1.setFont(font)
        self.pushButton_7_1.setObjectName("pushButton_7_1")
        
        
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(940, 410, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(940, 470, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(940, 530, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(30, 20, 501, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(35)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(810, 360, 82, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setText("Driver-In")
        self.checkBox.setChecked(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
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
        self.label_45.hide()
        self.label_46.setText(_translate("MainWindow", "0"))
        self.label_46.hide()
        self.label_50.setText(_translate("MainWindow", "Input Data :"))
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
        self.groupBox.setTitle(_translate("MainWindow", "Vehicle No."))
        #self.lineEdit_5.setText(_translate("MainWindow", "MH-43-AW-0302"))
        self.label_17.setText(_translate("MainWindow", "Material Name:"))
        self.label_41.setText(_translate("MainWindow", "Transport Type:"))
        self.label_22.setText(_translate("MainWindow", "Phone No(s) :"))
        self.label_44.setText(_translate("MainWindow", "Rate(Rs) :"))
        self.label_43.setText(_translate("MainWindow", "0"))
        self.pushButton_8.setText(_translate("MainWindow", "View Pdf"))
        self.pushButton_8.setDisabled(True)
        self.pushButton_7_1.setText(_translate("MainWindow", "Print Slip"))
        self.pushButton_7_1.setDisabled(True)
        self.pushButton_11.setText(_translate("MainWindow", "<<"))
        self.pushButton_12.setText(_translate("MainWindow", "<<"))
        self.pushButton_13.setText(_translate("MainWindow", "<<"))
        self.pushButton_13.hide()
        self.label_48.setText(_translate("MainWindow", "Public Weighing "))
        self.pushButton_7.clicked.connect(MainWindow.close)
        self.pushButton_11.clicked.connect(self.vehicle_type)
        self.pushButton_12.clicked.connect(self.material_list_load) 
        self.listWidget.doubleClicked.connect(self.selected_party)
        self.pushButton_9.clicked.connect(self.gross_wt_onclick)
        self.pushButton_10.clicked.connect(self.tare_wt_onclick)
        
        self.pushButton_17.clicked.connect(self.call_fetch_slip_via_get)
        self.pushButton_5.clicked.connect(self.save_data)
        self.pushButton_6.clicked.connect(self.reset_fun)
        self.radioButton_2.clicked.connect(self.mannual_onclick)
        self.radioButton.clicked.connect(self.auto_onclick)
        
        self.pushButton_8.clicked.connect(self.open_PPOP_window4)
        self.pushButton_7_1.clicked.connect(self.open_PPOP_window3)
        self.lineEdit_5.textChanged.connect(self.text_change_f)
        
        self.label_35.textChanged.connect(self.first_wt_onchange)
        self.label_29.textChanged.connect(self.second_wt_onchange)
        
        if (self.radioButton.isChecked()):
                    self.weight_type="AUTO"
                    self.label_35.setDisabled(True)
                    self.label_29.setDisabled(True)
        elif (self.radioButton_2.isChecked()):
                    self.weight_type="MANUAL"
                    self.label_35.setEnabled(True)
                    self.label_29.setEnabled(True)
        
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT AUTO_FLAG FROM SERIVES_SET") 
        for x in results:            
            if(str(x[0])=='MANNUAL_AND_AUTO'):
                    self.radioButton_2.setEnabled(True)                         
            else:
                    self.radioButton_2.setDisabled(True)
        self.timer1=QtCore.QTimer()
        self.timer2=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        self.start_wt()
    
    def device_date(self):     
        self.label_2.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def first_wt_onchange(self):
        self.label_3.hide() 
        if(str(self.label_35.text()) == ""):
                self.label_35.setText("0")
        else:
                self.label_31.setText(datetime.datetime.now().strftime("%Y-%m-%d"))               
                self.label_33.setText(datetime.datetime.now().strftime("%H:%M"))
                if(self.label_39.text() =="--"):
                            self.label_3.setText("2nd Wt Type is empty.")
                            self.label_3.show()
                else:
                            self.net_wt_calc()
        
        
    def second_wt_onchange(self):
        self.label_3.hide() 
        if(str(self.label_29.text()) == ""):
                self.label_29.setText("0")
        else:
                self.label_27.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
                self.label_28.setText(datetime.datetime.now().strftime("%H:%M"))
                if(self.label_37.text() =="--"):
                            self.label_3.setText("1st Wt Type is empty.")
                            self.label_3.show()
                else:
                            self.net_wt_calc()
    
    def text_change_f(self):
        #print("insedie finct ")
        string =self.lineEdit_5.text()
        if not (string.isupper()):
               self.lineEdit_5.setText(string.upper())
               #print(string.upper())
    
    def mannual_onclick(self):
        if(self.radioButton_2.isChecked()):
                    self.weight_type="MANUAL"
                    if(self.wt_type=="FIRST"):
                            self.label_35.setEnabled(True)
                    else:       
                            self.label_29.setEnabled(True)
                    self.radioButton.setChecked(False)
        else:
                    
                    self.weight_type="AUTO"
                    self.label_35.setDisabled(True)
                    self.label_29.setDisabled(True)
                    self.radioButton.setChecked(True)
    
    def auto_onclick(self):
        if(self.radioButton_2.isChecked()):
                    self.weight_type="MANUAL"
                    if(self.wt_type=="FIRST"):
                            self.label_35.setEnabled(True)
                    else:       
                            self.label_29.setEnabled(True)
                    self.radioButton.setChecked(False)
        else:
                    
                    self.weight_type="AUTO"
                    self.label_35.setDisabled(True)
                    self.label_29.setDisabled(True)
                    self.radioButton.setChecked(True)           
    def call_fetch_slip_via_get(self):        
        self.slip_no=str(self.lineEdit_15.text())
        print("Slip No :"+str(self.slip_no))
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
            #self.lineEdit_10.setText(str(x[1]))
            #self.lineEdit_11.setText(str(x[2]))
            #self.lineEdit_9.setText(str(x[3]))
            self.lineEdit_14.setText(str(x[4]))
            self.lineEdit_12.setText("") #Phone No 
            #self.lineEdit_13.setText("") #Transport Type
            self.lineEdit_13.setText(str(x[12]))
        
            self.label_37.setText(str(x[5]))
            
            print ("first wt mode :"+str(x[5]))
            if(str(x[5]) == "GROSS"):
                self.pushButton_9.setDisabled(True)
                self.pushButton_10.setEnabled(True)
                #self.pushButton_5.setEnabled(True)
                
            if(str(x[5]) == "TARE"):
                self.pushButton_10.setDisabled(True)
                self.pushButton_9.setEnabled(True)
                #self.pushButton_5.setEnabled(True)
            
            print("First Wt date :"+str(x[7]))
            self.label_27.setText(str(x[7])[0:11])
            self.label_28.setText(str(x[7])[11:16])
            self.label_29.setText(str(x[6]))
                
            
            '''
                self.lineEdit_9.setText("Transport Name")
                self.lineEdit_10.setText("Party Name")
                self.lineEdit_11.setText("Supplier Name")
                self.lineEdit_12.setText("Phone No")
                self.lineEdit_13.setText("Transport Type")
                self.lineEdit_14.setText("Material Name")
                self.lineEdit_15.setText("search slip No")
                self.lineEdit_16.setText("totalbags")
                self.lineEdit_17.setText("avg wt per bag")
            '''
            self.vehicle_no=(str(x[10])) 
            self.lineEdit_5.setText(str(x[10]))
            self.label_40.setText(str(x[9]))
            self.label_43.setText(str(x[11]))
            self.lineEdit_13.setText(str(x[12]))
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
            self.pushButton_7_1.setEnabled(True)
            self.pushButton_8.setEnabled(True)
            
            self.wt_type=str(x[16])
            if(str(x[16]) == "SECOND"):
               self.pushButton_9.setDisabled(True)
               self.pushButton_10.setDisabled(True)
               self.pushButton_5.setDisabled(True)
            self.create_pdf()
               
            
                 
    def reset_fun(self):        
        self.lineEdit_12.setText("") #Phone No 
        self.lineEdit_13.setText("") #Transport Type
        self.lineEdit_14.setText("") #Material Name
        self.lineEdit_15.setText("") #Search Slip No
        self.lineEdit_5.setText("")
        self.listWidget.clear()    
        
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
        
        #self.label_53.setText("0")
        #self.label_49.setText("")
        self.label_40.setText("0")
        self.label_46.setText("0")
        self.label_46.hide()
        self.label_45.hide()
        self.pushButton_9.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.pushButton_5.setEnabled(True)    
    
        self.pushButton_7_1.setDisabled(True)
        self.pushButton_8.setDisabled(True)
    
        self.lineEdit_12_1.setText("") #Phone No2
        self.lineEdit_12_2.setText("") #Phone No3
    
    def material_list_load(self):
        self.listWidget.clear()
        self.listWidget.addItem("====Materail =====")
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT DISTINCT MATERIAL_NAME  FROM WEIGHT_MST where MATERIAL_NAME not in ('None','')")       
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()   
        
    def vehicle_type(self):
        self.listWidget.clear()
        self.listWidget.addItem("====Vehicle Type =====")
        connection = sqlite3.connect("wt.db")
        results=connection.execute(" SELECT VEHICLE_TYPE || '(' || RATE_RS || ')' from RATES_MST where VEHICLE_TYPE not in ('None','')")       
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()       
        
          
        
    def selected_party(self): 
        self.list_type=self.listWidget.item(0).text()
        if(self.listWidget.currentItem().text() != self.listWidget.item(0).text()):
            if(self.list_type=="====Parties ====="):
                self.lineEdit_10.setText(self.listWidget.currentItem().text())
            elif(self.list_type=="====Suppliers ====="):
                self.lineEdit_11.setText(self.listWidget.currentItem().text())  
            elif(self.list_type=="====Transports ====="):
                self.lineEdit_9.setText(self.listWidget.currentItem().text())            
            elif(self.list_type=="====Materail ====="):
                self.lineEdit_14.setText(self.listWidget.currentItem().text())
            elif(self.list_type=="====Vehicle Type ====="):
                self.lineEdit_13.setText(self.listWidget.currentItem().text())
                self.re_str = str(self.listWidget.currentItem().text())                
                self.rate= re.search('\(([^)]+)', self.re_str).group(1)
                self.label_43.setText(str(self.rate))      
            else:             
                self.lineEdit_12.setText("Invalid")
        
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
            '''
            self.ser.write(b'*S2T000.0 000.0\r\n')
            self.ser.flush()
            self.ser.write(b'*G10.00\r\n')
            self.ser.write(b'*P0050_0010\r\n')
            self.ser.write(b'*D\r\n')
            '''
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
                #print("o/p:"+str(self.line,'utf-8')) 
                if (len(self.line) > 6):
                    #print("o/p:"+str(self.line))
                    self.ser.flush()
                    self.ser.write(b'*D\r')
                    try:
                        self.xstr3=str(self.line,'utf-8')
                    except ValueError:
                         print("IO Error.")
                    cnt=int(self.xstr3.find("\x02"))
                    #print("index of \x02 :"+str(cnt))
                    cnt=cnt+2                    
                    self.xstr2=self.xstr3[cnt:(cnt+6)]
                    #print("MString:"+str(self.xstr2))                    
                    
                    self.xstr2=self.xstr2[0:6]
                    try:
                        self.xstr4=int(self.xstr2)
                    except ValueError:                        
                        print("Value Error-"+str(self.xstr2))
                        self.xstr4=0
                    #print("Modified String:"+str(self.xstr4))                    
                    self.lcdNumber.setProperty("value", str(self.xstr2))
                    
                    
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
        
    def save_data(self):        
        self.vehicle_no=str(self.lineEdit_5.text())
        print(" Length is :"+str(len(self.vehicle_no)))
        if(len(self.vehicle_no) >= 4):
            '''
                self.lineEdit_9.setText("Transport Name")
                self.lineEdit_10.setText("Party Name")
                self.lineEdit_11.setText("Supplier Name")
                self.lineEdit_12.setText("Phone No")
                self.lineEdit_13.setText("Transport Type")
                self.lineEdit_14.setText("Material Name")
                self.lineEdit_15.setText("search slip No")
                self.lineEdit_16.setText("totalbags")
                self.lineEdit_17.setText("avg wt per bag")
            '''
            #self.party_name=str(self.lineEdit_10.text())
            #self.supplier_name=str(self.lineEdit_11.text()) 
            self.materail_name=str(self.lineEdit_14.text())
            #self.transport_name=str(self.lineEdit_9.text())
            self.amount=str(self.label_43.text())
            self.first_wt_mode=self.label_37.text()
            self.first_wt_val=self.label_29.text()
            self.second_wt_mode=self.label_39.text()
            self.second_wt_val=self.label_35.text()  
            self.net_wt_val=str(self.label_40.text())
            self.rate=str(self.label_43.text())
            self.sms_phnoe_no=str(self.lineEdit_12.text())
            self.sms_phnoe_no_2=str(self.lineEdit_12_1.text())
            self.sms_phnoe_no_3=str(self.lineEdit_12_2.text())
            print("save called")
            
            self.driver_in_out="IN"
            
            if(self.checkBox.isChecked()):
                self.driver_in_out="IN"
            else:
                self.driver_in_out="OUT"
            
            
            if (self.radioButton.isChecked()):
                    self.weight_type="AUTO"
            elif (self.radioButton_2.isChecked()):
                    self.weight_type="MANUAL"
            self.serial_id=0        
            if(str(self.label_46.text())=="0"):
               connection = sqlite3.connect("wt.db")
               results=connection.execute("SELECT max(SERIAL_ID)+1 FROM WEIGHT_MST")       
               for x in results:
                   self.serial_id=str(x[0])
               connection.close()    
            else:
                self.serial_id=str(self.label_46.text())
                
        
        if(len(self.vehicle_no) >= 4):
             print("self.label_46.text :"+str(self.label_46.text()))
             if(str(self.label_46.text()) == "0"):
                if(int(self.first_wt_val) > 0):
                            connection = sqlite3.connect("wt.db")
                            with connection:                            
                                cursor = connection.cursor()       
                                #print(" First Wt Date :"+str(self.label_27.text())+" First  Wt Time:"+str(self.label_28.text()))
                                cr_date_str=str(self.label_27.text()+" "+str(self.label_28.text())+":00")
                                #print("cr_date_str:"+str(cr_date_str))
                                cr_date= datetime.datetime.strptime(cr_date_str, '%Y-%m-%d %H:%M:%S')
                                #print("cr_date:"+str(cr_date))                                
                                cursor.execute("INSERT INTO WEIGHT_MST(MATERIAL_NAME,FIRST_WEIGHT_MODE,FIRST_WEIGHT_VAL,WEIGHT_TYPE,NET_WEIGHT_VAL,VEHICLE_NO,AMOUNT,PHONE_NO_1,PHONE_NO_2,PHONE_NO_3,FIRST_WT_CRTEATED_ON,TRANSPORT_TYPE,TOTAL_BAGS,AVG_BAG_WT,DRIVER_IN_OUT) VALUES('"+self.materail_name+"','"+self.first_wt_mode+"','"+self.first_wt_val+"','"+self.weight_type+"','"+self.net_wt_val+"','"+self.vehicle_no+"','"+self.amount+"','"+str(self.lineEdit_12.text())+"','"+str(self.lineEdit_12_1.text())+"','"+str(self.lineEdit_12_2.text())+"','"+str(cr_date)+"','"+str(self.lineEdit_13.text())+"','"+str(self.tot_bags)+"','"+str(self.AVG_bag_wt)+"','"+str(self.driver_in_out)+"')")
                            connection.commit();
                            connection.close()
                            #print("Data Inserted !!!!")                            
                            self.label_3.show()                            
                            self.create_sms_str()
                            resp =""
                            if(self.sms_phnoe_no != ""):
                                    resp =  self.sendSMS('', self.sms_phnoe_no,'',self.sms_message_str)
                                    time.sleep(1)
                            
                            if(self.sms_phnoe_no_2 != ""):
                                    resp =  self.sendSMS('', self.sms_phnoe_no_2,'',self.sms_message_str)
                                    time.sleep(1)
                            
                            if(self.sms_phnoe_no_3 != ""):
                                    resp =  self.sendSMS('', self.sms_phnoe_no_3,'',self.sms_message_str)
                                    time.sleep(1)
                                    
                            self.sms_status=""
                            self.sms_error=""
                            #b'{"errors":[{"code":192,"message":"Messages can only be sent between 9am to 9pm as restricted by TRAI NCCP regulation"}],"status":"failure"}'
                            if(resp != 'ERROR'):
                                 y = None
                                 try:
                                
                                      y = json.loads(str(resp,'utf-8'))
                                      print (str(y))
                                      print (y["status"])
                                      if(y["status"]=="failure"):
                                          self.sms_status="failure"
                                          self.sms_error=str(y["errors"][0]["message"])
                                      else:    
                                          self.sms_status="success"
                                 except BaseException as e:
                                      print("IO Errors"+str(e))        
                            else:        
                                  print (resp)
                                  self.sms_status="failure"
                                  self.sms_error="Deactivated SMS OR Phone Number is empty"
                                    
                            
                            connection = sqlite3.connect("services.db")
                            with connection:                            
                                cursor = connection.cursor()
                                cursor.execute("INSERT INTO SMS_HISTORY(PHONE_NO,SMS_TYPE,STATUS,ERROR_MSG,SERIAL_ID,SMS_MSG) values('"+str(self.sms_phnoe_no)+"','CUSTOMER','"+str(self.sms_status)+"','"+str(self.sms_error)+"','"+str(self.serial_id)+"','"+str(self.sms_message_str)+"')")
                            connection.commit();
                            connection.close()
                            self.label_3.setText(" Saved Successfully.")
                            self.label_3.show() 
                            self.create_pdf()
                            self.pushButton_5.setDisabled(True)
                            self.label_46.setText(str(self.serial_id))
                            self.label_46.show()
                            self.label_45.show()
                else:
                    self.label_3.setText(" Weight should be greater than 0.")
                    self.label_3.show()

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
                                cursor.execute("UPDATE WEIGHT_MST SET SECOND_WT_MODE='"+str(self.second_wt_mode)+"', SECOND_WT_VAL='"+str(self.second_wt_val)+"', NET_WEIGHT_VAL='"+str(self.net_wt_val)+"',SECOND_WT_CREATED_ON=current_timestamp, STATUS='SECOND' , AMOUNT_2='"+str(self.amount)+"', PHONE_NO_4='"+str(self.lineEdit_12.text())+"',PHONE_NO_5='"+str(self.lineEdit_12_1.text())+"',PHONE_NO_6='"+str(self.lineEdit_12_2.text())+"',SECOND_WT_CREATED_ON='"+str(cr_date_2)+"', DRIVER_IN_OUT=DRIVER_IN_OUT||'-'||'"+str(self.driver_in_out)+"' WHERE SERIAL_ID='"+str(self.label_46.text())+"'")
                            connection.commit();
                            connection.close()
                            print("Data Updated !!!!")
                            self.label_3.setText(" Successfully Saved 2nd Wt.")
                            self.label_3.show()
                            
                            self.create_sms_str()
                            resp =""
                            if(self.sms_phnoe_no != ""):
                                    resp =  self.sendSMS('', self.sms_phnoe_no,'',self.sms_message_str)
                                    time.sleep(1)
                            
                            if(self.sms_phnoe_no_2 != ""):
                                    resp =  self.sendSMS('', self.sms_phnoe_no_2,'',self.sms_message_str)
                                    time.sleep(1)
                            
                            if(self.sms_phnoe_no_3 != ""):
                                    resp =  self.sendSMS('', self.sms_phnoe_no_3,'',self.sms_message_str)
                                    time.sleep(1)
                            
                            
                            self.sms_status=""
                            self.sms_error=""
                            #b'{"errors":[{"code":192,"message":"Messages can only be sent between 9am to 9pm as restricted by TRAI NCCP regulation"}],"status":"failure"}'
                            if(resp != 'ERROR'):
                                  y = None
                                  try:
                                      y = json.loads(str(resp,'utf-8'))
                                      print (str(y))
                                      print (y["status"])
                                      if(y["status"]=="failure"):
                                          self.sms_status="failure"
                                          self.sms_error=str(y["errors"][0]["message"])
                                      else:    
                                          self.sms_status="success"
                                  except BaseException as e:
                                      print("IO Errors"+str(e))    
                            else:        
                                  print (resp)
                                  self.sms_status="failure"
                                  self.sms_error="Phone Number is empty"                                    
                            
                            connection = sqlite3.connect("services.db")
                            with connection:                            
                                cursor = connection.cursor()
                                cursor.execute("INSERT INTO SMS_HISTORY(PHONE_NO,SMS_TYPE,STATUS,ERROR_MSG,SERIAL_ID,SMS_MSG) values('"+str(self.sms_phnoe_no)+"','CUSTOMER','"+str(self.sms_status)+"','"+str(self.sms_error)+"','"+str(self.serial_id)+"','"+str(self.sms_message_str)+"')")
                            connection.commit();
                            connection.close()
                            self.create_pdf()
                            self.pushButton_5.setDisabled(True)

                else:
                            self.label_3.setText(" 2nd Wt should be greater than 0.")
                            self.label_3.show()  
                                
        else:
            self.label_3.setText("Vehical Number is empty.")
            self.label_3.show() 
        
        if(len(self.vehicle_no) >= 4 ):
                    self.pushButton_7_1.setEnabled(True)
                    self.pushButton_8.setEnabled(True)
    
    def create_pdf(self):
        self.first_wt=""
        self.first_wt_date=""
        self.first_wr_time=""
        self.second_wt=""
        self.second_wt_date=""
        self.second_wt_time=""
        self.first_wt_mode=""
        self.second_wt_mode=""
        self.address=""
        self.company_name_font=0
        self.company_address_font=0
        self.note=""
        
        if(self.label_46.text()=="--"):
              self.serial_id=0
        self.serial_id=self.label_46.text()
        print("self.serial_id :"+str(self.serial_id))
        if (self.serial_id=="0"):
            connection = sqlite3.connect("wt.db")       
            results=connection.execute("SELECT MAX(SERIAL_ID) FROM WEIGHT_MST_VW")
            for x in results:
                 self.serial_id=str(x[0])            
            connection.close()
            
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT IFNULL(COMPANY_NAME_FONT,10),IFNULL(COMPANY_ADDRESS_FONT,10) FROM USER_RIGHT_SET")
        for x in results:
                 self.company_name_font=str(x[0])
                 self.company_address_font=str(x[1])
        connection.close()
        
        connection = sqlite3.connect("services.db")       
        results=connection.execute("SELECT PRINT_NOTE FROM DEVICE_CONF")
        for x in results:
                 self.note=str(x[0])                 
        connection.close()
        
        connection = sqlite3.connect("wt.db")          
        with connection:        
             cursor = connection.cursor()                    
             cursor.execute("UPDATE PRINTER_DATA SET SERIAL_ID='"+str(self.serial_id)+"'") 
        connection.commit();
        connection.close()   
        
        data= [['           Weight Type         ','          Date           ','      Time     ','        Weight (Kg)          ']]
        
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT SERIAL_ID,VEHICLE_NO,FIRST_WEIGHT_VAL,FIRST_WT_CRTEATED_ON,SECOND_WT_VAL,SECOND_WT_CREATED_ON,"+
                                           "NET_WEIGHT_VAL ,(AMOUNT+AMOUNT_2) as CHARGES,PARTY_NAME,SUPPLIER_NAME,FIRST_WEIGHT_MODE,SECOND_WT_MODE,MATERIAL_NAME FROM WEIGHT_MST WHERE SERIAL_ID in (SELECT SERIAL_ID from PRINTER_DATA)") 
      
               
        for x in results:
               self.first_wt=str(x[2])
               self.first_wt_date=str(x[3])
               self.first_wr_time=str(x[3])
               self.second_wt=str(x[4])
               self.second_wt_date=str(x[5])
               self.second_wt_time=str(x[5])
               self.first_wt_mode=str(x[10])
               self.second_wt_mode=str(x[11])
        connection.close()
        data.append([str(self.first_wt_mode)+" Weight",str(self.first_wt_date[0:10]),str(self.first_wt_date[11:16]),str(self.first_wt)])        
        data.append([str(self.second_wt_mode)+" Weight",str(self.second_wt_date[0:10]),str(self.second_wt_date[11:16]),str(self.second_wt)])
        data.append(["NET Weight","","",str(x[6])])
        
        
        
        c = Canvas("./reports/currentSlip-Public.pdf")
        #c.setPageSize( landscape(letter) )
        #############################
        c.setFont('Helvetica-Bold', int(self.company_name_font) )
        PAGE_HEIGHT = letter[1]
        PAGE_WIDTH = letter[0]
        
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT COMPANY_NAME,COMPANY_ADDR||'(Phone:'||CONTACT_NO||')'  FROM USER_RIGHT_SET")
        for x in results:
              c.drawString(170,810,str(str(x[0])))             
              self.address=str(str(x[1]))
        connection.close()
        
        c.setFont('Helvetica-Bold', int(self.company_address_font) )
        c.drawString(80,790,str(self.address[0:76]))
        c.drawString(150,770,str(self.address[76:200]))
        
        c.line( 0.5*inch, PAGE_HEIGHT-( 0.45*inch ), PAGE_WIDTH-( 0.5*inch ), PAGE_HEIGHT-( 0.45*inch ) )
        ###################################################
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT SERIAL_ID_DISPLY,current_timestamp as dt,PARTY_NAME,SUPPLIER_NAME,MATERIAL_NAME,TRANSPORT_NAME,"+
                                           "GROSS_WT_DATE,TARE_WT_DATE,(IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOT_AMOUNT,GROSS_WT_VAL,TARE_WT_VAL,NET_WEIGHT_VAL,VEHICLE_NO,FPRM_NO,REMARK,MANNUAL_INS_FLG,OPERATOR_NAME,DRIVER_IN_OUT,IFNULL(round(TOTAL_BAGS,2),0),IFNULL(round(AVG_BAG_WT,2),0) FROM WEIGHT_MST_VW WHERE SERIAL_ID ='"+str(self.serial_id)+"' ") 
        
        
        for x in results:
                c.setFont('Helvetica',10)
                c.drawString(50,740,"Serial ID        : "+str(x[0]))
                c.drawString(50,710,"Party Name       : "+str(x[2]))     
                c.drawString(50,680,"Material Name    : "+str(x[4]))
                c.drawString(50,650,"Driver           : "+str(x[17]))
                if(float(x[18]) > 0):
                    c.drawString(50,620,"No. Of Bags      : "+str(x[18]))
                    c.drawString(250,620,"Weight Per Bag  : "+str(x[19]))
                    
                #c.drawString(250,740,"Date : "+str(x[1]))
                c.drawString(250,740,"Vehicle No      : "+str(x[12]))    
                c.drawString(250,710,"Supplier Name.  : "+str(x[3]))
                c.drawString(250,680,"Transport Name  : "+str(x[5]))   
                
                c.drawString(250,650,"Total Amount(Rs): "+str(x[8]))
                
                
                c.drawString(50,450,"Authorised Signature and stamp   : ")
                c.drawString(50,430,str(self.note))
                #c.drawString(250,550,"Net Wt. (Kg)    : "+str(x[11]))
                #c.drawString(250,530,"Total Amount(Rs): "+str(x[8]))
                c.line(0.5*inch,420,580,420)
        
        connection.close()
        
        ##############################################
        c.setFont('Helvetica',10)        
        f = Table(data)        
        f.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black), ('FONT', (0, 0), (-1, -1), "Helvetica", 10)]))
        width = 200
        height_1 = 400
        f.wrapOn(c, width, height_1)
        x = 40
        y = 530
        f.drawOn(c, x, y)        
        ############################################
        
        c.showPage()
        c.save()  
        
                        
    
    
    def create_pdf_camera(self):
        
        self.serial_id=self.label_46.text()
        print("self.serial_id :"+str(self.serial_id))
        if (self.serial_id=="0"):
            connection = sqlite3.connect("wt.db")       
            results=connection.execute("SELECT MAX(SERIAL_ID) FROM WEIGHT_MST_VW")
            for x in results:
                 self.serial_id=str(x[0])
            
            connection.close()
        
        connection = sqlite3.connect("wt.db")          
        with connection:        
             cursor = connection.cursor()                    
             cursor.execute("UPDATE PRINTER_DATA SET SERIAL_ID='"+str(self.serial_id)+"'") 
        connection.commit();
        connection.close()     
        
        data= [[' Vehicle.No ','Gross Wt.(Kg)','Tare Wt.(Kg)','Net Wt.(Kg)','Gross Wt. Rate (Rs)','Tare Wt.Rate (Rs)']]
        
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT VEHICLE_NO,"+                                   
                                   "IFNULL(GROSS_WT_VAL,0),IFNULL(TARE_WT_VAL,0),IFNULL(NET_WEIGHT_VAL,0),GROSS_WT_RATE,TARE_WT_RATE FROM WEIGHT_MST_VW WHERE SERIAL_ID ='"+str(self.serial_id)+"'") 
               
        for x in results:
             data.append(x)             
        connection.close()  
        c = Canvas("./reports/currentSlip-Public.pdf")
        #c.setPageSize( landscape(letter) )
        #############################
        c.setFont('Helvetica', 12 )
        PAGE_HEIGHT = letter[1]
        PAGE_WIDTH = letter[0]
        
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT COMPANY_NAME,CONTACT_NO FROM USER_RIGHT_SET")
        for x in results:
              c.drawCentredString( PAGE_WIDTH/2.0, PAGE_HEIGHT-( 0.125*inch ), str(x[0])+"   ( #"+str(x[1])+" )")
        connection.close()
        c.line( 0.5*inch, PAGE_HEIGHT-( 0.35*inch ), PAGE_WIDTH-( 0.5*inch ), PAGE_HEIGHT-( 0.35*inch ) )
        ###################################################
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT SERIAL_ID_DISPLY,current_timestamp as dt,PARTY_NAME,SUPPLIER_NAME,MATERIAL_NAME,TRANSPORT_NAME,"+
                                           "GROSS_WT_DATE,TARE_WT_DATE,(IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOT_AMOUNT,GROSS_WT_VAL,TARE_WT_VAL,NET_WEIGHT_VAL,VEHICLE_NO FROM WEIGHT_MST_VW WHERE SERIAL_ID ='"+str(self.serial_id)+"' ") 
        
        
        for x in results:
                c.setFont('Helvetica',10)
                c.drawString(50,740,"Serial ID: "+str(x[0]))
                c.drawString(250,740,"Date : "+str(x[1]))
                c.drawString(450,740,"Vehical No : "+str(x[12]))       
                
                c.drawString(50,710,"Party Name: "+str(x[2]))
                c.drawString(250,710,"Transport Name : "+str(x[5]))
                
                c.drawString(50,680,"Supplier Name : "+str(x[3]))        
                c.drawString(250,680,"Material Name : "+str(x[4]))
                
                c.drawString(50,650,"Gross Wt(Kg) : "+str(x[9]))                
                c.drawString(250,650,"Gross Wt. Date : "+str(x[6]))
                
                c.drawString(50,620,"Tare Wt(Kg)   : "+str(x[10]))  
                c.drawString(250,620,"Tare Wt. Date : "+str(x[7]))
                #c.line(50,600,180,600)
                
                
                c.drawString(50,590,"Net Wt(Kg)    : "+str(x[11]))
                c.drawString(50,560,"Total Amount(Rs): "+str(x[8]))
                c.line(50,530,580,530)
        
        connection.close()
       
        c.showPage()
        c.save()                    
    
    
    def open_PPOP_window3(self):               
        self.window = QtWidgets.QMainWindow()
        self.ui=wt_37_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show() #  os.system("./job_print_recipt.sh")
        
       
    
    def open_PPOP_window4(self):        
        os.system("xpdf ./reports/currentSlip-Public.pdf")
        
        
        
    def sendSMS(self,apikey, numbers, sender, message):
        if(numbers != ""):
            fr ='None'
            connection = sqlite3.connect("wt.db")       
            results=connection.execute("SELECT SMS_ACTIVATION,SMS_API_KEY,SMS_API_URL FROM USER_RIGHT_SET")
            for x in results:
                if(str(x[0]) == "ACTIVE"):
                    apikey=str(x[1])
                    try:
                            data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'message' : message, 'sender': sender})
                            data = data.encode('utf-8')
                            #request = urllib.request.Request("https://api.textlocal.in/send/?")
                            request = urllib.request.Request(str(x[2]))
                            f = urllib.request.urlopen(request, data)
                            fr = f.read()
                    except IOError:
                        print("IO Errors") 
                    return(fr)
                
                else:
                    print(" SMS Deactivated")
                    return("ERROR")
            connection.close()  
                
                
        else:
            print("SendSMS : Invalid Number.")
            return("ERROR")
        
    def create_sms_str(self):
        self.sms_message_str="SerialId:<s_id> ,Vehical No:<v_num>, Tare Wt(Kg):<t_wt>, Gross Wt(Kg):<g_wt> , Net Wt(Kg):<n_wt> , Amount :<final_amt>"
        connection = sqlite3.connect("wt.db")
        print("SELECT SERIAL_ID ,VEHICLE_NO, GROSS_WT_VAL,TARE_WT_VAL,NET_WEIGHT_VAL,TOTAL_AMOUNT  FROM WEIGHT_MST_VW WHERE SERIAL_ID ='"+str(self.serial_id)+"'")
        results=connection.execute("SELECT SERIAL_ID ,VEHICLE_NO, GROSS_WT_VAL,TARE_WT_VAL,NET_WEIGHT_VAL,TOTAL_AMOUNT  FROM WEIGHT_MST_VW WHERE SERIAL_ID ='"+str(self.serial_id)+"'") 
        for x in results:
                self.sms_message_str=self.sms_message_str.replace("<s_id>",str(x[0]))
                self.sms_message_str=self.sms_message_str.replace("<v_num>",str(x[1]))
                self.sms_message_str=self.sms_message_str.replace("<t_wt>",str(x[2]))
                self.sms_message_str=self.sms_message_str.replace("<g_wt>",str(x[3]))
                self.sms_message_str=self.sms_message_str.replace("<n_wt>",str(x[4]))
                self.sms_message_str=self.sms_message_str.replace("<final_amt>",str(x[5]))
                print("inside self.sms_message_str :"+str(self.sms_message_str))
        #print("self.sms_message_str :"+str(self.sms_message_str))
        connection.close()    
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_32_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
