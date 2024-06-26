from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow
from comment_popup import comment_Ui_MainWindow
from TY_07_UTM_MANNUAL_CONTROL_2 import  TY_07_Ui_MainWindow
from pop_peak_val import pop_peal_val_Ui_MainWindow

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

import minimalmodbus
#from minimalmodbus import BYTEORDER_LITTLE_SWAP
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
minimalmodbus.BYTEORDER_BIG= 0
minimalmodbus.BYTEORDER_LITTLE= 1

import statistics

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class TY_67_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 752)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1311, 701))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 160, 1321, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(1160, 10, 141, 31))
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
        self.pushButton_6.setGeometry(QtCore.QRect(1160, 60, 131, 41))
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
        self.frame_3.setGeometry(QtCore.QRect(10, 180, 1281, 511))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(810, 80, 101, 41))
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
        self.pushButton_11.setGeometry(QtCore.QRect(810, 30, 101, 41))
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
        self.pushButton_12.setGeometry(QtCore.QRect(810, 140, 101, 41))
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
        self.pushButton_13.setGeometry(QtCore.QRect(810, 380, 101, 41))
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
        self.pushButton_14.setGeometry(QtCore.QRect(810, 320, 101, 41))
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
        self.pushButton_15.setGeometry(QtCore.QRect(810, 260, 101, 41))
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
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(930, 110, 341, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        font.setFamily("Arial")
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
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_16.setGeometry(QtCore.QRect(810, 200, 101, 41))
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
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber.setGeometry(QtCore.QRect(1030, 360, 191, 51))
        self.lcdNumber.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_41 = QtWidgets.QLabel(self.frame_3)
        self.label_41.setGeometry(QtCore.QRect(1230, 360, 41, 51))
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
        self.lcdNumber_2.setGeometry(QtCore.QRect(1030, 430, 191, 51))
        self.lcdNumber_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_42 = QtWidgets.QLabel(self.frame_3)
        self.label_42.setGeometry(QtCore.QRect(1240, 430, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("")
        self.label_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
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
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_18.setGeometry(QtCore.QRect(810, 440, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_18.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_18.setFlat(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(930, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(1000, 20, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(1070, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(1170, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(940, 360, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setGeometry(QtCore.QRect(940, 420, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(930, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        
        
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_3.setGeometry(QtCore.QRect(1040, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-color: rgb(213, 248, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        
        self.pushButton_8_1 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8_1.setGeometry(QtCore.QRect(1170, 60, 100, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8_1.setFont(font)
        self.pushButton_8_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))        
        self.pushButton_8_1.setFlat(False)
        self.pushButton_8_1.setObjectName("pushButton_8_1")
        
        self.pushButton_8_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8_2.setGeometry(QtCore.QRect(930, 325, 80, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8_2.setFont(font)
        self.pushButton_8_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))        
        self.pushButton_8_2.setFlat(False)
        self.pushButton_8_2.setObjectName("pushButton_8_2")
        
        
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(1160, 120, 131, 41))
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
        self.pushButton_9.setGeometry(QtCore.QRect(10, 110, 111, 41))
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
        self.label_11.setGeometry(QtCore.QRect(10, 20, 61, 21))
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
        self.label_12.setGeometry(QtCore.QRect(80, 20, 61, 21))
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
        self.label_13.setGeometry(QtCore.QRect(160, 10, 101, 31))
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
        self.comboBox.setGeometry(QtCore.QRect(280, 10, 191, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
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
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(140, 0, 20, 171))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(490, 0, 20, 171))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(680, 30, 71, 31))
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
        self.label_21.setGeometry(QtCore.QRect(520, 30, 81, 31))
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
        self.lineEdit_9.setGeometry(QtCore.QRect(610, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        
        
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(760, 0, 20, 171))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        
        
        self.label_29 = QtWidgets.QLabel(self.frame)        
        self.label_29.setGeometry(QtCore.QRect(510, 95, 91, 31))
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
        self.comboBox_2.setGeometry(QtCore.QRect(610, 95, 71, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")       
        
        
        self.label_29_1 = QtWidgets.QLabel(self.frame)        
        self.label_29_1.setGeometry(QtCore.QRect(510, 135, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29_1.setFont(font)
        self.label_29_1.setText("Max. Length :")
        self.label_29_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29_1.setObjectName("label_29_1")
        
        
        self.lineEdit_9_1 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_9_1)
        self.lineEdit_9_1.setValidator(input_validator)
        self.lineEdit_9_1.setGeometry(QtCore.QRect(610, 135, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9_1.setFont(font)
        self.lineEdit_9_1.setObjectName("lineEdit_9_1")
        
        self.label_29_2 = QtWidgets.QLabel(self.frame)        
        self.label_29_2.setGeometry(QtCore.QRect(650, 135, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29_2.setFont(font)
        self.label_29_2.setText("(Mm)")
        self.label_29_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29_2.setObjectName("label_29_2")
        
        
        
        
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(1140, 0, 20, 171))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(770, 40, 51, 31))
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
        self.lineEdit_13.setGeometry(QtCore.QRect(840, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(770, 80, 51, 31))
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
        self.lineEdit_14.setGeometry(QtCore.QRect(840, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(800, 120, 131, 41))
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
        self.lineEdit_15.setGeometry(QtCore.QRect(280, 90, 191, 31))
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
        self.lineEdit_16.setGeometry(QtCore.QRect(280, 130, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_45 = QtWidgets.QLabel(self.frame)
        self.label_45.setGeometry(QtCore.QRect(820, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("")
        self.label_45.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(980, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_17.setStyleSheet("background-color: rgb(148, 255, 166);\n"
"background-color: rgb(251, 234, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_17.setFlat(False)
        self.pushButton_17.setObjectName("pushButton_17")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setGeometry(QtCore.QRect(500, 70, 271, 20))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setObjectName("line_9")
        self.label_63 = QtWidgets.QLabel(self.frame)
        self.label_63.setGeometry(QtCore.QRect(910, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("")
        self.label_63.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_63.setObjectName("label_63")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(910, 40, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("")
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(110, 59, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(10, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_25.setGeometry(QtCore.QRect(280, 50, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setText("")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(970, 70, 151, 61))
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
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(970, 130, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
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
        self.label_47.setText(_translate("MainWindow", "05 Aug 2020 14:23:00"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.pushButton_7.setText(_translate("MainWindow", "Stop"))
        self.pushButton_11.setText(_translate("MainWindow", "Start"))
        self.pushButton_12.setText(_translate("MainWindow", "All Graphs"))
        self.pushButton_13.setText(_translate("MainWindow", "View Report"))
        self.pushButton_14.setText(_translate("MainWindow", "Email"))
        self.pushButton_15.setText(_translate("MainWindow", "Comment"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Median(Kgf)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Range-From"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Range-To"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Peak Count"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Rec. No"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "100"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "123.8"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "200"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "300"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "400"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "500"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_16.setText(_translate("MainWindow", "Print"))
        self.label_41.setText(_translate("MainWindow", "Kgf."))
        self.label_42.setText(_translate("MainWindow", "Sec."))
        self.label_49.setText(_translate("MainWindow", "Data Saved Successfully ......"))
        self.pushButton_18.setText(_translate("MainWindow", "Peaks Data"))
        self.label_15.setText(_translate("MainWindow", "Load Cell :"))
        self.label_16.setText(_translate("MainWindow", "High"))
        self.label_17.setText(_translate("MainWindow", "Length Device : "))
        self.label_18.setText(_translate("MainWindow", "Extensometer"))
        self.label_22.setText(_translate("MainWindow", "Load :"))
        self.label_23.setText(_translate("MainWindow", "Time :"))
        self.label_19.setText(_translate("MainWindow", "Test Method:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Method A"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Method B"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Method C"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Method D"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Method E"))
        self.pushButton_8.setText(_translate("MainWindow", "Go For Test"))
        self.pushButton_8_1.setText(_translate("MainWindow", "Get-Results"))
        self.pushButton_8_2.setText(_translate("MainWindow", "Refresh"))
        
        self.pushButton_9.setText(_translate("MainWindow", "Reset"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "0001"))
        self.label_13.setText(_translate("MainWindow", "Spec.Name:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "spec-1254"))
        self.comboBox.setItemText(1, _translate("MainWindow", "spec-8788"))
        self.comboBox.setItemText(2, _translate("MainWindow", "spec-6543"))
        self.comboBox.setItemText(3, _translate("MainWindow", "spec-878"))
        self.label_14.setText(_translate("MainWindow", "Customer Name:"))
        self.label_20.setText(_translate("MainWindow", "(mm/min)"))
        self.label_21.setText(_translate("MainWindow", "Test Speed: "))
        self.label_29.setText(_translate("MainWindow", "Load Unit: "))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Kg"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Lb"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "N"))       
        self.label_31.setText(_translate("MainWindow", "X-axis: "))
        self.label_32.setText(_translate("MainWindow", "Y-axis: "))
        self.pushButton_10.setText(_translate("MainWindow", "Set Graph"))
        self.label_35.setText(_translate("MainWindow", "Job Id :"))
        self.label_36.setText(_translate("MainWindow", "Batch Number :"))
        self.label_45.setText(_translate("MainWindow", "Graph Scale "))
        self.pushButton_17.setText(_translate("MainWindow", "Set Sample"))
        self.label_63.setText(_translate("MainWindow", "(Kgf)"))
        self.label_37.setText(_translate("MainWindow", "(Sec)"))
        self.label_26.setText(_translate("MainWindow", "0"))
        self.label_28.setText(_translate("MainWindow", "Spec. Count:"))
        self.label_10.setText(_translate("MainWindow", "Tear Strength"))
        self.label_24.setText(_translate("MainWindow", ""))
        self.comboBox.currentTextChanged.connect(self.onchage_combo)
        #self.comboBox_4.currentTextChanged.connect(self.show_graph)
        
      
        self.pushButton_8.clicked.connect(self.go_for_test)
        self.pushButton_8_1.clicked.connect(self.get_results)
        self.pushButton_8_2.clicked.connect(self.show_grid_data_Tear) 
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_9.clicked.connect(self.new_test_reset)
        self.pushButton_18.clicked.connect(self.open_graph_data)
        self.pushButton_10.clicked.connect(self.set_graph_scale)
        self.pushButton_11.clicked.connect(self.start_test)
        self.tableWidget.doubleClicked.connect(self.delete_cycle)
        
        self.pushButton_13.clicked.connect(self.open_pdf)
        self.pushButton_16.clicked.connect(self.print_file)
        self.pushButton_14.clicked.connect(self.open_email_report)
        self.pushButton_15.clicked.connect(self.open_comment_popup)
        self.pushButton_12.clicked.connect(self.show_all_specimens)        
        self.pushButton_7.clicked.connect(self.manual_stop)
        self.pushButton_17.clicked.connect(self.open_manual_control)
        self.comboBox_2.currentTextChanged.connect(self.load_unit_onchange)
        #self.radioButton.clicked.connect(self.radiobutt_on_change)
        #self.radioButton_2.clicked.connect(self.radiobutt_on_change)
        
        self.test_method=""                             
        self.failure_mod=""
        self.tmperature=""
        self.test_type_for_flexural=""
        self.remark=""
        self.modbus_flag=""
        self.modbus_port=""
        self.non_modbus_port=""
        
        
        self.load_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.frame_3.hide()
        #self.show_grid_data_Tear()
        #self.tableWidget.setHorizontalHeaderLabels(['Thickness (mm)',' Peak Load (Kgf) ','Tear Strength (Kgf/Cm)','Created On','Cycle ID'])
        #self.tableWidget.setHorizontalHeaderLabels([' Peak Load ('+str(self.comboBox_2.currentText())+') ','cycle_id'])        
        
        self.pushButton_9.setDisabled(True)
        self.pushButton_8_1.setDisabled(True)
        self.comboBox_3.setDisabled(True)
    
    def load_unit_onchange(self):
        self.label_63.setText("("+str(self.comboBox_2.currentText())+")")
        
        
    def device_date(self):     
        self.label_47.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    
            
        
    def new_test_reset(self):
        self.cycle_num=0
        self.label_26.setText(str(self.cycle_num))
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
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'TEST_MST'")       
        for x in results:           
                 self.label_12.setText(str(x[0]).zfill(3))
                 self.test_id=str(x[0])
                 self.lineEdit_15.setText("Job_Name_"+str(x[0]).zfill(3))
                 self.lineEdit_16.setText("Batch_"+str(x[0]).zfill(3))
        connection.close()
        self.i=0
        self.comboBox.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SPECIMEN_NAME FROM SPECIMEN_MST ") 
        for x in results:            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 FROM SETTING_MST") 
        for x in results:            
            self.lineEdit_13.setText(str(x[0]))
            self.lineEdit_14.setText(str(x[1]))
        connection.close()
        
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT PROOF_MAX_LENGTH FROM GLOBAL_VAR") 
        for x in results:            
            self.lineEdit_9_1.setText(str(x[0]))           
        connection.close()

        
        self.sc_blank =PlotCanvas_blank(self) 
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        
        self.onchage_combo()
        self.label_49.setText("Start Test Please.")
        self.label_49.show()
        #self.frame_3.hide()
        #print("Timer4 Status :"+str(self.timer4.isActive()))
        self.pushButton_12.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setDisabled(True)
        self.pushButton_15.setDisabled(True)
        self.pushButton_16.setDisabled(True)
        self.pushButton_18.setDisabled(True)
        
        self.label_41.setText(str(self.comboBox_2.currentText()))
        #self.label_42.setText(str(self.comboBox_3.currentText() ))
        self.lcdNumber.setProperty("value", 0.0)     #load
        self.lcdNumber_2.setProperty("value",0.0)  #length
        #self.lcdNumber_3.setProperty("value",0.0)  #speed
        
        self.pushButton_7.setDisabled(True)
        self.pushButton_11.setEnabled(True)
        #self.show_grid_data_Tear()
        print("Data Loaded OK !!")
       
    
    
    def validations(self):        
        self.go_ahead="No"
        self.msg=""
        
        if(self.lineEdit_25.text() == ""):
              self.msg="Customer Name Should not Empty."              
              print("ok")
        else:
               self.go_ahead="Yes"       
               if(self.go_ahead=="Yes"):    
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
                                            cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(int(self.label_12.text()))+"'")
                                    connection.commit();
                                    connection.close()
                                    
                           else:        
                                    ### INSERT 
                                    connection = sqlite3.connect("tyr.db")              
                                    with connection:        
                                            cursor = connection.cursor()
                                            cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(int(self.label_12.text()))+"'")
                                            cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_PARTY_NAME='"+str(self.lineEdit_25.text())+"',NEW_TEST_MOTOR_SPEED='"+self.lineEdit_9.text()+"',PROOF_MAX_LENGTH='"+self.lineEdit_9_1.text()+"'")
                                            cursor.execute("INSERT INTO TEST_MST(SPECIMEN_NAME,TEST_TYPE,MOTOR_SPEED,PARTY_NAME,BATCH_ID,JOB_NAME) VALUES('"+str(self.comboBox.currentText())+"','TEAR_STRENGTH','"+str(self.lineEdit_9.text())+"','"+str(self.lineEdit_25.text())+"','"+str(self.lineEdit_16.text())+"','"+str(self.lineEdit_15.text())+"')")
                                            cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_Y_LOAD='"+self.lineEdit_14.text()+"',GRAPH_SCAL_X_LENGTH='"+self.lineEdit_13.text()+"'  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                                            cursor.execute("UPDATE TEST_MST SET LAST_UNIT_LOAD='"+str(self.comboBox_2.currentText())+"',LAST_UNIT_DISP='"+str(self.comboBox_3.currentText())+"'  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                                            cursor.execute("UPDATE TEST_MST SET TESTED_BY=(SELECT LOGIN_USER_NAME FROM GLOBAL_VAR)  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                                          
                                    connection.commit();
                                    connection.close()
       
    
                       
                       
    def readonly_fields(self):
        self.comboBox.setDisabled(True)
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_16.setReadOnly(True)
        #self.lineEdit_8.setReadOnly(True)
        self.lineEdit_9.setReadOnly(True)
        self.comboBox_2.setDisabled(True)
        #self.comboBox_3.setDisabled(True)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_14.setReadOnly(True)
    
    def readWrite_fields(self):
        self.comboBox.setEnabled(True)
        self.lineEdit_15.setReadOnly(False)
        self.lineEdit_16.setReadOnly(False)
        #self.lineEdit_8.setReadOnly(False)
        self.lineEdit_9.setReadOnly(False)
        self.comboBox_2.setEnabled(True)
        self.comboBox_3.setEnabled(True)
        self.lineEdit_13.setReadOnly(False)
        self.lineEdit_14.setReadOnly(False)
        
    
    def go_for_test(self):
        #print("Old object status :"+str(self.timer31.isActive()))
        self.label_24.hide()
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
                            connection = sqlite3.connect("tyr.db")
                            results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE,ISACTIVE_MODBUS,MODBUS_PORT,NON_MODBUS_PORT from SETTING_MST") 
                            for x in results:
                                 self.modbus_flag=str(x[4])
                                 self.modbus_port=str(x[5])
                                 self.non_modbus_port=str(x[6])
                            connection.close()
                            
                           
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
                            self.pushButton_8.setDisabled(True)
                            #self.pushButton_6.setDisabled(True)
                            self.readonly_fields()
                            self.show_lcd_vals="N"
                            
                            
                            
                        except IOError:
                            print("IO Errors")
                 else:
                         self.frame_3.hide()
        
        
        self.show_grid_data_Tear()
        self.label_41.setText(str(self.comboBox_2.currentText()))
        #self.label_42.setText(str(self.comboBox_3.currentText()))
        
        
    
    
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
                
           
            
            
            if(self.load_cell_hi==1):
                self.label_16.setText("(High)")
                if(self.extiometer==1):
                        self.label_18.setText("(Extensometer)")
                else:        
                        self.label_18.setText("(Encoder)")            
            else:
                self.label_16.setText("(Low)")
                if(self.extiometer==1):
                        self.label_18.setText("(Extensometer)")
                else:        
                        self.label_18.setText("(Encoder)")
    
    
    def save_units(self):
        connection = sqlite3.connect("tyr.db")
        with connection:        
           cursor = connection.cursor()
           cursor.execute("UPDATE GLOBAL_VAR2 SET LAST_LOAD_UNIT='"+str(str(self.comboBox_2.currentText()))+"', LAST_DISP_UNIT='"+str(self.comboBox_3.currentText())+"'")
           cursor.execute("UPDATE SPECIMEN_MST SET LAST_UNIT_LOAD='"+str(str(self.comboBox_2.currentText()))+"', LAST_UNIT_DISP='"+str(self.comboBox_3.currentText())+"'   where SPECIMEN_NAME = '"+str(self.comboBox.currentText())+"'")
           print("Units set Ok !!")          
           
        connection.commit();
        connection.close()
        
                                 
    
    def onchage_combo(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select PARTY_NAME,MOTOR_SPEED,LAST_UNIT_LOAD,LAST_UNIT_DISP FROM SPECIMEN_MST WHERE SPECIMEN_NAME='"+self.comboBox.currentText()+"'")
        for x in results:
            self.lineEdit_25.setText(str(x[0])) # CUSTOMER NAME
            self.lineEdit_15.setText(str("Job_ID_")+str(self.test_id)) # JOB ID
            self.lineEdit_16.setText(str("Batch_ID_")+str(self.test_id)) # BATCH ID            
            self.lineEdit_9.setText(str(x[1])) # TEST SPEED                    
            self.comboBox_2.setCurrentText(str(x[2])) #UNIT_LOAD           
        connection.close()
        
        
    def set_graph_scale(self):        
        self.x_axis_val=0.0
        self.x_axis_val_CM=0.0
        self.x_axis_val_INCH=0.0
        self.y_axis_val=0.0
        self.y_axis_val_N=0.0
        self.y_axis_val_LB=0.0
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
           self.frame_3.hide()
           self.pushButton_8.setEnabled(True)
           self.pushButton_9.setEnabled(True)
        connection.commit();
        connection.close()
        
        self.y_axis_val=float(self.y_axis_val)            
        #elif(str(self.comboBox_2.currentText())== "KN"  and str(self.comboBox_3.currentText())== "Cm"):
        if(self.comboBox_2.currentText()== "Kg"):
            self.y_axis_val=float(self.y_axis_val)
            self.y_axis_val_N=(self.y_axis_val)*9.80665  #Kg to N
            self.y_axis_val_LB=(self.y_axis_val)*2.20462  #Kg to Lb
        elif(self.comboBox_2.currentText()== "N"):
            self.y_axis_val_N=self.y_axis_val           
            self.y_axis_val_LB=(self.y_axis_val)*0.2248090795   #N to LB
            self.y_axis_val=(self.y_axis_val)*0.1019716    # N to KG
        elif(self.comboBox_2.currentText()== "MPa"):
            self.y_axis_val=float(self.y_axis_val)
            self.y_axis_val_N=(self.y_axis_val)*9.80665  #Kg to N
            self.y_axis_val_LB=(self.y_axis_val)*2.20462  #Kg to Lb
        elif(self.comboBox_2.currentText()== "Lb"):
            self.y_axis_val_LB=self.y_axis_val
            self.y_axis_val_N=(self.y_axis_val)*4.4482189159  #LB to Newton
            self.y_axis_val=(self.y_axis_val)*0.45359237  #LB to Kg            
        else:
            self.y_axis_val=0.0
            self.y_axis_val_N=0.0
            self.y_axis_val_LB=0.0
            
        self.x_axis_val=float(self.x_axis_val)        
        if(self.comboBox_3.currentText()== "Mm"):
             self.x_axis_val=float(self.x_axis_val)
             self.x_axis_val_CM=float(self.x_axis_val)*0.1  # Mm to CM 
             self.x_axis_val_INCH=float(self.x_axis_val)*0.0393701 # MM to Inch              
        elif(self.comboBox_3.currentText()== "Cm"):
             self.x_axis_val_CM=float(self.x_axis_val)
             self.x_axis_val=float(self.x_axis_val)*10  #Cm to Mm 
             self.x_axis_val_INCH=float(self.x_axis_val)*0.393701 # CM to Inch
        elif(self.comboBox_3.currentText()== "Inch"):
             self.x_axis_val_INCH=float(self.x_axis_val)
             self.x_axis_val=float(self.x_axis_val)*25.4 #Inch to Mm 
             self.x_axis_val_CM=float(self.x_axis_val)*2.54 # inch to CM
        else:
             self.x_axis_val=0.0
             self.x_axis_val_CM=0.0
             self.x_axis_val_INCH=0.0
        
        connection = sqlite3.connect("tyr.db")
        with connection:        
           cursor = connection.cursor()
           cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_X_LENGTH='"+str(self.x_axis_val)+"', GRAPH_SCAL_Y_LOAD='"+str(self.y_axis_val)+"' WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")
           cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_X_LENGTH_CM='"+str(self.x_axis_val_CM)+"', GRAPH_SCAL_Y_LOAD_N='"+str(self.y_axis_val_N)+"' WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")
           cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_X_LENGTH_INCH='"+str(self.x_axis_val_INCH)+"', GRAPH_SCAL_Y_LOAD_LB='"+str(self.y_axis_val_LB)+"' WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")
           print("Conversion of Graph Scale is Ok !!")
           self.label_24.setText("Graph Scale Set Ok")
           self.label_24.show()
        connection.commit();
        connection.close()
        
        
    
    
    def manual_stop(self):
        self.sc_new.save_data_flg="Yes"
        self.sc_new.on_ani_stop()
        self.reset()
        self.save_graph_data()        
        try:
            self.sc_new.ser.write(b'*Q\r')
        except IOError:
            print("IO Errors")    
#         self.reset()
#         self.save_graph_data()
#         self.sc_new.save_data_flg=""
        self.label_49.setText("Mannual stopped new.")
        self.label_49.show()
        self.pushButton_7.setDisabled(True)
        self.pushButton_11.setEnabled(True)
        self.label_26.setText(str(self.cycle_num))
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
        #self.lcdNumber_3.setProperty("value",0.0)  #speed
    
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
                    if(str(self.comboBox_2.currentText()) =="Kg"):
                               self.lcdNumber.setProperty("value", str(self.sc_new.q))
                    elif(str(self.comboBox_2.currentText()) =="Lb"):   
                               self.lcdNumber.setProperty("value", str(self.sc_new.q_lb))
                    elif(str(self.comboBox_2.currentText()) =="N"):   
                               self.lcdNumber.setProperty("value", str(self.sc_new.q_n))
                    else:
                               self.lcdNumber.setProperty("value", str(self.sc_new.q))
                                        #load
                    self.lcdNumber_2.setProperty("value", str(self.sc_new.t))
                    #self.lcdNumber_3.setProperty("value",str(max(self.sc_new.arr_speed)))
                    #self.lcdNumber_3.setProperty("value",str(self.lineEdit_8.text()))
                    self.pushButton_11.setDisabled(True)
                    self.pushButton_7.setEnabled(True)
                    self.pushButton_6.setDisabled(True)
                    #print("lcd printing .......")
                    if(str(self.sc_new.save_data_flg) =="Yes"):
                            self.reset()
                            #self.save_graph_data()
                            self.sc_new.save_data_flg=""
                            self.label_49.setText("Please Click on Get-Results...to view results")
                            self.label_49.show()
                            self.pushButton_7.setDisabled(True)                           
                            self.comboBox_3.setEnabled(True)
                            self.pushButton_8_1.setEnabled(True)
                                                          
                            
        else:
                           self.lcdNumber.setProperty("value", 0.0)     #load
                           self.lcdNumber_2.setProperty("value",0.0)  #length
                           #self.lcdNumber_3.setProperty("value",0.0)  #speed
                
    def get_results(self):
        self.save_graph_data()
        self.pushButton_11.setEnabled(True)        
        self.pushButton_12.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_14.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        self.pushButton_16.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_18.setEnabled(True)
        
        self.label_49.setText("Results are Calculated.")
        self.label_49.show()
        self.label_26.setText(str(self.cycle_num))
        
        
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
        
        print("1561 check........")  
        if( str(self.comboBox_3.currentText()) =="Cm"):         
                self.cs_area=self.cs_area*0.1*0.1       
        elif( str(self.comboBox_3.currentText()) =="Inch"):
                self.cs_area=self.cs_area*0.0393701
        else:                
                self.cs_area=1
        
        print("len of arr........"+str(len(self.sc_new.arr_p))) 
        if (len(self.sc_new.arr_p) > 1):            
            #### Get Guage length
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              cursor.execute("DELETE FROM STG_TEST_DATA")
              cursor.execute("DELETE FROM STG_PEAK_MST") 
              cursor.execute("DELETE FROM STG_LOW_VAL_MST")
              #cursor.execute("DELETE FROM TEST_DATA WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) and SPEC_ID = '"+str(int(self.label_26.text()))+"'")
            connection.commit();
            connection.close()
            
            ###### Spec ID ###################
            self.cycle_num=0
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("select IFNULL(MAX(SPEC_ID),0) FROM TEST_DATA WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")                 
            for x in results:
                       self.cycle_num=int(str(x[0]))       
            connection.close()                     
            ####################################
            
            
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)):
                   cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_LB,Y_NUM_KN,Y_NUM_MPA,T_SEC) VALUES ('"+str(float(self.sc_new.arr_t[g]))+"','"+str(float(self.sc_new.arr_p_cm[g]))+"','"+str(float(self.sc_new.arr_p_inch[g]))+"','"+str(self.sc_new.arr_q[g])+"','"+str(self.sc_new.arr_q_n[g])+"','"+str(self.sc_new.arr_q_lb[g])+"','"+str(self.sc_new.arr_q_kn[g])+"','"+str(self.sc_new.arr_q_mpa[g])+"','"+str(float(self.sc_new.arr_t[g]))+"')")
                  
            connection.commit();
            connection.close()
            self.populate_peak_loads()
            
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.peak_val_arr)):
                   cursor.execute("INSERT INTO STG_PEAK_MST(PEAK_VALUE,ID,TIME_VAL) VALUES ('"+str(float(self.peak_val_arr[g]))+"','"+str(g+1)+"','"+str(float(self.time_val_arr[g]))+"')")                  
            connection.commit();
            connection.close()
            
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.low_val_arr)):
                   cursor.execute("INSERT INTO STG_LOW_VAL_MST(LOW_VAL,ID) VALUES ('"+str(float(self.low_val_arr[g]))+"','"+str(g)+"')")                  
            connection.commit();
            connection.close()
       
        if (len(self.sc_new.arr_p) > 1):           
            self.cycle_num=self.cycle_num+1 
            connection = sqlite3.connect("tyr.db")              
            with connection:
                  cursor = connection.cursor()
                  print("0 Data saved........")
                  try:
                          cursor.execute("INSERT INTO GRAPH_MST(X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_MPA,Y_NUM_LB,Y_NUM_KN,T_SEC) SELECT X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_MPA,Y_NUM_LB,Y_NUM_KN,T_SEC FROM STG_GRAPH_MST")
                          cursor.execute("UPDATE GRAPH_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")
                          cursor.execute("UPDATE STG_PEAK_MST SET PEAK_LIST_ID = (SELECT MAX(IFNULL(PEAK_LIST_ID+1,0)) FROM PEAK_MST)")
                          cursor.execute("UPDATE STG_PEAK_MST SET TEST_METHOD_TYPE = '"+str(self.comboBox_3.currentText())+"'")
                          cursor.execute("INSERT INTO PEAK_MST(SQ_NO,PEAK_VAL,PEAK_LIST_ID,TEST_METHOD_TYPE,TIME_VAL,COMMENT,IGNORE_FLG,GRAPH_ID) SELECT ID,PEAK_VALUE,PEAK_LIST_ID,TEST_METHOD_TYPE,TIME_VAL,COMMENT,IGNORE_FLG,(SELECT MAX(IFNULL(GRAPH_ID,0)) FROM GRAPH_MST) FROM STG_PEAK_MST")         
                          cursor.execute("UPDATE TEST_MST SET STATUS='LOADED GRAPH' WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")                          
                          cursor.execute("INSERT INTO STG_TEST_DATA(TEST_ID) SELECT TEST_ID FROM GLOBAL_VAR")
                          cursor.execute("UPDATE STG_TEST_DATA SET TEST_ID = (SELECT TEST_ID FROM GLOBAL_VAR) ")
                          cursor.execute("UPDATE STG_TEST_DATA SET SPEC_ID = '"+str(self.cycle_num)+"'")                                      
                          cursor.execute("UPDATE STG_TEST_DATA SET GRAPH_ID = (SELECT MAX(IFNULL(GRAPH_ID,0)) FROM GRAPH_MST)")
                          cursor.execute("UPDATE STG_LOW_VAL_MST SET GRAPH_ID = (SELECT MAX(IFNULL(GRAPH_ID,0)) FROM GRAPH_MST)")
                          cursor.execute("INSERT INTO LOW_VAL_MST(LOW_VAL,GRAPH_ID) SELECT LOW_VAL,GRAPH_ID FROM STG_LOW_VAL_MST")
                          cursor.execute("UPDATE STG_TEST_DATA SET TEST_METHOD_TYPE = '"+str(self.comboBox_3.currentText())+"'")
                          cursor.execute("UPDATE STG_TEST_DATA SET PEAK_LIST_ID = (SELECT MAX(IFNULL(PEAK_LIST_ID,0)) FROM PEAK_MST)")                          
                          cursor.execute("INSERT INTO TEST_DATA(TEST_ID,MEDIAN,RANGE_FROM,RANGE_TO,GRAPH_ID,SPEC_ID,TEST_METHOD_TYPE,PEAK_LIST_ID) SELECT TEST_ID,MEDIAN,RANGE_FROM,RANGE_TO,GRAPH_ID,SPEC_ID,TEST_METHOD_TYPE,PEAK_LIST_ID FROM STG_TEST_DATA")                    
                          
                          print("Data saved........")
                  except Exception as e:
                                     print("SQL Error :"+str(e))
                                     connection.commit();
            
            connection.commit();
            connection.close()
            
            if(str(self.comboBox_3.currentText()) == "Method A"):
                   self.test_method_A_calc()
            elif(str(self.comboBox_3.currentText()) == "Method B"):
                   self.test_method_B_calc()
            elif(str(self.comboBox_3.currentText()) == "Method C"):
                   self.test_method_C_calc()
            elif(str(self.comboBox_3.currentText()) == "Method D"): 
                   self.test_method_D_calc()
            elif(str(self.comboBox_3.currentText()) == "Method E"): 
                   self.test_method_E_calc() 
            else:
                   self.test_method_A_calc()
            
        
        #self.load_data()
        #print("Save completed")
        self.show_grid_data_Tear()
    
    def populate_peak_loads(self):        
        #### Get All records based on rec id ascending
        self.load_vals=[]
        self.time_vals=[]        
        self.rec_id=[]
        self.UP_DWON_FLAG=""
        self.UP_COUNT=0
        self.DOWN_COUNT=0
        self.peak_val_arr=[]
        self.time_val_arr=[]
        self.low_val_arr=[]
        
        connection = sqlite3.connect("tyr.db")
        if(str(self.comboBox_2.currentText()) =="Kg"):
             results=connection.execute("SELECT round(Y_NUM,2),REC_ID,round(X_NUM,2) FROM STG_GRAPH_MST order by REC_ID ASC")
        elif(str(self.comboBox_2.currentText()) =="Lb"):
             results=connection.execute("SELECT round(Y_NUM_LB,2),REC_ID,round(X_NUM,2) FROM STG_GRAPH_MST order by REC_ID ASC")
        elif(str(self.comboBox_2.currentText()) =="N"):
             results=connection.execute("SELECT round(Y_NUM_N,2),REC_ID,round(X_NUM,2) FROM STG_GRAPH_MST order by REC_ID ASC")
        else:
             results=connection.execute("SELECT round(Y_NUM,2),REC_ID,round(X_NUM,2) FROM STG_GRAPH_MST order by REC_ID ASC")
        for x in results:
              self.load_vals.append(float(x[0]))
              self.rec_id.append(int(x[1]))
              self.time_vals.append(int(x[2]))
        connection.close()   
        
        for x in range(len(self.rec_id)-1):
             if(self.load_vals[x] < self.load_vals[x+1]):
                 #print("ID: "+str(x)+"  ....self.UP_DWON_FLAG : UP")
                 self.UP_DWON_FLAG="UP"
                 self.UP_COUNT=self.UP_COUNT+1
                 if(self.DOWN_COUNT > 0):
                     self.low_val_arr.append(self.load_vals[x])                    
                     self.DOWN_COUNT=0
             else:
                 #print("ID: "+str(x)+"  ....self.UP_DWON_FLAG : DOWN")
                 self.UP_DWON_FLAG="DOWN"
                 self.DOWN_COUNT=self.DOWN_COUNT+1
                 if(self.UP_COUNT > 0):
                     self.peak_val_arr.append(self.load_vals[x])
                     self.time_val_arr.append(self.time_vals[x])
                     self.UP_COUNT=0
                 
        #self.peak_val_arr.sort()
        #print("All Peak Values :"+str(self.peak_val_arr))    
    def test_method_A_calc(self):
        self.load_vals_A=[]        
        self.med = 0
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT PEAK_VALUE FROM STG_PEAK_MST order by ID ASC")
        for x in results:
              self.load_vals_A.append(float(x[0]))              
        connection.close()
        try:
            self.med = statistics.median(self.load_vals_A)
        except Exception as e:
                             print("median Error :"+str(e))   
        print("Median A :"+str(self.med))
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        cursor.execute("UPDATE TEST_DATA SET MEDIAN = '"+str(self.med)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")                          
                        cursor.execute("UPDATE TEST_DATA SET RANGE_FROM = (SELECT MIN(PEAK_VALUE) FROM STG_PEAK_MST) WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                        cursor.execute("UPDATE TEST_DATA SET RANGE_TO = (SELECT MAX(PEAK_VALUE) FROM STG_PEAK_MST) WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                  except Exception as e:
                           print("SQL Error- test_method_A_calc() :"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()                   
        
    def test_method_B_calc(self):
        self.load_vals_B=[]
        self.time_vals_B=[]
        self.t1=0
        self.t2=0
        self.time_diff=0
        self.med = 0
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TIME_VAL FROM STG_PEAK_MST WHERE ID = 1")
        for x in results:
              self.t1=(float(x[0]))              
        connection.close() 
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TIME_VAL FROM STG_PEAK_MST order by ID DESC LIMIT 1")
        for x in results:
              self.t2=(float(x[0]))              
        connection.close() 
        
        self.time_diff=(self.t2)-(self.t1)
        self.t1=(self.t1)+(0.1*(self.time_diff))
        self.t2=(self.t2)-(0.1*(self.time_diff))
        
        
        connection = sqlite3.connect("tyr.db")
        print("SELECT PEAK_VALUE FROM STG_PEAK_MST WHERE TIME_VAL BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' order by ID ASC")
        
        results=connection.execute("SELECT PEAK_VALUE FROM STG_PEAK_MST WHERE TIME_VAL BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' order by ID ASC")
        for x in results:
              self.load_vals_B.append(float(x[0]))              
        connection.close()   
        
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        print("UPDATE PEAK_MST SET COMMENT  = 'IGNORED BY 10PER',IGNORE_FLG='Y' WHERE TIME_VAL NOT BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' AND GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")              
                        cursor.execute("UPDATE PEAK_MST SET COMMENT  = 'IGNORED BY 10PER',IGNORE_FLG='Y' WHERE TIME_VAL NOT BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' AND GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                        cursor.execute("UPDATE STG_PEAK_MST SET COMMENT  = 'IGNORED BY 10PER',IGNORE_FLG='Y' WHERE TIME_VAL NOT BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"'")

                  except Exception as e:
                           print("SQL Error- Update:"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()
        
        
        self.med = statistics.median(self.load_vals_B)
        print("Median A :"+str(self.med))
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        cursor.execute("UPDATE TEST_DATA SET MEDIAN = '"+str(self.med)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")                          
                        cursor.execute("UPDATE TEST_DATA SET RANGE_FROM = (SELECT MIN(PEAK_VALUE) FROM STG_PEAK_MST WHERE IGNORE_FLG = 'N') WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                        cursor.execute("UPDATE TEST_DATA SET RANGE_TO = (SELECT MAX(PEAK_VALUE) FROM STG_PEAK_MST WHERE IGNORE_FLG = 'N') WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                  except Exception as e:
                           print("SQL Error- test_method_B_calc() :"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()
        
        
    def test_method_C_calc(self):
        self.load_vals_B=[]
        self.time_vals_B=[]
        self.t1=0
        self.t2=0
        self.time_diff=0
        self.med = 0
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TIME_VAL FROM STG_PEAK_MST WHERE ID = 1")
        for x in results:
              self.t1=(float(x[0]))              
        connection.close() 
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TIME_VAL FROM STG_PEAK_MST order by ID DESC LIMIT 1")
        for x in results:
              self.t2=(float(x[0]))              
        connection.close() 
        
        self.time_diff=(self.t2)-(self.t1)
        self.t1=(self.t1)+(0.1*(self.time_diff))
        self.t2=(self.t2)-(0.1*(self.time_diff))
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT PEAK_VALUE FROM STG_PEAK_MST WHERE TIME_VAL BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' order by ID ASC")
        for x in results:
              self.load_vals_B.append(float(x[0]))              
        connection.close()   
        
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        print("UPDATE PEAK_MST SET COMMENT  = 'IGNORED BY 10PER',IGNORE_FLG='Y' WHERE TIME_VAL NOT BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' AND GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")              
                        cursor.execute("UPDATE PEAK_MST SET COMMENT  = 'IGNORED BY 10PER',IGNORE_FLG='Y' WHERE TIME_VAL NOT BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' AND GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                        cursor.execute("UPDATE STG_PEAK_MST SET COMMENT  = 'IGNORED BY 10PER',IGNORE_FLG='Y' WHERE TIME_VAL NOT BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"'")

                  except Exception as e:
                           print("SQL Error- Update:"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()
        
        
        
        self.med = statistics.median(self.load_vals_B)
        print("Median A :"+str(self.med))
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        cursor.execute("UPDATE TEST_DATA SET MEDIAN = '"+str(self.med)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")                          
                        cursor.execute("UPDATE TEST_DATA SET RANGE_FROM = (SELECT MIN(PEAK_VALUE) FROM STG_PEAK_MST) WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                        cursor.execute("UPDATE TEST_DATA SET RANGE_TO = (SELECT MAX(PEAK_VALUE) FROM STG_PEAK_MST) WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                  except Exception as e:
                           print("SQL Error- test_method_A_calc() :"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()
    
    def test_method_D_calc(self):
        self.max_peak_load=""
        self.min_low_load="" 
        self.avg_load = 0
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT max(PEAK_VALUE) FROM STG_PEAK_MST order by ID ASC")
        for x in results:
              self.max_peak_load=(float(x[0]))              
        connection.close()
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT min(LOW_VAL) FROM STG_LOW_VAL_MST where LOW_VAL > 0  order by ID ASC")
        for x in results:
              self.min_low_load=(float(x[0]))              
        connection.close()       
        
        self.avg_load = (self.max_peak_load + self.min_low_load)/2
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        cursor.execute("UPDATE TEST_DATA SET MEDIAN = '"+str(self.avg_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")                          
                        cursor.execute("UPDATE TEST_DATA SET RANGE_FROM = '"+str(self.min_low_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                        cursor.execute("UPDATE TEST_DATA SET RANGE_TO ='"+str(self.max_peak_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                  except Exception as e:
                           print("SQL Error- test_method_A_calc() :"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()
        
    def test_method_E_calc(self):
        self.max_peak_load=""
        self.min_peak_load="" 
        self.avg_load = 0
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT max(PEAK_VALUE) FROM STG_PEAK_MST order by ID ASC")
        for x in results:
              self.max_peak_load=(float(x[0]))              
        connection.close()
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT min(PEAK_VALUE) FROM STG_PEAK_MST order by ID ASC")
        for x in results:
              self.min_peak_load=(float(x[0]))              
        connection.close()       
        
        self.avg_load = (self.max_peak_load + self.min_peak_load)/2
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        cursor.execute("UPDATE TEST_DATA SET MEDIAN = '"+str(self.avg_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")                          
                        cursor.execute("UPDATE TEST_DATA SET RANGE_FROM = '"+str(self.min_peak_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                        cursor.execute("UPDATE TEST_DATA SET RANGE_TO ='"+str(self.max_peak_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                  except Exception as e:
                           print("SQL Error- test_method_A_calc() :"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()  
        
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
          
    def open_manual_control(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_07_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
   
    def open_graph_data(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=pop_peal_val_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def show_all_specimens(self):        
        #self.pushButton_3.setDisabled(True) ### save
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                       cursor = connection.cursor()                
                       cursor.execute("UPDATE GLOBAL_VAR2 SET GRAPH_TYPE=''")                                   
        connection.commit();
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)    
        self.gridLayout.addWidget(self.sc_data, 1,0,1,1)
    
    def delete_cycle(self):       
            row = self.tableWidget.currentRow() 
            self.cycle_id=str(self.tableWidget.item(row, 5).text())
            if(int(self.cycle_id) > 0):
                close = QMessageBox()
                close.setText("Confirm Deleteing Cycle : "+str(self.cycle_id))
                close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                close = close.exec()
                if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")              
                    with connection:                                    
                                    connection = sqlite3.connect("tyr.db")
                                    results=connection.execute("select IFNULL(SPEC_ID,0),TEST_ID,IFNULL(GRAPH_ID,0) from TEST_DATA where ID = '"+str(self.cycle_id)+"' LIMIT 1")                 
                                    for x in results:
                                        self.curr_cycle_num=int(x[0])
                                        self.test_id=str(x[1])
                                        self.curr_graph_id=str(x[2])            
                                    connection.close()
                                    
                                    connection = sqlite3.connect("tyr.db")              
                                    with connection:        
                                                    cursor = connection.cursor()                
                                                    cursor.execute("DELETE FROM TEST_DATA WHERE ID = '"+str(self.cycle_id)+"'")
                                                    cursor.execute("UPDATE TEST_DATA SET SPEC_ID=IFNULL(SPEC_ID,0)-1 WHERE TEST_ID = '"+str(self.test_id)+"' and SPEC_ID > '"+str(self.curr_cycle_num)+"'")
                                                    cursor.execute("DELETE FROM GRAPH_MST WHERE GRAPH_ID = '"+str(self.curr_graph_id)+"'")                                    
                                    connection.commit();
                                    connection.close()
                                    
                                    connection = sqlite3.connect("tyr.db")
                                    results=connection.execute("select IFNULL(MAX(SPEC_ID),0) from TEST_DATA where TEST_ID = '"+str(self.test_id)+"'")                 
                                    for x in results:
                                        self.label_26.setText(str(x[0]))
                                        #print("updated cycle id :"+str(self.cycle_id))
                                    connection.close()
                   
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
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        
        connection = sqlite3.connect("tyr.db")
        self.tableWidget.setHorizontalHeaderLabels(['Spec.Id',' Median \n ('+str(self.comboBox_2.currentText())+') ',' Range From \n ('+str(self.comboBox_2.currentText())+') ',' Range To \n ('+str(self.comboBox_2.currentText())+') ','Test Method','cycle_id'])
        results=connection.execute("SELECT SPEC_ID,printf(\"%.2f\", MEDIAN),printf(\"%.2f\", RANGE_FROM),printf(\"%.2f\", RANGE_TO),TEST_METHOD_TYPE,ID FROM TEST_DATA WHERE TEST_ID = '"+self.test_id+"' order by ID ASC")
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
        
        
        data2= [ ['Spec. \n No','Median \n ('+str(self.last_load_unit)+')', 'Range From  \n ('+str(self.last_load_unit)+')', 'Range To  \n ('+str(self.last_load_unit)+')']]
                
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SPEC_ID ,printf(\"%.2f\", A.MEDIAN),printf(\"%.2f\", A.RANGE_FROM),printf(\"%.2f\", A.RANGE_TO) FROM TEST_DATA A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
                
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'AVG',printf(\"%.2f\", avg(A.MEDIAN)), printf(\"%.2f\", avg(A.RANGE_FROM)), printf(\"%.2f\", avg(A.RANGE_TO)) FROM TEST_DATA A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                   data2.append(x)
        connection.close()
                
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MAX',printf(\"%.2f\", max(A.MEDIAN)),printf(\"%.2f\", max(A.RANGE_FROM)), printf(\"%.2f\", max(A.RANGE_TO))  FROM TEST_DATA A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                    data2.append(x)
        connection.close()
                
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MIN',printf(\"%.2f\", min(A.MEDIAN)),printf(\"%.2f\", min(A.RANGE_FROM)),printf(\"%.2f\", min(A.RANGE_TO)) FROM TEST_DATA A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                    data2.append(x)
        connection.close()
        
        y=300
        Elements=[]
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT A.CREATED_ON,A.TEST_ID,A.SPECIMEN_NAME,A.BATCH_ID,NULL,A.JOB_NAME,A.TEST_TYPE,NULL,A.PARTY_NAME,A.MOTOR_SPEED,A.MATERIAL,datetime(current_timestamp,'localtime'),A.COMMENTS,A.OPERATOR   FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date-Time: ",str(x[0]),"Test No: ",str(x[1])],["Spec. Name : ",str(x[2]),"Batch ID: ",str(x[3])],["Test Type:",str(x[6]),"Job ID:",str(x[5])],["Customer Name :",str(x[8]),"Test Speed (min/min) :",str(x[9])],["Tested By :", str(self.tested_by),"Report Date-Time: ",str(x[11])]]
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
        
#         logo_arr=[]
#         report_gr_img="last_graph.png"        
#         pdf_img= Image(report_gr_img, 6 * inch, 4* inch)
#         logo_arr.append("odkfoksdf")
#         logo_arr.append(pdf_img)
        
        #f1=Table(data)
        #f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
        #
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
#         f4=Table(logo_arr)
#         f4.setStyle(TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),('BOX', (0,0), (-1,-1), 0.25, colors.black)]))
        
        #self.show_all_specimens()
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4* inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),Spacer(1,12),f2,Spacer(1,12),blank,comments,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
       
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
                       cursor.execute("UPDATE GLOBAL_VAR2 SET GRAPH_TYPE=''")                                   
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
        self.t=0
        
        self.q =0
        self.q_n =0
        self.q_lb =0
        self.q_kn =0
        self.q_mpa =0
        
        self.speed=500
        self.t_timestamp=0
        
        
        
        
        self.arr_p=[0.0]
        self.arr_p_cm=[0.0]
        self.arr_p_inch=[0.0]
        
        self.arr_t=[0.0]
        self.arr_q=[0.0]
        self.arr_q_n=[0.0]
        self.arr_q_lb=[0.0]
        self.arr_q_kn=[0.0]
        self.arr_q_mpa=[0.0]
        self.arr_t_timestamp=[""]
        
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
        self.unit_type =""
        self.graph_type=""
        self.load_unit=""
        self.disp_unit=""
        self.cs_area_cm="1"
        #self.start_time = datetime.datetime.now()
        #self.end_time = datetime.datetime.now()
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.elapsed_time=0
        self.elapsed_time_show=0
        
        
        
        self.modbus_flag=""
        self.modbus_port=""
        self.non_modbus_port=""
        self.proof_max_load=99999
        self.test_time_sec=00000
        
        self.chck_for_last_rec=0
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
        results=connection.execute("SELECT GRAPH_TYPE from GLOBAL_VAR2") 
        for x in results:
              self.graph_type=str(x[0])  
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_LOAD_UNIT,LAST_DISP_UNIT from GLOBAL_VAR2") 
        for x in results:
                        self.load_unit=str(x[0])
                        self.disp_unit=str(x[1])
        connection.close()                
                        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,IFNULL(NEW_TEST_AREA*0.1*0.1,0),PROOF_MAX_LENGTH from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=200            
             self.max_load=float(x[2])
             #self.max_load=100
             self.max_length=float(float(x[3]))
             self.flex_max_length=float(x[3])
             self.cof_max_length=float(x[4])
             #self.max_length=float(float(x[0])-float(x[3]))
             self.max_length=str(self.max_length).zfill(5)
             #print("Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
             self.unit_type=str(x[5])
             self.cs_area_cm=1
             self.proof_max_length=int(str(x[7]))
        connection.close()
        print(" xxx     gfgf self.unit_type:"+str(self.unit_type))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE,ISACTIVE_MODBUS,MODBUS_PORT,NON_MODBUS_PORT from SETTING_MST") 
        for x in results:
                 self.auto_rev_time_off=int(x[2])
                 self.break_sence=float(x[3])
                 self.modbus_flag=str(x[4])
                 self.modbus_port=str(x[5])
                 self.non_modbus_port=str(x[6])
                 self.graph_type="Load Vs Time"
                 if(self.graph_type=="Load Vs Travel"):
                             if(self.load_unit=="Kg" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Elongation (Mm)')
                                             self.axes.set_ylabel('Load (Kg)')
                             elif(self.load_unit=="Kg" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Elongation (Inch)')
                                             self.axes.set_ylabel('Load (Kg)')
                             elif(self.load_unit=="Kg" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Elongation (Cm)')
                                             self.axes.set_ylabel('Load (Kg)')                                                               
                             elif(self.load_unit=="Lb" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Elongation (Mm)')
                                             self.axes.set_ylabel('Load (Lb)')
                             elif(self.load_unit=="Lb" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Elongation (Cm)')
                                             self.axes.set_ylabel('Load (Lb)') 
                             elif(self.load_unit=="Lb" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Elongation (Inch)')
                                             self.axes.set_ylabel('Load (Lb)')                                                         
                             elif(self.load_unit=="N" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Elongation (Mm)')
                                             self.axes.set_ylabel('Load (N)')                                                         
                             elif(self.load_unit=="N" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Elongation (Cm)')
                                             self.axes.set_ylabel('Load (N)')                                 
                             elif(self.load_unit=="N" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Elongation (Inch)')
                                             self.axes.set_ylabel('Load (N)')
                             elif(self.load_unit=="KN" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Elongation (Mm)')
                                             self.axes.set_ylabel('Load (KN)')                                                         
                             elif(self.load_unit=="KN" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Elongation (Cm)')
                                             self.axes.set_ylabel('Load (KN)')                                 
                             elif(self.load_unit=="KN" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Elongation (Inch)')
                                             self.axes.set_ylabel('Load (KN)')
                             elif(self.load_unit=="gm" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Elongation (Mm)')
                                             self.axes.set_ylabel('Load (gm)') 
                             else:    
                                             self.axes.set_xlabel('Elongation (Mm)')
                                             self.axes.set_ylabel('Load (Kg)')
                                        
                 elif(self.graph_type=="Load Vs Time"):
                         #print("inside sadasdasd")
                         self.axes.set_xlabel('Time (Sec)')
                         self.axes.set_ylabel("Load ("+str(self.load_unit)+")")
                 self.axes.set_xlim(0,int(x[0]))
                 self.axes.set_ylim(0,int(x[1]))  
        connection.close()
         
        try:
            '''
            self.ser = serial.Serial(
                        port='/dev/ttyUSB0',
                        baudrate=19200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        xonxoff=False,
                        timeout = 0.05
                    )
            '''
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
            self.test_type="Elongation"
            
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
                          self.command_str="*S2C%05d"%self.max_load+" %.1f"%float(self.max_length)+"\r"
                    else:
                          self.command_str="*S1C%05d"%self.max_load+" %.1f"%float(self.max_length)+"\r"
                    
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
                #self.proof_max_load="99999"
                #self.test_time_sec="00000"
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                        #self.ser.write(b'*S2T000.0 000.0\r')
                        
                        self.command_str="*S2P%05d"%self.proof_max_load+" %05d"%self.proof_max_length+" %05d"%self.test_time_sec+"\r"
                        print("Proof Start Command :"+str(self.command_str))
                    else:
                        #self.ser.write(b'*S1T000.0 000.0\r')
                        self.command_str="*S1P%05d"%self.proof_max_load+" %05d"%self.proof_max_length+" %05d"%self.test_time_sec+"\r"
                        print("Proof Start Command :"+str(self.command_str))
                    
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    
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
        self.end_time = datetime.datetime.now()
        self.elapsed_time=self.end_time-self.start_time
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
                self.chck_for_last_rec=1
                
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
                    if(int(self.test_guage_mm) > int(self.p)):
                            self.p=int(self.test_guage_mm)-self.p
                    else:
                            self.p=int(self.p)-self.test_guage_mm
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
                
                self.t=self.elapsed_time.total_seconds()
                self.t_timestamp=str(self.end_time)
                self.arr_t_timestamp.append(self.t_timestamp)
                self.arr_t.append(float(self.t))
                
                print(" Timer P:"+str(self.p)+" q:"+str(self.q)+" t:"+str(self.t))
               
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
                
                ### This is change to process last repcord
                if(self.chck_for_last_rec==1):
                        self.chck_for_last_rec=0
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
                            if(int(self.test_guage_mm) > int(self.p)):
                                    self.p=int(self.test_guage_mm)-self.p
                            else:
                                    self.p=int(self.p)-self.test_guage_mm
                            #print("self.p :"+str(self.p))
                        elif(self.test_type=="Flexural"):
                            #self.p=self.p
                            self.p=int(self.test_guage_mm)-self.p
                        else:
                            self.p=self.p
      

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
                        
                        self.t=self.elapsed_time.total_seconds()
                        self.t_timestamp=str(self.end_time)
                        self.arr_t_timestamp.append(self.t_timestamp)
                        self.arr_t.append(float(self.t))
                        
                        print("Last Record.... Timer P:"+str(self.p)+" q:"+str(self.q)+" t:"+str(self.t))
                
                self.save_data_flg="Yes"
                self.on_ani_stop()
            
                   
    def plot_grah_only(self,i):
                self.graph_type="Load Vs Time"
                #print("self.load_unit :"+str(self.load_unit)+" self.disp_unit : "+str(self.disp_unit))
                if(self.graph_type=="Load Vs Travel"):
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
                elif(self.graph_type=="Load Vs Time"):
                            
                            if(self.load_unit=="Kg"):
                                self.line_cnt.set_data(self.arr_t,self.arr_q)
                                return [self.line_cnt]
                            elif(self.load_unit=="Lb"):
                                self.line_cnt.set_data(self.arr_t,self.arr_q_lb)
                                return [self.line_cnt]
                            elif(self.load_unit=="N"):
                                self.line_cnt.set_data(self.arr_t,self.arr_q_n)
                                return [self.line_cnt]
                            else:
                                self.line_cnt.set_data(self.arr_t,self.arr_q)
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
            if(int(self.input_speed_val) <= int(self.speed_val)):
                 #print(" Ok ")
                 self.goahead_flag=1
                 self.calc_speed=(int(self.input_speed_val)/int(self.speed_val))*1000                 
                 #print(" calc Speed : "+str(self.calc_speed))
                 #print(" command: *P"+str(self.calc_speed)+" \r")
                 #self.command_str="*P%04d"%self.calc_speed+"_%04d"%self.break_sence+"\r"
                 self.command_str="*P%04d"%self.calc_speed+"_%0.2f"%self.break_sence+"\r"
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
        results=connection.execute("SELECT DISTINCT GRAPH_ID FROM TEST_DATA WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
              self.graph_ids.append(x[0])            
             
        connection.close()
        

        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_UNIT_LOAD,LAST_UNIT_DISP,GRAPH_SCAL_X_LENGTH,GRAPH_SCAL_Y_LOAD from TEST_MST  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ") 
        for x in results:
              self.last_load_unit=str(x[0])
              self.last_disp_unit=str(x[1])
              ax.set_xlim(0,float(x[2]))
              ax.set_ylim(0,float(x[3]))  
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_TYPE from GLOBAL_VAR2") 
        for x in results:
              self.graph_type=str(x[0])  
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_TYPE from GLOBAL_VAR2") 
        for x in results:
              self.graph_type=str(x[0])  
        connection.close()
        
        
        self.graph_type="Load Vs Time"
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
            
            elif(self.graph_type=="Load Vs Time"):                    
                    if(self.last_load_unit=="Kg"):
                        results=connection.execute("SELECT T_SEC,Y_NUM FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Lb"):
                        results=connection.execute("SELECT T_SEC,Y_NUM_LB FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="N"):
                        results=connection.execute("SELECT T_SEC,Y_NUM_N FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    else:
                        results=connection.execute("SELECT T_SEC,Y_NUM FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
         
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
                ax.set_xlabel('Elongation ('+str(self.last_disp_unit)+')')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        
        elif(self.graph_type=="Load Vs Time"):
                ax.set_xlabel('Time (sec)')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        else:
                ax.set_xlabel('Elongation ('+str(self.last_disp_unit)+')')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
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
        self.graph_type=""
        
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
        results=connection.execute("SELECT GRAPH_TYPE from GLOBAL_VAR2") 
        for x in results:
              self.graph_type=str(x[0])  
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
        self.graph_type="Load Vs Time"
        if(self.graph_type=="Load Vs Travel"):
                ax.set_ylabel('Load  ('+str(self.last_load_unit)+')')
                ax.set_xlabel(' Elongation ('+str(self.last_disp_unit)+')')
        else:
                ax.set_ylabel('Load  ('+str(self.last_load_unit)+')')
                ax.set_xlabel(' Time (Sec)')
        
        self.draw()       
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_67_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


