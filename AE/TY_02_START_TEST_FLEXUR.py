

import sys
import os

from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow

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
import serial

import minimalmodbus
#from minimalmodbus import BYTEORDER_LITTLE_SWAP
#minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
minimalmodbus.clear_buffers_before_each_transaction = True
#minimalmodbus.BYTEORDER_BIG= 0
#minimalmodbus.BYTEORDER_LITTLE= 1
minimalmodbus.MODE_RTU= 'rtu'


class TY_02f_Ui_MainWindow(object):
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
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 0, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 4, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 1, 1, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 4, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(790, 360, 491, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_4.addWidget(self.label_35, 0, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_4.addWidget(self.label_37, 0, 2, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_4.addWidget(self.label_33, 1, 0, 1, 1)
        
        
        self.label_34 = QtWidgets.QLCDNumber(self.widget1) #QtWidgets.QLabel(self.widget1)
        self.label_34.setStyleSheet("background-color: rgb(0, 0, 0);\n" "font: 10pt \"Arial\";\n" "color: rgb(255, 0, 0);")
        self.label_34.setProperty("value", "0")
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 1, 1, 1, 1)
        
       
        
        
        
        self.label_39 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)        
        self.label_39.setObjectName("label_39")
        self.gridLayout_4.addWidget(self.label_39, 1, 2, 1, 1)
        
        
        self.label_40 = QtWidgets.QLCDNumber(self.widget1)
        self.label_40.setStyleSheet("background-color: rgb(0, 0, 0);\n" "font: 10pt \"Arial\";\n" "color: rgb(255, 0, 0);")
        self.label_40.setProperty("value", "00.0")
        self.label_40.setObjectName("label_40")
        self.gridLayout_4.addWidget(self.label_40, 1, 3, 1, 1)
        
        
        
        
        
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 530, 1271, 161))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(11, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(12, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(13, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(14, item)
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(15, item)
        
        
        
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 9, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(790, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        #font.setBold(True)
        #font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 85, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(1040, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        #font.setBold(False)
        #font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(790, 70, 371, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 3, 1, 1)
        
        self.label_24 = QtWidgets.QLineEdit(self.layoutWidget)
        
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.label_24)
        self.label_24.setValidator(input_validator)
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)        
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 4, 1, 1)
        
        
        
        self.label_31 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 1, 3, 1, 1)
        
        self.label_32 = QtWidgets.QLineEdit(self.layoutWidget)
        
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.label_32)
        self.label_32.setValidator(input_validator)
        
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 1, 0, 1, 1)
        #self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22 = QtWidgets.QLineEdit(self.layoutWidget)
        
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.label_22)
        self.label_22.setValidator(input_validator)
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        #self.label_22.setMaximumWidth(100)
        
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 1, 1, 2)
        self.label_26 = QtWidgets.QLineEdit(self.layoutWidget)
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.label_26)
        self.label_26.setValidator(input_validator)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setMaximumWidth(200)
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
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setText("Start")
        self.pushButton.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 200, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(247, 255, 226);")
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap("images/start.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.pushButton.setIcon(icon)
#         self.pushButton.setIconSize(QtCore.QSize(100, 80))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        
        
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
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
        font.setFamily("Arial")
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
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)     
        
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("Return")
        self.pushButton_4.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(200, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(247, 255, 226);")
#         icon4 = QtGui.QIcon()
#         icon4.addPixmap(QtGui.QPixmap("images/back.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.pushButton_4.setIcon(icon4)
#         self.pushButton_4.setIconSize(QtCore.QSize(100, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 2, 1, 1)
        
        
        
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(1180, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(1180, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        
        self.label_3_1 = QtWidgets.QLabel(self.frame)
        self.label_3_1.setGeometry(QtCore.QRect(790, 155, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        #font.setBold(False)        
        #font.setWeight(50)
        self.label_3_1.setText("Input Strain (%) :")
        self.label_3_1.setFont(font)
        #self.label_3_1.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3_1.setObjectName("label_3_1")
        
        self.lineEdit_3_1 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3_1)
        self.lineEdit_3_1.setValidator(input_validator)
        self.lineEdit_3_1.setGeometry(QtCore.QRect(945, 163, 52, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)        
        
        self.lineEdit_3_1.setFont(font)
        
        self.lineEdit_3_1.setObjectName("lineEdit_3_1")
        
        self.label_3_2 = QtWidgets.QLabel(self.frame)
        self.label_3_2.setGeometry(QtCore.QRect(1040, 155, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        
        
        self.label_3_2.setFont(font)
        self.label_3_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3_2.setObjectName("label_3_2")
        
        
        
        
        
        
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(790, 182, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        #font.setBold(False)        
        #font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.inut_strain_mm=0
        self.per_strain_mm=0
        self.span=0
        self.cycle_num=0
        self.guage_ext_flg='N'
        
        self.last_load_unit=""
        self.last_disp_unit=""
             
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
        self.label_35.hide()
        self.label_36.setText(_translate("MainWindow", "100"))
        self.label_36.hide()
        self.label_37.setText(_translate("MainWindow", "Length at Peak(mm):   "))
        self.label_37.hide()
        self.label_38.setText(_translate("MainWindow", "220"))
        self.label_38.hide()
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
        item.setText(_translate("MainWindow", "Product Length \n (mm)"))
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
        self.label.setText(_translate("MainWindow", "Flexural Test"))
        self.label_2.setText(_translate("MainWindow", datetime.datetime.now().strftime("%B  %d , %Y %I:%M ")+""))
        self.label_23.setText(_translate("MainWindow", "Support Radius(mm):"))
        self.label_24.setText(_translate("MainWindow", "Batch_900011"))
        self.label_31.setText(_translate("MainWindow", "Load Radius(mm):"))
        self.label_32.setText(_translate("MainWindow", "J11"))
        self.label_21.setText(_translate("MainWindow", "Span(mm) :"))
        self.label_25.setText(_translate("MainWindow", "Speed(mm/min).:"))
        self.label_22.setText(_translate("MainWindow", "90"))
        self.label_26.setText(_translate("MainWindow", "1"))
        self.lineEdit_3_1.setText("5") #% Strain at Break
        self.label_3_2.setText("2 mm") #% strain conversion to mm
        self.radioButton.setText(_translate("MainWindow", "Extentiometer"))
        self.radioButton_2.setText(_translate("MainWindow", "Encoder"))
        self.label_3.setText(_translate("MainWindow", "Msg:Test Started"))
        self.label_3.hide()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_LOAD_UNIT,LAST_DISP_UNIT from GLOBAL_VAR2") 
        for x in results:                 
             self.last_load_unit=str(x[0])
             self.last_disp_unit=str(x[1])  
        connection.close()
        print("self.last_load_unit:"+str(self.last_load_unit)+"    self.last_disp_unit:"+str(self.last_disp_unit))
        if(str(self.last_load_unit)=="MPa" and str(self.last_disp_unit)=="Mm"):
                self.label_35.setText("Force at Peak (N):")
                self.label_37.setText("Length at Peak(mm):   ")
                self.label_33.setText(" Force (N):   ")
                self.label_39.setText("Displacement (mm):")
        elif(self.last_load_unit == "Kg" and self.last_disp_unit=="Mm"):
                self.label_35.setText("Force at Peak (Kgf):")
                self.label_37.setText("Length at Peak(mm):   ")
                self.label_33.setText(" Force (Kgf):   ")
                self.label_39.setText("Displacement (mm):")
        else:
                self.label_35.setText("Force at Peak ("+str(self.last_load_unit)+"):")
                self.label_37.setText("Length at Peak("+str(self.last_disp_unit)+"):   ")
                self.label_33.setText(" Force ("+str(self.last_load_unit)+"):   ")
                self.label_39.setText("Displacement ("+str(self.last_disp_unit)+"):")
        
        
        
        
        
        self.sc_blank =PlotCanvas_blank(self,width=5, height=2)         
        self.gridLayout_2.addWidget(self.sc_blank, 0, 0, 1, 5)
        self.pushButton_5.clicked.connect(self.show_all_specimens)
       
        self.pushButton.clicked.connect(self.show_real_time)
        self.tableWidget.doubleClicked.connect(self.delete_cycle)
        #self.radioButton_3.clicked.connect(self.save_graph_data)
        self.load_data()
        #self.radioButton_4.setDisabled(True)  ### reset
        #self.radioButton_3.setDisabled(True) ### Save
        self.lineEdit_3.textChanged.connect(self.cal_cs_area)
        self.lineEdit_4.textChanged.connect(self.cal_cs_area)
        self.lineEdit_3_1.textChanged.connect(self.on_change_input_strain)
        self.label_22.textChanged.connect(self.on_change_input_strain)
        self.pushButton_4.clicked.connect(MainWindow.close)
        #self.lineEdit_2.setText("2")
        #self.lineEdit_3.setText("3")
        #self.lineEdit_4.setText("4")  
        #self.load_data()
        self.load_cell_hi=0
        self.load_cell_lo=0
        self.extiometer=0
        self.encoder=0
        self.cycle_id=0
        self.test_method=""       
                      
        self.failure_mod=""        
                      
        self.tmperature=""
        self.test_type_for_flexural=""
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select NEW_TEST_NAME FROM GLOBAL_VAR")                 
        for x in results:                
                    self.test_type_for_flexural=str(x[0])            
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
            
            self.timer3=QtCore.QTimer()
            self.timer3.setInterval(5000)        
            self.timer3.timeout.connect(self.loadcell_encoder_status)
            self.timer3.start(1)
        except IOError:
            print("IO Errors")
    
    def on_change_input_strain(self):
        self.inut_strain_mm=0
        self.per_strain_mm=0
        self.span=self.label_22.text()
        
        if(self.lineEdit_3_1.text() == ""):
             self.lineEdit_3_1.setText("0")
        else:
            print("% : "+str(self.label_3_1.text()))
            self.per_strain_mm=self.lineEdit_3_1.text()
            if(int(self.lineEdit_3_1.text()) > 0 ):
                    self.inut_strain_mm=float((int(self.per_strain_mm)/100)*int(self.span))
                    self.label_3_2.setText(str(round(self.inut_strain_mm,2))+" mm ")
        
             
    
    def delete_cycle(self):
        if(self.test_type_for_flexural=="Flexural"):
            row = self.tableWidget.currentRow() 
            self.cycle_id=str(self.tableWidget.item(row, 15).text())
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
        self.label_3_3.setGeometry(QtCore.QRect(1010, 490, 80, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)        
        font.setWeight(50)
        self.label_3_3.setFont(font)
        self.label_3_3.setText("Temp.(C):")
        self.label_3_3.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3_3.setObjectName("label_3_3")
        
        
        self.lineEdit_3_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_3.setGeometry(QtCore.QRect(1080, 490, 38, 31))
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3_3)
        self.lineEdit_3_3.setValidator(input_validator)        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)        
        font.setWeight(50)
        self.lineEdit_3_3.setFont(font)
        self.lineEdit_3_3.setText("25")
        self.lineEdit_3_3.setObjectName("lineEdit_3_3")
        
        
        self.pushButton_3_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3_3.setGeometry(QtCore.QRect(1130, 490, 40, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_3_3.setFont(font)
        #self.pushButton_3_3.setText("R")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Report.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3_3.setIcon(icon3)
        self.pushButton_3_3.setIconSize(QtCore.QSize(35, 35))        
        self.pushButton_3_3.setObjectName("pushButton_3_3")
        self.pushButton_3_3.clicked.connect(self.open_pdf)
        
        
        self.pushButton_3_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3_4.setGeometry(QtCore.QRect(1185, 490, 40, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_3_4.setFont(font)        
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Print.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3_4.setIcon(icon3)
        self.pushButton_3_4.setIconSize(QtCore.QSize(35, 35)) 
        self.pushButton_3_4.clicked.connect(self.print_file)
        self.pushButton_3_4.setObjectName("pushButton_3_4")
        
        
        self.pushButton_3_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3_5.setGeometry(QtCore.QRect(1240, 490, 40, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_3_5.setFont(font)        
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/email.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3_5.setIcon(icon3)
        self.pushButton_3_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3_5.clicked.connect(self.open_email_report)
        self.pushButton_3_5.setObjectName("pushButton_3_5")
       
        self.label_3_4= QtWidgets.QLabel(self.frame)
        self.label_3_4.setGeometry(QtCore.QRect(790, 490, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)        
        font.setWeight(50)
        self.label_3_4.setFont(font)
        self.label_3_4.setText("Failure Mode:")
        self.label_3_4.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3_4.setObjectName("label_3_4")
        
        
        self.lineEdit_3_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_4.setGeometry(QtCore.QRect(890, 490, 100, 31))               
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)        
        font.setWeight(50)
        self.lineEdit_3_4.setFont(font)
        self.lineEdit_3_4.setText("Bending")
        self.lineEdit_3_4.setObjectName("lineEdit_3_4")
        
        
        
        self.label_3_5= QtWidgets.QLabel(self.frame)
        self.label_3_5.setGeometry(QtCore.QRect(470, 490, 80, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
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
        
            
    
    def show_grid_data_flexure(self):        
        #print("inside tear list.....")
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(16)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        if(str(self.last_load_unit)=="MPa" and str(self.last_disp_unit)=="Mm"):
              self.tableWidget.setHorizontalHeaderLabels(['Length \n (mm)','Force at Peak \n (N)',' Displacement \n (mm) ','Support Span  \n(mm)','Width \n (mm)','Thickness \n (mm)','Flexural \n Strength (MPa)','Flexural \n Modulus \n ','Support Radius \n (mm)','Load Radius \n (mm)',' Speed \n (mm/min)','Input Strain \n (%)','Strain at Break \n ( % )','Failure \n Mode','Test  \n Method','Cycle ID'])        
        elif(self.last_load_unit == "Kg" and self.last_disp_unit=="Mm"):
              self.tableWidget.setHorizontalHeaderLabels(['Length \n (mm)','Force at Peak \n (Kgf)',' Displacement \n (mm) ','Support Span  \n(mm)','Width \n (mm)','Thickness \n (mm)','Flexural \n Strength (Kgf/cm2)','Flexural \n Modulus \n ','Support Radius \n (mm)','Load Radius \n (mm)',' Speed \n (mm/min)','Input Strain \n (%)','Strain at Break \n ( % )','Failure \n Mode','Test  \n Method','Cycle ID'])        
        else:
              self.tableWidget.setHorizontalHeaderLabels(['Length \n ('+str(self.last_disp_unit)+')','Force at Peak \n ('+str(self.last_load_unit)+')',' Displacement \n ('+str(self.last_disp_unit)+') ','Support Span  \n('+str(self.last_disp_unit)+')','Width \n ('+str(self.last_disp_unit)+')','Thickness \n ('+str(self.last_disp_unit)+')','Flexural \n Strength ('+str(self.last_load_unit)+'/'+str(self.last_disp_unit)+'2)','Flexural \n Modulus \n ','Support Radius \n ('+str(self.last_disp_unit)+')','Load Radius \n ('+str(self.last_disp_unit)+')',' Speed \n (mm/min)','Input Strain \n (%)','Strain at Break \n ( % )','Failure \n Mode','Test  \n Method','Cycle ID'])        
        
        
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 250)
        self.tableWidget.setColumnWidth(7, 100)
        self.tableWidget.setColumnWidth(8, 150)
        self.tableWidget.setColumnWidth(9, 150)
        self.tableWidget.setColumnWidth(10, 150)
        self.tableWidget.setColumnWidth(11, 150)
        self.tableWidget.setColumnWidth(12, 150)
        self.tableWidget.setColumnWidth(13, 150)
        self.tableWidget.setColumnWidth(14, 150)
        self.tableWidget.setColumnWidth(15, 150)
        
        connection = sqlite3.connect("tyr.db")
        if(str(self.last_load_unit)=="MPa" and str(self.last_disp_unit)=="Mm"):
             results=connection.execute("SELECT printf(\"%.2f\", GUAGE100),printf(\"%.2f\", PEAK_LOAD_N),printf(\"%.2f\", E_AT_BREAK_MM),(SELECT printf(\"%.2f\", NEW_TEST_MAX_LOAD) FROM GLOBAL_VAR),printf(\"%.2f\", WIDTH),printf(\"%.2f\", THINCKNESS),printf(\"%.2f\", FLEXURAL_STRENGTH_MPA) ,printf(\"%.2f\", FLEXURAL_MOD_MPA),printf(\"%.2f\", LOAD_RADIOUS),printf(\"%.2f\", SUPPORT_RADIOUS),SPEED_RPM,PER_STRAIN_AT_INPUT,PER_STRAIN_AT_BREAK,BREAK_MODE,TEST_METHOD,CYCLE_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID ")
       
        elif(self.last_load_unit == "Kg" and self.last_disp_unit=="Mm"):
             results=connection.execute("SELECT printf(\"%.2f\", GUAGE100),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_BREAK_MM),(SELECT printf(\"%.2f\", NEW_TEST_MAX_LOAD) FROM GLOBAL_VAR),printf(\"%.2f\", WIDTH),printf(\"%.2f\", THINCKNESS),printf(\"%.2f\", FLEXURAL_STRENGTH_KG_CM) ,printf(\"%.2f\", FLEXURAL_MOD_KG_CM),printf(\"%.2f\", LOAD_RADIOUS),printf(\"%.2f\", SUPPORT_RADIOUS),SPEED_RPM,PER_STRAIN_AT_INPUT,PER_STRAIN_AT_BREAK,BREAK_MODE,TEST_METHOD,CYCLE_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID ")
       
        else:
             results=connection.execute("SELECT printf(\"%.2f\", GUAGE100),printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_BREAK_MM),(SELECT printf(\"%.2f\", NEW_TEST_MAX_LOAD) FROM GLOBAL_VAR),printf(\"%.2f\", WIDTH),printf(\"%.2f\", THINCKNESS),printf(\"%.2f\", FLEXURAL_STRENGTH_KG_CM) ,printf(\"%.2f\", FLEXURAL_MOD_KG_CM),printf(\"%.2f\", LOAD_RADIOUS),printf(\"%.2f\", SUPPORT_RADIOUS),SPEED_RPM,PER_STRAIN_AT_INPUT,PER_STRAIN_AT_BREAK,BREAK_MODE,TEST_METHOD,CYCLE_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID ")
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
                
                self.sc_new =PlotCanvas_Auto(self,width=5, height=4, dpi=80)
                self.gridLayout_2.addWidget(self.sc_new, 0,0,1,5)
                
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
        print("Last value of P :"+str(self.sc_new.p))
        #print("Length of P :"+str(len(self.sc_new.arr_p)))
        #print("Length of q :"+str(len(self.sc_new.arr_q)))
        #self.label_34.setProperty("value", "0")
        #self.label_40.setProperty("value","0")   #length
        
        if (len(self.sc_new.arr_p) > 1):
            
            #### Get Guage length
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("select IFNULL(NEW_TEST_GUAGE_MM,0),NEW_TEST_NAME FROM GLOBAL_VAR")                 
            for x in results:
                self.guage_length_mm=int(x[0])
                self.test_type=str(x[1])
            
            connection.close()
            #print("self.guage_length_mm:"+str(self.guage_length_mm))
                                   
            print("length of arr P :"+str(len(self.sc_new.arr_p))+"  length of arr q "+str(len(self.sc_new.arr_q))+"  length of arr q_n "+str(len(self.sc_new.arr_q_n)))
       
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)-1):
                  if(self.test_type=="Compress" or self.test_type=="Flexural"):
                        cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM,Y_NUM_N) VALUES ('"+str(float(self.sc_new.arr_p[g]))+"','"+str(float(self.sc_new.arr_q[g]))+"','"+str(float(self.sc_new.arr_q_n[g]))+"')")
                        #cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_LB,Y_NUM_KN,Y_NUM_MPA) VALUES ('"+str(float(self.sc_new.arr_p[g]))+"','"+str(float(self.sc_new.arr_p_cm[g]))+"','"+str(float(self.sc_new.arr_p_inch[g]))+"','"+str(self.sc_new.arr_q[g])+"','"+str(self.sc_new.arr_q_n[g])+"','"+str(self.sc_new.arr_q_lb[g])+"','"+str(self.sc_new.arr_q_kn[g])+"','"+str(self.sc_new.arr_q_mpa[g])+"')")
                  else:   
                        cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM) VALUES ('"+str(int(self.sc_new.arr_p[g]))+"','"+str(self.sc_new.arr_q[g])+"')")
            connection.commit();
            connection.close()
            
            
            
            
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
            self.cycle_num=self.cycle_num+1
            #self.pushButton_2.setEnabled(True)
            connection = sqlite3.connect("tyr.db")              
            with connection:        
                  cursor = connection.cursor()              
                  #print("ok1")
                  cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_THICKNESS='"+str(self.lineEdit_4.text())+"',NEW_TEST_WIDTH='"+str(self.lineEdit_3.text())+"',NEW_TEST_AREA='"+str(self.lineEdit_2.text())+"',NEW_TEST_DIAMETER='"+str(self.lineEdit_4.text())+"', NEW_TEST_INN_DIAMETER='"+str(self.lineEdit_4.text())+"', NEW_TEST_OUTER_DIAMETER='"+str(self.lineEdit_3.text())+"',SPAN='"+str(self.label_22.text())+"',SUPPORT_RADIOUS='"+str(self.label_32.text())+"',LOAD_RADIOUS='"+str(self.label_24.text())+"',PER_STRAIN_AT_INPUT='"+str(self.lineEdit_3_1.text())+"',SPEED_RPM='"+str(self.label_26.text())+"'")
                  #print("ok2")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM) FROM STG_GRAPH_MST)")   ### STG_PEAK_LOAD_KG
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_N=(SELECT MAX(Y_NUM_N) FROM STG_GRAPH_MST)")  
                  
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
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_LOAD300_GUAGE='"+str(self.load300_guage)+"'")
                  
                  
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_MODULUS_200=((cast(STG_LOAD200_GUAGE as real)/cast(NEW_TEST_AREA as real))*100)")
                  
                  
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_LOAD300_GUAGE='"+str(self.load300_guage)+"'")              
                  
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_MODULUS_300=((cast(STG_LOAD300_GUAGE as real)/cast(NEW_TEST_AREA as real))*100)")
                 
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_MODULUS_100=IFNULL(STG_MODULUS_100,0),STG_MODULUS_200=IFNULL(STG_MODULUS_200,0),STG_MODULUS_300=IFNULL(STG_MODULUS_300,0)")
                  
                  cursor.execute("INSERT INTO CYCLES_MST(TEST_ID,SHAPE,THINCKNESS,WIDTH,CS_AREA,DIAMETER,INNER_DIAMETER,OUTER_DIAMETER,PEAK_LOAD_KG,PEAK_LOAD_N,E_AT_PEAK_LOAD_MM,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_ANY,BREAK_LOAD_KG,E_AT_BREAK_MM,SET_LOW,GUAGE100,LOAD100_GUAGE,GUAGE200,LOAD200_GUAGE,GUAGE300,LOAD300_GUAGE,BREAK_MODE,TEMPERATURE,TEST_METHOD,DEF_POINT,DEF_LOAD,DEF_YEILD_STRG,DEF_FLG,SPAN,SUPPORT_RADIOUS,LOAD_RADIOUS,PER_STRAIN_AT_INPUT,SPEED_RPM) SELECT TEST_ID,NEW_TEST_SPE_SHAPE,NEW_TEST_THICKNESS,NEW_TEST_WIDTH,NEW_TEST_AREA,NEW_TEST_DIAMETER, NEW_TEST_INN_DIAMETER, NEW_TEST_OUTER_DIAMETER,STG_PEAK_LOAD_KG,STG_PEAK_LOAD_N,STG_E_AT_PEAK_LOAD_MM,STG_TENSILE_STRENGTH,STG_MODULUS_100,STG_MODULUS_200,STG_MODULUS_300,STG_MODULUS_ANY,STG_BREAK_LOAD_KG,STG_E_AT_BREAK_MM,STG_SET_LOW,STG_GUAGE100,STG_LOAD100_GUAGE,STG_GUAGE200,STG_LOAD200_GUAGE,STG_GUAGE300,STG_LOAD300_GUAGE,BREAK_MODE,TEMPERATURE,TEST_METHOD,DEF_POINT,DEF_LOAD,DEF_YEILD_STRG,DEF_FLG,SPAN,SUPPORT_RADIOUS,LOAD_RADIOUS,PER_STRAIN_AT_INPUT,SPEED_RPM FROM GLOBAL_VAR")
                  #cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM) SELECT X_NUM,Y_NUM FROM STG_GRAPH_MST")
                  cursor.execute("INSERT INTO GRAPH_MST(X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_MPA,Y_NUM_LB,Y_NUM_KN) SELECT X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_MPA,Y_NUM_LB,Y_NUM_KN FROM STG_GRAPH_MST")
                  
              
                  cursor.execute("UPDATE CYCLES_MST SET PRC_E_AT_BREAK= (((E_AT_BREAK_MM+GUAGE100)*100)/GUAGE100)  WHERE GRAPH_ID IS NULL")
                  cursor.execute("UPDATE CYCLES_MST SET PRC_E_AT_PEAK= (((E_AT_PEAK_LOAD_MM+GUAGE100)*100)/GUAGE100)  WHERE GRAPH_ID IS NULL")
                  
                  cursor.execute("UPDATE CYCLES_MST SET PER_STRAIN_AT_BREAK= round(((cast (E_AT_BREAK_MM as real)/ cast(SPAN as real))*100),2)  WHERE GRAPH_ID IS NULL")
                  
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
                  #FLEXURAL_MOD_KG_CM=  ((L*L*L)*F)/(4b*d*d*d*y)
                  
                  cursor.execute("UPDATE CYCLES_MST SET FLEXURAL_MOD_KG_CM=(round(((PEAK_LOAD_KG*(SELECT SPAN*0.1*SPAN*0.1*SPAN*0.1 FROM GLOBAL_VAR))/(4*WIDTH*0.1*THINCKNESS*0.1*THINCKNESS*0.1*THINCKNESS*0.1*per_strain_at_break)),2))  WHERE GRAPH_ID IS NULL")
                  #self.kg_to_lb=float(2.20462)
                  #self.mm_to_inch=float(0.0393701)
                  cursor.execute("UPDATE CYCLES_MST SET FLEXURAL_MOD_LB_INCH=(round((((PEAK_LOAD_KG*2.20462)*(SELECT SPAN*0.0393701*SPAN*0.0393701*SPAN*0.0393701 FROM GLOBAL_VAR))/(4*WIDTH*0.0393701*THINCKNESS*0.0393701*THINCKNESS*0.0393701*THINCKNESS*0.0393701*per_strain_at_break)),2))  WHERE GRAPH_ID IS NULL")
                  
                  #self.kg_to_Newton=float(9.81)
                  cursor.execute("UPDATE CYCLES_MST SET FLEXURAL_MOD_N_MM=(round((((PEAK_LOAD_KG*9.81)*(SELECT SPAN*SPAN*SPAN FROM GLOBAL_VAR))/(4*WIDTH*THINCKNESS*THINCKNESS*THINCKNESS*per_strain_at_break)),2))  WHERE GRAPH_ID IS NULL")
                  
                  #self.kgCm2_toMPA=float(0.0980665)
                  cursor.execute("UPDATE CYCLES_MST SET FLEXURAL_MOD_MPA=round((FLEXURAL_MOD_KG_CM*0.0980665),2) WHERE GRAPH_ID IS NULL")
                 
                 
                 
                 
                 
                  
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
                  cursor.execute("UPDATE TEST_MST SET LAST_UNIT_LOAD='"+str(self.last_load_unit)+"',LAST_UNIT_DISP='"+str(self.last_disp_unit)+"'  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                  
        
                  
                                                          
            connection.commit();
            connection.close()
            
            #self.pushButton_3.setDisabled(True) ### save
        
        self.load_data()
        
    def show_load_cell_val(self):        
        #self.label_34.setText(str(max(self.sc_new.arr_q)))   #load
        #self.label_36.setText(str(max(self.sc_new.arr_q)))
        #self.label_38.setText(str(max(self.sc_new.arr_p)))      
        #self.label_34.setProperty("value", str(max(self.sc_new.arr_q)))
        #self.label_40.setProperty("value",str(max(self.sc_new.arr_p)))   #length
        #self.label_34.setProperty("value", str(self.sc_new.arr_q))
        #self.label_40.setProperty("value",str(self.sc_new.arr_p))   #lengt
        
        #self.last_load_unit=str(x[0])
        #self.last_disp_unit=str(x[1])  
        if((str(self.last_load_unit) =="Kg") and (str(self.last_disp_unit) =="Mm")):
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q)))    #load
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p)))   #length
        elif((str(self.last_load_unit) =="Kg") and (str(self.last_disp_unit) =="Cm")):
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q)))    #load
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p_cm)))   #length
        elif((str(self.last_load_unit) =="Kg") and (str(self.last_disp_unit) =="Inch")):
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q)))    #load
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p_inch)))   #length
        elif((str(self.last_load_unit) =="Lb") and (str(self.last_disp_unit) =="Mm")):
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q_lb)))    #load
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p)))   #length
        elif((str(self.last_load_unit) =="Lb") and (str(self.last_disp_unit) =="Cm")):
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q_lb)))    #load
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p_cm)))   #length
        elif((str(self.last_load_unit) =="Lb") and (str(self.last_disp_unit) =="Inch")):
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q_lb)))     #load
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p_inch)))  #length
        elif((str(self.last_load_unit) =="N") and (str(self.last_disp_unit) =="Mm")):
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q_n)))     #load
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p)))  #length
        elif((str(self.last_load_unit) =="N") and (str(self.last_disp_unit) =="Cm")):
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q_n)))     #load
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p_cm)))  #length
        elif((str(self.last_load_unit) =="N") and (str(self.last_disp_unit) =="Inch")):
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q_n)))     #load
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p_inch)))  #length
        elif((str(self.last_load_unit) =="KN") and (str(self.last_disp_unit) =="Mm")):
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q_kn)))     #load
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p)))  #length
        elif((str(self.last_load_unit) =="MPa") and (str(self.last_disp_unit) =="Mm")):
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q_n)))     #load
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p)))  #length
                                    
        else:
                                    self.label_34.setProperty("value", str(max(self.sc_new.arr_q)))
                                    self.label_40.setProperty("value",str(max(self.sc_new.arr_p)))   #length
        if(str(self.sc_new.save_data_flg) =="Yes"):
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
        #self.label_26.setText(str(rows[0][0])) #cycle number
     
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_SPE_SHAPE,IFNULL(NEW_TEST_THICKNESS,0),IFNULL(NEW_TEST_WIDTH,0),NEW_TEST_DIAMETER,NEW_TEST_INN_DIAMETER,NEW_TEST_OUTER_DIAMETER,NEW_TEST_AREA,TEST_ID,STG_PEAK_LOAD_KG,STG_E_AT_PEAK_LOAD_MM,STG_LOAD_CELL_NO,STG_ENCO_EXT_FLG,NEW_TEST_JOB_NAME,NEW_TEST_BATCH_ID,NEW_TEST_NAME,IFNULL(SPAN,0),IFNULL(SUPPORT_RADIOUS,0),IFNULL(LOAD_RADIOUS,0),IFNULL(PER_STRAIN_AT_INPUT,0),IFNULL(SPEED_RPM,0) FROM GLOBAL_VAR")
        rows=results.fetchall()
        connection.close()        
        self.shape=rows[0][0]
        self.label_27.setText(self.shape) ###shap
        self.label_22.setText(str(rows[0][15])) ##SUPPORT_RADIOUS
        self.label_32.setText(str(rows[0][16])) ##LOAD_RADIOUS
        self.label_24.setText(str(rows[0][17])) 
        self.lineEdit_3_1.setText(str(rows[0][18])) ##PER_STRAIN_AT_BREAK
        self.label_26.setText(str(rows[0][19])) 
        
        if (int(self.label_26.text()) > 0):
                    self.label_36.setText(str(round(rows[0][8],2)))
                    self.label_38.setText(str(round(rows[0][9],2)))           
            #self.label_34.setProperty("value", str(rows[0][8]))#load
            #self.label_40.setProperty("value",str(rows[0][9]))   #length 
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
        else:
           print("Invalid Shape")
        
        if(str(rows[0][14])=="Compress"):
            #self.show_grid_data_compress()
            self.show_grid_data_flexure()
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
            self.show_grid_data()
            self.label_28.show()
            #self.label_30.show()
            #self.lineEdit_3.show()
            self.lineEdit_2.show()
        self.radioButton_4.setChecked(True)
        self.on_change_input_strain()
        
        
    def create_pdf_flexural(self):
        self.length=0
        self.remark=""
        
       
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,A.MOTOR_SPEED as test_speed,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime'),A.TEMPERATURE, A.TESTED_BY  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Shape:",str(x[9])],["Test Type:",str(x[3]),"Details:",str(x[8])],["Party Name :",str(x[7]),"Test Speed (mm/min) :",str(x[5])],[" Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", str(x[13])," Temp.(C) :",str(x[12])]]
            self.length=str(x[6])        
        connection.close()
        
        #### Header 1 
        
        if(self.last_load_unit == "MPa" and self.last_disp_unit=="Mm"):
             data2= [ ['Spec. \n No', 'Length \n (Mm)','Thickness  \n (Mm)','Width  \n (Mm)','Support \n Span  \n (Mm)','Max.\n Displ. \n (Mm)', 'Force  \n @  Peak\n (N)', 'Flexural \n Strength \n (MPa)','Flexural \n Modulus \n','Flexural \n Strain \n at Break (%)','Flexural \n Strain \n at Input (%)']]
        elif(self.last_load_unit == "Kg" and self.last_disp_unit=="Mm"):
             self.length=float(int(self.length))
             data2= [ ['Spec. \n No', 'Length \n (Mm)','Thickness  \n (Mm)','Width  \n (Mm)','Support \n Span  \n (Mm)','Max.\n Displ. \n (Mm)', 'Force  \n @  Peak\n (Kgf)', 'Flexural \n Strength \n (Kgf/cm2)','Flexural \n Modulus \n','Flexural \n Strain \n at Break (%)','Flexural \n Strain \n at Input (%)']]
        else:    
             data2= [ ['Spec. \n No', 'Length \n ('+str(self.last_disp_unit)+')','Thickness  \n ('+str(self.last_disp_unit)+')','Width  \n ('+str(self.last_disp_unit)+')','Support \n Span  \n ('+str(self.last_disp_unit)+')','Max.\n Displ. \n ('+str(self.last_disp_unit)+')', 'Force  \n @  Peak\n ('+str(self.last_load_unit)+')', 'Flexural \n Strength \n ('+str(self.last_load_unit)+'/'+str(self.last_disp_unit)+'2)','Flexural \n Modulus \n','Flexural \n Strain \n at Break (%)','Flexural \n Strain \n at Input (%)']]
        
        ###### Data 1
        
        if(self.last_load_unit == "MPa" and self.last_disp_unit=="Mm"):
                connection = sqlite3.connect("tyr.db")
                print("SELECT CYCLE_NUM,"+str(self.length)+",printf(\"%.2f\", A.THINCKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.2f\", A.SPAN),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM),printf(\"%.4f\", A.PEAK_LOAD_N),printf(\"%.2f\", A.FLEXURAL_STRENGTH_MPA),printf(\"%.2f\", A.flexural_mod_mpa),printf(\"%.2f\", A.per_strain_at_break),printf(\"%.2f\", A.per_strain_at_input) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                
                results=connection.execute("SELECT CYCLE_NUM,"+str(self.length)+",printf(\"%.2f\", A.THINCKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.2f\", A.SPAN),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM),printf(\"%.4f\", A.PEAK_LOAD_N),printf(\"%.2f\", A.FLEXURAL_STRENGTH_MPA),printf(\"%.2f\", A.flexural_mod_mpa),printf(\"%.2f\", A.per_strain_at_break),printf(\"%.2f\", A.per_strain_at_input) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'AVG',"+str(self.length)+",printf(\"%.2f\", avg(A.THINCKNESS)),printf(\"%.2f\", avg(A.WIDTH)),printf(\"%.2f\", avg(A.SPAN)),printf(\"%.2f\", avg(A.E_AT_PEAK_LOAD_MM)),printf(\"%.4f\", avg(A.PEAK_LOAD_N)),printf(\"%.2f\", avg(A.FLEXURAL_STRENGTH_MPA)),printf(\"%.2f\", avg(A.flexural_mod_mpa)),printf(\"%.2f\", avg(A.per_strain_at_break)),printf(\"%.2f\", avg(A.per_strain_at_input)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MAX',"+str(self.length)+",printf(\"%.2f\", max(A.THINCKNESS)),printf(\"%.2f\", max(A.WIDTH)),printf(\"%.2f\", max(A.SPAN)),printf(\"%.2f\", max(A.E_AT_PEAK_LOAD_MM)),printf(\"%.4f\", max(A.PEAK_LOAD_N)),printf(\"%.2f\", max(A.FLEXURAL_STRENGTH_MPA)),printf(\"%.2f\", max(A.flexural_mod_mpa)),printf(\"%.2f\", max(A.per_strain_at_break)),printf(\"%.2f\", max(A.per_strain_at_input)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MIN',"+str(self.length)+",printf(\"%.2f\", min(A.THINCKNESS)),printf(\"%.2f\", min(A.WIDTH)),printf(\"%.2f\", min(A.SPAN)),printf(\"%.2f\", min(A.E_AT_PEAK_LOAD_MM)),printf(\"%.4f\", min(A.PEAK_LOAD_N)),printf(\"%.2f\", min(A.FLEXURAL_STRENGTH_MPA)),printf(\"%.2f\", min(A.flexural_mod_mpa)),printf(\"%.2f\", min(A.per_strain_at_break)),printf(\"%.2f\", min(A.per_strain_at_input)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
            
        elif(self.last_load_unit == "Kg" and self.last_disp_unit=="Mm"):
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT CYCLE_NUM,"+str(self.length)+",printf(\"%.2f\", A.THINCKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.2f\", A.SPAN),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM),printf(\"%.4f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.FLEXURAL_STRENGTH*100),printf(\"%.2f\", A.flexural_mod_kg_cm),printf(\"%.2f\", A.per_strain_at_break),printf(\"%.2f\", A.per_strain_at_input) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'AVG',"+str(self.length)+",printf(\"%.2f\", avg(A.THINCKNESS)),printf(\"%.2f\", avg(A.WIDTH)),printf(\"%.2f\", avg(A.SPAN)),printf(\"%.2f\", avg(A.E_AT_PEAK_LOAD_MM)),printf(\"%.4f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg(A.FLEXURAL_STRENGTH*100)),printf(\"%.2f\", avg(A.flexural_mod_kg_cm)),printf(\"%.2f\", avg(A.per_strain_at_break)),printf(\"%.2f\", avg(A.per_strain_at_input)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MAX',"+str(self.length)+",printf(\"%.2f\", max(A.THINCKNESS)),printf(\"%.2f\", max(A.WIDTH)),printf(\"%.2f\", max(A.SPAN)),printf(\"%.2f\", max(A.E_AT_PEAK_LOAD_MM)),printf(\"%.4f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max(A.FLEXURAL_STRENGTH*100)),printf(\"%.2f\", max(A.flexural_mod_kg_cm)),printf(\"%.2f\", max(A.per_strain_at_break)),printf(\"%.2f\", max(A.per_strain_at_input)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MIN',"+str(self.length)+",printf(\"%.2f\", min(A.THINCKNESS)),printf(\"%.2f\", min(A.WIDTH)),printf(\"%.2f\", min(A.SPAN)),printf(\"%.2f\", min(A.E_AT_PEAK_LOAD_MM)),printf(\"%.4f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\", min(A.FLEXURAL_STRENGTH*100)),printf(\"%.2f\", min(A.flexural_mod_kg_cm)),printf(\"%.2f\", min(A.per_strain_at_break)),printf(\"%.2f\", min(A.per_strain_at_input)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
        else:
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT CYCLE_NUM,"+str(self.length)+",printf(\"%.2f\", A.THINCKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.2f\", A.SPAN),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM),printf(\"%.4f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.FLEXURAL_STRENGTH*100),printf(\"%.2f\", A.flexural_mod_kg_cm),printf(\"%.2f\", A.per_strain_at_break),printf(\"%.2f\", A.per_strain_at_input) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'AVG',"+str(self.length)+",printf(\"%.2f\", avg(A.THINCKNESS)),printf(\"%.2f\", avg(A.WIDTH)),printf(\"%.2f\", avg(A.SPAN)),printf(\"%.2f\", avg(A.E_AT_PEAK_LOAD_MM)),printf(\"%.4f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg(A.FLEXURAL_STRENGTH_LB_INCH)),printf(\"%.2f\", avg(A.flexural_mod_lb_inch)),printf(\"%.2f\", avg(A.per_strain_at_break)),printf(\"%.2f\", avg(A.per_strain_at_input)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MAX',"+str(self.length)+",printf(\"%.2f\", max(A.THINCKNESS)),printf(\"%.2f\", max(A.WIDTH)),printf(\"%.2f\", max(A.SPAN)),printf(\"%.2f\", max(A.E_AT_PEAK_LOAD_MM)),printf(\"%.4f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max(A.FLEXURAL_STRENGTH_LB_INCH)),printf(\"%.2f\", max(A.flexural_mod_lb_inch)),printf(\"%.2f\", max(A.per_strain_at_break)),printf(\"%.2f\", max(A.per_strain_at_input)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MIN',"+str(self.length)+",printf(\"%.2f\", min(A.THINCKNESS)),printf(\"%.2f\", min(A.WIDTH)),printf(\"%.2f\", min(A.SPAN)),printf(\"%.2f\", min(A.E_AT_PEAK_LOAD_MM)),printf(\"%.4f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\", min(A.FLEXURAL_STRENGTH_LB_INCH)),printf(\"%.2f\", min(A.flexural_mod_lb_inch)),printf(\"%.2f\", min(A.per_strain_at_break)),printf(\"%.2f\", min(A.per_strain_at_input)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data2.append(x)
                connection.close()
       
       
       
       
       
       
        
        if(self.last_load_unit == "MPa" and self.last_disp_unit=="Mm"):
                data3= [ ['Spec. \n No', 'Test Speed \n (mm/min)', 'Load Radious \n (Mm)','Support Radious \n (Mm)','Failure \n Mode','Test \n Method']]        
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", A.speed_rpm),printf(\"%.2f\", A.load_radious),printf(\"%.2f\", A.support_radious),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(A.speed_rpm)),printf(\"%.2f\", avg(A.load_radious)),printf(\"%.2f\", avg(A.support_radious)),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(A.speed_rpm)),printf(\"%.2f\", max(A.load_radious)),printf(\"%.2f\", max(A.support_radious)),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(A.speed_rpm)),printf(\"%.2f\", min(A.load_radious)),printf(\"%.2f\", min(A.support_radious)),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()
            
        elif(self.last_load_unit == "Kg" and self.last_disp_unit=="Mm"):   
        
                data3= [ ['Spec. \n No', 'Test Speed \n (mm/min)', 'Load Radious \n (Mm)','Support Radious \n (Mm)','Failure \n Mode','Test \n Method']]        
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", A.speed_rpm),printf(\"%.2f\", A.load_radious),printf(\"%.2f\", A.support_radious),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(A.speed_rpm)),printf(\"%.2f\", avg(A.load_radious)),printf(\"%.2f\", avg(A.support_radious)),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(A.speed_rpm)),printf(\"%.2f\", max(A.load_radious)),printf(\"%.2f\", max(A.support_radious)),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(A.speed_rpm)),printf(\"%.2f\", min(A.load_radious)),printf(\"%.2f\", min(A.support_radious)),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()
       
        else:
                data3= [ ['Spec. \n No', 'Test Speed \n (mm/min)', 'Load Radious \n ('+str(self.last_disp_unit)+')','Support Radious \n ('+str(self.last_disp_unit)+')','Failure \n Mode','Test \n Method']]        
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", A.speed_rpm),printf(\"%.2f\", A.load_radious),printf(\"%.2f\", A.support_radious),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(A.speed_rpm)),printf(\"%.2f\", avg(A.load_radious)),printf(\"%.2f\", avg(A.support_radious)),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(A.speed_rpm)),printf(\"%.2f\", max(A.load_radious)),printf(\"%.2f\", max(A.support_radious)),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(A.speed_rpm)),printf(\"%.2f\", min(A.load_radious)),printf(\"%.2f\", min(A.support_radious)),A.BREAK_MODE,A.TEST_METHOD FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                        data3.append(x)
                connection.close()


        
        y=300
        Elements=[]
        
        
        
        
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
        comments = Paragraph("Remark : ______________________________________________________________________________", styles["Normal"])
        
        footer_2= Paragraph("Authorised and Signed By : _________________.", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
       
        
     
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f4=Table(data3)
        f4.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
         
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),f4,Spacer(1,12),comments,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        doc = SimpleDocTemplate('./reports/test_report.pdf', rightMargin=10,
                                leftMargin=30,
                                topMargin=20,
                                bottomMargin=20,)
        doc.build(Elements)
        #print("Done")
        
    def open_pdf(self):
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)    
        self.create_pdf_flexural()
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
        #print(" test_id :"+str(self.test_id))  
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
        
        
        
class PlotCanvas_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=5, height=4, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="Tensile"
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME,TEST_ID,NEW_TEST_JOB_NAME,NEW_TEST_BATCH_ID ,(SELECT COUNT(CYCLE_ID)+1 as x FROM CYCLES_MST B WHERE B.TEST_ID = TEST_ID) as CycleNo   FROM GLOBAL_VAR") 
        for x in results:
             self.test_type=str(x[0])
             self.axes.set_title("Test Id="+str(x[1])+", Cycle No="+str(x[4])+", Job Name="+str(x[2])+", Batch Id="+str(x[3]))  
        connection.close()
        
        if(self.test_type=="Compress"):
            self.axes.set_xlabel('Compression (mm)')        
        else:        
            self.axes.set_xlabel('Displacement (mm)')
          
        self.axes.set_ylabel('Load (Kgf)') 
        self.axes.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p1 =0
        self.p =0
        self.p_cm =0
        self.p_inch =0
        
        self.q =0
        self.q_n =0
        self.q_lb =0
        self.q_kn =0
        self.q_mpa =0
        self.kg_cm2=0
        
        self.arr_p1=[0.0]
        self.arr_p=[0.0]
        self.arr_p_cm=[0.0]
        self.arr_p_inch=[0.0]
        
        self.arr_q1=[0.0]
        self.arr_q=[0.0]
        self.arr_q_n=[0.0]
        self.arr_q_lb=[0.0]
        self.arr_q_kn=[0.0]
        self.arr_q_mpa=[0.0]
        
        self.speed=500
        self.arr_speed=[0.0]
       
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
        
        self.load_unit=""
        self.disp_unit=""
        self.cs_area_cm=""
        
        self.test_method=-1
        self.load_cell_no=-1
        
        
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
   
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)       
        
        
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                cursor = connection.cursor()                            
                cursor.execute("DELETE FROM STG_GRAPH_MST ")
                cursor.execute("DELETE FROM MODBUS_LOGS ") 
        connection.commit();
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_LOAD_UNIT,LAST_DISP_UNIT,GRAPH_TYPE from GLOBAL_VAR2") 
        for x in results:
                        self.load_unit=str(x[0])
                        self.disp_unit=str(x[1])
                        self.graph_type=str(x[2])  
        connection.close()
                        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,IFNULL(NEW_TEST_AREA*0.1*0.1,0),TEST_ID,STG_CYCLE_ID,LOGIN_USER_ROLE,NEW_TEST_MOTOR_SPEED,NEW_TEST_MOTOR_REV_SPEED from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=int(x[0])             
             self.max_load=int(x[2])             
             self.max_length=float(x[3])
             self.flex_max_length=float(x[3])
             self.cof_max_length=float(x[4])            
             print("Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
             self.unit_type=str(x[5])
             self.cs_area_cm=str(x[6])
             self.test_id=str(x[7])
             self.cycle_num=str(x[8])
             self.login_user_role=str(x[9])
             self.test_method=2 ### Test Type Set For Compression here.
             self.load_cell_no=1
             self.guage_length=self.test_guage_mm             
             self.test_speed=str(x[10])
             self.test_rev_speed=str(x[11])
        connection.close()
        print(" xxx     gfgf self.test_type:"+str(self.test_type))
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE,ISACTIVE_MODBUS,MODBUS_PORT,NON_MODBUS_PORT from SETTING_MST") 
        for x in results:
             self.axes.set_xlim(0,int(x[0]))
             self.axes.set_ylim(0,int(x[1]))
             self.flexural_max_load=int(x[1])
             print("inside setting mst ...self.flexural_max_load : "+str(self.flexural_max_load))
             self.xlim=int(x[0])
             self.ylim=int(x[1])
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
             self.modbus_flag=str(x[4])
             self.modbus_port=str(x[5])
             self.non_modbus_port=str(x[6])
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_LOAD_UNIT,LAST_DISP_UNIT from GLOBAL_VAR2") 
        for x in results:
                        self.load_unit=str(x[0])
                        self.disp_unit=str(x[1])
        connection.close()
        self.graph_type="Load Vs Compression" #This is Fixed
        if(self.graph_type=="Load Vs Compression"):
                    if(self.load_unit=="Kg" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Displacement (Mm)')
                                             self.axes.set_ylabel('Load (Kg)')
                    elif(self.load_unit=="Kg" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Displacement (Inch)')
                                             self.axes.set_ylabel('Load (Kg)')
                    elif(self.load_unit=="Kg" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Displacement (Cm)')
                                             self.axes.set_ylabel('Load (Kg)')                                                               
                    elif(self.load_unit=="Lb" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Displacement (Mm)')
                                             self.axes.set_ylabel('Load (Lb)')
                    elif(self.load_unit=="Lb" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Displacement (Cm)')
                                             self.axes.set_ylabel('Load (Lb)') 
                    elif(self.load_unit=="Lb" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Displacement (Inch)')
                                             self.axes.set_ylabel('Load (Lb)')                                                         
                    elif(self.load_unit=="N" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Displacement (Mm)')
                                             self.axes.set_ylabel('Load (N)')                                                         
                    elif(self.load_unit=="N" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Displacement (Cm)')
                                             self.axes.set_ylabel('Load (N)')                                 
                    elif(self.load_unit=="N" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Displacement (Inch)')
                                             self.axes.set_ylabel('Load (N)')
                    elif(self.load_unit=="KN" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Displacement (Mm)')
                                             self.axes.set_ylabel('Load (KN)')                                                         
                    elif(self.load_unit=="KN" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Displacement (Cm)')
                                             self.axes.set_ylabel('Load (KN)')                                 
                    elif(self.load_unit=="KN" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Displacement (Inch)')
                                             self.axes.set_ylabel('Load (KN)')
                    elif(self.load_unit=="MPa" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Displacement (Mm)')
                                             self.axes.set_ylabel('Load (N)') 
                    else:    
                                             self.axes.set_xlabel('Displacement (Mm)')
                                             self.axes.set_ylabel('Load (Kg)')
        
        elif(self.graph_type=="Stress Vs Strain"):
                                         print("inside sadasdasd")
                                         self.axes.set_xlabel('Strain (%)')
                                         self.axes.set_ylabel("Stress (MPa)'") 
                 
        else:
                       print("Invalid Graph Type")
                       
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(NEW_TEST_AREA*0.1*0.1,0) from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=int(x[0])
             if(str(x[1]) == "Flexural"):
                 self.test_type="Compress"
             else:
                  self.test_type=str(x[1])
             self.max_load=int(x[2])
             #self.max_load=100
             #self.max_length=float(float(x[0])-float(x[3]))
             if(float(x[3]) > float(x[0])):
                  self.max_length=float(float(x[3]) - float(x[0]))
             else:
                  self.max_length=float(float(x[0]) - float(x[3]))
             
             
             self.flex_max_length=float(x[3])
             #self.max_load=str(self.max_load).zfill(5)
             self.max_length=str(int(self.max_length)).zfill(5)
             #self.max_length=float(x[3])
             print("Max Load :"+str(self.max_load).zfill(5)+" Max length :"+str(int(self.max_length)).zfill(5))
             self.cs_area_cm=str(x[4])
        connection.close()
        
###### Set Modbus register for Test   ##########
#         self.test_method=1
#         self.load_cell_no=1
#         self.guage_length=11.20
#         self.max_load=61.10
#         self.max_length=67.03
#         self.breaking_sence=1
#         self.test_speed=400
        
        try:
                #instrument = minimalmodbus.Instrument('/dev/ttyACM0', 7,debug = True) # port name, slave address (in decimal)                   
                self.instrument = minimalmodbus.Instrument('/dev/ttyACM0', 7) # port name, slave address (in decimal)
                self.instrument.serial.timeout = 1
                self.instrument.serial.baudrate = 115200
                #time.sleep(5)
                self.IO_error_flg=0
        except IOError as e:
                print("IO Errors- Connection to Modbus......:"+str(e))
                self.IO_error_flg=1
        
        if(self.IO_error_flg==0):
                    try:
                        #self.instrument.write_register(REGISTER, NEW_VALUE, DECIMALS, functioncode=6, signed=True)    
                        print("\n\n\n\n##### SET : TEST_METHOD ######")
                        self.instrument.write_register(0,int(self.test_method),0,6)                    
                        self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET Test Method :"+str(self.test_method),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- Test Method..:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET Test Method :"+str(self.test_method),self.login_user_role)
                       
                    try:
                        print("\n\n\n\n##### SET : LOAD CELL NUMBER ######")
                        self.instrument.write_register(1,int(self.load_cell_no),0,6)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET Load Cell Number :"+str(self.load_cell_no),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- Load Cell Number.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET Load Cell Number :"+str(self.load_cell_no),self.login_user_role)
                       
                    
                    try:
                        print("\n\n\n\n##### SET : guage_length ######")
                        self.instrument.write_float(2,float(self.guage_length),2)
                        #self.instrument.write_register(6,0,0)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET guage_length :"+str(self.guage_length),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- self.guage_length.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET guage_length :"+str(self.guage_length),self.login_user_role)
                            time.sleep(5)
                    
                    try:
                        print("\n\n\n\n##### SET : MAX LOAD ######")
                        self.instrument.write_float(4,float(self.max_load),2)
                        #self.instrument.write_register(6,0,0)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET MAX. Load :"+str(self.max_load),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- self.max_load.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET MAX. Load :"+str(self.max_load),self.login_user_role)
                            time.sleep(5)
                            
                    
                    try:
                        print("\n\n\n\n##### SET : max_length ######")
                        self.instrument.write_float(6,float(self.max_length),2)
                        #self.instrument.write_register(6,0,0)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET max_length :"+str(self.max_length),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- self.max_length.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET max_length :"+str(self.max_length),self.login_user_role)
                            time.sleep(5)
                            
                    try:
                        print("\n\n\n\n##### SET : Breaking Sence Or SET LOW ######")
                        self.instrument.write_float(8,float(self.break_sence),2)
                        #self.instrument.write_register(6,0,0)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET Breaking Sence :"+str(self.break_sence),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- break_sence.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET breaking_sence :"+str(self.break_sence),self.login_user_role)
                            time.sleep(5)
                            
                    
                    try:
                        print("\n\n\n\n##### SET : test_speed ######")
                        self.instrument.write_float(10,float(self.test_speed),2)
                        #self.instrument.write_register(6,0,0)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET test_speed :"+str(self.test_speed),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- self.test_speed.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET test_speed :"+str(self.test_speed),self.login_user_role)
                            time.sleep(5)
                    
                    try:
                        print("\n\n\n\n##### SET : test_rev_speed ######")
                        self.instrument.write_float(12,float(self.test_rev_speed),2)
                        #self.instrument.write_register(6,0,0)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET test_rev_speed :"+str(self.test_rev_speed),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- self.test_rev_speed.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET test_rev_speed :"+str(self.test_rev_speed),self.login_user_role)
                            time.sleep(5)
                    
                    try:
                        print("\n\n\n\n##### SET : auto_rev_time_off ######")
                        self.instrument.write_float(14,float(self.auto_rev_time_off),2)
                        #self.instrument.write_register(6,0,0)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET auto_rev_time_off :"+str(self.auto_rev_time_off),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- self.auto_rev_time_off.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET auto_rev_time_off :"+str(self.auto_rev_time_off),self.login_user_role)
                            time.sleep(5)
                    
                    
                    time.sleep(1)
                    self.test_method=-1
                    self.load_cell_no=-1
                    self.guage_length=-1
                    self.max_load=-1
                    self.max_length=-1
                    self.break_sence=-1
                    self.test_speed=-1
                    self.test_rev_speed=-1
                    self.auto_rev_time_off=-1
                    
                    try:
                        ##read_register( Register number, number of decimals, function code)
                        ##read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) → float[source]
                        print("\n\n\n\n##### GET  : TEST_METHOD ######")
                        self.test_method=self.instrument.read_register(0,0,3)                              
                        self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET Test Method :"+str(self.test_method),self.login_user_role)
                        #time.sleep(5)                        
                    except IOError as e:
                            print("Ignore-Modbus Error- Get Test Method.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET Test Method :"+str(self.test_method),self.login_user_role)
                            self.IO_error_flg=1
                            time.sleep(5)
                    
                    try:
                        print("\n\n\n\n##### GET  : LOAD CELL NUMBER ######")
                        self.load_cell_no=self.instrument.read_register(1,0,3)                               
                        self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET Load Cell Number :"+str(self.load_cell_no),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- Get Load Cell Number.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET Load Cell Number :"+str(self.load_cell_no),self.login_user_role)                
                            self.IO_error_flg=1
                            time.sleep(5)
                            
                    
                    try:
                        print("\n\n\n\n##### GET  : guage_length ######")
                        ##read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) → float[source]   
                        self.guage_length=self.instrument.read_float(2,3,2)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET guage_length :"+str(self.guage_length),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- Get guage_length.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET guage_length :"+str(self.guage_length),self.login_user_role)                
                            self.IO_error_flg=1
                            time.sleep(5)
                            
                    try:
                        print("\n\n\n\n##### GET  : MAX LOAD ######")
                        ##read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) → float[source]   
                        self.max_load=self.instrument.read_float(4,3,2)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET max_load :"+str(self.max_load),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- Get max_load.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET max_load :"+str(self.max_load),self.login_user_role)                
                            self.IO_error_flg=1
                            time.sleep(5)
                            
                    
                    try:
                        print("\n\n\n\n##### GET  : max_length ######")
                        ##read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) → float[source]   
                        self.max_length=self.instrument.read_float(6,3,2)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET max_length :"+str(self.max_length),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- Get max_length.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET max_length :"+str(self.max_length),self.login_user_role)                
                            self.IO_error_flg=1
                            time.sleep(5)
                            
                    
                    try:
                        print("\n\n\n\n##### GET  : break_sence ######")
                        ##read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) → float[source]   
                        self.break_sence=self.instrument.read_float(8,3,2)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET break_sence :"+str(self.break_sence),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- Get break_sence:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET break_sence :"+str(self.break_sence),self.login_user_role)                
                            self.IO_error_flg=1
                            time.sleep(5)
                            
                    try:
                        print("\n\n\n\n##### GET  : test_speed ######")
                        ##read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) → float[source]   
                        self.test_speed=self.instrument.read_float(10,3,2)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET test_speed :"+str(self.test_speed),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- Get test_speed:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET test_speed :"+str(self.test_speed),self.login_user_role)                
                            self.IO_error_flg=1
                            time.sleep(5)
                    
                    try:
                        print("\n\n\n\n##### GET  : test_rev_speed ######")
                        ##read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) → float[source]   
                        self.test_speed=self.instrument.read_float(12,3,2)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET test_rev_speed :"+str(self.test_rev_speed),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- Get test_rev_speed:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET test_rev_speed :"+str(self.test_rev_speed),self.login_user_role)                
                            self.IO_error_flg=1
                            time.sleep(5)
                    
                    try:
                        print("\n\n\n\n##### GET  : auto_rev_time_off ######")
                        ##read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) → float[source]   
                        self.test_speed=self.instrument.read_float(12,3,2)
                        self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET auto_rev_time_off :"+str(self.auto_rev_time_off),self.login_user_role)
                        #time.sleep(5)
                    except IOError as e:
                            print("Ignore-Modbus Error- Get auto_rev_time_off:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET auto_rev_time_off :"+str(self.auto_rev_time_off),self.login_user_role)                
                            self.IO_error_flg=1
                            time.sleep(5)
                            
                            
                    
        else:
            print("Modbus Communication Error.... ")
         
        time.sleep(1)
        self.start_bit=0   #Default value
        self.is_stopped=-1
        if(self.IO_error_flg==0):
            ####### Start Test-Read Coil Register. ############
            try:
                print("\n\n\n\n##### GET -VERIFY CURENT STATUS : COIL start_bit ######")
                #read_bit(registeraddress: int, functioncode: int = 2) → int
                self.is_stopped=self.instrument.read_register(1,0,4)
                self.is_stopped=round(self.is_stopped,0)
                self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET Status (1=Running,2=Hold,3=Reverse):"+str(self.is_stopped),self.login_user_role)
                #time.sleep(5)                
            except IOError as e:                    
                print("Ignore-Modbus Error- Get start_bit.:"+str(e))
                self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET start_bit :"+str(self.start_bit),self.login_user_role)                
                self.IO_error_flg=1
            if((self.is_stopped == 0) or (self.is_stopped == 3)):     
                        ####### Start Test-Write in Coil Register. ############
                        try:
                             #write_bit(registeraddress: int, value: int, functioncode: int = 5) → None[source]   
                             print("\n\n\n\n##### SET :COIL start_bit ######")
                             self.instrument.write_bit(0,1,5)                    
                             self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET Test start_bit :1",self.login_user_role)
                              #time.sleep(5)
                        except IOError as e:
                             print("Ignore-Modbus Error- SET COIL start_bit..:"+str(e))
                             self.record_modbus_logs(self.test_id,self.cycle_num,"SET","SET start_bit :"+str(self.start_bit),self.login_user_role)
                             self.IO_error_flg=1                       
             
                        ####### Start Test-Read Coil Register. ############
                        try:
                            print("\n\n\n\n##### GET  : COIL start_bit ######")
                            #read_bit(registeraddress: int, functioncode: int = 2) → int
                            self.start_bit=self.instrument.read_bit(0,1)
                            self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET start_bit :"+str(self.start_bit),self.login_user_role)
                            #time.sleep(5)                
                        except IOError as e:                    
                            print("Ignore-Modbus Error- Get start_bit.:"+str(e))
                            self.record_modbus_logs(self.test_id,self.cycle_num,"GET","GET start_bit :"+str(self.start_bit),self.login_user_role)                
                            self.IO_error_flg=1
            else:
                print("Test is already running......")
                
 
        else:
                  print("Test Not Started.")
        if(self.IO_error_flg==1):       
                    print("Could not Start Test Beacuse of MODBUS IO Error.......")
        else:
                    self.save_data_flg="No"
                    print("Started Test ....call read. input register.")
                    self.timer1.setInterval(1000)     
                    self.timer1.timeout.connect(self.update_graph)
                    self.timer1.start(1)
                    self.on_ani_start()
    
    def update_graph(self):       
        if(self.save_data_flg=="No"):            
            try:
                ##### Read all Input Ragisters ########
                self.load_cell_number=1
                self.extiometer=1
                self.encoder=0
                self.p=-1
                self.q=-1
                self.is_stopped=-1
                try:
                    ##read_float(registeraddress: int, functioncode: int = 3, number_of_registers: int = 2, byteorder: int = 0) → float[source]                                    
                    self.p=self.instrument.read_float(7,4,2)
                    self.p=round(self.p,3)
                    self.q=self.instrument.read_float(3,4,2)
                    self.q=round(self.q,3)
                    ##read_register( Register number, number of decimals, function code)
                    self.is_stopped=self.instrument.read_register(1,0,4)
                    round(self.is_stopped,0)
                    print("self.p= :"+str(round(self.p,2))+" self.q :"+str(round(self.q,2))+"  self.is_stopped  :"+str(self.is_stopped))
                except IOError:
                    print("IO Errors- Reading Input Register......update graph")
                    self.IO_error_flg=1
                
                if(self.is_stopped==1): # Running
                        self.p_cm=float(self.p)/10
                        self.arr_p_cm.append(float(self.p_cm))
                        
                        self.p_inch=float(self.p)*0.0393701
                        self.arr_p_inch.append(float(self.p_inch))
                        
                        self.q_n=float(self.q)*9.81
                        self.arr_q_n.append(float(self.q_n))
                        
                        self.q_lb=float(self.q)*2.20462
                        self.arr_q_lb.append(float(self.q_lb))
                        
                        self.q_kn=float(self.q_n)/1000
                        self.arr_q_kn.append(float(self.q_kn))
                        
                        self.kg_cm2=float(self.q)/float(self.cs_area_cm)
                        self.q_mpa=float(self.kg_cm2)*0.0980665
                        self.arr_q_mpa.append(float(self.q_mpa))
                        
                        
                        self.arr_speed.append(float(self.speed))
                        
                        self.arr_p.append(float(self.p))
                        self.arr_q.append(float(self.q))
                        
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
                        #self.is_stopped=0 ### Read stop flag
                        if(int(self.is_stopped) == 3):                    
                            self.save_data_flg="Yes"
                            self.on_ani_stop()
                        elif(int(self.is_stopped) == 2):                            
                            print("Testing Stopped.......")
                        else:
                            print("Invalid is stopped flag.......")
            except IOError:
                print("Stopped !!!!!!")
                if(self.is_stopped==3):                    
                    self.save_data_flg="Yes"
                    self.on_ani_stop()
                
    #self.record_modbus_logs(self.test_id,self.cycle_num,"SET","Login into to System.",self.login_user_role)
    def record_modbus_logs(self,test_id,cycle_num,set_or_get,log_str,user_name):
        connection = sqlite3.connect("tyr.db")
        with connection:        
            cursor = connection.cursor()
            print("INSERT INTO MODBUS_LOGS(TEST_ID,CYCLE_NUM,SET_OR_GET,LOG_STR,USER_NAME) VALUES(?,?,?,?,?)",(test_id,cycle_num,set_or_get,log_str,user_name))
            cursor.execute("INSERT INTO MODBUS_LOGS(TEST_ID,CYCLE_NUM,SET_OR_GET,LOG_STR,USER_NAME) VALUES(?,?,?,?,?)",(test_id,cycle_num,set_or_get,log_str,user_name))                         
        connection.commit();
        connection.close()
       
         
       
                    
                
               
     
          
    def plot_grah_only(self,i):
                   if(self.graph_type=="Load Vs Compression"):
                                if(self.load_unit=="Kg" and self.disp_unit=="Mm"):
                                                    self.line_cnt.set_data(self.arr_p,self.arr_q)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="Kg" and self.disp_unit=="Cm"):
                                                    self.line_cnt.set_data(self.arr_p_cm,self.arr_q)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="Kg" and self.disp_unit=="Inch"):
                                                    self.line_cnt.set_data(self.arr_p_inch,self.arr_q)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="Lb" and self.disp_unit=="Inch"):
                                                    self.line_cnt.set_data(self.arr_p_inch,self.arr_q_lb)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="Lb" and self.disp_unit=="Cm"):
                                                    print("Lb/Cm ...")
                                                    self.line_cnt.set_data(self.arr_p_cm,self.arr_q_lb)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="Lb" and self.disp_unit=="Mm"):
                                                    self.line_cnt.set_data(self.arr_p,self.arr_q_lb)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="N" and self.disp_unit=="Mm"):
                                                    self.line_cnt.set_data(self.arr_p,self.arr_q_n)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="N" and self.disp_unit=="Cm"):
                                                    self.line_cnt.set_data(self.arr_p_cm,self.arr_q_n)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="N" and self.disp_unit=="Inch"):
                                                    self.line_cnt.set_data(self.arr_p_inch,self.arr_q_n)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="KN" and self.disp_unit=="Mm"):
                                                    self.line_cnt.set_data(self.arr_p,self.arr_q_kn)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="KN" and self.disp_unit=="Cm"):
                                                    self.line_cnt.set_data(self.arr_p_cm,self.arr_q_kn)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="KN" and self.disp_unit=="Inch"):
                                                    self.line_cnt.set_data(self.arr_p_inch,self.arr_q_kn)
                                                    return [self.line_cnt]
                                elif(self.load_unit=="MPa" and self.disp_unit=="Mm"):
                                                    self.line_cnt.set_data(self.arr_p,self.arr_q_n)  ### in case MPa there will beload in Newton only
                                                    return [self.line_cnt]
                                else:    
                                                    self.line_cnt.set_data(self.arr_p,self.arr_q)
                                                    return [self.line_cnt]
                                                    #return self.line_cnt,
                                self.line_cnt.set_data(self.arr_p,self.arr_q)
                                return [self.line_cnt]
                        #         #return self.line_cnt,
                        #         self.line_cnt.set_data(self.arr_p,self.arr_q)
                        #         return [self.line_cnt]
                        #         #return self.line_cnt,
                   elif(self.graph_type=="Stress Vs Strain"):
                            self.line_cnt.set_data(self.arr_p,self.arr_q)
                            return [self.line_cnt]
                   else:
                            print("Invalida Graph Type")
    
    
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
       
    

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=2, dpi=80):
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
        
        self.last_load_unit=""
        self.last_disp_unit=""
        self.graph_type=""
        self.cs_area_mm="1"       
        self.guage_length_mm="1"
        
        
        
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
             #ax.set_title("Test Id="+str(x[1]))
             self.graph_ids.append(x[0])             
        connection.close()
        
        ### Univarsal change for  Graphs ####################
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
             ax.set_xlim(0,int(x[0]))
             ax.set_ylim(0,int(x[1]))          
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME,TEST_ID,NEW_TEST_JOB_NAME,NEW_TEST_BATCH_ID ,(SELECT COUNT(CYCLE_ID) as x FROM CYCLES_MST B WHERE B.TEST_ID = TEST_ID) as CycleNo   FROM GLOBAL_VAR") 
        for x in results:
             self.test_type=str(x[0])
             self.axes.set_title("Test Id="+str(x[1])+", Cycle No="+str(x[4])+", Job Name="+str(x[2])+", Batch Id="+str(x[3]))  
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        
        results=connection.execute("SELECT LAST_UNIT_LOAD,LAST_UNIT_DISP,GRAPH_SCAL_X_LENGTH,CASE LAST_UNIT_LOAD WHEN 'MPa' THEN GRAPH_SCAL_Y_LOAD_N WHEN 'N' THEN GRAPH_SCAL_Y_LOAD_N WHEN 'LB' THEN GRAPH_SCAL_Y_LOAD_LB ELSE GRAPH_SCAL_Y_LOAD END  ,TEST_TYPE from TEST_MST  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ") 
        for x in results:
              self.last_load_unit=str(x[0])
              self.last_disp_unit=str(x[1])
              ax.set_xlim(0,float(x[2]))
              ax.set_ylim(0,float(x[3]))
              self.test_type=str(x[4])
        connection.close()

        
        self.graph_type="Load Vs Displacement"
        
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
        
            connection = sqlite3.connect("tyr.db")
            if(self.graph_type=="Load Vs Displacement"):
                    print("self.last_load_unit:"+str(self.last_load_unit))
                    if(self.last_load_unit=="Kg" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Kg" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Kg" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Lb" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM_LB FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Lb" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM_LB FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Lb" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_LB FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="N" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="N" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="N" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="KN" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_KN FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="KN" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM_KN FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="KN" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM_KN FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="MPa" and self.last_disp_unit=="Mm"):
                                    print("SELECT X_NUM,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                                    results=connection.execute("SELECT X_NUM,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    else:    
                                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")           
                
            else:
                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            for k in results:        
                self.x_num.append(k[0])
                self.y_num.append(k[1])
            connection.close()
        
            if(g < 8 ):
                ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
        
        
        ax.set_xlabel('Displacement ('+str(self.last_disp_unit)+')')
        if(str(self.last_load_unit) == 'MPa'):
             ax.set_ylabel('Load (N)')
        else:
             ax.set_ylabel('Load ('+str(self.last_load_unit)+')')   
        
        
        
        ax.legend()        
        self.draw()
        self.figure.savefig('last_graph.png',dpi=100)
        #ax.connect('motion_notify_event', mouse_move)

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
        self.plot_blank()
        self.last_load_unit=""
        self.last_disp_unit=""
        
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
        results=connection.execute("SELECT NEW_TEST_NAME,TEST_ID,NEW_TEST_JOB_NAME,NEW_TEST_BATCH_ID ,(SELECT COUNT(CYCLE_ID)+1 as x FROM CYCLES_MST B WHERE B.TEST_ID = TEST_ID) as CycleNo   FROM GLOBAL_VAR") 
        for x in results:
             self.test_type=str(x[0])
             self.axes.set_title("Test Id="+str(x[1])+", Cycle No="+str(x[4])+", Job Name="+str(x[2])+", Batch Id="+str(x[3]))  
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_LOAD_UNIT,LAST_DISP_UNIT from GLOBAL_VAR2") 
        for x in results:
             self.last_load_unit=str(x[0])
             self.last_disp_unit=str(x[1])  
        connection.close()
        
        ax.set_ylabel('Load (Kgf)')
        
        if(str(self.last_load_unit) == 'MPa'):
             ax.set_ylabel('Load (N)')
        else:
             ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        
        ax.set_xlabel('Displacement ('+str(self.last_disp_unit)+')')
       
        self.draw() 

    
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_02f_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
