


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
        


class TY_26_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 709))
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
        self.pushButton_4.setGeometry(QtCore.QRect(650, 540, 81, 41))
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
        self.pushButton_13.setGeometry(QtCore.QRect(650, 600, 81, 41))
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
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 111, 31))
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
        self.tableWidget.setGeometry(QtCore.QRect(760, 260, 561, 201))
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
        self.label_9.setGeometry(QtCore.QRect(330, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_5)
        self.lineEdit_5.setValidator(input_validator)
        self.lineEdit_5.setGeometry(QtCore.QRect(860, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 121, 31))
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
        self.label_12.setGeometry(QtCore.QRect(150, 10, 41, 31))
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
        self.lcdNumber.setGeometry(QtCore.QRect(650, 320, 81, 61))
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("value", 100.0)
        self.lcdNumber.setProperty("intValue", 100)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(650, 280, 71, 31))
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
        self.label_23.setGeometry(QtCore.QRect(1070, 480, 111, 31))
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
        self.label_24.setGeometry(QtCore.QRect(1210, 480, 111, 31))
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
        self.label_25.setGeometry(QtCore.QRect(940, 480, 101, 31))
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
        self.label_26.setGeometry(QtCore.QRect(830, 480, 81, 31))
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
        self.label_33.setGeometry(QtCore.QRect(960, 590, 41, 41))
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
        self.label_34.setGeometry(QtCore.QRect(960, 630, 41, 41))
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
        self.label_35.setGeometry(QtCore.QRect(960, 670, 41, 41))
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
        self.label_36.setGeometry(QtCore.QRect(850, 670, 41, 41))
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
        self.label_37.setGeometry(QtCore.QRect(1110, 510, 41, 41))
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
        self.label_38.setGeometry(QtCore.QRect(1110, 550, 41, 41))
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
        self.label_39.setGeometry(QtCore.QRect(1110, 590, 41, 41))
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
        self.label_40.setGeometry(QtCore.QRect(1110, 630, 41, 41))
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
        self.label_41.setGeometry(QtCore.QRect(1110, 670, 41, 41))
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
        self.label_42.setGeometry(QtCore.QRect(1220, 510, 41, 41))
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
        self.label_43.setGeometry(QtCore.QRect(1220, 550, 41, 41))
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
        self.label_44.setGeometry(QtCore.QRect(1220, 590, 41, 41))
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
        self.label_45.setGeometry(QtCore.QRect(1220, 630, 41, 41))
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
        self.label_46.setGeometry(QtCore.QRect(1220, 670, 41, 41))
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
        self.comboBox.setGeometry(QtCore.QRect(150, 50, 161, 31))
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
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(330, 150, 81, 31))
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
        self.lineEdit_3.setGeometry(QtCore.QRect(450, 150, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)        
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.label_48_1 = QtWidgets.QLabel(self.frame)
        self.label_48_1.setGeometry(QtCore.QRect(330, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_48_1.setFont(font)
        self.label_48_1.setText("Load1 (N):")
        self.label_48_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_48_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48_1.setObjectName("label_48_1")
        
        self.lineEdit_3_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_1.setGeometry(QtCore.QRect(450, 200, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3_1.setFont(font)
        self.lineEdit_3_1.setText("1500")
        self.lineEdit_3_1.setObjectName("lineEdit_3_1")
        
        
        self.label_48_2 = QtWidgets.QLabel(self.frame)
        self.label_48_2.setGeometry(QtCore.QRect(530, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_48_2.setFont(font)
        self.label_48_2.setText("Load2 (N):")
        self.label_48_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_48_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48_2.setObjectName("label_48_2")
        
        self.lineEdit_3_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3_2.setGeometry(QtCore.QRect(630, 200, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3_2.setFont(font)
        self.lineEdit_3_2.setText("5800")
        self.lineEdit_3_2.setObjectName("lineEdit_3_2")
        
        
        
        
        
        
        self.label_49 = QtWidgets.QLabel(self.frame)
        self.label_49.setGeometry(QtCore.QRect(430, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_49.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(1040, 60, 81, 31))
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
        self.pushButton_6.setGeometry(QtCore.QRect(1040, 110, 81, 31))
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
        self.pushButton_7.setGeometry(QtCore.QRect(1170, 60, 121, 31))
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
        self.pushButton_8.setGeometry(QtCore.QRect(1170, 110, 121, 31))
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
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(330, 50, 51, 31))
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
        self.comboBox_2.setGeometry(QtCore.QRect(400, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        
        self.label_51 = QtWidgets.QLabel(self.frame)
        self.label_51.setGeometry(QtCore.QRect(450, 100, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.frame)
        self.label_52.setGeometry(QtCore.QRect(10, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_52.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_52.setObjectName("label_52")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_4)
        self.lineEdit_4.setValidator(input_validator)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_53 = QtWidgets.QLabel(self.frame)
        self.label_53.setGeometry(QtCore.QRect(240, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_53.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.frame)
        self.label_54.setGeometry(QtCore.QRect(740, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_54.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.frame)
        self.label_55.setGeometry(QtCore.QRect(740, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_55.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.frame)
        self.label_56.setGeometry(QtCore.QRect(950, 60, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_56.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_56.setObjectName("label_56")
        self.label_58 = QtWidgets.QLabel(self.frame)
        self.label_58.setGeometry(QtCore.QRect(10, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_58.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_58.setObjectName("label_58")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_7)
        self.lineEdit_7.setValidator(input_validator)
        self.lineEdit_7.setGeometry(QtCore.QRect(150, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_59 = QtWidgets.QLabel(self.frame)
        self.label_59.setGeometry(QtCore.QRect(240, 150, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_59.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.frame)
        self.label_60.setGeometry(QtCore.QRect(10, 200, 111, 31))
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
        self.lineEdit_9.setGeometry(QtCore.QRect(150, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_63 = QtWidgets.QLabel(self.frame)
        self.label_63.setGeometry(QtCore.QRect(240, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_63.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_63.setObjectName("label_63")
        self.line_14 = QtWidgets.QFrame(self.frame)
        self.line_14.setGeometry(QtCore.QRect(1010, 0, 20, 241))
        self.line_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_14.setLineWidth(3)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setObjectName("line_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(1170, 160, 121, 31))
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
        self.pushButton_9.setGeometry(QtCore.QRect(1040, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(650, 400, 81, 41))
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
        self.lcdNumber_2.setGeometry(QtCore.QRect(650, 450, 81, 61))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setProperty("value", 100.0)
        self.lcdNumber_2.setProperty("intValue", 100)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.line_15 = QtWidgets.QFrame(self.frame)
        self.line_15.setGeometry(QtCore.QRect(720, 0, 20, 241))
        self.line_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_15.setLineWidth(3)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setObjectName("line_15")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(740, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_61 = QtWidgets.QLabel(self.frame)
        self.label_61.setGeometry(QtCore.QRect(820, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_61.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_61.setObjectName("label_61")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_8)
        self.lineEdit_8.setValidator(input_validator)
        self.lineEdit_8.setGeometry(QtCore.QRect(860, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_62 = QtWidgets.QLabel(self.frame)
        self.label_62.setGeometry(QtCore.QRect(950, 110, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_62.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_62.setObjectName("label_62")
        self.line_16 = QtWidgets.QFrame(self.frame)
        self.line_16.setGeometry(QtCore.QRect(750, 150, 251, 21))
        self.line_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_16.setLineWidth(3)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setObjectName("line_16")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(750, 170, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.label_64 = QtWidgets.QLabel(self.frame)
        self.label_64.setGeometry(QtCore.QRect(860, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_64.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.frame)
        self.label_65.setGeometry(QtCore.QRect(950, 170, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_65.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.frame)
        self.label_66.setGeometry(QtCore.QRect(500, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_66.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.frame)
        self.label_67.setGeometry(QtCore.QRect(670, 50, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_67.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_67.setObjectName("label_67")
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


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00"))
        self.label_20.setText(_translate("MainWindow", datetime.datetime.now().strftime("%B  %d , %Y %I:%M ")+""))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.pushButton_13.setText(_translate("MainWindow", "All"))
        self.label_21.setText(_translate("MainWindow", "Compleated Successfully. "))
        self.label_21.hide()
        self.label_6.setText(_translate("MainWindow", "Spec.Name :"))
        self.tableWidget.setSortingEnabled(True)
        
        self.tableWidget.setHorizontalHeaderLabels(['Spec.No.','Break Load (N)','E@Break (mm)','E@Load_Point1 (mm)','E@Load_Point2 (mm)','REC.NO '])
        self.tableWidget.resizeColumnsToContents()
      
        '''       
        '''
        #self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(_translate("MainWindow", "Party Name :"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "001"))
        self.label_13.setText(_translate("MainWindow", "LOAD (N) :"))
        self.label_22.setText(_translate("MainWindow", "Running......"))
        self.label_22.hide()
        self.label_15.setText(_translate("MainWindow", "Max :"))
        self.label_16.setText(_translate("MainWindow", "Min :"))
        self.label_17.setText(_translate("MainWindow", "Avg :"))
        self.label_18.setText(_translate("MainWindow", "Std. :"))
        self.label_19.setText(_translate("MainWindow", "Var. :"))
        self.label_23.setText(_translate("MainWindow", "%E@"+str(self.lineEdit_3_1.text())+" "+str(self.y_unit)))
        self.label_24.setText(_translate("MainWindow", "%E@"+str(self.lineEdit_3_2.text())+" "+str(self.y_unit)))
        self.label_25.setText(_translate("MainWindow", "E@Break(mm)"))
        self.label_26.setText(_translate("MainWindow", "BrkLoad(N)"))
        self.label_27.setText(_translate("MainWindow", "111.00"))
        self.label_28.setText(_translate("MainWindow", "222.00"))
        self.label_29.setText(_translate("MainWindow", "333.00"))
        self.label_30.setText(_translate("MainWindow", "0"))
        self.label_31.setText(_translate("MainWindow", "666.99"))
        self.label_32.setText(_translate("MainWindow", "777.00"))
        self.label_33.setText(_translate("MainWindow", "888.00"))
        self.label_34.setText(_translate("MainWindow", "0"))
        self.label_35.setText(_translate("MainWindow", "0"))
        self.label_36.setText(_translate("MainWindow", "0"))
        self.label_37.setText(_translate("MainWindow", "B11.00"))
        self.label_38.setText(_translate("MainWindow", "C22.00"))
        self.label_39.setText(_translate("MainWindow", "D33.00"))
        self.label_40.setText(_translate("MainWindow", "0"))
        self.label_41.setText(_translate("MainWindow", "0"))
        self.label_42.setText(_translate("MainWindow", "G34.00"))
        self.label_43.setText(_translate("MainWindow", "F56.00"))
        self.label_44.setText(_translate("MainWindow", "Y66.89"))
        self.label_45.setText(_translate("MainWindow", "0"))
        self.label_46.setText(_translate("MainWindow", "0"))
        self.comboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(4, _translate("MainWindow", "New Item"))
        self.label_48.setText(_translate("MainWindow", "BatchID:"))
        self.label_49.setText(_translate("MainWindow", "FOUNDATION BREAKING TEST"))
        self.pushButton_5.setText(_translate("MainWindow", "Email"))
        self.pushButton_6.setText(_translate("MainWindow", "Remark"))
        self.pushButton_7.setText(_translate("MainWindow", "Report View"))
        self.pushButton_8.setText(_translate("MainWindow", "Report Print"))
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        self.label_50.setText(_translate("MainWindow", "Stat."))
        self.label_7.setText(_translate("MainWindow", "Unit :"))
        self.comboBox_2.addItem("")
        #self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, _translate("MainWindow", "N/mm"))
        #self.comboBox_2.setItemText(1, _translate("MainWindow", "Kgf/cm"))
        #self.comboBox_2.setItemText(2, _translate("MainWindow", "Lbs/inch"))
        #self.comboBox_2.setItemText(3, _translate("MainWindow", "MPa/mm"))
        self.label_51.setText(_translate("MainWindow", "MRF"))
        self.label_52.setText(_translate("MainWindow", "CS Area :"))
        self.label_53.setText(_translate("MainWindow", "(mm2)"))
        self.label_54.setText(_translate("MainWindow", "Thickness :"))
        self.label_55.setText(_translate("MainWindow", "Width :"))
        self.label_56.setText(_translate("MainWindow", "(mm)"))
        self.label_58.setText(_translate("MainWindow", "Guage Length :"))
        self.label_59.setText(_translate("MainWindow", "(mm)"))
        self.label_60.setText(_translate("MainWindow", "Test Speed :"))
        self.label_63.setText(_translate("MainWindow", "(mm / min)"))
        self.pushButton_15.setText(_translate("MainWindow", "Return"))
        self.pushButton_9.setText(_translate("MainWindow", "Save"))
        self.label_14.setText(_translate("MainWindow", "Elongation : \n"
" (mm) "))
        self.label_10.setText(_translate("MainWindow", "Shape:"))
        self.label_61.setText(_translate("MainWindow", "Rectangle"))
        self.label_62.setText(_translate("MainWindow", "(mm)"))
        self.label_47.setText(_translate("MainWindow", "CS Area:"))
        self.label_64.setText(_translate("MainWindow", "100"))
        self.label_65.setText(_translate("MainWindow", "(mm2)"))
        self.label_66.setText(_translate("MainWindow", "Total Specemens :"))
        self.label_67.setText(_translate("MainWindow", "00"))
        
        
        
        
        self.pushButton_15.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(self.start_test_FBST)
        self.comboBox.currentTextChanged.connect(self.onchage_combo)
        self.comboBox_2.currentTextChanged.connect(self.on_change_unit_type)
        self.pushButton_13.clicked.connect(self.show_all_specimens)
        
        self.pushButton_8.clicked.connect(self.print_file)
        self.pushButton_5.clicked.connect(self.open_email_report)
        self.pushButton_9.clicked.connect(self.validation)
        self.pushButton_7.clicked.connect(self.open_pdf)
        self.pushButton_6.clicked.connect(self.open_comment_popup)
        self.lineEdit_5.textChanged.connect(self.cs_area_calculation)
        self.lineEdit_8.textChanged.connect(self.cs_area_calculation)
        self.tableWidget.doubleClicked.connect(self.delete_cycle)
        
        
        self.load_data()
        self.delete_all_records()
    
    
            
    
    def load_data(self):
        self.on_change_unit_type()
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
        results=connection.execute("SELECT LOAD_POINT_1,LOAD_POINT_2 FROM GLOBAL_VAR") 
        for x in results:
            if(self.comboBox_2.currentText() =="N/mm"):
                self.lineEdit_3_1.setText(str(x[0]))
                self.lineEdit_3_2.setText(str(x[1]))
            else:
                self.lineEdit_3_1.setText(str(x[0])/9.81)
                self.lineEdit_3_2.setText(str(x[1])/9.81)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'TEST_MST'")       
        for x in results:           
                 self.label_12.setText(str(x[0]).zfill(3))
                 self.test_id=str(x[0])
                 self.lineEdit_3.setText("Batch_"+str(x[0]).zfill(3))
        connection.close()
        
        self.onchage_combo()
        self.show_grid_data_FBST()
        
        
    def on_change_unit_type(self):
        if(self.comboBox_2.currentText() =="N/mm"):
            self.x_unit='(mm)'
            self.y_unit='(N)'
            self.area_unit=('mm2')            
        elif(self.comboBox_2.currentText() =="Kgf/cm"):
            self.x_unit='(cm)'
            self.y_unit='(Kgf)'
            self.area_unit=('cm2')
            
        else:
            self.x_unit='mm'
            self.y_unit='N'
            self.area_unit=('cm2')
        
        self.label_23.setText("%E@"+str(self.lineEdit_3_1.text())+" "+str(self.y_unit))
        self.label_24.setText("%E@"+str(self.lineEdit_3_2.text())+" "+str(self.y_unit))
        self.label_25.setText("E@Break"+str(self.x_unit))
        self.label_26.setText("BrkLoad"+str(self.y_unit))
        self.label_48_1.setText("Load1"+str(self.y_unit))
        self.label_48_2.setText("Load2"+str(self.y_unit))
        self.label_53.setText(str(self.area_unit))
        self.label_56.setText(str(self.x_unit))
        self.label_59.setText(str(self.x_unit))
        
        self.label_62.setText(str(self.x_unit))
       
        self.label_65.setText(str(self.area_unit))
        self.tableWidget.setHorizontalHeaderLabels(['Spec.No.','Break Load '+str(self.y_unit),'E@Break '+str(self.x_unit),'%E@'+str(self.lineEdit_3_1.text())+' '+str(self.y_unit),'%E@'+str(self.lineEdit_3_2.text())+' '+str(self.y_unit),'REC.NO '])  
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LOAD_POINT_1,LOAD_POINT_2 FROM GLOBAL_VAR") 
        for x in results:
            if(self.comboBox_2.currentText() =="N/mm"):
                self.lineEdit_3_1.setText(str(x[0]))
                self.lineEdit_3_2.setText(str(x[1]))
            else:
                d=float(x[0])/9.81
                self.lineEdit_3_1.setText(str(round(d,2)))
                d2=float(x[1])/9.81
                self.lineEdit_3_2.setText(str(round(d2,2)))
        connection.close()
    
    
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                       cursor = connection.cursor()                
                       cursor.execute("UPDATE GLOBAL_VAR SET CURR_UNIT_TYPE = '"+str(self.comboBox_2.currentText())+"'")
                                        
        connection.commit();
        connection.close()
        self.onchage_combo()
        self.sc_blank =PlotCanvas_blank(self)          
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
        
        
        
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
                        self.show_grid_data_FBST()
                        
            else:
                    pass
            
    
    def cs_area_calculation(self):
        self.shape=""
        self.thickness=""
        self.width=""
        self.diameter=""
        self.cs_area=""
        self.out_dia=""
        self.inn_dia=""
        
        self.shape=self.label_61.text()
        if(self.shape== "Rectangle"):
            if(self.lineEdit_5.text() != ""):
                try:
                        self.thickness=int(self.lineEdit_5.text())
                except ValueError as e:
                        try:
                                self.thickness=float(self.lineEdit_5.text())
                        except ValueError as e:
                                self.label_64.setText("0.00") 
                try:
                        self.width=int(self.lineEdit_8.text())
                except ValueError as e:
                        try:
                            self.width=float(self.lineEdit_8.text())
                        except ValueError as e:
                                self.label_64.setText("0.00")
                                
                try:
                        self.label_64.setText(str(float(self.thickness * self.width)))
                except ValueError as e:
                    #self.lineEdit_3.setText("0.00")
                    print("Caluculation error1");
                    self.label_64.setText(str("0"))
                except TypeError as e:
                    print("Caluculation error2");
                    self.label_64.setText(str("0"))
                except:
                    print("Caluculation error3");
                    self.label_64.setText(str("0"))
            else:
                    self.label_64.setText(str("0"))
        elif(self.shape== "Cylindrical"):
                try:
                    self.diameter=int(self.lineEdit_5.text())
                except ValueError as e:
                        try:
                            self.diameter=float(self.lineEdit_5.text())
                        except ValueError as e:
                            self.label_64.setText("0.00")
                
                try:
                            self.label_64.setText(str(round(float((self.diameter * self.diameter * 3.14)/4),2)))
                except ValueError as e:
                            #self.lineEdit_3.setText("0.00")
                            print("Caluculation error4");
                            self.label_64.setText(str("0"))
                except TypeError as e:
                            print("Caluculation error5");
                            self.label_64.setText(str("0"))
                except:
                            print("Caluculation error6");
                            self.label_64.setText(str("0"))                           
        
        elif(self.shape== "Pipe"):
                try:
                        self.inn_dia=int(self.lineEdit_5.text())
                except ValueError as e:
                        try:
                                self.inn_dia=float(self.lineEdit_5.text())
                        except ValueError as e:
                                self.label_64.setText("0.00") 
                try:
                        self.out_dia=int(self.lineEdit_8.text())
                except ValueError as e:
                        try:
                            self.out_dia=float(self.lineEdit_8.text())
                        except ValueError as e:
                                self.label_64.setText("0.00")
                                
                try:
                        self.cs_area=((float(self.out_dia)*float(self.out_dia)*3.14)/4)-((float(self.inn_dia)*float(self.inn_dia)*3.14)/4) 
                        self.label_64.setText(str(float(self.cs_area)))
                except ValueError as e:
                    #self.lineEdit_3.setText("0.00")
                    print("Caluculation error7");
                    self.label_64.setText(str("0"))
                except TypeError as e:
                    print("Caluculation error8");
                    self.label_64.setText(str("0"))
                except:
                    print("Caluculation error9");
                    self.label_64.setText(str("0"))
        else:
            self.label_64.setText(str("0"))
        
        
    def calculations(self):
        #results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_PEAK_LOAD_MM),printf(\"%.2f\", E_AT_LOAD_POINT_1)||'@'||LOAD_POINT_1,printf(\"%.2f\", E_AT_LOAD_POINT_2)||'@'||LOAD_POINT_2, CYCLE_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by cycle_id Asc")
        self.label_23.setText("%E@"+str(self.lineEdit_3_1.text())+"(N)")
        self.label_24.setText("%E@"+str(self.lineEdit_3_2.text())+"(N)")
        self.unit_type=self.comboBox_2.currentText()
        connection = sqlite3.connect("tyr.db")
        if(self.unit_type=="N/mm"):
            results=connection.execute(" select round(max(PEAK_LOAD_N),2), round(max(E_AT_PEAK_LOAD_MM),2), round(max(E_AT_LOAD_POINT_1),2), round(max(E_AT_LOAD_POINT_2),2) from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
        
        elif(self.unit_type == "Kgf/cm"):
            results=connection.execute(" select round(max(PEAK_LOAD_KG),2), round(max(E_AT_PEAK_LOAD_CM),2), round(max(E_AT_LOAD_POINT_1),2), round(max(E_AT_LOAD_POINT_2),2) from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
        else:
            results=connection.execute(" select round(max(PEAK_LOAD_KG),2), round(max(E_AT_PEAK_LOAD_MM),2), round(max(E_AT_LOAD_POINT_1),2), round(max(E_AT_LOAD_POINT_2),2) from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
        for x in results:
                    self.label_27.setText(str(x[0]))  #111.00
                    self.label_31.setText(str(x[1]))   #666.99
                    self.label_37.setText(str(x[2]))   #B11.00"
                    self.label_42.setText(str(x[3]))    #G34.00                 
        connection.close()
       
        connection = sqlite3.connect("tyr.db")
        if(self.unit_type=="N/mm"):
                    results=connection.execute(" select round(min(PEAK_LOAD_N),2), round(min(E_AT_PEAK_LOAD_MM),2), round(min(E_AT_LOAD_POINT_1),2), round(min(E_AT_LOAD_POINT_2),2) from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
        elif(self.unit_type == "Kgf/cm"):
                    results=connection.execute(" select round(min(PEAK_LOAD_KG),2), round(min(E_AT_PEAK_LOAD_CM),2), round(min(E_AT_LOAD_POINT_1),2), round(min(E_AT_LOAD_POINT_2),2) from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
        else:
                    results=connection.execute(" select round(min(PEAK_LOAD_KG),2), round(min(E_AT_PEAK_LOAD_MM),2), round(min(E_AT_LOAD_POINT_1),2), round(min(E_AT_LOAD_POINT_2),2) from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
        
        for x in results:
                    self.label_28.setText(str(x[0]))  #222.00
                    self.label_32.setText(str(x[1]))   #777.99
                    self.label_38.setText(str(x[2]))   #C22.00"
                    self.label_43.setText(str(x[3]))    #F56.00                 
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        if(self.unit_type=="N/mm"):
            results=connection.execute(" select round(avg(PEAK_LOAD_N),2), round(avg(E_AT_PEAK_LOAD_MM),2), round(avg(E_AT_LOAD_POINT_1),2), round(avg(E_AT_LOAD_POINT_2),2) from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
       
        elif(self.unit_type == "Kgf/cm"):
            results=connection.execute(" select round(avg(PEAK_LOAD_KG),2), round(avg(E_AT_PEAK_LOAD_CM),2), round(avg(E_AT_LOAD_POINT_1),2), round(avg(E_AT_LOAD_POINT_2),2) from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
       
        else:
            results=connection.execute(" select round(avg(PEAK_LOAD_KG),2), round(avg(E_AT_PEAK_LOAD_MM),2), round(avg(E_AT_LOAD_POINT_1),2), round(avg(E_AT_LOAD_POINT_2),2) from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
        for x in results:
                    self.label_29.setText(str(x[0]))  #333.00
                    self.label_33.setText(str(x[1]))   #888.00
                    self.label_39.setText(str(x[2]))   #D33.00"
                    self.label_44.setText(str(x[3]))    #Y66.00                 
        connection.close()
        
        '''
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select round(PEAK_LOAD_KG,2), round(E_AT_PEAK_LOAD_MM,2), round(E_AT_LOAD_POINT_1,2), round(E_AT_LOAD_POINT_2,2) from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
        for x in results:
                    self.label_30.setText(str(np.std(x[0])))  #444.00
                    self.label_34.setText(str(np.std(x[1])))   #999.00
                    self.label_40.setText(str(np.std(x[2])))   #E34.00"
                    self.label_45.setText(str(np.std(x[3])))    #J69.00                 
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select round(PEAK_LOAD_KG,2), round(E_AT_PEAK_LOAD_MM,2), round(E_AT_LOAD_POINT_1,2), round(E_AT_LOAD_POINT_2,2) from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
        for x in results:
                    self.label_36.setText(str(np.var(x[0])))  #555.00
                    self.label_35.setText(str(np.var(x[1])))   #A10.00
                    self.label_41.setText(str(np.var(x[2])))   #E34.00"
                    self.label_46.setText(str(np.var(x[3])))    #K87.00                 
        connection.close()
        '''
        connection = sqlite3.connect("tyr.db")
        results=connection.execute(" select count(cycle_id),ifnull(max(cycle_num),0)+1 from CYCLES_MST WHERE TEST_ID ='"+str(self.label_12.text())+"' ")       
        for x in results:
                    self.label_67.setText(str(x[0]))                    
                    self.cycle_num=int(x[1])
                    print("self.cycle_num :"+str(self.cycle_num))
        connection.close()
        
        
    
    def onchage_combo(self):                      
        connection = sqlite3.connect("tyr.db")
        #print("select C_A_AREA,GUAGE_LENGTH_MM,MOTOR_SPEED,PARTY_NAME,THICKNESS,WIDTH,DIAMETER,SHAPE ,IN_DIAMETER_MM,OUTER_DIAMETER_MM FROM SPECIMEN_MST WHERE SPECIMEN_NAME='"+self.comboBox.currentText()+"'")                 
        
        results=connection.execute("select C_A_AREA,GUAGE_LENGTH_MM,MOTOR_SPEED,PARTY_NAME,THICKNESS,WIDTH,DIAMETER,SHAPE ,IN_DIAMETER_MM,OUTER_DIAMETER_MM FROM SPECIMEN_MST WHERE SPECIMEN_NAME='"+self.comboBox.currentText()+"'")                 
        for x in results:
           if(self.comboBox_2.currentText()=="N/mm"):
               self.lineEdit_4.setText(str(x[0])) # CS AREA
               self.label_64.setText(str(x[0])) # ca area label
               self.lineEdit_7.setText(str(x[1])) # GUAGE LENGTH
           elif(self.comboBox_2.currentText()=="Kgf/cm"):    
               self.lineEdit_4.setText(str(int(x[0])/10)) # CS AREA
               self.label_64.setText(str(int(x[0])/10)) # ca area label
               self.lineEdit_7.setText(str(int(x[1]/10))) # GUAGE LENGTH
           else:
               self.lineEdit_4.setText(str(x[0])) # CS AREA
               self.label_64.setText(str(x[0])) # ca area label
               self.lineEdit_7.setText(str(x[1])) # GUAGE LENGTH
               
           self.lineEdit_9.setText(str(x[2])) # SPEED
           self.label_51.setText(str(x[3])) # Party Name
           self.label_61.setText(str(x[7]))
           self.label_54.show()
           self.lineEdit_5.show()
           self.label_55.show()
           self.lineEdit_8.show()
           self.label_56.show()
           self.label_62.show()
          
           if(str(x[7]) == "Rectangle"):
               if(self.comboBox_2.currentText()=="N/mm"):
                     self.lineEdit_5.setText(str(x[4]))#THICKNESS
                     self.lineEdit_8.setText(str(x[5]))#WIDTH
               elif(self.comboBox_2.currentText()=="Kgf/cm"):
                     self.lineEdit_5.setText(str(float(x[4])/10))#THICKNESS
                     self.lineEdit_8.setText(str(float(x[5])/10))#WIDTH                   
           elif(str(x[7]) == "Pipe"):
                 self.label_54.setText("Inn.Diam.")                
                 self.label_55.setText("Out.Diam.")
                 self.lineEdit_5.setText(str(x[8]))#INN Diameter
                 self.lineEdit_8.setText(str(x[9]))#OUT.DIAMETER        
           elif(str(x[7]) == "Cylindrical"):
                 self.label_54.setText("Diameter.")
                 self.lineEdit_5.setText(str(x[6]))# Diameter
                 self.label_55.hide()
                 self.lineEdit_8.hide()
                 self.label_62.hide()
           elif(str(x[7]) == "DirectValue"):
                self.label_54.hide()
                self.lineEdit_5.hide()
                self.label_55.hide()
                self.lineEdit_8.hide()
                self.label_56.hide()
                self.label_62.hide()
           else:
                self.label_21.setText("Invalid:"+str(x[7]))
           
           #self.lineEdit_5.setText("5")#Party NAme
            
            
        connection.close()
        
    
    
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
        
    def start_test_FBST(self):
        #elf.label_35.setText("")
        
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
        if(self.lineEdit_4.text() == ""): # CS AREA
                    self.label_21.show()
                    self.label_21.setText("CS AREA Should not Empty.")           
        elif(self.label_64.text() == "0"): # ca area label
                    self.label_21.show()
                    self.label_21.setText("CS AREA Should not zero.")
        elif(self.lineEdit_7.text() == ""): # GUAGE LENGTH
                    self.label_21.show()
                    self.label_21.setText("Guage Length Should not Empty.")   
        elif(self.lineEdit_3.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("Batch ID Should not Empty.")
                    
        elif(self.lineEdit_9.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("Test Speed Should not Empty.")
               
        elif(self.lineEdit_3_1.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("Load 1 Should not Empty.")
        elif(self.lineEdit_3_2.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("Load 2 Should not Empty.")
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
                            cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"'")
                            cursor.execute("UPDATE TEST_MST SET SPECIMEN_NAME='"+str(self.comboBox.currentText())+"',BATCH_ID='"+str(self.lineEdit_3.text())+"',PARTY_NAME='"+str(self.label_51.text())+"',GUAGE_LENGTH='"+str(self.lineEdit_7.text())+"',MOTOR_SPEED='"+str(self.lineEdit_9.text())+"'  WHERE  TEST_ID = '"+str(self.label_12.text())+"'")
                        connection.commit();
                        connection.close()
                        
               else:        
                        ### INSERT 
                        connection = sqlite3.connect("tyr.db")              
                        with connection:        
                          cursor = connection.cursor()                  
                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"'")
                          cursor.execute("INSERT INTO TEST_MST(SPECIMEN_NAME,BATCH_ID,PARTY_NAME,TEST_TYPE,GUAGE_LENGTH,MOTOR_SPEED) VALUES('"+str(self.comboBox.currentText())+"','"+str(self.lineEdit_3.text())+"','"+str(self.label_51.text())+"','FBST','"+str(self.lineEdit_7.text())+"','"+str(self.lineEdit_9.text())+"')")
                        connection.commit();
                        connection.close()
       
              
    
    def show_load_cell_val(self):      
        
        self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q_n)))        
        self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))   #length
        
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
                
        
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
    
    def show_all_specimens(self): 
        self.sc_data =PlotCanvas(self,width=5, height=4, dpi=80)    
        self.gridLayout.addWidget(self.sc_data, 1, 0, 1, 1)
    
    def save_graph_data(self):         
         if (len(self.sc_new.arr_p) > 1):            
            
            #self.cycle_num=int(str(self.label_67.text()))+1
            
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)):                     
                        cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM_N,Y_NUM_LB) VALUES ('"+str(self.sc_new.arr_p[g])+"','"+str(self.sc_new.arr_q[g])+"','"+str(self.sc_new.arr_p_cm[g])+"','"+str(self.sc_new.arr_p_inch[g])+"','"+str(self.sc_new.arr_q_n[g])+"','"+str(self.sc_new.arr_q_lb[g])+"')")
            connection.commit();
            connection.close()
            
            self.get_points()
            #self.cycle_num=self.cycle_num+1
            connection = sqlite3.connect("tyr.db")              
            with connection:        
                  cursor = connection.cursor()
                  #print("ok1")
                  try:
                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"',LOAD_POINT_1='"+str(self.lineEdit_3_1.text())+"',LOAD_POINT_2='"+str(self.lineEdit_3_2.text())+"',NEW_TEST_GUAGE_MM='"+str(self.lineEdit_7.text())+"'")                          
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM) FROM STG_GRAPH_MST),NEW_TEST_MOTOR_SPEED='"+str(self.lineEdit_9.text())+"'") 
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_N=(SELECT MAX(Y_NUM_N) FROM STG_GRAPH_MST)") 
                         
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_PEAK_LOAD_MM=(SELECT X_NUM FROM STG_GRAPH_MST WHERE Y_NUM=(SELECT STG_PEAK_LOAD_KG FROM GLOBAL_VAR))")
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_PEAK_LOAD_CM=(SELECT X_NUM_CM FROM STG_GRAPH_MST WHERE Y_NUM=(SELECT STG_PEAK_LOAD_KG FROM GLOBAL_VAR))") 
                          #print("ok2")
                          cursor.execute("INSERT INTO CYCLES_MST(TEST_ID,TEST_METHOD,PEAK_LOAD_KG,PEAK_LOAD_N,E_AT_PEAK_LOAD_MM,E_AT_PEAK_LAOD_CM,LOAD_POINT_1,LOAD_POINT_2,E_AT_LOAD_POINT_1,E_AT_LOAD_POINT_2) SELECT TEST_ID,'FBST',STG_PEAK_LOAD_KG,STG_PEAK_LOAD_N,STG_E_AT_PEAK_LOAD_MM,STG_E_AT_PEAK_LOAD_CM,LOAD_POINT_1,LOAD_POINT_2,E_AT_LOAD_POINT_1,E_AT_LOAD_POINT_2 FROM GLOBAL_VAR")
                          
                          cursor.execute("UPDATE CYCLES_MST SET CYCLE_NUM='"+str(self.cycle_num)+"'  WHERE GRAPH_ID IS NULL")
                          cursor.execute("UPDATE CYCLES_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")
                          
                          cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM,X_NUM_CM,Y_NUM_N) SELECT X_NUM,Y_NUM,X_NUM_CM,Y_NUM_N FROM STG_GRAPH_MST")                  
                          cursor.execute("UPDATE GRAPH_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL") 
                          cursor.execute("UPDATE TEST_MST SET STATUS='LOADED GRAPH'  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")                  
                          cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_X_LENGTH=(SELECT GRAPH_SCALE_CELL_2 FROM SETTING_MST),GRAPH_SCAL_Y_LOAD=(SELECT GRAPH_SCALE_CELL_1 FROM SETTING_MST)  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                    
                  except Exception as e:
                          print("SQL Error:"+str(e))
                      
            connection.commit();
            connection.close()            
            print("Data Saved Ok in STG_GRAPH_MST")           
            self.show_grid_data_FBST()
            
        
    def get_points(self):
       
        self.guage_length=0
        self.E_at_load_point_1=0
        self.E_at_load_point_2=0
        
        self.PER_E_at_load_point_1=0
        self.PER_E_at_load_point_2=0
        c=0
        def_rec_id_1=0
        self.unit_typex=self.comboBox_2.currentText()
        if(str(self.lineEdit_7.text()) != ""):        
                     self.guage_length=str(self.lineEdit_7.text())         
                
        connection = sqlite3.connect("tyr.db")        
        #results=connection.execute("SELECT X_NUM,Y_NUM,REC_ID FROM STG_GRAPH_MST where X_NUM >  0  order by REC_ID ASC")
        if(self.unit_typex == "N/mm"):
             results=connection.execute("SELECT X_NUM,Y_NUM_N,REC_ID FROM STG_GRAPH_MST where X_NUM >  0  order by REC_ID ASC")
        elif(self.unit_typex == "Kgf/cm"):
             results=connection.execute("SELECT X_NUM,Y_NUM,REC_ID FROM STG_GRAPH_MST where X_NUM >  0   order by REC_ID ASC")
        else:   
             results=connection.execute("SELECT X_NUM,Y_NUM,REC_ID FROM STG_GRAPH_MST where X_NUM >  0   order by REC_ID ASC")
       
        for x in results:
            print("x_num :"+str(x[0])+"   y_num:"+str(x[1]))
            if (float(c)==0):                
                c=float(round(x[1],2))
            else:
                if(float(x[1]) < float((self.lineEdit_3_1.text()))):
                    c=float(x[1])
                    continue
                elif(float(x[1]) == float((self.lineEdit_3_1.text()))):
                    self.E_at_load_point_1=float(x[0])
                    def_rec_id_1=int(str(x[2]))
                    print("Break 1 Point :"+str(self.E_at_load_point_1))
                    break
                elif(float(x[1]) > float((self.lineEdit_3_1.text()))):
                    self.E_at_load_point_1=float(x[0])
                    def_rec_id_1=int(str(x[2]))
                    print("Break 2 Point :"+str(self.E_at_load_point_1))
                    break
                else:
                    c=float(x[1])
                    self.E_at_load_point_1=float(x[0])
                    def_rec_id_1=int(str(x[2]))
                    print("Break 3 Point :"+str(self.E_at_load_point_1))
                    break
        connection.close()
        
        print("##############################")
        c=0
        def_rec_id_2=0
        
        connection = sqlite3.connect("tyr.db")
        if(self.unit_typex == "N/mm"):
             results=connection.execute("SELECT X_NUM,Y_NUM_N,REC_ID FROM STG_GRAPH_MST where X_NUM >  0  and REC_ID > "+str(def_rec_id_1)+" order by REC_ID ASC")
        elif(self.unit_typex == "Kgf/cm"):
             results=connection.execute("SELECT X_NUM,Y_NUM,REC_ID FROM STG_GRAPH_MST where X_NUM >  0  and REC_ID > "+str(def_rec_id_1)+" order by REC_ID ASC")
        else:   
             results=connection.execute("SELECT X_NUM,Y_NUM,REC_ID FROM STG_GRAPH_MST where X_NUM >  0  and REC_ID > "+str(def_rec_id_1)+" order by REC_ID ASC")
        for x in results:
            print("x_num :"+str(x[0])+"   y_num:"+str(x[1]))
            if (float(c)==0):                
                c=float(round(x[1],2))
            else:
                if(float(x[1]) < float((self.lineEdit_3_2.text()))):
                    c=float(x[1])
                    continue
                elif(float(x[1]) == float((self.lineEdit_3_2.text()))):
                    self.E_at_load_point_2=float(x[0])
                    def_rec_id_2=int(str(x[2]))
                    print("Break 1 Point :"+str(self.E_at_load_point_2))
                    break
                elif(float(x[1]) > float((self.lineEdit_3_2.text()))):
                    self.E_at_load_point_2=float(x[0])
                    def_rec_id_2=int(str(x[2]))
                    print("Break 2 Point :"+str(self.E_at_load_point_2))
                    break
                else:
                    c=float(x[1])
                    self.E_at_load_point_2=float(x[0])
                    def_rec_id_2=int(str(x[2]))
                    print("Break 3 Point :"+str(self.E_at_load_point_3))
                    break
        connection.close()
        
        #### Elongation Load Point 2       
        
               
        #connection.close()
        if(int(self.guage_length) > 0):
                print(" self.guage_length:"+str(self.guage_length))
                self.PER_E_at_load_point_1=float((int(self.E_at_load_point_1)/int(self.guage_length))*100)
                self.PER_E_at_load_point_2=float((int(self.E_at_load_point_2)/int(self.guage_length))*100)
        print("E_at_load_point_1:"+str(self.PER_E_at_load_point_2)+" E_at_load_point_2:"+str(self.PER_E_at_load_point_2))
        connection = sqlite3.connect("tyr.db")              
        with connection:
                cursor = connection.cursor()               
                cursor.execute("UPDATE GLOBAL_VAR SET E_AT_LOAD_POINT_1='"+str(self.PER_E_at_load_point_1)+"',E_AT_LOAD_POINT_2='"+str(self.PER_E_at_load_point_2)+"'")
        connection.commit();
        connection.close()
        
                
        
    def show_grid_data_FBST(self):        
        #print("inside tear list.....")
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setHorizontalHeaderLabels(['Spec.No.','Break Load '+str(self.y_unit),'E@Break '+str(self.x_unit),'%E@'+str(self.lineEdit_3_1.text())+' '+str(self.y_unit),'%E@'+str(self.lineEdit_3_2.text())+' '+str(self.y_unit),'REC.NO '])  
              
        self.tableWidget.setColumnWidth(0, 170)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)
        
        self.unit_type=self.comboBox_2.currentText()
        connection = sqlite3.connect("tyr.db")
        if(self.unit_type=="N/mm"): 
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", PEAK_LOAD_N),printf(\"%.2f\", E_AT_PEAK_LOAD_MM),printf(\"%.2f\", E_AT_LOAD_POINT_1),printf(\"%.2f\", E_AT_LOAD_POINT_2), CYCLE_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by CYCLE_NUM Asc")
        elif(self.unit_type == "Kgf/cm"):
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_PEAK_LAOD_CM),printf(\"%.2f\", E_AT_LOAD_POINT_1),printf(\"%.2f\", E_AT_LOAD_POINT_2), CYCLE_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by CYCLE_NUM Asc")
        else:
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_PEAK_LOAD_MM),printf(\"%.2f\", E_AT_LOAD_POINT_1),printf(\"%.2f\", E_AT_LOAD_POINT_2), CYCLE_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by CYCLE_NUM Asc")
        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()
        self.calculations()
       
    
         
    def reset(self):        
        if(self.timer3.isActive()): 
           self.timer3.stop() 
        
        #self.sc_blank =PlotCanvas_blank(self) 
        #self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
        
        
    def print_file(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POP_TEST_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
              
    
    def create_pdf_FBST(self):        
#        connection = sqlite3.connect("tyr.db")
#        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
#        for x in results:
#            self.graph_typex=x[0]
#            self.unit_typex=x[1]
#        connection.close()
        self.remark=""
        self.unit_typex=self.comboBox_2.currentText()
        if(self.unit_typex == "N/mm"):
            data2= [ ['Spec.No', 'Break. Load (N)', 'E@Break(mm)', 'E@'+str(self.lineEdit_3_1.text())+'(N)', 'E@'+str(self.lineEdit_3_2.text())+'(N)']]
        elif(self.unit_typex == "Kgf/cm"):
            data2= [ ['Spec.No', 'Break. Load (Kgf)', 'E@Break(cm)', 'E@'+str(self.lineEdit_3_1.text())+'(Kgf)', 'E@'+str(self.lineEdit_3_2.text())+'(Kgf)']]        
        else:
            data2= [ ['Spec.No', 'Avg. Load (N)', 'Load at First Peak\n (N)', 'Max Load \n (N)', 'Min Load \n (N)']]
          
        #esults=connection.execute("SELECT CYCLE_NUM,printf(\"%.2f\", PEAK_LOAD_KG),printf(\"%.2f\", E_AT_PEAK_LOAD_MM),printf(\"%.2f\", E_AT_LOAD_POINT_1)||'@'||LOAD_POINT_1,printf(\"%.2f\", E_AT_LOAD_POINT_2)||'@'||LOAD_POINT_2, CYCLE_ID FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by CYCLE_NUM Asc")
        
        connection = sqlite3.connect("tyr.db")
        if(self.unit_typex == "N/mm"):
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.4f\", A.PEAK_LOAD_N),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM),printf(\"%.2f\", A.E_AT_LOAD_POINT_1),printf(\"%.2f\", A.E_AT_LOAD_POINT_2) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
        elif(self.unit_typex == "Kgf/cm"):
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.4f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.E_AT_PEAK_LAOD_CM),printf(\"%.2f\", A.E_AT_LOAD_POINT_1),printf(\"%.2f\", A.E_AT_LOAD_POINT_2) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
        else:
            results=connection.execute("SELECT CYCLE_NUM,printf(\"%.4f\", A.PEAK_LOAD_KG),printf(\"%.2f\", A.E_AT_PEAK_LOAD_MM),printf(\"%.2f\", A.E_AT_LOAD_POINT_1),printf(\"%.2f\", A.E_AT_LOAD_POINT_2) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
        
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        if(self.unit_typex == "N/mm"):
                results=connection.execute("SELECT 'AVG',printf(\"%.4f\", avg(A.PEAK_LOAD_N)),printf(\"%.2f\",avg(A.E_AT_PEAK_LOAD_MM)),printf(\"%.2f\", avg(A.E_AT_LOAD_POINT_1)),printf(\"%.2f\", avg(A.E_AT_LOAD_POINT_2)) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
        elif(self.unit_typex == "Kgf/cm"):
                results=connection.execute("SELECT 'AVG',printf(\"%.4f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\",avg(A.E_AT_PEAK_LAOD_CM)),printf(\"%.2f\", avg(A.E_AT_LOAD_POINT_1)),printf(\"%.2f\", avg(A.E_AT_LOAD_POINT_2)) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
        else:
                results=connection.execute("SELECT 'AVG',printf(\"%.4f\", avg(A.PEAK_LOAD_KG)),printf(\"%.2f\",avg(A.E_AT_PEAK_LOAD_MM)),printf(\"%.2f\", avg(A.E_AT_LOAD_POINT_1)),printf(\"%.2f\", avg(A.E_AT_LOAD_POINT_2)) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
       
        for x in results:
                data2.append(x)
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        if(self.unit_typex == "N/mm"):
            results=connection.execute("SELECT 'MAX',printf(\"%.4f\", max(A.PEAK_LOAD_N)),printf(\"%.2f\",max(A.E_AT_PEAK_LOAD_MM)),printf(\"%.2f\", max(A.E_AT_LOAD_POINT_1)),printf(\"%.2f\", max(A.E_AT_LOAD_POINT_2)) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
        
        elif(self.unit_typex == "Kgf/cm"):
            results=connection.execute("SELECT 'MAX',printf(\"%.4f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\",max(A.E_AT_PEAK_LAOD_CM)),printf(\"%.2f\", max(A.E_AT_LOAD_POINT_1)),printf(\"%.2f\", max(A.E_AT_LOAD_POINT_2)) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
        
        else:
            results=connection.execute("SELECT 'MAX',printf(\"%.4f\", max(A.PEAK_LOAD_KG)),printf(\"%.2f\",max(A.E_AT_PEAK_LOAD_MM)),printf(\"%.2f\", max(A.E_AT_LOAD_POINT_1)),printf(\"%.2f\", max(A.E_AT_LOAD_POINT_2)) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        if(self.unit_typex == "N/mm"):
                results=connection.execute("SELECT 'MIN',printf(\"%.4f\", min(A.PEAK_LOAD_N)),printf(\"%.2f\",min(A.E_AT_PEAK_LOAD_MM)),printf(\"%.2f\", min(A.E_AT_LOAD_POINT_1)),printf(\"%.2f\", min(A.E_AT_LOAD_POINT_2)) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
        elif(self.unit_typex == "Kgf/cm"):
                results=connection.execute("SELECT 'MIN',printf(\"%.4f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\",min(A.E_AT_PEAK_LAOD_CM)),printf(\"%.2f\", min(A.E_AT_LOAD_POINT_1)),printf(\"%.2f\", min(A.E_AT_LOAD_POINT_2)) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
        else:
              results=connection.execute("SELECT 'MIN',printf(\"%.4f\", min(A.PEAK_LOAD_KG)),printf(\"%.2f\",min(A.E_AT_PEAK_LOAD_MM)),printf(\"%.2f\", min(A.E_AT_LOAD_POINT_1)),printf(\"%.2f\", min(A.E_AT_LOAD_POINT_2)) FROM  CYCLES_MST A WHERE A.TEST_ID ='"+str(self.label_12.text())+"'") 
        for x in results:
                data2.append(x)
        connection.close()
        
        y=300
        Elements=[]
        summary_data=[]
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,A.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime') ,A.COMMENTS FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID ='"+str(self.label_12.text())+"'")
        
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Specmen Shape:",str(x[9])],["Test Type:",str(x[3]),"Specmen Specs:",str(x[0])],["Party Name :",str(x[7]),"Test Speed (mm/min) :",str(x[5])],["Guage Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", "","",""]]
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
                                bottomMargin=30,)
        doc.build(Elements)
        
    def open_pdf(self):
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90) 
        self.create_pdf_FBST() 
        
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
        self.unit_type=""
        self.color=['b','r','g','y','k','c','m','b']
        #ax.set_title('Test Id=32         Samples=3       BreakLoad(Kg)=110        Length(mm)=3')
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME,CURR_UNIT_TYPE FROM GLOBAL_VAR") 
        for x in results:
            self.test_type=str(x[0])
            self.unit_type=str(x[1])
        connection.close()
        
        ### Univarsal change for  Graphs #####################
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
            if(self.unit_type == "N/mm"):
                 ax.set_xlim(0,int(x[0]))
                 ax.set_ylim(0,int(x[1])*9.81)
                 ax.set_xlabel('Distance (mm)')
                 ax.set_ylabel('Load (N)')
            if(self.unit_type == "Kgf/cm"):
                 ax.set_xlim(0,int(x[0])/10)
                 ax.set_ylim(0,int(x[1]))
                 ax.set_xlabel('Distance (cm)')
                 ax.set_ylabel('Load kgf)')
            else:     
                 ax.set_xlim(0,int(x[0]))
                 ax.set_ylim(0,int(x[1])*9.81)
                 ax.set_xlabel('Distance (mm)')
                 ax.set_ylabel('Load (N)')
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
            elif(self.unit_type == "Kgf/cm"):
                results=connection.execute("SELECT X_NUM_CM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
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
        
        #ax.connect('motion_notify_event', mouse_move)
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
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE from GLOBAL_VAR") 
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
        connection.close()
        print(" xxx     gfgf self.unit_type:"+str(self.unit_type))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:
             if(self.unit_type == "Kgf/cm"):
                     self.axes.set_xlim(0,int(x[0])/10)
                     self.axes.set_ylim(0,int(x[1]))
                     #self.flexural_max_load=int(x[1])/9.81
                     self.xlim=int(x[0])/10
                     self.ylim=int(x[1])
                     self.axes.set_xlabel('Distance (cm)')
                     self.axes.set_ylabel('Load (Kgf)')
             elif(self.unit_type == "N/mm"):
                     self.axes.set_xlim(0,int(x[0]))
                     self.axes.set_ylim(0,int(x[1])*9.81)
                     #self.flexural_max_load=int(x[1])/9.81
                     self.xlim=int(x[0])
                     self.ylim=int(x[1])* 9.81
                     self.axes.set_xlabel('Distance (mm)')
                     self.axes.set_ylabel('Load (N)')         
             else:
                     self.axes.set_xlim(0,int(x[0]))
                     self.axes.set_ylim(0,int(x[1]))
                     #self.flexural_max_load=int(x[1])
                     self.xlim=int(x[0])/10
                     self.ylim=int(x[1])
                     self.axes.set_xlabel('Distance (xxmm)')
                     self.axes.set_ylabel('Load (xN)') 
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


                self.p_cm=float(self.p)/10
                self.arr_p_cm.append(float(self.p_cm))
                
                self.p_inch=float(self.p)*0.0393701
                self.arr_p_inch.append(float(self.p_inch))
                
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
        if(self.unit_type == "Kgf/cm"):
            self.line_cnt.set_data(self.arr_p_cm,self.arr_q)
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
        self.unit_type=""
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
        results=connection.execute("SELECT CURR_UNIT_TYPE from GLOBAL_VAR") 
        for x in results:
                self.unit_type=str(x[0]) 
        connection.close() 
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
             if(self.unit_type=="Kgf/cm"):
                 ax.set_xlim(0,int(x[0])/10)
                 ax.set_ylim(0,int(x[1]))
                 ax.set_xlabel('Distance (cm)')
                 ax.set_ylabel('Load (Kgf) ')
             else:
                 ax.set_xlim(0,int(x[0]))
                 ax.set_ylim(0,int(x[1]) * 9.81)
                 ax.set_xlabel('Distance (mm)')
                 ax.set_ylabel('Load (N) ')
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
    ui = TY_26_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
