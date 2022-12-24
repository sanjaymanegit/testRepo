


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow
from comment_popup import comment_Ui_MainWindow


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





class TY_23_PEELOFF_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1341, 711))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.frame.setFont(font)
        self.frame.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(970, 20, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 500, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(650, 570, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 230, 1331, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(650, 640, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(1040, 180, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(150, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(920, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 180, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(760, 260, 571, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 6, item)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(590, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(590, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(730, 130, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(30, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(150, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(650, 310, 81, 51))
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("value", 100.0)
        self.lcdNumber.setProperty("intValue", 100)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(650, 270, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_2.setGeometry(QtCore.QRect(650, 410, 81, 51))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setProperty("value", 100.0)
        self.lcdNumber_2.setProperty("intValue", 100)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        
        self.label_13_2 = QtWidgets.QLabel(self.frame)
        self.label_13_2.setGeometry(QtCore.QRect(650, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13_2.setFont(font)
        self.label_13_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_13_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13_2.setObjectName("label_13_2")
        
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 250, 611, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(770, 520, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(770, 560, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(770, 590, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(770, 640, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(770, 670, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(760, 540, 581, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(760, 580, 581, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(760, 620, 581, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(760, 660, 581, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_6.setFont(font)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(810, 480, 20, 231))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setGeometry(QtCore.QRect(910, 480, 20, 231))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setGeometry(QtCore.QRect(1050, 480, 20, 231))
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.frame)
        self.line_11.setGeometry(QtCore.QRect(1190, 480, 20, 231))
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setObjectName("line_11")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(760, 500, 581, 21))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(1100, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(1220, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(960, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(840, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.line_12 = QtWidgets.QFrame(self.frame)
        self.line_12.setGeometry(QtCore.QRect(760, 470, 581, 20))
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.frame)
        self.line_13.setGeometry(QtCore.QRect(750, 480, 20, 231))
        self.line_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_13.setLineWidth(3)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setObjectName("line_13")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(850, 510, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(850, 550, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(850, 590, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(850, 630, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(960, 510, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(960, 550, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(960, 590, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(960, 630, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(960, 670, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(850, 670, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(1110, 510, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame)
        self.label_38.setGeometry(QtCore.QRect(1110, 550, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_38.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.frame)
        self.label_39.setGeometry(QtCore.QRect(1110, 590, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame)
        self.label_40.setGeometry(QtCore.QRect(1110, 630, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_40.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.frame)
        self.label_41.setGeometry(QtCore.QRect(1110, 670, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame)
        self.label_42.setGeometry(QtCore.QRect(1220, 510, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_42.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame)
        self.label_43.setGeometry(QtCore.QRect(1220, 550, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_43.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.frame)
        self.label_44.setGeometry(QtCore.QRect(1220, 590, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.frame)
        self.label_45.setGeometry(QtCore.QRect(1220, 630, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_45.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.frame)
        self.label_46.setGeometry(QtCore.QRect(1220, 670, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(320, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(840, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(150, 130, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 130, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_49 = QtWidgets.QLabel(self.frame)
        self.label_49.setGeometry(QtCore.QRect(590, 20, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_49.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(1030, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1030, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(1130, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(1130, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(770, 480, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.frame)
        self.label_51.setGeometry(QtCore.QRect(730, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(590, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(730, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.goAhead="Yes"
        self.test_id_exist="No"
        self.timer3=QtCore.QTimer()
        self.sc_blank=""
        self.cycle_num=0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", datetime.datetime.now().strftime("%B  %d , %Y %I:%M ")+""))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.pushButton_13.setText(_translate("MainWindow", "All"))
        self.pushButton_14.setText(_translate("MainWindow", "Return"))
        self.label_21.setText(_translate("MainWindow", "Compleated Successfully. "))
        self.label_21.hide()
        self.label_5.setText(_translate("MainWindow", "Spec.Details"))
        self.label_6.setText(_translate("MainWindow", "Speciment Name :"))
        
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setHorizontalHeaderLabels(['Avg. Load (N)','First Peak Load (N)','Max Load (N)','Min Load (N)','Layers','REC.NO '])  
        '''
        
        '''
        self.label_9.setText(_translate("MainWindow", "Party Name :"))
        self.label_10.setText(_translate("MainWindow", "Total Samples :"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "001"))
        self.label_13.setText(_translate("MainWindow", "LOAD (N) :"))
        self.label_13_2.setText(_translate("MainWindow", "Distance (mm) :"))
        self.label_22.setText(_translate("MainWindow", "Running......"))
        self.label_22.hide()
        self.label_15.setText(_translate("MainWindow", "Max :"))
        self.label_16.setText(_translate("MainWindow", "Min :"))
        self.label_17.setText(_translate("MainWindow", "Avg :"))
        self.label_18.setText(_translate("MainWindow", "Std. :"))
        self.label_19.setText(_translate("MainWindow", "Var. :"))
        self.label_23.setText(_translate("MainWindow", "Max Loads"))
        self.label_24.setText(_translate("MainWindow", "Min Loads"))
        self.label_25.setText(_translate("MainWindow", "First Peak"))
        self.label_26.setText(_translate("MainWindow", "Avg Load"))
        self.label_27.setText(_translate("MainWindow", "0.00"))
        self.label_28.setText(_translate("MainWindow", "0.00"))
        self.label_29.setText(_translate("MainWindow", "0.00"))
        self.label_30.setText(_translate("MainWindow", "0.00"))
        self.label_31.setText(_translate("MainWindow", "0.99"))
        self.label_32.setText(_translate("MainWindow", "0.00"))
        self.label_33.setText(_translate("MainWindow", "0.00"))
        self.label_34.setText(_translate("MainWindow", "0.00"))
        self.label_35.setText(_translate("MainWindow", "0.00"))
        self.label_36.setText(_translate("MainWindow", "0.00"))
        self.label_37.setText(_translate("MainWindow", "0.00"))
        self.label_38.setText(_translate("MainWindow", "0.00"))
        self.label_39.setText(_translate("MainWindow", "0.00"))
        self.label_40.setText(_translate("MainWindow", "0.00"))
        self.label_41.setText(_translate("MainWindow", "0.00"))
        self.label_42.setText(_translate("MainWindow", "0.00"))
        self.label_43.setText(_translate("MainWindow", "0.00"))
        self.label_44.setText(_translate("MainWindow", "0.00"))
        self.label_45.setText(_translate("MainWindow", "0.00"))
        self.label_46.setText(_translate("MainWindow", "0.00"))
        
        self.label_47.setText(_translate("MainWindow", "Layers :"))
        self.label_48.setText(_translate("MainWindow", "BatchID:"))
        self.label_49.setText(_translate("MainWindow", "PEELOFF TEST"))
        self.pushButton_5.setText(_translate("MainWindow", "Email"))
        self.pushButton_6.setText(_translate("MainWindow", "Save"))
        self.pushButton_7.setText(_translate("MainWindow", "Report View"))
        self.pushButton_8.setText(_translate("MainWindow", "Report Print"))
        self.label_50.setText(_translate("MainWindow", "Stat."))
        self.label_51.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Unit :"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "N/mm"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Kgf/cm"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Lbs/inch"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "MPa/mm"))
        
        self.sc_blank =PlotCanvas_blank(self)          
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
        
        
        self.pushButton_14.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(self.start_test_peeloff)
        self.comboBox.currentTextChanged.connect(self.onchage_combo)
        self.pushButton_13.clicked.connect(self.show_all_specimens)
        
        self.pushButton_8.clicked.connect(self.print_file)
        self.pushButton_5.clicked.connect(self.open_email_report)
        self.pushButton_6.clicked.connect(self.save_data)
        self.pushButton_7.clicked.connect(self.open_pdf)
        self.tableWidget.doubleClicked.connect(self.delete_cycle)
        
        #self.reset()
        self.load_data()
        
        
    def reset(self):        
        if(self.timer3.isActive()): 
           self.timer3.stop() 
        
        #self.sc_blank =PlotCanvas_blank(self) 
        #self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
        
        
    
    def load_data(self):
        self.i=0
        self.comboBox.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SPECIMEN_NAME FROM SPECIMEN_MST") 
        for x in results:            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()             
            
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'TEST_MST'")       
        for x in results:           
                 self.label_12.setText(str(x[0]).zfill(3))
                 self.test_id=str(x[0])
        connection.close()
        self.onchage_combo()
        self.show_grid_data_peeloff()
    
    def delete_cycle(self):
        i = self.tableWidget.rowCount()   
        if(i>0):
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
                                        cursor = connection.cursor()                
                                        cursor.execute("DELETE FROM CYCLES_MST WHERE CYCLE_ID = '"+self.cycle_id+"'")
                                        
                        connection.commit();
                        connection.close()
                        self.show_grid_data_peeloff()
                        
            else:
                    pass    
       
    def calculations(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select round(max(AVG_FORCE),2), round(max(DEF_LOAD),2), round(max(MAX_FORCE),2), round(max(MIN_FORCE),2) from CYCLES_MST WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
        for x in results:
                    self.label_27.setText(str(x[0]))  #111.00
                    self.label_31.setText(str(x[1]))   #666.99
                    self.label_37.setText(str(x[2]))   #B11.00"
                    self.label_42.setText(str(x[3]))    #G34.00                 
        connection.close()
       
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select round(min(AVG_FORCE),2), round(min(DEF_LOAD),2), round(min(MAX_FORCE),2), round(min(MIN_FORCE),2) from CYCLES_MST WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
        for x in results:
                    self.label_28.setText(str(x[0]))  #222.00
                    self.label_32.setText(str(x[1]))   #777.99
                    self.label_38.setText(str(x[2]))   #C22.00"
                    self.label_43.setText(str(x[3]))    #F56.00                 
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select round(avg(AVG_FORCE),2), round(avg(DEF_LOAD),2), round(avg(MAX_FORCE),2), round(avg(MIN_FORCE),2) from CYCLES_MST WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
        for x in results:
                    self.label_29.setText(str(x[0]))  #333.00
                    self.label_33.setText(str(x[1]))   #888.00
                    self.label_39.setText(str(x[2]))   #D33.00"
                    self.label_44.setText(str(x[3]))    #Y66.00                 
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select round(AVG_FORCE,2), round(DEF_LOAD,2), round(MAX_FORCE,2), round(MIN_FORCE,2) from CYCLES_MST WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
        for x in results:
                    self.label_30.setText(str(np.std(x[0])))  #444.00
                    self.label_34.setText(str(np.std(x[1])))   #999.00
                    self.label_40.setText(str(np.std(x[2])))   #E34.00"
                    self.label_45.setText(str(np.std(x[3])))    #J69.00                 
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select round(AVG_FORCE,2), round(DEF_LOAD,2), round(MAX_FORCE,2), round(MIN_FORCE,2) from CYCLES_MST WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
        for x in results:
                    self.label_36.setText(str(np.var(x[0])))  #555.00
                    self.label_35.setText(str(np.var(x[1])))   #A10.00
                    self.label_41.setText(str(np.var(x[2])))   #E34.00"
                    self.label_46.setText(str(np.var(x[3])))    #K87.00                 
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select count(cycle_id) from CYCLES_MST WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
        for x in results:
                    self.label_51.setText(str(x[0]))                           
        connection.close()
        
        
    
    def onchage_combo(self):                      
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select PARTY_NAME,GUAGE_LENGTH_MM,SPECIMEN_SPECS FROM SPECIMEN_MST WHERE SPECIMEN_NAME='"+self.comboBox.currentText()+"'")                 
        for x in results:
           #self.lineEdit.setText(str(x[0])) # Layers
            self.lineEdit_2.setText(str(x[2])) # Sepc Details
           #self.lineEdit_3.setText(str(x[0])) # Batch ID
            self.lineEdit_5.setText(str(x[0]))#Party NAme
            
        connection.close()
        
        
    def start_test_peeloff(self):
        #elf.label_35.setText("")
        #self.validation()
        if(self.goAhead=="Yes"):
            
               connection = sqlite3.connect("tyr.db")
               results=connection.execute("select count(*) from TEST_MST WHERE TEST_ID = '"+str(self.label_12.text())+"'")       
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
                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"'")
                          cursor.execute("UPDATE TEST_MST SET SPECIMEN_NAME='"+str(self.comboBox.currentText())+"',BATCH_ID='"+str(self.lineEdit_3.text())+"',PARTY_NAME='"+str(self.lineEdit_5.text())+"'  WHERE  TEST_ID = '"+str(self.label_12.text())+"'")
                        connection.commit();
                        connection.close()
                        
               else:        
                        ### INSERT 
                        connection = sqlite3.connect("tyr.db")              
                        with connection:        
                          cursor = connection.cursor()                  
                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"'")
                          cursor.execute("INSERT INTO TEST_MST(SPECIMEN_NAME,BATCH_ID,PARTY_NAME,TEST_TYPE) VALUES('"+self.comboBox.currentText()+"','"+self.lineEdit_3.text()+"','"+self.lineEdit_5.text()+"','PEELOFF')")
                        connection.commit();
                        connection.close()
                
                
               self.sc_new =PlotCanvas_Auto(self,width=5, height=4, dpi=80)
               self.gridLayout.addWidget(self.sc_new, 1, 0, 1, 1)
                
               connection = sqlite3.connect("tyr.db")
               results=connection.execute("SELECT COUNT(*) FROM STG_GRAPH_MST")
               rows=results.fetchall()
               connection.close()
               if(int(rows[0][0]) > -2 ):
                    self.timer3.setInterval(1000)        
                    self.timer3.timeout.connect(self.show_load_cell_val)
                    self.timer3.start(1)
                
        else:
                print("validation Error")
                
    def validation(self):
        self.goAhead="No"
        '''
        if(str(self.lineEdit.text()) == ""):
               self.label_35.setText("Initail Size Parameters  1 should not be NULL.")
               self.label_35.show()
        elif(str(self.lineEdit_2.text()) == "" and self.label_31.text() == "(Rectangle)"):
               self.label_35.setText("Initail Size Parameters  2 should not be NULL.")
               self.label_35.show()
        elif(str(self.lineEdit_3.text()) == ""):
               self.label_35.setText("Inital Area should not be NULL.")
               self.label_35.show()
        elif(str(self.lineEdit_4.text()) == ""):
               self.label_35.setText("Guage Length Should not be NULL")
               self.label_35.show()
        elif(str(self.lineEdit_5.text()) == ""):
               self.label_35.setText("Final Lenght Should not be NULL")
               self.label_35.show()
        elif(str(self.lineEdit_6.text()) == ""):
               self.label_35.setText("Final Size Parameters  1 should not be NULL.")
               self.label_35.show()
        elif(str(self.lineEdit_7.text()) == "" and self.label_31.text() == "(Rectangle)"):
               self.label_35.setText("Size Parameters  2 should not be NULL.")
               self.label_35.show()
        else:
               self.goAhead="Yes"
        '''
        self.goAhead="Yes"
        if(self.goAhead=="Yes"):
               connection = sqlite3.connect("tyr.db")
               results=connection.execute("select count(*) from TEST_MST WHERE TEST_ID = '"+str(self.label_12.text())+"'")       
               for x in results:           
                 if(int(x[0]) > 0):
                       self.test_id_exist="Yes"
                 else:
                       self.test_id_exist="No"                     
               connection.close() 
               
               if(self.test_id_exist=="Yes"):                   
                   connection = sqlite3.connect("tyr.db")
                   with connection:        
                       cursor = connection.cursor()
                       cursor.execute("UPDATE TEST_MST SET      WHERE  TEST_ID = '"+str(self.label_12.text())+"'")
                       
                   connection.commit();
                   connection.close()
                   print("Record updated  in TEST_MST:")
                   
               else:
                   print("Record is not updated  in TEST_MST:")
                   self.label_35.setText("Test Data is not Saved Successfully")
    
    def show_load_cell_val(self):      
        
        self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q)))        
        self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))   #length
        
        if(str(self.sc_new.save_data_flg) =="Yes"):            
                self.reset()
                self.save_graph_data()
                self.sc_new.save_data_flg=""
                self.label_21.show()
                self.label_21.setText("Data Saved Successfully.")
                
        
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
    
    def show_all_specimens(self): 
        self.sc_data =PlotCanvas(self,width=5, height=4, dpi=80)    
        self.gridLayout.addWidget(self.sc_data, 1, 0, 1, 1)
       
            
    def save_graph_data(self):
         self.cycle_num=0
         if (len(self.sc_new.arr_p) > 1):            
            self.cycle_num=int(str(self.label_51.text()))+1
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)):                     
                        cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM) VALUES ('"+str(int(self.sc_new.arr_p[g]))+"','"+str(self.sc_new.arr_q[g])+"')")
            connection.commit();
            connection.close()
            
            self.get_defarmetion_point()
            
            connection = sqlite3.connect("tyr.db")              
            with connection:        
                  cursor = connection.cursor()
                  #print("ok1")
                  try:
                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"',LAYERS='"+str(self.lineEdit.text())+"'")                          
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM) FROM STG_GRAPH_MST)")
                          cursor.execute("UPDATE GLOBAL_VAR SET MIN_FORCE=(SELECT MIN(Y_NUM) FROM STG_GRAPH_MST)")
                          cursor.execute("UPDATE GLOBAL_VAR SET COF_MAX_FORCE=(SELECT MAX(Y_NUM) FROM STG_GRAPH_MST)")
                          cursor.execute("UPDATE GLOBAL_VAR SET COF_AVG_FORCE=(SELECT AVG(Y_NUM) FROM STG_GRAPH_MST)")
                          
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_PEAK_LOAD_MM=(SELECT X_NUM FROM STG_GRAPH_MST WHERE Y_NUM=(SELECT STG_PEAK_LOAD_KG FROM GLOBAL_VAR))")                         
                          #print("ok2")
                          cursor.execute("INSERT INTO CYCLES_MST(TEST_ID,TEST_METHOD,AVG_FORCE,DEF_LOAD,MAX_FORCE,MIN_FORCE,LAYERS) SELECT TEST_ID,'PEELOFF',COF_AVG_FORCE,DEF_LOAD,COF_MAX_FORCE,MIN_FORCE,LAYERS FROM GLOBAL_VAR")
                          
                          cursor.execute("UPDATE CYCLES_MST SET CYCLE_NUM='"+str(self.cycle_num)+"'  WHERE GRAPH_ID IS NULL")
                          cursor.execute("UPDATE CYCLES_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")
                          
                          cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM) SELECT X_NUM,Y_NUM FROM STG_GRAPH_MST")                  
                          cursor.execute("UPDATE GRAPH_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL") 
                          cursor.execute("UPDATE TEST_MST SET STATUS='LOADED GRAPH' ,BATCH_ID='"+str(self.lineEdit_3.text())+"',PARTY_NAME='"+str(self.lineEdit_5.text())+"' WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")                  
                          cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_X_LENGTH=(SELECT GRAPH_SCALE_CELL_2 FROM SETTING_MST),GRAPH_SCAL_Y_LOAD=(SELECT GRAPH_SCALE_CELL_1 FROM SETTING_MST)  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                    
                  except:
                          print("SQL Error")
                      
            connection.commit();
            connection.close()            
            print("Data Saved Ok in STG_GRAPH_MST")           
            self.show_grid_data_peeloff()
            
        
    def get_defarmetion_point(self):
        c=0.0
        def_point=-1.00
        def_point_x=-1.00
        def_point_y=-1.00
        def_buffer_6_prc=0.0
        self.yeild_strength=""
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
                c=float(round(x[1],2))
            else:    
                if(float(x[1]) > float(c)):
                    c=float(x[1])
                    continue
                elif(float(x[1]) == float(c)):
                    def_point=float(x[0])
                    def_point_y=float(x[1])
                    print("Break 1 Point :"+str(def_point_y))
                    break
                elif(float(x[1]) <  float(c)):
                    def_point=float(x[0])
                    def_point_y=float(x[1])
                    print("Break 1.5 Point :"+str(def_point_y))
                    break
                else:
                    c=float(x[1])
                    def_point=float(x[0])
                    def_point_y=float(x[1])
                    print("Break 2 Point :"+str(def_point_y))
                    break                    
        connection.close()        
        
        self.yeild_strength=str(round(def_point_y,2))
        connection = sqlite3.connect("tyr.db")              
        with connection:
                cursor = connection.cursor()
                if(float(def_point) > 0):
                    cursor.execute("UPDATE GLOBAL_VAR SET DEF_POINT = '"+str(def_point)+"',DEF_LOAD='"+str(def_point_y)+"'")
                else:                    
                    cursor.execute("UPDATE GLOBAL_VAR SET DEF_POINT = 0,DEF_LOAD=0")
                    
        connection.commit();
        connection.close()
    
    def show_grid_data_peeloff(self):        
        #print("inside tear list.....")
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setHorizontalHeaderLabels(['Avg. Load (N)','First Peak Load (N)','Max Load (N)','Min Load (N)','Layers','REC.NO '])        
        self.tableWidget.setColumnWidth(0, 170)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)
        
        
        connection = sqlite3.connect("tyr.db")
         
        results=connection.execute("SELECT printf(\"%.2f\", AVG_FORCE),printf(\"%.2f\", DEF_LOAD),printf(\"%.2f\", MAX_FORCE),printf(\"%.2f\", MIN_FORCE), printf(\"%.2f\", LAYERS),CYCLE_ID FROM CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' order by cycle_id Asc")
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()
        self.calculations()
       
    
    def print_file(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POP_TEST_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_email_report(self):
        #self.test_id=(self.tableWidget.item(row, 1).text() )
        self.test_id=self.label_12.text()
        print(" test_id :"+str(self.test_id))  
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("update global_var set EMAIL_TEST_ID='"+str(self.test_id)+"'")                 
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
                    cursor.execute("update global_var set EMAIL_TEST_ID='"+str(self.test_id)+"'")                 
        connection.commit()
        connection.close()
            
        self.window = QtWidgets.QMainWindow()
        self.ui=comment_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def save_data(self):
        #print(" test_id :"+str(self.test_id))  
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                    cursor = connection.cursor()                
                    cursor.execute("update TEST_MST SET BATCH_ID='"+str(self.lineEdit_3.text())+"', PARTY_NAME='"+str(self.lineEdit_5.text())+"',JOB_NAME='"+str(self.lineEdit_2.text())+"' WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ")
                    self.label_21.show()
                    self.label_21.setText("Data Saved Successfully .")
                    
        connection.commit()
        connection.close()
        
    def create_pdf_PEELOFF(self):        
#        connection = sqlite3.connect("tyr.db")
#        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
#        for x in results:
#            self.graph_typex=x[0]
#            self.unit_typex=x[1]
#        connection.close()
        self.unit_typex="N/mm"
        if(self.unit_typex == "N/mm"):
            data2= [ ['Spec. \n No', 'Avg. Load \n (N)', 'Load at First Peak\n (N)', 'Max Load \n (N)', 'Min Load \n (N)','Layers\n']]
        else:
            data2= [ ['Spec. \n No', 'Avg. Load \n (N)', 'Load at First Peak\n (N)', 'Max Load \n (N)', 'Min Load \n (N)','Layers\n']]
          
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT CYCLE_NUM,printf(\"%.4f\", A.AVG_FORCE),printf(\"%.2f\", A.DEF_LOAD),printf(\"%.2f\", A.MAX_FORCE),printf(\"%.2f\", A.MIN_FORCE),printf(\"%.2f\", A.LAYERS) FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'AVG',printf(\"%.4f\", avg(A.AVG_FORCE)),printf(\"%.2f\",avg(A.DEF_LOAD)),printf(\"%.2f\", avg(A.MAX_FORCE)),printf(\"%.2f\", avg(A.MIN_FORCE)),printf(\"%.2f\", avg(A.LAYERS)) FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MAX',printf(\"%.4f\", max(A.AVG_FORCE)),printf(\"%.2f\",max(A.DEF_LOAD)),printf(\"%.2f\", max(A.MAX_FORCE)),printf(\"%.2f\", max(A.MIN_FORCE)),printf(\"%.2f\", max(A.LAYERS)) FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MIN',printf(\"%.4f\", min(A.AVG_FORCE)),printf(\"%.2f\",min(A.DEF_LOAD)),printf(\"%.2f\", min(A.MAX_FORCE)),printf(\"%.2f\", min(A.MIN_FORCE)),printf(\"%.2f\", min(A.LAYERS)) FROM  CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        '''
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select round(AVG_FORCE,2), round(DEF_LOAD,2), round(MAX_FORCE,2), round(MIN_FORCE,2) from CYCLES_MST WHERE TEST_ID in ( SELECT TEST_ID FROM GLOBAL_VAR) ")       
        for x in results:                    
                    data2.append(['STDev',str(np.std(x[0])),str(np.std(x[1])),str(np.std(x[2])),str(np.std(x[3]))])
        connection.close()
        
        self.arr1=[]
        self.arr2=[]
        self.arr3=[]
        self.arr4=[]
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select round(AVG_FORCE,2), round(DEF_LOAD,2), round(MAX_FORCE,2), round(MIN_FORCE,2) from CYCLES_MST WHERE TEST_ID in ( SELECT TEST_ID FROM GLOBAL_VAR) ")       
        for x in results:
                        self.arr1.append(str(x[0]))
                        self.arr2.append(str(x[1]))
                        self.arr3.append(str(x[2]))
                        self.arr4.append(str(x[3])) 
        connection.close()
        #data2.append(['Var',str(np.std(self.arr1)),str(np.std(self.arr2)),str(np.std(self.arr3)),str(np.std(self.arr4)),'0']) 
        c=np.std(self.arr1)
        print(" arr1 :"+str(c))
        '''
        y=300
        Elements=[]
        summary_data=[]
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime')  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
        
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Specmen Shape:",str(x[9])],["Test Type:",str(x[3]),"Specmen Specs:",str(x[0])],["Party Name :",str(x[7]),"Motor Speed :",str(x[5])],["Guage Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", "Stech engineers testing machine","",""]]
      
        
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
        comments = Paragraph("    Remark : ______________________________________________________________________________", styles["Normal"])
        
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
        
         
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,blank,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/test_report.pdf', rightMargin=10,
                                leftMargin=20,
                                topMargin=20,
                                bottomMargin=30,)
        doc.build(Elements)
        
    def open_pdf(self):
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90) 
        self.create_pdf_PEELOFF() 
        
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
        results=connection.execute("SELECT GRAPH_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
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
            ax.set_xlabel('All-Distance (mm)')
        ax.set_ylabel('Load (N)')
        #self.connect('motion_notify_event', mouse_move)
        ax.legend()        
        self.draw()
        self.figure.savefig('last_graph.png',dpi=100)
        
        #ax.connect('motion_notify_event', mouse_move)
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
             #self.axes.set_title("Test Id="+str(x[1])+", Cycle No="+str(x[4])+", Job Name="+str(x[2])+", Batch Id="+str(x[3]))  
        connection.close()
        
        if(self.test_type=="Compress"):
            self.axes.set_xlabel('Compression (mm)')
        elif(self.test_type=="COF"):
            self.axes.set_xlabel('Length (mm)') 
        else:        
            self.axes.set_xlabel('Distance (mm)')
          
        self.axes.set_ylabel('Load (N)') 
        self.axes.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.q =0
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
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0) from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=int(x[0])
             if(str(x[1]) == "Flexural"):
                 self.test_type="Compress"
             else:
                  self.test_type=str(x[1])
             self.max_load=int(x[2])
             #self.max_load=100
             self.max_length=float(float(x[0])-float(x[3]))
             self.flex_max_length=float(x[3])
             self.cof_max_length=float(x[4])
             #self.max_load=str(self.max_load).zfill(5)
             #self.max_length=str(int(self.max_length)).zfill(5)
             #self.max_length=float(x[3])
             print("Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
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
                #print("started with default motor speed . Not gohead ")
            #self.ser.write(b'*D\r\n')
                
            #time.sleep(2)
            #========Final Motor start Command =========    
            self.ser.flush()
            if(self.test_type=="Compress"):
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                          self.command_str="*S2E%04d"%self.flexural_max_load+" %04d"%self.max_length+"\r"
                    else:
                          self.command_str="*S1E%04d"%self.flexural_max_load+" %04d"%self.max_length+"\r"
                    
                    print("self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)                 
                else:
                    print("Compress test not started ")               
                               
            elif(self.test_type=="Flexural"):
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                            #self.ser.write(b'*S2E0599 200\r')
                            self.command_str="*S2C%04d"%self.flexural_max_load+" %04d"%self.flexural_max_load+"\r"
                            #self.command_str="*S2E%04d"%self.flexural_max_load+" 0000\r"
                    else:
                            #self.command_str="*S1E%04d"%self.flexural_max_load+" 0000\r"
                            self.command_str="*S1C%04d"%self.flexural_max_load+" %04d"%self.flexural_max_load+"\r"
                            
                    print("self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    print("fluexural test started ")
                else:
                    
                    print("fluexural test not started ")
            elif(self.test_type=="COF"):                
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                        self.command_str="*S2F%04d"%self.cof_max_length+"_000.0\r"                        
                    else:
                        self.command_str="*S1F%04d"%self.cof_max_length+"_000.0\r"
                        
                    print("COF self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    print("COF test started ")   
                        
                else:
                    print("Error :Serial O/P is not getting ")               
                
                
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
                    self.p=int(self.test_guage_mm)-self.p
                    #print("self.p :"+str(self.p))
                elif(self.test_type=="Flexural"):
                    #self.p=self.p
                    self.p=int(self.test_guage_mm)-self.p
                else:
                    self.p=self.p
                    #self.p=int(self.test_guage_mm)-self.p
                    #self.p=self.p
                self.q=float(self.q)*9.81
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
                self.save_data_flg="No"
            else:                
               
                self.save_data_flg="Yes"
                self.on_ani_stop()
            
                   
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
             #self.axes.set_title("Test Id="+str(x[1])+", Cycle No="+str(x[4])+", Job Name="+str(x[2])+", Batch Id="+str(x[3]))  
        connection.close()
        
        
        ax.set_ylabel('Load (N) ')
        
        
        if(self.test_type=="Compress"):
            ax.set_xlabel('Compression (mm)')       
        else:
            ax.set_xlabel('Distance (mm)')
        self.draw() 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_23_PEELOFF_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
