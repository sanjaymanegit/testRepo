# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TY_02_START_TEST.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


import sys
import os

from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow
from comment_popup import comment_Ui_MainWindow

#from P1_main_screen import P1_Ui_MainWindow
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


import minimalmodbus
#from minimalmodbus import BYTEORDER_LITTLE_SWAP
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
minimalmodbus.BYTEORDER_BIG= 0
minimalmodbus.BYTEORDER_LITTLE= 1


class TY_02_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 769)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 709))
        self.frame.setStyleSheet("")
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.thickness=0
        self.width=0
        self.inn_dia=0
        self.out_dia=0
        self.diameter=0
        self.cs_area=0
        self.load100_guage=0
        self.load200_guage=0
        self.load300_guage=0
        self.guage_length_mm=0
        self.goAhead="No"
        self.test_type=""
        self.test_id="1"
        self.remark=""
        
        
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(790, 220, 491, 131))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 30, 461, 91))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_20 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 0, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 0, 2, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_2)
        self.lineEdit_2.setValidator(input_validator)
        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 4, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_4)
        self.lineEdit_4.setValidator(input_validator)
        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 1, 1, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 1, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
        self.lineEdit_3.setValidator(input_validator)
        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 4, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(790, 360, 491, 121))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget1 = QtWidgets.QWidget(self.groupBox_2)
        self.widget1.setGeometry(QtCore.QRect(20, 20, 451, 91))
        self.widget1.setObjectName("widget1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_35 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_4.addWidget(self.label_35, 0, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(0, 170, 127);")
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_4.addWidget(self.label_36, 0, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_4.addWidget(self.label_37, 0, 2, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(0, 170, 127);")
        self.label_38.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_4.addWidget(self.label_38, 0, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_4.addWidget(self.label_33, 1, 0, 1, 1)
        
        
        self.label_34 = QtWidgets.QLCDNumber(self.widget1) #QtWidgets.QLabel(self.widget1)
        self.label_34.setStyleSheet("background-color: rgb(0, 0, 0);\n" "font: 10pt \"MS Sans Serif\";\n" "color: rgb(255, 0, 0);")
        self.label_34.setProperty("value", "0")
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 1, 1, 1, 1)
        
       
        
        
        
        self.label_39 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)        
        self.label_39.setObjectName("label_39")
        self.gridLayout_4.addWidget(self.label_39, 1, 2, 1, 1)
        
        
        self.label_40 = QtWidgets.QLCDNumber(self.widget1)
        self.label_40.setStyleSheet("background-color: rgb(0, 0, 0);\n" "font: 10pt \"MS Sans Serif\";\n" "color: rgb(255, 0, 0);")
        self.label_40.setProperty("value", "00.0")
        self.label_40.setObjectName("label_40")
        self.gridLayout_4.addWidget(self.label_40, 1, 3, 1, 1)
        
        
        
        
        
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 530, 1271, 161))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
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
        font.setFamily("MS Sans Serif")
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
        font.setFamily("MS Sans Serif")
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
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 9, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(790, 10, 171, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        #font.setBold(True)
        #font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 85, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(1090, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        #font.setBold(False)
        #font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(790, 70, 291, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 4, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 1, 3, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 1, 4, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 1, 1, 2)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 1, 1, 2)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 761, 491))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/start.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(100, 80))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        
        
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setText("Load Cell-High ")
        #icon1 = QtGui.QIcon()
        #icon1.addPixmap(QtGui.QPixmap("images/stop1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.radioButton_4.setIcon(icon1)
        self.radioButton_4.setIconSize(QtCore.QSize(100, 80))
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_2.addWidget(self.radioButton_4, 1, 3, 1, 1)
        
        
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget1)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 5)
        
        
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget1) #QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setText("Load Cell-Low")
        #icon2 = QtGui.QIcon()
        #icon2.addPixmap(QtGui.QPixmap("images/save.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.pushButton_3.setIcon(icon2)
        self.radioButton_3.setIconSize(QtCore.QSize(100, 80))
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_2.addWidget(self.radioButton_3, 1, 4, 1, 1)
        
        
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/show_graphs.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(100, 80))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)
       
        
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/back.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(100, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 2, 1, 1)
        
        
        
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(1130, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(1130, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(790, 170, 301, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        #font.setBold(False)        
        #font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3.setObjectName("label_3")
        
        
        self.pushButton_4_1 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_4_1.setFont(font)       
        self.pushButton_4_1.setGeometry(QtCore.QRect(1130, 495, 131, 31))        
        self.pushButton_4_1.setObjectName("pushButton_4_1")
        
        self.pushButton_4_2 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_4_2.setFont(font)       
        self.pushButton_4_2.setGeometry(QtCore.QRect(960, 495, 131, 31))        
        self.pushButton_4_2.setObjectName("pushButton_4_2")
        
        
        
        
        self.pushButton_4_3 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_4_3.setFont(font)       
        self.pushButton_4_3.setGeometry(QtCore.QRect(790, 495, 131, 31))        
        self.pushButton_4_3.setObjectName("pushButton_4_3")
        
        
        self.pushButton_4_4 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_4_4.setFont(font)       
        self.pushButton_4_4.setGeometry(QtCore.QRect(620, 495, 131, 31))        
        self.pushButton_4_4.setObjectName("pushButton_4_4")
        
        self.pushButton_4_5 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_4_5.setFont(font)        
        self.pushButton_4_5.setGeometry(QtCore.QRect(520, 495, 70, 31))        
        self.pushButton_4_5.setObjectName("pushButton_4_5")
         
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.cycle_num=0
        self.guage_ext_flg='N'
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Specimen Details"))
        self.label_20.setText(_translate("MainWindow", "Shape:"))
        self.label_27.setText(_translate("MainWindow", "Rectangle"))
        self.label_28.setText(_translate("MainWindow", "CS Area(mm2):   "))
        self.label_29.setText(_translate("MainWindow", "Thickness(mm):"))
        self.label_30.setText(_translate("MainWindow", "Width(mm):    "))
        self.label_35.setText(_translate("MainWindow", "Force at Peak (Kgf):"))
        self.label_36.setText(_translate("MainWindow", "100"))
        self.label_37.setText(_translate("MainWindow", "Length at Peak(mm):   "))
        self.label_38.setText(_translate("MainWindow", "220"))
        self.label_33.setText(_translate("MainWindow", " Force (Kgf):   "))
        #self.label_34.setText(_translate("MainWindow", "120"))
        self.label_39.setText(_translate("MainWindow", "Displacement (mm):"))
        #self.label_40.setText(_translate("MainWindow", "12.4"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CS Area (mm2)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Force at Peak \n (Kgf)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Length at Peak \n (mm)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Shape"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Guage Length \n (mm)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Tensile Strength \n (Kgf/Cm2)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Mod@100% \n (Kgf/Cm2)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Mod@200% \n (Kgf/Cm2)"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Mod@300% \n (Kgf/Cm2)"))
        
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "%E@Peak"))
        
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "%E@Break"))
        
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Cycle Id"))
        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "122"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "34"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "45"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Rectangle"))
        item = self.tableWidget.item(0, 9)
        item.setText(_translate("MainWindow", "12 Sep 2019 12:12:11 AM"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "New Test"))
        self.label_2.setText(_translate("MainWindow", datetime.datetime.now().strftime("%B  %d , %Y %I:%M ")+""))
        self.label_23.setText(_translate("MainWindow", "Batch Id:"))
        self.label_24.setText(_translate("MainWindow", "Batch_900011"))
        self.label_31.setText(_translate("MainWindow", "Job Id:"))
        self.label_32.setText(_translate("MainWindow", "Job_900011"))
        self.label_21.setText(_translate("MainWindow", "Test Id :"))
        self.label_25.setText(_translate("MainWindow", "Spec. No.:"))
        self.label_22.setText(_translate("MainWindow", "90011"))
        self.label_26.setText(_translate("MainWindow", "1"))
        self.radioButton.setText(_translate("MainWindow", "Extentiometer"))
        self.radioButton_2.setText(_translate("MainWindow", "Encoder"))
        self.label_3.setText(_translate("MainWindow", "Msg:Test Started"))
        self.pushButton_4_1.setText("View Report")
        self.pushButton_4_2.setText("Print Report")
        self.pushButton_4_2.setDisabled(True)
        self.pushButton_4_3.setText("Email Report")
        self.pushButton_4_3.setDisabled(True)
        self.pushButton_4_4.setText("Comments")
        self.pushButton_4_5.setText("Stop")
        self.pushButton_4_5.setDisabled(True)
        self.label_3.hide()
        self.sc_blank =PlotCanvas_blank(self,width=8, height=5,dpi=90)         
        self.gridLayout_2.addWidget(self.sc_blank, 0, 0, 1, 5)
        self.pushButton_5.clicked.connect(self.show_all_specimens)
       
        self.pushButton.clicked.connect(self.show_real_time)
        self.tableWidget.doubleClicked.connect(self.delete_cycle)
        #self.radioButton_3.clicked.connect(self.save_graph_data)
        #self.load_data()
        #self.radioButton_4.setDisabled(True)  ### reset
        #self.radioButton_3.setDisabled(True) ### Save
        self.lineEdit_3.textChanged.connect(self.cal_cs_area)
        self.lineEdit_4.textChanged.connect(self.cal_cs_area)
        self.pushButton_4.clicked.connect(MainWindow.close)
        self.pushButton_4_1.clicked.connect(self.open_pdf)
        self.pushButton_4_2.clicked.connect(self.print_file)
        self.pushButton_4_3.clicked.connect(self.open_email_report)
        self.pushButton_4_4.clicked.connect(self.open_comment_popup)
        self.pushButton_4_5.clicked.connect(self.manual_stop)
        
        
        
        
        #self.lineEdit_2.setText("2")
        #self.lineEdit_3.setText("3")
        #self.lineEdit_4.setText("4")  
        self.load_data()
        self.load_cell_hi=0
        self.load_cell_lo=0
        self.extiometer=0
        self.encoder=0
        self.cycle_id=0
        self.test_method=""       
                      
        self.failure_mod=""        
                      
        self.tmperature=""
        self.pushButton_4_1.setDisabled(True)
        self.test_type_for_flexural=""
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select NEW_TEST_NAME,IS_INTERNAL_ENCODER,GUAGE_EXT_FLG FROM GLOBAL_VAR")                 
        for x in results:                
                    self.test_type_for_flexural=str(x[0])
                    self.guage_ext_flg=str(x[1])
                    
                    self.label.setText(str(x[0])+" Test")
                    if(str(x[0]) == "Tensile"):
                        self.pushButton_4_1.setEnabled(True)
                    elif(str(x[0]) == "Compress"):
                        self.pushButton_4_1.setEnabled(True)
                    elif(str(x[0]) == "Tear"):
                        self.pushButton_4_1.setEnabled(True)
                    else:
                        self.pushButton_4_1.setDisabled(True)         
        connection.close()
        if(self.test_type_for_flexural=="Flexural"):
            self.flexual_objects() 
        else:
            pass
            
        try:
            self.serial_3 = serial.Serial(
                        port='/dev/ttyUSB0',
                        baudrate=19200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        xonxoff=False,
                        timeout = 0.05
                    )
            if(self.guage_ext_flg=='Y'):
                self.extiometer=1
                self.radioButton.setChecked(True)
                self.radioButton_2.setDisabled(True)
                self.radioButton_2.setChecked(False)
                self.radioButton.setEnabled(True)
            else:
                self.timer3=QtCore.QTimer()
                self.timer3.setInterval(5000)        
                self.timer3.timeout.connect(self.loadcell_encoder_status)
                self.timer3.start(1)
        except IOError:
            print("IO Errors")
    
    
    
    
    def delete_cycle(self):
        if(self.test_type_for_flexural=="Flexural"):
            row = self.tableWidget.currentRow() 
            self.cycle_id=str(self.tableWidget.item(row, 10).text())
            if(int(self.cycle_id) > 0):
                close = QMessageBox()
                close.setText("Confirm Deleteing Cycle : "+str(self.cycle_id))
                close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                close = close.exec()
                if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")              
                    with connection:        
                                    cursor = connection.cursor()                
                                    cursor.execute("DELETE FROM CYCLES_MST WHERE CYCLE_ID = '"+self.cycle_id+"'")
                                    #cursor.execute("DELETE FROM GRAPH_MST2 WHERE GRAPHI_ID in (SELECT GRAPHI_ID2 FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"')")
                                    #cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"'")
                    connection.commit();
                    connection.close()
                    self.load_data()
            else:
                pass
        elif(self.test_type_for_flexural=="Tensile"):
            row = self.tableWidget.currentRow() 
            self.cycle_id=str(self.tableWidget.item(row, 11).text())
            if(int(self.cycle_id) > 0):
                close = QMessageBox()
                close.setText("Confirm Deleteing Cycle : "+str(self.cycle_id))
                close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                close = close.exec()
                if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")              
                    with connection:        
                                    cursor = connection.cursor()                
                                    cursor.execute("DELETE FROM CYCLES_MST WHERE CYCLE_ID = '"+self.cycle_id+"'")
                                    #cursor.execute("DELETE FROM GRAPH_MST2 WHERE GRAPHI_ID in (SELECT GRAPHI_ID2 FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"')")
                                    #cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"'")
                    connection.commit();
                    connection.close()
                    self.load_data()
        elif(self.test_type_for_flexural=="Compress"):
            row = self.tableWidget.currentRow() 
            self.cycle_id=str(self.tableWidget.item(row, 7).text())
            if(int(self.cycle_id) > 0):
                close = QMessageBox()
                close.setText("Confirm Deleteing Cycle : "+str(self.cycle_id))
                close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                close = close.exec()
                if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")              
                    with connection:        
                                    cursor = connection.cursor()                
                                    cursor.execute("DELETE FROM CYCLES_MST WHERE CYCLE_ID = '"+self.cycle_id+"'")
                                    #cursor.execute("DELETE FROM GRAPH_MST2 WHERE GRAPHI_ID in (SELECT GRAPHI_ID2 FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"')")
                                    #cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"'")
                    connection.commit();
                    connection.close()
                    self.load_data()
        elif(self.test_type_for_flexural=="Tear"):
            row = self.tableWidget.currentRow() 
            self.cycle_id=str(self.tableWidget.item(row, 4).text())
            if(int(self.cycle_id) > 0):
                close = QMessageBox()
                close.setText("Confirm Deleteing Cycle : "+str(self.cycle_id))
                close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                close = close.exec()
                if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")              
                    with connection:        
                                    cursor = connection.cursor()                
                                    cursor.execute("DELETE FROM CYCLES_MST WHERE CYCLE_ID = '"+self.cycle_id+"'")
                                    #cursor.execute("DELETE FROM GRAPH_MST2 WHERE GRAPHI_ID in (SELECT GRAPHI_ID2 FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"')")
                                    #cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"'")
                    connection.commit();
                    connection.close()
                    self.load_data()     
        else:
            pass
            
    
    def on_timer3_stop(self):
        if(self.timer3.isActive()): 
           self.timer3.stop()
        else:
           pass
           
    def flexual_objects(self):
        self.label_3_3= QtWidgets.QLabel(self.frame)
        self.label_3_3.setGeometry(QtCore.QRect(1080, 490, 80, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)        
        font.setWeight(50)
        self.label_3_3.setFont(font)
        self.label_3_3.setText("Temp.(C):")
        self.label_3_3.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3_3.setObjectName("label_3_3")
        
        
        self.lineEdit_3_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_3.setGeometry(QtCore.QRect(1150, 490, 58, 31))
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3_3)
        self.lineEdit_3_3.setValidator(input_validator)        
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)        
        font.setWeight(50)
        self.lineEdit_3_3.setFont(font)
        self.lineEdit_3_3.setText("25")
        self.lineEdit_3_3.setObjectName("lineEdit_3_3")
       
        self.label_3_4= QtWidgets.QLabel(self.frame)
        self.label_3_4.setGeometry(QtCore.QRect(790, 490, 90, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)        
        font.setWeight(50)
        self.label_3_4.setFont(font)
        self.label_3_4.setText("Failure Mode:")
        self.label_3_4.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3_4.setObjectName("label_3_4")
        
        
        self.lineEdit_3_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_4.setGeometry(QtCore.QRect(890, 490, 150, 31))               
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)        
        font.setWeight(50)
        self.lineEdit_3_4.setFont(font)
        self.lineEdit_3_4.setText("Bending")
        self.lineEdit_3_4.setObjectName("lineEdit_3_4")
        
        
        
        self.label_3_5= QtWidgets.QLabel(self.frame)
        self.label_3_5.setGeometry(QtCore.QRect(470, 490, 80, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)        
        font.setWeight(50)
        self.label_3_5.setFont(font)
        self.label_3_5.setText("Test Method:")
        self.label_3_5.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3_5.setObjectName("label_3_5")
        
        
        self.lineEdit_3_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_5.setGeometry(QtCore.QRect(570, 490, 200, 31))               
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)        
        font.setWeight(50)
        self.lineEdit_3_5.setFont(font)
        self.lineEdit_3_5.setText("Test Specs.:ADS 26")
        self.lineEdit_3_5.setObjectName("lineEdit_3_5")
    
    
    
    def loadcell_encoder_status(self):         
        try:                
            self.serial_3.flush()
            self.serial_3.write(b'*D\r')
            self.line_3 = self.serial_3.readline()
            print("encoder_status:o/p:"+str(self.line_3))
        except IOError:
            print("IO Errors")    
                
        xstr3=str(self.line_3)        
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
            print("Load Cell No... :"+str(self.buff[7]))
            print("Encoder No.. :"+str(self.buff[6]))
            if(str(self.buff[6])=="2"):
                self.load_cell_hi=0
                self.load_cell_lo=1
            else:
                self.load_cell_hi=1
                self.load_cell_lo=0
                    
            if(str(self.buff[7])=="2"):
                self.extiometer=1
                self.encoder=0
            else:
                self.extiometer=0
                self.encoder=1
                
           
            
            
            if(self.load_cell_hi==1):
                self.radioButton_3.setChecked(True)
                self.radioButton_4.setDisabled(True)
                self.radioButton_4.setChecked(False)
                self.radioButton_3.setEnabled(True)
            elif(self.load_cell_lo==1):
                self.radioButton_4.setChecked(True)
                self.radioButton_3.setDisabled(True)
                self.radioButton_3.setChecked(False)
                self.radioButton_4.setEnabled(True)
         
        
            if(self.extiometer==1):
                self.radioButton.setChecked(True)
                self.radioButton_2.setDisabled(True)
                self.radioButton_2.setChecked(False)
                self.radioButton.setEnabled(True)            
            elif(self.encoder==1):
                self.radioButton_2.setChecked(True)
                self.radioButton.setDisabled(True)
                self.radioButton.setChecked(False)
                self.radioButton_2.setEnabled(True)
                                   
        
        
        
    def cal_cs_area(self):
       #print ("Shape :"+self.label_27.text()) 
       self.thickness=0
       self.width=0
       self.inn_dia=0
       self.out_dia=0
       self.diameter=0
       self.cs_area=0
              
       if(self.label_27.text() == 'Rectangle'):
           if(self.lineEdit_4.text() != ""):
               if(self.lineEdit_3.text() != ""):
                   self.thickness=float(self.lineEdit_4.text())
                   self.width=float(self.lineEdit_3.text())
                   self.cs_area=self.thickness * self.width  
                   self.lineEdit_2.setText(str(self.cs_area))
               else:
                   self.lineEdit_2.setText("0")
           else:
                   self.lineEdit_2.setText("0") 
           
       elif (self.label_27.text() == 'Cylindrical'):
          if(self.lineEdit_4.text() != ""):
               self.diameter=str(self.lineEdit_4.text())           
               self.cs_area=(float(self.diameter)*float(self.diameter)*3.14)/4 
               self.lineEdit_2.setText(str(round(self.cs_area,5)))
          else:
               self.lineEdit_2.setText("0")      
           #print("okofdg"+self.lineEdit_3.text())
       elif (self.label_27.text() == 'Pipe'):
           if(self.lineEdit_4.text() != ""):
               if(self.lineEdit_3.text() != ""):
                   self.inn_dia=float(self.lineEdit_4.text())
                   self.out_dia=float(self.lineEdit_3.text())
                   #self.cs_area=((self.inn_dia*3.14)/2)-((self.out_dia*3.14)/2)
                   self.cs_area=((self.out_dia*self.out_dia*3.14)/4)-((self.inn_dia*self.inn_dia*3.14)/4) 
                   self.lineEdit_2.setText(str(round(self.cs_area,5)))           
               else:
                   self.lineEdit_2.setText("0")
           else:
                   self.lineEdit_2.setText("0")                
        
    def show_all_specimens(self):        
        #self.pushButton_3.setDisabled(True) ### save
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)    
        self.gridLayout_2.addWidget(self.sc_data, 0,0,1,5)
        self.load_data()   
        
    
        
    def show_grid_data(self):
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 120)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 150)    
        self.tableWidget.setColumnWidth(7, 120)
        self.tableWidget.setColumnWidth(8, 50) 
        
        connection = sqlite3.connect("tyr.db")
        #print("SELECT printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_PEAK_LOAD_MM),SHAPE,GUAGE100,printf(\"%.2f\", TENSILE_STRENGTH) ,printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200),printf(\"%.2f\", MODULUS_300),printf(\"%.2f\", PRC_E_AT_PEAK),printf(\"%.2f\", PRC_E_AT_BREAK),CREATED_ON FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID")
        
        results=connection.execute("SELECT printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_PEAK_LOAD_MM),SHAPE,GUAGE100,printf(\"%.2f\", TENSILE_STRENGTH) ,printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200),printf(\"%.2f\", MODULUS_300),printf(\"%.2f\", PRC_E_AT_PEAK),printf(\"%.2f\", PRC_E_AT_BREAK),cycle_id FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID")
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()  
     
    def show_grid_data_guage_tensile(self):
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 150)    
        
        
        #self.tableWidget.setHorizontalHeaderLabels(['CS Area(mm2)', ' Force at Peak \n (Kgf) ', 'Length at Peak \n (mm)', 'Guage Length \n (mm)','Tensile Strength \n (Kgf/Cm2)','Mod@100% \n (Kgf/Cm2)','Mod@200% \n (Kgf/Cm2)','Mod@300% \n (Kgf/Cm2)','%E@Peak','%E@Break','Yeild Strength \n (Kgf/Cm2)','E@Yeild Strength \n (Cm)','Cycle Id'])        
       
        self.tableWidget.setHorizontalHeaderLabels(['CS Area(mm2)', ' Force at Peak \n (Kgf) ', 'Guage Length \n (mm)','Tensile Strength \n (Kgf/Cm2)','%E','Yeild Strength \n (Kgf/Cm2)','Cycle Id'])        
       
        connection = sqlite3.connect("tyr.db")
        #print("SELECT printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_PEAK_LOAD_MM),SHAPE,GUAGE100,printf(\"%.2f\", TENSILE_STRENGTH) ,printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200),printf(\"%.2f\", MODULUS_300),printf(\"%.2f\", PRC_E_AT_PEAK),printf(\"%.2f\", PRC_E_AT_BREAK),CREATED_ON FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID")
        
        results=connection.execute("SELECT printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD_KG),GUAGE100,printf(\"%.2f\", TENSILE_STRENGTH) ,printf(\"%.2f\", PRC_E_AT_BREAK),printf(\"%.2f\", DEF_YEILD_STRG),cycle_id FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID")
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()  
    
    
    
    
    
    
    def show_grid_data_compress(self):
        #print("inside compress list.....")
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 150)
        self.tableWidget.setColumnWidth(7, 50)
        
        self.tableWidget.setHorizontalHeaderLabels(['CS Area(mm2)', ' Peak Load (Kgf) ', 'Comp.@ Peak (mm)', 'Comp. Strength (Kgf/Cm2)','Guage Length (mm)','% Compression','Created On','Cycle Id'])        
       
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_BREAK_MM),printf(\"%.2f\", TENSILE_STRENGTH) ,printf(\"%.2f\", GUAGE100),printf(\"%.2f\", PRC_E_AT_BREAK) ,CREATED_ON,cycle_id FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID")
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()  
  
    def show_grid_data_tear(self):
        print("inside tear list.....")
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(5)
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setHorizontalHeaderLabels(['Thickness (mm)',' Peak Load (Kgf) ','Tear Strength (Kgf/Cm)','Created On','Cycle ID'])        
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 400)
        self.tableWidget.setColumnWidth(4, 50)
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT printf(\"%.2f\", THINCKNESS),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\",(round(PEAK_LOAD_KG,2)/round(THINCKNESS,2)*10)),CREATED_ON,cycle_id FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID")
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()     
    
    def show_grid_data_flexure(self):        
        #print("inside tear list.....")
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setHorizontalHeaderLabels(['Length \n (mm)','Force at Peak \n (Kgf)',' Displacement \n (mm) ','Support Span  \n(mm)','Width \n (mm)','Thickness \n (mm)','Flexural \n Strength (Kgf/cm2)','Failure \n Mode','Test  \n Method','Cycle ID'])        
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 250)
        self.tableWidget.setColumnWidth(7, 100)
        self.tableWidget.setColumnWidth(8, 100)
        self.tableWidget.setColumnWidth(9, 50)
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT printf(\"%.2f\", GUAGE100),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_BREAK_MM),(SELECT printf(\"%.2f\", NEW_TEST_MAX_LOAD) FROM GLOBAL_VAR),printf(\"%.2f\", WIDTH),printf(\"%.2f\", THINCKNESS),printf(\"%.2f\", FLEXURAL_STRENGTH_KG_CM) ,BREAK_MODE,TEST_METHOD,CYCLE_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID ")
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()
        
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)          
        
        
    
    def show_real_time(self):
        #self.pushButton_2.setEnabled(True)    ## Reset
        #self.pushButton_3.setEnabled(True)    ## Show 
        self.label_3.hide()
        #print("shape:"+str(self.shape))
        #self.sc_new =PlotCanvas_new1(self,width=5, height=4, dpi=80)
        
          
        if(self.shape=="Rectangle"):
            if(self.test_type !="Tear"):
                    self.lineEdit_3.show()
            self.thickness=str(self.lineEdit_4.text())
            self.width=str(self.lineEdit_3.text())
            self.cs_area=str(self.lineEdit_2.text())
        elif(self.shape=="Pipe"):
            if(self.test_type !="Tear"):
                    self.lineEdit_3.show()
            self.inn_dia=str(self.lineEdit_4.text())
            self.out_dia=str(self.lineEdit_3.text())
            self.cs_area=str(self.lineEdit_2.text())
        elif(self.shape=="Cylindrical"):     
            self.diameter=str(self.lineEdit_4.text())
            self.cs_area=str(self.lineEdit_2.text())
        elif(self.shape=="DirectValue"):
            self.cs_area=str(self.lineEdit_2.text())
        
        self.validation()
        if(self.goAhead=="Yes"):                
                ### Update Flexural parameters
                
            
                print("test_type :"+str(self.test_type_for_flexural))
                if(self.test_type_for_flexural == 'Flexural'):
                      self.test_method=""        
                      self.test_method=str(self.lineEdit_3_5.text())
                      self.failure_mod=""        
                      self.failure_mod=str(self.lineEdit_3_4.text())
                      self.tmperature=""        
                      self.tmperature=str(self.lineEdit_3_3.text())
                      print("Failuer maode:"+str(self.lineEdit_3_4.text()))
                      print("Failuer maodevar:"+str(self.failure_mod))
                      connection = sqlite3.connect("tyr.db")             
                      with connection:
                              cursor = connection.cursor() 
                              cursor.execute("UPDATE GLOBAL_VAR SET  BREAK_MODE='"+str(self.failure_mod)+"',TEMPERATURE='"+str(self.tmperature)+"',TEST_METHOD='"+str(self.test_method)+"' ")
                      connection.commit();
                      connection.close()
                      self.failure_mod="" 
                else:
                      pass
                if(self.test_type_for_flexural == "Tensile"):
                    if(self.guage_ext_flg=="Y"):                    
                        self.sc_new =Ext_PlotCanvas_Auto(self,width=8, height=5, dpi=90)
                        self.gridLayout_2.addWidget(self.sc_new, 0,0,1,5)
                    else:
                        self.sc_new =PlotCanvas_Auto(self,width=8, height=5, dpi=90)
                        self.gridLayout_2.addWidget(self.sc_new, 0,0,1,5)                        
                else:     
                        self.sc_new =PlotCanvas_Auto(self,width=8, height=5, dpi=90)
                        self.gridLayout_2.addWidget(self.sc_new, 0,0,1,5)
                        print("Non Tensile and  Non Guage extetiometer")
                
                connection = sqlite3.connect("tyr.db")             
                with connection:        
                      cursor = connection.cursor()            
                      cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_THICKNESS='"+str(self.thickness)+"',NEW_TEST_WIDTH="+str(self.width)+",NEW_TEST_AREA='"+str(self.cs_area)+"',NEW_TEST_DIAMETER='"+str(self.diameter)+"', NEW_TEST_INN_DIAMETER='"+str(self.inn_dia)+"', NEW_TEST_OUTER_DIAMETER='"+str(self.out_dia)+"'")                                              
               
                connection.commit();
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT COUNT(*) FROM STG_GRAPH_MST")
                rows=results.fetchall()
                connection.close()
                
                
                #self.label_4.setText(str(rows[0][0]))
                #print("count of stg records :"+str(rows[0][0]))
                if(int(rows[0][0]) > -2 ):
                    self.timer3=QtCore.QTimer()
                    self.timer3.setInterval(1000)        
                    self.timer3.timeout.connect(self.show_load_cell_val)
                    self.timer3.start(1)
                    self.pushButton_4_5.setEnabled(True)
     
    def validation(self):
        self.goAhead="No"
        if(self.shape=="Rectangle"):           
            self.thickness=str(self.lineEdit_4.text())
            self.width=str(self.lineEdit_3.text())
            self.cs_area=str(self.lineEdit_2.text())
            if(self.cs_area != "" and self.thickness !="" and self.width != ""):
                if(float(self.thickness) <= 0):
                    self.label_3.setText("Thickness should be greater than zero.")
                    self.label_3.show()
                    
                elif(float(self.width) <= 0):
                    self.label_3.setText("Paramater should be greater than zero.")
                    self.label_3.show()                    
                elif(float(self.cs_area) <= 0):
                    self.label_3.setText("CS.Area should be greater than zero.")
                    self.label_3.show()
                else:
                    self.label_3.hide()
                    self.goAhead="Yes"
            else:
                self.label_3.setText("Specimen Parameter(s) empty.")
                self.label_3.show()
        elif(self.shape=="Pipe"):
            self.lineEdit_3.show()
            self.inn_dia=str(self.lineEdit_4.text())
            self.out_dia=str(self.lineEdit_3.text())
            self.cs_area=str(self.lineEdit_2.text())
            if(self.cs_area != "" and self.inn_dia !="" and self.out_dia != ""):
                if(float(self.out_dia) <= 0):
                    self.label_3.setText("Out.Dia should be greater than zero.")
                    self.label_3.show()
                elif(float(self.inn_dia) <= 0):
                    self.label_3.setText("Inn.Dia should be greater than zero.")
                    self.label_3.show()                    
                elif(float(self.cs_area) <= 0):
                    self.label_3.setText("CS.Area should be greater than zero.")
                    self.label_3.show()
                else:
                    self.label_3.hide()
                    self.goAhead="Yes"
            else:
                self.label_3.setText("Specimen Parameter(s) empty.")
                self.label_3.show()
        elif(self.shape=="Cylindrical"):     
            self.diameter=str(self.lineEdit_4.text())
            self.cs_area=str(self.lineEdit_2.text())
            if(self.cs_area != "" and self.diameter !=""):
                if(float(self.diameter) <= 0):
                    self.label_3.setText("Diameter should be greater than zero.")
                    self.label_3.show()                                   
                elif(float(self.cs_area) <= 0):
                    self.label_3.setText("CS.Area should be greater than zero.")
                    self.label_3.show()
                else:
                    self.label_3.show()
                    self.goAhead="Yes"
            else:
                self.label_3.setText("Specimen Parameter(s) empty.")
                self.label_3.show()
            
        elif(self.shape=="DirectValue"):
            self.cs_area=str(self.lineEdit_2.text())
            if(self.cs_area != ""):
                if(float(self.cs_area) <= 0):
                    self.label_3.setText("CS.Area should be greater than zero.")
                    self.label_3.show()
                else:
                    self.label_3.show()
                    self.goAhead="Yes"
            else:
                self.label_3.setText("Specimen Parameter(s) empty.")
                self.label_3.show()
        
        
    def save_graph_data(self):                 
        ### LOAD_CYCLE_MST
        self.on_timer3_stop()
        self.sc_new.on_ani_stop()
        self.load100_guage=0
        self.load200_guage=0
        self.load300_guage=0
        self.def_flg="N"
       
        print("Last value of P :"+str(self.sc_new.p))
        #print("Length of P :"+str(len(self.sc_new.arr_p)))
        #print("Length of q :"+str(len(self.sc_new.arr_q)))
        #self.label_34.setProperty("value", "0")
        #self.label_40.setProperty("value","0")   #length
        
        if (len(self.sc_new.arr_p) > 1):
            
            #### Get Guage length
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("select IFNULL(NEW_TEST_GUAGE_MM,0),NEW_TEST_NAME,IS_METAL FROM GLOBAL_VAR")                 
            for x in results:
                self.guage_length_mm=int(x[0])
                self.test_type=str(x[1])
                self.def_flg=str(x[2])
            
            connection.close()
            #print("self.guage_length_mm:"+str(self.guage_length_mm))
                                   
            
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)):
                  if(self.test_type=="Compress" or self.test_type=="Flexural"):
                        cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM) VALUES ('"+str(float(self.sc_new.arr_p[g]))+"','"+str(self.sc_new.arr_q[g])+"')")
                  else:   
                        if(self.guage_ext_flg=="Y"):
                                cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM) VALUES ('"+str(float(self.sc_new.arr_p[g]))+"','"+str(self.sc_new.arr_q[g])+"')")
                        else:
                                cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM) VALUES ('"+str(float(self.sc_new.arr_p[g]))+"','"+str(self.sc_new.arr_q[g])+"')")
            connection.commit();
            connection.close()
            
            
            if(self.def_flg=="Y"):
                self.get_defarmetion_point()
                self.get_load_at_Defarmation()
                self.get_yeild_strength()
                
            
            for g in range(len(self.sc_new.arr_p)):
                 
                 if((float(self.guage_length_mm)*1) <= float(self.sc_new.arr_p[g])):
                        self.load100_guage=float(self.sc_new.arr_q[g])
                        break;            
            for g in range(len(self.sc_new.arr_p)):    
                 if((float(self.guage_length_mm)*2) <= float(self.sc_new.arr_p[g])):
                        self.load200_guage=float(self.sc_new.arr_q[g])
                        break;
            for g in range(len(self.sc_new.arr_p)):
                 #print(" self.sc_new.arr_p: "+str(self.sc_new.arr_p[g]))
                 #print(" self.sc_new.arr_q: "+str(self.sc_new.arr_q[g]))                 
                 if((float(self.guage_length_mm)*3) <= float(self.sc_new.arr_p[g])):
                        self.load300_guage=float(self.sc_new.arr_q[g])
                        break;
            
            #print("self.load100_guage:"+str(self.load100_guage))
            #print("self.load200_guage:"+str(self.load200_guage))
            #print("self.load300_guage:"+str(self.load300_guage))
        
        if (len(self.sc_new.arr_p) > 1):
            #self.pushButton_2.setEnabled(True)
            self.cycle_num=self.cycle_num+1
            connection = sqlite3.connect("tyr.db")              
            with connection:
                
                  cursor = connection.cursor()              
                  #print("ok1")
                  cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_THICKNESS='"+str(self.lineEdit_4.text())+"',NEW_TEST_WIDTH='"+str(self.lineEdit_3.text())+"',NEW_TEST_AREA='"+str(self.lineEdit_2.text())+"',NEW_TEST_DIAMETER='"+str(self.lineEdit_4.text())+"', NEW_TEST_INN_DIAMETER='"+str(self.lineEdit_4.text())+"', NEW_TEST_OUTER_DIAMETER='"+str(self.lineEdit_3.text())+"'")
                  #print("ok2")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM) FROM STG_GRAPH_MST)")   ### STG_PEAK_LOAD_KG
                  #print("ok3") 
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_PEAK_LOAD_MM = (SELECT X_NUM FROM STG_GRAPH_MST where Y_NUM = (SELECT MAX(Y_NUM) FROM STG_GRAPH_MST))") #STG_E_AT_PEAK_LOAD_MM
                  #print("ok4")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_TENSILE_STRENGTH=((cast(STG_PEAK_LOAD_KG as real)/IFNULL(cast(NEW_TEST_AREA as real),1)))*100") #STG_TENSILE_STRENGTH
                   
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_SET_LOW=(SELECT  BREAKING_SENCE FROM SETTING_MST) ") #STG_SET_LOW              
                  
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_BREAK_LOAD_KG=(SELECT  BREAKING_SENCE FROM SETTING_MST) ") #STG_TENSILE_STRENGTH
                  
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_BREAK_MM=(SELECT max(X_NUM) FROM STG_GRAPH_MST)") #STG_TENSILE_STRENGTH
                               
                  
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE100=NEW_TEST_GUAGE_MM")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE200=(NEW_TEST_GUAGE_MM*2)")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE300=(NEW_TEST_GUAGE_MM*3)")
                  
                  
                  
                  #print("ok5")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_LOAD100_GUAGE='"+str(self.load100_guage)+"'")
                                       
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_MODULUS_100=((cast(STG_LOAD100_GUAGE as real)/cast(NEW_TEST_AREA as real))*100)")
                  
                  
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_LOAD200_GUAGE='"+str(self.load200_guage)+"'")
                  
                  
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_MODULUS_200=((cast(STG_LOAD200_GUAGE as real)/cast(NEW_TEST_AREA as real))*100)")
                  
                  
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_LOAD300_GUAGE='"+str(self.load300_guage)+"'")              
                  
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_MODULUS_300=((cast(STG_LOAD300_GUAGE as real)/cast(NEW_TEST_AREA as real))*100)")
                 
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_MODULUS_100=IFNULL(STG_MODULUS_100,0),STG_MODULUS_200=IFNULL(STG_MODULUS_200,0),STG_MODULUS_300=IFNULL(STG_MODULUS_300,0)")
                  print("INSERT INTO CYCLES_MST(TEST_ID,SHAPE,THINCKNESS,WIDTH,CS_AREA,DIAMETER,INNER_DIAMETER,OUTER_DIAMETER,PEAK_LOAD_KG,E_AT_PEAK_LOAD_MM,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_ANY,BREAK_LOAD_KG,E_AT_BREAK_MM,SET_LOW,GUAGE100,LOAD100_GUAGE,GUAGE200,LOAD200_GUAGE,GUAGE300,LOAD300_GUAGE) SELECT TEST_ID,NEW_TEST_SPE_SHAPE,NEW_TEST_THICKNESS,NEW_TEST_WIDTH,NEW_TEST_AREA,NEW_TEST_DIAMETER, NEW_TEST_INN_DIAMETER, NEW_TEST_OUTER_DIAMETER,STG_PEAK_LOAD_KG,STG_E_AT_PEAK_LOAD_MM,STG_TENSILE_STRENGTH,STG_MODULUS_100,STG_MODULUS_200,STG_MODULUS_300,STG_MODULUS_ANY,STG_BREAK_LOAD_KG,STG_E_AT_BREAK_MM,STG_SET_LOW,STG_GUAGE100,STG_LOAD100_GUAGE,STG_GUAGE200,STG_LOAD200_GUAGE,STG_GUAGE300,STG_LOAD300_GUAGE FROM GLOBAL_VAR")
                 
                  cursor.execute("INSERT INTO CYCLES_MST(TEST_ID,SHAPE,THINCKNESS,WIDTH,CS_AREA,DIAMETER,INNER_DIAMETER,OUTER_DIAMETER,PEAK_LOAD_KG,E_AT_PEAK_LOAD_MM,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_ANY,BREAK_LOAD_KG,E_AT_BREAK_MM,SET_LOW,GUAGE100,LOAD100_GUAGE,GUAGE200,LOAD200_GUAGE,GUAGE300,LOAD300_GUAGE,BREAK_MODE,TEMPERATURE,TEST_METHOD,DEF_POINT,DEF_LOAD,DEF_YEILD_STRG,DEF_FLG) SELECT TEST_ID,NEW_TEST_SPE_SHAPE,NEW_TEST_THICKNESS,NEW_TEST_WIDTH,NEW_TEST_AREA,NEW_TEST_DIAMETER, NEW_TEST_INN_DIAMETER, NEW_TEST_OUTER_DIAMETER,STG_PEAK_LOAD_KG,STG_E_AT_PEAK_LOAD_MM,STG_TENSILE_STRENGTH,STG_MODULUS_100,STG_MODULUS_200,STG_MODULUS_300,STG_MODULUS_ANY,STG_BREAK_LOAD_KG,STG_E_AT_BREAK_MM,STG_SET_LOW,STG_GUAGE100,STG_LOAD100_GUAGE,STG_GUAGE200,STG_LOAD200_GUAGE,STG_GUAGE300,STG_LOAD300_GUAGE,BREAK_MODE,TEMPERATURE,TEST_METHOD,DEF_POINT,DEF_LOAD,DEF_YEILD_STRG,DEF_FLG FROM GLOBAL_VAR")
                  cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM) SELECT X_NUM,Y_NUM FROM STG_GRAPH_MST")
                  
              
                  cursor.execute("UPDATE CYCLES_MST SET PRC_E_AT_BREAK= (((E_AT_BREAK_MM+GUAGE100)*100)/GUAGE100)  WHERE GRAPH_ID IS NULL")
                  cursor.execute("UPDATE CYCLES_MST SET PRC_E_AT_PEAK= (((E_AT_PEAK_LOAD_MM+GUAGE100)*100)/GUAGE100)  WHERE GRAPH_ID IS NULL")
                  
                  cursor.execute("UPDATE CYCLES_MST SET PRC_E_AT_BREAK=(PRC_E_AT_BREAK-100)   WHERE GRAPH_ID IS NULL")
                  cursor.execute("UPDATE CYCLES_MST SET PRC_E_AT_PEAK=(PRC_E_AT_PEAK-100)  WHERE GRAPH_ID IS NULL")
                  cursor.execute("UPDATE CYCLES_MST SET CYCLE_NUM='"+str(self.cycle_num)+"'  WHERE GRAPH_ID IS NULL")
                  cursor.execute("UPDATE CYCLES_MST SET SPAN=(SELECT max(NEW_TEST_MAX_LOAD) FROM GLOBAL_VAR) WHERE GRAPH_ID IS NULL")
                  cursor.execute("UPDATE CYCLES_MST SET FLEXURAL_STRENGTH=(round(((3*PEAK_LOAD_KG*(SELECT NEW_TEST_MAX_LOAD FROM GLOBAL_VAR))/(2*WIDTH*THINCKNESS*THINCKNESS)),2))  WHERE GRAPH_ID IS NULL")
                  
                  cursor.execute("UPDATE CYCLES_MST SET FLEXURAL_STRENGTH_KG_CM=(round(((3*PEAK_LOAD_KG*(SELECT NEW_TEST_MAX_LOAD*0.1 FROM GLOBAL_VAR))/(2*WIDTH*0.1*THINCKNESS*0.1*THINCKNESS*0.1)),2))  WHERE GRAPH_ID IS NULL")
                  #self.kg_to_lb=float(2.20462)
                  #self.mm_to_inch=float(0.0393701)
                  cursor.execute("UPDATE CYCLES_MST SET FLEXURAL_STRENGTH_LB_INCH=((3*round((PEAK_LOAD_KG*2.20462),2)*(SELECT round((NEW_TEST_MAX_LOAD*0.0393701),2) FROM GLOBAL_VAR))/(2*round((WIDTH*0.0393701),2)*round((THINCKNESS*0.0393701),2)*round((THINCKNESS*0.0393701),2)))  WHERE GRAPH_ID IS NULL")
                  #self.kg_to_Newton=float(9.81)
                  cursor.execute("UPDATE CYCLES_MST SET FLEXURAL_STRENGTH_N_MM=(3*round((PEAK_LOAD_KG*9.81),2)*(SELECT round(NEW_TEST_MAX_LOAD,2) FROM GLOBAL_VAR))/(2*WIDTH*THINCKNESS*THINCKNESS)  WHERE GRAPH_ID IS NULL")
                  
                  #self.kgCm2_toMPA=float(0.0980665)
                  cursor.execute("UPDATE CYCLES_MST SET FLEXURAL_STRENGTH_MPA=round((FLEXURAL_STRENGTH_KG_CM*0.0980665),2) WHERE GRAPH_ID IS NULL")
                  
                  
                  
                  cursor.execute("UPDATE CYCLES_MST SET STG_TENSILE_STRENGTH_KG_CM=(SELECT ((cast(STG_PEAK_LOAD_KG as real)/IFNULL(cast(NEW_TEST_AREA as real),1)))*100 FROM GLOBAL_VAR)   WHERE GRAPH_ID IS NULL") #STG_TENSILE_STRENGTH
                  #self.kg_to_lb=float(2.20462)
                  #self.mm_to_inch=float(0.0393701)
                  cursor.execute("UPDATE CYCLES_MST SET STG_TENSILE_STRENGTH_LB_INCH=(SELECT (((cast(STG_PEAK_LOAD_KG as real)*2.20462)/(IFNULL(cast(NEW_TEST_AREA as real),1)*0.0393701*0.0393701))) FROM GLOBAL_VAR )   WHERE GRAPH_ID IS NULL") #STG_TENSILE_STRENGTH
                  
                  #self.kg_to_Newton=float(9.81)
                  cursor.execute("UPDATE CYCLES_MST SET STG_TENSILE_STRENGTH_N_MM=(SELECT ((cast(STG_PEAK_LOAD_KG as real)*9.81/IFNULL(cast(NEW_TEST_AREA as real),1))) FROM GLOBAL_VAR)    WHERE GRAPH_ID IS NULL") #STG_TENSILE_STRENGTH
                  
                  #self.kgCm2_toMPA=float(0.0980665)
                  cursor.execute("UPDATE CYCLES_MST SET STG_TENSILE_STRENGTH_MPA=round((STG_TENSILE_STRENGTH_KG_CM*0.0980665),2) WHERE GRAPH_ID IS NULL") #STG_TENSILE_STRENGTH
                
                  
                  
                  
                  
                  cursor.execute("UPDATE CYCLES_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")
                  
                  cursor.execute("UPDATE GRAPH_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")              
                  cursor.execute("UPDATE TEST_MST SET STATUS='LOADED GRAPH' WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                  cursor.execute("UPDATE TEST_MST SET TEMPERATURE = (SELECT TEMPERATURE FROM GLOBAL_VAR) WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                  
        
                  
                                                          
            connection.commit();
            connection.close()
            #self.pushButton_3.setDisabled(True) ### save
        
        self.load_data()
        
    
    def get_defarmetion_point(self):
        c=0.0
        def_point=-1.00
        def_buffer_6_prc=0.0
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT max(X_NUM) FROM STG_GRAPH_MST where X_NUM > 0 order by REC_ID ASC")
        for x in results:
            def_buffer_6_prc=float(x[0])*0.15            
        connection.close()
        
        if(float(def_buffer_6_prc) > 0):
               print("def_buffer_6_prc :"+str(def_buffer_6_prc))     
        else:
               def_buffer_6_prc=6.0
                
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT X_NUM,Y_NUM FROM STG_GRAPH_MST where X_NUM >  "+str(def_buffer_6_prc)+"  order by REC_ID ASC")
        for x in results:
            print("x_num :"+str(x[0])+"   y_num:"+str(x[1]))
            if (float(c)==0):                
                c=float(x[1])
            else:    
                if(float(x[1]) > float(c)):
                    c=float(x[1])
                    continue
                elif(float(x[1]) == float(c)):
                    def_point=float(x[0])
                    print("Break 1 Point :"+str(def_point))
                    break
                else:
                    def_point=float(x[0])
                    print("Break 2 Point :"+str(def_point))
                    break                    
        connection.close()        
        
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                cursor = connection.cursor()
                if(float(def_point) > 0):
                    cursor.execute("UPDATE GLOBAL_VAR SET DEF_POINT = '"+str(def_point)+"'")
                else:                    
                    cursor.execute("UPDATE GLOBAL_VAR SET DEF_POINT = 0")
                    
        connection.commit();
        connection.close()
    
    def get_load_at_Defarmation(self):
        def_load=0.0
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT Y_NUM FROM STG_GRAPH_MST WHERE X_NUM  in (SELECT DEF_POINT FROM GLOBAL_VAR) LIMIT 1")
        for x in results:
              def_load=str(x[0])
              
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                cursor = connection.cursor()
                if(float(def_load) > 0):
                        cursor.execute("UPDATE GLOBAL_VAR SET DEF_LOAD = '"+str(def_load)+"'")
                else:
                        cursor.execute("UPDATE GLOBAL_VAR SET DEF_LOAD = '"+str(def_load)+"'")
                        
        connection.commit();
        connection.close()
        
        
    def get_yeild_strength(self):
        connection = sqlite3.connect("tyr.db")              
        with connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE GLOBAL_VAR SET DEF_YEILD_STRG = ((DEF_LOAD)/(NEW_TEST_AREA*0.1*0.1))")
            #cursor.execute("UPDATE GLOBAL_VAR SET DEF_YEILD_STRG = '100.33'")
            
        connection.commit();
        connection.close()
        
    def manual_stop(self):
        if(self.timer3.isActive()): 
                self.sc_new.save_data_flg='Yes'
                self.sc_new.ser.write(b'*Q\r')
                if(self.sc_new.timer1.isActive()): 
                           self.sc_new.timer1.stop()
                self.timer3.stop()
        self.pushButton_4_5.setDisabled(True)
        
    
    
    
    def reset(self):
        if(self.sc_new.timer1.isActive()): 
           self.sc_new.timer1.stop()
           
        if(self.timer3.isActive()): 
           self.timer3.stop()     
        
    def show_load_cell_val(self):        
        #self.label_34.setText(str(max(self.sc_new.arr_q)))   #load
        self.label_34.setProperty("value", str(max(self.sc_new.arr_q)))
        self.label_40.setProperty("value",str(max(self.sc_new.arr_p)))   #length
        
        if(str(self.sc_new.save_data_flg) =="Yes"):
                self.reset()
                self.save_graph_data()
                self.sc_new.save_data_flg=""
                self.label_3.setText("Data Saved Successfully.")
                self.label_3.show()

    def load_data(self):        
        #self.pushButton_2.setDisabled(True) ### Stop
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT COUNT(*) FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
        rows=results.fetchall()
        connection.close()
        self.label_26.setText(str(rows[0][0]))
     
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_SPE_SHAPE,IFNULL(NEW_TEST_THICKNESS,0),IFNULL(NEW_TEST_WIDTH,0),NEW_TEST_DIAMETER,NEW_TEST_INN_DIAMETER,NEW_TEST_OUTER_DIAMETER,NEW_TEST_AREA,TEST_ID,STG_PEAK_LOAD_KG,STG_E_AT_PEAK_LOAD_MM,STG_LOAD_CELL_NO,STG_ENCO_EXT_FLG,NEW_TEST_JOB_NAME,NEW_TEST_BATCH_ID,NEW_TEST_NAME,DEF_FLG FROM GLOBAL_VAR")
        rows=results.fetchall()
        connection.close()        
        self.shape=rows[0][0]
        self.label_27.setText(self.shape) ###shap
        self.label_22.setText(str(rows[0][7])) ##test id
        self.label_32.setText(str(rows[0][12])) ##Job name
        self.label_24.setText(str(rows[0][13])) ##batch id
        
        
        if (int(self.label_26.text()) > 0):
            self.label_36.setText(str(round(rows[0][8],2)))
            self.label_38.setText(str(round(rows[0][9],2)))           
            self.label_34.setProperty("value", str(rows[0][8]))#load
            self.label_40.setProperty("value",str(rows[0][9]))   #length 
        else:
            self.label_36.setText("NA")
            self.label_38.setText("NA")
          
                   
        if(self.shape=="Rectangle"):        
           self.label_29.setText("Thickness(mm):")
           self.lineEdit_2.setText(str(rows[0][6])) 
           #print("thick ness value "+str(rows[0][1]))                    
           self.lineEdit_4.setText(str(rows[0][1]))
           self.label_30.setText("Width(mm):")
           self.lineEdit_3.setText(str(rows[0][2]))
           self.label_28.show()
                     
           #print("thick ness value "+str(rows[0][1]))                                
        elif(self.shape=="Cylindrical"):           
           self.label_28.show() 
           self.lineEdit_2.setText(str(rows[0][6]))
           self.label_29.setText("Diameter(mm):")     
           self.lineEdit_4.setText(str(rows[0][3]))
           self.label_30.hide()
           self.lineEdit_3.hide()
                 
        elif(self.shape=="Pipe"):
            
           self.label_29.setText("Inn.Dia(mm):")           
           self.lineEdit_4.setText(str(rows[0][4]))
           self.label_30.setText("Out.Dia(mm):")
           self.lineEdit_3.setText(str(rows[0][5]))
           self.label_28.show()
           self.lineEdit_2.setText(str(rows[0][6]))
           
        elif(self.shape=="DirectValue"):              
           self.label_28.show()     
           self.lineEdit_2.setText(str(rows[0][6]))
           self.label_29.hide()
           self.lineEdit_3.hide()
           self.label_30.hide()
           self.lineEdit_4.hide()            
        
        if(str(rows[0][14])=="Compress"):
            self.show_grid_data_compress()            
        elif(str(rows[0][14])=="Tear"):
            self.show_grid_data_tear()
            self.test_type="Tear"
            self.label_28.hide()
            '''
            self.lineEdit_4.hide()
            '''
            self.label_30.hide()           
            self.lineEdit_3.hide()
            self.lineEdit_2.hide()
            
        elif(str(rows[0][14])=="Flexural"):            
            self.show_grid_data_flexure()
            
        else:
            if(str(rows[0][15])=="Y"):
                 self.show_grid_data_guage_tensile()
            else:
                 self.show_grid_data()
            self.label_28.show()
            #self.label_30.show()
            #self.lineEdit_3.show()
            self.lineEdit_2.show()
        self.radioButton_4.setChecked(True)
 
    
    def create_pdf_tensile(self):
        self.remark=""
        self.unit_typex="Kg/Cm"
        if (self.shape=="Rectangle"):
            
            if(self.unit_typex == "Kg/Cm"):            
                    data= [['Spec. \n No.', 'Thickness \n (cm)', 'Width \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n']]
                    #data= [['Spec. \n No.', 'Thickness \n (mm)', 'Width \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]
          
            connection = sqlite3.connect("tyr.db")
            #print("SELECT row_number() OVER (ORDER BY CYCLE_ID) ,printf(\"%.2f\", THINCKNESS*0.1),printf(\"%.2f\", WIDTH*0.1) ,printf(\"%.4f\", CS_AREA*0.1*0.1),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_BREAK_MM*0.1),printf(\"%.2f\", PRC_E_AT_PEAK),printf(\"%.2f\", E_AT_BREAK_MM*0.1),printf(\"%.2f\", PRC_E_AT_BREAK)  FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
           
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", THINCKNESS*0.1),printf(\"%.2f\", WIDTH*0.1) ,printf(\"%.4f\", CS_AREA*0.1*0.1),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_PEAK_LOAD_MM*0.1),printf(\"%.2f\", PRC_E_AT_PEAK),printf(\"%.2f\", E_AT_BREAK_MM*0.1),printf(\"%.2f\", PRC_E_AT_BREAK)  FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")            
            results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(THINCKNESS*0.1)),printf(\"%.2f\", avg(WIDTH*0.1)) ,printf(\"%.4f\", avg(CS_AREA*0.1*0.1)),printf(\"%.2f\", avg(PEAK_LOAD_KG)),printf(\"%.2f\", avg(E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", avg(PRC_E_AT_PEAK)),printf(\"%.2f\", avg(E_AT_BREAK_MM*0.1)),printf(\"%.2f\", avg(PRC_E_AT_BREAK))  FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1")
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(THINCKNESS*0.1)),printf(\"%.2f\", max(WIDTH*0.1)) ,printf(\"%.4f\", max(CS_AREA*0.1*0.1)),printf(\"%.2f\", max(PEAK_LOAD_KG)),printf(\"%.2f\", max(E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", max(PRC_E_AT_PEAK)),printf(\"%.2f\", max(E_AT_BREAK_MM*0.1)),printf(\"%.2f\", max(PRC_E_AT_BREAK))  FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1")
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(THINCKNESS*0.1)),printf(\"%.2f\", min(WIDTH*0.1)) ,printf(\"%.4f\", min(CS_AREA*0.1*0.1)),printf(\"%.2f\", min(PEAK_LOAD_KG)),printf(\"%.2f\", min(E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", min(PRC_E_AT_PEAK)),printf(\"%.2f\", min(E_AT_BREAK_MM*0.1)),printf(\"%.2f\", min(PRC_E_AT_BREAK))  FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1")
            for x in results:
                data.append(x)
            connection.close()
                    
        elif (self.shape=="Cylindrical"):
            if(self.unit_typex == "Kg/Cm"):    
                data= [['Spe. \n No.', 'Diameter \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n']]
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", A.DIAMETER*0.1),printf(\"%.4f\", A.CS_AREA*0.1*0.1),printf(\"%.2f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM*0.1),printf(\"%.2f\", A.PRC_E_AT_PEAK),printf(\"%.2f\", A.E_AT_BREAK_MM*0.1),printf(\"%.2f\", A.PRC_E_AT_BREAK) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(A.DIAMETER*0.1)),printf(\"%.4f\", avg(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg(A.E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", avg(A.PRC_E_AT_PEAK)),printf(\"%.2f\", avg(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", avg(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(A.DIAMETER*0.1)),printf(\"%.4f\", max(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max(A.E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", max(A.PRC_E_AT_PEAK)),printf(\"%.2f\", max(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", max(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(A.DIAMETER*0.1)),printf(\"%.4f\", min(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\", min(A.E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", min(A.PRC_E_AT_PEAK)),printf(\"%.2f\", min(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", min(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
        elif (self.shape=="Pipe"):            
            if(self.unit_typex == "Kg/Cm"):                
                data= [['Spec. \n No.', 'Inn.Dia \n (cm)', 'Out. Dia \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n']]
            
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", A.INNER_DIAMETER*0.1),printf(\"%.2f\", A.OUTER_DIAMETER*0.1),printf(\"%.4f\", A.CS_AREA*0.1*0.1),printf(\"%.2f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM*0.1), printf(\"%.2f\", A.PRC_E_AT_PEAK),printf(\"%.2f\", A.E_AT_BREAK_MM*0.1),printf(\"%.2f\", A.PRC_E_AT_BREAK) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(A.INNER_DIAMETER*0.1)),printf(\"%.2f\", avg(A.OUTER_DIAMETER*0.1)),printf(\"%.4f\", avg(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg(A.E_AT_PEAK_LOAD_MM*0.1)), printf(\"%.2f\", avg(A.PRC_E_AT_PEAK)),printf(\"%.2f\", avg(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", avg(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(A.INNER_DIAMETER*0.1)),printf(\"%.2f\", max(A.OUTER_DIAMETER*0.1)),printf(\"%.4f\", max(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max(A.E_AT_PEAK_LOAD_MM*0.1)), printf(\"%.2f\", max(A.PRC_E_AT_PEAK)),printf(\"%.2f\", max(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", max(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(A.INNER_DIAMETER*0.1)),printf(\"%.2f\", min(A.OUTER_DIAMETER*0.1)),printf(\"%.4f\", min(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\", min(A.E_AT_PEAK_LOAD_MM*0.1)), printf(\"%.2f\", min(A.PRC_E_AT_PEAK)),printf(\"%.2f\", min(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", min(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close() 
        
                       
            
        elif (self.shape=="DirectValue"):
            if(self.unit_typex == "Kg/Cm"):    
                data= [['Spec.\n No.', 'CS.Area \n (cm)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n']]
            elif(self.unit_typex == "Lb/Inch"):
                data= [['Spec.\n No.', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak \n','E@Break \n (Inch)','%E@Break \n']]
            elif(self.unit_typex == "Newton/Mm"):
                data= [['Spec.\n No.', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]
            else:                
                data= [['Spec.\n No.', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']] 
                
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.4f\", A.CS_AREA*0.1*0.1),printf(\"%.2f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM*0.1),printf(\"%.2f\", A.PRC_E_AT_PEAK),printf(\"%.2f\", A.E_AT_BREAK_MM*0.1),printf(\"%.2f\", A.PRC_E_AT_BREAK) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'AVG',printf(\"%.4f\",avg(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg(A.E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", avg(A.PRC_E_AT_PEAK)),printf(\"%.2f\", avg(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", avg(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MAX',printf(\"%.4f\",max(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max(A.E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", max(A.PRC_E_AT_PEAK)),printf(\"%.2f\", max(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", max(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MIN',printf(\"%.4f\",min(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\", min(A.E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", min(A.PRC_E_AT_PEAK)),printf(\"%.2f\", min(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", min(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
        
                       
                       
        else:
           data= [['Spec. \n No.', 'Thickness (mm)', 'Width (mm)', 'CS.Area (mm2)','Peak Load (kgf)' ,'% E@Peak \n','Break Load (Kg)','E@Break (mm)','%E@Break \n']]
          
           connection = sqlite3.connect("tyr.db")
           results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,A.THICKNESS,A.WIDTH,printf(\"%.4f\", A.CS_AREA),A.PEAK_LOAD,A.E_PAEK_LOAD,round(A.PREC_E_AT_PEAK,2),round(A.E_BREAK_LOAD,2),round(A.PREC_E_AT_BREAK,2) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
           for x in results:
                data.append(x)
           connection.close()  
 
           connection = sqlite3.connect("tyr.db")
           results=connection.execute("SELECT TYPE_STR,round(THICKNESS,2),round(WIDTH,2),printf(\"%.4f\", CS_AREA),PEAK_LOAD,round(E_PAEK_LOAD,2),PREC_E_AT_BREAK FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
           for x in results:
               data.append(x)
           connection.close()            

           
           
        if(self.unit_typex == "Kg/Cm"):
            data2= [ ['Spec. \n No', 'TensileStrength \n (Kgf/Cm2)', 'Mod@100% \n (Kgf/Cm2)', 'Mod@200% \n (Kgf/Cm2)', 'Mod@300% \n (Kgf/Cm2)']]
        
                  
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select CYCLE_NUM,printf(\"%.2f\", A.TENSILE_STRENGTH),printf(\"%.2f\", A.MODULUS_100),printf(\"%.2f\", A.MODULUS_200) ,printf(\"%.2f\", A.MODULUS_300)  FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
            data2.append(x)
        connection.close()  
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select 'AVG' as SPECIMEN_NUM,printf(\"%.2f\", avg(A.TENSILE_STRENGTH)),printf(\"%.2f\", avg(A.MODULUS_100)),printf(\"%.2f\", avg(A.MODULUS_200)) ,printf(\"%.2f\", avg(A.MODULUS_300))  FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1") 
        for x in results:
            data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select 'MAX' as SPECIMEN_NUM,printf(\"%.2f\", max(A.TENSILE_STRENGTH)),printf(\"%.2f\", max(A.MODULUS_100)),printf(\"%.2f\", max(A.MODULUS_200)) ,printf(\"%.2f\", max(A.MODULUS_300))  FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1") 
        for x in results:
            data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select 'MIN' as SPECIMEN_NUM,printf(\"%.2f\", min(A.TENSILE_STRENGTH)),printf(\"%.2f\", min(A.MODULUS_100)),printf(\"%.2f\", min(A.MODULUS_200)) ,printf(\"%.2f\", min(A.MODULUS_300))  FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1") 
        for x in results:
            data2.append(x)
        connection.close() 
        
        
        y=300
        Elements=[]
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime'),A.COMMENTS   FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Specmen Shape:",str(x[9])],["Test Type:",str(x[3]),"Specmen Specs:",str(x[0])],["Party Name :",str(x[7]),"Motor Speed :",str(x[5])],["Guage Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", " ","",""]]
            self.remark=str(x[12]) 
        connection.close() 
        
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select COMPANY_NAME,ADDRESS1 from SETTING_MST ") 
        for x in results:            
            Title = Paragraph(str(x[0]), styles["Title"])
            #Title2 = Paragraph(str(x[1]), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        blank=Paragraph("                                                                                          ", styles["Normal"])
        #comments = Paragraph("Remark : ______________________________________________________________________________", styles["Normal"])
        if(str(self.remark) == ""):
                comments = Paragraph("    Remark : ______________________________________________________________________________", styles["Normal"])
        else:
                comments = Paragraph("    Remark : "+str(self.remark), styles["Normal"])
        footer_2= Paragraph("Authorised and Signed By : _________________.", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
       
        
        f1=Table(data)
        f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
        #
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
        #self.show_all_specimens()
        report_gr_img="last_graph_kg_cm.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4* inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f1,Spacer(1,12),Spacer(1,12),f2,Spacer(1,12),blank,comments,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        '''
        doc = SimpleDocTemplate('./reports/Reportxxx.pdf', pagesize=A4, rightMargin=10,
                                leftMargin=40,
                                topMargin=30,
                                bottomMargin=30,)
        '''
        doc = SimpleDocTemplate('./reports/test_report.pdf', pagesize=A4,rightMargin=20,
                                leftMargin=30,
                                topMargin=10,
                                bottomMargin=10)
        doc.build(Elements)
        #print("Done")
       
    def create_pdf_compress(self):        
#        connection = sqlite3.connect("tyr.db")
#        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
#        for x in results:
#            self.graph_typex=x[0]
#            self.unit_typex=x[1]
#        connection.close()
        self.unit_typex="Kg/Cm"
        self.remark=""
        if(self.unit_typex == "Kg/Cm"):
            data2= [ ['Spec. \n No', 'CS Area \n (cm2)', 'Force at Peak\n (Kgf)', 'Compression \n (cm)', 'Compressive Strength \n (Kgf/Cm2)',' % Compression \n']]
        else:
            data2= [ ['Spec. \n No', 'CS Area \n (mm2)', 'Force at Peak\n (Kg)', 'Compression \n (mm)', 'Compressive Strength \n (MPA)',' % Compression \n']]
          
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT CYCLE_NUM,printf(\"%.4f\", A.CS_AREA*0.1*0.1),printf(\"%.2f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.E_AT_BREAK_MM*0.1),printf(\"%.2f\", A.TENSILE_STRENGTH),printf(\"%.2f\", A.PRC_E_AT_BREAK) FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'AVG',printf(\"%.4f\", avg(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", avg(A.TENSILE_STRENGTH)),printf(\"%.2f\", avg(A.PRC_E_AT_BREAK)) FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MAX',printf(\"%.4f\", max(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", max(A.TENSILE_STRENGTH)),printf(\"%.2f\", max(A.PRC_E_AT_BREAK)) FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MIN',printf(\"%.4f\", min(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\", min(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", min(A.TENSILE_STRENGTH)),printf(\"%.2f\", min(A.PRC_E_AT_BREAK)) FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        
        y=300
        Elements=[]
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime'),A.COMMENTS  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
        
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Specmen Shape:",str(x[9])],["Test Type:",str(x[3]),"Specmen Specs:",str(x[0])],["Party Name :",str(x[7]),"Motor Speed :",str(x[5])],["Guage Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", "","",""]]
            self.remark=str(x[12])
        
        connection.close() 
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select COMPANY_NAME,ADDRESS1 from SETTING_MST ") 
        for x in results:            
            Title = Paragraph(str(x[0]), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        blank=Paragraph("                                                                                          ", styles["Normal"])
        #comments = Paragraph("    Remark : ______________________________________________________________________________", styles["Normal"])
        if(str(self.remark) == ""):
                comments = Paragraph("    Remark : ______________________________________________________________________________", styles["Normal"])
        else:
                comments = Paragraph("    Remark : "+str(self.remark), styles["Normal"])
        footer_2= Paragraph("     Authorised and Signed By : _________________.", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
        #f1=Table(data)
        #f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
        
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
         
        report_gr_img="last_graph_kg_cm.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,blank,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/test_report.pdf', rightMargin=10,
                                leftMargin=20,
                                topMargin=20,
                                bottomMargin=30,)
        doc.build(Elements)
    
    def create_pdf_tear(self):
        self.remark=""
       
        self.unit_typex="Kg/Cm"
        if(self.unit_typex == "Kg/Cm"):
            data2= [ ['Spec. \n No', 'Thickness \n (cm)', 'Force at Peak\n (Kgf)', 'Tear Strength \n (Kgf/cm)']]
                 
        else:
            data2= [ ['Spec. \n No', 'Thickness \n (mm)', 'Force at Peak\n (Kg)', 'Tear Strength \n (Kg/cm)']]
          
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", A.THINCKNESS*0.1),printf(\"%.2f\", A.PEAK_LOAD_KG),printf(\"%.2f\",(round(A.PEAK_LOAD_KG,2)/round(A.THINCKNESS,2)*10)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(A.THINCKNESS*0.1)),printf(\"%.2f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg((round(A.PEAK_LOAD_KG,2)/round(A.THINCKNESS,2)*10))) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(A.THINCKNESS*0.1)),printf(\"%.2f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max((round(A.PEAK_LOAD_KG,2)/round(A.THINCKNESS,2)*10))) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(A.THINCKNESS*0.1)),printf(\"%.2f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\", min((round(A.PEAK_LOAD_KG,2)/round(A.THINCKNESS,2)*10))) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        
        
        y=300
        Elements=[]
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime'),A.COMMENTS  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Specmen Shape:",str(x[9])],["Test Type:",str(x[3]),"Specmen Specs:",str(x[0])],["Party Name :",str(x[7]),"Motor Speed :",str(x[5])],["Guage Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", "","",""]]
            self.remark=str(x[12])
        
        connection.close() 
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select COMPANY_NAME,ADDRESS1 from SETTING_MST ") 
        for x in results:            
            Title = Paragraph(str(x[0]), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        blank=Paragraph("                                                                                          ", styles["Normal"])
        #comments = Paragraph("    Remark : ______________________________________________________________________________", styles["Normal"])
        
        if(str(self.remark) == ""):
                comments = Paragraph("    Remark : ______________________________________________________________________________", styles["Normal"])
        else:
                comments = Paragraph("    Remark : "+str(self.remark), styles["Normal"])
        footer_2= Paragraph("     Authorised and Signed By : _________________.", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
        
        #f1=Table(data)
        #f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
        
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
         
        report_gr_img="last_graph_kg_cm.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,blank,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/test_report.pdf', rightMargin=10,
                                leftMargin=20,
                                topMargin=20,
                                bottomMargin=30,)
        doc.build(Elements)
        
    def open_pdf(self):
        self.sc_data =Kg_Cm_PlotCanvas(self,width=8, height=5,dpi=90) 
        self.pushButton_4_2.setEnabled(True)
        self.pushButton_4_3.setEnabled(True)
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select NEW_TEST_NAME,IS_METAL FROM GLOBAL_VAR")                 
        for x in results:
                    if(str(x[0]) == "Tensile"):
                        if(str(x[1]) == "Y"):
                             self.create_pdf_guage_tensile()
                        else:
                             self.create_pdf_tensile()
                    elif(str(x[0]) == "Compress"):
                        self.create_pdf_compress()
                    elif(str(x[0]) == "Tear"):
                        self.create_pdf_tear()                    
                    else:
                        print("View PDF is not available")
                        
                    
        connection.close()
        
        
        
        
        os.system("xpdf ./reports/test_report.pdf")        
        #os.system("cp ./reports/Reportxxx.pdf /media/pi/003B-E2B4")
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                os.system("cp ./reports/test_report.pdf /media/usb/Report_of_test_"+str(self.test_id)+".pdf")
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
    
    def print_file(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POP_TEST_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_email_report(self):
        #self.test_id=(self.tableWidget.item(row, 1).text() )
        print(" test_id :"+str(self.test_id))  
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("update global_var set EMAIL_TEST_ID=TEST_ID")                 
        connection.commit()
        connection.close()
            
        self.window = QtWidgets.QMainWindow()
        self.ui=popup_email_test_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def open_comment_popup(self):
        
        #print(" test_id :"+str(self.test_id))  
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                    cursor = connection.cursor()                
                    cursor.execute("update global_var set EMAIL_TEST_ID=TEST_ID")                 
        connection.commit()
        connection.close()
            
        self.window = QtWidgets.QMainWindow()
        self.ui=comment_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
          
        
  
  
    
    def create_pdf_guage_tensile(self):        
        self.comments=""
        self.unit_typex="Kg/Cm"
        if (self.shape=="Rectangle"):
            
            if(self.unit_typex == "Kg/Cm"):            
                    data= [['Spec. \n No.', 'Thickness \n (cm)', 'Width \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)' ,'%E \n','Yeild \n Strength \n (Kgf/cm2)']]
                    #data= [['Spec. \n No.', 'Thickness \n (mm)', 'Width \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]
          
            connection = sqlite3.connect("tyr.db")
            #print("SELECT row_number() OVER (ORDER BY CYCLE_ID) ,printf(\"%.2f\", THINCKNESS*0.1),printf(\"%.2f\", WIDTH*0.1) ,printf(\"%.4f\", CS_AREA*0.1*0.1),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_BREAK_MM*0.1),printf(\"%.2f\", PRC_E_AT_PEAK),printf(\"%.2f\", E_AT_BREAK_MM*0.1),printf(\"%.2f\", PRC_E_AT_BREAK)  FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
           
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", THINCKNESS*0.1),printf(\"%.2f\", WIDTH*0.1) ,printf(\"%.4f\", CS_AREA*0.1*0.1),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", PRC_E_AT_BREAK),printf(\"%.2f\", DEF_YEILD_STRG)   FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")            
            results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(THINCKNESS*0.1)),printf(\"%.2f\", avg(WIDTH*0.1)) ,printf(\"%.4f\", avg(CS_AREA*0.1*0.1)),printf(\"%.2f\", avg(PEAK_LOAD_KG)),printf(\"%.2f\", avg(PRC_E_AT_BREAK)),printf(\"%.2f\", avg(DEF_YEILD_STRG))  FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1")
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(THINCKNESS*0.1)),printf(\"%.2f\", max(WIDTH*0.1)) ,printf(\"%.4f\", max(CS_AREA*0.1*0.1)),printf(\"%.2f\", max(PEAK_LOAD_KG)),printf(\"%.2f\", max(PRC_E_AT_BREAK)),printf(\"%.2f\", max(DEF_YEILD_STRG))  FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1")
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(THINCKNESS*0.1)),printf(\"%.2f\", min(WIDTH*0.1)) ,printf(\"%.4f\", min(CS_AREA*0.1*0.1)),printf(\"%.2f\", min(PEAK_LOAD_KG)),printf(\"%.2f\", min(PRC_E_AT_BREAK)),printf(\"%.2f\", min(DEF_YEILD_STRG))  FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1")
            for x in results:
                data.append(x)
            connection.close()
                    
        elif (self.shape=="Cylindrical"):
            if(self.unit_typex == "Kg/Cm"):    
                data= [['Spe. \n No.', 'Diameter \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)','%E \n']]
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", A.DIAMETER*0.1),printf(\"%.4f\", A.CS_AREA*0.1*0.1),printf(\"%.2f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.PRC_E_AT_BREAK) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(A.DIAMETER*0.1)),printf(\"%.4f\", avg(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(A.DIAMETER*0.1)),printf(\"%.4f\", max(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max(A.E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", max(A.PRC_E_AT_PEAK)),printf(\"%.2f\", max(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", max(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(A.DIAMETER*0.1)),printf(\"%.4f\", min(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\", min(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
        elif (self.shape=="Pipe"):            
            if(self.unit_typex == "Kg/Cm"):                
                data= [['Spec. \n No.', 'Inn.Dia \n (cm)', 'Out. Dia \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)' ,'%E@Break \n']]
            
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", A.INNER_DIAMETER*0.1),printf(\"%.2f\", A.OUTER_DIAMETER*0.1),printf(\"%.4f\", A.CS_AREA*0.1*0.1),printf(\"%.2f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM*0.1), printf(\"%.2f\", A.PRC_E_AT_PEAK),printf(\"%.2f\", A.E_AT_BREAK_MM*0.1),printf(\"%.2f\", A.PRC_E_AT_BREAK) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(A.INNER_DIAMETER*0.1)),printf(\"%.2f\", avg(A.OUTER_DIAMETER*0.1)),printf(\"%.4f\", avg(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(A.INNER_DIAMETER*0.1)),printf(\"%.2f\", max(A.OUTER_DIAMETER*0.1)),printf(\"%.4f\", max(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(A.INNER_DIAMETER*0.1)),printf(\"%.2f\", min(A.OUTER_DIAMETER*0.1)),printf(\"%.4f\", min(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", min(A.PEAK_LOAD_KG)), printf(\"%.2f\", min(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close() 
        
        elif (self.shape=="DirectValue"):
            if(self.unit_typex == "Kg/Cm"):    
                data= [['Spec.\n No.', 'CS.Area \n (cm)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n']]
            elif(self.unit_typex == "Lb/Inch"):
                data= [['Spec.\n No.', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak \n','E@Break \n (Inch)','%E@Break \n']]
            elif(self.unit_typex == "Newton/Mm"):
                data= [['Spec.\n No.', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]
            else:                
                data= [['Spec.\n No.', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']] 
                
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.4f\", A.CS_AREA*0.1*0.1),printf(\"%.2f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM*0.1),printf(\"%.2f\", A.PRC_E_AT_PEAK),printf(\"%.2f\", A.E_AT_BREAK_MM*0.1),printf(\"%.2f\", A.PRC_E_AT_BREAK) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'AVG',printf(\"%.4f\",avg(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg(A.E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", avg(A.PRC_E_AT_PEAK)),printf(\"%.2f\", avg(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", avg(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MAX',printf(\"%.4f\",max(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max(A.E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", max(A.PRC_E_AT_PEAK)),printf(\"%.2f\", max(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", max(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT 'MIN',printf(\"%.4f\",min(A.CS_AREA*0.1*0.1)),printf(\"%.2f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\", min(A.E_AT_PEAK_LOAD_MM*0.1)),printf(\"%.2f\", min(A.PRC_E_AT_PEAK)),printf(\"%.2f\", min(A.E_AT_BREAK_MM*0.1)),printf(\"%.2f\", min(A.PRC_E_AT_BREAK)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()
            
        
                       
                       
        else:
           data= [['Spec. \n No.', 'Thickness (mm)', 'Width (mm)', 'CS.Area (mm2)','Peak Load (kgf)' ,'% E@Peak \n','Break Load (Kg)','E@Break (mm)','%E@Break \n']]
          
           connection = sqlite3.connect("tyr.db")
           results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,A.THICKNESS,A.WIDTH,printf(\"%.4f\", A.CS_AREA),A.PEAK_LOAD,A.E_PAEK_LOAD,round(A.PREC_E_AT_PEAK,2),round(A.E_BREAK_LOAD,2),round(A.PREC_E_AT_BREAK,2) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
           for x in results:
                data.append(x)
           connection.close()  
 
           connection = sqlite3.connect("tyr.db")
           results=connection.execute("SELECT TYPE_STR,round(THICKNESS,2),round(WIDTH,2),printf(\"%.4f\", CS_AREA),PEAK_LOAD,round(E_PAEK_LOAD,2),PREC_E_AT_BREAK FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
           for x in results:
               data.append(x)
           connection.close()            

           
           
        if(self.unit_typex == "Kg/Cm"):
            data2= [ ['Spec. \n No', 'TensileStrength \n (Kgf/Cm2)']]
        
                  
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select CYCLE_NUM,printf(\"%.2f\", A.TENSILE_STRENGTH)  FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
            data2.append(x)
        connection.close()  
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select 'AVG' as SPECIMEN_NUM,printf(\"%.2f\", avg(A.TENSILE_STRENGTH)) FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1") 
        for x in results:
            data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select 'MAX' as SPECIMEN_NUM,printf(\"%.2f\", max(A.TENSILE_STRENGTH))  FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1") 
        for x in results:
            data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select 'MIN' as SPECIMEN_NUM,printf(\"%.2f\", min(A.TENSILE_STRENGTH))  FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) LIMIT 1") 
        for x in results:
            data2.append(x)
        connection.close() 
        
        
        y=300
        Elements=[]
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime'),A.comments  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Specmen Shape:",str(x[9])],["Test Type:",str(x[3]),"Specmen Specs:",str(x[0])],["Party Name :",str(x[7]),"Motor Speed :",str(x[5])],["Guage Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", "","",""]]
            self.comments=str(x[12])
        connection.close() 
        
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select COMPANY_NAME,ADDRESS1 from SETTING_MST ") 
        for x in results:            
            Title = Paragraph(str(x[0]), styles["Title"])
            #Title2 = Paragraph(str(x[1]), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        blank=Paragraph("                                                                                          ", styles["Normal"])
        comments = Paragraph("Remark : ______________________________________________________________________________", styles["Normal"])
        
        footer_2= Paragraph("Authorised and Signed By : _________________.", styles["Normal"])
        
        footer_3= Paragraph("Comments :  "+str(self.comments), styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
        
        f1=Table(data)
        f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
        
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
        #self.show_all_specimens()
        report_gr_img="last_graph_kg_cm.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4* inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f1,Spacer(1,12),Spacer(1,12),f2,Spacer(1,12),blank,comments,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12),Spacer(1,12),footer_3,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/test_report.pdf', pagesize=A4,rightMargin=20,
                                leftMargin=30,
                                topMargin=10,
                                bottomMargin=10)
        doc.build(Elements)
        #print("Done")
       
       
        
            
      
       
        
class PlotCanvas_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="Tensile"
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME from GLOBAL_VAR") 
        for x in results:
            self.test_type=str(x[0])
        connection.close()
        
        if(self.test_type=="Compress"):
            self.axes.set_xlabel('Compression (mm)')        
        else:        
            self.axes.set_xlabel('Elongation (mm)')
          
        self.axes.set_ylabel('Load (Kgf)') 
        self.axes.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.q =0
        self.p_old=0
        self.arr_p=[0.0]
        self.arr_q=[0.0]
        self.arr_p1=[0.0]
        self.arr_q1=[0.0]
        self.x=0
        self.y=0
        #self.ax = self.figure.add_subplot(111) 
        self.xlim=0
        self.ylim=10
        self.line_cnt=0
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
        self.input_rev_speed_val=""
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
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.modbus_flag=""
        self.modbus_port=""
        self.non_modbus_port=""
        
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
   
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                cursor = connection.cursor()                            
                cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
        connection.commit();
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE,ISACTIVE_MODBUS,MODBUS_PORT,NON_MODBUS_PORT from SETTING_MST") 
        for x in results:
             self.axes.set_xlim(0,int(x[0]))
             self.axes.set_ylim(0,int(x[1]))
             self.flexural_max_load=int(x[1])
             self.xlim=int(x[0])
             self.ylim=int(x[1])
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
             self.modbus_flag=str(x[4])
             self.modbus_port=str(x[5])
             self.non_modbus_port=str(x[6])
        connection.close()
        
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0) from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=int(x[0])
             self.test_type=str(x[1])
             self.max_load=int(x[2])
             #self.max_load=100
             self.max_length=float(float(x[0])-float(x[3]))
             #self.max_load=str(self.max_load).zfill(5)
             #self.max_length=str(int(self.max_length)).zfill(5)
             #self.max_length=float(x[3])
             print("Max Load :"+str(self.max_load).zfill(5)+" Max length :"+str(int(self.max_length)).zfill(5))
        connection.close()
        
        try:
            print("indicatior -Modbus Flag :"+str(self.modbus_flag))
            if(self.modbus_flag == 'Y'):
                print("indicatior  non_modbus_port:"+str(self.non_modbus_port))
                if(self.non_modbus_port=="/dev/ttyUSB1"):
                        self.ser = serial.Serial(
                                    port='/dev/ttyUSB1',
                                    baudrate=19200,
                                    bytesize=serial.EIGHTBITS,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    xonxoff=False,
                                    timeout = 0.05
                                )
                else:
                        self.ser = serial.Serial(
                                    port='/dev/ttyUSB0',
                                    baudrate=19200,
                                    bytesize=serial.EIGHTBITS,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    xonxoff=False,
                                    timeout = 0.05
                                )
            else:
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
                self.test_guage_mm=0
                self.command_str="*G0.00\r"
            else:
                self.command_str="*G%.2f"%self.test_guage_mm+"\r"
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
                print("started with default motor speed . Not gohead ")
            #self.ser.write(b'*D\r\n')
                
            #time.sleep(2)
            #========Final Motor start Command =========    
            self.ser.flush()
            if(self.test_type=="Compress"):
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                          self.command_str="*S2C%04d"%self.max_load+" %04d"%self.max_length+"\r"
                    else:
                          self.command_str="*S1C%04d"%self.max_load+" %04d"%self.max_length+"\r"
                    
                    print("self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)                 
                else:
                    print("Compress test not started ")               
                               
            elif(self.test_type=="Flexural"):
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                            #self.ser.write(b'*S2E0599 200\r')
                            self.command_str="*S2E%04d"%self.flexural_max_load+" 0000\r"
                    else:
                            self.command_str="*S1E%04d"%self.flexural_max_load+" 0000\r"
                    print("self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    print("fluexural test started ")
                else:
                    print("fluexural test not started ")
            else:
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
            
        
        
        #self.axes.set_autoscale_on(False)
        #self.axes.autoscale(tight=True)
        #self.axes.autoscale(True, 'both', True)
        #self.axes.plot(self.arr_p,self.arr_q)
        #Create Timer here          
        
        self.timer1.setInterval(1000)     
        self.timer1.timeout.connect(self.update_graph)
        self.timer1.start(1)
       
        self.on_ani_start()
    
    def update_graph(self):       
        if(self.IO_error_flg==0):
            '''
            self.ser.flush()
            self.ser.write(b'*D\r')
            self.line = self.ser.readline()
            print("With Readline Timer Job o/p:"+str(self.line))
            #print("Running")
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
                #print("Running.... :"+str(self.check_R))
                #print("length(X).... :"+str(self.buff[4]))
                #print("load(Y)... :"+str(self.buff[1]))
                #print("Load Cell No... :"+str(self.buff[7]))
                #print("Encoder No.. :"+str(self.buff[6]))
                
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
                    #self.p=int(self.test_guage_mm)-self.p                    
                    if(float(self.test_guage_mm) > float(self.p)):
                        self.p=float(self.test_guage_mm) - float(self.p)
                    else:
                         self.p=self.p-float(self.test_guage_mm)
                    #self.p=self.p-int(self.test_guage_mm)
                    #print("actual self.p :"+str(self.p))
                elif(self.test_type=="Flexural"):
                    self.p=self.p
                else:                    
                    self.p=self.p-int(self.test_guage_mm)
                    if(self.p_old > self.p):
                         self.p=self.p_old                                            
                    self.p_old=self.p
                    #self.p_new=self.p-int(self.test_guage_mm)
                    
                    #self.p=int(self.test_guage_mm)-self.p
                    #self.p=self.p   
                    
                '''
                elif(self.test_type=="Tensile"):
                    self.p=self.p-int(self.test_guage_mm)
                    if(int(len(self.arr_p)) > 0):
                        self.p=float(max(self.arr_p))
                        print("ARRY-P      : XXX "+str(self.arr_p))
                        print("MAX-P      : XXX "+str(self.p))
                        
                        #self.p=float(int(self.p)-int(self.test_guage_mm))
                        print("Length : XXX  "+str(int(len(self.arr_p))))
                        print("P      : XXX "+str(self.p))
                    else:
                        self.p=self.p-int(self.test_guage_mm)
                '''   
                
                
                self.arr_p.append(self.p)
                self.arr_q.append(self.q)
                print(" Timer P:"+str(self.p)+" q:"+str(self.q))
                print("final P :::"+str(self.p)+", guage lengt :"+str(int(self.test_guage_mm)))
                #print(" Array P:"+str(self.arr_p))
                #print(" Array Q:"+str(self.arr_q))
               
                
                #print(" self.q :"+str(self.q)+" self.ylim: "+str(self.ylim))

                if(int(self.q) > int(self.ylim)):
                   self.ylim=(int(self.q)+100)
                   self.ylim_update='YES'                   
                   #print(" self.ylim:"+str(self.ylim))
                
                #print(" self.p :"+str(self.p)+" self.xlim: "+str(self.xlim))
                              
                if(self.p > self.xlim):
                   self.xlim=(int(self.p)+100)
                   self.xlim_update='YES'
                   
                   
                   
                   
                   
                #time.sleep(1) 
            else:                
                if(self.test_type=="Compress"):
                    self.p=abs(float(self.buff[4])) #+random.randint(0,50)
                    self.q=abs(float(self.buff[1])) #+random.randint(0,50)
                    #self.p=int(self.test_guage_mm)-self.p
                    if(float(self.test_guage_mm) > float(self.p)):
                        self.p=float(self.test_guage_mm) - float(self.p)
                    else:
                         self.p=self.p-float(self.test_guage_mm)
                    #print("final P :::"+str(self.p)+", guage lengt :"+str(int(self.test_guage_mm)))
                    self.arr_p.append(self.p)
                    self.arr_q.append(self.q)
                    self.save_data_flg="Yes"
                    #self.on_ani_stop()
                elif(self.test_type=="Flexural"):
                    self.p=abs(float(self.buff[4])) #+random.randint(0,50)
                    self.q=abs(float(self.buff[1])) #+random.randint(0,50)
                    #self.p=int(self.test_guage_mm)-self.p
                    print("final P :::"+str(self.p))
                    self.arr_p.append(self.p)
                    self.arr_q.append(self.q)
                    self.save_data_flg="Yes"
                
                else:
                
                    self.save_data_flg="Yes"
                
       
                    
                
               
     
          
    def plot_grah_only(self,i):        
        #self.arr_p1.append(self.p)
        #self.arr_q1.append(self.q)
        #print("Animation :"+str(i))
        #print(" ANI _P:"+str(self.p)+" q:"+str(self.q))
        #print("data :"+str(self.arr_p1[0]))
        '''
        if(self.xlim_update=='YES'):
             self.axes.set_xlim(0,int(self.xlim))
             self.xlim_update='NO'
             self.axes.relim()
             #time.sleep(1)
        if(self.ylim_update=='YES'): 
             self.axes.set_ylim(0,int(self.ylim))
             self.ylim_update='NO'
             self.axes.relim()
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
           #print("Time 1 has been stopped ")
        #if(self.timer3.isActive()): 
           #self.timer3.stop()                                                                                      
           #print("Time 2 has been stopped ")
           
    def init(self):
        self.line_cnt.set_data([], [])
        return self.line_cnt,

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
       
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT IFNULL(NEW_TEST_MOTOR_SPEED,0), IFNULL(NEW_TEST_MOTOR_REV_SPEED,0) from GLOBAL_VAR") 
        for x in results:
             self.input_speed_val=str(x[0])
             self.input_rev_speed_val=str(x[1])
        connection.close()
        
        if(self.input_speed_val != ""):
            if(float(self.input_speed_val) <= float(self.speed_val)):
                 #print(" Ok ")
                 self.goahead_flag=1
                 self.calc_speed=(float(self.input_speed_val)/float(self.speed_val))*1000                 
                 #print(" calc Speed : "+str(self.calc_speed))
                 #print(" command: *P"+str(self.calc_speed)+" \r")
                 self.command_str="*P%04d"%self.calc_speed+"_%04d"%self.break_sence+"\r"
                 print("Morot Speed and Breaking speed Command  :"+str(self.command_str))                 
            else:
                 print(" not Ok ")
                 #self.label_9_1.show()
                 #self.label_3.setText("Speed Should not more than MAX Speed :"+str(self.speed_val))
                 #self.label_3.show()
        else:
            print(" not Ok ")
            #self.label_3.setText("Motor Speed is Required")
            #self.label_3.show()            
         
        print("test type :"+str(self.test_type))
        print("Modbus Flag :"+str(self.modbus_flag))
        print("Modbus Port :"+str(self.modbus_port))
        if(self.modbus_flag=='Y' and self.modbus_port != "" ):
            if(self.test_type=="Compress"):        
                v=0
                try:
                    v=float(self.input_rev_speed_val) 
                    v=v*40
                    if(float(v) < 1 ):
                        v=1.0
                    elif(float(v)== 1 ):
                        v=1.0
                    else:
                        v=round(v,0)
                        
                    print("compress :int part :%d"%v)
                    print("compress :decial part:%.2f"%v)
                    #v=v*100
                    if(self.modbus_port=="/dev/ttyUSB0"):
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) #
                    else:
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) # port name, slave address (in decimal)                
                    
                    instrument.serial.timeout = 1
                    instrument.serial.baudrate = 9600 
                    instrument.write_register(4098,v,0) ###self.input_speed_val RPM
                    instrument.write_register(4099,0,0) ###self.input_speed_val RPM
                    print(" write1 :"+str(v))
                except IOError as e:
                    print("Forward-Write Modbus IO Error -Motor start : "+str(e))
                
                print("Forward speed : "+str(v))
            
                v=0
                try:     
                    v=float(self.input_speed_val)
                    #v=float(self.input_rev_speed_val)            
                    v=v*40
                    if(float(v) < 1 ):
                        v=1.0
                    elif(float(v)== 1 ):
                        v=1.0
                    else:
                        v=round(v,0)
                    print("int part :%d"%v)
                    print("decial part:%.2f"%v)         
                    print("self.modbus_port :"+str(self.modbus_port))
                    if(self.modbus_port=="/dev/ttyUSB0"):
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) #
                    elif(self.modbus_port=="/dev/ttyUSB1"):
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) #
                    else:
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) #                        
                   
                    instrument.serial.timeout = 1
                    instrument.serial.baudrate = 9600 
                    instrument.write_register(4096,v,0) ###self.input_speed_val RPM
                    instrument.write_register(4097,0,0) ###self.input_speed_val RPM
                    print(" write2 :"+str(v))
                except IOError as e:
                    print("Reverse-Write Modbus IO Error -Motor start : "+str(e))
                
                print("Reverse speed : "+str(v))
            
            
            
            else:   
                print("inside tesnsile part .....")
                v=0
                try:
                    v=float(self.input_speed_val)
                    v=v*40
                    if(float(v) < 1 ):
                        v=1.0
                    elif(float(v)== 1 ):
                        
                        v=1.0
                    else:
                        v=round(v,0)
                        
                    #print("int part :%d"%v)
                    #print("decial part:%.2f"%v)
                    #v=v*100
                    print("self.modbus_port :"+str(self.modbus_port))
                    if(self.modbus_port=="/dev/ttyUSB1"):
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) #                
                    else:
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) #
                                
                    instrument.serial.timeout = 1
                    instrument.serial.baudrate = 9600            
                    instrument.write_register(4098,v,0) ###self.input_speed_val RPM
                    instrument.write_register(4099,0,0) ###self.input_speed_val RPM
                    print(" write1 :"+str(v))
                except IOError as e:
                    print("Forward-Write Modbus IO Error -Motor start : "+str(e))
                
                print("Forward speed : "+str(v))
            
                v=0
                try:     
                    
                    v=float(self.input_rev_speed_val)            
                    v=v*40
                    if(float(v) < 1 ):
                        v=1.0
                    elif(float(v)== 1 ):
                        v=1.0
                    else:
                        v=round(v,0)
                    print("int part :%d"%v)
                    print("decial part:%.2f"%v)         
                    print("self.modbus_port:"+str(self.modbus_port))
                    if(self.modbus_port=="/dev/ttyUSB1"):
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) #                       
                    else:
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) #
                    instrument.serial.timeout = 1
                    instrument.serial.baudrate = 9600            
                    instrument.write_register(4096,v,0) ###self.input_speed_val RPM
                    instrument.write_register(4097,0,0) ###self.input_speed_val RPM
                    print(" write2 :"+str(v))
                except IOError as e:
                    print("Reverse-Write Modbus IO Error -Motor start : "+str(e))
                
                print("Reverse speed : "+str(v))
            
 



        
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #fig.savefig('ssdsd.png')
        self.axes = fig.add_subplot(111)        
        FigureCanvas.__init__(self, fig)
        #FigureCanvas.setStyleSheet("background-color:red;")
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)       
        
        self.plot()        
        
        
    def plot(self):
        ax = self.figure.add_subplot(111)
       
        ax.set_facecolor('#CCFFFF')   
        ax.minorticks_on()
        
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        
        self.s=[]
        self.t=[]
        self.graph_ids=[]    
        self.x_num=[0.0]
        self.y_num=[0.0]
        self.test_type="Tensile"
        self.color=['b','r','g','y','k','c','m','b']
        #ax.set_title('Test Id=32         Samples=3       BreakLoad(Kg)=110        Length(mm)=3')         
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_ID,TEST_ID,SHAPE FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
             self.graph_ids.append(x[0])             
        connection.close()
        
        ### Univarsal change for  Graphs #####################
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
             ax.set_xlim(0,int(x[0]))
             ax.set_ylim(0,int(x[1]))          
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME FROM GLOBAL_VAR") 
        for x in results:
             self.test_type=str(x[0])            
        connection.close()
        
        
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
        
            connection = sqlite3.connect("tyr.db")
            if(self.test_type=="Compress" or self.test_type=="Flexural"):
                results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE GRAPH_ID='"+str(self.graph_ids[g])+"'")
            else:   
                results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            for k in results:        
                self.x_num.append(k[0])
                self.y_num.append(k[1])
            connection.close() 
        
            if(g < 8 ):
                ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
        
        print("self.test_type:"+str(self.test_type))
        if(str(self.test_type)=="Compress"):
            ax.set_xlabel('Compression (mm)')        
        else:
            ax.set_xlabel('Elongation (mm)')
        ax.set_ylabel('Load (Kgf)')
        #self.connect('motion_notify_event', mouse_move)
        ax.legend()        
        self.draw()
        self.figure.savefig('last_graph.png',dpi=100)
        
        #ax.connect('motion_notify_event', mouse_move)
    
    

class PlotCanvas_blank(FigureCanvas):
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)        
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot_blank()        
        
    def plot_blank(self):                
        
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                cursor = connection.cursor()                            
                cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
        connection.commit();
        connection.close()
        
        self.x=[0,0,0,0,0,0,0,0]
        self.y=[0,0,0,0,0,0,0,0]
        
        self.p=list()
        self.q=list()
        self.test_type="Tensile"
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#CCFFFF')
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
       
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
             ax.set_xlim(0,int(x[0]))
             ax.set_ylim(0,int(x[1]))          
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])  
              
        ax.plot(self.x,self.y,'b')
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME FROM GLOBAL_VAR") 
        for x in results:
             self.test_type=str(x[0])            
        connection.close()
        
        ax.set_ylabel('Load (Kgf)')
        
        
        if(self.test_type=="Compress"):
            ax.set_xlabel('Compression (mm)')       
        else:
            ax.set_xlabel('Elongation (mm)')
        self.draw() 


class Ext_PlotCanvas_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="Tensile"
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME from GLOBAL_VAR") 
        for x in results:
            self.test_type=str(x[0])
        connection.close()
        
        if(self.test_type=="Compress"):
            self.axes.set_xlabel('Compression (mm)')        
        else:        
            self.axes.set_xlabel('Elongation (mm)')
          
        self.axes.set_ylabel('Load (Kgf)') 
        self.axes.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.q =0
        self.p_old=0
        self.arr_p=[0.0]
        self.arr_q=[0.0]
        self.arr_p1=[0.0]
        self.arr_q1=[0.0]
        self.x=0
        self.y=0
        #self.ax = self.figure.add_subplot(111) 
        self.xlim=0
        self.ylim=10
        self.line_cnt=0
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
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
   
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                cursor = connection.cursor()                            
                cursor.execute("DELETE FROM STG_GRAPH_MST ")                
                cursor.execute("UPDATE GLOBAL_VAR SET DEF_POINT='0.0', DEF_LOAD='0.0',DEF_YEILD_STRG='0.0' ") 
        connection.commit();
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:
             self.axes.set_xlim(0,int(x[0]))
             self.axes.set_ylim(0,int(x[1]))
             self.flexural_max_load=int(x[1])
             self.xlim=int(x[0])
             self.ylim=int(x[1])
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
        connection.close()
        
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0) from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=int(x[0])
             self.test_type=str(x[1])
             self.max_load=int(x[2])
             #self.max_load=100
             self.max_length=float(float(x[0])-float(x[3]))
             #self.max_load=str(self.max_load).zfill(5)
             #self.max_length=str(int(self.max_length)).zfill(5)
             #self.max_length=float(x[3])
             print("Max Load :"+str(self.max_load).zfill(5)+" Max length :"+str(int(self.max_length)).zfill(5))
        connection.close()
        
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
            
            self.ser2 = serial.Serial(
                        port='/dev/ttyAMA0',
                        baudrate=115200,
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
            
            
            self.ser2.flush()           
            self.yline2 = self.ser2.readline()
            
            
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
                self.test_guage_mm=0
                self.command_str="*G0.00\r"
            else:
                self.command_str="*G%.2f"%self.test_guage_mm+"\r"
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
                #print("started with default motor speed . Not gohead ")
            #self.ser.write(b'*D\r\n')
                
            #time.sleep(2)
            #========Final Motor start Command =========    
            self.ser.flush()
            if(self.test_type=="Compress"):
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                          self.command_str="*S2C%04d"%self.max_load+" %04d"%self.max_length+"\r"
                    else:
                          self.command_str="*S1C%04d"%self.max_load+" %04d"%self.max_length+"\r"
                    
                    print("self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)                 
                else:
                    print("Compress test not started ")               
                               
            elif(self.test_type=="Flexural"):
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                            #self.ser.write(b'*S2E0599 200\r')
                            self.command_str="*S2E%04d"%self.flexural_max_load+" 0000\r"
                    else:
                            self.command_str="*S1E%04d"%self.flexural_max_load+" 0000\r"
                    print("self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    print("fluexural test started ")
                else:
                    print("fluexural test not started ")
            else:
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
            
        
        
        #self.axes.set_autoscale_on(False)
        #self.axes.autoscale(tight=True)
        #self.axes.autoscale(True, 'both', True)
        #self.axes.plot(self.arr_p,self.arr_q)
        #Create Timer here          
        
        self.timer1.setInterval(1000)     
        self.timer1.timeout.connect(self.update_graph)
        self.timer1.start(1)
       
        self.on_ani_start()
    
    def update_graph(self):       
        if(self.IO_error_flg==0):
            '''
            self.ser.flush()
            self.ser.write(b'*D\r')
            self.line = self.ser.readline()
            print("With Readline Timer Job o/p:"+str(self.line))
            #print("Running")
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
                #print("Running.... :"+str(self.check_R))
                #print("length(X).... :"+str(self.buff[4]))
                #print("load(Y)... :"+str(self.buff[1]))
                #print("Load Cell No... :"+str(self.buff[7]))
                #print("Encoder No.. :"+str(self.buff[6]))
                
               
                
#                if(self.load_cell_hi==1):              
#                    self.q=abs(float(self.buff[1])) #+random.randint(0,50)
#                else:
#                    self.q=abs(float(self.buff[0]))
                
                self.q=abs(float(self.buff[1]))
                self.p=self.ser2.readline(15)                
                self.xstr0=str(self.p,'utf-8')
                print("Second Port2:"+str(self.xstr0))
                self.xstr1=self.xstr0.replace("\r","")
                self.xstr2=self.xstr1.replace("\n","")
                self.buff=self.xstr2.split("_")                
                if(len(self.buff)> 1):
                                self.xstr2=str(self.buff[0])
                                try:
                                     self.xstr4=float(self.xstr2)
                                except ValueError:                        
                                    print("Value Error"+str(self.xstr2))
                                    self.xstr4=0   
                
                                self.p=float(self.xstr4)
                    #self.p_new=self.p-int(self.test_guage_mm)
                    
                    #self.p=int(self.test_guage_mm)-self.p
                    #self.p=self.p   
                    
                 
                
                
                self.arr_p.append(self.p)
                self.arr_q.append(self.q)
                print(" Timer P:"+str(self.p)+" q:"+str(self.q))
               
                #print(" Array P:"+str(self.arr_p))
                #print(" Array Q:"+str(self.arr_q))
               
                
                #print(" self.q :"+str(self.q)+" self.ylim: "+str(self.ylim))

                if(int(self.q) > int(self.ylim)):
                   self.ylim=(int(self.q)+100)
                   self.ylim_update='YES'                   
                   #print(" self.ylim:"+str(self.ylim))
                
                #print(" self.p :"+str(self.p)+" self.xlim: "+str(self.xlim))
                              
                if(self.p > self.xlim):
                   self.xlim=(int(self.p)+100)
                   self.xlim_update='YES'
                   
                   
                   
                   
                   
                #time.sleep(1) 
            else:                
                if(self.test_type=="Compress"):
                    self.p=abs(float(self.buff[4])) #+random.randint(0,50)
                    self.q=abs(float(self.buff[1])) #+random.randint(0,50)
                    self.p=int(self.test_guage_mm)-self.p
                    #self.p=self.p-int(self.test_guage_mm)
                    print("final P :::"+str(self.p))
                    self.arr_p.append(self.p)
                    self.arr_q.append(self.q)
                    self.save_data_flg="Yes"
                    #self.on_ani_stop()
                elif(self.test_type=="Flexural"):
                    self.p=abs(float(self.buff[4])) #+random.randint(0,50)
                    self.q=abs(float(self.buff[1])) #+random.randint(0,50)
                    #self.p=int(self.test_guage_mm)-self.p
                    print("final P :::"+str(self.p))
                    self.arr_p.append(self.p)
                    self.arr_q.append(self.q)
                    self.save_data_flg="Yes"
                
                else:
                
                    self.save_data_flg="Yes"
                
       
                    
                
               
     
          
    def plot_grah_only(self,i):        
        #self.arr_p1.append(self.p)
        #self.arr_q1.append(self.q)
        #print("Animation :"+str(i))
        #print(" ANI _P:"+str(self.p)+" q:"+str(self.q))
        #print("data :"+str(self.arr_p1[0]))
        '''
        if(self.xlim_update=='YES'):
             self.axes.set_xlim(0,int(self.xlim))
             self.xlim_update='NO'
             self.axes.relim()
             #time.sleep(1)
        if(self.ylim_update=='YES'): 
             self.axes.set_ylim(0,int(self.ylim))
             self.ylim_update='NO'
             self.axes.relim()
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
           #print("Time 1 has been stopped ")
        #if(self.timer3.isActive()): 
           #self.timer3.stop()                                                                                      
           #print("Time 2 has been stopped ")
           
    def init(self):
        self.line_cnt.set_data([], [])
        return self.line_cnt,

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
       
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT IFNULL(NEW_TEST_MOTOR_SPEED,0) from GLOBAL_VAR") 
        for x in results:
             self.input_speed_val=str(x[0])
        connection.close()
        
        if(self.input_speed_val != ""):
            if(int(self.input_speed_val) <= int(self.speed_val)):
                 #print(" Ok ")
                 self.goahead_flag=1
                 self.calc_speed=(int(self.input_speed_val)/int(self.speed_val))*1000                 
                 #print(" calc Speed : "+str(self.calc_speed))
                 #print(" command: *P"+str(self.calc_speed)+" \r")
                 self.command_str="*P%04d"%self.calc_speed+"_%04d"%self.break_sence+"\r"
                 print("Morot Speed and Breaking speed Command  :"+str(self.command_str))                 
            else:
                 print(" not Ok ")
                 #self.label_9_1.show()
                 #self.label_3.setText("Speed Should not more than MAX Speed :"+str(self.speed_val))
                 #self.label_3.show()
        else:
            print(" not Ok ")
            #self.label_3.setText("Motor Speed is Required")
            #self.label_3.show()            
    
    
 




class Kg_Cm_PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #fig.savefig('ssdsd.png')
        self.axes = fig.add_subplot(111)        
        FigureCanvas.__init__(self, fig)
        #FigureCanvas.setStyleSheet("background-color:red;")
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)       
        
        self.plot()        
        
        
    def plot(self):
        ax = self.figure.add_subplot(111)
       
        ax.set_facecolor('#CCFFFF')   
        ax.minorticks_on()
        
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        
        self.s=[]
        self.t=[]
        self.graph_ids=[]    
        self.x_num=[0.0]
        self.y_num=[0.0]
        self.test_type="Tensile"
        self.color=['b','r','g','y','k','c','m','b']
        #ax.set_title('Test Id=32         Samples=3       BreakLoad(Kg)=110        Length(mm)=3')         
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_ID,TEST_ID,SHAPE FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
             self.graph_ids.append(x[0])             
        connection.close()
        
        ### Univarsal change for  Graphs #####################
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2*0.1,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
             ax.set_xlim(0,int(x[0]))
             ax.set_ylim(0,int(x[1]))          
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME FROM GLOBAL_VAR") 
        for x in results:
             self.test_type=str(x[0])            
        connection.close()
        
        
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
        
            connection = sqlite3.connect("tyr.db")
            if(self.test_type=="Compress" or self.test_type=="Flexural"):
                results=connection.execute("SELECT X_NUM*0.1,Y_NUM FROM GRAPH_MST WHERE GRAPH_ID='"+str(self.graph_ids[g])+"'")
            else:   
                results=connection.execute("SELECT X_NUM*0.1,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            for k in results:        
                self.x_num.append(k[0])
                self.y_num.append(k[1])
            connection.close() 
        
            if(g < 8 ):
                ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
        
        print("self.test_type:"+str(self.test_type))
        if(str(self.test_type)=="Compress"):
            ax.set_xlabel('Compression (Cm)')        
        else:
            ax.set_xlabel('Elongation (Cm)')
        ax.set_ylabel('Load (Kgf)')
        #self.connect('motion_notify_event', mouse_move)
        ax.legend()        
        self.draw()
        self.figure.savefig('last_graph_kg_cm.png',dpi=100)
        
        #ax.connect('motion_notify_event', mouse_move)
    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_02_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
