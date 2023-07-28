from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow
from comment_popup import comment_Ui_MainWindow

import inspect

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import QTableWidgetItem

### ##### This Lib is for General Purpose.
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import datetime
import random
import serial,time
import array  as arr
import numpy as np

### This lib is for Graph only 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import re

#### PDF creation Libs ########
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY 
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import portrait,landscape, letter,inch,A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Line, Drawing
import sys
import os

class TY_54_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 769)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1321, 701))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 240, 1321, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(1160, 50, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(1170, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1170, 120, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 260, 1301, 431))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(670, 140, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setGeometry(QtCore.QRect(670, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_11.setStyleSheet("border-radius:20px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(148, 255, 166);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(670, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_12.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_13.setGeometry(QtCore.QRect(390, 370, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_13.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_14.setGeometry(QtCore.QRect(530, 370, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_14.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_14.setFlat(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_15.setGeometry(QtCore.QRect(670, 370, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_15.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_15.setFlat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_33 = QtWidgets.QLabel(self.frame_3)
        self.label_33.setGeometry(QtCore.QRect(10, 370, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("")
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        
        self.buttongroup = QtWidgets.QButtonGroup()
        self.buttongroup_2 = QtWidgets.QButtonGroup()
        
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton.setGeometry(QtCore.QRect(680, 10, 101, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setGeometry(QtCore.QRect(830, 10, 101, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        
        self.buttongroup.addButton(self.radioButton, 1)
        self.buttongroup.addButton(self.radioButton_2, 2)
        
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_3.setGeometry(QtCore.QRect(980, 10, 81, 31))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_4.setGeometry(QtCore.QRect(1090, 10, 111, 31))
        self.radioButton_4.setObjectName("radioButton_4")
        
        self.buttongroup_2.addButton(self.radioButton_3, 1)
        self.buttongroup_2.addButton(self.radioButton_4, 2)
        
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(810, 320, 471, 101))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
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
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_16.setGeometry(QtCore.QRect(670, 300, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_16.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_16.setFlat(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_39 = QtWidgets.QLabel(self.frame_3)
        self.label_39.setGeometry(QtCore.QRect(800, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("")
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame_3)
        self.label_40.setGeometry(QtCore.QRect(810, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("")
        self.label_40.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber.setGeometry(QtCore.QRect(940, 90, 261, 51))
        self.lcdNumber.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_41 = QtWidgets.QLabel(self.frame_3)
        self.label_41.setGeometry(QtCore.QRect(1230, 90, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("")
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber_2.setGeometry(QtCore.QRect(940, 170, 261, 51))
        self.lcdNumber_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_42 = QtWidgets.QLabel(self.frame_3)
        self.label_42.setGeometry(QtCore.QRect(1230, 180, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("")
        self.label_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_3)
        self.label_43.setGeometry(QtCore.QRect(790, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("")
        self.label_43.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber_3.setGeometry(QtCore.QRect(940, 250, 261, 51))
        self.lcdNumber_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_44 = QtWidgets.QLabel(self.frame_3)
        self.label_44.setGeometry(QtCore.QRect(1220, 260, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("")
        self.label_44.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_4.setGeometry(QtCore.QRect(120, 370, 191, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 641, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_49 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_49.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.gridLayout.addWidget(self.label_49, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(1170, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_8.setStyleSheet("background-color: rgb(148, 255, 166);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 190, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(70, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(140, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(310, 20, 161, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(150, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(310, 60, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(180, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(310, 180, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(130, 0, 20, 251))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(490, 0, 20, 251))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(980, 0, 20, 251))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_8)
        self.lineEdit_8.setValidator(input_validator)
        self.lineEdit_8.setGeometry(QtCore.QRect(590, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(500, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(660, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(500, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_9)
        self.lineEdit_9.setValidator(input_validator)
        self.lineEdit_9.setGeometry(QtCore.QRect(590, 70, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(660, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("")
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(800, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("")
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(900, 20, 61, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(740, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("")
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(900, 70, 61, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")      
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(1140, 0, 20, 251))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(990, 70, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("")
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_13)
        self.lineEdit_13.setValidator(input_validator)
        self.lineEdit_13.setGeometry(QtCore.QRect(1050, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(990, 130, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("")
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_14)
        self.lineEdit_14.setValidator(input_validator)
        self.lineEdit_14.setGeometry(QtCore.QRect(1050, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(1010, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_10.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(150, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("")
        self.label_35.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(310, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(150, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("")
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(310, 130, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(10, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame)
        self.label_38.setGeometry(QtCore.QRect(100, 70, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(85, 0, 0);")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.label_45 = QtWidgets.QLabel(self.frame)
        self.label_45.setGeometry(QtCore.QRect(1020, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("")
        self.label_45.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(170, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(310, 210, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(500, 110, 491, 21))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(520, 190, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(510, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("")
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setGeometry(QtCore.QRect(620, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(690, 140, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("")
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(725, 140, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("")
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_11)
        self.lineEdit_11.setValidator(input_validator)
        self.lineEdit_11.setGeometry(QtCore.QRect(870, 140, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(930, 140, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("")
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(760, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("")
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_12)
        self.lineEdit_12.setValidator(input_validator)
        self.lineEdit_12.setGeometry(QtCore.QRect(870, 190, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(940, 190, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("")
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.load100_guage=0
        self.load200_guage=0
        self.load300_guage=0
        self.guage_length_mm=0
        self.goAhead="No"
        self.test_type=""
        self.test_id="1"
        self.remark=""
        self.timer3=QtCore.QTimer()
        self.timer31=QtCore.QTimer()
        self.cycle_num=0
        self.show_lcd_vals="N"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "PUSH ON FORCE"))
        self.label_47.setText(_translate("MainWindow", "05 Aug 2020 14:23:00"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.pushButton_7.setText(_translate("MainWindow", "Stop"))
        self.pushButton_11.setText(_translate("MainWindow", "Start"))
        self.pushButton_12.setText(_translate("MainWindow", "All Graphs"))
        self.pushButton_13.setText(_translate("MainWindow", "View Report"))
        self.pushButton_14.setText(_translate("MainWindow", "Email"))
        self.pushButton_15.setText(_translate("MainWindow", "Comment"))
        self.label_33.setText(_translate("MainWindow", "Show Graph :"))
        self.radioButton.setText(_translate("MainWindow", "Low-Load cell"))
        self.radioButton_2.setText(_translate("MainWindow", "Hi-Load cell"))
        self.radioButton_3.setText(_translate("MainWindow", "Encoder"))
        self.radioButton_4.setText(_translate("MainWindow", "Extentiometer"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Spec.No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Peak Load (Kg.)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cycle.No"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "1"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_16.setText(_translate("MainWindow", "Print"))
        self.label_39.setText(_translate("MainWindow", "Load:"))
        self.label_40.setText(_translate("MainWindow", "Travel:"))
        self.label_41.setText(_translate("MainWindow", "Kgf."))
        self.label_42.setText(_translate("MainWindow", "Mm."))
        self.label_43.setText(_translate("MainWindow", "Current Test Speed:"))
        self.label_44.setText(_translate("MainWindow", "Mm/Min"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Load Vs Travel"))
        self.label_49.setText(_translate("MainWindow", "Data Saved Successfully ......"))
        self.pushButton_8.setText(_translate("MainWindow", "Go For Test"))
        self.pushButton_9.setText(_translate("MainWindow", "New Test"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "0001"))
        self.label_13.setText(_translate("MainWindow", "Speciment Name:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Speciment 1 XXXXXXXXXXXXXX"))
        self.label_14.setText(_translate("MainWindow", "Customer Name:"))
        self.label_48.setText(_translate("MainWindow", "Panakj Polymerst Pvt. Ltd."))
        self.label_15.setText(_translate("MainWindow", "Load Cell:"))
        self.label_16.setText(_translate("MainWindow", "5KN "))
        self.label_19.setText(_translate("MainWindow", "Test Speed:"))
        self.label_20.setText(_translate("MainWindow", "(mm/min)"))
        self.label_21.setText(_translate("MainWindow", "Rev. Speed:"))
        self.label_22.setText(_translate("MainWindow", "(mm/min)"))
        self.label_29.setText(_translate("MainWindow", "Load Unit:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Kg"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "N"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "KN"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "gm"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Lb"))
        self.label_30.setText(_translate("MainWindow", "Travel.  Unit:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Mm"))       
        self.label_31.setText(_translate("MainWindow", "X-axis: "))
        self.label_32.setText(_translate("MainWindow", "Y-axis: "))
        self.pushButton_10.setText(_translate("MainWindow", "Set Graph"))
        self.label_35.setText(_translate("MainWindow", "Job Name:"))
        self.label_36.setText(_translate("MainWindow", "Batch ID:"))
        self.label_37.setText(_translate("MainWindow", "Spec.Count:"))
        self.label_38.setText(_translate("MainWindow", "0"))
        self.label_45.setText(_translate("MainWindow", "Graph Scale "))
        self.label_17.setText(_translate("MainWindow", "Testing Mode:"))
        self.label_18.setText(_translate("MainWindow", "Compression"))
        self.label_50.setText(_translate("MainWindow", ""))
        self.label_23.setText(_translate("MainWindow", "Max .Load :"))
        self.label_24.setText(_translate("MainWindow", "Kg."))
        self.label_25.setText(_translate("MainWindow", "Compress. Length :"))
        self.label_26.setText(_translate("MainWindow", "Mm."))
        self.label_27.setText(_translate("MainWindow", "Guage. Length :"))
        self.label_28.setText(_translate("MainWindow", "Mm."))
        self.comboBox.currentTextChanged.connect(self.onchage_combo)
        self.comboBox_4.currentTextChanged.connect(self.show_graph)
        
      
        self.pushButton_8.clicked.connect(self.go_for_test)
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_9.clicked.connect(self.new_test_reset)
        self.pushButton_10.clicked.connect(self.set_graph_scale)
        self.pushButton_11.clicked.connect(self.start_test)
        self.tableWidget.doubleClicked.connect(self.delete_cycle)
        
        self.pushButton_13.clicked.connect(self.open_pdf)
        self.pushButton_16.clicked.connect(self.print_file)
        self.pushButton_14.clicked.connect(self.open_email_report)
        self.pushButton_15.clicked.connect(self.open_comment_popup)
        self.pushButton_12.clicked.connect(self.show_all_specimens)        
        self.pushButton_7.clicked.connect(self.manual_stop)
        #self.comboBox_2.currentTextChanged.connect(self.load_unit_onchange)
        self.test_method=""                             
        self.failure_mod=""
        self.tmperature=""
        self.test_type_for_flexural=""
        self.i=0
        self.comboBox.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SPECIMEN_NAME FROM SPECIMEN_MST") 
        for x in results:            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        self.load_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.frame_3.hide()
        self.show_grid_data_Tear()
        #self.tableWidget.setHorizontalHeaderLabels(['Thickness (mm)',' Peak Load (Kgf) ','Tear Strength (Kgf/Cm)','Created On','Cycle ID'])
        self.tableWidget.setHorizontalHeaderLabels([' Peak Load ('+str(self.comboBox_2.currentText())+') ','cycle_id'])        
        
        self.pushButton_9.setDisabled(True)
        self.report_fun_1()
        
    
    
    def report_fun_1(self):
        self.pushButton_8.setDisabled(True)
        self.pushButton_10.setDisabled(True) 
        self.frame_3.show()
        
        
        self.pushButton_12.setDisabled(True)
        #self.pushButton_13.setDisabled(True)
        
        self.radioButton.setDisabled(True)
        self.radioButton_2.setDisabled(True)
        self.radioButton_3.setDisabled(True)
        self.radioButton_4.setDisabled(True)
        
        self.lcdNumber.setDisabled(True)
        self.lcdNumber_2.setDisabled(True)
        self.lcdNumber_3.setDisabled(True)
        
        
        
        
        self.pushButton_13.setEnabled(True)
        self.pushButton_14.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        self.pushButton_16.setEnabled(True)
        self.show_graph()
        self.pushButton_11.setDisabled(True)
        
        ## Read Only Fields 
        self.readonly_fields()
    def load_unit_onchange(self):
        self.i=0        
        if(str(self.comboBox_2.currentText())=="KN"):        
              self.comboBox_3.setCurrentText(str("Mm"))
        elif(str(self.comboBox_2.currentText())=="MPa"):
              self.comboBox_3.setCurrentText(str("Mm"))
        else:
              print("No change in combo3")
        
        
    def device_date(self):     
        self.label_47.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def new_test_reset(self):
        self.cycle_num=0
        self.label_38.setText(str(self.cycle_num))
        self.readWrite_fields()
        self.load_data()
        self.pushButton_8.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.frame_3.hide()
        
        print("Timer3 status: "+str(self.timer3.isActive()))
        if(self.timer3.isActive()): 
                        self.timer3.stop()
                        print("Timer3 Stopped......Timer3 status: "+str(self.timer3.isActive()))
        
    def load_data(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TEST_ID,SPECIMEN_NAME,PARTY_NAME,JOB_NAME,BATCH_ID,MOTOR_SPEED,MOTOR_REV_SPEED,GUAGE_LENGTH,GRAPH_SCAL_Y_LOAD,GRAPH_SCAL_X_LENGTH,LAST_UNIT_LOAD,LAST_UNIT_DISP,NEW_TEST_MAX_LOAD,NEW_TEST_MAX_LENGTH FROM TEST_MST WHERE TEST_ID IN (Select TEST_ID FROM GLOBAL_VAR)")       
        for x in results:           
                 self.label_12.setText(str(x[0]).zfill(3))
                 self.test_id=str(x[0])                
                 self.comboBox.setCurrentText(str(x[1]))
                 self.comboBox.setDisabled(True)
                 print("spec name "+str(x[1]))
                 self.label_48.setText(str(x[2]))
                 #self.lineEdit_16.setText("Batch_"+str(x[0]).zfill(3))
                 self.lineEdit_15.setText(str(x[3]))
                 self.lineEdit_16.setText(str(x[4]))
                 
                 self.lineEdit_8.setText(str(x[5]))
                 self.lineEdit_9.setText(str(x[6]))
                 
                 #self.lineEdit_12.setText(str(x[7]))
                 
                 self.lineEdit_14.setText(str(x[8]))
                 self.lineEdit_13.setText(str(x[9]))
                 self.comboBox_2.setCurrentText(str(x[10]))
                 self.comboBox_3.setCurrentText(str(x[11]))
                 self.lineEdit_10.setText(str(x[12]))
                 self.lineEdit_11.setText(str(x[13]))
                 
        connection.close()
        #self.onchage_combo()
        

       
        self.sc_blank =PlotCanvas(self) 
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        
        
        self.label_49.setText("")
        self.label_49.show()
        #self.frame_3.hide()
        #print("Timer4 Status :"+str(self.timer4.isActive()))
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setDisabled(True)
        self.pushButton_15.setDisabled(True)
        self.pushButton_16.setDisabled(True)
        
        self.label_41.setText(str(self.comboBox_2.currentText()))
        self.label_42.setText(str(self.comboBox_3.currentText() ))
        self.lcdNumber.setProperty("value", 0.0)     #load
        self.lcdNumber_2.setProperty("value",0.0)  #length
        self.lcdNumber_3.setProperty("value",0.0)  #speed
        
        self.pushButton_7.setDisabled(True)
        self.pushButton_11.setEnabled(True)
        self.show_grid_data_Tear()
        print("Data Loaded OK !!")
       
    
    
    def validations(self):        
        self.go_ahead="No"
        self.msg=""
        if(self.lineEdit_15.text() == ""):
             self.msg="Test Details is Empty."            
        elif(self.lineEdit_16.text()== ""):
             self.msg="Batch ID is Empty."             
        elif(self.lineEdit_8.text()== ""):
             self.msg="Test Speed is Empty."            
        elif(self.lineEdit_9.text() == ""):
             self.msg="Rev.Speed is Empty"
        elif(self.lineEdit_10.text() == ""):
             self.msg="Max. Load is Empty"
        elif(int(self.lineEdit_10.text()) == 0):
             self.msg="Max. Load should not zero"
        elif(self.lineEdit_11.text() == ""):
             self.msg="Max. Length is Empty"
        elif(int(self.lineEdit_11.text()) == 0):
             self.msg="Max. Length should not zero"
        elif(self.lineEdit_12.text() == ""):
             self.msg="Guage. Length is Empty"
        elif(int(self.lineEdit_12.text()) == 0):
             self.msg="Guage. Length should not zero"
        elif(str(self.comboBox_2.currentText())== "KN"  and str(self.comboBox_3.currentText())== "Cm"):
            self.msg="Unity Type : KN/CM incorrect."
        elif(str(self.comboBox_2.currentText())== "KN"  and str(self.comboBox_3.currentText())== "Inch"):
            self.msg="Unity Type : KN/Inch incorrect."
        elif(str(self.comboBox_2.currentText())== "MPa"  and str(self.comboBox_3.currentText())== "Cm"):
            self.msg="Unity Type : MPa/Cm incorrect."
        elif(str(self.comboBox_2.currentText())== "MPa"  and str(self.comboBox_3.currentText())== "Inch"):
            self.msg="Unity Type : MPa/Inch incorrect."
        else:
               self.msg="Confirm to start Test."
               self.go_ahead="Yes"
               connection = sqlite3.connect("tyr.db")
               results=connection.execute("select count(*) from TEST_MST WHERE TEST_ID = '"+str(int(self.label_12.text()))+"'")       
               for x in results:           
                 if(int(x[0]) > 0):
                       self.test_id_exist="Yes"
                 else:
                       self.test_id_exist="No"                     
               connection.close() 
               
               if(self.test_id_exist=="Yes"):
                   
                     ### Update global var
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                                cursor = connection.cursor()                  
                                cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(int(self.label_12.text()))+"',NEW_TEST_GUAGE_MM='"+str(self.lineEdit_12.text())+"'")
                                cursor.execute("UPDATE TEST_MST SET SPECIMEN_NAME='"+str(self.comboBox.currentText())+"',BATCH_ID='"+str(self.lineEdit_16.text())+"',PARTY_NAME='"+str(self.label_48.text())+"',GUAGE_LENGTH='"+str(self.lineEdit_12.text())+"',MOTOR_SPEED='"+str(self.lineEdit_8.text())+"'  WHERE  TEST_ID = '"+str(int(self.label_12.text()))+"'")
                        connection.commit();
                        connection.close()
                        
               else:        
                        ### INSERT 
                        connection = sqlite3.connect("tyr.db")              
                        with connection:        
                              cursor = connection.cursor()
                              cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_MAX_LOAD='"+str(self.lineEdit_10.text())+"',NEW_TEST_MAX_LENGTH='"+str(self.lineEdit_11.text())+"',NEW_TEST_SPECIMEN_NAME='"+self.comboBox.currentText()+"',NEW_TEST_SPE_SHAPE='"+str(self.label_16.text())+"',NEW_TEST_PARTY_NAME='"+str(self.label_48.text())+"',NEW_TEST_MOTOR_SPEED='"+str(self.lineEdit_8.text())+"',NEW_TEST_JOB_NAME='"+str(self.lineEdit_15.text())+"',NEW_TEST_BATCH_ID='"+self.lineEdit_16.text()+"',NEW_TEST_MOTOR_REV_SPEED='"+str(self.lineEdit_9.text())+"'") 
                              cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(int(self.label_12.text()))+"',NEW_TEST_GUAGE_MM='"+str(self.lineEdit_12.text())+"'")
                              cursor.execute("INSERT INTO TEST_MST(SPECIMEN_NAME,BATCH_ID,PARTY_NAME,TEST_TYPE,GUAGE_LENGTH,MOTOR_SPEED,MOTOR_REV_SPEED,JOB_NAME,NEW_TEST_MAX_LOAD,NEW_TEST_MAX_LENGTH) VALUES('"+str(self.comboBox.currentText())+"','"+str(self.lineEdit_16.text())+"','"+str(self.label_48.text())+"','PUSH_ON_FORCE','','"+str(self.lineEdit_8.text())+"','"+str(self.lineEdit_9.text())+"','"+str(self.lineEdit_10.text())+"','"+str(self.lineEdit_11.text())+"','')")
                              cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_Y_LOAD='"+self.lineEdit_14.text()+"',GRAPH_SCAL_X_LENGTH='"+self.lineEdit_13.text()+"'  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                              cursor.execute("UPDATE TEST_MST SET LAST_UNIT_LOAD='"+str(self.comboBox_2.currentText())+"',LAST_UNIT_DISP='"+str(self.comboBox_3.currentText())+"'  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                              cursor.execute("UPDATE TEST_MST SET TESTED_BY=(SELECT LOGIN_USER_NAME FROM GLOBAL_VAR)  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                        connection.commit();
                        connection.close()
       
    
    def readonly_fields(self):
        self.comboBox.setDisabled(True)
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_9.setReadOnly(True)
        self.comboBox_2.setDisabled(True)
        self.comboBox_3.setDisabled(True)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_14.setReadOnly(True)
    
    def readWrite_fields(self):
        self.comboBox.setEnabled(True)
        self.lineEdit_15.setReadOnly(False)
        self.lineEdit_16.setReadOnly(False)
        self.lineEdit_8.setReadOnly(False)
        self.lineEdit_9.setReadOnly(False)
        self.comboBox_2.setEnabled(True)
        self.comboBox_3.setEnabled(True)
        self.lineEdit_13.setReadOnly(False)
        self.lineEdit_14.setReadOnly(False)
        
    
    def go_for_test(self):
        print("Old object status :"+str(self.timer31.isActive()))
        self.validations()        
        close = QMessageBox()
        close.setText("Message: "+str(self.msg))
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:
                 if(self.go_ahead=="Yes"):
                         self.save_units();
                         self.frame_3.show()
                         self.sc_blank =PlotCanvas_blank(self) 
                         self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
                         
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
                                self.timer3.setInterval(5000)        
                                self.timer3.timeout.connect(self.loadcell_encoder_status)
                                self.timer3.start(1)
                                self.pushButton_8.setDisabled(True)
                                #self.pushButton_6.setDisabled(True)
                                self.readonly_fields()
                                self.show_lcd_vals="N"
                                
                                
                                
                         except IOError:
                                    print("IO Errors") 
                        
                 else:
                         self.frame_3.hide()
        
        
        #self.show_grid_data_Tear()
        self.label_41.setText(str(self.comboBox_2.currentText()))
        self.label_42.setText(str(self.comboBox_3.currentText()))
        
        
    def save_units(self):
        connection = sqlite3.connect("tyr.db")
        with connection:        
           cursor = connection.cursor()
           cursor.execute("UPDATE GLOBAL_VAR2 SET LAST_LOAD_UNIT='"+str(str(self.comboBox_2.currentText()))+"', LAST_DISP_UNIT='"+str(self.comboBox_3.currentText())+"'")
           cursor.execute("UPDATE SPECIMEN_MST SET LAST_UNIT_LOAD='"+str(str(self.comboBox_2.currentText()))+"', LAST_UNIT_DISP='"+str(self.comboBox_3.currentText())+"'   where SPECIMEN_NAME = '"+str(self.comboBox.currentText())+"'")
           print("Units set Ok !!")          
           
        connection.commit();
        connection.close()
        
    
    def loadcell_encoder_status(self):
        self.load_cell_hi=-1
        self.load_cell_lo=-1
        self.extiometer=-1
        self.encoder=-1
        try:                
            self.serial_3.flush()
            self.serial_3.write(b'*D\r')
            self.line_3 = self.serial_3.readline()
            #print("encoder_status:o/p:"+str(self.line_3))
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
                
           
            
            
            if(self.load_cell_hi==0):
                #print("Load Cell: Hi")
                self.radioButton.setEnabled(True)
                self.radioButton.setChecked(True)
                self.radioButton_2.setDisabled(True)
                self.radioButton_2.setChecked(False)
            else:  
            #elif(self.load_cell_lo==1):
                #print("Load Cell: Low")
                self.radioButton_2.setEnabled(True)
                self.radioButton_2.setChecked(True)
                self.radioButton.setDisabled(True)
                self.radioButton.setChecked(False)
                
         
        
            if(self.extiometer==1):
                #print("Proxy: Extentiometer")
                self.radioButton_4.setChecked(True)
                self.radioButton_3.setDisabled(True)
                self.radioButton_3.setChecked(False)
                self.radioButton_4.setEnabled(True)            
            else:
            #elif(self.encoder==1):
                #print("Proxy: Encoder")
                self.radioButton_3.setChecked(True)
                self.radioButton_4.setDisabled(True)
                self.radioButton_4.setChecked(False)
                self.radioButton_3.setEnabled(True)
                                   
    
    def onchage_combo(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select C_A_AREA,GUAGE_LENGTH_MM,MOTOR_SPEED,PARTY_NAME,THICKNESS,WIDTH,DIAMETER,SHAPE ,IN_DIAMETER_MM,OUTER_DIAMETER_MM,REV_MOTOR_SPEED,LAST_UNIT_LOAD,LAST_UNIT_DISP,LOAD_CELL FROM SPECIMEN_MST WHERE SPECIMEN_NAME='"+self.comboBox.currentText()+"'")                 
        for x in results:
            self.lineEdit_12.setText(str(x[1])) # GUAGE LENGTH
            self.lineEdit_8.setText(str(x[2])) # SPEED
            self.label_48.setText(str(x[3])) # Customer Name
            self.label_16.setText(str(x[13])) #shape
            self.shape=str(x[7])
            self.lineEdit_9.setText(str(x[10])) #rev. speed
            self.comboBox_2.setCurrentText(str(x[11])) #UNIT_LOAD
            self.comboBox_3.setCurrentText(str(x[12])) #UNIT_Travel
                     
        
        connection.close()
        #self.click_onRadiobutt()
        #self.cs_area_calculation()
        
    def set_graph_scale(self):
        self.x_axis_val="0.0"
        self.y_axis_val="0.0"        
        try:
                self.x_axis_val=int(self.lineEdit_13.text())
        except ValueError as e:
                try:
                       self.x_axis_val=float(self.lineEdit_13.text())
                except ValueError as e:
                       self.lineEdit_13.setText("0.00") 
        try:
                self.y_axis_val=int(self.lineEdit_14.text())
        except ValueError as e:
                try:
                        self.y_axis_val=float(self.lineEdit_14.text())
                except ValueError as e:
                        self.lineEdit_14.setText("0.00")
        
        connection = sqlite3.connect("tyr.db")
        with connection:        
           cursor = connection.cursor()
           cursor.execute("UPDATE SETTING_MST SET GRAPH_SCALE_CELL_2='"+str(self.x_axis_val)+"', GRAPH_SCALE_CELL_1='"+str(self.y_axis_val)+"'")
           print("Graph Scale set Ok !!")
           self.label_50.setText("Graph Scale set Ok !!")
           self.frame_3.hide()
           self.pushButton_8.setEnabled(True)
           self.pushButton_9.setEnabled(True)
        connection.commit();
        connection.close()
        
    
    
    def manual_stop(self):
        self.sc_new.ser.write(b'*Q\r')
        self.reset()
        self.save_graph_data()
        self.sc_new.save_data_flg=""
        self.label_49.setText("Mannual stopped new.")
        self.label_49.show()
        self.pushButton_7.setDisabled(True)
        self.pushButton_11.setEnabled(True)
        self.label_38.setText(str(self.cycle_num))
        self.pushButton_12.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_14.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        self.pushButton_16.setEnabled(True)
        self.sc_new.arr_p=[0.0]
        self.sc_new.arr_q=[0.0]
        self.sc_new.arr_speed=[0.0]
        self.lcdNumber.setProperty("value", 0.0)     #load
        self.lcdNumber_2.setProperty("value",0.0)  #length
        self.lcdNumber_3.setProperty("value",0.0)  #speed
                
    def reset(self):
        if(self.sc_new.timer1.isActive()): 
           self.sc_new.on_ani_stop()
           self.sc_new.timer1.stop()
           self.sc_new.arr_p=[0.0]
           self.sc_new.arr_q=[0.0]
           self.sc_new.arr_speed=[0.0]
           
           
        if(self.timer3.isActive()): 
           self.timer3.stop()
           
    #def frame_1_read_only(self):
        
        

    def start_test(self):
        self.show_lcd_vals="Y"
        self.label_49.setText("Running Test ........")
        self.label_49.show()
        self.pushButton_11.setDisabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.sc_new =PlotCanvas_Auto(self,width=8, height=5, dpi=90)
        self.gridLayout.addWidget(self.sc_new, 1, 0, 1, 1)
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT COUNT(*) FROM STG_GRAPH_MST")
        rows=results.fetchall()
        connection.close()               
        print("Test Strated.")
        if(int(rows[0][0]) > -2 ):
                    self.timer3=QtCore.QTimer()
                    self.timer3.setInterval(1000)        
                    self.timer3.timeout.connect(self.show_load_cell_val)
                    self.timer3.start(1)
                    
    
    def show_load_cell_val(self):
        if(self.show_lcd_vals=="Y"):
                    if((str(self.comboBox_2.currentText()) =="Kg") and (str(self.comboBox_3.currentText()) =="Mm")):
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q)))    #load
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))   #length
                    elif((str(self.comboBox_2.currentText()) =="Kg") and (str(self.comboBox_3.currentText()) =="Cm")):
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q)))    #load
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p_cm)))   #length
                    elif((str(self.comboBox_2.currentText()) =="Kg") and (str(self.comboBox_3.currentText()) =="Inch")):
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q)))    #load
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p_inch)))   #length
                    elif((str(self.comboBox_2.currentText()) =="Lb") and (str(self.comboBox_3.currentText()) =="Mm")):
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q_lb)))    #load
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))   #length
                    elif((str(self.comboBox_2.currentText()) =="Lb") and (str(self.comboBox_3.currentText()) =="Cm")):
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q_lb)))    #load
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p_cm)))   #length
                    elif((str(self.comboBox_2.currentText()) =="Lb") and (str(self.comboBox_3.currentText()) =="Inch")):
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q_lb)))     #load
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p_inch)))  #length
                    elif((str(self.comboBox_2.currentText()) =="N") and (str(self.comboBox_3.currentText()) =="Mm")):
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q_n)))     #load
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))  #length
                    elif((str(self.comboBox_2.currentText()) =="N") and (str(self.comboBox_3.currentText()) =="Cm")):
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q_n)))     #load
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p_cm)))  #length
                    elif((str(self.comboBox_2.currentText()) =="N") and (str(self.comboBox_3.currentText()) =="Inch")):
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q_n)))     #load
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p_inch)))  #length
                    elif((str(self.comboBox_2.currentText()) =="KN") and (str(self.comboBox_3.currentText()) =="Mm")):
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q_kn)))     #load
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))  #length
                    elif((str(self.comboBox_2.currentText()) =="gm") and (str(self.comboBox_3.currentText()) =="Mm")):
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q_mpa)))     #load
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))  #length
                    else:
                                    self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q)))
                                    self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))   #length
                    #self.lcdNumber_3.setProperty("value",str(max(self.sc_new.arr_speed)))
                    self.lcdNumber_3.setProperty("value",str(self.lineEdit_8.text()))
                    self.pushButton_11.setDisabled(True)
                    self.pushButton_7.setEnabled(True)
                    self.pushButton_6.setDisabled(True)
                    #print("lcd printing .......")
                    if(str(self.sc_new.save_data_flg) =="Yes"):
                            self.reset()
                            self.save_graph_data()
                            self.sc_new.save_data_flg=""
                            self.label_49.setText("Data Saved Successfully.")
                            self.label_49.show()
                            self.pushButton_7.setDisabled(True)
                            self.pushButton_11.setEnabled(True)
                            self.label_38.setText(str(self.cycle_num))
                            self.pushButton_12.setEnabled(True)
                            self.pushButton_13.setEnabled(True)
                            self.pushButton_14.setEnabled(True)
                            self.pushButton_15.setEnabled(True)
                            self.pushButton_16.setEnabled(True)
                            self.pushButton_6.setEnabled(True)
                            
        else:
                           self.lcdNumber.setProperty("value", 0.0)     #load
                           self.lcdNumber_2.setProperty("value",0.0)  #length
                           self.lcdNumber_3.setProperty("value",0.0)  #speed
                
                
        
    def save_graph_data(self):                
        
        self.load100_guage=0
        self.load200_guage=0
        self.load300_guage=0
        self.cs_area="0.0"
        try:
                self.cs_area=1
        except ValueError as e:
                try:
                       self.cs_area=1
                except ValueError as e:
                       self.lineEdit_12.setText("error")
                       self.cs_area="0.0"
        
        
        if( str(self.comboBox_3.currentText()) =="Cm"):         
                self.cs_area=self.cs_area*0.1*0.1       
        elif( str(self.comboBox_3.currentText()) =="Inch"):
                self.cs_area=self.cs_area*0.0393701
        else:                
                self.cs_area=1
        
        if (len(self.sc_new.arr_p) > 1):            
            #### Get Guage length
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("select IFNULL(NEW_TEST_GUAGE_MM,0),NEW_TEST_NAME,IS_METAL FROM GLOBAL_VAR")                 
            for x in results:
                self.guage_length_mm=int(x[0])
                self.test_type=str(x[1])
                self.def_flg=str(x[2])            
            connection.close()                                  
            
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)):
                   cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_LB,Y_NUM_KN,Y_NUM_MPA) VALUES ('"+str(float(self.sc_new.arr_p[g]))+"','"+str(float(self.sc_new.arr_p_cm[g]))+"','"+str(float(self.sc_new.arr_p_inch[g]))+"','"+str(self.sc_new.arr_q[g])+"','"+str(self.sc_new.arr_q_n[g])+"','"+str(self.sc_new.arr_q_lb[g])+"','"+str(self.sc_new.arr_q_kn[g])+"','"+str(self.sc_new.arr_q_mpa[g])+"')")
                   
            connection.commit();
            connection.close()
            if(str(self.comboBox_2.currentText()) =="Lb"):                   
                    for g in range(len(self.sc_new.arr_p)):
                         if((float(self.guage_length_mm)*1) <= float(self.sc_new.arr_p[g])):
                                self.load100_guage=float(self.sc_new.arr_q_lb[g])
                                break;            
                    for g in range(len(self.sc_new.arr_p)):    
                         if((float(self.guage_length_mm)*2) <= float(self.sc_new.arr_p[g])):
                                self.load200_guage=float(self.sc_new.arr_q_lb[g])
                                break;
                    for g in range(len(self.sc_new.arr_p)):                                
                         if((float(self.guage_length_mm)*3) <= float(self.sc_new.arr_p[g])):
                                self.load300_guage=float(self.sc_new.arr_q_lb[g])
                                break;
            elif(str(self.comboBox_2.currentText()) =="N"):
                    for g in range(len(self.sc_new.arr_p)):
                         if((float(self.guage_length_mm)*1) <= float(self.sc_new.arr_p[g])):
                                self.load100_guage=float(self.sc_new.arr_q_n[g])
                                break;            
                    for g in range(len(self.sc_new.arr_p)):    
                         if((float(self.guage_length_mm)*2) <= float(self.sc_new.arr_p[g])):
                                self.load200_guage=float(self.sc_new.arr_q_n[g])
                                break;
                    for g in range(len(self.sc_new.arr_p)):                                
                         if((float(self.guage_length_mm)*3) <= float(self.sc_new.arr_p[g])):
                                self.load300_guage=float(self.sc_new.arr_q_n[g])
                                break;
            elif(str(self.comboBox_2.currentText()) =="KN"):
                    for g in range(len(self.sc_new.arr_p)):
                         if((float(self.guage_length_mm)*1) <= float(self.sc_new.arr_p[g])):
                                self.load100_guage=float(self.sc_new.arr_q_kn[g])
                                break;            
                    for g in range(len(self.sc_new.arr_p)):    
                         if((float(self.guage_length_mm)*2) <= float(self.sc_new.arr_p[g])):
                                self.load200_guage=float(self.sc_new.arr_q_kn[g])
                                break;
                    for g in range(len(self.sc_new.arr_p)):                                
                         if((float(self.guage_length_mm)*3) <= float(self.sc_new.arr_p[g])):
                                self.load300_guage=float(self.sc_new.arr_q_kn[g])
                                break;
            elif(str(self.comboBox_2.currentText()) =="MPa"):
                    for g in range(len(self.sc_new.arr_p)):
                         if((float(self.guage_length_mm)*1) <= float(self.sc_new.arr_p[g])):
                                self.load100_guage=float(self.sc_new.arr_q_mpa[g])
                                break;            
                    for g in range(len(self.sc_new.arr_p)):    
                         if((float(self.guage_length_mm)*2) <= float(self.sc_new.arr_p[g])):
                                self.load200_guage=float(self.sc_new.arr_q_mpa[g])
                                break;
                    for g in range(len(self.sc_new.arr_p)):                                
                         if((float(self.guage_length_mm)*3) <= float(self.sc_new.arr_p[g])):
                                self.load300_guage=float(self.sc_new.arr_q_mpa[g])
                                break;  
            else:
                    for g in range(len(self.sc_new.arr_p)):
                         if((float(self.guage_length_mm)*1) <= float(self.sc_new.arr_p[g])):
                                self.load100_guage=float(self.sc_new.arr_q[g])
                                break;            
                    for g in range(len(self.sc_new.arr_p)):    
                         if((float(self.guage_length_mm)*2) <= float(self.sc_new.arr_p[g])):
                                self.load200_guage=float(self.sc_new.arr_q[g])
                                break;
                    for g in range(len(self.sc_new.arr_p)):                                
                         if((float(self.guage_length_mm)*3) <= float(self.sc_new.arr_p[g])):
                                self.load300_guage=float(self.sc_new.arr_q[g])
                                break;
          
        
        if (len(self.sc_new.arr_p) > 1):            
            self.cycle_num=self.cycle_num+1
            connection = sqlite3.connect("tyr.db")              
            with connection:                
                  cursor = connection.cursor()              
                  #print("ok1")
                  #cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_THICKNESS='"+str(self.lineEdit_10.text())+"',NEW_TEST_WIDTH='"+str(self.lineEdit_11.text())+"',NEW_TEST_AREA='"+str(self.cs_area)+"',NEW_TEST_DIAMETER='"+str(self.lineEdit_10.text())+"', NEW_TEST_INN_DIAMETER='"+str(self.lineEdit_11.text())+"', NEW_TEST_OUTER_DIAMETER='"+str(self.lineEdit_10.text())+"'")
                 
                  if( str(self.comboBox_2.currentText()) =="Lb"):
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM_LB) FROM STG_GRAPH_MST)")   ###    
                  elif( str(self.comboBox_2.currentText()) =="N"):
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM_N) FROM STG_GRAPH_MST)")   ###
                  elif( str(self.comboBox_2.currentText()) =="KN"):
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM_KN) FROM STG_GRAPH_MST)")   ###
                  elif( str(self.comboBox_2.currentText()) =="gm"):
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM_MPA) FROM STG_GRAPH_MST)")   ###  
                  else:    
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM) FROM STG_GRAPH_MST)")   ### STG_PEAK_LOAD_KG                 
                  
                  if( str(self.comboBox_3.currentText()) =="Cm"):
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_PEAK_LOAD_MM = (SELECT X_NUM_CM FROM STG_GRAPH_MST where Y_NUM = (SELECT MAX(Y_NUM) FROM STG_GRAPH_MST))") #
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_BREAK_MM=(SELECT max(X_NUM_CM) FROM STG_GRAPH_MST)") #
                  elif( str(self.comboBox_3.currentText()) =="Inch"):
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_PEAK_LOAD_MM = (SELECT X_NUM_INCH FROM STG_GRAPH_MST where Y_NUM = (SELECT MAX(Y_NUM) FROM STG_GRAPH_MST))") #
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_BREAK_MM=(SELECT max(X_NUM_INCH) FROM STG_GRAPH_MST)") #
                  else:
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_PEAK_LOAD_MM = (SELECT X_NUM FROM STG_GRAPH_MST where Y_NUM = (SELECT MAX(Y_NUM) FROM STG_GRAPH_MST))") #STG_E_AT_PEAK_LOAD_MM
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_BREAK_MM=(SELECT max(X_NUM) FROM STG_GRAPH_MST)") #STG_TENSILE_STRENGTH
                  
                  
                  
                  if( str(self.comboBox_2.currentText()) =="MPa"):
                         cursor.execute("UPDATE GLOBAL_VAR SET STG_TENSILE_STRENGTH=cast(STG_PEAK_LOAD_KG as real)") #STG_TENSILE_STRENGTH                           
                  else:
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_TENSILE_STRENGTH=((cast(STG_PEAK_LOAD_KG as real)/IFNULL(cast(NEW_TEST_AREA as real),1)))") #STG_TENSILE_STRENGTH                  
                  
                  
                  if( str(self.comboBox_3.currentText()) =="Cm"):
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE100=NEW_TEST_GUAGE_MM*0.1")
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE200=(NEW_TEST_GUAGE_MM*2*0.1)")
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE300=(NEW_TEST_GUAGE_MM*3*0.1)")
                  elif( str(self.comboBox_3.currentText()) =="Inch"):
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE100=NEW_TEST_GUAGE_MM*0.0393701")
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE200=(NEW_TEST_GUAGE_MM*2*0.0393701)")
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE300=(NEW_TEST_GUAGE_MM*3*0.0393701)")
                  else:
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE100=NEW_TEST_GUAGE_MM")
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE200=(NEW_TEST_GUAGE_MM*2)")
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_GUAGE300=(NEW_TEST_GUAGE_MM*3)")
                          
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_SET_LOW=(SELECT  BREAKING_SENCE FROM SETTING_MST) ") #STG_SET_LOW
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_BREAK_LOAD_KG=(SELECT  BREAKING_SENCE FROM SETTING_MST) ") #STG_BREAK_LOAD_KG
                 
                  
                  #print("ok5")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_LOAD100_GUAGE='"+str(self.load100_guage)+"'")                                       
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_MODULUS_100=((cast(STG_LOAD100_GUAGE as real)/cast(NEW_TEST_AREA as real)))")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_LOAD200_GUAGE='"+str(self.load200_guage)+"'")  
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_MODULUS_200=((cast(STG_LOAD200_GUAGE as real)/cast(NEW_TEST_AREA as real)))")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_LOAD300_GUAGE='"+str(self.load300_guage)+"'")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_MODULUS_300=((cast(STG_LOAD300_GUAGE as real)/cast(NEW_TEST_AREA as real)))")                 
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_MODULUS_100=IFNULL(STG_MODULUS_100,0),STG_MODULUS_200=IFNULL(STG_MODULUS_200,0),STG_MODULUS_300=IFNULL(STG_MODULUS_300,0)")
                  
                   
                  cursor.execute("INSERT INTO CYCLES_MST(TEST_ID,SHAPE,THINCKNESS,WIDTH,CS_AREA,DIAMETER,INNER_DIAMETER,OUTER_DIAMETER,PEAK_LOAD_KG,E_AT_PEAK_LOAD_MM,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_ANY,BREAK_LOAD_KG,E_AT_BREAK_MM,SET_LOW,GUAGE100,LOAD100_GUAGE,GUAGE200,LOAD200_GUAGE,GUAGE300,LOAD300_GUAGE,BREAK_MODE,TEMPERATURE,TEST_METHOD,DEF_POINT,DEF_LOAD,DEF_YEILD_STRG,DEF_FLG) SELECT TEST_ID,NEW_TEST_SPE_SHAPE,NEW_TEST_THICKNESS,NEW_TEST_WIDTH,NEW_TEST_AREA,NEW_TEST_DIAMETER, NEW_TEST_INN_DIAMETER, NEW_TEST_OUTER_DIAMETER,STG_PEAK_LOAD_KG,STG_E_AT_PEAK_LOAD_MM,STG_TENSILE_STRENGTH,STG_MODULUS_100,STG_MODULUS_200,STG_MODULUS_300,STG_MODULUS_ANY,STG_BREAK_LOAD_KG,STG_E_AT_BREAK_MM,STG_SET_LOW,STG_GUAGE100,STG_LOAD100_GUAGE,STG_GUAGE200,STG_LOAD200_GUAGE,STG_GUAGE300,STG_LOAD300_GUAGE,BREAK_MODE,TEMPERATURE,TEST_METHOD,DEF_POINT,DEF_LOAD,DEF_YEILD_STRG,DEF_FLG FROM GLOBAL_VAR")
                  cursor.execute("INSERT INTO GRAPH_MST(X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_MPA,Y_NUM_LB,Y_NUM_KN) SELECT X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_MPA,Y_NUM_LB,Y_NUM_KN FROM STG_GRAPH_MST")
                  
              
                  cursor.execute("UPDATE CYCLES_MST SET PRC_E_AT_BREAK= (((E_AT_BREAK_MM+GUAGE100)*100)/GUAGE100)  WHERE GRAPH_ID IS NULL")
                  cursor.execute("UPDATE CYCLES_MST SET PRC_E_AT_PEAK= (((E_AT_PEAK_LOAD_MM+GUAGE100)*100)/GUAGE100)  WHERE GRAPH_ID IS NULL")                  
                  cursor.execute("UPDATE CYCLES_MST SET PRC_E_AT_BREAK=(PRC_E_AT_BREAK-100)   WHERE GRAPH_ID IS NULL")
                  cursor.execute("UPDATE CYCLES_MST SET PRC_E_AT_PEAK=(PRC_E_AT_PEAK-100)  WHERE GRAPH_ID IS NULL")
                  
                  cursor.execute("UPDATE CYCLES_MST SET CYCLE_NUM='"+str(self.cycle_num)+"'  WHERE GRAPH_ID IS NULL")
                  
                  cursor.execute("UPDATE CYCLES_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")
                  
                  cursor.execute("UPDATE GRAPH_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")              
                  cursor.execute("UPDATE TEST_MST SET STATUS='LOADED GRAPH' WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                  #cursor.execute("UPDATE TEST_MST SET TEMPERATURE = (SELECT TEMPERATURE FROM GLOBAL_VAR) WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                  print("data saved.")                  
            
            connection.commit();
            connection.close()            
        
        #self.load_data()
        print("Save completed")
        self.show_grid_data_Tear()
        
        
    def open_pdf(self):
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90) 
        #self.pushButton_4_2.setEnabled(True)
        #self.pushButton_4_3.setEnabled(True)
        self.create_pdf_Tear()        
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
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)
        self.create_pdf_Tear()
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
          
     
    def show_all_specimens(self):        
        #self.pushButton_3.setDisabled(True) ### save
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                       cursor = connection.cursor()                
                       cursor.execute("UPDATE GLOBAL_VAR2 SET GRAPH_TYPE='"+str(self.comboBox_4.currentText())+"'")                                   
        connection.commit();
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)    
        self.gridLayout.addWidget(self.sc_data, 1,0,1,1)
    
    def delete_cycle(self):       
            row = self.tableWidget.currentRow() 
            self.cycle_id=str(self.tableWidget.item(row, 1).text())
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
                    #self.load_data()
                    self.show_grid_data_Tear()
        
    
    
    
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
            
    def show_grid_data_Tear(self):
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels([' Peak Load ('+str(self.comboBox_2.currentText())+') ','cycle_id'])        
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT printf(\"%.2f\", PEAK_LOAD_KG),cycle_id FROM CYCLES_MST WHERE TEST_ID = '"+self.test_id+"' order by GRAPH_ID")
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close() 
        
    def create_pdf_Tear(self):
        self.remark=""
        self.login_user_name=""
        self.unit_typex="Kg/Cm"
        self.tested_by=""
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_UNIT_LOAD,LAST_UNIT_DISP,TEST_ID,TESTED_BY from TEST_MST  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ") 
        for x in results:
              self.last_load_unit=str(x[0])
              self.last_disp_unit=str(x[1])
              self.test_id=str(x[2])
              self.tested_by=str(x[3])
        connection.close()
        
        data2= [ ['Spec. \n No', 'Force at Peak\n ('+str(self.last_load_unit)+')']]
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", A.PEAK_LOAD_KG) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(A.PEAK_LOAD_KG)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(A.PEAK_LOAD_KG)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(A.PEAK_LOAD_KG)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        y=300
        Elements=[]
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.LOAD_CELL,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime'),A.COMMENTS   FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date-Time: ",str(x[10]),"Test No: ",str(x[0])],["Test Details : ",str(x[1]),"Batch ID: ",str(x[2])],["Product Name:  ",str(x[4])," Shape:",str(x[9])],["Test Type:",str(x[3]),"Test Method:",str(x[8])],["Customer Name :",str(x[7]),"Test Speed (min/min) :",str(x[5])],["Load cell:",str(x[6]),"Report Date-Time: ",str(x[11])],["Tested By :", str(self.tested_by),"",""]]
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
       
        
        #f1=Table(data)
        #f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
        #
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
        #self.show_all_specimens()
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4* inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),Spacer(1,12),f2,Spacer(1,12),blank,comments,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
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

      
    
    def show_graph(self):
        print("Show graph function called.")
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                       cursor = connection.cursor()                
                       cursor.execute("UPDATE GLOBAL_VAR2 SET GRAPH_TYPE='"+str(self.comboBox_4.currentText())+"'")                                   
        connection.commit();
        self.show_all_specimens()

class PlotCanvas_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=5, height=4, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="Tensile"
        self.axes.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.p_cm =0
        self.p_inch =0
        
        self.q =0
        self.q_n =0
        self.q_lb =0
        self.q_kn =0
        self.q_mpa =0
        
        self.speed=500
        
        
        
        
        self.arr_p=[0.0]
        self.arr_p_cm=[0.0]
        self.arr_p_inch=[0.0]
        
        
        self.arr_q=[0.0]
        self.arr_q_n=[0.0]
        self.arr_q_lb=[0.0]
        self.arr_q_kn=[0.0]
        self.arr_q_mpa=[0.0]
        
        self.arr_speed=[0.0]
        
        self.arr_p1=[0.0]
        self.arr_q1=[0.0]
        self.x=0
        self.y=0
        #self.ax = self.figure.add_subplot(111) 
        self.xlim=0
        self.ylim=10
        self.line_cnt=0
        self.kg_cm2=0
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
        self.unit_type =""
        self.load_unit=""
        self.disp_unit=""
        self.cs_area_cm="1"
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
        connection.commit();
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_LOAD_UNIT,LAST_DISP_UNIT from GLOBAL_VAR2") 
        for x in results:
                        self.load_unit=str(x[0])
                        self.disp_unit=str(x[1])
        connection.close()                
                        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,IFNULL(NEW_TEST_AREA*0.1*0.1,0) from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=int(x[0])             
             self.max_load=int(x[2])
             #self.max_load=100
             self.max_length=float(float(x[3]))
             self.flex_max_length=float(x[3])
             self.cof_max_length=float(x[4])
             self.max_length=float(float(x[0])-float(x[3]))
             print("Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
             self.unit_type=str(x[5])
             self.cs_area_cm=1
        connection.close()
        print(" xxx     gfgf self.unit_type:"+str(self.unit_type))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:
                 self.auto_rev_time_off=int(x[2])
                 self.break_sence=int(x[3])
                 print("self.load_unit:"+str(self.load_unit)+"self.disp_unit:"+str(self.disp_unit))
                 if(self.load_unit=="Kg" and self.disp_unit=="Mm"):
                                 self.axes.set_xlabel('Travel (Mm)')
                                 self.axes.set_ylabel('Load (Kg)')
                 elif(self.load_unit=="Kg" and self.disp_unit=="Inch"):
                                 self.axes.set_xlabel('Travel (Inch)')
                                 self.axes.set_ylabel('Load (Kg)')
                 elif(self.load_unit=="Kg" and self.disp_unit=="Cm"):
                                 self.axes.set_xlabel('Travel (Cm)')
                                 self.axes.set_ylabel('Load (Kg)')                                                               
                 elif(self.load_unit=="Lb" and self.disp_unit=="Mm"):
                                 self.axes.set_xlabel('Travel (Mm)')
                                 self.axes.set_ylabel('Load (Lb)')
                 elif(self.load_unit=="Lb" and self.disp_unit=="Cm"):
                                 self.axes.set_xlabel('Travel (Cm)')
                                 self.axes.set_ylabel('Load (Lb)') 
                 elif(self.load_unit=="Lb" and self.disp_unit=="Inch"):
                                 self.axes.set_xlabel('Travel (Inch)')
                                 self.axes.set_ylabel('Load (Lb)')                                                         
                 elif(self.load_unit=="N" and self.disp_unit=="Mm"):
                                 self.axes.set_xlabel('Travel (Mm)')
                                 self.axes.set_ylabel('Load (N)')                                                         
                 elif(self.load_unit=="N" and self.disp_unit=="Cm"):
                                 self.axes.set_xlabel('Travel (Cm)')
                                 self.axes.set_ylabel('Load (N)')                                 
                 elif(self.load_unit=="N" and self.disp_unit=="Inch"):
                                 self.axes.set_xlabel('Travel (Inch)')
                                 self.axes.set_ylabel('Load (N)')
                 elif(self.load_unit=="KN" and self.disp_unit=="Mm"):
                                 self.axes.set_xlabel('Travel (Mm)')
                                 self.axes.set_ylabel('Load (KN)')                                                         
                 elif(self.load_unit=="KN" and self.disp_unit=="Cm"):
                                 self.axes.set_xlabel('Travel (Cm)')
                                 self.axes.set_ylabel('Load (KN)')                                 
                 elif(self.load_unit=="KN" and self.disp_unit=="Inch"):
                                 self.axes.set_xlabel('Travel (Inch)')
                                 self.axes.set_ylabel('Load (KN)')
                 elif(self.load_unit=="gm" and self.disp_unit=="Mm"):
                                 self.axes.set_xlabel('Travel (Mm)')
                                 self.axes.set_ylabel('Load (gm)') 
                 else:    
                                 self.axes.set_xlabel('Travel (Mm)')
                                 self.axes.set_ylabel('Load (Kg)')
                                        
                 
                 self.axes.set_xlim(0,int(x[0]))
                 self.axes.set_ylim(0,int(x[1]))  
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
            self.test_type="Compression"
            
            if(self.test_type=="Compression"):
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
                #print("started with default motor speed . Not gohead ")
            #self.ser.write(b'*D\r\n')
            
            #time.sleep(2)
            #========Final Motor start Command =========    
            self.ser.flush()
            if(self.test_type=="Compression"):
                 print("Compression")                 
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
                print("Flexural")    
            elif(self.test_type=="COF"):
                print("COF")
            else:
                print("len(self.ybuff) :"+str(len(self.ybuff)))
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
        
        self.on_ani_start()
    
    def update_graph(self):       
        if(self.IO_error_flg==0):            
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
                #print("self.test_typexx: "+str(self.test_type))
                if(self.test_type=="Compression"):
                    self.p=int(self.test_guage_mm)-self.p
                    #print("self.p :"+str(self.p))
                elif(self.test_type=="Flexural"):
                    #self.p=self.p
                    self.p=int(self.test_guage_mm)-self.p
                else:
                    self.p=self.p
                    #self.p=int(self.test_guage_mm)-self.p
                    #self.p=self.p
                
#                if(self.unit_type == "N/mm"):    
#                        self.q=float(self.q)*9.81
#                elif(self.unit_type == "Kgf/cm"):
#                        self.p=float(self.p)/10
#                else:
#                        self.p=float(self.p)
#                        self.q=float(self.q)


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
                self.q_mpa=float(self.q)*1000
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
                self.save_data_flg="No"
            else:                
               
                self.save_data_flg="Yes"
                self.on_ani_stop()
            
                   
    def plot_grah_only(self,i):
                #print("self.load_unit :"+str(self.load_unit)+" self.disp_unit : "+str(self.disp_unit))
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
                            #print("Inside N/mm plot") 
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
                elif(self.load_unit=="gm" and self.disp_unit=="Mm"):
                            self.line_cnt.set_data(self.arr_p,self.arr_q_mpa)
                            return [self.line_cnt]
                else:    
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
                 
        else:
            print(" not Ok ")
               
                
   
 
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
        self.test_type="Tear"
        self.color=['b','r','g','y','k','c','m','b']
        #ax.set_title('Test Id=32         Samples=3       BreakLoad(Kg)=110        Length(mm)=3')         
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
              self.graph_ids.append(x[0])            
             
        connection.close()
        
#         ### Univarsal change for  Graphs #####################
#         connection = sqlite3.connect("tyr.db")
#         results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
#         for x in results:
#              ax.set_xlim(0,int(x[0]))
#              ax.set_ylim(0,int(x[1]))          
#         connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_UNIT_LOAD,LAST_UNIT_DISP,GRAPH_SCAL_X_LENGTH,GRAPH_SCAL_Y_LOAD from TEST_MST  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ") 
        for x in results:
              self.last_load_unit=str(x[0])
              self.last_disp_unit=str(x[1])
              ax.set_xlim(0,int(x[2]))
              ax.set_ylim(0,int(x[3]))  
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_TYPE from GLOBAL_VAR2") 
        for x in results:
              self.graph_type=str(x[0])  
        connection.close()
        
        
        
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
            
            
            
            
           
            connection = sqlite3.connect("tyr.db")
            if(self.graph_type=="Load Vs Travel"):
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
                    elif(self.last_load_unit=="gm" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_MPA FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
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
        print("self.graph_type :"+str(self.graph_type))
        if(self.graph_type=="Load Vs Travel"):
                ax.set_xlabel('Travel ('+str(self.last_disp_unit)+')')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        else:
                ax.set_xlabel('Strain %')
                ax.set_ylabel('Stress')
        #self.connect('motion_notify_event', mouse_move)
        ax.legend()        
        self.draw()
        self.figure.savefig('last_graph.png',dpi=100)
        
        #ax.connect('motion_notify_event', mouse_move)
    
            

class PlotCanvas_blank(FigureCanvas):
    def __init__(self, parent=None, width=1, height=0.1, dpi=80):
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
        self.test_type="Tear"
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#CCFFFF')
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
       
         
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
             ax.set_xlim(0,float(x[0]))
             ax.set_ylim(0,float(x[1]))          
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_LOAD_UNIT,LAST_DISP_UNIT from GLOBAL_VAR2") 
        for x in results:
             self.last_load_unit=str(x[0])
             self.last_disp_unit=str(x[1])  
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])  
              
        ax.plot(self.x,self.y,'b')
        ax.set_ylabel('Load  ('+str(self.last_load_unit)+')')
        ax.set_xlabel(' Travel ('+str(self.last_disp_unit)+')')
        
        
        self.draw()       
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_54_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
