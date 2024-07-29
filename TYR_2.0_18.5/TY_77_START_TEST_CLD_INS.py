from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow
from comment_popup import comment_Ui_MainWindow
from TY_07_UTM_MANNUAL_CONTROL_3 import  TY_07_3_Ui_MainWindow
from pop_graph_data import pop_graph_data_Ui_MainWindow

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




class TY_77_Ui_MainWindow(object):
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
        self.line.setGeometry(QtCore.QRect(0, 200, 1311, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(1160, 10, 141, 21))
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
        self.pushButton_6.setGeometry(QtCore.QRect(1160, 40, 131, 41))
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
        self.frame_3.setGeometry(QtCore.QRect(10, 270, 1281, 421))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(810, 60, 101, 41))
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
        self.pushButton_11.setGeometry(QtCore.QRect(810, 10, 101, 41))
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
        self.pushButton_12.setGeometry(QtCore.QRect(810, 110, 101, 41))
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
        self.pushButton_13.setGeometry(QtCore.QRect(810, 310, 101, 41))
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
        self.pushButton_14.setGeometry(QtCore.QRect(810, 260, 101, 41))
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
        self.pushButton_15.setGeometry(QtCore.QRect(810, 210, 101, 41))
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
        self.tableWidget.setGeometry(QtCore.QRect(930, 20, 341, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
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
        self.pushButton_16.setGeometry(QtCore.QRect(810, 160, 101, 41))
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
        self.lcdNumber.setGeometry(QtCore.QRect(940, 280, 231, 51))
        self.lcdNumber.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_41 = QtWidgets.QLabel(self.frame_3)
        self.label_41.setGeometry(QtCore.QRect(1180, 290, 51, 31))
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
        self.lcdNumber_2.setGeometry(QtCore.QRect(940, 350, 231, 51))
        self.lcdNumber_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_42 = QtWidgets.QLabel(self.frame_3)
        self.label_42.setGeometry(QtCore.QRect(1200, 350, 31, 41))
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
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 401))
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
        self.pushButton_18.setGeometry(QtCore.QRect(810, 360, 111, 41))
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
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(1160, 160, 131, 41))
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
        self.pushButton_9.setGeometry(QtCore.QRect(20, 160, 111, 41))
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
        self.label_11.setGeometry(QtCore.QRect(10, 30, 61, 21))
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
        self.label_12.setGeometry(QtCore.QRect(80, 31, 61, 20))
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
        self.label_13.setGeometry(QtCore.QRect(170, 10, 81, 31))
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
        self.comboBox.setGeometry(QtCore.QRect(250, 10, 91, 31))
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
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(160, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(140, 0, 20, 211))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(490, 0, 20, 211))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(760, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_7)
        self.lineEdit_7.setValidator(input_validator)
        self.lineEdit_7.setGeometry(QtCore.QRect(850, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(930, 170, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("")
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(980, 0, 20, 211))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(600, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(510, 10, 81, 31))
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
        self.label_20.setGeometry(QtCore.QRect(670, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        
        self.label_20_1 = QtWidgets.QLabel(self.frame)
        self.label_20_1.setGeometry(QtCore.QRect(670, 15, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20_1.setFont(font)
        self.label_20_1.setStyleSheet("(mm/min)")
        self.label_20_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20_1.setObjectName("label_20_1")
        
        
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(510, 60, 81, 31))
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
        self.lineEdit_9.setGeometry(QtCore.QRect(600, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(740, 0, 20, 211))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(760, 10, 81, 31))
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
        self.lineEdit_10.setGeometry(QtCore.QRect(850, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(750, 60, 91, 31))
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
        self.lineEdit_11.setGeometry(QtCore.QRect(850, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(750, 100, 241, 21))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(760, 130, 71, 31))
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
        self.lineEdit_12.setGeometry(QtCore.QRect(850, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(10, 60, 71, 31))
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
        self.comboBox_2.setGeometry(QtCore.QRect(90, 60, 51, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(10, 110, 71, 31))
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
        self.comboBox_3.setGeometry(QtCore.QRect(90, 110, 51, 41))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(1140, 0, 20, 211))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(990, 40, 51, 31))
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
        self.lineEdit_13.setGeometry(QtCore.QRect(1050, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(990, 90, 51, 31))
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
        self.lineEdit_14.setGeometry(QtCore.QRect(1050, 90, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(1010, 130, 131, 41))
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
        self.label_45.setGeometry(QtCore.QRect(1010, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("")
        self.label_45.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(0, 250, 1321, 21))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.label_46 = QtWidgets.QLabel(self.frame)
        self.label_46.setGeometry(QtCore.QRect(500, 170, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("")
        self.label_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_17)
        self.lineEdit_17.setValidator(input_validator)
        self.lineEdit_17.setGeometry(QtCore.QRect(620, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(500, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("")
        self.label_50.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_18)
        self.lineEdit_18.setValidator(input_validator)
        self.lineEdit_18.setGeometry(QtCore.QRect(620, 130, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(700, 130, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("")
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.label_51 = QtWidgets.QLabel(self.frame)
        self.label_51.setGeometry(QtCore.QRect(700, 170, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("")
        self.label_51.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.frame)
        self.label_52.setGeometry(QtCore.QRect(1000, 220, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_52.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_52.setObjectName("label_52")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_19.setGeometry(QtCore.QRect(280, 170, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(1160, 100, 131, 41))
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
        self.line_9.setGeometry(QtCore.QRect(500, 100, 251, 20))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setObjectName("line_9")
        self.label_53 = QtWidgets.QLabel(self.frame)
        self.label_53.setGeometry(QtCore.QRect(10, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("")
        self.label_53.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_53.setObjectName("label_53")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_20)
        self.lineEdit_20.setValidator(input_validator)
        self.lineEdit_20.setGeometry(QtCore.QRect(100, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_54 = QtWidgets.QLabel(self.frame)
        self.label_54.setGeometry(QtCore.QRect(160, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("")
        self.label_54.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_54.setObjectName("label_54")
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setGeometry(QtCore.QRect(190, 210, 20, 51))
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setObjectName("line_10")
        self.label_55 = QtWidgets.QLabel(self.frame)
        self.label_55.setGeometry(QtCore.QRect(210, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("")
        self.label_55.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.frame)
        self.label_56.setGeometry(QtCore.QRect(360, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("")
        self.label_56.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_56.setObjectName("label_56")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_21)
        self.lineEdit_21.setValidator(input_validator)
        self.lineEdit_21.setGeometry(QtCore.QRect(300, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_57 = QtWidgets.QLabel(self.frame)
        self.label_57.setGeometry(QtCore.QRect(410, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("")
        self.label_57.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.frame)
        self.label_58.setGeometry(QtCore.QRect(550, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("")
        self.label_58.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_58.setObjectName("label_58")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_22)
        self.lineEdit_22.setValidator(input_validator)
        self.lineEdit_22.setGeometry(QtCore.QRect(500, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_59 = QtWidgets.QLabel(self.frame)
        self.label_59.setGeometry(QtCore.QRect(600, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("")
        self.label_59.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.frame)
        self.label_60.setGeometry(QtCore.QRect(760, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("")
        self.label_60.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_60.setObjectName("label_60")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_23)
        self.lineEdit_23.setValidator(input_validator)
        self.lineEdit_23.setGeometry(QtCore.QRect(700, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_61 = QtWidgets.QLabel(self.frame)
        self.label_61.setGeometry(QtCore.QRect(810, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("")
        self.label_61.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.frame)
        self.label_62.setGeometry(QtCore.QRect(950, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("")
        self.label_62.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_62.setObjectName("label_62")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_24)
        self.lineEdit_24.setValidator(input_validator)
        self.lineEdit_24.setGeometry(QtCore.QRect(900, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.line_11 = QtWidgets.QFrame(self.frame)
        self.line_11.setGeometry(QtCore.QRect(390, 210, 20, 51))
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.frame)
        self.line_12.setGeometry(QtCore.QRect(580, 210, 20, 51))
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.frame)
        self.line_13.setGeometry(QtCore.QRect(790, 210, 20, 51))
        self.line_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_13.setLineWidth(3)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.frame)
        self.line_14.setGeometry(QtCore.QRect(980, 210, 20, 51))
        self.line_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_14.setLineWidth(3)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setObjectName("line_14")
        self.label_63 = QtWidgets.QLabel(self.frame)
        self.label_63.setGeometry(QtCore.QRect(1110, 90, 31, 31))
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
        self.label_37.setGeometry(QtCore.QRect(1110, 40, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("")
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(320, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(410, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(1130, 230, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setChecked(False)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(170, 85, 127);")        
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(1210, 230, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(1100, 180, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(1010, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
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
        self.lineEdit_25.setObjectName("lineEdit_25")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
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
        self.label_10.setText(_translate("MainWindow", "CLD_INS"))
        self.label_47.setText(_translate("MainWindow", "05 Aug 2020 14:23:00"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.pushButton_7.setText(_translate("MainWindow", "Stop"))
        self.pushButton_11.setText(_translate("MainWindow", "Start"))
        self.pushButton_12.setText(_translate("MainWindow", "All Graphs"))
        self.pushButton_13.setText(_translate("MainWindow", "View Report"))
        self.pushButton_14.setText(_translate("MainWindow", "Email"))
        self.pushButton_15.setText(_translate("MainWindow", "Comment"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Load (Kgf)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Deflection (mm)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Rec# "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", ""))
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
        self.label_42.setText(_translate("MainWindow", "Mm."))
        self.label_49.setText(_translate("MainWindow", "Data Saved Successfully ......"))
        self.pushButton_18.setText(_translate("MainWindow", "Data"))
        self.pushButton_8.setText(_translate("MainWindow", "Go For Test"))
        self.pushButton_9.setText(_translate("MainWindow", "Reset"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "0001"))
        self.label_13.setText(_translate("MainWindow", "Spec. Name: "))
        self.comboBox.setItemText(0, _translate("MainWindow", "1254"))
        self.comboBox.setItemText(1, _translate("MainWindow", "8788"))
        self.comboBox.setItemText(2, _translate("MainWindow", "6543"))
        self.comboBox.setItemText(3, _translate("MainWindow", "878"))
        self.label_14.setText(_translate("MainWindow", "Customer Name:"))
        self.label_15.setText(_translate("MainWindow", "Capacity :"))
        self.label_17.setText(_translate("MainWindow", "Pre Load:"))
        self.label_18.setText(_translate("MainWindow", "(Kgf)"))
        self.label_19.setText(_translate("MainWindow", "Rev.Speed:"))
        self.label_20.setText(_translate("MainWindow", "(mm/min)"))
        self.label_20_1.setText(_translate("MainWindow", "(mm/min)"))
        self.label_21.setText(_translate("MainWindow", "Test Speed: "))
        self.label_23.setText(_translate("MainWindow", "Hardness :"))
        self.label_25.setText(_translate("MainWindow", "M/C No :"))
        self.label_27.setText(_translate("MainWindow", "Operator :"))
        self.label_29.setText(_translate("MainWindow", "Load Unit:"))
        
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Kg"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Lb"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "N"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "gm"))
        
        self.label_30.setText(_translate("MainWindow", "Deflection \n Unit:"))
        
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Mm"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Cm"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Inch"))        
        
        self.label_31.setText(_translate("MainWindow", "X-axis: "))
        self.label_32.setText(_translate("MainWindow", "Y-axis: "))
        self.pushButton_10.setText(_translate("MainWindow", "Set Graph"))
        self.label_35.setText(_translate("MainWindow", "Part Name :"))
        self.label_36.setText(_translate("MainWindow", "Batch Number :"))
        self.label_45.setText(_translate("MainWindow", "Graph Scale "))
        self.label_46.setText(_translate("MainWindow", "Max. Load:"))
        self.label_50.setText(_translate("MainWindow", "Max. Deflection:"))
        self.label_34.setText(_translate("MainWindow", "(Mm)"))
        self.label_51.setText(_translate("MainWindow", "(Kgf)"))
        self.label_52.setText(_translate("MainWindow", "Graph Set Done."))
        self.label_52.hide()
        self.pushButton_17.setText(_translate("MainWindow", "Set Pre.Load"))
        self.label_53.setText(_translate("MainWindow", "Load (1):"))
        self.label_54.setText(_translate("MainWindow", "(Kgf)"))
        self.label_55.setText(_translate("MainWindow", " Load (2):"))
        self.label_56.setText(_translate("MainWindow", "(Kgf)"))
        self.label_57.setText(_translate("MainWindow", " Load (3):"))
        self.label_58.setText(_translate("MainWindow", "(Kgf)"))
        self.label_59.setText(_translate("MainWindow", " Load (4):"))
        self.label_60.setText(_translate("MainWindow", "(Kgf)"))
        self.label_61.setText(_translate("MainWindow", " Load (5):"))
        self.label_62.setText(_translate("MainWindow", "(Kgf)"))
        self.label_63.setText(_translate("MainWindow", "(Kgf)"))
        self.label_37.setText(_translate("MainWindow", "(Mm)"))
        self.label_16.setText(_translate("MainWindow", "Method :"))
        self.label_24.setText(_translate("MainWindow", "Compression"))
        self.radioButton.setText(_translate("MainWindow", "Load"))
        self.radioButton_2.setText(_translate("MainWindow", "Deflection"))
        self.label_26.setText(_translate("MainWindow", "01"))
        self.label_28.setText(_translate("MainWindow", "Spec. Count:"))
        self.lineEdit_25.setText(_translate("MainWindow", ""))
        self.comboBox.currentTextChanged.connect(self.onchage_combo)
        #self.comboBox_4.currentTextChanged.connect(self.show_graph)
        
      
        self.pushButton_8.clicked.connect(self.go_for_test)
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_9.clicked.connect(self.new_test_reset)
        self.pushButton_18.clicked.connect(self.open_graph_data)
        self.pushButton_10.clicked.connect(self.set_graph_scale)
        self.pushButton_11.clicked.connect(self.start_test)
        #self.tableWidget.doubleClicked.connect(self.delete_cycle)
        
        self.pushButton_13.clicked.connect(self.open_pdf)
        self.pushButton_16.clicked.connect(self.print_file)
        self.pushButton_14.clicked.connect(self.open_email_report)
        self.pushButton_15.clicked.connect(self.open_comment_popup)
        self.pushButton_12.clicked.connect(self.show_all_specimens)        
        self.pushButton_7.clicked.connect(self.manual_stop)
        self.pushButton_17.clicked.connect(self.open_manual_control)
        
        self.comboBox_2.currentTextChanged.connect(self.load_unit_onchange)
        self.radioButton.clicked.connect(self.radiobutt_on_change)
        self.radioButton_2.clicked.connect(self.radiobutt_on_change)
        
        self.test_method=""                             
        self.failure_mod=""
        self.tmperature=""
        self.test_type_for_flexural=""
        self.remark=""
        self.modbus_flag=""
        self.modbus_port=""
        self.non_modbus_port=""
        self.pre_load="0"
        self.load_cell_no="0"
        
        
        
        self.load_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.frame_3.hide()
        self.show_grid_data_Tear()
        #self.tableWidget.setHorizontalHeaderLabels(['Thickness (mm)',' Peak Load (Kgf) ','Tear Strength (Kgf/Cm)','Created On','Cycle ID'])
        #self.tableWidget.setHorizontalHeaderLabels([' Peak Load ('+str(self.comboBox_2.currentText())+') ','cycle_id'])        
        
        self.pushButton_9.setDisabled(True)
    
    def load_unit_onchange(self):
        self.i=0
        self.comboBox_3.clear()
        if(str(self.comboBox_2.currentText())=="KN"):
              self.comboBox_3.addItem("")
              self.comboBox_3.setItemText(self.i,"Mm")
              self.i=self.i+1
        elif(str(self.comboBox_2.currentText())=="MPa"):
              self.comboBox_3.addItem("")
              self.comboBox_3.setItemText(self.i,"Mm")
              self.i=self.i+1
        elif(str(self.comboBox_2.currentText())=="Kg"):
              self.comboBox_3.addItem("")
              self.comboBox_3.setItemText(self.i,"Mm")
              self.i=self.i+1
              self.comboBox_3.addItem("")
              self.comboBox_3.setItemText(self.i,"Cm")
              self.i=self.i+1
        elif(str(self.comboBox_2.currentText())=="Lb"):
              self.comboBox_3.addItem("")
              self.comboBox_3.setItemText(self.i,"Inch")
              self.i=self.i+1
        elif(str(self.comboBox_2.currentText())=="N"):
              self.comboBox_3.addItem("")
              self.comboBox_3.setItemText(self.i,"Mm")
              self.i=self.i+1
        elif(str(self.comboBox_2.currentText())=="gm"):
              self.comboBox_3.addItem("")
              self.comboBox_3.setItemText(self.i,"Mm")
              self.i=self.i+1   
        else:
              #print("No change in combo3")
              self.comboBox_3.setDisabled(True)
        
        #self.radiobutt_on_change()
        self.label_63.setText("("+str(self.comboBox_2.currentText())+")")
        
    def device_date(self):     
        self.label_47.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def radiobutt_on_change(self):
        
        if(self.radioButton_2.isChecked()):
                self.label_53.setText("Deflection:")
                self.label_55.setText("Deflection:")
                self.label_57.setText("Deflection:")
                self.label_59.setText("Deflection:")
                self.label_61.setText("Deflection:")                
                self.label_54.setText("("+str(self.comboBox_3.currentText())+")")
                self.label_56.setText("("+str(self.comboBox_3.currentText())+")")
                self.label_58.setText("("+str(self.comboBox_3.currentText())+")")
                self.label_60.setText("("+str(self.comboBox_3.currentText())+")")
                self.label_62.setText("("+str(self.comboBox_3.currentText())+")")
        elif(self.radioButton.isChecked()):
                self.label_53.setText("Load:")
                self.label_55.setText("Load:")
                self.label_57.setText("Load:")
                self.label_59.setText("Load:")
                self.label_61.setText("Load:")
                self.label_54.setText("("+str(self.comboBox_2.currentText())+")")
                self.label_56.setText("("+str(self.comboBox_2.currentText())+")")
                self.label_58.setText("("+str(self.comboBox_2.currentText())+")")
                self.label_60.setText("("+str(self.comboBox_2.currentText())+")")
                self.label_62.setText("("+str(self.comboBox_2.currentText())+")")
        else:
                self.label_53.setText("Load:")
                self.label_55.setText("Load:")
                self.label_57.setText("Load:")
                self.label_59.setText("Load:")
                self.label_61.setText("Load:")                
                self.label_54.setText("("+str(self.comboBox_2.currentText())+")")
                self.label_56.setText("("+str(self.comboBox_2.currentText())+")")
                self.label_58.setText("("+str(self.comboBox_2.currentText())+")")
                self.label_60.setText("("+str(self.comboBox_2.currentText())+")")
                self.label_62.setText("("+str(self.comboBox_2.currentText())+")")
            
        
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
        results=connection.execute("SELECT SPECIMEN_NAME FROM SPECIMEN_MST WHERE TEST_MODE='Compression'") 
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
        results=connection.execute("SELECT NEW_TEST_MAX_LOAD,NEW_TEST_MAX_LENGTH,NEW_TEST_PARTY_NAME FROM GLOBAL_VAR") 
        for x in results:            
            self.lineEdit_10.setText(str(x[0]))
            self.lineEdit_11.setText(str(x[1]))
            self.lineEdit_25.setText(str(x[2]))
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
        
        self.label_41.setText(str(self.comboBox_2.currentText()))
        self.label_42.setText(str(self.comboBox_3.currentText() ))
        self.lcdNumber.setProperty("value", 0.0)     #load
        self.lcdNumber_2.setProperty("value",0.0)  #length
        #self.lcdNumber_3.setProperty("value",0.0)  #speed
        
        self.pushButton_7.setDisabled(True)
        self.pushButton_11.setEnabled(True)
        self.show_grid_data_Tear()
        
        ##### CLD_INS - Changes####
        self.label_59.hide()
        self.label_60.hide()
        self.label_61.hide()
        self.label_62.hide()
        self.lineEdit_23.hide()
        self.lineEdit_24.hide()
        self.line_13.hide()
        self.radioButton.hide()
        self.radioButton_2.hide()
        
        self.label_23.hide()
        self.label_25.hide()
        self.lineEdit_10.hide()
        self.lineEdit_11.hide()
        
        
        self.radiobutt_on_change()
        print("Data Loaded OK !!")
       
    
    
    def validations(self):        
        self.go_ahead="No"
        self.msg=""
        if(self.lineEdit_25.text() == ""):
              self.msg="Customer Name Should not Empty."              
        elif(self.lineEdit_8.text() == ""):
              self.msg="Test Type Should not Empty."
        elif(self.lineEdit_15.text() == ""):
              self.msg="Job Name Should not Empty."
        elif(self.lineEdit_16.text() == ""):
              self.msg="Batch Number Should not Empty."
        elif(self.lineEdit_19.text() == ""):
              self.msg="Capacity Should not Empty."
        elif(self.lineEdit_9.text() == ""):
              self.msg="Test Speed Should not Empty."
        elif(self.lineEdit_18.text() == ""):
              self.msg="Max Deflection Should not Empty."
        elif(self.lineEdit_17.text() == ""):
              self.msg="Max Load Should not Empty."
#         elif(self.lineEdit_10.text() == ""):
#               self.msg="Hardness Should not Empty."
#         elif(self.lineEdit_10.text() == ""):
#               self.msg="Hardness Should not Empty."
#         elif(self.lineEdit_11.text() == ""):
#               self.msg="Machine No Should not Empty."
        elif(self.lineEdit_12.text() == ""):
              self.msg="Operator Should not Empty."
        elif(self.lineEdit_7.text() == ""):
              self.msg="Pre Load Should not Empty."
        elif(self.lineEdit_13.text() == ""):
              self.msg="Graph Scale x-axsis Should not Empty."
        elif(self.lineEdit_14.text() == ""):
              self.msg="Graph Scale y-axsis  Should not Empty."
        elif(self.lineEdit_20.text() == ""):
              self.msg="LOAD/DEFLECTION-1  Should not Empty."       
        elif(self.lineEdit_21.text() == ""):
              self.msg="LOAD/DEFLECTION-2  Should not Empty."       
        elif(self.lineEdit_22.text() == ""):
              self.msg="LOAD/DEFLECTION-3  Should not Empty."       
        
#         elif(self.lineEdit_23.text() == ""):
#               self.msg="LOAD/DEFLECTION-4  Should not Empty."        
#         elif(self.lineEdit_24.text() == ""):
#               self.msg="LOAD/DEFLECTION-5  Should not Empty."
        
        else:
               #self.check_for_max_load_deflection()
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
                                            cursor.execute("UPDATE TEST_MST SET PART_NO='"+str(self.comboBox.currentText())+"',PARTY_NAME='"+str(self.lineEdit_25.text())+"',MOTOR_SPEED='"+str(self.lineEdit_9.text())+"'  WHERE  TEST_ID = '"+str(int(self.label_12.text()))+"'")
                                            cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_MAX_LOAD='"+str(self.lineEdit_17.text())+"',NEW_TEST_MAX_LENGTH='"+str(self.lineEdit_18.text())+"'")                                
                                            cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_PARTY_NAME='"+str(self.lineEdit_25.text())+"',PRE_LOAD='"+str(self.lineEdit_7.text())+"',NEW_TEST_MOTOR_SPEED='"+str(self.lineEdit_9.text())+"'")                               
                                            cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_Y_LOAD='"+self.lineEdit_14.text()+"',GRAPH_SCAL_X_LENGTH='"+self.lineEdit_13.text()+"'  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                                            cursor.execute("UPDATE TEST_MST SET LAST_UNIT_LOAD='"+str(self.comboBox_2.currentText())+"',LAST_UNIT_DISP='"+str(self.comboBox_3.currentText())+"'  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                                            cursor.execute("UPDATE TEST_MST SET TESTED_BY=(SELECT LOGIN_USER_NAME FROM GLOBAL_VAR)  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                                
                                    connection.commit();
                                    connection.close()
                                    
                           else:        
                                    ### INSERT 
                                    connection = sqlite3.connect("tyr.db")              
                                    with connection:        
                                          cursor = connection.cursor()
                                          cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_MAX_LOAD='"+str(self.lineEdit_17.text())+"',NEW_TEST_MAX_LENGTH='"+str(self.lineEdit_18.text())+"',PART_NO='"+self.comboBox.currentText()+"',NEW_TEST_PARTY_NAME='"+str(self.lineEdit_25.text())+"'") 
                                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(int(self.label_12.text()))+"',NEW_TEST_GUAGE_MM='200'")
                                          cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_PARTY_NAME='"+str(self.lineEdit_25.text())+"',PRE_LOAD='"+str(self.lineEdit_7.text())+"',LOAD_CELL_NO='',TEST_MODE='',NEW_TEST_MOTOR_SPEED='"+str(self.lineEdit_9.text())+"'") 
                                          cursor.execute("INSERT INTO TEST_MST(SPECIMEN_NAME,TEST_TYPE,MOTOR_REV_SPEED,NEW_TEST_MAX_LOAD,NEW_TEST_MAX_LENGTH,PART_NO,PART_NAME,MOTOR_SPEED,HARDNESS,MATERIAL,MACHINE_NO,TEST_MODE,OPERATOR,PARTY_NAME,BATCH_ID,PRE_LOAD) VALUES('"+str(self.lineEdit_15.text())+"','CLD_INS','"+str(self.lineEdit_9.text())+"','"+str(self.lineEdit_17.text())+"','"+str(self.lineEdit_18.text())+"','"+self.comboBox.currentText()+"','"+str(self.lineEdit_15.text())+"','"+str(self.lineEdit_8.text())+"','"+str(self.lineEdit_10.text())+"','"+str(self.lineEdit_19.text())+"','"+str(self.lineEdit_11.text())+"','Compression','"+str(self.lineEdit_12.text())+"','"+str(self.lineEdit_25.text())+"','"+str(self.lineEdit_16.text())+"','"+str(self.lineEdit_7.text())+"')")
                                          cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_Y_LOAD='"+self.lineEdit_14.text()+"',GRAPH_SCAL_X_LENGTH='"+self.lineEdit_13.text()+"'  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                                          cursor.execute("UPDATE TEST_MST SET LAST_UNIT_LOAD='"+str(self.comboBox_2.currentText())+"',LAST_UNIT_DISP='"+str(self.comboBox_3.currentText())+"'  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                                          cursor.execute("UPDATE TEST_MST SET TESTED_BY=(SELECT LOGIN_USER_NAME FROM GLOBAL_VAR)  where TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
                                          
                                    connection.commit();
                                    connection.close()
       
    def check_for_max_load_deflection(self):
        if(self.radioButton.isChecked()):        
            if(float(self.lineEdit_20.text()) > float(self.lineEdit_17.text())):
                          self.msg="LOAD/DEFLECTION-1  Should not Greater than Max. Load."
            elif(float(self.lineEdit_21.text()) > float(self.lineEdit_17.text())):
                          self.msg="LOAD/DEFLECTION-2  Should not Greater than Max. Load."
            elif(float(self.lineEdit_22.text()) > float(self.lineEdit_17.text())):
                          self.msg="LOAD/DEFLECTION-3  Should not Greater than Max. Load."
            elif(float(self.lineEdit_23.text()) > float(self.lineEdit_17.text())):
                          self.msg="LOAD/DEFLECTION-4  Should not Greater than Max. Load."
            elif(float(self.lineEdit_24.text()) > float(self.lineEdit_17.text())):
                          self.msg="LOAD/DEFLECTION-5  Should not Greater than Max. Load."
            else:
                       print("Ok")
                       self.go_ahead="Yes"
        else:
            if(float(self.lineEdit_20.text()) > float(self.lineEdit_18.text())):
                          self.msg="LOAD/DEFLECTION-1  Should not Greater than Max. DEFLECTION."
            elif(float(self.lineEdit_21.text()) > float(self.lineEdit_18.text())):
                          self.msg="LOAD/DEFLECTION-2  Should not Greater than Max. DEFLECTION."
            elif(float(self.lineEdit_22.text()) > float(self.lineEdit_18.text())):
                          self.msg="LOAD/DEFLECTION-3  Should not Greater than Max. DEFLECTION."
            elif(float(self.lineEdit_23.text()) > float(self.lineEdit_18.text())):
                          self.msg="LOAD/DEFLECTION-4  Should not Greater than Max. DEFLECTION."
            elif(float(self.lineEdit_24.text()) > float(self.lineEdit_18.text())):
                          self.msg="LOAD/DEFLECTION-5  Should not Greater than Max. DEFLECTION."
            else:
                       print("Ok")
                       self.go_ahead="Yes"
                       
                       
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
        #print("Old object status :"+str(self.timer31.isActive()))
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
                     
#                             self.timer3=QtCore.QTimer()
#                             self.timer3.setInterval(5000)        
#                             self.timer3.timeout.connect(self.loadcell_encoder_status)
#                             self.timer3.start(1)
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
        self.label_42.setText(str(self.comboBox_3.currentText()))
        '''
        time.sleep(3)
        connection = sqlite3.connect("tyr.db")
        with connection:        
           cursor = connection.cursor()
           print("UPDATE GLOBAL_VAR SET LOAD_CELL_NO='"+str(self.load_cell_no)+"', TEST_MODE= 'TENSILE'")
           cursor.execute("UPDATE GLOBAL_VAR SET LOAD_CELL_NO='"+str(self.load_cell_no)+"', TEST_MODE= 'TENSILE'")
        connection.commit();
        connection.close()
        '''
    
    def loadcell_encoder_status(self):
        self.load_cell_hi=-1
        self.load_cell_lo=-1
        self.extiometer=-1
        self.encoder=-1
        self.load_cell_no="0"
        
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
            #print("Load Cell No... :"+str(self.buff[7]))
            #print("Encoder No.. :"+str(self.buff[6]))
            if(str(self.buff[6])=="2"):
                self.load_cell_no="2"
            else:
                self.load_cell_no="1"
                    
            if(str(self.buff[7])=="2"):
                self.extiometer=1
                self.encoder=0
            else:
                self.extiometer=0
                self.encoder=1
                
           
            
            
#             if(self.load_cell_hi==1):
#                 if(self.extiometer==1):
#                         self.label_26_1.setText("Load cell: (Hi)-Extensometer ")
#                 else:        
#                         self.label_26_1.setText("Load cell: (Hi)-Encoder ")
#             
#             else:
#                 if(self.extiometer==1):
#                         self.label_26_1.setText("Load cell: (Low)-Extensometer ")
#                 else:
#                         self.label_26_1.setText("Load cell: (Low)-Encoder ")
        
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
        results=connection.execute("select PART_NAME,REV_MOTOR_SPEED,OPERATOR,LOAD_CELL,HARDNESS,MAX_LOAD,MAX_DEFLECTION,PRE_LOAD,MOTOR_SPEED,TEST_MODE,LAST_UNIT_LOAD,LAST_UNIT_DISP,LOAD_CELL FROM SPECIMEN_MST WHERE SPECIMEN_NAME='"+self.comboBox.currentText()+"'")                 
        for x in results:
            self.lineEdit_15.setText(str(x[0])) # PART_NAME
            self.lineEdit_8.setText(str(x[1])) # TEST_TYPE
            self.lineEdit_12.setText(str(x[2])) # OPERATOR
            self.lineEdit_19.setText(str(x[3])) # Material
            self.lineEdit_10.setText(str(x[4])) # Hardness
            self.lineEdit_17.setText(str(x[5])) # MAX LOAD
            self.lineEdit_18.setText(str(x[6])) # MAX DEFLECTION
            self.lineEdit_7.setText(str(x[7])) # PRE LOAD
            self.lineEdit_9.setText(str(x[8])) # TEST SPEED 
            self.label_24.setText(str(x[9])) #TEST MODE          
            self.comboBox_2.setCurrentText(str(x[10])) #UNIT_LOAD
            self.comboBox_3.setCurrentText(str(x[11])) #UNIT_Travel
        connection.close()
        #self.click_onRadiobutt()
        #self.cs_area_calculation()
        
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
                    if((str(self.comboBox_2.currentText()) =="Kg") and (str(self.comboBox_3.currentText()) =="Mm")):
                                    self.lcdNumber.setProperty("value", str(self.sc_new.q))    #load
                                    self.lcdNumber_2.setProperty("value",str(self.sc_new.p))   #length
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
                    #self.lcdNumber_3.setProperty("value",str(self.lineEdit_8.text()))
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
                            self.label_26.setText(str(self.cycle_num))
                            self.pushButton_12.setEnabled(True)
                            self.pushButton_13.setEnabled(True)
                            self.pushButton_14.setEnabled(True)
                            self.pushButton_15.setEnabled(True)
                            self.pushButton_16.setEnabled(True)
                            self.pushButton_6.setEnabled(True)
                            
        else:
                           self.lcdNumber.setProperty("value", 0.0)     #load
                           self.lcdNumber_2.setProperty("value",0.0)  #length
                           #self.lcdNumber_3.setProperty("value",0.0)  #speed
                
                
        
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
            results=connection.execute("select IFNULL(NEW_TEST_GUAGE_MM,0),NEW_TEST_NAME,IS_METAL FROM GLOBAL_VAR")                 
            for x in results:
                self.guage_length_mm=0
                self.test_type=str(x[1])
                self.def_flg=str(x[2])            
            connection.close()                                  
            
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)):
                   cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_LB,Y_NUM_KN,Y_NUM_MPA,T_SEC) VALUES ('"+str(float(self.sc_new.arr_p[g]))+"','"+str(float(self.sc_new.arr_p_cm[g]))+"','"+str(float(self.sc_new.arr_p_inch[g]))+"','"+str(self.sc_new.arr_q[g])+"','"+str(self.sc_new.arr_q_n[g])+"','"+str(self.sc_new.arr_q_lb[g])+"','"+str(self.sc_new.arr_q_kn[g])+"','"+str(self.sc_new.arr_q_mpa[g])+"','"+str(float(self.sc_new.arr_t[g]))+"')")
                   cursor.execute("DELETE FROM STG_TEST_DATA")                  
            connection.commit();
            connection.close()
           
            
          
        
        if (len(self.sc_new.arr_p) > 1):            
            self.cycle_num=self.cycle_num+1
            connection = sqlite3.connect("tyr.db")              
            with connection:
                  
                  cursor = connection.cursor()              
                  if(self.radioButton.isChecked()):  ### Load
                          try:
                                cursor.execute("INSERT INTO STG_TEST_DATA(LOAD)VALUES('"+str(self.lineEdit_20.text())+"')")
                                cursor.execute("INSERT INTO STG_TEST_DATA(LOAD)VALUES('"+str(self.lineEdit_21.text())+"')")
                                cursor.execute("INSERT INTO STG_TEST_DATA(LOAD)VALUES('"+str(self.lineEdit_22.text())+"')")
                                cursor.execute("INSERT INTO STG_TEST_DATA(LOAD)VALUES('"+str(self.lineEdit_23.text())+"')")
                                cursor.execute("INSERT INTO STG_TEST_DATA(LOAD)VALUES('"+str(self.lineEdit_24.text())+"')")
                                if( str(self.comboBox_2.currentText()) =="Kg" and str(self.comboBox_3.currentText()) =="Mm"):
                                            cursor.execute("UPDATE STG_TEST_DATA SET DEFLCTION = (SELECT MAX(X_NUM) FROM STG_GRAPH_MST where Y_NUM <= LOAD),DATA_EXIST_FLAG=(SELECT COUNT(*) FROM STG_GRAPH_MST WHERE Y_NUM >= LOAD)   ")                                    
                                elif( str(self.comboBox_2.currentText()) =="Lb" and str(self.comboBox_3.currentText()) =="Inch"):
                                             cursor.execute("UPDATE STG_TEST_DATA SET DEFLCTION = (SELECT MAX(X_NUM_INCH) FROM STG_GRAPH_MST where Y_NUM_LB <= LOAD),DATA_EXIST_FLAG=(SELECT COUNT(*) FROM STG_GRAPH_MST WHERE Y_NUM_LB >= LOAD) ")
                                elif( str(self.comboBox_2.currentText()) =="N" and str(self.comboBox_3.currentText()) =="Mm"):
                                             cursor.execute("UPDATE STG_TEST_DATA SET DEFLCTION = (SELECT MAX(X_NUM) FROM STG_GRAPH_MST where Y_NUM_N <= LOAD),DATA_EXIST_FLAG=(SELECT COUNT(*) FROM STG_GRAPH_MST WHERE Y_NUM_N >= LOAD) ")
                                else:
                                             cursor.execute("UPDATE STG_TEST_DATA SET DEFLCTION = (SELECT MAX(X_NUM) FROM STG_GRAPH_MST where Y_NUM <= LOAD),DATA_EXIST_FLAG=(SELECT COUNT(*) FROM STG_GRAPH_MST WHERE Y_NUM >= LOAD) ")
                                cursor.execute("UPDATE STG_TEST_DATA SET FLAG = 'L' ")
                                print("L Data saved........Cycle no : "+str(self.cycle_num))
                          except IOError as e:
                                    print("SQL Error : "+str(e))
                            
                  else: ### Deflection 
                        cursor.execute("INSERT INTO STG_TEST_DATA(DEFLCTION)VALUES('"+str(self.lineEdit_20.text())+"')")
                        cursor.execute("INSERT INTO STG_TEST_DATA(DEFLCTION)VALUES('"+str(self.lineEdit_21.text())+"')")
                        cursor.execute("INSERT INTO STG_TEST_DATA(DEFLCTION)VALUES('"+str(self.lineEdit_22.text())+"')")
                        cursor.execute("INSERT INTO STG_TEST_DATA(DEFLCTION)VALUES('"+str(self.lineEdit_23.text())+"')")
                        cursor.execute("INSERT INTO STG_TEST_DATA(DEFLCTION)VALUES('"+str(self.lineEdit_24.text())+"')")
                        if( str(self.comboBox_2.currentText()) =="Kg" and str(self.comboBox_3.currentText()) =="Mm"):
                                     cursor.execute("UPDATE STG_TEST_DATA SET LOAD = (SELECT MAX(Y_NUM) FROM STG_GRAPH_MST where X_NUM <= DEFLCTION),DATA_EXIST_FLAG=(SELECT COUNT(*) FROM STG_GRAPH_MST WHERE X_NUM >= DEFLCTION) ")                                    
                        elif( str(self.comboBox_2.currentText()) =="Lb" and str(self.comboBox_3.currentText()) =="Inch"):
                                     cursor.execute("UPDATE STG_TEST_DATA SET LOAD = (SELECT MAX(Y_NUM_LB) FROM STG_GRAPH_MST where X_NUM_INCH <= DEFLCTION),DATA_EXIST_FLAG=(SELECT COUNT(*) FROM STG_GRAPH_MST WHERE X_NUM_INCH >= DEFLCTION) ")
                        elif( str(self.comboBox_2.currentText()) =="N" and str(self.comboBox_3.currentText()) =="Mm"):
                                     cursor.execute("UPDATE STG_TEST_DATA SET LOAD = (SELECT MAX(Y_NUM_N) FROM STG_GRAPH_MST where X_NUM <= DEFLCTION),DATA_EXIST_FLAG=(SELECT COUNT(*) FROM STG_GRAPH_MST WHERE X_NUM >= DEFLCTION) ")
                        else:
                                     cursor.execute("UPDATE STG_TEST_DATA SET LOAD = (SELECT MAX(Y_NUM) FROM STG_GRAPH_MST where X_NUM <= DEFLCTION),DATA_EXIST_FLAG=(SELECT COUNT(*) FROM STG_GRAPH_MST WHERE X_NUM >= DEFLCTION) ") 
                        cursor.execute("UPDATE STG_TEST_DATA SET FLAG = 'D' ")
                        print("D Data saved........Cycle no : "+str(self.cycle_num))  
                
                  print("0 Data saved........Cycle no : "+str(self.cycle_num))  
                  cursor.execute("INSERT INTO GRAPH_MST(X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_MPA,Y_NUM_LB,Y_NUM_KN,T_SEC) SELECT X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_MPA,Y_NUM_LB,Y_NUM_KN,T_SEC FROM STG_GRAPH_MST")
                  cursor.execute("UPDATE STG_TEST_DATA SET TEST_ID = (SELECT TEST_ID FROM GLOBAL_VAR) ")
                  cursor.execute("UPDATE STG_TEST_DATA SET SPEC_ID = '"+str(self.cycle_num)+"'")
                  cursor.execute("UPDATE GRAPH_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")
                  cursor.execute("UPDATE STG_TEST_DATA SET GRAPH_ID = (SELECT MAX(IFNULL(GRAPH_ID,0)) FROM GRAPH_MST)")
                  cursor.execute("UPDATE TEST_MST SET STATUS='LOADED GRAPH' WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                  cursor.execute("INSERT INTO TEST_DATA(TEST_ID,LOAD,DEFLCTION,FLAG,GRAPH_ID,SPEC_ID,DATA_EXIST_FLAG) SELECT TEST_ID,LOAD,DEFLCTION,FLAG,GRAPH_ID,SPEC_ID,DATA_EXIST_FLAG FROM STG_TEST_DATA")                    
                  print("Data saved........")
                    
            
            connection.commit();
            connection.close()
            
            connection = sqlite3.connect("tyr.db")              
            with connection:
                  print("Update the Load and Defection data : "+str(self.cycle_num))  
                  cursor = connection.cursor() 
                  if(self.radioButton.isChecked()):  
                           if(str(self.cycle_num) == "1"):
                                  cursor.execute("INSERT INTO DEFLECTION_DATA(TEST_ID,LOAD,DEF_1) SELECT TEST_ID,LOAD,DEFLCTION FROM STG_TEST_DATA")
                           else:
                                   print("OK ....")
                  else: 
                           if(str(self.cycle_num) == "1"):
                                  cursor.execute("INSERT INTO LOAD_DATA(TEST_ID,DEFLECTION,LOAD_1) SELECT TEST_ID,DEFLCTION,LOAD FROM STG_TEST_DATA")                      
                           else:
                                  print("OK..")    
            connection.commit();
            connection.close()
            
            if(str(self.cycle_num) == "2"):                    
                    self.test_id_arr=[]
                    self.load=[]
                    self.deflc=[]     
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("select TEST_ID,LOAD,DEFLCTION FROM STG_TEST_DATA")                 
                    for x in results:
                             self.test_id_arr.append(str(x[0]))
                             self.load.append(str(x[1]))
                             self.deflc.append(str(x[2]))
                    connection.close()
                    if(self.radioButton.isChecked()):
                            connection = sqlite3.connect("tyr.db")              
                            with connection:
                                cursor = connection.cursor()
                                for x in range(len(self.load)):
                                        cursor.execute("UPDATE DEFLECTION_DATA set DEF_2='"+str(self.deflc[x])+"' WHERE LOAD='"+str(self.load[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'")
                                        cursor.execute("UPDATE DEFLECTION_DATA set AVG_DEF=(DEF_2+DEF_1)/2 ,MAX_DEF= CASE WHEN DEF_1 > DEF_2 THEN DEF_1 ELSE DEF_2 END, MIN_DEF=CASE WHEN DEF_1 < DEF_2 THEN DEF_1 ELSE DEF_2 END WHERE LOAD='"+str(self.load[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'") 
                            connection.commit();
                            connection.close()                   
                    else:
                            connection = sqlite3.connect("tyr.db")              
                            with connection:
                                cursor = connection.cursor()
                                for x in range(len(self.load)):
                                        cursor.execute("UPDATE LOAD_DATA set LOAD_2='"+str(self.load[x])+"' WHERE DEFLECTION='"+str(self.deflc[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'")
                                        cursor.execute("UPDATE LOAD_DATA set AVG_LOAD=(LOAD_2+LOAD_1)/2 ,MAX_LOAD= CASE WHEN LOAD_1 > LOAD_2 THEN LOAD_1 ELSE LOAD_2 END, MIN_LOAD=CASE WHEN LOAD_1 < LOAD_2 THEN LOAD_1 ELSE LOAD_2 END WHERE DEFLECTION='"+str(self.deflc[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'") 
                            connection.commit();
                            connection.close()                   

                            print("ok--load data table")
            elif(str(self.cycle_num) == "3"):                    
                    self.test_id_arr=[]
                    self.load=[]
                    self.deflc=[]     
                    
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("select TEST_ID,LOAD,DEFLCTION FROM STG_TEST_DATA")                 
                    for x in results:
                             self.test_id_arr.append(str(x[0]))
                             self.load.append(str(x[1]))
                             self.deflc.append(str(x[2]))
                    connection.close()
                    if(self.radioButton.isChecked()):     
                            connection = sqlite3.connect("tyr.db")              
                            with connection:
                                cursor = connection.cursor()
                                for x in range(len(self.load)):
                                        cursor.execute("UPDATE DEFLECTION_DATA set DEF_3='"+str(self.deflc[x])+"' WHERE LOAD='"+str(self.load[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'")
                                        cursor.execute("UPDATE DEFLECTION_DATA set AVG_DEF=(DEF_2+DEF_1+DEF_3)/3 ,MAX_DEF= (select max(DEFLCTION) from TEST_DATA WHERE LOAD='"+str(self.load[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'), MIN_DEF=((select min(DEFLCTION) from TEST_DATA WHERE LOAD='"+str(self.load[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"')) WHERE LOAD='"+str(self.load[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'") 
                            connection.commit();
                            connection.close()
                    else:
                            connection = sqlite3.connect("tyr.db")              
                            with connection:
                                cursor = connection.cursor()
                                for x in range(len(self.load)):
                                        cursor.execute("UPDATE LOAD_DATA set LOAD_3='"+str(self.load[x])+"' WHERE DEFLECTION='"+str(self.deflc[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'")
                                        #print("UPDATE LOAD_DATA set LOAD_2='"+str(self.load[x])+"' WHERE DEFLECTION='"+str(self.deflc[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'")
                                        
                                        cursor.execute("UPDATE LOAD_DATA set AVG_LOAD=(LOAD_2+LOAD_1+LOAD_3)/3 ,MAX_LOAD= (select max(LOAD) from TEST_DATA WHERE DEFLCTION='"+str(self.deflc[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'), MIN_LOAD=(select min(LOAD) from TEST_DATA WHERE DEFLCTION='"+str(self.deflc[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"') WHERE DEFLECTION='"+str(self.deflc[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'") 
                                        #print("UPDATE LOAD_DATA set AVG_LOAD=(LOAD_2+LOAD_1+LOAD_3)/3 ,MAX_LOAD= (select max(LOAD) from TEST_DATA WHERE DEFLCTION='"+str(self.deflc[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'), MIN_LOAD=(select min(LOAD) from TEST_DATA WHERE DEFLCTION='"+str(self.deflc[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"') WHERE DEFLECTION='"+str(self.deflc[x])+"' and TEST_ID='"+str(self.test_id_arr[x])+"'") 
                         
                            connection.commit();
                            connection.close() 
                            print("Cycle - 3 ok--load data table")
            else:
                   print("ok")
            
        #self.load_data()
        #print("Save completed")
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
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)
        self.create_pdf_Tear()
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
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                    cursor = connection.cursor()                
                    cursor.execute("update global_var set PRE_LOAD='"+str(self.lineEdit_7.text())+"'")                 
        connection.commit()
        connection.close()
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_07_3_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
   
    def open_graph_data(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=pop_graph_data_Ui_MainWindow()
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
            self.cycle_id=str(self.tableWidget.item(row, 3).text())
            if(int(self.cycle_id) > 0):
                close = QMessageBox()
                close.setText("Confirm Deleteing Cycle : "+str(self.cycle_id))
                close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                close = close.exec()
                if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")              
                    with connection:        
                                    cursor = connection.cursor()                
                                    cursor.execute("DELETE FROM TEST_DATA WHERE ID = '"+self.cycle_id+"'")
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
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        
        connection = sqlite3.connect("tyr.db")
        if(self.radioButton.isChecked()):
                    if(str(self.cycle_num) == "2"):
                            self.tableWidget.setHorizontalHeaderLabels([' Load \n ('+str(self.comboBox_2.currentText())+') ',' Def_1 \n ('+str(self.comboBox_3.currentText())+') ',' Def_2 \n ('+str(self.comboBox_3.currentText())+') ','cycle_id'])
                            results=connection.execute("SELECT printf(\"%.2f\", LOAD),printf(\"%.2f\", DEF_1),printf(\"%.2f\", DEF_2),ID FROM DEFLECTION_DATA WHERE TEST_ID = '"+self.test_id+"' order by ID ASC")
                    elif(str(self.cycle_num) == "3"):
                            self.tableWidget.setHorizontalHeaderLabels([' Load \n ('+str(self.comboBox_2.currentText())+') ',' Def_1 \n ('+str(self.comboBox_3.currentText())+') ',' Def_2 \n ('+str(self.comboBox_3.currentText())+') ',' Def_3 \n ('+str(self.comboBox_3.currentText())+') ','cycle_id'])
                            results=connection.execute("SELECT printf(\"%.2f\", LOAD),printf(\"%.2f\", DEF_1),printf(\"%.2f\", DEF_2),printf(\"%.2f\", DEF_3),ID FROM DEFLECTION_DATA WHERE TEST_ID = '"+self.test_id+"' order by ID ASC")
                       
                    else:
                            self.tableWidget.setHorizontalHeaderLabels([' Load \n ('+str(self.comboBox_2.currentText())+') ',' Def_1 \n ('+str(self.comboBox_3.currentText())+') ','cycle_id'])
                            results=connection.execute("SELECT printf(\"%.2f\", LOAD),printf(\"%.2f\", DEF_1),ID FROM DEFLECTION_DATA WHERE TEST_ID = '"+self.test_id+"' order by ID ASC")
                            
        else:
                    if(str(self.cycle_num) == "2"):
                            self.tableWidget.setHorizontalHeaderLabels([' Deflection \n ('+str(self.comboBox_3.currentText())+') ',' Load_1 \n ('+str(self.comboBox_2.currentText())+') ',' Load_2 \n ('+str(self.comboBox_2.currentText())+') ','cycle_id'])
                            results=connection.execute("SELECT printf(\"%.2f\", DEFLECTION),printf(\"%.2f\", LOAD_1),printf(\"%.2f\", LOAD_2),ID FROM LOAD_DATA WHERE TEST_ID = '"+self.test_id+"' order by ID ASC")
                    elif(str(self.cycle_num) == "3"):
                            self.tableWidget.setHorizontalHeaderLabels([' Deflection \n ('+str(self.comboBox_3.currentText())+') ',' Load_1 \n ('+str(self.comboBox_2.currentText())+') ',' Load_2 \n ('+str(self.comboBox_2.currentText())+') ',' Load_3 \n ('+str(self.comboBox_2.currentText())+') ','cycle_id'])
                            results=connection.execute("SELECT printf(\"%.2f\", DEFLECTION),printf(\"%.2f\", LOAD_1),printf(\"%.2f\", LOAD_2),printf(\"%.2f\", LOAD_3),ID FROM LOAD_DATA WHERE TEST_ID = '"+self.test_id+"' order by ID ASC")
                       
                    else:
                            self.tableWidget.setHorizontalHeaderLabels([' Deflection \n ('+str(self.comboBox_3.currentText())+') ',' Load_1 \n ('+str(self.comboBox_2.currentText())+') ','cycle_id'])
                            results=connection.execute("SELECT printf(\"%.2f\", DEFLECTION),printf(\"%.2f\", LOAD_1),ID FROM LOAD_DATA WHERE TEST_ID = '"+self.test_id+"' order by ID ASC")
                            
                    
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
        if(self.radioButton.isChecked()): ### LOAD
                connection = sqlite3.connect("tyr.db")
                if(str(self.cycle_num) == "2"):
                        data2= [['Load \n ('+str(self.last_load_unit)+')', 'Def_1 \n ('+str(self.last_disp_unit)+')', 'Def_2 \n ('+str(self.last_disp_unit)+')','Avg.Defl','Max.Defl','Min_Defl']]
                        results=connection.execute("SELECT printf(\"%.2f\", A.LOAD),printf(\"%.2f\", A.DEF_1),printf(\"%.2f\", A.DEF_2),printf(\"%.2f\", A.AVG_DEF),printf(\"%.2f\", A.MAX_DEF),printf(\"%.2f\", A.MIN_DEF) FROM DEFLECTION_DATA A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ORDER BY ID ASC")  
                elif(str(self.cycle_num) == "3"):
                        data2= [['Load \n ('+str(self.last_load_unit)+')', 'Def_1 \n ('+str(self.last_disp_unit)+')', 'Def_2 \n ('+str(self.last_disp_unit)+')','Def_3 \n ('+str(self.last_disp_unit)+')','Avg.Defl','Max.Defl','Min_Defl']]
                        results=connection.execute("SELECT printf(\"%.2f\", A.LOAD),printf(\"%.2f\", A.DEF_1),printf(\"%.2f\", A.DEF_2),printf(\"%.2f\", A.DEF_3),printf(\"%.2f\", A.AVG_DEF),printf(\"%.2f\", A.MAX_DEF),printf(\"%.2f\", A.MIN_DEF) FROM DEFLECTION_DATA A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ORDER BY ID ASC")  
              
                else:
                        data2= [['Load \n ('+str(self.last_load_unit)+')', 'Def_1 \n ('+str(self.last_disp_unit)+')']]
                        results=connection.execute("SELECT printf(\"%.2f\", A.LOAD),printf(\"%.2f\", A.DEF_1) FROM DEFLECTION_DATA A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ORDER BY ID ASC") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                
        else:
                connection = sqlite3.connect("tyr.db")
                if(str(self.cycle_num) == "2"):
                        data2= [['Deflection \n ('+str(self.last_disp_unit)+')', 'Load_1 \n ('+str(self.last_load_unit)+')', 'Load_2 \n ('+str(self.last_load_unit)+')','Avg.Load','Max.Load','Min_Load']]
                        results=connection.execute("SELECT printf(\"%.2f\", A.DEFLECTION),printf(\"%.2f\", A.Load_1),printf(\"%.2f\", A.Load_2),printf(\"%.2f\", A.AVG_LOAD),printf(\"%.2f\", A.MAX_LOAD),printf(\"%.2f\", A.MIN_LOAD) FROM LOAD_DATA A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ORDER BY ID ASC")  
                elif(str(self.cycle_num) == "3"):
                        data2= [['Deflection \n ('+str(self.last_disp_unit)+')', 'Load_1 \n ('+str(self.last_load_unit)+')', 'Load_2 \n ('+str(self.last_load_unit)+')','Load_3 \n ('+str(self.last_load_unit)+')','Avg.Defl','Max.Defl','Min_Defl']]
                        results=connection.execute("SELECT printf(\"%.2f\", A.DEFLECTION),printf(\"%.2f\", A.Load_1),printf(\"%.2f\", A.Load_2),printf(\"%.2f\", A.Load_3),printf(\"%.2f\", A.AVG_LOAD),printf(\"%.2f\", A.MAX_LOAD),printf(\"%.2f\", A.MIN_LOAD) FROM LOAD_DATA A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ORDER BY ID ASC")  
              
                else:
                        data2= [['Deflection \n ('+str(self.last_disp_unit)+')', 'Load_1 \n ('+str(self.last_load_unit)+')']]
                        results=connection.execute("SELECT printf(\"%.2f\", A.DEFLECTION),printf(\"%.2f\", A.Load_1) FROM LOAD_DATA A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ORDER BY ID ASC") 
                for x in results:
                        data2.append(x)
                connection.close()
                
        
        y=300
        Elements=[]
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT A.CREATED_ON,A.TEST_ID,A.PART_NO,A.BATCH_ID,A.PART_NAME,A.HARDNESS,B.TEST_TYPE,A.MACHINE_NO,A.PARTY_NAME,A.MOTOR_REV_SPEED,A.MATERIAL,datetime(current_timestamp,'localtime'),A.COMMENTS,A.OPERATOR   FROM TEST_MST A, SPECIMEN_MST B WHERE A.PART_NO=B.PART_NO AND A.TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date-Time: ",str(x[0]),"Test No: ",str(x[1])],["Part No : ",str(x[2]),"Batch ID: ",str(x[3])],["Part Name:  ",str(x[4]),"Hardness:",str(x[5])],["Test Type:",str(x[6]),"M/C No:",str(x[7])],["Customer Name :",str(x[8]),"Test Speed (min/min) :",str(x[9])],["Material:",str(x[10]),"Report Date-Time: ",str(x[11])],["Tested By :", str(self.tested_by),"Operator :",str(x[13])]]
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
        
        self.chck_for_last_rec=0
        self.pre_load="0"
        self.load_cell_no="1"
        self.command_str_rev=""
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
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,IFNULL(NEW_TEST_AREA*0.1*0.1,0),IFNULL(PRE_LOAD,0) from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=200            
             self.max_load=float(x[2])
             #self.max_load=100
             self.max_length=float(self.test_guage_mm)-float(float(x[3]))
             self.flex_max_length=float(x[3])
             self.cof_max_length=float(x[4])
             #self.max_length=float(float(x[0])-float(x[3]))
             self.max_length=str(self.max_length).zfill(5)
             #print("Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
             self.unit_type=str(x[5])
             self.cs_area_cm=1
             self.pre_load=float(str(x[7]))
        connection.close()
        print("self.unit_type: "+str(self.unit_type)+" self.pre_load :"+str(self.pre_load)+" Max Load :"+str(self.max_load).zfill(5)+" self.max_length: "+str(self.max_length))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE,ISACTIVE_MODBUS,MODBUS_PORT,NON_MODBUS_PORT from SETTING_MST") 
        for x in results:
                 self.auto_rev_time_off=int(x[2])
                 self.break_sence=float(x[3])
                 self.break_sence=self.break_sence+float(self.pre_load)
                 print(" self.break_sence and preload :"+str(self.break_sence))
                 self.modbus_flag=str(x[4])
                 self.modbus_port=str(x[5])
                 self.non_modbus_port=str(x[6])
                 self.graph_type="Load Vs Travel"
                 if(self.graph_type=="Load Vs Travel"):
                             if(self.load_unit=="Kg" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Deflection (Mm)')
                                             self.axes.set_ylabel('Load (Kg)')
                             elif(self.load_unit=="Kg" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Deflection (Inch)')
                                             self.axes.set_ylabel('Load (Kg)')
                             elif(self.load_unit=="Kg" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Deflection (Cm)')
                                             self.axes.set_ylabel('Load (Kg)')                                                               
                             elif(self.load_unit=="Lb" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Deflection (Mm)')
                                             self.axes.set_ylabel('Load (Lb)')
                             elif(self.load_unit=="Lb" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Deflection (Cm)')
                                             self.axes.set_ylabel('Load (Lb)') 
                             elif(self.load_unit=="Lb" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Deflection (Inch)')
                                             self.axes.set_ylabel('Load (Lb)')                                                         
                             elif(self.load_unit=="N" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Deflection (Mm)')
                                             self.axes.set_ylabel('Load (N)')                                                         
                             elif(self.load_unit=="N" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Deflection (Cm)')
                                             self.axes.set_ylabel('Load (N)')                                 
                             elif(self.load_unit=="N" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Deflection (Inch)')
                                             self.axes.set_ylabel('Load (N)')
                             elif(self.load_unit=="KN" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Deflection (Mm)')
                                             self.axes.set_ylabel('Load (KN)')                                                         
                             elif(self.load_unit=="KN" and self.disp_unit=="Cm"):
                                             self.axes.set_xlabel('Deflection (Cm)')
                                             self.axes.set_ylabel('Load (KN)')                                 
                             elif(self.load_unit=="KN" and self.disp_unit=="Inch"):
                                             self.axes.set_xlabel('Deflection (Inch)')
                                             self.axes.set_ylabel('Load (KN)')
                             elif(self.load_unit=="gm" and self.disp_unit=="Mm"):
                                             self.axes.set_xlabel('Deflection (Mm)')
                                             self.axes.set_ylabel('Load (gm)') 
                             else:    
                                             self.axes.set_xlabel('Deflection (Mm)')
                                             self.axes.set_ylabel('Load (Kg)')
                                        
                 elif(self.graph_type=="Load Vs Time"):
                         #print("inside sadasdasd")
                         self.axes.set_xlabel('Time (Sec)')
                         self.axes.set_ylabel("'"+str(self.load_unit)+"'")
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
            
            
            if(self.goahead_flag==1):
                b = bytes(self.command_str_rev, 'utf-8')
                self.ser.write(b)
            else:   
                print("rev speed command problem")
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
        
        #time.sleep(2)
        self.timer1.setInterval(1)     
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
                    
                self.test_type="Compression"    
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
                self.graph_type="Load Vs Travel"
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
            if(float(self.input_speed_val) <= float(self.speed_val)):
                 #print(" Ok ")
                 self.goahead_flag=1
                 self.calc_speed=(float(self.input_speed_val)/float(self.speed_val))*1000                 
                 #print(" calc Speed : "+str(self.calc_speed))
                 #print(" command: *P"+str(self.calc_speed)+" \r")
                 #self.command_str="*P%04d"%self.calc_speed+"_%04d"%self.break_sence+"\r"
                 self.command_str="*P%04d"%self.calc_speed+"_%0.2f"%self.break_sence+"\r"
                 print("Morot Speed and Breaking speed Command  :"+str(self.command_str))
            else:
                 print(" not Ok ")
            
            if(float(self.input_rev_speed_val) <= float(self.speed_val)):
                 #print(" Ok ")
                 self.goahead_flag=1
                 self.calc_speed=(float(self.input_rev_speed_val)/float(self.speed_val))*1000                 
                 #print(" calc Speed : "+str(self.calc_speed))
                 #print(" command: *P"+str(self.calc_speed)+" \r")
                 #self.command_str="*P%04d"%self.calc_speed+"_%04d"%self.break_sence+"\r"
                 self.command_str_rev="*Y%04d"%self.calc_speed+"\r"
                 print("Rever Speed Command   :"+str(self.command_str_rev))
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
              ax.set_xlim(0,int(x[2]))
              ax.set_ylim(0,int(x[3]))  
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
        
        
        self.graph_type="Load Vs Travel"
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
                ax.set_xlabel('Deflection ('+str(self.last_disp_unit)+')')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        
        elif(self.graph_type=="Load Vs Time"):
                ax.set_xlabel('Time (sec)')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        else:
                ax.set_xlabel('Deflection ('+str(self.last_disp_unit)+')')
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
        
        if(self.graph_type=="Load Vs Travel"):
                ax.set_ylabel('Load  ('+str(self.last_load_unit)+')')
                ax.set_xlabel(' Deflection ('+str(self.last_disp_unit)+')')
        else:
                ax.set_ylabel('Load  ('+str(self.last_load_unit)+')')
                ax.set_xlabel(' Deflection ('+str(self.last_disp_unit)+')')
        
        self.draw()       
    

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_77_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
