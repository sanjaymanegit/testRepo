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
import pandas as pd
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


class ty_29_Ui_MainWindow(object):
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
        self.label_20.setGeometry(QtCore.QRect(1140, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 560, 81, 41))
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
        self.pushButton_13.setGeometry(QtCore.QRect(650, 630, 81, 41))
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
        self.line.setGeometry(QtCore.QRect(0, 230, 1341, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(1040, 200, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(660, 260, 661, 201))
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
        self.tableWidget.setColumnCount(5)
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
        font.setPointSize(10)
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
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(330, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 91, 31))
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
        self.label_12.setGeometry(QtCore.QRect(120, 20, 71, 31))
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
        self.lcdNumber.setGeometry(QtCore.QRect(840, 630, 81, 61))
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("value", 100.0)
        self.lcdNumber.setProperty("intValue", 100)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(750, 540, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
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
        self.label_15.setGeometry(QtCore.QRect(980, 670, 41, 31))
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
        self.label_16.setGeometry(QtCore.QRect(980, 640, 41, 21))
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
        self.label_17.setGeometry(QtCore.QRect(980, 590, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(950, 620, 391, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(950, 660, 391, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(1030, 530, 20, 181))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setGeometry(QtCore.QRect(1190, 530, 20, 181))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(950, 570, 391, 21))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(1210, 540, 121, 31))
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
        self.label_26.setGeometry(QtCore.QRect(1060, 540, 101, 31))
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
        self.line_12.setGeometry(QtCore.QRect(950, 520, 391, 20))
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.frame)
        self.line_13.setGeometry(QtCore.QRect(940, 530, 20, 181))
        self.line_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_13.setLineWidth(3)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setObjectName("line_13")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(1090, 590, 41, 41))
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
        self.label_28.setGeometry(QtCore.QRect(1090, 630, 41, 41))
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
        self.label_29.setGeometry(QtCore.QRect(1090, 670, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(1240, 590, 41, 31))
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
        self.label_32.setGeometry(QtCore.QRect(1240, 630, 41, 41))
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
        self.label_33.setGeometry(QtCore.QRect(1240, 670, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(120, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(10, 180, 81, 41))
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
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_49 = QtWidgets.QLabel(self.frame)
        self.label_49.setGeometry(QtCore.QRect(680, 10, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_49.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(1040, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 255, 227);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1040, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 255, 227);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(1170, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 255, 227);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(1170, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 255, 227);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(970, 540, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(330, 70, 51, 31))
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
        self.comboBox_2.setGeometry(QtCore.QRect(450, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.label_51 = QtWidgets.QLabel(self.frame)
        self.label_51.setGeometry(QtCore.QRect(450, 20, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.label_60 = QtWidgets.QLabel(self.frame)
        self.label_60.setGeometry(QtCore.QRect(10, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_60.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_60.setObjectName("label_60")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_9)
        self.lineEdit_9.setValidator(input_validator)
        self.lineEdit_9.setGeometry(QtCore.QRect(120, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_63 = QtWidgets.QLabel(self.frame)
        self.label_63.setGeometry(QtCore.QRect(230, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_63.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_63.setObjectName("label_63")
        ##########
        self.label_60_1 = QtWidgets.QLabel(self.frame)
        self.label_60_1.setGeometry(QtCore.QRect(330, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_60_1.setFont(font)
        self.label_60_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_60_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_60_1.setObjectName("label_60_1")
        self.lineEdit_9_1 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_9)
        self.lineEdit_9_1.setValidator(input_validator)
        self.lineEdit_9_1.setGeometry(QtCore.QRect(430, 130, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9_1.setFont(font)
        self.lineEdit_9_1.setObjectName("lineEdit_9_1")
        self.label_63_1 = QtWidgets.QLabel(self.frame)
        self.label_63_1.setGeometry(QtCore.QRect(510, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_63_1.setFont(font)
        self.label_63_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_63_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_63_1.setObjectName("label_63_1")
        
        
        
        
        
        #########
        self.line_14 = QtWidgets.QFrame(self.frame)
        self.line_14.setGeometry(QtCore.QRect(1010, 0, 20, 241))
        self.line_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_14.setLineWidth(3)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setObjectName("line_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(1170, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(1040, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(750, 630, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_2.setGeometry(QtCore.QRect(840, 540, 81, 61))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setProperty("value", 100.0)
        self.lcdNumber_2.setProperty("intValue", 100)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_61 = QtWidgets.QLabel(self.frame)
        self.label_61.setGeometry(QtCore.QRect(830, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_61.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_61.setObjectName("label_61")
        self.label_66 = QtWidgets.QLabel(self.frame)
        self.label_66.setGeometry(QtCore.QRect(690, 130, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_66.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.label_67)
        self.label_67.setValidator(input_validator)
        
        self.label_67.setGeometry(QtCore.QRect(850, 130, 60, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_67.setFont(font)
        self.label_67.setMaxLength(5)
        self.label_67.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_67.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_67.setObjectName("label_67")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_10)
        self.lineEdit_10.setValidator(input_validator)
        self.lineEdit_10.setGeometry(QtCore.QRect(450, 190, 60, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setMaxLength(5)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_68 = QtWidgets.QLabel(self.frame)
        self.label_68.setGeometry(QtCore.QRect(520, 190, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_68.setFont(font)
        self.label_68.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_68.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_68.setObjectName("label_68")
        self.line_17 = QtWidgets.QFrame(self.frame)
        self.line_17.setGeometry(QtCore.QRect(310, 0, 20, 241))
        self.line_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_17.setLineWidth(3)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setObjectName("line_17")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_11)
        self.lineEdit_11.setValidator(input_validator)
        self.lineEdit_11.setGeometry(QtCore.QRect(850, 190, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setMaxLength(5)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_70 = QtWidgets.QLabel(self.frame)
        self.label_70.setGeometry(QtCore.QRect(920, 190, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_70.setFont(font)
        self.label_70.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_70.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.frame)
        self.label_71.setGeometry(QtCore.QRect(660, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_71.setFont(font)
        self.label_71.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_71.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_71.setObjectName("label_71")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_12)
        self.lineEdit_12.setValidator(input_validator)
        self.lineEdit_12.setGeometry(QtCore.QRect(740, 480, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_72 = QtWidgets.QLabel(self.frame)
        self.label_72.setGeometry(QtCore.QRect(840, 480, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_72.setFont(font)
        self.label_72.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_72.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.frame)
        self.label_73.setGeometry(QtCore.QRect(940, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_73.setFont(font)
        self.label_73.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_73.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_73.setObjectName("label_73")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_13)
        self.lineEdit_13.setValidator(input_validator)
        self.lineEdit_13.setGeometry(QtCore.QRect(1020, 480, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_74 = QtWidgets.QLabel(self.frame)
        self.label_74.setGeometry(QtCore.QRect(1090, 480, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_74.setFont(font)
        self.label_74.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_74.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_74.setObjectName("label_74")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(1220, 480, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(680, 190, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_69 = QtWidgets.QLabel(self.frame)
        self.label_69.setGeometry(QtCore.QRect(690, 70, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_69.setFont(font)
        self.label_69.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_69.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_69.setObjectName("label_69")
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
        self.x_unit='mm'
        self.y_unit='N'
        self.start_test_by="load"  #### This status is "load" Or "elongation"
        self.status_str=""
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", datetime.datetime.now().strftime("%B  %d , %Y %I:%M ")+""))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.pushButton_13.setText(_translate("MainWindow", "All"))
        self.label_21.setText(_translate("MainWindow", ""))
        
        self.label_6.setText(_translate("MainWindow", "Spec.Name :"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Spec.No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Max.Load (Kgf)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Max. Length(mm)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Rec.No"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "100"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "67"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "PASS"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "11"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(_translate("MainWindow", "Party Name :"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "001"))
        self.label_13.setText(_translate("MainWindow", "Load \n"
" (Kgf) :"))
        self.label_22.setText(_translate("MainWindow", ""))
        self.label_15.setText(_translate("MainWindow", "Max :"))
        self.label_16.setText(_translate("MainWindow", "Min :"))
        self.label_17.setText(_translate("MainWindow", "Avg :"))
        self.label_25.setText(_translate("MainWindow", "Elongation (mm)"))
        self.label_26.setText(_translate("MainWindow", "Max. Load(Kgf)"))
        self.label_27.setText(_translate("MainWindow", "111.00"))
        self.label_28.setText(_translate("MainWindow", "222.00"))
        self.label_29.setText(_translate("MainWindow", "333.00"))
        self.label_31.setText(_translate("MainWindow", "666.99"))
        self.label_32.setText(_translate("MainWindow", "777.00"))
        self.label_33.setText(_translate("MainWindow", "888.00"))
        self.comboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(4, _translate("MainWindow", "New Item"))
        self.label_48.setText(_translate("MainWindow", "Batch ID:"))
        self.label_49.setText(_translate("MainWindow", "PROOF TEST"))
        self.pushButton_5.setText(_translate("MainWindow", "Email"))
        self.pushButton_6.setText(_translate("MainWindow", "Remark"))
        self.pushButton_7.setText(_translate("MainWindow", "Report View"))
        self.pushButton_8.setText(_translate("MainWindow", "Report Print"))
        self.label_50.setText(_translate("MainWindow", "Stat."))
        self.label_7.setText(_translate("MainWindow", "Unit :"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Kgf/mm"))
        self.label_51.setText(_translate("MainWindow", "MRF INDIA PPVT LTD"))
        self.label_60.setText(_translate("MainWindow", "Speed :"))
        self.label_63.setText(_translate("MainWindow", "(mm / min)"))
        
        self.label_60_1.setText("Rev.Speed:")
        self.label_63_1.setText("mm/min")
        
        self.pushButton_15.setText(_translate("MainWindow", "Return"))
        self.pushButton_9.setText(_translate("MainWindow", "Save"))
        self.label_14.setText(_translate("MainWindow", "Elongation: \n"
" (mm) "))
        self.label_61.setText(_translate("MainWindow", "Rectangle"))
        self.label_66.setText(_translate("MainWindow", "Test Time (sec) :"))
        self.label_67.setText(_translate("MainWindow", "5"))
        self.label_68.setText(_translate("MainWindow", "(Kgf.)"))
        self.label_70.setText(_translate("MainWindow", "(mm)"))
        self.label_71.setText(_translate("MainWindow", "Y- Axis:"))
        self.label_72.setText(_translate("MainWindow", "(Kgf.)"))
        self.label_73.setText(_translate("MainWindow", "X- Axis:"))
        self.label_74.setText(_translate("MainWindow", "(mm)"))
        self.pushButton_16.setText(_translate("MainWindow", "Set-Graph"))
        self.radioButton.setText(_translate("MainWindow", "Max. Elongation:"))
        self.radioButton_2.setText(_translate("MainWindow", "Max.Load:"))
        self.label_69.setText(_translate("MainWindow", "Shape :"))
        self.pushButton_15.clicked.connect(MainWindow.close)
        self.pushButton_16.clicked.connect(self.set_graoh)
        self.pushButton_4.clicked.connect(self.start_test_PROOF)
        self.radioButton.clicked.connect(self.click_onRadiobutt)
        self.radioButton_2.clicked.connect(self.click_onRadiobutt)
        self.lineEdit_10.textChanged.connect(self.click_onRadiobutt)
        self.lineEdit_11.textChanged.connect(self.click_onRadiobutt)
        self.comboBox.currentTextChanged.connect(self.onchage_combo)
        self.pushButton_13.clicked.connect(self.show_all_specimens)
        self.pushButton_5.clicked.connect(self.open_email_report)    
        self.pushButton_7.clicked.connect(self.open_pdf)
        self.pushButton_6.clicked.connect(self.open_comment_popup)
        self.pushButton_8.clicked.connect(self.print_file)
        self.tableWidget.doubleClicked.connect(self.delete_cycle)
        self.load_data()
        
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
        with connection:        
                       cursor = connection.cursor()                
                       cursor.execute("UPDATE GLOBAL_VAR SET CURR_UNIT_TYPE = '"+str(self.comboBox_2.currentText())+"'")                                        
        connection.commit();
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT IFNULL(PROOF_MAX_LOAD,0),IFNULL(PROOF_MAX_LENGTH ,0),IFNULL(NEW_TEST_MOTOR_REV_SPEED ,0) FROM GLOBAL_VAR") 
        for x in results:
            if(self.comboBox_2.currentText() =="N/mm"):
                self.lineEdit_10.setText(str(x[0]))
                self.lineEdit_11.setText(str(x[1]))
            else:
                self.lineEdit_10.setText(str(x[0]))
                self.lineEdit_11.setText(str(x[1]))
            self.lineEdit_9_1.setText(str(x[2]))
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_1 as Load_Y_axis,GRAPH_SCALE_CELL_2  as length_x_axis FROM SETTING_MST") 
        for x in results:
            if(self.comboBox_2.currentText() =="N/mm"):
                self.lineEdit_12.setText(str(x[0]))
                self.lineEdit_13.setText(str(x[1]))
            else:
                self.lineEdit_12.setText(str(x[0]))
                self.lineEdit_13.setText(str(x[1]))
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'TEST_MST'")       
        for x in results:           
                 self.label_12.setText(str(x[0]).zfill(3))
                 self.test_id=str(x[0])
                 self.lineEdit_3.setText("Batch_"+str(x[0]).zfill(3))
        connection.close()
        self.onchage_combo()
        self.show_grid_data_PROOF()
        self.sc_blank =PlotCanvas_blank(self)          
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
        
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setDisabled(True)
    
    def onchage_combo(self):                      
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select C_A_AREA,GUAGE_LENGTH_MM,MOTOR_SPEED,PARTY_NAME,THICKNESS,WIDTH,DIAMETER,SHAPE ,IN_DIAMETER_MM,OUTER_DIAMETER_MM,REV_MOTOR_SPEED FROM SPECIMEN_MST WHERE SPECIMEN_NAME='"+self.comboBox.currentText()+"'")                 
        for x in results:
            self.lineEdit_9.setText(str(x[2])) # SPEED
            self.label_51.setText(str(x[3])) # Party Name
            self.label_61.setText(str(x[7]))
            self.lineEdit_9_1.setText(str(x[10]))
        connection.close()
        self.click_onRadiobutt()
        
    def click_onRadiobutt(self):
        if(self.radioButton.isChecked()): ### Elongation 
                self.lineEdit_10.setDisabled(True)
                self.lineEdit_10.setText("99999")
                self.lineEdit_11.setEnabled(True)
                self.label_21.show()
                self.label_21.setText("Start Test for Max Elongation :"+str(self.lineEdit_11.text())+" (mm)")
                self.start_test_by="elongation"
                #self.label_13.setText("Load \n (Kgf)")
#                self.sc_blank =PlotCanvas2_blank(self)          
#                self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        elif(self.radioButton_2.isChecked()):### Load
                self.lineEdit_10.setEnabled(True)
                self.lineEdit_11.setText("99999")
                self.lineEdit_11.setDisabled(True)
                self.label_21.show()
                self.label_21.setText("Start Test for Max Load :"+str(self.lineEdit_10.text())+" (Kgf)")
                self.start_test_by="load"
                #self.label_13.setText("Load \n (Kgf)")
#                self.sc_blank =PlotCanvas_blank(self)          
#                self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        else:
            print("Enable Radio Button Please ......")
        
        

        self.show_grid_data_PROOF()
        
       
            
     
            
    
    def set_graoh(self):
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                       cursor = connection.cursor()                
                       cursor.execute("UPDATE SETTING_MST SET GRAPH_SCALE_CELL_1 = '"+str(self.lineEdit_12.text())+"', GRAPH_SCALE_CELL_2= '"+str(self.lineEdit_13.text())+"' ")                                        
        connection.commit();
        connection.close()        
        self.sc_blank =PlotCanvas_blank(self)          
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        
        
    def start_test_PROOF(self):
        #elf.label_35.setText("")
        
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                       cursor = connection.cursor()                
                       cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_MOTOR_SPEED='"+str(self.lineEdit_9.text())+"',NEW_TEST_MOTOR_REV_SPEED='"+str(self.lineEdit_9_1.text())+"'")                                        
        connection.commit();
        connection.close()
        
        self.validation()
        if(self.goAhead=="Yes"):               
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
        self.label_21.setText("") 
          
        if(self.lineEdit_3.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("Batch ID Should not Empty.")                    
        elif(self.lineEdit_9.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("Test Speed Should not Empty.")               
        elif(self.lineEdit_10.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("Max Load Should not Empty.")
        elif(self.lineEdit_11.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("Max Length Should not Empty.")
        else:
               self.goAhead="Yes"
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
                            cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"',PROOF_TEST_BY='"+str(self.start_test_by)+"',TEST_TIME_SEC='"+str(self.label_67.text())+"',PROOF_MAX_LOAD='"+str(self.lineEdit_10.text())+"',PROOF_MAX_LENGTH='"+str(self.lineEdit_11.text())+"'")
                            cursor.execute("UPDATE TEST_MST SET SPECIMEN_NAME='"+str(self.comboBox.currentText())+"',BATCH_ID='"+str(self.lineEdit_3.text())+"',PARTY_NAME='"+str(self.label_51.text())+"',MOTOR_SPEED='"+str(self.lineEdit_9.text())+"'  WHERE  TEST_ID = '"+str(self.label_12.text())+"'")
                        connection.commit();
                        connection.close()
                        
               else:        
                        ### INSERT 
                        connection = sqlite3.connect("tyr.db")              
                        with connection:        
                          cursor = connection.cursor()                  
                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"',PROOF_TEST_BY='"+str(self.start_test_by)+"',TEST_TIME_SEC='"+str(self.label_67.text())+"',PROOF_MAX_LOAD='"+str(self.lineEdit_10.text())+"',PROOF_MAX_LENGTH='"+str(self.lineEdit_11.text())+"'")
                          cursor.execute("INSERT INTO TEST_MST(SPECIMEN_NAME,BATCH_ID,PARTY_NAME,TEST_TYPE,MOTOR_SPEED) VALUES('"+str(self.comboBox.currentText())+"','"+str(self.lineEdit_3.text())+"','"+str(self.label_51.text())+"','PROOF','"+str(self.lineEdit_9.text())+"')")
                        connection.commit();
                        connection.close()
       
              
    
    def show_load_cell_val(self):
        self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q)))        
        self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p)))   #length
        self.label_22.setText("ElapsedTime(sec) : "+str(self.sc_new.t))
        self.label_22.show()
        if(str(self.sc_new.save_data_flg) =="Yes"):            
                self.reset()
                self.save_graph_data()
                self.sc_new.save_data_flg=""
                self.label_21.show()
                self.label_21.setText("Data Saved Successfully.")
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q)))        
                self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p)))   #length
        
    
    def reset(self):
        if(self.sc_new.timer1.isActive()): 
           self.sc_new.timer1.stop()
           
        if(self.timer3.isActive()): 
           self.timer3.stop() 
        
        #self.sc_blank =PlotCanvas_blank(self) 
        #self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
    
    def save_graph_data(self):         
         if (len(self.sc_new.arr_p) > 1):            
            
            #self.cycle_num=int(str(self.label_67.text()))+1
            
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)):                     
                        cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM_N,Y_NUM_LB) VALUES ('"+str(float(self.sc_new.arr_p[g]))+"','"+str(float(self.sc_new.arr_q[g]))+"','"+str(self.sc_new.arr_p_cm[g])+"','"+str(self.sc_new.arr_p_inch[g])+"','"+str(self.sc_new.arr_q_n[g])+"','"+str(self.sc_new.arr_q_lb[g])+"')")
            connection.commit();
            connection.close()
            
            self.update_status()
            #self.cycle_num=self.cycle_num+1
            connection = sqlite3.connect("tyr.db")              
            with connection:        
                  cursor = connection.cursor()
                  #print("ok1")
                  try:
                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"',PROOF_MAX_LOAD='"+str(self.lineEdit_10.text())+"',PROOF_MAX_LENGTH='"+str(self.lineEdit_11.text())+"',STATUS='"+str(self.status_str)+"',TEST_TIME_SEC='"+str(self.label_67.text())+"'")                          
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM) FROM STG_GRAPH_MST),NEW_TEST_MOTOR_SPEED='"+str(self.lineEdit_9.text())+"',NEW_TEST_MOTOR_REV_SPEED='"+str(self.lineEdit_9_1.text())+"'") 
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_N=(SELECT MAX(Y_NUM_N) FROM STG_GRAPH_MST)") 
                         
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_PEAK_LOAD_MM=(SELECT MAX(X_NUM) FROM STG_GRAPH_MST)")
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_PEAK_LOAD_CM=(SELECT X_NUM_CM FROM STG_GRAPH_MST WHERE Y_NUM=(SELECT STG_PEAK_LOAD_KG FROM GLOBAL_VAR))") 
                          #print("ok2")
                          cursor.execute("INSERT INTO CYCLES_MST(TEST_ID,TEST_METHOD,PEAK_LOAD_KG,E_AT_PEAK_LOAD_MM,LOAD_POINT_1,LOAD_POINT_2,STATUS) SELECT TEST_ID,'FBST',STG_PEAK_LOAD_KG,STG_E_AT_PEAK_LOAD_MM,PROOF_MAX_LOAD,PROOF_MAX_LENGTH,STATUS FROM GLOBAL_VAR")
                          
                          cursor.execute("UPDATE CYCLES_MST SET CYCLE_NUM='"+str(self.cycle_num)+"'  WHERE GRAPH_ID IS NULL")
                          cursor.execute("UPDATE CYCLES_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")                          
                          cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM,X_NUM_CM,Y_NUM_N) SELECT X_NUM,Y_NUM,X_NUM_CM,Y_NUM_N FROM STG_GRAPH_MST")                  
                          cursor.execute("UPDATE GRAPH_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL") 
                          cursor.execute("UPDATE TEST_MST SET STATUS='LOADED GRAPH'  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")                  
                          cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_X_LENGTH=(SELECT GRAPH_SCALE_CELL_2 FROM SETTING_MST),GRAPH_SCAL_Y_LOAD=(SELECT GRAPH_SCALE_CELL_1 FROM SETTING_MST)  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                    
                  
                  except Exception as e:
                          print("SQL Error:"+str(e))
                          connection.commit();
           
            connection.commit();
            connection.close()            
            print("Data Saved Ok in STG_GRAPH_MST")           
            self.show_grid_data_PROOF()
    
    def update_status(self):
        #self.start_test_by="load"  #### This status is "load" Or "elongation"
        self.status_str=""
        self.max_load_proof=str(self.lineEdit_10.text())
        self.max_elongation_proof=str(self.lineEdit_11.text())
        if(self.start_test_by=="load"):
            connection = sqlite3.connect("tyr.db")         
            results=connection.execute("SELECT IFNULL(MAX(Y_NUM),0) FROM STG_GRAPH_MST")
            for x in results:
                if(float(x[0]) > int(self.max_load_proof)):
                         print("PASS for Max Load :"+str(self.max_load_proof))
                         self.status_str="PASS for Max Load :"+str(self.max_load_proof)
                         
                elif(float(x[0]) == int(self.max_load_proof)):
                         print("PASS for Max Load :"+str(self.max_load_proof))
                         self.status_str="PASS for Max Load :"+str(self.max_load_proof)
                else:
                         print("FAIL for Max Load :"+str(self.max_load_proof))
                         self.status_str="FAIL for Max Load :"+str(self.max_load_proof)
                         
            connection.close()           
        elif(self.start_test_by=="elongation"):
            connection = sqlite3.connect("tyr.db")         
            results=connection.execute("SELECT IFNULL(MAX(X_NUM),0) FROM STG_GRAPH_MST")
            for x in results:
                if(float(x[0]) > int(self.max_elongation_proof)):
                         print("PASS")
                         self.status_str="PASS for Max Elong. :"+str(self.max_elongation_proof)
                elif(float(x[0]) == int(self.max_elongation_proof)):
                         print("PASS")
                         self.status_str="PASS for Max Elong. :"+str(self.max_elongation_proof)
                else:
                         print("FAIL")
                         self.status_str="FAIL for Max Elong. :"+str(self.max_elongation_proof)
            connection.close()            
        else:
            print("Invalid Status.")
            
        
        
    
    def show_grid_data_PROOF(self):
        self.x_unit='(mm)'
        self.y_unit='(Kgf)'
        self.unit_type = "Kgf/mm"
        #print("inside tear list.....")
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        if(self.start_test_by=="load"):
                self.tableWidget.setHorizontalHeaderLabels(['Spec.No.','Max.Load '+str(self.y_unit),'Elongation(mm)','Status','REC.NO '])  
        else:
                self.tableWidget.setHorizontalHeaderLabels(['Spec.No.','Max.Load '+str(self.y_unit),'Elongation(mm)','Status','REC.NO '])
                
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 170)
        self.tableWidget.setColumnWidth(2, 170)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 100)
     
        
        self.unit_type=self.comboBox_2.currentText()
        print(" Grid data :"+str(self.unit_type))
        connection = sqlite3.connect("tyr.db")
        if(self.unit_type=="N/mm"): 
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_PEAK_LOAD_MM),STATUS, CYCLE_ID FROM CYCLES_MST WHERE TEST_ID ='"+str(int(self.label_12.text()))+"' order by CYCLE_NUM Asc")
        elif(self.unit_type == "Kgf/mm"):
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_PEAK_LOAD_MM),STATUS, CYCLE_ID FROM CYCLES_MST WHERE TEST_ID ='"+str(int(self.label_12.text()))+"' order by CYCLE_NUM Asc")
        else:
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_PEAK_LOAD_MM),STATUS, CYCLE_ID FROM CYCLES_MST WHERE TEST_ID ='"+str(int(self.label_12.text()))+"' order by CYCLE_NUM Asc")
        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()
        self.calculations()
            
    def calculations(self):        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select count(cycle_id),ifnull(max(cycle_num),0)+1 from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
        for x in results:
                    #self.label_67.setText(str(x[0]))                    
                    self.cycle_num=int(x[1])
                    print("self.cycle_num :"+str(self.cycle_num))
        connection.close()
        
        self.unit_type=self.comboBox_2.currentText()
        connection = sqlite3.connect("tyr.db")
        if(self.unit_type == "Kgf/mm"):
               
               results=connection.execute(" select  ifnull(round(avg(PEAK_LOAD_KG),2),0), ifnull(round(avg(E_AT_PEAK_LOAD_MM),2),0),ifnull(round(min(PEAK_LOAD_KG),2),0), ifnull(round(min(E_AT_PEAK_LOAD_MM),2),0),ifnull(round(max(PEAK_LOAD_KG),2),0), ifnull(round(max(E_AT_PEAK_LOAD_MM),2),0) from CYCLES_MST WHERE TEST_ID ='"+str(int(self.label_12.text()))+"' ")       
        else:
               results=connection.execute(" select  round(avg(PEAK_LOAD_KG),2), round(avg(E_AT_PEAK_LOAD_MM),2),round(min(PEAK_LOAD_KG),2), round(min(E_AT_PEAK_LOAD_MM),2),round(max(PEAK_LOAD_KG),2), round(max(E_AT_PEAK_LOAD_MM),2) from CYCLES_MST WHERE TEST_ID ='"+str(int(self.label_12.text()))+"' ")       
      
        for x in results:
                    self.label_27.setText(str(x[0]))  
                    self.label_31.setText(str(x[1]))
                    
                    self.label_28.setText(str(x[2]))  
                    self.label_32.setText(str(x[3]))
                    
                    self.label_29.setText(str(x[4]))  
                    self.label_33.setText(str(x[5]))
                                   
        connection.close()
        print("Calculations Updated !!!!!")
        
        
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)      
                
    def show_all_specimens(self): 
        self.sc_data =PlotCanvas(self,width=5, height=4, dpi=100)    
        self.gridLayout.addWidget(self.sc_data, 1, 0, 1, 1)
        
        
    def print_file(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POP_TEST_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def create_pdf_PROOF(self):
        self.remark=""
        self.unit_typex=self.comboBox_2.currentText()
        self.unit_typex == "Kgf/mm"        
        
        if(self.start_test_by=="load"):
            if(self.unit_typex == "Kgf/mm"):            
                data2= [['Spec.No', 'Max.Load(Kgf)', 'Test Time (sec)', 'Status']]
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT CYCLE_NUM,printf(\"%.4f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM),STATUS FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'AVG',printf(\"%.4f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg(A.E_AT_PEAK_LOAD_MM)),'' FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MIN',printf(\"%.4f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\", min(A.E_AT_PEAK_LOAD_MM)),'' FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MAX',printf(\"%.4f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max(A.E_AT_PEAK_LOAD_MM)),'' FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
                for x in results:
                        data2.append(x)
                connection.close()
        else:
                data2= [['Spec.No', 'Max.Elongation(mm)', 'Test Time (sec)', 'Status']]
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT CYCLE_NUM,printf(\"%.4f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM),STATUS FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'AVG',printf(\"%.4f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\", avg(A.E_AT_PEAK_LOAD_MM)),'' FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MIN',printf(\"%.4f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\", min(A.E_AT_PEAK_LOAD_MM)),'' FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
                for x in results:
                        data2.append(x)
                connection.close()
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT 'MAX',printf(\"%.4f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\", max(A.E_AT_PEAK_LOAD_MM)),'' FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
                for x in results:
                        data2.append(x)
                connection.close()
        
        y=300
        Elements=[]
        summary_data=[]
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,A.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime') ,A.COMMENTS FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID ='"+str(self.label_12.text())+"'")
        
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Specmen Shape:",str(x[9])],["Test Type:",str(x[3]),"Specmen Specs:",str(x[8])],["Party Name :",str(x[7]),"Test Speed (mm/min) :",str(x[5])],["Guage Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", "Stech engineers testing machine","",""]]
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
        
        
        if(str(self.remark) == ""):
                comments = Paragraph("    Remark : ______________________________________________________________________________", styles["Normal"])
        else:
                comments = Paragraph("    Remark : "+str(self.remark), styles["Normal"])
                
        footer_2= Paragraph("     Authorised: __________________________________.            Signed By : _________________.", styles["Normal"])
        
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
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,blank,blank,blank,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/test_report.pdf', rightMargin=10,
                                leftMargin=20,
                                topMargin=20,
                                bottomMargin=10,)
        doc.build(Elements)
        
    def open_pdf(self):
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=100) 
        self.create_pdf_PROOF() 
        
        os.system("xpdf ./reports/test_report.pdf")
        os.system("cp ./reports/test_report.pdf ./reports/Report_of_test_"+str(self.test_id)+".pdf")
        
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
    
    def delete_cycle(self):
        i = self.tableWidget.rowCount()   
        if(i>0):
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
                                        
                        connection.commit();
                        connection.close()
                        self.show_grid_data_PROOF()
                        
            else:
                    pass  

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
        self.proof_test_by=""
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
        self.unit_type=""
        self.color=['b','r','g','y','k','c','m','b']
        #ax.set_title('Test Id=32         Samples=3       BreakLoad(Kg)=110        Length(mm)=3')

        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT PROOF_TEST_BY FROM GLOBAL_VAR") 
        for x in results:
            self.proof_test_by=str(x[0])
            if(self.proof_test_by=="load"):
                     ax.set_xlabel('Time (sec)')
                     ax.set_ylabel('Load kgf)')                
            else:
                     ax.set_xlabel('Time (sec)')
                     ax.set_ylabel('Elongation mm)')  
        connection.close()
        
        self.unit_type="Kgf/mm"
        ### Univarsal change for  Graphs #####################
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
            if(self.unit_type == "N/mm"):
                 ax.set_xlim(0,int(x[0]))
                 ax.set_ylim(0,int(x[1])*9.81)
                 
            if(self.unit_type == "Kgf/mm"):
                 ax.set_xlim(0,int(x[0]))
                 ax.set_ylim(0,int(x[1]))
                 
            else:     
                 ax.set_xlim(0,int(x[0]))
                 ax.set_ylim(0,int(x[1])*9.81)
                 
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
             self.graph_ids.append(x[0])             
        connection.close()
        
        
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
            print(" Unit Type :"+str(self.unit_type))
            connection = sqlite3.connect("tyr.db")
            if(self.unit_type == "N/mm"):
                results=connection.execute("SELECT X_NUM,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            elif(self.unit_type == "Kgf/mm"):
                results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            else:                
                results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            for k in results:        
                    self.x_num.append(k[0])
                    self.y_num.append(k[1])
            connection.close()
            if(g < 8 ):
                    ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
            
        print("self.test_type:"+str(self.test_type))
        
        ax.legend()        
        self.draw()
        self.figure.savefig('last_graph.png',dpi=100)


class PlotCanvas_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=5, height=4, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="FBST"
        
        
       
        
        
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
        
        
        
        
        self.arr_p=[0.0]
        self.arr_p_cm=[0.0]
        self.arr_p_inch=[0.0]
        
        
        self.arr_q=[0.0]
        self.arr_q_n=[0.0]
        self.arr_q_lb=[0.0]
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
        self.unit_type =""
        self.proof_test_by=""
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
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,PROOF_TEST_BY,PROOF_MAX_LOAD,PROOF_MAX_LENGTH,TEST_TIME_SEC from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=int(x[0])             
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
             if(self.proof_test_by=="load"):
                     self.axes.set_xlabel('Elongation (mm)')
                     self.axes.set_ylabel('Load (kgf)')                
             else:
                     self.axes.set_xlabel('Elongation (mm)')
                     self.axes.set_ylabel('Load (kgf)')
             try:
                 self.proof_max_load=int(str(x[7]))
             except ValueError as e:
                        try:
                            self.width=float(str(x[7]))
                        except ValueError as e:
                                self.proof_max_load=99999
                 
             self.proof_max_length=int(str(x[8]))
             self.test_time_sec=int(str(x[9]))
             
        connection.close()
        print(" xxx     gfgf self.unit_type:"+str(self.unit_type))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:
             if(self.unit_type == "Kgf/mm"):
                     self.axes.set_xlim(0,int(x[0]))
                     self.axes.set_ylim(0,int(x[1]))
                     #self.flexural_max_load=int(x[1])/9.81
                     self.xlim=int(x[0])
                     self.ylim=int(x[1])
                     
             elif(self.unit_type == "N/mm"):
                     self.axes.set_xlim(0,int(x[0]))
                     self.axes.set_ylim(0,int(x[1])*9.81)
                     #self.flexural_max_load=int(x[1])/9.81
                     self.xlim=int(x[0])
                     self.ylim=int(x[1])* 9.81
                              
             else:
                     self.axes.set_xlim(0,int(x[0]))
                     self.axes.set_ylim(0,int(x[1]))
                     #self.flexural_max_load=int(x[1])
                     self.xlim=int(x[0])
                     self.ylim=int(x[1])
                      
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
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
                 print("Compress")                  
            elif(self.test_type=="Flexural"):
                print("Flexural")    
            elif(self.test_type=="COF"):
                print("COF")
            else:
                print("len(self.ybuff) :"+str(len(self.ybuff)))
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                        #self.ser.write(b'*S2T000.0 000.0\r')
                        #print("Start Command :*S2P"+str(self.proof_max_load)+" "+str(self.proof_max_length)+" "+str(self.test_time_sec)+"\r")
                        self.command_str="*S2P%05d"%self.proof_max_load+" %05d"%self.proof_max_length+" %05d"%self.test_time_sec+"\r"
                        print("Proof Start Command :"+str(self.command_str))
                        b = bytes(self.command_str, 'utf-8')
                        self.ser.write(b)
                        
                    else:
                        #self.ser.write(b'*S1P000.0 000.0\r')
                        #print("Start Command:*S1T000.0 000.0\r")
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
        if(self.IO_error_flg==0):
            '''
            self.ser.flush()
            self.ser.write(b'*D\r')
            self.line = self.ser.readline()
            print("With Readline Timer Job o/p:"+str(self.line))
            #print("")
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
                
                self.t=abs(float(self.buff[3]))
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
                
#                if(self.unit_type == "N/mm"):    
#                        self.q=float(self.q)*9.81
#                elif(self.unit_type == "Kgf/cm"):
#                        self.p=float(self.p)/10
#                else:
#                        self.p=float(self.p)
#                        self.q=float(self.q)


                self.p=float(self.p)
                self.p_cm=float(self.p)/10
                self.arr_p_cm.append(float(self.p_cm))
                
                self.p_inch=float(self.p)*0.0393701
                self.arr_p_inch.append(float(self.p_inch))
                
                self.q=float(self.q)
                self.q_n=float(self.q)*9.81
                self.arr_q_n.append(float(self.q_n))
                
                self.q_lb=float(self.q)*2.20462
                self.arr_q_lb.append(float(self.q_lb))
                
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
        if(self.unit_type == "Kgf/mm"):
            self.line_cnt.set_data(self.arr_p,self.arr_q)
            return [self.line_cnt]
            #return self.line_cnt,
        elif(self.unit_type == "N/mm"):
            self.line_cnt.set_data(self.arr_p,self.arr_q_n)
            return [self.line_cnt]
            #return self.line_cnt,
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
        results=connection.execute("SELECT IFNULL(NEW_TEST_MOTOR_SPEED,0) , IFNULL(NEW_TEST_MOTOR_REV_SPEED,0)  from GLOBAL_VAR") 
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
                
            print("int part :%d"%v)
            print("decial part:%.2f"%v)
            #v=v*100
            instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) # port name, slave address (in decimal)
            instrument.serial.timeout = 1
            instrument.serial.baudrate = 9600
            instrument.write_register(4096,v,0) ###self.input_speed_val RPM
            instrument.write_register(4097,0,0) ###self.input_speed_val RPM
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
            instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) # port name, slave address (in decimal)
            instrument.serial.timeout = 1
            instrument.serial.baudrate = 9600
            instrument.write_register(4098,v,0) ###self.input_speed_val RPM
            instrument.write_register(4099,0,0) ###self.input_speed_val RPM
            print(" write2 :"+str(v))
        except IOError as e:
            print("Reverse-Write Modbus IO Error -Motor start : "+str(e))
        
        print("Reverse speed : "+str(v))
        
                
            
            
               

class PlotCanvas_blank(FigureCanvas):
    def __init__(self, parent=None, width=1, height=0.1, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.unit_type=""
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot_blank()        
        
    def plot_blank(self):               
        
#        connection = sqlite3.connect("tyr.db")
#        connection.commit();
#        with connection:        
#                cursor = connection.cursor()                            
#                cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
#        connection.commit();
#        connection.close()
        
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
        results=connection.execute("SELECT CURR_UNIT_TYPE from GLOBAL_VAR") 
        for x in results:
                self.unit_type=str(x[0]) 
        connection.close() 
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:             
                 ax.set_xlim(0,int(x[0]))
                 ax.set_ylim(0,int(x[1]))                               
                 ax.set_xlabel('Elongation (mm)')
                 ax.set_ylabel('Load (Kgf) ')             
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])
        
        ax.plot(self.x,self.y,'b')
        self.draw() 


      
        

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ty_29_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
