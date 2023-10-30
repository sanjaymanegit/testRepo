from GRAPH_SCALES_ALL import set_two_graphs_Ui_MainWindow
from POP_GRAPH_2_SET import pop_graph2_Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow
from email_popup_log_report import popup_email_log_Ui_MainWindow
from comment_popup_expansion import comment_Ui_MainWindow



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
import serial
import time

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


class RL_01_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 950)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1780, 880))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 830, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(150, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(130, 730, 91, 51))
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("value", 100.0)
        self.lcdNumber.setProperty("intValue", 100)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(1310, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 255, 227);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1120, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 255, 227);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(1120, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 255, 227);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(1310, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 255, 227);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_2.setGeometry(QtCore.QRect(10, 730, 91, 51))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setProperty("value", 100.0)
        self.lcdNumber_2.setProperty("intValue", 100)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_78 = QtWidgets.QLabel(self.frame)
        self.label_78.setGeometry(QtCore.QRect(10, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_78.setFont(font)
        self.label_78.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_78.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_78.setObjectName("label_78")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(150, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setGeometry(QtCore.QRect(150, 90, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_79 = QtWidgets.QLabel(self.frame)
        self.label_79.setGeometry(QtCore.QRect(10, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_79.setFont(font)
        self.label_79.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_79.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_79.setObjectName("label_79")
        self.line_18 = QtWidgets.QFrame(self.frame)
        self.line_18.setGeometry(QtCore.QRect(370, 0, 20, 141))
        self.line_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_18.setLineWidth(3)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.frame)
        self.line_19.setGeometry(QtCore.QRect(1510, 0, 20, 141))
        self.line_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_19.setLineWidth(3)
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setObjectName("line_19")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(870, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        
        
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(1230, 810, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        
        
        self.label_9_1 = QtWidgets.QLabel(self.frame)
        self.label_9_1.setGeometry(QtCore.QRect(1230, 840, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_9_1.setFont(font)
        self.label_9_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9_1.setText("Test Stand. :")
        self.label_9_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9_1.setObjectName("label_9_1")
        
        
        
        
        
        self.lineEdit_44 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_44.setGeometry(QtCore.QRect(1330, 820, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_44.setFont(font)
        self.lineEdit_44.setObjectName("lineEdit_44")
        
        self.lineEdit_44_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_44_1.setGeometry(QtCore.QRect(1330, 850, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_44_1.setFont(font)       
        self.lineEdit_44_1.setObjectName("lineEdit_44_1")
        
        
        
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 830, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_140 = QtWidgets.QLabel(self.frame)
        self.label_140.setGeometry(QtCore.QRect(510, 700, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_140.setFont(font)
        self.label_140.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_140.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_140.setObjectName("label_140")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_46.setGeometry(QtCore.QRect(510, 730, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_46.setFont(font)
        self.lineEdit_46.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.label_143 = QtWidgets.QLabel(self.frame)
        self.label_143.setGeometry(QtCore.QRect(640, 700, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_143.setFont(font)
        self.label_143.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_143.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_143.setObjectName("label_143")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_47.setGeometry(QtCore.QRect(650, 730, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_47.setFont(font)
        self.lineEdit_47.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_47.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.label_144 = QtWidgets.QLabel(self.frame)
        self.label_144.setGeometry(QtCore.QRect(790, 700, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_144.setFont(font)
        self.label_144.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_144.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_144.setObjectName("label_144")
        
        #self.lineEdit_48 = QtWidgets.QLineEdit(self.frame) #QtWidgets.QLCDNumber(self.frame)
        self.lineEdit_48 = QtWidgets.QLCDNumber(self.frame)
        self.lineEdit_48.setGeometry(QtCore.QRect(250, 730, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_48.setFont(font)
        #self.lineEdit_48.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_48.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        #self.lineEdit_48.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.label_145 = QtWidgets.QLabel(self.frame)
        self.label_145.setGeometry(QtCore.QRect(10, 700, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_145.setFont(font)
        self.label_145.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_145.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_145.setObjectName("label_145")
        self.label_146 = QtWidgets.QLabel(self.frame)
        self.label_146.setGeometry(QtCore.QRect(130, 700, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_146.setFont(font)
        self.label_146.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_146.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_146.setObjectName("label_146")
        self.label_147 = QtWidgets.QLabel(self.frame)
        self.label_147.setGeometry(QtCore.QRect(280, 700, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_147.setFont(font)
        self.label_147.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_147.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_147.setObjectName("label_147")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_51.setGeometry(QtCore.QRect(800, 730, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_51.setFont(font)
        self.lineEdit_51.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_51.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.label_148 = QtWidgets.QLabel(self.frame)
        self.label_148.setGeometry(QtCore.QRect(360, 700, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_148.setFont(font)
        self.label_148.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_148.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_148.setObjectName("label_148")
        #self.lineEdit_52 = QtWidgets.QLineEdit(self.frame) #QLCDNumber
        self.lineEdit_52 = QtWidgets.QLCDNumber(self.frame)
        self.lineEdit_52.setGeometry(QtCore.QRect(360, 730, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_52.setFont(font)
        #self.lineEdit_52.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_52.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        #self.lineEdit_52.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(910, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(1540, 20, 230, 111))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/GIG_SYS_NEWLOGO1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(200, 160))
        self.pushButton.setObjectName("pushButton")
        self.label_149 = QtWidgets.QLabel(self.frame)
        self.label_149.setGeometry(QtCore.QRect(960, 700, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_149.setFont(font)
        self.label_149.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_149.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_149.setObjectName("label_149")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_53.setGeometry(QtCore.QRect(960, 730, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_53.setFont(font)
        self.lineEdit_53.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_53.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.label_150 = QtWidgets.QLabel(self.frame)
        self.label_150.setGeometry(QtCore.QRect(40, 790, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_150.setFont(font)
        self.label_150.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_150.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_150.setObjectName("label_150")
        self.label_151 = QtWidgets.QLabel(self.frame)
        self.label_151.setGeometry(QtCore.QRect(160, 790, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_151.setFont(font)
        self.label_151.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_151.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_151.setObjectName("label_151")
        self.label_152 = QtWidgets.QLabel(self.frame)
        self.label_152.setGeometry(QtCore.QRect(270, 790, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_152.setFont(font)
        self.label_152.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_152.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_152.setObjectName("label_152")
        self.label_153 = QtWidgets.QLabel(self.frame)
        self.label_153.setGeometry(QtCore.QRect(1070, 730, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_153.setFont(font)
        self.label_153.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_153.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_153.setObjectName("label_153")
        self.label_154 = QtWidgets.QLabel(self.frame)
        self.label_154.setGeometry(QtCore.QRect(460, 730, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_154.setFont(font)
        self.label_154.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_154.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_154.setObjectName("label_154")
        self.label_155 = QtWidgets.QLabel(self.frame)
        self.label_155.setGeometry(QtCore.QRect(590, 730, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_155.setFont(font)
        self.label_155.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_155.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_155.setObjectName("label_155")
        self.label_156 = QtWidgets.QLabel(self.frame)
        self.label_156.setGeometry(QtCore.QRect(730, 730, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_156.setFont(font)
        self.label_156.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_156.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_156.setObjectName("label_156")
        self.label_157 = QtWidgets.QLabel(self.frame)
        self.label_157.setGeometry(QtCore.QRect(890, 730, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_157.setFont(font)
        self.label_157.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_157.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_157.setObjectName("label_157")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(800, 830, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        
        self.pushButton_img_logo = QtWidgets.QPushButton(self.frame)
        self.pushButton_img_logo.setGeometry(QtCore.QRect(390, 15, 210, 51))
        self.pushButton_img_logo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/logo_new_2.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_img_logo.setIcon(icon1)
        self.pushButton_img_logo.setIconSize(QtCore.QSize(200, 160))
        self.pushButton_img_logo.setObjectName("pushButton_img_logo")
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(570, 20, 290, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        
        
        
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(400, 80, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(410, 65, 371, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(1540, 810, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line_20 = QtWidgets.QFrame(self.frame)
        self.line_20.setGeometry(QtCore.QRect(820, 0, 20, 141))
        self.line_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_20.setLineWidth(3)
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setObjectName("line_20")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 130, 1851, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 510, 591, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(610, 510, 591, 171))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_2.setItem(0, 2, item)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_3.setGeometry(QtCore.QRect(1210, 510, 551, 171))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget_3.setItem(0, 2, item)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(200, 160, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setGeometry(QtCore.QRect(800, 160, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setGeometry(QtCore.QRect(1360, 160, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame)
        self.pushButton_20.setGeometry(QtCore.QRect(410, 830, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 200, 1730, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 0, 1, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout.addWidget(self.graphicsView_3, 0, 2, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.frame)
        self.pushButton_21.setGeometry(QtCore.QRect(1220, 720, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame)
        self.pushButton_22.setGeometry(QtCore.QRect(1350, 720, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(1320, 780, 331, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(1210, 780, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame)
        self.pushButton_23.setGeometry(QtCore.QRect(600, 830, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_23.setObjectName("pushButton_23")
        
        
        self.pushButton_23_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_23_1.setGeometry(QtCore.QRect(600, 830, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23_1.setFont(font)
        self.pushButton_23_1.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_23_1.setObjectName("pushButton_23_1")
        
        
        
        self.pushButton_24 = QtWidgets.QPushButton(self.frame)
        self.pushButton_24.setGeometry(QtCore.QRect(1540, 720, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_24.setObjectName("pushButton_24")
        
        
        
        
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.goAhead="Yes"
        self.test_id_exist="No"
        self.timer3=QtCore.QTimer()
        self.timer4=QtCore.QTimer()
        self.timer5=QtCore.QTimer()
        self.timer6=QtCore.QTimer()
        self.sc_blank=""
        self.cycle_num=0
        self.x_unit='mm'
        self.y_unit='N'
        self.start_test_by="load"  #### This status is "load" Or "elongation"
        self.status_str=""
        self.graph_type="STRESS_VS_STRAIN"
        self.graph_group_no=1
        
        self.rev_arr=[]
        self.rev_arr2=[]
        self.rev_arr3=[]
        self.rev_arr4=[]
        self.rev_arr5=[]
        self.rev_arr6=[]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Start Logging"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "001"))
        self.pushButton_5.setText(_translate("MainWindow", "Email"))
        self.pushButton_5.hide()
        self.pushButton_6.setText(_translate("MainWindow", "Remark"))
        self.pushButton_7.setText(_translate("MainWindow", "Report View"))
        self.pushButton_8.setText(_translate("MainWindow", "Report Print"))
        self.label_78.setText(_translate("MainWindow", "Sample Pipe No:"))
        self.lineEdit_16.setText(_translate("MainWindow", "H22079627"))
        self.lineEdit_17.setText(_translate("MainWindow", "TEST-05"))
        self.label_79.setText(_translate("MainWindow", "Sample Identification:"))
        self.pushButton_16.setText(_translate("MainWindow", "Set Graphs Scales"))
        self.label_9.setText(_translate("MainWindow", "Reviewd  By :"))
        self.lineEdit_44.setText(_translate("MainWindow", "Dr.John"))
        self.pushButton_9.setText(_translate("MainWindow", "Stop Logging"))
        self.label_140.setText(_translate("MainWindow", "Diameter:"))
        self.lineEdit_46.setText(_translate("MainWindow", "0"))
        self.label_143.setText(_translate("MainWindow", "Thickness (mm):"))
        self.lineEdit_47.setText(_translate("MainWindow", "0"))
        self.label_144.setText(_translate("MainWindow", "Circumference (mm):"))
        #self.lineEdit_48.setText(_translate("MainWindow", "0")) #
        self.lineEdit_48.setProperty("Value",0.0)
        self.label_145.setText(_translate("MainWindow", "Pressure :"))
        self.label_146.setText(_translate("MainWindow", "Expansion :"))
        self.label_147.setText(_translate("MainWindow", "Stress :"))
        self.lineEdit_51.setText(_translate("MainWindow", "0"))
        self.label_148.setText(_translate("MainWindow", "Strain :"))
        #self.lineEdit_52.setText(_translate("MainWindow", "0"))
        self.lineEdit_52.setProperty("Value",0.0)
        self.pushButton_15.setText(_translate("MainWindow", "Return"))
        self.label_149.setText(_translate("MainWindow", "Elapsed Time:"))
        self.lineEdit_53.setText(_translate("MainWindow", "00:00:00"))
        self.label_150.setText(_translate("MainWindow", " (MPa) "))
        self.label_151.setText(_translate("MainWindow", " (mm) "))
        self.label_152.setText(_translate("MainWindow", "(MPa) "))
        self.label_153.setText(_translate("MainWindow", "HH:MI:SS"))
        self.label_154.setText(_translate("MainWindow", "(%) "))
        self.label_155.setText(_translate("MainWindow", " (mm)"))
        self.label_156.setText(_translate("MainWindow", " (mm)"))
        self.label_157.setText(_translate("MainWindow", " (mm)"))
        self.label_15.setText(_translate("MainWindow", ""))
        self.label.setText(_translate("MainWindow", "Company Name Pvt. Ltd"))
        self.label_2.setText(_translate("MainWindow", "Blue Star IT PArk ,\n"
"  MIDC , Thane ,  Mumbai Andhrei  Pin No 400232"))
        self.label_3.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Trend"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Timestamp"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Trend"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Timestamp"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)

        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Trend"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Timestamp"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)

        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.pushButton_17.setText(_translate("MainWindow", "Pressure Vs  Time"))
        self.pushButton_18.setText(_translate("MainWindow", "Pressure Vs Expansion"))
        self.pushButton_19.setText(_translate("MainWindow", "Stress Vs Strain"))
        self.pushButton_20.setText(_translate("MainWindow", "View Log"))
        self.pushButton_21.setText(_translate("MainWindow", "Graph set -1"))
        self.pushButton_21.hide()
        self.pushButton_22.setText(_translate("MainWindow", "Graph set -2"))
        self.pushButton_22.hide()
        self.comboBox.setItemText(0, _translate("MainWindow", "Pressure Vs Time"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Expansion Vs Time"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Stress Vs Time"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Strain Vs Time"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Stress Vs Strain"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Pressure Vs Expansion"))
        
        
        self.label_4.setText(_translate("MainWindow", "Report Graph :"))
        self.pushButton_23.setText(_translate("MainWindow", "Email Log"))
        self.pushButton_23.hide()
        self.pushButton_23_1.setText(_translate("MainWindow", "Set Zero"))
        self.pushButton_24.setText(_translate("MainWindow", "Reset Graph"))
        self.pushButton_24.hide()
        self.pushButton_15.clicked.connect(MainWindow.close)
        self.pushButton_9.setDisabled(True)
        self.pushButton_20.setDisabled(True)
        self.pushButton_21.setDisabled(True)
        #self.pushButton_4.setDisabled(True)
        self.pushButton_23.setDisabled(True)
        
        self.display_bank_graphs()
        self.load_ops()

    def load_ops(self):
        
        self.pushButton_4.clicked.connect(self.start_test_1_or_2)
        self.pushButton_9.clicked.connect(self.mannual_stop)
        
        self.pushButton_16.clicked.connect(self.pop_graph_scales)
        
        
        self.pushButton_5.clicked.connect(self.open_email_report)    
        self.pushButton_7.clicked.connect(self.open_pdf)
        self.pushButton_20.clicked.connect(self.open_log_pdf)
        self.pushButton_23.clicked.connect(self.open_log_email)
        self.pushButton_23_1.clicked.connect(self.set_zero)
        
        self.pushButton_6.clicked.connect(self.open_comment_popup)
        self.pushButton_8.clicked.connect(self.print_file)
        #self.pushButton_18.clicked.connect(self.graph_type_strain)
        #self.pushButton_17.clicked.connect(self.graph_type_pressure)
        #self.pushButton_20.clicked.connect(self.show_grid1_val_P0)
        #self.pushButton_21.clicked.connect(self.graph_group1_onclick)
        #self.pushButton_22.clicked.connect(self.open_pop_graph2)
        #self.pushButton_24.clicked.connect(self.reset_graph_onclick)
        self.comboBox.currentTextChanged.connect(self.update_graph_type)
        
        
       
        
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        
        
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
       
        self.load_data()
        #self.graph_type_pressure()
    
    
    def set_zero(self):
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lineEdit_48.setProperty("value", 0.0)
        self.lineEdit_52.setProperty("value", 0.0)
        self.label_15.setText("Set Zero Done.")
        #self.pushButton_21.show()
        self.pushButton_15.setEnabled(True)
        
    def start_test_1_or_2(self):
        if(self.graph_group_no==1):
                self.start_test_expansion()
        elif(self.graph_group_no==2):
                self.start2_test_expansion()
        else:
                print("invalid Graph group")
        self.pushButton_4.setDisabled(True)
        self.pushButton_15.setDisabled(True)        
                
    def graph_group2_onclick(self):
        self.graph_group_no=2
        #self.pushButton_22.setDisabled(True)
        self.pushButton_21.setEnabled(True)
        self.display_bank_graphs2()
        self.pushButton_17.setText("Pressure Vs  Expansion")
        self.pushButton_18.setText("Stress Vs Strain")
        self.pushButton_19.setText("Stress Vs Time")
        self.label_15.setText("Graph-set2 selected.")
        self.pushButton_4.setEnabled(True)
        
    
    def graph_group1_onclick(self):
        self.graph_group_no=1
        self.pushButton_21.setDisabled(True)
        #self.pushButton_22.setEnabled(True)
        self.display_bank_graphs()
        self.pushButton_17.setText("Pressure Vs  Time")
        self.pushButton_18.setText("Expansion Vs Time")
        self.pushButton_19.setText("Strain Vs Time")
        self.label_15.setText("Graph-set1 selected.")
        self.pushButton_4.setEnabled(True)
     

    def reset_graph_onclick(self):
        self.pushButton_4.setDisabled(True)
        self.pushButton_20.setDisabled(True)
        self.pushButton_23.setDisabled(True)
        self.label_15.setText("<font color=red> Please select the graph -Sets </font>")
        self.pushButton_21.show()
        self.pushButton_22.show()
        self.pushButton_21.setEnabled(True)
        #self.pushButton_22.setEnabled(True)
        
        
        

    def display_bank_graphs(self):
        self.sc_blank =PlotCanvas_blank(self,width=5, height=4, dpi=80)          
        self.gridLayout.addWidget(self.sc_blank, 0, 0, 1, 1)
        
        self.sc_blank_p1 =PlotCanvas_blank_P1(self,width=5, height=4, dpi=80)
        self.gridLayout.addWidget(self.sc_blank_p1, 0, 1, 1, 1)
        
        
        self.sc_blank_p2 =PlotCanvas_blank_P2(self,width=5, height=4, dpi=80)
        self.gridLayout.addWidget(self.sc_blank_p2, 0, 2, 1, 1)
        
    
    def display_bank_graphs2(self):
        self.sc_blank =PlotCanvasG2_blank(self,width=5, height=4, dpi=80)          
        self.gridLayout.addWidget(self.sc_blank, 0, 0, 1, 1)
        
        self.sc_blank_p1 =PlotCanvasG2_blank_P1(self,width=5, height=4, dpi=80)
        self.gridLayout.addWidget(self.sc_blank_p1, 0, 1, 1, 1)
        
        
        self.sc_blank_p2 =PlotCanvasG2_blank_P2(self,width=5, height=4, dpi=80)
        self.gridLayout.addWidget(self.sc_blank_p2, 0, 2, 1, 1)
        
    def load_data(self):
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'TEST_MST_EXPANSION'")       
        for x in results:           
                 self.label_12.setText(str(x[0]).zfill(3))
                 self.test_id=str(x[0])                 
        connection.close()
        
        
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select SAMPLE_PIPE_NO,SAMPLE_ID,REVIEWED_BY,D_AV,T_AV,CIRCUMFARANCE FROM TEST_MST_TMP")                 
        for x in results:                    
                    self.lineEdit_16.setText(str(x[0])) #SAMPLE_PIPE_NO,
                    self.lineEdit_17.setText(str(x[1])) #SAMPLE_ID
                    self.lineEdit_44.setText(str(x[2]))
                    self.lineEdit_46.setText(str(x[3])) #D_AV                    
                    self.lineEdit_47.setText(str(x[4]))#T_AV
                    self.lineEdit_51.setText(str(x[5]))#CIRCUMFARANCE

              
        connection.close()
        
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select COMPANY_NAME,ADDRESS1 from SETTING_MST ") 
        for x in results:
                self.label.setText(str(x[0]))
                self.label_2.setText(str(x[1]))
            
        connection.close()
        
    def disable_all(self):
        self.pushButton_20.setDisabled(True);
        self.pushButton_5.setDisabled(True);
        self.pushButton_6.setDisabled(True);
        self.pushButton_7.setDisabled(True);
        self.pushButton_8.setDisabled(True);
        self.lineEdit_46.setReadOnly(True) #D_AV                    
        self.lineEdit_47.setReadOnly(True) #T_AV
        self.lineEdit_51.setReadOnly(True)#CI
        
    
    def enable_all(self):
        self.pushButton_20.setEnabled(True);
        self.pushButton_5.setEnabled(True);
        self.pushButton_6.setEnabled(True);
        self.pushButton_7.setEnabled(True);
        self.pushButton_8.setEnabled(True);
        self.lineEdit_46.setReadOnly(False) #D_AV                    
        self.lineEdit_47.setReadOnly(False) #T_AV
        self.lineEdit_51.setReadOnly(False)#CI
        
                
    def start_test_expansion(self):
        self.pushButton_21.show()
        #self.pushButton_22.hide()
        self.pushButton_21.setDisabled(True)
        self.validation() 
        self.disable_all()
        self.pushButton_9.setEnabled(True)
        connection = sqlite3.connect("tyr.db")              
        with connection:
                            cursor = connection.cursor()                  
                            cursor.execute("UPDATE GLOBAL_VAR SET D_AV='"+str(self.lineEdit_46.text())+"',T_AV='"+str(self.lineEdit_47.text())+"',NEW_TEST_GUAGE_MM='"+str(self.lineEdit_51.text())+"'")
                            cursor.execute("DELETE FROM STG_GRAPH_MST ")  
        connection.commit();
        connection.close();        
        if(self.goAhead=="Yes"):              
                        #time.sleep(2)
                        self.sc_new =PlotCanvas_Auto(self,width=5, height=4, dpi=80)
                        self.gridLayout.addWidget(self.sc_new, 0, 0, 1, 1)
                        
                        self.sc_new_P1 =PlotCanvas_Auto_P1(self,width=5, height=4, dpi=80)
                        self.gridLayout.addWidget(self.sc_new_P1, 0, 1, 1, 1)
                        
                        self.sc_new_P2 =PlotCanvas_Auto_P2(self,width=5, height=4, dpi=80)
                        self.gridLayout.addWidget(self.sc_new_P2, 0, 2, 1, 1)
                        time.sleep(4)
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT COUNT(*) FROM STG_GRAPH_MST")
                        rows=results.fetchall()
                        connection.close()
                        if(int(rows[0][0]) > -2 ):
                                        self.timer3.setInterval(1000)        
                                        self.timer3.timeout.connect(self.show_load_cell_val)
                                        #time.sleep(2)
                                        
                                        self.timer3.timeout.connect(self.show_grid1_val_P1)
                                        self.timer3.timeout.connect(self.show_grid1_val_P2)
                                        self.timer3.timeout.connect(self.show_grid1_val_P0)
                                        self.timer3.start(1)
                                        
                                        
                                        #self.timer4.setInterval(1000)        
                                        #self.timer3.timeout.connect(self.show_load_cell_val)
                                        #self.timer4.timeout.connect(self.show_grid1_val_P0)
                                        #self.timer3.timeout.connect(self.show_grid1_val_P1)
                                        #self.timer3.timeout.connect(self.show_grid1_val_P2)
                                        #self.timer4.start(1)
                                        
                                        
                                        '''
                                        
                                        '''
        else:            
                    print("validation Error")
        
    def show_grid1_val_P0(self):        
        self.rev_arr3=[]
        self.rev_arr4=[]
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)      
        self.tableWidget.setHorizontalHeaderLabels(['Parameter','Value','Time (sec)'] )
        #self.z=[123.00,344.4,24.5,45.77,34,565]
       
        self.rev_arr3=self.sc_new.arr_q
        self.rev_arr4=self.sc_new.arr_t
        self.rev_arr3.reverse()
        self.rev_arr4.reverse()
        #i=i+1
        if(len(self.rev_arr3) > 0):            
                for i in range(len(self.rev_arr3)):
                        self.tableWidget.insertRow(i)
                        item = QtWidgets.QTableWidgetItem()        
                        item.setText(str("Pressure"))
                        self.tableWidget.setItem(i,0,item) 
                        item2 = QtWidgets.QTableWidgetItem()        
                        item2.setText(str(self.rev_arr3[i]))
                        self.tableWidget.setItem(i,1,item2)
                        item3 = QtWidgets.QTableWidgetItem()        
                        item3.setText(str(self.rev_arr4[i]))
                        self.tableWidget.setItem(i,2,item3)
                        #print("OK OK1 :"+str(len(self.rev_arr3)))
                
                
            
        self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
        
    
    
    def show_grid1_val_P1(self):
        
        self.rev_arr=[]
        self.rev_arr2=[]
        self.delete2_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_2.setFont(font) 
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)      
        self.tableWidget_2.setHorizontalHeaderLabels(['Parameter','Value','Pressure'] )
        #self.z=[123.00,344.4,24.5,45.77,34,565]
       
        self.rev_arr=self.sc_new_P1.arr_p
        self.rev_arr2=self.sc_new_P1.arr_q
        self.rev_arr.reverse()
        self.rev_arr2.reverse()
        if(len(self.rev_arr) > 0):
            for i in range(len(self.rev_arr)):
                        self.tableWidget_2.insertRow(i)
                        item4 = QtWidgets.QTableWidgetItem()        
                        item4.setText(str("Expansion"))
                        self.tableWidget_2.setItem(i,0,item4) 
                        item5 = QtWidgets.QTableWidgetItem()        
                        item5.setText(str(round(self.rev_arr[i],2)))
                        self.tableWidget_2.setItem(i,1,item5)
                        item6 = QtWidgets.QTableWidgetItem()        
                        item6.setText(str(self.rev_arr2[i]))
                        self.tableWidget_2.setItem(i,2,item6) 
                
                
        #self.tableWidget.setItem(2,1,str('Param-value2')) 
        #self.tableWidget.setItem(3,1,str('Param-value2'))         
        '''
       
        '''        
        self.tableWidget_2.resizeColumnsToContents()
        #self.tableWidget_2.resizeRowsToContents()
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
    def show_grid1_val_P2(self):
        
        self.rev_arr5=[]
        self.rev_arr6=[]
        self.delete3_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_3.setFont(font) 
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)      
        self.tableWidget_3.setHorizontalHeaderLabels(['Parameter','Value','Strain(%)'] )
        #self.z=[123.00,344.4,24.5,45.77,34,565]
        #self.rev_arr5=[]
        #self.rev_arr6=[]
        self.rev_arr5=self.sc_new_P2.arr_q_mpa
        self.rev_arr6=self.sc_new_P2.arr_p_strain
        #print("length-rev_arr5 :"+str(len(self.rev_arr5))+"  length-rev_arr6 :"+str(len(self.rev_arr6)))
        self.rev_arr5.reverse()
        self.rev_arr6.reverse()
        if(len(self.rev_arr5) > 0):
                for i in range(len(self.rev_arr5)):
                        self.tableWidget_3.insertRow(i)
                        item7 = QtWidgets.QTableWidgetItem()        
                        item7.setText(str("Stress"))
                        self.tableWidget_3.setItem(i,0,item7) 
                        item8 = QtWidgets.QTableWidgetItem()        
                        item8.setText(str(round(self.rev_arr5[i],2)))
                        self.tableWidget_3.setItem(i,1,item8)
                        item9 = QtWidgets.QTableWidgetItem()        
                        item9.setText(str(self.rev_arr6[i]))
                        self.tableWidget_3.setItem(i,2,item9) 
                       # print("length-rev_arr5 :"+str(len(self.rev_arr5))+"  length-rev_arr6 :"+str(len(self.rev_arr6)))
                
        #self.tableWidget.setItem(2,1,str('Param-value2')) 
        #self.tableWidget.setItem(3,1,str('Param-value2'))         
        '''
       
        '''        
        self.tableWidget_3.resizeColumnsToContents()
        #self.tableWidget_3.resizeRowsToContents()
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
  
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
    
    def delete2_all_records(self):
        i = self.tableWidget_2.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget_2.removeRow(i) 
        
    def delete3_all_records(self):
        i = self.tableWidget_3.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget_3.removeRow(i)   

        
    def start2_test_expansion(self):
        print("Group2 started")
        self.pushButton_21.hide()
        self.pushButton_22.show()
        #self.pushButton_22.setDisabled(True)
    
        self.validation() 
        self.disable_all()
        self.pushButton_9.setEnabled(True)
        connection = sqlite3.connect("tyr.db")              
        with connection:
                            cursor = connection.cursor()                  
                            cursor.execute("UPDATE GLOBAL_VAR SET D_AV='"+str(self.lineEdit_46.text())+"',T_AV='"+str(self.lineEdit_47.text())+"',NEW_TEST_GUAGE_MM='"+str(self.lineEdit_51.text())+"'")
                            cursor.execute("DELETE FROM STG_GRAPH_MST ")  
        connection.commit();
        connection.close();        
        if(self.goAhead=="Yes"):              
                        
                        self.sc_new =PlotCanvasG2_Auto(self,width=5, height=4, dpi=80)
                        self.gridLayout.addWidget(self.sc_new, 0, 0, 1, 1)
                        
                        self.sc_new_P1 =PlotCanvasG2_Auto_P1(self,width=5, height=4, dpi=80)
                        self.gridLayout.addWidget(self.sc_new_P1, 0, 1, 1, 1)
                        
                        self.sc_new_P2 =PlotCanvasG2_Auto_P2(self,width=5, height=4, dpi=80)
                        self.gridLayout.addWidget(self.sc_new_P2, 0, 2, 1, 1)
                        
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT COUNT(*) FROM STG_GRAPH_MST")
                        rows=results.fetchall()
                        connection.close()
                        if(int(rows[0][0]) > -2 ):
                                        self.timer3.setInterval(1000)        
                                        self.timer3.timeout.connect(self.show_load_cell_val)
                                        self.timer3.timeout.connect(self.show_grid1_val_P3)
                                        self.timer3.timeout.connect(self.show_grid1_val_P4)
                                        self.timer3.timeout.connect(self.show_grid1_val_P5)
                                        self.timer3.start(1)
                                        
        else:            
                    print("validation Error") 


                    
                    
    def show_grid1_val_P3(self):        
        self.rev_arr3=[]        
        self.rev_arr4=[]
        self.delete3x_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)      
        self.tableWidget.setHorizontalHeaderLabels(['Parameter','Pressure(MPa)','Expansion (mm)'] )
        #self.z=[123.00,344.4,24.5,45.77,34,565]
       
        self.rev_arr3=self.sc_new.arr_q
        self.rev_arr4=self.sc_new.arr_p
        self.rev_arr3.reverse()
        self.rev_arr4.reverse()
        if(len(self.rev_arr3) > 0):
              for i in range(len(self.rev_arr3)):
                        self.tableWidget.insertRow(i)
                        item = QtWidgets.QTableWidgetItem()        
                        item.setText(str("Pressure vs Expansion"))
                        self.tableWidget.setItem(i,0,item) 
                        item2 = QtWidgets.QTableWidgetItem()        
                        item2.setText(str(self.rev_arr3[i]))
                        self.tableWidget.setItem(i,1,item2)
                        item3 = QtWidgets.QTableWidgetItem()        
                        item3.setText(str(self.rev_arr4[i]))
                        self.tableWidget.setItem(i,2,item3) 
                
                
               
        self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
    def show_grid1_val_P4(self):
        
        self.rev_arr=[]
        self.rev_arr2=[]
        self.delete4_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_2.setFont(font) 
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)      
        self.tableWidget_2.setHorizontalHeaderLabels(['Parameter','Stress(MPa)','Strain (%)'] )
        #self.z=[123.00,344.4,24.5,45.77,34,565]
       
        self.rev_arr=self.sc_new_P1.arr_q_mpa
        self.rev_arr2=self.sc_new_P1.arr_p_strain
        self.rev_arr.reverse()
        self.rev_arr2.reverse()
        if(len(self.rev_arr) > 0):
                for i in range(len(self.rev_arr)):
                        self.tableWidget_2.insertRow(i)
                        item4 = QtWidgets.QTableWidgetItem()        
                        item4.setText(str("Stress Vs Strain"))
                        self.tableWidget_2.setItem(i,0,item4) 
                        item5 = QtWidgets.QTableWidgetItem()        
                        item5.setText(str(self.rev_arr[i]))
                        self.tableWidget_2.setItem(i,1,item5)
                        item6 = QtWidgets.QTableWidgetItem()        
                        item6.setText(str(self.rev_arr2[i]))
                        self.tableWidget_2.setItem(i,2,item6) 
                
                
              
        self.tableWidget_2.resizeColumnsToContents()
        #self.tableWidget_2.resizeRowsToContents()
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            
            
    def show_grid1_val_P5(self):        
        self.rev_arr5=[]
        self.rev_arr6=[]
        self.delete5_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_3.setFont(font) 
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)      
        self.tableWidget_3.setHorizontalHeaderLabels(['Parameter','Stress(MPa)','Time (sec)'] )
        #self.z=[123.00,344.4,24.5,45.77,34,565]
       
        self.rev_arr5=self.sc_new_P2.arr_q_mpa
        self.rev_arr6=self.sc_new_P2.arr_t
        self.rev_arr5.reverse()
        self.rev_arr6.reverse()
        if(len(self.rev_arr5) > 0):
                for i in range(len(self.rev_arr6)):
                        self.tableWidget_3.insertRow(i)
                        item7 = QtWidgets.QTableWidgetItem()        
                        item7.setText(str("Stress Vs Time"))
                        self.tableWidget_3.setItem(i,0,item7) 
                        item8 = QtWidgets.QTableWidgetItem()        
                        item8.setText(str(self.rev_arr5[i]))
                        self.tableWidget_3.setItem(i,1,item8)
                        item9 = QtWidgets.QTableWidgetItem()        
                        item9.setText(str(self.rev_arr6[i]))
                        self.tableWidget_3.setItem(i,2,item9) 
                       
        self.tableWidget_3.resizeColumnsToContents()
        #self.tableWidget_3.resizeRowsToContents()
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
  
    
    def delete3x_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
    
    def delete4_all_records(self):
        i = self.tableWidget_2.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget_2.removeRow(i) 
        
    def delete5_all_records(self):
        i = self.tableWidget_3.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget_3.removeRow(i)       
            
    ################### End Start Group 2 ######################


            
    def validation(self):
        self.goAhead="No"
        if(self.lineEdit_46.text() == ""): #    
                    self.label_15.show()
                    self.label_15.setText(" Dia. Should not Empty.")                    
        elif(self.lineEdit_47.text() == ""): #    
                    self.label_15.show()
                    self.label_15.setText("Thickness Should not Empty.")               
        elif(self.lineEdit_51.text() == ""): #    
                    self.label_15.show()
                    self.label_15.setText("Circumference Should not Empty. ")
        elif(self.lineEdit_16.text() == ""): #    
                    self.label_15.show()
                    self.label_15.setText("Sample Pipe No Should not Empty .")
        elif(self.lineEdit_17.text() == ""): #    
                    self.label_15.show()
                    self.label_15.setText("Sample Id Should not Empty .")
        else:
               self.goAhead="Yes"
               connection = sqlite3.connect("tyr.db")
               print("select count(*) from TEST_MST_EXPANSION WHERE TEST_ID = '"+str(int(self.label_12.text()))+"'")       
               
               results=connection.execute("select count(*) from TEST_MST_EXPANSION WHERE TEST_ID = '"+str(int(self.label_12.text()))+"'")       
               for x in results:           
                 if(int(x[0]) > 0):
                       self.test_id_exist="Yes"
                 else:
                       self.test_id_exist="No"                     
               connection.close() 
               print("self.test_id_exist:"+str(self.test_id_exist))
               if(self.test_id_exist=="Yes"):
                   ### Update global var
                        connection = sqlite3.connect("tyr.db")              
                        with connection:
                            cursor = connection.cursor()                  
                            cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(int(self.label_12.text()))+"'")
                           
                            try:
                                    cursor.execute("UPDATE  TEST_MST_TMP SET TEST_ID="+str(int(self.label_12.text()))+
                                                    ", SAMPLE_PIPE_NO='"+str(self.lineEdit_16.text())+
                                                    "', SAMPLE_ID='"+str(self.lineEdit_17.text())+                                                   
                                                    "', D_AV='"+str(self.lineEdit_46.text())+
                                                    "', T_AV='"+str(self.lineEdit_47.text())+
                                                    "', CIRCUMFARANCE='"+str(self.lineEdit_51.text())+
                                                    "', REVIEWED_BY='"+str(self.lineEdit_44.text())+                                                   
                                                    "', GRAPH_TYPE='"+str(self.graph_type)+
                                                    "' ")

                            except Exception as e:
                                              print("UPDATE SQL Error-TEST_MST_TMP No- 1:"+str(e))
                                              connection.commit();
                            cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_AREA=( SELECT  (SAMPLE_WIDTH_MM * T_AV)*0.1*0.1 FROM TEST_MST_TMP)")
                                              
                            try:
                                    cursor.execute("UPDATE  TEST_MST_EXPANSION SET TEST_ID="+str(int(self.label_12.text()))+
                                                   " ,SAMPLE_PIPE_NO='"+str(self.lineEdit_16.text())+
                                                    "', SAMPLE_ID='"+str(self.lineEdit_17.text())+                                                   
                                                    "', D_AV='"+str(self.lineEdit_46.text())+
                                                    "', T_AV='"+str(self.lineEdit_47.text())+
                                                    "', CIRCUMFARANCE='"+str(self.lineEdit_51.text())+
                                                    "', REVIEWED_BY='"+str(self.lineEdit_44.text())+
                                                   # "', TEST_DATE='"+str(self.label_18.text())+
                                                    "', GRAPH_TYPE='"+str(self.graph_type)+                                                    
                                                    "' WHERE TEST_ID='"+str(int(self.label_12.text()))+"'")

                            except Exception as e:
                                              print("UPDATE SQL Error-TEST_MST_EXPANSION No- 3:"+str(e))
                                              connection.commit();
                        connection.commit();
                        connection.close()                        
               else:        
                        ### INSERT 
                        connection = sqlite3.connect("tyr.db")              
                        with connection:        
                              cursor = connection.cursor()                  
                              cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(int(self.label_12.text()))+"'")
                              try:     
                                      
                                      print("INSERT INTO TEST_MST_EXPANSION (TEST_ID,SAMPLE_PIPE_NO,SAMPLE_ID,D_AV,T_AV,CIRCUMFARANCE, REVIEWED_BY,GRAPH_TYPE)"
                                                    "VALUES(   "+str(int(self.label_12.text()))+","
                                                                "'"+str(self.lineEdit_16.text())+"'," 
                                                                "'"+str(self.lineEdit_17.text())+"',"
                                                                "'"+str(self.lineEdit_46.text())+"',"                                                     
                                                                "'"+str(self.lineEdit_47.text())+"',"
                                                                "'"+str(self.lineEdit_51.text())+"',"
                                                                "'"+str(self.lineEdit_44.text())+"'," #REVIEWED_BY
                                                                "'"+self.graph_type+"')" #GRAPH_TYPE
                                                                )
                                      cursor.execute("INSERT INTO TEST_MST_EXPANSION (TEST_ID,SAMPLE_PIPE_NO,SAMPLE_ID,D_AV,T_AV,CIRCUMFARANCE, REVIEWED_BY,GRAPH_TYPE,TEST_STD)"
                                                    "VALUES(   "+str(int(self.label_12.text()))+","
                                                                "'"+str(self.lineEdit_16.text())+"'," 
                                                                "'"+str(self.lineEdit_17.text())+"',"
                                                                "'"+str(self.lineEdit_46.text())+"',"                                                     
                                                                "'"+str(self.lineEdit_47.text())+"',"
                                                                "'"+str(self.lineEdit_51.text())+"',"
                                                                "'"+str(self.lineEdit_44.text())+"'," #REVIEWED_BY
                                                                "'"+self.graph_type+"'," #GRAPH_TYPE
                                                                "'"+self.lineEdit_44_1.text()+"')" #TEST_STD
                                                                )
                                      print("inserted OK ")


                              except Exception as e:
                                              print("INSERT  SQL Error-TEST_MST_EXPANSION No- 2:"+str(e))
                                              connection.commit();

                              try:
                                    cursor.execute("UPDATE  TEST_MST_TMP SET TEST_ID="+str(int(self.label_12.text()))+
                                                   " ,SAMPLE_PIPE_NO='"+str(self.lineEdit_16.text())+
                                                    "', SAMPLE_ID='"+str(self.lineEdit_17.text())+                                                   
                                                    "', D_AV='"+str(self.lineEdit_46.text())+
                                                    "', T_AV='"+str(self.lineEdit_47.text())+
                                                    "', CIRCUMFARANCE='"+str(self.lineEdit_51.text())+
                                                    "', REVIEWED_BY='"+str(self.lineEdit_44.text())+
                                                   # "', TEST_DATE='"+str(self.label_18.text())+
                                                    "', GRAPH_TYPE='"+str(self.graph_type)+                                                    
                                                    "' ")

                                    print("updated  OK ")

                              except Exception as e:
                                              print("UPDATE SQL Error-TEST_MST_TMP No- 4:"+str(e))
                                              connection.commit();

                              cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_AREA=0  ")
                           
                        connection.commit();
                        connection.close()
                        
    def mannual_stop(self):
            close = QMessageBox()
            close.setText("Confirm Again to stop Logging: ")
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Yes:
                self.sc_new.save_data_flg="Yes"
                self.reset()
                self.save_graph_data()
                self.sc_new.save_data_flg=""
                self.label_15.show()
                self.label_15.setText("Logging stopped Successfully.")
                
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                self.pushButton_15.setEnabled(True)
                   
                self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q)))        
                self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p)))   #length
                        
                #self.label_15.setText("")
                self.pushButton_4.setEnabled(True)
                self.pushButton_23.setEnabled(True)
            else:
                print("cancled")
                    
    
    def reset(self):        
                
#             self.label_15.show()
#             self.label_15.setText("Data Saving is in progress....wait.")#             
            
            if(self.sc_new.timer1.isActive()): 
                  
                  self.sc_new.timer1.stop()
                  print("Stopped  : sc_new :timer1")
                  self.sc_new.on_ani_stop()
                  
                 
            if(self.sc_new_P1.timer1.isActive()): 
                  self.sc_new_P1.timer1.stop()
                  print("Stopped  : sc_new1 :timer1")
                  self.sc_new_P1.on_ani_stop()
                  
            if(self.sc_new_P2.timer1.isActive()): 
                  self.sc_new_P2.timer1.stop()
                  print("Stopped  : sc_new2 :timer1")
                  self.sc_new_P2.on_ani_stop()
                 
                  
            if(self.timer3.isActive()): 
                  self.timer3.stop()
                  print("Stopped timer3")
            if(self.timer4.isActive()): 
                  self.timer4.stop()
                  print("Stopped timer4")
                  
            #self.label_15.show()
            #self.label_15.setText("Data Saved Successful")
                  
            self.lcdNumber.setProperty("value", 0.0)
            self.lcdNumber_2.setProperty("value", 0.0)
            self.enable_all()
            self.pushButton_9.setDisabled(True)
            
    def show_load_cell_val(self):       
            self.lcdNumber_2.setProperty("value", str(self.sc_new.q))        
            self.lcdNumber.setProperty("value",str(self.sc_new.p))   #length  
            
            #self.lineEdit_48.setText(str(round(self.sc_new.q_mpa,0)))    #stress     
            self.lineEdit_48.setProperty("value",round(self.sc_new.q_mpa,0))
            #self.lineEdit_52.setText(str(round(self.sc_new.p_strain,0)))   #Strain
            self.lineEdit_52.setProperty("value",round(self.sc_new.p_strain,4))
            #self.elapsed_time_show=self.time.strftime("%H:%M:%S",self.sc_new.t)
            self.mod=int(self.sc_new.t) % 60 
            self.lineEdit_53.setText(str(int(int(self.sc_new.t)/3600)).zfill(2)+":"+str(int(int(self.sc_new.t)/60)).zfill(2)+":"+str(int(int(self.mod))).zfill(2))
            self.label_15.setText("Test Running.....")
            
            
            if(str(self.sc_new.save_data_flg) =="Yes"):
                    
                    self.reset()
                    self.save_graph_data()
                    self.sc_new.save_data_flg=""
                    self.label_15.show()
                    self.label_15.setText("Logging Stopped Successfully.")
                    #self.go_to_next=self.go_to_next+1
                    self.pushButton_5.setEnabled(True)
                    self.pushButton_6.setEnabled(True)
                    self.pushButton_7.setEnabled(True)
                    self.pushButton_8.setEnabled(True)
                    
                    self.lcdNumber_2.setProperty("value", str(max(self.sc_new.db_arr_q)))        
                    self.lcdNumber.setProperty("value",str(max(self.sc_new.db_arr_p)))   #leng
                            
                    self.label_15.setText("")    
                    
    def save_graph_data(self):         
         if (len(self.sc_new.db_arr_p) > 1):            
            
            #self.cycle_num=int(str(self.label_67.text()))+1
            print("Data saved fun called ....xssxsxsx")
            print("length_p:"+str(len(self.sc_new.arr_p))+" length_t:"+str(len(self.sc_new.arr_t)))
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(2,len(self.sc_new.db_arr_p)):                     
                        cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM,Y_NUM_MPA,X_STRAIN,T_SEC,T_TIMESTAMP) VALUES ('"+str(float(self.sc_new.db_arr_p[g]))+"','"+str(float(self.sc_new.db_arr_q[g]))+"','"+str(float(self.sc_new.db_arr_q_mpa[g]))+"','"+str(float(self.sc_new.db_arr_p_strain[g]))+"','"+str(self.sc_new.db_arr_key_id[g])+"','"+str(self.sc_new.db_arr_t_timestamp[g])+"')")
            connection.commit();
            connection.close()
            
            #self.update_status()
            #self.cycle_num=self.cycle_num+1
            connection = sqlite3.connect("tyr.db")              
            with connection:        
                  cursor = connection.cursor()
                  #print("ok1")
                  try:
                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(int(self.label_12.text()))+"'")                          
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM) FROM STG_GRAPH_MST)") 
                          cursor.execute("UPDATE TEST_MST_TMP SET YEILD_STRENGTH=(SELECT MAX(Y_NUM) FROM STG_GRAPH_MST)") 
                          cursor.execute("UPDATE GLOBAL_VAR SET LENGTH_AT_MAX_MPA=(SELECT MAX(X_NUM_CM) FROM STG_GRAPH_MST WHERE Y_NUM=(SELECT YEILD_STRENGTH FROM TEST_MST_TMP))")
                          cursor.execute("UPDATE TEST_MST_TMP SET MODULUS_OF_ELASTICITY=((YEILD_STRENGTH) / ( SELECT (LENGTH_AT_MAX_MPA/NEW_TEST_AREA ) FROM GLOBAL_VAR))")
                          cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM,X_NUM_CM,Y_NUM_N,Y_NUM_MPA,X_NUM_STRAIN,T_SEC,T_TIMESTAMP) SELECT X_NUM,Y_NUM,X_NUM_CM,Y_NUM_N,Y_NUM_MPA,X_STRAIN,T_SEC,T_TIMESTAMP FROM STG_GRAPH_MST")                  
                          cursor.execute("UPDATE GRAPH_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL") 
                          cursor.execute("UPDATE TEST_MST_EXPANSION SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0)) FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")
                          cursor.execute("UPDATE TEST_MST_EXPANSION SET GRAPH_STATUS='LOADED GRAPH'  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")                  
                          cursor.execute("UPDATE TEST_MST_EXPANSION SET GRAPH_SCAL_X_LENGTH=(SELECT GRAPH_SCALE_CELL_2 FROM SETTING_MST),GRAPH_SCAL_Y_LOAD=(SELECT GRAPH_SCALE_CELL_1 FROM SETTING_MST)  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                          cursor.execute("UPDATE TEST_MST_EXPANSION SET YEILD_STRENGTH=(SELECT YEILD_STRENGTH FROM TEST_MST_TMP),MODULUS_OF_ELASTICITY=(SELECT MODULUS_OF_ELASTICITY FROM TEST_MST_TMP)  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                    
                          #cursor.execute("UPDATE TEST_MST_EXPANSION SET GRAPH_SCAL_X_LENGTH=(SELECT GRAPH_SCALE_CELL_2 FROM SETTING_MST),GRAPH_SCAL_Y_LOAD=(SELECT GRAPH_SCALE_CELL_1 FROM SETTING_MST)  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                          print("Data Saved Ok in STG_GRAPH_MST")
                          self.label_15.show()
                          self.label_15.setText("Data Saved Successfully.")
                  
                  #update max load , yead strength , modulus 
                  
                  except Exception as e:
                          print("SQL Error:"+str(e))
                          connection.commit();
                          
            connection.commit();
            connection.close()            
                     
            #self.show_grid_data_PROOF()
            ###### Create and SAVE all PDF's
            self.create_log_pdf()
            os.system("cp ./reports/log_report.pdf ./reports/Report_of_log_"+str(self.test_id)+".pdf")        
            product_id=self.get_usb_storage_id()
            if(product_id != "ERROR"):
                    os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                    os.system("cp ./reports/log_report.pdf /media/usb/Report_of_log_test_"+str(self.test_id)+".pdf")
                    os.system("sudo umount /media/usb")
            else:
                    print("Log-Please connect usb storage device")
            
            self.create_pdf_expansion()        
            #os.system("xpdf ./reports/test_report.pdf")
            os.system("cp ./reports/test_report.pdf ./reports/Report_of_test_"+str(self.test_id)+".pdf")
           
            
            #product_id=self.get_usb_storage_id()
            if(product_id != "ERROR"):
                    os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                    os.system("cp ./reports/test_report.pdf /media/usb/Report_of_test_"+str(self.test_id)+".pdf")
                    os.system("sudo umount /media/usb")
            else:
                    print("Test PDF- Please connect usb storage device")
       
     
    def open_pop_graph2(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.window = QtWidgets.QMainWindow()
        self.ui=pop_graph2_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()       
            
    def print_file(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POP_TEST_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def update_graph_type(self):
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='"+str(self.comboBox.currentText())+"'")                 
        connection.commit()
        connection.close()
    
    def open_log_pdf(self):
        
        
        self.create_log_pdf()
        os.system("xpdf ./reports/log_report.pdf")
        os.system("cp ./reports/log_report.pdf ./reports/Report_of_log_"+str(self.test_id)+".pdf")
        
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                os.system("cp ./reports/log_report.pdf /media/usb/Report_of_log_test_"+str(self.test_id)+".pdf")
                os.system("sudo umount /media/usb")
        else:
             print("Please connect usb storage device")
        
    def open_pdf(self):
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                    cursor = connection.cursor()
                    if(self.comboBox.currentText() == "Stress Vs Strain"):
                               cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='STRESS_VS_STRAIN'")                      
                    elif(self.comboBox.currentText() == "Pressure Vs Expansion"):
                               cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='PRESSURE_VS_EXPANSION'") 
                    elif(self.comboBox.currentText() == "Pressure Vs Time"):
                               cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='PRESSURE_VS_TIME'")  
                    elif(self.comboBox.currentText() == "Expansion Vs Time"):
                               cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='EXPANSION_VS_TIME'") 
                    elif(self.comboBox.currentText() == "Stress Vs Time"):
                               cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='STRESS_VS_TIME'")    
                    elif(self.comboBox.currentText() == "Strain Vs Time"):
                               cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='STRAIN_VS_TIME'")    
                    else:
                               cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='STRESS_VS_STRAIN'")  
                               print("invalid graph type")  
        connection.commit()
        connection.close()
        
        self.sc_data =PlotCanvas(self,width=8, height=4,dpi=80) 
        self.create_pdf_expansion() 
        
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
    
    def open_log_email(self):
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
        self.ui=popup_email_log_Ui_MainWindow()
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
        
    def pop_graph_scales(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=set_two_graphs_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def create_pdf_expansion(self):
        self.remark=""
        #self.unit_typex=self.comboBox_2.currentText()
        self.unit_typex = "N/mm"
        
        
             
        y=300
        Elements=[]
        summary_data=[]
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TEST_ID,DATE(TEST_DATE),SAMPLE_PIPE_NO,SAMPLE_ID,D_AV,T_AV,CIRCUMFARANCE, REVIEWED_BY,REMARK,TEST_STD FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(int(self.label_12.text()))+"'")
        for x in results:
            summary_data=[["Parameter","Value","Prarameter","Value"],["Test ID: ",str(x[0]),"Tested On: ",str(x[1])],["Sample Pipe No : ",str(x[2]),"Sample ID: ",str(x[3])],["Diameter:  ",str(x[4]),"Thickness:",str(x[5])]]
            summary_data.append([" Reviewed By: ",str(x[7]),"Circumference",str(x[6])])
            summary_data.append([" Test Standered: ",str(x[9]),"",""])
            self.remark=str(x[8])        
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
        
        h_line=Paragraph("              _____________________________________________________________________________________________", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
        
        #f1=Table(data)
        #f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
        
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        f=Table(summary_data)
        f.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 8),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
         
        #f2=Table(summary_data2)
        #f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 8),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
#        
#        f3=Table(summary_data3)
#        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 8),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
#        
#        f4=Table(summary_data4)
#        f4.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 8),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
#        
        #self.sc_data =PlotCanvas(self,width=8, height=4,dpi=80) 
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        #Elements=[Title,Title2,Spacer(1,12),f4,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,blank,blank,blank,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        Elements=[Title,Title2,Spacer(1,12),f,Spacer(1,12),pdf_img,Spacer(1,12),footer_2,Spacer(1,12),comments]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/test_report.pdf', rightMargin=10,
                                leftMargin=20,
                                topMargin=10,
                                bottomMargin=10,)
        doc.build(Elements) 


    def create_log_pdf(self):
        self.remark=""
        #self.unit_typex=self.comboBox_2.currentText()
        self.unit_typex = "N/mm"
        
             
        y=300
        Elements=[]
        summary_data=[]
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TEST_ID,DATE(TEST_DATE),SAMPLE_PIPE_NO,SAMPLE_ID,D_AV,T_AV,CIRCUMFARANCE, REVIEWED_BY,GRAPH_TYPE FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(int(self.label_12.text()))+"'")
        for x in results:
            summary_data=[["Parameter","Value","Prarameter","Value"],["Test ID: ",str(x[0]),"Tested On: ",str(x[1])],["Sample Pipe No : ",str(x[2]),"Sample.ID: ",str(x[3])],["Diameter:  ",str(x[4]),"Thickness:",str(x[5])]]
            summary_data.append([" Circumference: ",str(x[6]),"Reviewed By",str(x[7])])
            self.remark=str(x[5])        
        connection.close() 
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT GRAPH_ID FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(int(self.label_12.text()))+"'")
        for x in results:
                self.graph_id=str(x[0])       
        connection.close()
        
        summary_data2=[["Pressure(MPa)","Expansion(mm)","Stress(MPa)","Strain(%)","Sec","Time(HH:MI:SS)"]]
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT printf(\"%.4f\", Y_NUM) as PRESSURE, X_NUM as expansion, printf(\"%.4f\", Y_NUM_MPA) as stress, printf(\"%.4f\", X_NUM_STRAIN)  as strain, T_SEC, T_TIMESTAMP  FROM GRAPH_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"'")
        for x in results:
                    summary_data2.append([str(x[0]),str(x[1]),str(x[2]),str(x[3]),str(x[4]),str(x[5])])
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
          
        h_line=Paragraph("              _____________________________________________________________________________________________", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
        
        f=Table(summary_data)
        f.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 8),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
          
        f2=Table(summary_data2)
        f.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 8),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
        #f3=Table(summary_data3)
        #f.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 8),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
                 
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        #Elements=[Title,Title2,Spacer(1,12),f4,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,blank,blank,blank,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        Elements=[Title,Title2,Spacer(1,12),f,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12)]
              
        
        doc = SimpleDocTemplate('./reports/log_report.pdf', rightMargin=10,
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
        self.proof_test_by=""
        self.plot()        
        
        
    def plot(self):
        ax = self.figure.add_subplot(111)       
        ax.set_facecolor('#CCFFFF')   
        ax.minorticks_on()        
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        ax.set_xlabel('Strain (%)')
        ax.set_ylabel('Stress (MPa)')
        self.s=[]
        self.t=[]
        self.graph_ids=[]    
        self.x_num=[0.0]
        self.y_num=[0.0]
        self.test_type="Tensile"
        self.unit_type=""
        self.graph_type=""
        self.cs_area=0
        self.color=['b','r','g','y','k','c','m','b']
        #ax.set_title('Test Id=32         Samples=3       BreakLoad(Kg)=110        Length(mm)=3')

        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_IDENTIFICATION_NO,CURRENT_TIMESTAMP,GRAPH_TYPE,(SAMPLE_WIDTH_MM * T_AV)*0.1*0.1 as CS_AREA_CM  FROM TEST_MST_TMP") 
        for x in results:                        
                        self.graph_type= str(x[2])   
                        self.cs_area=float(x[3])                        
        connection.close()
        
        
        
        
        print("xxx graph Type :"+str(self.graph_type))
        ### Univarsal change for  Graphs #####################
            
        connection = sqlite3.connect("tyr.db")
        if(self.graph_type == "PRESSURE_VS_TIME"):
                #print("xxx-> SELECT X_SCALE_MAX, Y_SCALE_MAX from GRAPH_SCALES WHERE Y_SCALE_MAX > 0 AND GRAPH_NAME = 'PRESSURE_VS_TIME'") 
                results=connection.execute("SELECT X_SCALE_MAX, Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME = 'PRESSURE_VS_TIME'") 
        elif(self.graph_type == "EXPANSION_VS_TIME"):
                results=connection.execute("SELECT X_SCALE_MAX, Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME = 'EXPANSION_VS_TIME'") 
        elif(self.graph_type == "STRESS_VS_TIME"):
                results=connection.execute("SELECT X_SCALE_MAX, Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME = 'STRESS_VS_TIME'") 
        elif(self.graph_type == "STRAIN_VS_TIME"):
                results=connection.execute("SELECT X_SCALE_MAX, Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME = 'STRAIN_VS_TIME'") 
        elif(self.graph_type == "PRESSURE_VS_EXPANSION"):
                results=connection.execute("SELECT X_SCALE_MAX, Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME = 'PRESSURE_VS_EXPANSION'") 
        elif(self.graph_type == "STRESS_VS_STRAIN"):
                results=connection.execute("SELECT X_SCALE_MAX, Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME = 'STRESS_VS_STRAIN'") 
        else:
                results=connection.execute("SELECT X_SCALE_MAX, Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME = 'PRESSURE_VS_TIME'") 
        for x in results: 
                        ax.set_xlim(0,float(x[0]))
                        ax.set_ylim(0,float(x[1])) 
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_ID,SAMPLE_ID ,TEST_DATE FROM TEST_MST_EXPANSION WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
             ax.set_title('Sample ID :'+str(x[1])+" Date:"+str(x[2])[0:10]+"") 
             self.graph_ids.append(x[0])             
        connection.close()
        
        
        for g in range(len(self.graph_ids)):
            self.x_num=[0]
            self.y_num=[0]
            self.x1_num=[0]
            self.y1_num=[0]              
            #self.graph_type="STRESS_VS_STRAIN"           
            
            connection = sqlite3.connect("tyr.db")
            if(self.graph_type == "STRESS_VS_STRAIN"):
                    results=connection.execute("SELECT Y_NUM_MPA,X_NUM_STRAIN FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"' order by REC_ID asc     ")
                    ax.set_xlabel('Strain (%)')
                    ax.set_ylabel('Stress (MPa)')
            elif(self.graph_type == "PRESSURE_VS_TIME"):
                    #print("SELECT Y_NUM,T_SEC FROM GRAPH_MST WHERE Y_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"' order by REC_ID asc  ")                   
                    results=connection.execute("SELECT Y_NUM,T_SEC FROM GRAPH_MST WHERE Y_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"' order by REC_ID asc  ")
                    ax.set_xlabel('Time (sec)')
                    ax.set_ylabel('Pressure (MPa)')            
            elif(self.graph_type == "EXPANSION_VS_TIME"):
                    results=connection.execute("SELECT X_NUM,T_SEC FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'  order by REC_ID asc")
                    ax.set_xlabel('Time (sec)')
                    ax.set_ylabel('Expansion (mm)')                     
            elif(self.graph_type == "STRESS_VS_TIME"):
                    results=connection.execute("SELECT Y_NUM_MPA,T_SEC FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"' order by REC_ID asc")
                    ax.set_xlabel('Time (sec)')
                    ax.set_ylabel('Stress (MPa)')
            elif(self.graph_type == "STRAIN_VS_TIME"):
                    results=connection.execute("SELECT X_NUM_STRAIN,T_SEC FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"' order by REC_ID asc")
                    ax.set_xlabel('Time (sec)')
                    ax.set_ylabel('Strain (%)')
            elif(self.graph_type == "PRESSURE_VS_EXPANSION"):
                    results=connection.execute("SELECT Y_NUM,X_NUM FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"' order by REC_ID asc")
                    ax.set_xlabel('Expansion (mm)')
                    ax.set_ylabel('Pressure (MPa)')
            else:
                    results=connection.execute("SELECT X_NUM_STRAIN,Y_NUM_MPA FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"' order by REC_ID asc")
                    ax.set_xlabel('Strain (%)')
                    ax.set_ylabel('Stress (MPa)')
            for k in results:        
                                        self.y_num.append(float(k[0]))
                                        self.x_num.append(float(k[1]))
            connection.close() 
            
            
            ax.plot(self.x_num,self.y_num, 'b',label="Sample No:1")
            #ax1.plot(self.x1_num,self.y1_num, 'b',label="Sample No:1")
            
        
        
        ax.legend()
        #ax1.legend() 
        self.draw()
        self.figure.savefig('last_graph.png',dpi=100)            
        connection.close()
        
class PlotCanvas_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
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
        self.q_mpa =0
        self.t_timestamp=0
        self.key_id="P0"
        self.real_sec=0.0
        self.p_strain=0.0
        
        
        
        
        self.arr_p=[0.0]
        self.arr_p_cm=[0.0]
        self.arr_p_inch=[0.0]
        self.arr_p_strain=[0.0]
        self.arr_key_id=[0.0]
       
        
        self.arr_t=[0]
        self.arr_q=[0.0]
        self.arr_q_n=[0.0]
        self.arr_q_lb=[0.0]
        self.arr_q_mpa=[0.0]
        self.arr_t_timestamp=[""]
        
        self.db_arr_p=[0.0]
        self.db_arr_q=[0.0]
        self.db_arr_q_mpa=[0.0]
        self.db_arr_p_strain=[0.0]
        self.db_arr_t_timestamp=[""]
        self.db_arr_key_id=[0.0]
        self.db_arr_t=[0]
        self.p_start_val=0.0
        
        
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
        self.proof_test_by=""
        self.cs_area=0
        self.d_av=0
        self.t_av=0
        self.graph_type=""       
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.elapsed_time=0
        self.elapsed_time_show=0
        self.circumference=0
        self.i=0
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
        #self.line_cnt2, = self.axes1.plot([0,0], [0,0], lw=2)
#         connection = sqlite3.connect("tyr.db")              
#         with connection:        
#                 cursor = connection.cursor()                            
#                 cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
#         connection.commit();
#         connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_ID,CURRENT_TIMESTAMP ,GRAPH_TYPE,CIRCUMFARANCE FROM TEST_MST_TMP") 
        for x in results:
                        self.axes.set_title('Sample ID :'+str(x[0])+" Date :"+str(x[1])[0:10]+"")                        
                        self.graph_type=str(x[2])
                        self.axes.set_xlabel('Time (S)')
                        self.axes.set_ylabel('Pressure (MPa)')
                        self.cs_area= 0
                        self.circumference=str(x[3])
        connection.close()
        
        
                   
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,PROOF_TEST_BY,PROOF_MAX_LOAD,PROOF_MAX_LENGTH,TEST_TIME_SEC,D_AV,T_AV from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=float(x[0])
             
             self.test_guage_mm=1.0
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
            
             
             self.proof_max_load=int(str("9999"))
             self.proof_max_length=float(str(x[8]))
             self.test_time_sec=int(str(x[9]))
             self.d_av=float((str(x[10])))
             self.t_av=float((str(x[11])))
             
        connection.close()
        print(" xxx     gfgf self.unit_type:"+str(self.unit_type))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:  
                     #self.axes1.set_xlim(0,float(x[0]))
                     #self.axes1.set_ylim(0,float(x[1]))
                     #self.flexural_max_load=int(x[1])
                     #self.xlim=float(x[0])
                     #self.ylim=float(x[1])
                      
                     self.auto_rev_time_off=int(x[2])
                     self.break_sence=int(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX, Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME = 'PRESSURE_VS_TIME'") 
        for x in results:             
                    self.axes.set_xlim(0,float(x[0]))
                    self.axes.set_ylim(0,float(x[1]))
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
        time.sleep(2)
        self.timer1.setInterval(1000)     
        self.timer1.timeout.connect(self.update_graph)
        self.timer1.start(1)
        
        self.on_ani_start()
    
    def update_graph(self):
        self.end_time = datetime.datetime.now()
        self.elapsed_time=self.end_time-self.start_time
        #self.elapsed_time_show=self.end_time-self.start_time
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
                 
                 
                if(float(self.p_start_val)==0.0):
                      self.p_start_val=float(self.p)
                else: 
                      self.p=float(self.p)-float(self.p_start_val)
                #self.q=abs(float(self.buff[0])) #fix val
                self.t=self.elapsed_time.seconds
                #self.p=abs(float(self.buff[4])) #fix val
                
                self.t_timestamp=str(self.end_time)
                #self.arr_t_timestamp.append(self.t_timestamp)
                
                
                
                self.t_mod=int(self.t) % 60 
                self.t_timestamp=str(self.end_time)
                self.arr_t_timestamp.append(str(int(int(self.t)/3600)).zfill(2)+":"+str(int(int(self.t)/60)).zfill(2)+":"+str(int(int(self.t_mod))).zfill(2))
                self.real_sec=float(self.t)
                
#                 if(int(self.t) > 0):                    
#                      if(self.flgx=='N'):
#                             self.real_sec=int(self.t_mod)                            
#                      elif(int(self.t_mod) == 0):
#                             self.real_sec=int("60")+int(self.real_sec)
#                             self.flgx='Y'
#                      elif(self.flgx=='Y'):
#                             self.real_sec=self.real_sec+
#                      else:

                            
                
                   
                if(self.test_type=="Compress"):
                    self.p=int(self.test_guage_mm)-self.p
                    #print("self.p :"+str(self.p))
                elif(self.test_type=="Flexural"):
                    #self.p=self.p
                    self.p=int(self.test_guage_mm)-self.p
                else:
                    self.p=self.p
                    
                
                
                self.p=float(self.p)
                self.p_cm=float(self.p)/10
                self.arr_p_cm.append(float(self.p_cm))
                
                self.p_inch=float(self.p)*0.0393701
                self.arr_p_inch.append(float(self.p_inch))
                
                #self.p_strain=float(self.p)*100/float(20.00)
#                 self.arr_p_strain.append(float(self.p_strain))
                
                if(int(self.circumference) > 0):
                     self.p_strain=(float(self.p)/float(self.circumference))*100
                else:
                     self.p_strain=0
                print("  self.circumference :"+str(self.circumference)+"   self.p:"+str(self.p)+"  self.p_strain: "+str(self.p_strain))     
                self.arr_p_strain.append(float(self.p_strain))  
                
                self.arr_t.append(int(self.t))
                
                self.q=float(self.q)
                self.q_n=float(self.q)*9.81
                self.arr_q_n.append(float(self.q_n))
                
                self.q_lb=float(self.q)*2.20462
                self.arr_q_lb.append(float(self.q_lb))
                
                if(float(self.t_av) > 0.0):
                        self.q_mpa=float(((float(self.q)* float(self.d_av))/(2*float(self.t_av))))
                else:
                        self.q_mpa=0.0
                
                self.arr_q_mpa.append(float(self.q_mpa))              
                print(" (P0) P:"+str(self.p)+" q:"+str(self.q)+" real_sec:"+str(self.real_sec))
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                print(" self.q: "+str(self.q)+" self.d_av: "+str(self.d_av)+" self.t_av: "+str(self.t_av)+" self.q_mpa : "+str(self.q_mpa))
                
                
                self.db_arr_p.append(float(self.p))
                self.db_arr_q.append(float(self.q))
                self.db_arr_q_mpa.append(float(self.q_mpa))
                self.db_arr_p_strain.append(float(self.p_strain))
                self.db_arr_key_id.append(float(self.real_sec))
                self.db_arr_t_timestamp.append(str(int(int(self.t)/3600)).zfill(2)+":"+str(int(int(self.t)/60)).zfill(2)+":"+str(int(int(self.t_mod))).zfill(2))
                self.db_arr_t.append(int(self.t))
                
                
                self.arr_key_id.append(float(self.real_sec))
                #print(" Array P:"+str(self.arr_p))
                #print(" Array Q:"+str(self.arr_q))
               
                
                #print(" self.q :"+str(self.q)+" self.ylim: "+str(self.ylim))

                if(int(self.q) > int(self.ylim)):
                    self.ylim=(int(self.q)+100)
                    self.ylim_update='YES'
                    
                    #time.sleep(1)
                self.save_data_flg="No"
            
            else:                
               
                self.save_data_flg="Yes"
                self.on_ani_stop()
        
    def plot_grah_only(self,i):
            self.line_cnt.set_data(self.db_arr_key_id,self.db_arr_q)
            return [self.line_cnt]
          
    

        
    def on_ani_stop(self):
        self.on_stop()
        if self.playing:
            self.ani._stop()
            #self.ani_2._stop()
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
            
#            self.ani_2 = animation.FuncAnimation(
#                self.figure,
#                self.plot2_grah_only,
#                blit=True, interval=10
#                    )
#            print("Done2")
       
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
            # End of auto    

class PlotCanvas_Auto_P1(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
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
        self.q_mpa =0
        self.key_id="P1"
        
        
        
        self.arr_p=[0.0]
        self.arr_p_cm=[0.0]
        self.arr_p_inch=[0.0]
        self.arr_p_strain=[0.0]
        
        self.arr_t=[0.0]
        self.arr_q=[0.0]
        self.arr_q_n=[0.0]
        self.arr_q_lb=[0.0]
        self.arr_q_mpa=[0.0]
        self.arr_key_id=[""]
        
        
        self.db_arr_p1=[0.0]
        self.db_arr_q1=[0.0]
        self.db_arr_q_mpa1=[0.0]
        self.db_arr_p_strain1=[0.0]
        self.db_arr_t_timestamp1=[""]
        self.db_arr_key_id1=[0.0]
        self.db_arr_t1=[0]
        self.p_start_val=0.0
        
        
        
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
        self.proof_test_by=""
        self.cs_area=0
        self.d_av=0
        self.t_av=0
        self.graph_type=""       
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.elapsed_time=0
        self.elapsed_time_show=0
        self.circumference=0
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
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
        except IOError:
                print("IO Errors")
                self.ser=""
                self.IO_error_flg=1
        #self.line_cnt2, = self.axes1.plot([0,0], [0,0], lw=2)
        
        '''
        
        '''
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_ID,CURRENT_TIMESTAMP ,GRAPH_TYPE,CIRCUMFARANCE FROM TEST_MST_TMP") 
        for x in results:
                        self.axes.set_title('Sample ID :'+str(x[0])+" Date :"+str(x[1])[0:10]+"")                        
                        self.graph_type=str(x[2])
                        self.axes.set_ylabel('Pressure (Mpa)')
                        self.axes.set_xlabel('Expansion (mm)')
                        self.cs_area= 0
                        self.circumference=str(x[3])
        connection.close()
        
        
                   
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,PROOF_TEST_BY,PROOF_MAX_LOAD,PROOF_MAX_LENGTH,TEST_TIME_SEC,D_AV,T_AV from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=float(x[0])
             self.test_guage_mm=1.0
             print("self.test_guage_mm:"+str(self.test_guage_mm))
             self.test_guage_mm=1
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
            
             
             self.proof_max_load=int(str("9999"))
             self.proof_max_length=float(str(x[8]))
             self.test_time_sec=int(str(x[9]))
             self.d_av=float((str(x[10])))
             self.t_av=float((str(x[11])))
             
        connection.close()
        print(" xxx     gfgf self.unit_type:"+str(self.unit_type))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:  
                     #self.axes1.set_xlim(0,float(x[0]))
                     #self.axes1.set_ylim(0,float(x[1]))
                     #self.flexural_max_load=int(x[1])
                     #self.xlim=float(x[0])
                     #self.ylim=float(x[1])
                      
                     self.auto_rev_time_off=int(x[2])
                     self.break_sence=int(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX, Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME = 'PRESSURE_VS_EXPANSION'") 
        for x in results:             
                    self.axes.set_xlim(0,float(x[0]))
                    self.axes.set_ylim(0,float(x[1]))
        connection.close()
        
        '''
        
        
        '''
        self.timer1.setInterval(1000)     
        self.timer1.timeout.connect(self.update_graph)
        self.timer1.start(1)
        
        self.on_ani_start()
    
    def update_graph(self): 
        self.end_time = datetime.datetime.now()
        self.elapsed_time=self.end_time-self.start_time
            
        if(self.IO_error_flg==0 and str(self.ser) != "" ):
            '''
            
            '''
            try:
                self.line = self.ser.readline()
                #print("Timer Job o/p:"+str(self.line))
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
                 
                 
                 
                if(float(self.p_start_val)==0.0):
                      self.p_start_val=float(self.p)
                else: 
                      self.p=float(self.p)-float(self.p_start_val)
					   
                 
                #self.q=abs(float(self.buff[0])) #fix val
                #self.t=abs(float(self.buff[3]))
                self.t=self.elapsed_time.seconds
                #self.p=abs(float(self.buff[4])) #fix val
                
                if(self.test_type=="Compress"):
                    self.p=int(self.test_guage_mm)-self.p
                    #print("self.p :"+str(self.p))
                elif(self.test_type=="Flexural"):
                    #self.p=self.p
                    self.p=int(self.test_guage_mm)-self.p
                else:
                    self.p=self.p
                    
                
                
                self.p=float(self.p)
                self.p_cm=float(self.p)/10
                self.arr_p_cm.append(float(self.p_cm))
                
                self.p_inch=float(self.p)*0.0393701
                self.arr_p_inch.append(float(self.p_inch))
                
                #self.arr_p_strain.append(float(self.p)*100/float(20.00))
                if(int(self.circumference) > 0):
                     self.p_strain=(float(self.p)/float(self.circumference))*100
                else:
                     self.p_strain=0
                self.arr_p_strain.append(float(self.p_strain))    
                
                self.arr_t.append(float(self.t))
                
                self.q=float(self.q)
                self.q_n=float(self.q)*9.81
                self.arr_q_n.append(float(self.q_n))
                
                self.q_lb=float(self.q)*2.20462
                self.arr_q_lb.append(float(self.q_lb))
                
                if(float(self.t_av) > 0.0):
                        self.q_mpa=float(((float(self.q)* float(self.d_av))/(2*float(self.t_av))))
                else:
                        self.q_mpa=0.0
                
                self.arr_q_mpa.append(float(self.q_mpa))              
                
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                print(" (P1) :P:"+str(self.p)+" q:"+str(self.q)+" t:"+str(self.t))
                self.arr_key_id.append(self.key_id)
                #print(" Array P:"+str(self.arr_p))
                #print(" Array Q:"+str(self.arr_q))
                self.db_arr_p1.append(float(self.p))
                self.db_arr_q1.append(float(self.q))
                self.db_arr_q_mpa1.append(float(self.q_mpa))
                self.db_arr_p_strain1.append(float(self.p_strain))
                #self.db_arr_key_id1.append(float(self.real_sec))
                #self.db_arr_t_timestamp1.append(str(int(int(self.t)/3600)).zfill(2)+":"+str(int(int(self.t)/60)).zfill(2)+":"+str(int(int(self.t_mod))).zfill(2))
                self.db_arr_t1.append(int(self.t))
                
                #print(" self.q :"+str(self.q)+" self.ylim: "+str(self.ylim))

                if(int(self.q) > int(self.ylim)):
                    self.ylim=(int(self.q)+100)
                    self.ylim_update='YES'
                    
                    #time.sleep(1)
                self.save_data_flg="No"
            
            else:                
               
                self.save_data_flg="Yes"
                self.on_ani_stop()
        
    def plot_grah_only(self,i):
            self.line_cnt.set_data(self.db_arr_p1,self.db_arr_q1)
            return [self.line_cnt]
          

        
    def on_ani_stop(self):
        self.on_stop()
        if self.playing:
            self.ani._stop()
            #self.ani_2._stop()
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
            # End of P1     


class PlotCanvas_Auto_P2(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
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
        self.p_strain =0
         
        self.t=0
        self.q =0
        self.q_n =0
        self.q_lb =0
        self.q_mpa =0
        self.key_id="P2"
        
        
        
        self.arr_p=[0.0]
        self.arr_p_cm=[0.0]
        self.arr_p_inch=[0.0]
        self.arr_p_strain=[0.0]
        self.arr_key_id=[""]
        
        self.arr_t=[0.0]
        self.arr_q=[0.0]
        self.arr_q_n=[0.0]
        self.arr_q_lb=[0.0]
        self.arr_q_mpa=[0.0]
        
        self.db_arr_p2=[0.0]
        self.db_arr_q2=[0.0]
        self.db_arr_q_mpa2=[0.0]
        self.db_arr_p_strain2=[0.0]
        self.db_arr_t_timestamp2=[""]
        self.db_arr_key_id2=[0.0]
        self.db_arr_t2=[0]
        self.p_start_val=0.0
        
        
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
        self.proof_test_by=""
        self.cs_area=0
        self.d_av=0
        self.t_av=0
        self.graph_type=""       
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.elapsed_time=0
        self.elapsed_time_show=0
        self.circumference=0
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
        #self.line_cnt2, = self.axes1.plot([0,0], [0,0], lw=2)
#         connection = sqlite3.connect("tyr.db")              
#         with connection:        
#                 cursor = connection.cursor()                            
#                 cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
#         connection.commit();
#         connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_ID,CURRENT_TIMESTAMP ,GRAPH_TYPE,CIRCUMFARANCE FROM TEST_MST_TMP") 
        for x in results:
                        self.axes.set_title('Sample ID :'+str(x[0])+" Date :"+str(x[1])[0:10]+"")                        
                        self.graph_type=str(x[2])
                        self.axes.set_ylabel('Stress (MPa)')
                        self.axes.set_xlabel('Strain (%)')
                        self.cs_area= 0
                        self.circumference=str(x[3])
        connection.close()
        
        
                   
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,PROOF_TEST_BY,PROOF_MAX_LOAD,PROOF_MAX_LENGTH,TEST_TIME_SEC,D_AV,T_AV from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=float(x[0])
             self.test_guage_mm=1.0
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
            
             
             self.proof_max_load=int(str("9999"))
             self.proof_max_length=float(str(x[8]))
             self.test_time_sec=int(str(x[9]))
             self.d_av=float((str(x[10])))
             self.t_av=float((str(x[11])))
             
        connection.close()
        print(" xxx     gfgf self.unit_type:"+str(self.unit_type))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:  
                     #self.axes1.set_xlim(0,float(x[0]))
                     #self.axes1.set_ylim(0,float(x[1]))
                     #self.flexural_max_load=int(x[1])
                     #self.xlim=float(x[0])
                     #self.ylim=float(x[1])
                      
                     self.auto_rev_time_off=int(x[2])
                     self.break_sence=int(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX, Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME = 'STRESS_VS_STRAIN'") 
        for x in results:             
                    self.axes.set_xlim(0,float(x[0]))
                    self.axes.set_ylim(0,float(x[1]))
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
        except IOError:
                print("IO Errors")
                self.IO_error_flg=1
        self.timer1.setInterval(1000)     
        self.timer1.timeout.connect(self.update_graph)
        self.timer1.start(1)
        
        self.on_ani_start()
    
    def update_graph(self): 
        self.end_time = datetime.datetime.now()
        self.elapsed_time=self.end_time-self.start_time
            
        if(self.IO_error_flg==0):
            '''
           
            '''
            try:
                self.line = self.ser.readline()
                #print("Timer Job o/p:"+str(self.line))
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
                 
                 
                if(float(self.p_start_val)==0.0):
                      self.p_start_val=float(self.p)
                else: 
                      self.p=float(self.p)-float(self.p_start_val)
					   
                 
                 
                #self.q=abs(float(self.buff[0])) #fix val
                #self.t=abs(float(self.buff[3]))
                self.t=self.elapsed_time.seconds
                #self.p=abs(float(self.buff[4])) #fix val
                
                if(self.test_type=="Compress"):
                    self.p=int(self.test_guage_mm)-self.p
                    #print("self.p :"+str(self.p))
                elif(self.test_type=="Flexural"):
                    #self.p=self.p
                    self.p=int(self.test_guage_mm)-self.p
                else:
                    self.p=self.p
                    
                
                
                self.p=float(self.p)
                self.p_cm=float(self.p)/10
                self.arr_p_cm.append(float(self.p_cm))
                
                self.p_inch=float(self.p)*0.0393701
                self.arr_p_inch.append(float(self.p_inch))
                
                #self.arr_p_strain.append(float(self.p)*100/float(20.00))
                if(int(self.circumference) > 0):
                     self.p_strain=(float(self.p)/float(self.circumference))*100
                else:
                     self.p_strain=0
                
                self.arr_p_strain.append(float(self.p_strain))     
                self.arr_t.append(float(self.t))
                
                self.q=float(self.q)
                self.q_n=float(self.q)*9.81
                self.arr_q_n.append(float(self.q_n))
                
                self.q_lb=float(self.q)*2.20462
                self.arr_q_lb.append(float(self.q_lb))
                
                if(float(self.t_av) > 0.0):
                        self.q_mpa=float(((float(self.q)* float(self.d_av))/(2*float(self.t_av))))
                else:
                        self.q_mpa=0.0
                
                self.arr_q_mpa.append(float(self.q_mpa))              
                
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                print(" (P2) P:"+str(self.p)+" q_mpa:"+str(self.q_mpa)+" t:"+str(self.t))
                self.arr_key_id.append(self.key_id)
                #print(" Array P:"+str(self.arr_p))
                #print(" Array Q:"+str(self.arr_q))
                
                self.db_arr_p2.append(float(self.p))
                self.db_arr_q2.append(float(self.q))
                self.db_arr_q_mpa2.append(float(self.q_mpa))
                self.db_arr_p_strain2.append(float(self.p_strain))
                #self.db_arr_key_id2.append(float(self.real_sec))
                #self.db_arr_t_timestamp2.append(str(int(int(self.t)/3600)).zfill(2)+":"+str(int(int(self.t)/60)).zfill(2)+":"+str(int(int(self.t_mod))).zfill(2))
                self.db_arr_t2.append(int(self.t))
               
                
                #print(" self.q :"+str(self.q)+" self.ylim: "+str(self.ylim))

                if(int(self.q) > int(self.ylim)):
                    self.ylim=(int(self.q)+100)
                    self.ylim_update='YES'
                    
                    #time.sleep(1)
                self.save_data_flg="No"
            
            else:                
               
                self.save_data_flg="Yes"
                self.on_ani_stop()
        
    def plot_grah_only(self,i):
            self.line_cnt.set_data(self.db_arr_p_strain2,self.db_arr_q_mpa2)
            return [self.line_cnt]
          
    
#    def plot2_grah_only(self,i):      
#           self.line_cnt2.set_data(self.arr_p,self.arr_q_mpa)
#           return [self.line_cnt2]
        
    def on_ani_stop(self):
        self.on_stop()
        if self.playing:
            self.ani._stop()
            #self.ani_2._stop()
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
            
#            self.ani_2 = animation.FuncAnimation(
#                self.figure,
#                self.plot2_grah_only,
#                blit=True, interval=10
#                    )
#            print("Done2")
       
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
            # End of P2        

            

            



class PlotCanvas_blank(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
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
        self.x=[0,0,0,0,0,0,0,0]
        self.y=[0,0,0,0,0,0,0,0]
        
        self.p=list()
        self.q=list()
        self.graph_type=""
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#CCFFFF')
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
       
#        connection = sqlite3.connect("tyr.db")
#        results=connection.execute("SELECT GRAPH_TYPE from TEST_MST_TMP") 
#        for x in results:
#                self.graph_type=str(x[0]) 
#        connection.close() 
#        connection = sqlite3.connect("tyr.db")
#        results=connection.execute("SELECT FLOW_TIME_X_AXIS,FLOW_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS, VOLUMN_TIME_Y_AXIS FROM OTER_INFO  ") 
#        for x in results:
#                        
#                         ax.set_xlim(0,float(x[0]))
#                         ax.set_ylim(0,float(x[1]))
#                         
#
#                         
#                         
#                              
#        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'PRESSURE_VS_TIME' LIMIT 1") 
        for x in results:
             ax.set_xlim(0,float(x[0]))
             ax.set_ylim(0,float(x[1]))          
        connection.close()
        ax.set_xlabel('Time (sec)')
        ax.set_ylabel('Pressure (MPa)')
        
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])
        
        
        ax.plot(self.x,self.y,'b')
        
        ########
        '''
       
      
        '''
        self.draw() 

class PlotCanvas_blank_P1(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
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
        self.x=[0,0,0,0,0,0,0,0]
        self.y=[0,0,0,0,0,0,0,0]
        
        self.p=list()
        self.q=list()
        self.graph_type=""
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#CCFFFF')
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
       
#        connection = sqlite3.connect("tyr.db")
#        results=connection.execute("SELECT GRAPH_TYPE from TEST_MST_TMP") 
#        for x in results:
#                self.graph_type=str(x[0]) 
#        connection.close() 
#        connection = sqlite3.connect("tyr.db")
#        results=connection.execute("SELECT FLOW_TIME_X_AXIS,FLOW_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS, VOLUMN_TIME_Y_AXIS FROM OTER_INFO") 
#        for x in results:             
#                         ax.set_xlabel('Time (sec)')
#                         ax.set_ylabel('Expansion (mm)')
#                         ax.set_xlim(0,float(x[0]))
#                         ax.set_ylim(0,float(x[1]))
#        
#        connection.close()
         
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'PRESSURE_VS_EXPANSION' LIMIT 1") 
        for x in results:
             ax.set_xlim(0,float(x[0]))
             ax.set_ylim(0,float(x[1]))          
        connection.close()
        ax.set_ylabel('Pressure (MPa)')
        ax.set_xlabel('Expansion (mm)')
        
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])
        
        
        ax.plot(self.x,self.y,'b')
        
        ########
        
        '''
        
        '''
        self.draw() 



class PlotCanvas_blank_P2(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
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
        self.x=[0,0,0,0,0,0,0,0]
        self.y=[0,0,0,0,0,0,0,0]
        
        self.p=list()
        self.q=list()
        self.graph_type=""
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#CCFFFF')
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
       
#        connection = sqlite3.connect("tyr.db")
#        results=connection.execute("SELECT GRAPH_TYPE from TEST_MST_TMP") 
#        for x in results:
#                self.graph_type=str(x[0]) 
#        connection.close() 
#        connection = sqlite3.connect("tyr.db")
#        results=connection.execute("SELECT FLOW_TIME_X_AXIS,FLOW_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS, VOLUMN_TIME_Y_AXIS FROM OTER_INFO") 
#        for x in results:             
#                         ax.set_xlabel('Time (sec)')
#                         ax.set_ylabel('Stress (MPa)')
#                         ax.set_xlim(0,float(x[0]))
#                         ax.set_ylim(0,float(x[1]))
#        
#        connection.close()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'STRESS_VS_STRAIN' LIMIT 1") 
        for x in results:
             ax.set_xlim(0,float(x[0]))
             ax.set_ylim(0,float(x[1]))          
        connection.close()
        ax.set_ylabel('Stress (MPa)')
        ax.set_xlabel('Strain (%)')
        
        
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])
        
        
        ax.plot(self.x,self.y,'b')
        
        ########
        
        
        self.draw() 

################ GRAPH GROUP 2 ############################

class PlotCanvasG2_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="tyr"
        self.axes.set_xlabel('Expansion (mm)')
        self.axes.set_ylabel('Pressure (MPa)')
        self.axes.grid(which='major', linestyle='-', linewidth='0.50', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.50', color='black')
        
#         self.axes2 = self.axes.twinx()
#         color = 'tab:green'
#         self.axes2.set_ylabel('Time (Sec)', color = color)
#         self.axes2.set_ylim(0,500)
        
        
        
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.q =0
        self.t =170
        self.t_timestamp=""
        self.p_strain=0.0
        self.real_sec=0.0
        
        self.arr_p=[0.0]
        self.arr_q=[0.0]
        self.arr_t=[0.0]
        self.arr_p1=[0.0]
        self.arr_q1=[0.0]
        self.arr_t_timestamp=[""]
        self.arr_key_id=[0.0]
        
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
        self.q_mpa =0
        self.arr_p_strain=[0.0]
        self.arr_q_mpa=[0.0]
        self.cs_area=0
        self.d_av=0
        self.t_av=0
        self.graph_type=""
        self.elapsed_time=0
        self.elapsed_time_show=0
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.circumference=0
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
   
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
        #self.line_cnt2, = self.axes2.plot([0,0], [0,0], lw=2)
#         connection = sqlite3.connect("tyr.db")              
#         with connection:        
#                 cursor = connection.cursor()                            
#                 cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
#         connection.commit();
#         connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_ID,CURRENT_TIMESTAMP ,GRAPH_TYPE,CIRCUMFARANCE FROM TEST_MST_TMP") 
        for x in results:
                        self.axes.set_title('Sample ID :'+str(x[0])+" Date :"+str(x[1])[0:10]+"")                        
                        self.graph_type=str(x[2])
                        self.axes.set_xlabel('Expansion (mm)')
                        self.axes.set_ylabel('Pressure (MPa)')
                        self.cs_area= 0
                        self.circumference=str(x[3])
        connection.close()
        
        
                   
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,PROOF_TEST_BY,PROOF_MAX_LOAD,PROOF_MAX_LENGTH,TEST_TIME_SEC,D_AV,T_AV from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=float(x[0])             
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
             self.proof_max_load=int(str("9999"))
             self.proof_max_length=float(str(x[8]))
             self.test_time_sec=int(str(x[9]))
             self.d_av=float((str(x[10])))
             self.t_av=float((str(x[11])))
             
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:
             #self.axes.set_xlim(0,int(x[0]))
             #self.axes.set_ylim(0,int(x[1]))
             #self.flexural_max_load=int(x[1])
             #self.xlim=int(x[0])
             #self.ylim=int(x[1])
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'PRESSURE_VS_EXPANSION' LIMIT 1") 
        for x in results:
             self.axes.set_xlim(0,float(x[0]))
             self.axes.set_ylim(0,float(x[1]))          
        connection.close()
        
        
        '''
        
        '''
        self.test_guage_mm=609
        self.max_load=0
        self.cof_max_length=100
        #print("434Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
        
        
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
        #lobj2 = self.axes2.plot([],[],lw=2)[0]
        
        self.lines.append(lobj)
        #self.lines.append(lobj2)
        self.on_ani_start()
        
        
    def update_graph(self):
        self.end_time = datetime.datetime.now()
        self.elapsed_time=self.end_time-self.start_time
        if(self.IO_error_flg==0):
            '''
           
            '''
            try:
                self.line = self.ser.readline()
                #print("Timer Job o/p:"+str(self.line))
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
                '''
                self.r=170.00
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                self.arr_t.append(float(self.t))
                '''
                
                
                #self.q=abs(float(self.buff[1])) #fix val
                #self.t=abs(float(self.buff[3]))
                self.t=float(self.elapsed_time.seconds)
                #self.p=abs(float(self.buff[4])) #fix val
                #self.p_strain=(float(self.p)*100/float(20.00))
                #self.arr_p_strain.append(float(self.p)*100/float(20.00))
                if(int(self.circumference) > 0):
                     self.p_strain=(float(self.p)/float(self.p))*100
                else:
                     self.p_strain=0
                     
                self.arr_p_strain.append(float(self.p_strain))  
                if(float(self.t_av) > 0.0):
                        self.q_mpa=float((float(self.q)* float(self.d_av)/2*float(self.t_av)))
                else:
                        self.q_mpa=0.0
                
                self.arr_q_mpa.append(float(self.q_mpa)) 
                self.arr_t.append(float(self.t))
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                
                
                self.t_mod=int(self.t) % 60 
                self.t_timestamp=str(self.end_time)
                self.arr_t_timestamp.append(str(int(int(self.t)/3600)).zfill(2)+":"+str(int(int(self.t)/60)).zfill(2)+":"+str(int(int(self.t_mod))).zfill(2))
                self.real_sec=float(self.t)                
                self.arr_key_id.append(float(self.real_sec))
                
                print(" [G2 P0 ] P:"+str(self.p)+" q:"+str(self.q)+" t:"+str(self.t))
                

                
                
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
        '''
        self.x1.append(self.p)
        self.y1.append(self.q)
        self.x2.append(self.p)
        self.y2.append(self.t)

        self.xlist = [self.x1, self.x2]
        self.ylist = [self.y1, self.y2]
        #for index in range(0,1):
        for lnum,line in enumerate(self.lines):
            line.set_data(self.xlist[lnum], self.ylist[lnum]) # set data for each line separately.
        return self.lines
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
        connection = sqlite3.connect("tyr.db")
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
            print(" not Ok  ")  ### End of G2
            

class PlotCanvasG2_Auto_P1(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="tyr"
#         self.axes.set_xlabel('Expansion (mm)')
#         self.axes.set_ylabel('Pressure (MPa)')
        self.axes.grid(which='major', linestyle='-', linewidth='0.50', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.50', color='black')
        
#         self.axes2 = self.axes.twinx()
#         color = 'tab:green'
#         self.axes2.set_ylabel('Time (Sec)', color = color)
#         self.axes2.set_ylim(0,500)
        
        
        
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.p_strain=0
        self.q =0
        self.t =170
        
        self.arr_p=[0.0]
        self.arr_q=[0.0]
        self.arr_t=[0.0]
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
        self.q_mpa =0
        self.arr_p_strain=[0.0]
        self.arr_q_mpa=[0.0]
        self.cs_area=0
        self.d_av=0
        self.t_av=0
        self.graph_type=""
        self.elapsed_time=0
        self.elapsed_time_show=0
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.circumference="0"
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
   
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
        #self.line_cnt2, = self.axes2.plot([0,0], [0,0], lw=2)
#         connection = sqlite3.connect("tyr.db")              
#         with connection:        
#                 cursor = connection.cursor()                            
#                 cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
#         connection.commit();
#         connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_ID,CURRENT_TIMESTAMP ,GRAPH_TYPE,CIRCUMFARANCE FROM TEST_MST_TMP") 
        for x in results:
                        self.axes.set_title('Sample ID :'+str(x[0])+" Date :"+str(x[1])[0:10]+"")                        
                        self.graph_type=str(x[2])
                        self.axes.set_xlabel('Strain (%)')
                        self.axes.set_ylabel('Stress (MPa)')
                        self.cs_area= 0
                        self.circumference=str(x[3])
        connection.close()
        
        
                   
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,PROOF_TEST_BY,PROOF_MAX_LOAD,PROOF_MAX_LENGTH,TEST_TIME_SEC,D_AV,T_AV from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=float(x[0])             
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
             self.proof_max_load=int(str("9999"))
             self.proof_max_length=float(str(x[8]))
             self.test_time_sec=int(str(x[9]))
             self.d_av=float((str(x[10])))
             self.t_av=float((str(x[11])))
             
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:
             #self.axes.set_xlim(0,int(x[0]))
             #self.axes.set_ylim(0,int(x[1]))
             #self.flexural_max_load=int(x[1])
             #self.xlim=int(x[0])
             #self.ylim=int(x[1])
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'STRESS_VS_STRAIN' LIMIT 1") 
        for x in results:
             self.axes.set_xlim(0,float(x[0]))
             self.axes.set_ylim(0,float(x[1]))          
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
        except IOError:
                 self.ser=""
                 self.IO_error_flg=1
        '''
       
        
        '''
        self.timer1.setInterval(1000)     
        self.timer1.timeout.connect(self.update_graph)
        self.timer1.start(1)
   
        self.x1,self.y1 = [],[]
        self.x2,self.y2 = [],[]
        self.lines = []
        lobj = self.axes.plot([],[],lw=2)[0]
        #lobj2 = self.axes2.plot([],[],lw=2)[0]
        
        self.lines.append(lobj)
        #self.lines.append(lobj2)
        self.on_ani_start()
        
        
    def update_graph(self):
        self.end_time = datetime.datetime.now()
        self.elapsed_time=self.end_time-self.start_time
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
                '''
                self.r=170.00
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                self.arr_t.append(float(self.t))
                '''
                
                
                #self.q=abs(float(self.buff[1])) #fix val
                #self.t=abs(float(self.buff[3]))
                self.t=float(self.elapsed_time.seconds)
                
                #self.p=abs(float(self.buff[4])) #fix val
                
                #self.p_strain=float(float(self.p)*100/float(20.00))
                #self.arr_p_strain.append(float(self.p)*100/float(20.00))
                if(int(self.circumference) > 0):
                     self.p_strain=(float(self.p)/float(self.p))*100
                else:
                     self.p_strain=0
                     
                self.arr_p_strain.append(float(self.p_strain))
                if(float(self.t_av) > 0.0):
                        self.q_mpa=float((float(self.q)* float(self.d_av)/2*float(self.t_av)))
                else:
                        self.q_mpa=0.0
                
                self.arr_q_mpa.append(float(self.q_mpa)) 
                self.arr_t.append(float(self.t))
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                #print(" Timer P:"+str(self.p)+" q:"+str(self.q)+" t:"+str(self.t))
                print(" [G2 P1 ] arr_p_strain:"+str(self.p_strain)+" q_mpa:"+str(self.q_mpa)+" t:"+str(self.t))
                


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
        ''''
        self.x1.append(self.p)
        self.y1.append(self.q_mpa)
        self.x2.append(self.p)
        self.y2.append(self.t)

        self.xlist = [self.x1, self.x2]
        self.ylist = [self.y1, self.y2]
        #for index in range(0,1):
        for lnum,line in enumerate(self.lines):
            line.set_data(self.xlist[lnum], self.ylist[lnum]) # set data for each line separately.
        return self.lines
        '''

        self.line_cnt.set_data(self.arr_p_strain,self.arr_q_mpa)       
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
        connection = sqlite3.connect("tyr.db")
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
            print(" not Ok ") ### End G2 Auto P1
            
            
   


class PlotCanvasG2_Auto_P2(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="tyr"
        self.axes.set_xlabel('Expansion (mm)')
        self.axes.set_ylabel('Pressure (MPa)')
        self.axes.grid(which='major', linestyle='-', linewidth='0.50', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.50', color='black')
        
#         self.axes2 = self.axes.twinx()
#         color = 'tab:green'
#         self.axes2.set_ylabel('Time (Sec)', color = color)
#         self.axes2.set_ylim(0,500)
        
        
        
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.p_strain=0
        self.q =0
        self.t =170
        
        self.arr_p=[0.0]
        self.arr_q=[0.0]
        self.arr_t=[0.0]
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
        self.q_mpa =0
        self.arr_p_strain=[0.0]
        self.arr_q_mpa=[0.0]
        self.cs_area=0
        self.d_av=0
        self.t_av=0
        self.graph_type=""
        self.elapsed_time=0
        self.elapsed_time_show=0
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
   
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
        #self.line_cnt2, = self.axes2.plot([0,0], [0,0], lw=2)
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                cursor = connection.cursor()                            
                cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
        connection.commit();
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_ID,CURRENT_TIMESTAMP ,GRAPH_TYPE FROM TEST_MST_TMP") 
        for x in results:
                        self.axes.set_title('Sample ID :'+str(x[0])+" Date :"+str(x[1])[0:10]+"")                        
                        self.graph_type=str(x[2])
                        self.axes.set_xlabel('Time (Sec)')
                        self.axes.set_ylabel('Stress (MPa)')
                        self.cs_area= 0
        connection.close()
        
        
                   
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),CURR_UNIT_TYPE,PROOF_TEST_BY,PROOF_MAX_LOAD,PROOF_MAX_LENGTH,TEST_TIME_SEC,D_AV,T_AV from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=float(x[0])             
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
             self.proof_max_load=int(str("9999"))
             self.proof_max_length=float(str(x[8]))
             self.test_time_sec=int(str(x[9]))
             self.d_av=float((str(x[10])))
             self.t_av=float((str(x[11])))
             
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:
             #self.axes.set_xlim(0,int(x[0]))
             #self.axes.set_ylim(0,int(x[1]))
             #self.flexural_max_load=int(x[1])
             #self.xlim=int(x[0])
             #self.ylim=int(x[1])
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'STRESS_VS_TIME' LIMIT 1") 
        for x in results:
             self.axes.set_xlim(0,float(x[0]))
             self.axes.set_ylim(0,float(x[1]))          
        connection.close()
        
        
        '''
        
        '''
        self.test_guage_mm=609
        self.max_load=0
        self.cof_max_length=100
        #print("434Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
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
        except IOError:
                 self.ser=""
                 self.IO_error_flg=1
        
        '''
       
        
        '''
        self.timer1.setInterval(1000)     
        self.timer1.timeout.connect(self.update_graph)
        self.timer1.start(1)
   
        self.x1,self.y1 = [],[]
        self.x2,self.y2 = [],[]
        self.lines = []
        lobj = self.axes.plot([],[],lw=2)[0]
        #lobj2 = self.axes2.plot([],[],lw=2)[0]
        
        self.lines.append(lobj)
        #self.lines.append(lobj2)
        self.on_ani_start()
        
        
    def update_graph(self):
        self.end_time = datetime.datetime.now()
        self.elapsed_time=self.end_time-self.start_time
        if(self.IO_error_flg==0):
            '''
           
            '''
            try:
                self.line = self.ser.readline()
                #print("Timer Job o/p:"+str(self.line))
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
                '''
                self.r=170.00
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                self.arr_t.append(float(self.t))
                '''
                
                
                #self.q=abs(float(self.buff[1])) #fix val
                #self.t=abs(float(self.buff[3]))
                self.t=float(self.elapsed_time.seconds)
                #self.p=abs(float(self.buff[4])) #fix val
                self.p_strain=float(float(self.p)*100/float(20.00))
                self.arr_p_strain.append(float(self.p)*100/float(20.00))
                
                if(float(self.t_av) > 0.0):
                        self.q_mpa=float((float(self.q)* float(self.d_av)/2*float(self.t_av)))
                else:
                        self.q_mpa=0.0
                
                self.arr_q_mpa.append(float(self.q_mpa)) 
                self.arr_t.append(float(self.t))
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                print(" [G2 P2] P:"+str(self.p)+" q:"+str(self.q)+" t:"+str(self.t))
                

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
        '''
        self.x1.append(self.t)
        self.y1.append(self.q_mpa)
        self.x2.append(self.t)
        self.y2.append(self.t)

        self.xlist = [self.x1, self.x2]
        self.ylist = [self.y1, self.y2]
        #for index in range(0,1):
        for lnum,line in enumerate(self.lines):
            line.set_data(self.xlist[lnum], self.ylist[lnum]) # set data for each line separately.
        return self.lines
        '''

        self.line_cnt.set_data(self.arr_t,self.arr_q_mpa)       
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
        connection = sqlite3.connect("tyr.db")
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
            

            




















class PlotCanvasG2_blank(FigureCanvas):
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
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'PRESSURE_VS_EXPANSION' LIMIT 1") 
        for x in results:
             ax.set_xlim(0,float(x[0]))
             ax.set_ylim(0,float(x[1]))          
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])
        
        ax.plot(self.x,self.y,'b')
        ax.set_ylabel('Pressure (MPa) ')
        ax.set_xlabel('Expansion (mm)')
#        ax2 = ax.twinx()
#        color = 'tab:green'
#        ax2.set_ylabel('Time (Sec)', color = color)
#        ax2.set_ylim(0,500) 
          
        self.draw() 

class PlotCanvasG2_blank_P1(FigureCanvas):
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
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'STRESS_VS_STRAIN' LIMIT 1") 
        for x in results:
             ax.set_xlim(0,float(x[0]))
             ax.set_ylim(0,float(x[1]))          
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])
        
        ax.plot(self.x,self.y,'b')
        ax.set_ylabel('Stress (MPa) ')
        ax.set_xlabel('Strain (%)')
#        ax2 = ax.twinx()
#        color = 'tab:green'
#        ax2.set_ylabel('Time (Sec)', color = color)
#        ax2.set_ylim(0,500) 
#          
        self.draw() 




class PlotCanvasG2_blank_P2(FigureCanvas):
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
        results=connection.execute("SELECT X_SCALE_MAX,Y_SCALE_MAX from GRAPH_SCALES WHERE GRAPH_NAME= 'STRESS_VS_TIME' LIMIT 1") 
        for x in results:
             ax.set_xlim(0,float(x[0]))
             ax.set_ylim(0,float(x[1]))          
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])
        
        ax.plot(self.x,self.y,'b')
        ax.set_ylabel('Stress (Mpa) ')
        ax.set_xlabel('Time (Sec)')
#        ax2 = ax.twinx()
#        color = 'tab:green'
#        ax2.set_ylabel('Time (Sec)', color = color)
#        ax2.set_ylim(0,500) 
          
        self.draw() 

        
            
            
            
            
            
            
            
            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RL_01_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
