
from MDR_02_SETTING import mdr_02_Ui_MainWindow
from MDR_05_SP_MDR import mdr_05_Ui_MainWindow

from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow
from comment_popup import comment_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os


from PyQt5 import QtCore, QtGui, QtWidgets

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

class MDR_01_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1341, 711))
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
        self.label_20.setGeometry(QtCore.QRect(1110, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 120, 1341, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 600, 1341, 111))
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
        self.tableWidget.setColumnCount(19)
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
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(19, item)
       
        
        
       
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
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(410, 50, 81, 61))
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("value", 100.0)
        self.lcdNumber.setProperty("intValue", 100)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(410, 10, 81, 31))
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
        self.layoutWidget.setGeometry(QtCore.QRect(10, 140, 761, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
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
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(540, 10, 81, 31))
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
        self.lcdNumber_2.setGeometry(QtCore.QRect(540, 50, 81, 61))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setProperty("value", 100.0)
        self.lcdNumber_2.setProperty("intValue", 100)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.line_15 = QtWidgets.QFrame(self.frame)
        self.line_15.setGeometry(QtCore.QRect(370, 0, 20, 131))
        self.line_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_15.setLineWidth(3)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setObjectName("line_15")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(270, 30, 81, 81))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/stop.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(100, 100))
        
        self.toolButton.setObjectName("toolButton")
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(10, 80, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_3.setGeometry(QtCore.QRect(670, 50, 81, 61))
        self.lcdNumber_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_3.setSmallDecimalPoint(False)
        self.lcdNumber_3.setProperty("value", 100.0)
        self.lcdNumber_3.setProperty("intValue", 100)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(670, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.line_16 = QtWidgets.QFrame(self.frame)
        self.line_16.setGeometry(QtCore.QRect(510, 0, 20, 131))
        self.line_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_16.setLineWidth(3)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.frame)
        self.line_17.setGeometry(QtCore.QRect(640, 0, 20, 131))
        self.line_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_17.setLineWidth(3)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.frame)
        self.line_18.setGeometry(QtCore.QRect(770, 0, 20, 131))
        self.line_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_18.setLineWidth(3)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.frame)
        self.line_19.setGeometry(QtCore.QRect(1080, 0, 20, 131))
        self.line_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_19.setLineWidth(3)
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setObjectName("line_19")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(1240, 50, 61, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/report3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setIconSize(QtCore.QSize(250, 150))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.frame)
        self.toolButton_4.setGeometry(QtCore.QRect(1130, 50, 71, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon2)
        self.toolButton_4.setIconSize(QtCore.QSize(250, 150))
        self.toolButton_4.setObjectName("toolButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(800, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 180);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(940, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 180);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(940, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 180);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(800, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(0, 0, 180);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(1100, 140, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(1100, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(910, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(790, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(1190, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(790, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(910, 180, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(790, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(910, 220, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(790, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(790, 310, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(920, 270, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(990, 270, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(920, 320, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(990, 310, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(790, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(920, 350, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(990, 350, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(790, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(920, 390, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(770, 420, 321, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(883, 130, 20, 301))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(770, 380, 321, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(770, 340, 321, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(770, 300, 321, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(770, 250, 321, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(1080, 130, 20, 301))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(780, 550, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(920, 550, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 85, 127);\n ")
        self.pushButton_11.setObjectName("pushButton_11")
        
        self.pushButton_11_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11_1.setGeometry(QtCore.QRect(1060, 550, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11_1.setFont(font)
        self.pushButton_11_1.setStyleSheet("background-color: rgb(170, 170, 255);\n")
        self.pushButton_11_1.setObjectName("pushButton_11_1")
        
        
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(1090, 270, 251, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_2.setLineWidth(3)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        '''
        
        
        '''
        
        
        
        
        
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(790, 510, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.frame)
        self.label_51.setGeometry(QtCore.QRect(90, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(1100, 240, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        
        self.buttongroup = QtWidgets.QButtonGroup()
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 20, 82, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        
        self.buttongroup.addButton(self.radioButton, 1)
        self.buttongroup.addButton(self.radioButton_2, 2)
        
        
        self.label_52 = QtWidgets.QLabel(self.frame)
        self.label_52.setGeometry(QtCore.QRect(1050, 510, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_52.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_52.setObjectName("label_52")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(1160, 510, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(1220, 510, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.goAhead="No"
        self.test_id_exist="No"
        self.timer3=QtCore.QTimer()
        self.sc_blank=""
        self.cycle_num=0
        self.machine_health="NOTOK"
        self.max_time_mm=0
        self.test_per=0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Spec.No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CA. Area (mm2)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Load@Break(N)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Elong.@Break(%)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Elong.@1500(%)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Elong.@5800(%)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Rec.No"))
        '''
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "T_S2"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "T_S5"))
        '''
        
        
        
        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "100"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "67"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "45"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "23"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "23"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "11"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_13.setText(_translate("MainWindow", "Torque (N) :"))
        self.label_22.setText(_translate("MainWindow", "Running......"))
        self.label_22.hide()
        self.label_14.setText(_translate("MainWindow", "Temp1 (.C) "))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_48.setText(_translate("MainWindow", "Status :"))
        self.label_21.setText(_translate("MainWindow", "Temp2 (.C) "))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.pushButton_5.setText(_translate("MainWindow", "Email Report"))
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setText(_translate("MainWindow", "View Report"))
        self.pushButton_6.setDisabled(True)
        self.pushButton_7.setText(_translate("MainWindow", "Print Report"))
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setText(_translate("MainWindow", "Remark"))
        self.pushButton_8.setDisabled(True)
        self.comboBox.setItemText(0, _translate("MainWindow", "Method 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Method 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Method 3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Method 4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Method 5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Method 6"))
        self.label_11.setText(_translate("MainWindow", "Spec.No:"))
        self.label_9.setText(_translate("MainWindow", "Batch ID :"))
        self.label_12.setText(_translate("MainWindow", "0017"))
        self.label_10.setText(_translate("MainWindow", "Operator :"))
        self.label_15.setText(_translate("MainWindow", "Shift.No:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Shift 1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Shift  2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Shift  3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Shift  4"))
        self.label_16.setText(_translate("MainWindow", "Max. Torq"))
        self.label_17.setText(_translate("MainWindow", "Test. Temp "))
        self.label_18.setText(_translate("MainWindow", "455"))
        self.label_19.setText(_translate("MainWindow", "(N)"))
        self.label_23.setText(_translate("MainWindow", "156"))
        self.label_24.setText(_translate("MainWindow", "(.C)"))
        self.label_25.setText(_translate("MainWindow", "Test. Time "))
        self.label_26.setText(_translate("MainWindow", "60"))
        self.label_27.setText(_translate("MainWindow", "(Min)"))
        self.label_28.setText(_translate("MainWindow", "Arc. "))
        self.label_29.setText(_translate("MainWindow", "0.5"))
        self.pushButton_9.setText(_translate("MainWindow", "Start Test"))
        self.pushButton_9.setDisabled(True)
        self.pushButton_11.setText(_translate("MainWindow", "Stop Test"))
        self.pushButton_11.setDisabled(True)
        self.pushButton_11_1.setText(_translate("MainWindow", "Reset"))
        self.pushButton_11_1.setDisabled(True)
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "P"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "L"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "U"))
        self.label_50.setText(_translate("MainWindow", "Preparing for Test is in Progress .....36%"))
        self.label_50.hide()
        self.label_51.setText(_translate("MainWindow", " Machine is Down."))
        self.label_32.setText(_translate("MainWindow", "Limits :"))
        self.radioButton.setText(_translate("MainWindow", "ON"))
        self.radioButton_2.setText(_translate("MainWindow", "OFF"))
        self.label_52.setText(_translate("MainWindow", "Elapsed Time :"))
        self.label_33.setText(_translate("MainWindow", "0"))
        self.label_34.setText(_translate("MainWindow", "(Min)"))
        self.sc_blank =PlotCanvas_blank(self,width=8, height=5,dpi=90)          
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_3.setProperty("value", 0.0)
        self.load_data()
        self.pushButton_9.clicked.connect(self.start_test_MDR)
        self.pushButton_11.clicked.connect(self.stop_test_MDR)
        self.comboBox.currentTextChanged.connect(self.onchage_combo)
        self.toolButton_4.clicked.connect(self.open_setting)
        self.toolButton_3.clicked.connect(self.open_report)
        
        self.pushButton_8.clicked.connect(self.open_comment_popup)
        self.pushButton_7.clicked.connect(self.print_file)
        self.pushButton_5.clicked.connect(self.open_email_report)
        self.pushButton_6.clicked.connect(self.open_pdf)
        self.pushButton_11_1.clicked.connect(self.reset_test)
        
        self.radioButton.clicked.connect(self.machine_status)
        self.radioButton_2.clicked.connect(self.machine_status)
         
        
        self.show_grid_data_MDR()
        self.show_grid_data_LIMITS()
        self.onchage_combo()
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
       
    def reset_test(self):
        self.sc_blank =PlotCanvas_blank(self,width=8, height=5,dpi=90)          
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_3.setProperty("value", 0.0)
        self.label_50.hide()
        self.label_22.hide()
        self.label_33.setText("0")
        connection = sqlite3.connect("mdr.db")        
        with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("update global_var set TEST_ID='0'")                 
        connection.commit()
        connection.close()
        self.show_grid_data_MDR()
        
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def machine_status(self):
        self.machine_health="NOTOK"
        self.ErrorMsg=""
        if(self.radioButton.isChecked()):
            self.radioButton.setDisabled(True)
            self.radioButton_2.setEnabled(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("./images/start.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton.setIcon(icon)
            self.toolButton.setIconSize(QtCore.QSize(100, 100))
            self.check_machine_health()
            if(self.machine_health=="NOTOK"):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("./images/stop1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.toolButton.setIcon(icon)
                self.toolButton.setIconSize(QtCore.QSize(100, 100))
                self.label_51.setText(str(self.ErrorMsg))                
            else:
                self.label_51.setText("Machine is ON")
                self.pushButton_9.setEnabled(True)
                self.pushButton_11.setEnabled(True)
                
            
        elif(self.radioButton_2.isChecked()):
            self.radioButton_2.setDisabled(True)
            self.radioButton.setEnabled(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("./images/stop.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton.setIcon(icon)
            self.toolButton.setIconSize(QtCore.QSize(100, 100))
            self.label_51.setText("Machine is DOWN")
            self.pushButton_9.setDisabled(True)
            self.pushButton_11.setDisabled(True)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("./images/stop.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton.setIcon(icon)
            self.toolButton.setIconSize(QtCore.QSize(100, 100))
            self.pushButton_9.setDisabled(True)
            self.pushButton_11.setDisabled(True)
            
    def check_machine_health(self):
        self.machine_health="OK"
        self.go_ahead="No"
        self.ErrorMsg="Connection Issue"
        self.check_registration()
        if(self.go_ahead=="No"):            
            self.ErrorMsg="Registration Error"
            self.machine_health="NOTOK"
        else:
            self.ErrorMsg="Start Test"
            
        
        
    def check_registration(self):        
        self.go_ahead="No"
        f = open("/var/local/devid", "r")
        dev_id=f.read()
        f.close()
        serial_no=self.getserial()        
        
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("select DEVICE_SERIAL_NO from GLOBAL_VAR") 
        for x in results:
            #print("serial_no:"+str(serial_no))
            if(serial_no == str(x[0])):
               self.go_ahead="Yes"
            else:
               self.go_ahead="No"
        connection.close()
        
        if(self.go_ahead =="Yes"):  
            if(dev_id=='201910:0003'):
                #self.label_51.setText("Start Test")
                print("dev id ok :"+str(dev_id))
                
            else:
                print("dev id Error :"+str(dev_id))   
        else:
           print("Device Invalid :call 9773540255")
        
    
    
    def getserial(self):
        # Extract serial from cpuinfo file
        cpuserial = "0000000000000000"
        try:
           f = open('/proc/cpuinfo','r')
           for line in f:
                if line[0:6]=='Serial':
                   cpuserial = line[10:26]
           f.close()
        except:
           cpuserial = "ERROR000000000"
        return cpuserial
            
            
    def load_data(self):
        self.i=0
        self.comboBox.clear()
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("SELECT METHOD_NAME FROM METHODS_MST WHERE STATUS = 'ACTIVE'") 
        for x in results:            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        
        self.i=0
        self.comboBox_2.clear()
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("SELECT SHIFT_NAME FROM SHIFT_MST ") 
        for x in results:            
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        
        connection = sqlite3.connect("mdr.db")        
        with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("update global_var set TEST_ID=''")                 
        connection.commit()
        connection.close() 
    
    def onchage_combo(self):                      
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("select SET_TEMP,SET_TORQUE,SET_TEST_TIME,SPEC_NUM,ARC FROM METHODS_MST WHERE METHOD_NAME='"+self.comboBox.currentText()+"'")                 
        for x in results:
           self.label_23.setText(str(x[0])) # TempA
           self.label_18.setText(str(x[1])) # Tarq
           self.label_26.setText(str(x[2])) # Time
           self.max_time_mm=str((x[2]))
           self.test_per=0
           self.label_12.setText(str(x[3])) # Spec Name
           self.label_29.setText(str(x[4])) # Arc
           self.lineEdit_3.setText("BATCH_ID_"+str(x[3]))
          
        connection.close()
        self.show_grid_data_LIMITS()
    
    def print_file(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POP_TEST_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_email_report(self):        
        connection = sqlite3.connect("mdr.db")        
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
        connection = sqlite3.connect("mdr.db")        
        with connection:        
                    cursor = connection.cursor()                
                    cursor.execute("update global_var set EMAIL_TEST_ID=TEST_ID")                 
        connection.commit()
        connection.close()            
        self.window = QtWidgets.QMainWindow()
        self.ui=comment_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def start_test_MDR(self):
        close = QMessageBox()
        close.setText("Are You Sure Want To Start Test ? Please Confirm ")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:
               self.label_22.show()
               self.sc_new =PlotCanvas_Auto(self,width=5, height=4, dpi=80)
               self.gridLayout.addWidget(self.sc_new, 1, 0, 1, 1)                
               connection = sqlite3.connect("mdr.db")
               results=connection.execute("SELECT COUNT(*) FROM STG_GRAPH_MST")
               rows=results.fetchall()
               connection.close()
               if(int(rows[0][0]) > -2 ):
                    self.timer3.setInterval(1000)        
                    self.timer3.timeout.connect(self.show_load_cell_val)
                    self.timer3.start(1)
                
        else:
                print("validation Error")
    
    def stop_test_MDR(self):
        close = QMessageBox()
        close.setText("Are You Sure Want To Stop Test ? Please Confirm ")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:  
               
               print("Stop Test Here")
                
        else:
                print("validation Error")
    
    
    def show_load_cell_val(self):      
        
        self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q)))        
        self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))   #length
        self.label_33.setText(str(int(max(self.sc_new.arr_p))))
        self.lcdNumber_3.setProperty("value",str(max(self.sc_new.arr_r)))
        
        #self.max_time_mm=int((x[2]))
        if(int(self.max_time_mm) > int(self.label_33.text())):
             self.test_per=((int(self.max_time_mm) -  int(self.label_33.text()) )/int(self.max_time_mm)) *100
             
        else:
             self.test_per=100
        self.label_50.setText("Test Started..."+str(int(self.test_per))+"  % ")
        
        self.label_50.show()
        #self.label_50.setText(" Test Started  ..... %")
        if(str(self.sc_new.save_data_flg) =="Yes"):            
                self.reset()
                self.save_graph_data()
                self.sc_new.save_data_flg=""
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q)))        
                self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))   #length
                self.label_33.setText(str(int(max(self.sc_new.arr_p))))
                self.lcdNumber_3.setProperty("value",str(int(max(self.sc_new.arr_r)))) 
                
                
    def reset(self):        
        if(self.timer3.isActive()): 
           self.timer3.stop() 
        
        #self.sc_blank =PlotCanvas_blank(self) 
        #self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.label_33.setText("0")
        
    def save_graph_data(self):         
         if (len(self.sc_new.arr_p) > 1):            
            
            #self.cycle_num=int(str(self.label_67.text()))+1
            
            connection = sqlite3.connect("mdr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)):                     
                        cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM,R_NUM) VALUES ('"+str(float(self.sc_new.arr_p[g]))+"','"+str(float(self.sc_new.arr_q[g]))+"','"+str(float(self.sc_new.arr_r[g]))+"')")
            connection.commit();
            connection.close()
            
            #self.get_points()
            #self.cycle_num=self.cycle_num+1
            connection = sqlite3.connect("mdr.db")              
            with connection:        
                  cursor = connection.cursor()
                  #print("ok1")
                  try:
                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_TORQUE='"+str(self.label_18.text())+"',SPECIMEN_NAME_ID='"+str(self.label_12.text())+"',BATCH_ID='"+str(self.lineEdit_3.text())+"',TEST_TEMP='"+str(self.label_23.text())+"',METHOD_NAME='"+str(self.comboBox.currentText())+"',TEST_TIME_MM='"+str(self.label_26.text())+"',OPERATOR='"+str(self.lineEdit_4.text())+"',SHIFT='"+str(self.comboBox_2.currentText())+"'")                         
                          cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM,R_NUM) SELECT X_NUM,Y_NUM,R_NUM FROM STG_GRAPH_MST")
                          cursor.execute("UPDATE GLOBAL_VAR SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST)")
                          cursor.execute("UPDATE GRAPH_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")
                          cursor.execute("INSERT INTO TEST_MST_MDR(SPECIMEN_NUM,BATCH_ID,TEST_TEMP,METHOD_NAME,TRQ,TEST_TIME_MIN,GRAPH_ID,OPERATOR,SHIFT) SELECT SPECIMEN_NAME_ID,BATCH_ID,TEST_TEMP,METHOD_NAME,TEST_TORQUE,TEST_TIME_MM,GRAPH_ID ,OPERATOR,SHIFT FROM GLOBAL_VAR")
                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID = (SELECT MAX(TEST_ID) FROM TEST_MST_MDR)")
                          cursor.execute("UPDATE TEST_MST_MDR SET STATUS='LOADED GRAPH'  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")                  
                          cursor.execute("UPDATE TEST_MST_MDR SET GRAPH_SCAL_X_LENGTH=(SELECT GRAPH_SCALE_CELL_2 FROM SETTING_MST),GRAPH_SCAL_Y_LOAD=(SELECT GRAPH_SCALE_CELL_1 FROM SETTING_MST)  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                     
                          self.label_22.show()
                          self.label_22.setText("Data Saved.")
                
                  except e:
                          print("SQL Error"+str(e))
                          self.label_22.show()
                          self.label_22.setText("SQL Error.")
            #self.calculations()         
            connection.commit();
            connection.close()            
            print("Data Saved Ok in STG_GRAPH_MST")
            self.show_grid_data_MDR()
            self.pushButton_11_1.setEnabled(True)
        
    def show_grid_data_MDR(self):        
        #print("inside tear list.....")
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(19)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setHorizontalHeaderLabels(['Test Id','Spec.No.','S_ML','S_MH','S2_ML','S2_MH','T_S1','T_S2','T_S5','TC_10','TC_50','TC_90','Tan at ML','Tan at MH','OC','CR','End Temp.','Trend','RT'])  
              
        self.tableWidget.setColumnWidth(0, 170)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 170)
        self.tableWidget.setColumnWidth(7, 120)
        self.tableWidget.setColumnWidth(8, 150)
        self.tableWidget.setColumnWidth(9, 150)
        self.tableWidget.setColumnWidth(10, 150)
        self.tableWidget.setColumnWidth(11, 150)
        self.tableWidget.setColumnWidth(12, 170)
        self.tableWidget.setColumnWidth(13, 120)
        self.tableWidget.setColumnWidth(14, 150)
        self.tableWidget.setColumnWidth(15, 150)
        self.tableWidget.setColumnWidth(16, 150)
        self.tableWidget.setColumnWidth(17, 150)
        self.tableWidget.setColumnWidth(18, 170)
        self.tableWidget.setColumnWidth(19, 150)
        
        
        
        connection = sqlite3.connect("mdr.db")
         
        results=connection.execute("SELECT TEST_ID,SPECIMEN_NUM,printf(\"%.2f\", S_ML),printf(\"%.2f\", S_MH),printf(\"%.2f\", S2_ML),printf(\"%.2f\", S2_MH),printf(\"%.2f\", T_S1),printf(\"%.2f\", T_S2),printf(\"%.2f\", T_S5),printf(\"%.2f\", TC_10),printf(\"%.2f\", TC_50),printf(\"%.2f\", TC_90),printf(\"%.2f\", TAN_AT_ML),printf(\"%.2f\", TAN_AT_MH),printf(\"%.2f\", OC),printf(\"%.2f\", CR),printf(\"%.2f\", END_TEMP),TREAND,printf(\"%.2f\", RT)   FROM TEST_MST_MDR WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()
    
    def show_grid_data_LIMITS(self):        
        #print("inside tear list.....")
        self.delete_all_records2()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.setHorizontalHeaderLabels(['Param','L-Limit','U-Limit'])  
              
        self.tableWidget_2.setColumnWidth(0, 170)
        self.tableWidget_2.setColumnWidth(1, 120)
        self.tableWidget_2.setColumnWidth(2, 120)
        
        connection = sqlite3.connect("mdr.db")         
        results=connection.execute("SELECT A.PARAM,printf(\"%.2f\", A.L_VAL),printf(\"%.2f\", A.U_VAL)    FROM LIMITS_MST A,METHODS_MST B WHERE A.LIMIT_ID=B.LIMIT_ID AND B.METHOD_NAME='"+str(self.comboBox.currentText())+"'")
        for row_number, row_data in enumerate(results):            
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        self.tableWidget_2.resizeColumnsToContents()
        #self.tableWidget_2.resizeRowsToContents()
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()
     
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
    
    def delete_all_records2(self):
        i = self.tableWidget_2.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget_2.removeRow(i)
    
    def open_setting(self):    
        self.window = QtWidgets.QMainWindow()
        self.ui=mdr_02_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_report(self):    
        self.window = QtWidgets.QMainWindow()
        self.ui=mdr_05_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_pdf(self):
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90) 
        self.create_pdf_mdr()
        os.system("xpdf ./reports/test_report.pdf")
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
    
    def create_pdf_mdr(self):
        self.sample_type=""
        self.remark="______________________________________________________________________________"
        y=300
        Elements=[]
        
        connection = sqlite3.connect("mdr.db")        
        results=connection.execute("SELECT METHOD_NAME,SPECIMEN_NUM,BATCH_ID,CREATED_ON,ARC,TEST_TEMP,TEST_TIME_MIN,SHIFT,COMMENTS,OPERATOR  FROM TEST_MST_MDR A where A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:                    
                    
                    self.summary_data=[["Method : ",str(x[0]),"Spec.No: ",str(x[1])],["Batch No: ",str(x[2]),"Date: ",str(x[3])],["Arc: ",str(x[4]),"Set Temp(.c):",str(x[5])]]
                    self.summary_data.append(["Test Time (min) : ",str(x[6]),"Shift: ",str(x[7])+" ( "+str(x[9])+" )"])
                    self.remark=str(x[8])
        connection.close()
        
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        
        
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("SELECT S_ML,S_MH,S2_ML,S2_MH,T_S1,T_S2,T_S5,TC_10,TC_50,TC_90,TAN_AT_ML,TAN_AT_MH,OC,CR,END_TEMP,TREAND,RT,STATUS FROM TEST_MST_MDR A where A.TEST_ID IN (SELECT IFNULL(TEST_ID,1) FROM GLOBAL_VAR)")
        for x in results:
            ptext2 = "<font name=Helvetica size=14> <b>Parameters : </b> </font>"            
            Title3 = Paragraph(str(ptext2), styles["Normal"])
               
            self.param_data=[["S` ML : ",str(x[0]),"S` MH : ",str(x[1])]]
            self.param_data.append(["S`` ML: ",str(x[2]),"S`` MH: ",str(x[3])])
            self.param_data.append(["TS1: ",str(x[4]),"TS2: ",str(x[5])])
            self.param_data.append(["TS5: ",str(x[6]),"TC10 ",str(x[7])])
            self.param_data.append(["TC50 : ",str(x[8]),"TC90: ",str(x[9])])
            self.param_data.append(["TAN AT ML: ",str(x[10]),"TAN AT MH: ",str(x[11])])
            self.param_data.append(["OC : ",str(x[12]),"CR : ",str(x[13])])
            self.param_data.append(["End. Temp.: ",str(x[14]),"Trend: ",str(x[15])])
            self.param_data.append(["RT : ",str(x[16]),"Status : ",str(x[17])])
                   
        connection.close()
        
        
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("select COMPANY_NAME,ADDRESS1 from SETTING_MST ") 
        for x in results:            
            Title = Paragraph(str(x[0]), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        
        blank=Paragraph("                                                                                          ", styles["Normal"])
        comments = Paragraph("<font name=Helvetica size=14><b>  Remark : </b></font>"+str(self.remark), styles["Normal"])        
        
        footer_2= Paragraph("<font name=Helvetica size=14><b>   Tested By: _________________                    Verified  By:_________________  </b></font>",styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
        
        #f1=Table(data)
        #f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
        
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        TS_STR = Paragraph("<font name=Helvetica size=11>"+str(self.sample_type)+" </font>", styles["Title"])
        #f2=Table(data2)
        #f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(self.summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
        f4=Table(self.param_data)
        f4.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,TS_STR,Spacer(1,12),Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),Title3,Spacer(1,12),Spacer(1,12),f4,Spacer(1,12),Spacer(1,12),Spacer(1,12),blank,blank,blank,Spacer(1,12),comments,Spacer(1,12),footer_2,Spacer(1,12),Spacer(1,12),Spacer(1,12),Spacer(1,12)]
        
        
        doc = SimpleDocTemplate('./reports/test_report.pdf', rightMargin=10,
                                leftMargin=20,
                                topMargin=10,
                                bottomMargin=10,)
        doc.build(Elements)
    


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
        ax2 = ax.twinx()
        color = 'tab:green'
        ax2.set_ylabel('TEMP (.C)', color = color)
#        ax.set_xlim(0,200)
#        ax.set_ylim(0,200)
        ax2.set_ylim(0,200)
        
        ax.grid(which='major', linestyle='-', linewidth='0.50', color='black')
        ax.grid(which='minor', linestyle=':', linewidth='0.50', color='black')
        
        self.s=[]
        self.t=[]
        self.graph_ids=[]    
        self.x_num=[0.0]
        self.y_num=[133.0]
        self.r_num=[0.0]
        self.test_type="Tensile"
        self.color=['b','r','g','y','k','c','m','b']
        #ax.set_title('Test Id=32         Samples=3       BreakLoad(Kg)=110        Length(mm)=3')         
        
        
        
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
             ax.set_xlim(0,int(x[0]))
             ax.set_ylim(0,int(x[1]))            
#             self.xlim=int(x[0])
#             self.ylim=int(x[1])            
        connection.close()
        
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("SELECT GRAPH_ID FROM TEST_MST_MDR WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
             self.graph_ids.append(x[0])             
        connection.close()
        
        
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
        
            connection = sqlite3.connect("mdr.db")               
            results=connection.execute("SELECT X_NUM,Y_NUM,R_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            for k in results:        
                self.x_num.append(k[0])
                self.y_num.append(k[1])
                self.r_num.append(k[2])
            connection.close() 
        
            if(g < 8 ):
                ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
                ax2.plot(self.x_num,self.r_num, 'g',label="Temparature")
        
        
        ax.set_xlabel('TIME (Min)')
        ax.set_ylabel('TORQUE(N)')
       
        #self.connect('motion_notify_event', mouse_move)
        ax.legend()
        #ax2.legend() 
        self.draw()
        self.figure.savefig('last_graph.png',dpi=100)
        
       




class PlotCanvas_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="MDR"
        self.axes.set_xlabel('TIME (min)')
        self.axes.set_ylabel('TORQUE (N)')
        self.axes.grid(which='major', linestyle='-', linewidth='0.50', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.50', color='black')
        
        self.axes2 = self.axes.twinx()
        color = 'tab:green'
        self.axes2.set_ylabel('TEMP (.C)', color = color)
        self.axes2.set_ylim(0,200)
        
        
        
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.q =0
        self.r =170
        
        self.arr_p=[0.0]
        self.arr_q=[133.0]
        self.arr_r=[0.0]
        self.arr_p1=[0.0]
        self.arr_q1=[0.0]
        self.x=0
        self.y=0
        #self.ax = self.figure.add_subplot(111) 
        self.xlim=0
        self.ylim=10
        self.line_cnt=0
        self.line_cnt2=0
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
        #self.line_cnt2, = self.axes2.plot([0,0], [0,0], lw=2)
        connection = sqlite3.connect("mdr.db")              
        with connection:        
                cursor = connection.cursor()                            
                cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
        connection.commit();
        connection.close()
        
        connection = sqlite3.connect("mdr.db")
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
        '''
        
        '''
        self.test_guage_mm=609
        self.max_load=0
        self.cof_max_length=100
        print("434Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
        
        
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
                
                
            #time.sleep(2)
            #========Final Motor start Command =========
            self.ser.flush()           
                
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
   
        self.x1,self.y1 = [],[]
        self.x2,self.y2 = [],[]
        self.lines = []
        lobj = self.axes.plot([],[],lw=2)[0]
        lobj2 = self.axes2.plot([],[],lw=2)[0]
        
        self.lines.append(lobj)
        self.lines.append(lobj2)
        self.on_ani_start()
        
        
    def update_graph(self):       
        if(self.IO_error_flg==0):
            '''
           
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
                self.r=170.00
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                self.arr_r.append(float(self.r))
                print(" Timer P:"+str(self.p)+" q:"+str(self.q))
                

                if(int(self.q) > int(self.ylim)):
                    self.ylim=(int(self.q)+100)
                    self.ylim_update='YES'                   
                   
                              
                if(self.p > self.xlim):
                   self.xlim=(int(self.p)+100)
                   self.xlim_update='YES'                   
                #time.sleep(1)
                self.save_data_flg="No"
            else:                
               
                self.save_data_flg="Yes"
                self.on_ani_stop()
            
                   
    def plot_grah_only(self,i):
        self.x1.append(self.p)
        self.y1.append(self.q)
        self.x2.append(self.p)
        self.y2.append(self.r)

        self.xlist = [self.x1, self.x2]
        self.ylist = [self.y1, self.y2]
        #for index in range(0,1):
        for lnum,line in enumerate(self.lines):
            line.set_data(self.xlist[lnum], self.ylist[lnum]) # set data for each line separately.
        return self.lines

        #self.line_cnt.set_data(self.arr_p,self.arr_q)       
        #return [self.line_cnt]
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
           
#    def init(self):
#        self.line_cnt.set_data([], [])
#        return self.line_cnt,



    def init(self):
        for line in self.lines:
            line.set_data([],[])
        return self.lines
   

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
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("SELECT IFNULL(MOTOR_MAX_SPEED,0) from SETTING_MST") 
        for x in results:
             self.speed_val=str(x[0])
        connection.close()
        self.goahead_flag=0
        '''
        
        '''
        self.input_speed_val=100
        if(self.input_speed_val != ""):
            if(int(self.input_speed_val) <= int(self.speed_val)):
                 #print(" Ok ")
                 self.goahead_flag=1
                 self.calc_speed=(int(self.input_speed_val)/int(self.speed_val))*1000                 
                 
                 self.command_str="*P%04d"%self.calc_speed+"_%04d"%self.break_sence+"\r"
                 print("Morot Speed and Breaking speed Command  :"+str(self.command_str))
            else:
                 print(" not Ok ")
                 
        else:
            print(" not Ok ")
            

class PlotCanvas_blank(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=80):
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
        
        connection = sqlite3.connect("mdr.db")              
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
       
         
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
             ax.set_xlim(0,int(x[0]))
             ax.set_ylim(0,int(x[1]))          
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])
        
        ax.plot(self.x,self.y,'b')
        ax.set_ylabel('TORQUE (N) ')
        ax.set_xlabel('TIME (min)')
        ax2 = ax.twinx()
        color = 'tab:green'
        ax2.set_ylabel('TEMP (.C)', color = color)
        ax2.set_ylim(0,200) 
          
        self.draw() 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MDR_01_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
