# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_31_weight_cam_2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
import re


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
#from print_popup_slip import P_POPUi_MainWindow

from PyQt5.Qt import QTableWidgetItem
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from reportlab.lib.utils import ImageReader

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

class wt_31_Ui_MainWindow(object):
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
        
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 650, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(260, 650, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(690, 650, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(380, 240, 121, 31))
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
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(380, 70, 221, 131))
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
        self.label_40.setGeometry(QtCore.QRect(520, 240, 91, 31))
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
        self.label_45 = QtWidgets.QLabel(self.frame)
        self.label_45.setGeometry(QtCore.QRect(70, 10, 61, 31))
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
        self.label_46.setGeometry(QtCore.QRect(140, 10, 91, 31))
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
        self.line.setGeometry(QtCore.QRect(90, 220, 551, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 70, 221, 131))
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
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(290, 10, 181, 31))
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
        self.label_3.setGeometry(QtCore.QRect(190, 600, 241, 31))
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
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(530, 10, 91, 31))
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
        self.label_48.setGeometry(QtCore.QRect(630, 0, 241, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(19)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(530, 330, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(530, 370, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_12.setGeometry(QtCore.QRect(190, 530, 321, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(60, 410, 120, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(60, 490, 120, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(530, 450, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setGeometry(QtCore.QRect(190, 451, 323, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(190, 330, 323, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(530, 490, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(190, 370, 321, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(60, 530, 111, 31))
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
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(530, 410, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(190, 411, 323, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_41 = QtWidgets.QLabel(self.frame)
        self.label_41.setGeometry(QtCore.QRect(60, 331, 120, 31))
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
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(530, 530, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(60, 370, 120, 31))
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
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_11.setGeometry(QtCore.QRect(190, 490, 323, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(60, 450, 120, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(630, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(630, 330, 256, 231))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.label_44 = QtWidgets.QLabel(self.frame)
        self.label_44.setGeometry(QtCore.QRect(630, 580, 81, 31))
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
        self.label_43.setGeometry(QtCore.QRect(720, 580, 91, 31))
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
        self.pushButton_8.setGeometry(QtCore.QRect(550, 650, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(420, 650, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(920, 20, 381, 681))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 1, 0, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout.addWidget(self.graphicsView_3, 2, 0, 1, 1)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout.addWidget(self.graphicsView_4, 3, 0, 1, 1)
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
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
        self.pushButton_6.setText(_translate("MainWindow", "Reset"))
        self.pushButton_7.setText(_translate("MainWindow", "Return"))
        self.label_24.setText(_translate("MainWindow", "Net Weight (Kg) :"))
        self.label_39.setText(_translate("MainWindow", "--"))
        self.label_31.setText(_translate("MainWindow", "--"))
        self.label_38.setText(_translate("MainWindow", "Second. Wt.Type :"))
        self.label_30.setText(_translate("MainWindow", "Second. Wt. Date :"))
        self.label_34.setText(_translate("MainWindow", "Second. Wt. (Kg) :"))
        self.label_32.setText(_translate("MainWindow", "Second Wt. Time :"))
        self.label_35.setText(_translate("MainWindow", "0"))
        self.label_33.setText(_translate("MainWindow", "--:-- "))
        self.label_40.setText(_translate("MainWindow", "0"))
        self.label_45.setText(_translate("MainWindow", " Slip No:"))
        self.label_46.setText(_translate("MainWindow", "0"))
        self.label_36.setText(_translate("MainWindow", "First Wt.Type :"))
        self.label_37.setText(_translate("MainWindow", "--"))
        self.label_23.setText(_translate("MainWindow", "First Wt. Date :"))
        self.label_27.setText(_translate("MainWindow", "--"))
        self.label_25.setText(_translate("MainWindow", "First Wt. Time :"))
        self.label_28.setText(_translate("MainWindow", "--:-- "))
        self.label_26.setText(_translate("MainWindow", "First Wt. (Kg) :"))
        self.label_29.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.label_3.setText(_translate("MainWindow", "Saved Successfully !"))
        self.label_3.hide()
        self.label_47.setText(_translate("MainWindow", "Vehicle No:"))
        self.label_48.setText(_translate("MainWindow", "MH43-AW-0302"))
        self.pushButton_11.setText(_translate("MainWindow", "<<"))
        self.pushButton_16.setText(_translate("MainWindow", "<<"))
        self.label_21.setText(_translate("MainWindow", "Transportl Name:"))
        self.label_16.setText(_translate("MainWindow", "Supplier Name:"))
        self.pushButton_13.setText(_translate("MainWindow", "<<"))
        self.pushButton_14.setText(_translate("MainWindow", "<<"))
        self.label_22.setText(_translate("MainWindow", "Phone No :"))
        self.pushButton_12.setText(_translate("MainWindow", "<<"))
        self.label_41.setText(_translate("MainWindow", "Transport Type:"))
        self.pushButton_15.setText(_translate("MainWindow", "<<"))
        self.label_17.setText(_translate("MainWindow", "Material Name:"))
        self.label_15.setText(_translate("MainWindow", "Party Name:"))
        self.label_20.setText(_translate("MainWindow", "Input Data :"))
        self.label_44.setText(_translate("MainWindow", "Rate(Rs) :"))
        self.label_43.setText(_translate("MainWindow", "0"))
        self.pushButton_8.setText(_translate("MainWindow", "View Print"))
        self.pushButton_8.setDisabled(True)
        self.pushButton_9.setText(_translate("MainWindow", "Print"))
        self.pushButton_7.clicked.connect(MainWindow.close)
        self.pushButton_5.clicked.connect(self.save_data)
          
        self.pushButton_11.clicked.connect(self.vehicle_type)
        self.pushButton_13.clicked.connect(self.parties_list_load)
        self.pushButton_14.clicked.connect(self.supplier_list_load)
        self.pushButton_12.clicked.connect(self.transport_list_load)
        self.pushButton_16.clicked.connect(self.material_list_load)
        self.pushButton_8.clicked.connect(self.open_PPOP_window4)
        self.pushButton_9.clicked.connect(self.open_PPOP_window3)
        
        self.listWidget.doubleClicked.connect(self.selected_party)
        self.fetch_slip_data()
        self.timer1=QtCore.QTimer()        
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
   
    
        
    def device_date(self):     
        self.label_2.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        print("Timer cam2")
     
    def close_win(self):
        self.stop_all_timers()
        self.close()        
        print("Window Closed !!!!! ")
        
    def stop_all_timers(self):
        if(self.timer1.isActive()):
              self.timer1.stop()
              print(" Timer stopeped i n close enevnt ")
        
    
    def parties_list_load(self):
        self.listWidget.clear()
        self.listWidget.addItem("====Parties =====")
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT DISTINCT PARTY_NAME FROM WEIGHT_MST")       
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()
        
        
    def supplier_list_load(self):
        self.listWidget.clear()
        self.listWidget.addItem("====Suppliers =====")
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT DISTINCT SUPPLIER_NAME FROM WEIGHT_MST")       
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()       
        
    def transport_list_load(self):
        self.listWidget.clear()
        self.listWidget.addItem("====Transports =====")
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT DISTINCT TRANSPORT_NAME FROM WEIGHT_MST")       
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()       
    
    def material_list_load(self):
        self.listWidget.clear()
        self.listWidget.addItem("====Materail =====")
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT DISTINCT MATERIAL_NAME  FROM WEIGHT_MST")       
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()
     
    def vehicle_type(self):
        self.listWidget.clear()
        self.listWidget.addItem("====Vehicle Type =====")
        connection = sqlite3.connect("wt.db")
        results=connection.execute(" SELECT VEHICLE_TYPE || '(' || RATE_RS || ')' from RATES_MST")       
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
  
    def fetch_slip_data(self):        
        self.vehicle_no=""
        connection = sqlite3.connect("wt.db")
        #print("SELECT SERIAL_ID, PARTY_NAME,SUPPLIER_NAME,TRANSPORT_NAME,MATERIAL_NAME,FIRST_WEIGHT_MODE,FIRST_WEIGHT_VAL,FIRST_WT_CRTEATED_ON ,FIRST_WT_CRTEATED_ON,NET_WEIGHT_VAL,VEHICLE_NO,AMOUNT,TRANSPORT_TYPE,SECOND_WT_MODE,SECOND_WT_VAL,SECOND_WT_CREATED_ON  FROM WEIGHT_MST WHERE SERIAL_ID='"+self.slip_no+"'")
        results=connection.execute("SELECT SERIAL_ID, PARTY_NAME,SUPPLIER_NAME,TRANSPORT_NAME,MATERIAL_NAME,FIRST_WEIGHT_MODE,FIRST_WEIGHT_VAL,FIRST_WT_CRTEATED_ON ,FIRST_WT_CRTEATED_ON,NET_WEIGHT_VAL,VEHICLE_NO,AMOUNT,TRANSPORT_TYPE,IFNULL(SECOND_WT_MODE,'--'),IFNULL(SECOND_WT_VAL,0),IFNULL(SECOND_WT_CREATED_ON,'0'),STATUS FROM WEIGHT_MST WHERE CAM_REC_TYPE='CURRENT' ")       
        for x in results:        
            self.label_46.setText(str(x[0]).zfill(4))
            self.label_46.show()
            self.label_45.show()
            self.lineEdit_10.setText(str(x[1]))
            self.lineEdit_11.setText(str(x[2]))
            self.lineEdit_9.setText(str(x[3]))
            self.lineEdit_14.setText(str(x[4]))
            self.lineEdit_13.setText(str(x[12]))
            self.label_37.setText(str(x[5]))
           
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
            self.label_48.setText(str(x[10]))
            self.label_40.setText(str(x[9]))
            
            self.label_3.hide()
            # second wt data 
            self.label_39.setText(str(x[13]))
            print ("second wt mode :"+str(x[13]))
                
            if(str(x[15]) != "0"):    
                self.label_31.setText(str(x[15])[0:11])
                self.label_33.setText(str(x[15])[11:16])
            else:    
                self.label_31.setText("00")
                self.label_33.setText("00:00")
            
            self.label_43.setText(str(x[11]))
            print("second wt:"+str(x[14]))
            self.label_35.setText(str(x[14]))
            print("Status:"+str(x[16]))
            
            
            
            
        connection.close()   
        self.net_wt_calc()
        self.upd_cam_rec_type()
            
    
    def upd_cam_rec_type(self):
        self.serial_id=str(self.label_46.text())
        connection = sqlite3.connect("wt.db")
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE WEIGHT_MST SET CAM_REC_TYPE='' WHERE SERIAL_ID='"+str(self.label_46.text())+"'")        
        connection.commit();
        connection.close()                    
        
    def save_data(self):
        self.pushButton_8.setEnabled(True)
        #self.vehicle_no=str(self.lineEdit_5.text())
        print(" Length is :"+str(len(self.vehicle_no)))
        if(len(self.vehicle_no) >= 10):
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
            self.party_name=str(self.lineEdit_10.text())
            self.supplier_name=str(self.lineEdit_11.text()) 
            self.materail_name=str(self.lineEdit_14.text())
            self.transport_name=str(self.lineEdit_9.text())
            self.amount=str(self.label_43.text())
            self.first_wt_mode=self.label_37.text()
            self.first_wt_val=self.label_29.text()
            self.second_wt_mode=self.label_39.text()
            self.second_wt_val=self.label_35.text()  
            self.net_wt_val=str(self.label_40.text())
            self.rate=str(self.label_43.text())
            self.sms_phnoe_no=str(self.lineEdit_12.text())
            print("save called")
            self.serial_id=str(self.label_46.text())
              
        if(len(self.vehicle_no) >= 10):
             print("self.label_46.text :"+str(self.label_46.text()))
             if(str(self.label_46.text()) != "0"):
                            connection = sqlite3.connect("wt.db")
                            with connection:        
                                cursor = connection.cursor()
                                #print("UPDATE WEIGHT_MST SET SECOND_WT_MODE='"+str(self.second_wt_mode)+"', SECOND_WT_VAL='"+str(self.second_wt_val)+"', NET_WEIGHT_VAL='"+str(self.net_wt_val)+"',SECOND_WT_CREATED_ON=current_timestamp, STATUS='SECOND' , AMOUNT_2='"+str(self.rate)+"', PHONE_NO_2='"+str(self.lineEdit_12.text())+"',SECOND_WT_CREATED_ON='"+cr_date_str_2+"' WHERE SERIAL_ID='"+str(self.label_46.text())+"'")
                                cursor.execute("UPDATE WEIGHT_MST SET PARTY_NAME='"+str(self.party_name)+"',SUPPLIER_NAME='"+str(self.supplier_name)+"',MATERIAL_NAME='"+str(self.materail_name)+"',TRANSPORT_NAME='"+str(self.transport_name)+"', TRANSPORT_TYPE='"+str(self.lineEdit_13.text())+"', PHONE_NO_2='"+str(self.lineEdit_12.text())+"',CAM_REC_TYPE='', AMOUNT='"+str(self.amount)+"' WHERE SERIAL_ID='"+str(self.label_46.text())+"'")
                            connection.commit();
                            connection.close()
                            print("Data Updated !!!!")
                            self.label_3.setText(" Successfuly Saved.")
                            self.label_3.show()
                            
                            self.create_sms_str()
                            resp =  self.sendSMS('', self.sms_phnoe_no,'',self.sms_message_str)
                            self.sms_status=""
                            self.sms_error=""
                            #b'{"errors":[{"code":192,"message":"Messages can only be sent between 9am to 9pm as restricted by TRAI NCCP regulation"}],"status":"failure"}'
                            if(resp != 'ERROR'):
                                  y = None
                                  try:
                                      y = json.loads(str(resp,'utf-8'))
                                      y["status"]="failure"
                                      print (str(y))
                                      print (y["status"]) 
                                      if(y["status"]=="failure"):
                                            self.sms_status="failure"
                                            self.sms_error=str(y["errors"][0]["message"]  )                                     
                                              
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
    
    def open_PPOP_window4(self):        
        #self.create_pdf() 
        os.system("xpdf ./reports/currentSlip.pdf")
        
        
     
    def open_PPOP_window3(self):     
        self.create_pdf()  
        os.system("./job_print_recipt.sh")  
        
                            
    def create_pdf(self):
        
        self.serial_id=self.label_46.text()
        print("self.serial_id :"+str(self.serial_id))
        if (self.serial_id=="0"):
            connection = sqlite3.connect("wt.db")       
            results=connection.execute("SELECT MAX(SERIAL_ID) FROM WEIGHT_MST_VW")
            for x in results:
                 self.serial_id=str(x[0])
            
            connection.close()
        
            
        
        data= [[' Vehicle.No ','Gross Wt.(Kg)','Tare Wt.(Kg)','Net Wt.(Kg)','Gross Wt. Rate (Rs)','Tare Wt.Rate (Rs)']]
        
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT VEHICLE_NO,"+                                   
                                   "IFNULL(GROSS_WT_VAL,0),IFNULL(TARE_WT_VAL,0),IFNULL(NET_WEIGHT_VAL,0),GROSS_WT_RATE,TARE_WT_RATE FROM WEIGHT_MST_VW WHERE SERIAL_ID ='"+str(self.serial_id)+"'") 
               
        for x in results:
             data.append(x)             
        connection.close()  
        c = Canvas("./reports/currentSlip.pdf")
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
        
        try:
            cam1_img = ImageReader("/home/pi/WT_2.0/camera_images/CAM1_"+str(self.serial_id)+".jpg")
        except BaseException as e:
            print("IO Errors"+str(e))
            cam1_img=None
            
        try:    
            cam2_img = ImageReader("/home/pi/WT_2.0/camera_images/CAM2_"+str(self.serial_id)+".jpg")            
        except BaseException as e:
            print("IO Errors"+str(e))
            cam2_img=None
        
        try:
            cam3_img = ImageReader("/home/pi/WT_2.0/camera_images/CAM3_"+str(self.serial_id)+".jpg")            
        except BaseException as e:
            print("IO Errors"+str(e))
            cam3_img=None
        
        try:    
            cam4_img = ImageReader("/home/pi/WT_2.0/camera_images/CAM4_"+str(self.serial_id)+".jpg")
        except BaseException as e:
            print("IO Errors"+str(e))
            cam4_img=None
            
        try:
            cam5_img = ImageReader("/home/pi/WT_2.0/camera_images/CAM5_"+str(self.serial_id)+".jpg")
        except BaseException as e:
            print("IO Errors"+str(e))
            cam5_img=None
            
        try:    
            cam6_img = ImageReader("/home/pi/WT_2.0/camera_images/CAM6_"+str(self.serial_id)+".jpg")            
        except BaseException as e:
            print("IO Errors"+str(e))
            cam6_img=None
        
        try:
            cam7_img = ImageReader("/home/pi/WT_2.0/camera_images/CAM7_"+str(self.serial_id)+".jpg")            
        except BaseException as e:
            print("IO Errors"+str(e))
            cam7_img=None
        
        try:    
            cam8_img = ImageReader("/home/pi/WT_2.0/camera_images/CAM8_"+str(self.serial_id)+".jpg")
        except BaseException as e:
            print("IO Errors"+str(e))
            cam8_img=None
        
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
        
        c.drawImage(cam1_img, 10, 320, mask='auto')
        c.drawImage(cam2_img, 320, 320, mask='auto')
        c.drawImage(cam3_img, 10, 100, mask='auto')
        c.drawImage(cam4_img, 320, 100, mask='auto')
        c.showPage()
        c.drawImage(cam5_img, 10, 500, mask='auto')
        c.drawImage(cam6_img, 320, 500, mask='auto')
        c.drawImage(cam7_img, 10, 250, mask='auto')
        c.drawImage(cam8_img, 320, 250, mask='auto')
        c.showPage()
        c.save()                    
                          
         
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
    ui = wt_31_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
