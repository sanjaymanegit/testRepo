
from pop_set_two_graphs import set_two_graphs_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow
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



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1370, 770)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1351, 711))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 670, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
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
        self.lcdNumber.setGeometry(QtCore.QRect(160, 620, 91, 41))
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("value", 100.0)
        self.lcdNumber.setProperty("intValue", 100)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(930, 20, 121, 31))
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
        self.pushButton_6.setGeometry(QtCore.QRect(770, 20, 141, 31))
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
        self.pushButton_7.setGeometry(QtCore.QRect(770, 60, 141, 31))
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
        self.pushButton_8.setGeometry(QtCore.QRect(930, 60, 121, 31))
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
        self.lcdNumber_2.setGeometry(QtCore.QRect(30, 620, 91, 41))
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
        self.lineEdit_17.setGeometry(QtCore.QRect(150, 90, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_79 = QtWidgets.QLabel(self.frame)
        self.label_79.setGeometry(QtCore.QRect(10, 90, 141, 31))
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
        self.line_18.setGeometry(QtCore.QRect(290, 0, 20, 141))
        self.line_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_18.setLineWidth(3)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.frame)
        self.line_19.setGeometry(QtCore.QRect(1070, 0, 20, 141))
        self.line_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_19.setLineWidth(3)
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setObjectName("line_19")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(770, 100, 141, 31))
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
        self.label_9.setGeometry(QtCore.QRect(780, 670, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_44.setGeometry(QtCore.QRect(870, 670, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_44.setFont(font)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 670, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_140 = QtWidgets.QLabel(self.frame)
        self.label_140.setGeometry(QtCore.QRect(540, 580, 101, 31))
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
        self.lineEdit_46.setGeometry(QtCore.QRect(540, 620, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_46.setFont(font)
        self.lineEdit_46.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.label_143 = QtWidgets.QLabel(self.frame)
        self.label_143.setGeometry(QtCore.QRect(670, 580, 101, 31))
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
        self.lineEdit_47.setGeometry(QtCore.QRect(670, 620, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_47.setFont(font)
        self.lineEdit_47.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_47.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.label_144 = QtWidgets.QLabel(self.frame)
        self.label_144.setGeometry(QtCore.QRect(800, 580, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_144.setFont(font)
        self.label_144.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_144.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_144.setObjectName("label_144")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_48.setGeometry(QtCore.QRect(310, 620, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_48.setFont(font)
        self.lineEdit_48.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_48.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.label_145 = QtWidgets.QLabel(self.frame)
        self.label_145.setGeometry(QtCore.QRect(40, 580, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_145.setFont(font)
        self.label_145.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_145.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_145.setObjectName("label_145")
        self.label_146 = QtWidgets.QLabel(self.frame)
        self.label_146.setGeometry(QtCore.QRect(160, 580, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_146.setFont(font)
        self.label_146.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_146.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_146.setObjectName("label_146")
        self.label_147 = QtWidgets.QLabel(self.frame)
        self.label_147.setGeometry(QtCore.QRect(310, 580, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_147.setFont(font)
        self.label_147.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_147.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_147.setObjectName("label_147")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_51.setGeometry(QtCore.QRect(800, 620, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_51.setFont(font)
        self.lineEdit_51.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_51.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.label_148 = QtWidgets.QLabel(self.frame)
        self.label_148.setGeometry(QtCore.QRect(430, 580, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_148.setFont(font)
        self.label_148.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_148.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_148.setObjectName("label_148")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_52.setGeometry(QtCore.QRect(430, 620, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_52.setFont(font)
        self.lineEdit_52.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_52.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(930, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(1110, 20, 211, 111))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/GIGSYSlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(150, 110))
        self.pushButton.setObjectName("pushButton")
        self.label_149 = QtWidgets.QLabel(self.frame)
        self.label_149.setGeometry(QtCore.QRect(960, 580, 81, 31))
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
        self.lineEdit_53.setGeometry(QtCore.QRect(960, 620, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_53.setFont(font)
        self.lineEdit_53.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_53.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.label_150 = QtWidgets.QLabel(self.frame)
        self.label_150.setGeometry(QtCore.QRect(120, 630, 41, 31))
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
        self.label_151.setGeometry(QtCore.QRect(260, 620, 41, 31))
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
        self.label_152.setGeometry(QtCore.QRect(380, 620, 41, 31))
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
        self.label_153.setGeometry(QtCore.QRect(1050, 620, 41, 31))
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
        self.label_154.setGeometry(QtCore.QRect(490, 630, 31, 21))
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
        self.label_155.setGeometry(QtCore.QRect(610, 620, 41, 31))
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
        self.label_156.setGeometry(QtCore.QRect(740, 620, 41, 31))
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
        self.label_157.setGeometry(QtCore.QRect(870, 620, 51, 31))
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
        self.label_15.setGeometry(QtCore.QRect(430, 670, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(330, 20, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(350, 80, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(340, 60, 371, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(1080, 670, 161, 31))
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
        self.line_20.setGeometry(QtCore.QRect(740, 0, 20, 141))
        self.line_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_20.setLineWidth(3)
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setObjectName("line_20")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 130, 1351, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 470, 441, 101))
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
        self.tableWidget_2.setGeometry(QtCore.QRect(460, 470, 441, 101))
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
        self.tableWidget_3.setGeometry(QtCore.QRect(900, 470, 431, 101))
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
        self.pushButton_17.setGeometry(QtCore.QRect(150, 160, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setGeometry(QtCore.QRect(570, 160, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setGeometry(QtCore.QRect(1050, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame)
        self.pushButton_20.setGeometry(QtCore.QRect(300, 670, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 190, 1311, 281))
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
        self.pushButton_21.setGeometry(QtCore.QRect(1100, 630, 91, 21))
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
        self.pushButton_22.setGeometry(QtCore.QRect(1230, 630, 91, 21))
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
        self.comboBox.setGeometry(QtCore.QRect(1188, 590, 141, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
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
        self.label_4.setGeometry(QtCore.QRect(1090, 590, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1370, 21))
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
        self.graph_type="STRESS_VS_STRAIN"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Start Logging"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "001"))
        self.pushButton_5.setText(_translate("MainWindow", "Email"))
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
        self.lineEdit_46.setText(_translate("MainWindow", "355"))
        self.label_143.setText(_translate("MainWindow", "Thickness (mm):"))
        self.lineEdit_47.setText(_translate("MainWindow", "355"))
        self.label_144.setText(_translate("MainWindow", "Circumference (mm):"))
        self.lineEdit_48.setText(_translate("MainWindow", "355"))
        self.label_145.setText(_translate("MainWindow", "Pressure :"))
        self.label_146.setText(_translate("MainWindow", "Expansion :"))
        self.label_147.setText(_translate("MainWindow", "Stress :"))
        self.lineEdit_51.setText(_translate("MainWindow", "355"))
        self.label_148.setText(_translate("MainWindow", "Strain :"))
        self.lineEdit_52.setText(_translate("MainWindow", "355"))
        self.pushButton_15.setText(_translate("MainWindow", "Return"))
        self.label_149.setText(_translate("MainWindow", "Graph Time :"))
        self.lineEdit_53.setText(_translate("MainWindow", "12:55"))
        self.label_150.setText(_translate("MainWindow", " (MPa) "))
        self.label_151.setText(_translate("MainWindow", " (mm) "))
        self.label_152.setText(_translate("MainWindow", "(MPa) "))
        self.label_153.setText(_translate("MainWindow", "MI:SS"))
        self.label_154.setText(_translate("MainWindow", "(%) "))
        self.label_155.setText(_translate("MainWindow", " (mm)"))
        self.label_156.setText(_translate("MainWindow", " (mm)"))
        self.label_157.setText(_translate("MainWindow", " (mm)"))
        self.label_15.setText(_translate("MainWindow", "Data Saved Successfully !"))
        self.label.setText(_translate("MainWindow", "Company Name Pvt. Ltd"))
        self.label_2.setText(_translate("MainWindow", "Blue Star IT PArk ,\n"
"  MIDC , Thane ,  Mumbai Andhrei  Pin No 400232"))
        self.label_3.setText(_translate("MainWindow", "29-Nov-2022 11:22:33"))
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
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Pressure"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "233.2"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "22-11-2011 03:44:55"))
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
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainWindow", "Expansion"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("MainWindow", "233.2"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("MainWindow", "22-11-2011 03:44:55"))
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
        item = self.tableWidget_3.item(0, 0)
        item.setText(_translate("MainWindow", "Stress"))
        item = self.tableWidget_3.item(0, 1)
        item.setText(_translate("MainWindow", "233.2"))
        item = self.tableWidget_3.item(0, 2)
        item.setText(_translate("MainWindow", "22-11-2011 03:44:55"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.pushButton_17.setText(_translate("MainWindow", "Pressure Vs  Time"))
        self.pushButton_18.setText(_translate("MainWindow", "Expansion Vs Time"))
        self.pushButton_19.setText(_translate("MainWindow", "Stress Vs Time"))
        self.pushButton_20.setText(_translate("MainWindow", "View Log"))
        self.pushButton_21.setText(_translate("MainWindow", "Graph set -1"))
        self.pushButton_22.setText(_translate("MainWindow", "Graph set -2"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Stress Vs Strain"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Pressure Vs Expansion"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Pressure Vs Time"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Expansion Vs Time"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Stress Vs Time"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Strain Vs Time"))
        self.label_4.setText(_translate("MainWindow", "Report Graph :"))
        self.display_bank_graphs()
        self.load_ops()

    def load_ops(self):
        self.pushButton_15.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(self.start_test_expansion)
        self.pushButton_9.clicked.connect(self.mannual_stop)
        
        self.pushButton_16.clicked.connect(self.pop_graph_scales)
        
        
        self.pushButton_5.clicked.connect(self.open_email_report)    
        self.pushButton_7.clicked.connect(self.open_pdf)
        self.pushButton_6.clicked.connect(self.open_comment_popup)
        self.pushButton_8.clicked.connect(self.print_file)
        self.pushButton_18.clicked.connect(self.graph_type_strain)
        self.pushButton_17.clicked.connect(self.graph_type_pressure)
        
       
        
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        
        
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
       
        #self.load_data()
        #self.graph_type_pressure()

    def graph_type_strain(self):
        self.graph_type="STRESS_VS_STRAIN"
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='"+str(self.graph_type)+"'")                 
        connection.commit()
        connection.close()
        self.sc_blank =PlotCanvas_blank(self)
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select count(*) from TEST_MST_EXPANSION WHERE TEST_ID = '"+str(int(self.label_12.text()))+"'")       
        for x in results:           
                 if(int(x[0]) > 0):
                            self.sc_blank =PlotCanvas(self,width=5, height=4, dpi=80) 
                 else:
                            self.sc_blank =PlotCanvas_blank(self,width=5, height=4, dpi=80)
        
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)   
        self.pushButton_18.hide()
        self.pushButton_17.show()
        
        #self.label_13.setText("Stress(MPa)")
        #self.label_14.setText("Strain(%)")
        
        
    def graph_type_pressure(self):
        self.graph_type="PRESSURE_VS_ELONGATION"
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='"+str(self.graph_type)+"'")                 
        connection.commit()
        connection.close()
        self.sc_blank =PlotCanvas_blank(self)
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select count(*) from TEST_MST_EXPANSION WHERE TEST_ID = '"+str(int(self.label_12.text()))+"'")       
        for x in results:           
                 if(int(x[0]) > 0):
                            self.sc_blank =PlotCanvas(self,width=5, height=4, dpi=80) 
                 else:
                            self.sc_blank =PlotCanvas_blank(self,width=5, height=4, dpi=80)
        
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.pushButton_17.hide()
        self.pushButton_18.show()
        
        self.label_13.setText("Pressure(MPa)")
        self.label_14.setText("Elongation(mm)")
        




    def display_bank_graphs(self):
        self.sc_blank =PlotCanvas_blank(self,width=5, height=4, dpi=80)          
        self.gridLayout.addWidget(self.sc_blank, 0, 0, 1, 1)
        
        self.sc_blank_p1 =PlotCanvas_blank_P1(self,width=5, height=4, dpi=80)
        self.gridLayout.addWidget(self.sc_blank_p1, 0, 1, 1, 1)
        
        
        self.sc_blank_p2 =PlotCanvas_blank_P2(self,width=5, height=4, dpi=80)
        self.gridLayout.addWidget(self.sc_blank_p2, 0, 2, 1, 1)
        
    def load_data(self):
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'TEST_MST_EXPANSION'")       
        for x in results:           
                 self.label_12.setText(str(x[0]).zfill(3))
                 self.test_id=str(x[0])                 
        connection.close()
        
        
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select SPECIMEN_NAME,NOMINAL_OUTER_DIA_MM,GREAD,NOMINAL_WALL_THICKNESS_MM,SPECIFIED_YEILD_STRENGTH"
                                   ",SAMPLE_IDENTIFICATION_NO,SAMPLE_DESCRIPTION,MILL_HYDROTEST_PRESSURE,GRAPH_TYPE,PRESSURE_TRANDUSER_NO,FORCE_SAPN_ON_PDSC,"
                                   "LAST_CAL_DATE_1,EXTENSOMETER_NO,POSITION_SPAN_ON_PDSC,LAST_CAL_DATE_2,YEILD_STRENGTH,MODULUS_OF_ELASTICITY,REVIEWED_BY,TEST_DATE,TESTED_BY FROM TEST_MST_TMP")                 
        for x in results:
                    #self.label_64.setText(str(x[0]))  #combobox
                    self.lineEdit_9.setText(str(x[1])) #NOMINAL_OUTER_DIA_MM,
                    self.lineEdit_11.setText(str(x[2])) #GREAD
                    self.lineEdit_3.setText(str(x[3])) #NOMINAL_WALL_THICKNESS_MM
                    self.lineEdit_14.setText(str(x[4])) #SPECIFIED_YEILD_STRENGTH
                    self.lineEdit_16.setText(str(x[5])) #SAMPLE_IDENTIFICATION_NO
                    self.lineEdit_17.setText(str(x[6])) #SAMPLE_DESCRIPTION
                    self.lineEdit_18.setText(str(x[7])) #MILL_HYDROTEST_PRESSURE
                    #self.lineEdit_3.setText(str(x[8])) #GRAPH_TYPE                    
                    
                    self.lineEdit_19.setText(str(x[9])) #PRESSURE_TRANDUSER_NO
                    self.lineEdit_20.setText(str(x[10])) #FORCE_SAPN_ON_PDSC
                    self.lineEdit_21.setText(str(x[11])) #LAST_CAL_DATE_1
                    self.lineEdit_22.setText(str(x[12])) #EXTENSOMETER_NO
                    self.lineEdit_23.setText(str(x[13])) #POSITION_SPAN_ON_PDSC
                    self.lineEdit_24.setText(str(x[14])) #LAST_CAL_DATE_2
                    
                    self.lineEdit_42.setText("0") #YEILD_STRENGTH
                    self.lineEdit_43.setText("0") #MODULUS_OF_ELASTICITY
                    self.lineEdit_44.setText(str(x[17])) #REVIEWED_BY
                    #self.label_18.setText(str(x[43])) #TEST_DATE
                    self.lineEdit_15.setText(str(x[19]))#TESTED_BY
              
        connection.close()
        
    def start_test_expansion(self):               
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
        if(self.lineEdit_9.text() == ""): #    
                    self.label_22.show()
                    self.label_22.setText("Nominal Outer Dia. Should not Empty.")                    
        elif(self.lineEdit_11.text() == ""): #    
                    self.label_22.show()
                    self.label_22.setText("Gread Should not Empty.")               
        elif(self.lineEdit_3.text() == ""): #    
                    self.label_22.show()
                    self.label_22.setText("Nominal Wall Thickness Should not Empty. ")
        elif(self.lineEdit_14.text() == ""): #    
                    self.label_22.show()
                    self.label_22.setText("SMYS Should not Empty .")
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
                                    cursor.execute("UPDATE  TEST_MST_TMP SET TEST_ID='"+str(int(self.label_12.text()))+
                                                    "',NOMINAL_OUTER_DIA_MM='"+str(self.lineEdit_9.text())+
                                                    "',GREAD='"+str(self.lineEdit_11.text())+
                                                    "', NOMINAL_WALL_THICKNESS_MM='"+str(self.lineEdit_3.text())+
                                                    "', SPECIFIED_YEILD_STRENGTH='"+str(self.lineEdit_14.text())+
                                                    "', SAMPLE_IDENTIFICATION_NO='"+str(self.lineEdit_16.text())+
                                                    "', SAMPLE_DESCRIPTION='"+str(self.lineEdit_17.text())+
                                                    "', MILL_HYDROTEST_PRESSURE='"+str(self.lineEdit_18.text())+
                                                    "', PRESSURE_TRANDUSER_NO='"+str(self.lineEdit_19.text())+
                                                    "', FORCE_SAPN_ON_PDSC='"+str(self.lineEdit_20.text())+
                                                    "', LAST_CAL_DATE_1='"+str(self.lineEdit_21.text())+
                                                    "', EXTENSOMETER_NO='"+str(self.lineEdit_22.text())+
                                                    "', POSITION_SPAN_ON_PDSC='"+str(self.lineEdit_23.text())+
                                                    "', LAST_CAL_DATE_2='"+str(self.lineEdit_24.text())+                                                   
                                                    "', YEILD_STRENGTH=0"
                                                    ", MODULUS_OF_ELASTICITY=0"
                                                    ", REVIEWED_BY='"+str(self.lineEdit_44.text())+
                                                   # "', TEST_DATE='"+str(self.label_18.text())+
                                                    "', GRAPH_TYPE='"+str(self.graph_type)+
                                                    "' ")

                            except Exception as e:
                                              print("UPDATE SQL Error-TEST_MST_TMP No- 1:"+str(e))
                                              connection.commit();
                            cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_AREA=( SELECT  (SAMPLE_WIDTH_MM * T_AV)*0.1*0.1 FROM TEST_MST_TMP)")
                                              
                            try:
                                    cursor.execute("UPDATE  TEST_MST_EXPANSION SET "+
                                                    "NOMINAL_OUTER_DIA_MM='"+str(self.lineEdit_9.text())+
                                                    "',GREAD='"+str(self.lineEdit_11.text())+
                                                    "', NOMINAL_WALL_THICKNESS_MM='"+str(self.lineEdit_3.text())+
                                                    "', SPECIFIED_YEILD_STRENGTH='"+str(self.lineEdit_14.text())+
                                                    "', SAMPLE_IDENTIFICATION_NO='"+str(self.lineEdit_16.text())+
                                                    "', SAMPLE_DESCRIPTION='"+str(self.lineEdit_17.text())+
                                                    "', MILL_HYDROTEST_PRESSURE='"+str(self.lineEdit_18.text())+
                                                    "', PRESSURE_TRANDUSER_NO='"+str(self.lineEdit_19.text())+
                                                    "', FORCE_SAPN_ON_PDSC='"+str(self.lineEdit_20.text())+
                                                    "', LAST_CAL_DATE_1='"+str(self.lineEdit_21.text())+
                                                    "', EXTENSOMETER_NO='"+str(self.lineEdit_22.text())+
                                                    "', POSITION_SPAN_ON_PDSC='"+str(self.lineEdit_23.text())+
                                                    "', LAST_CAL_DATE_2='"+str(self.lineEdit_24.text())+                                                  
                                                    "', YEILD_STRENGTH='0"
                                                    "', MODULUS_OF_ELASTICITY='0"
                                                    "', REVIEWED_BY='"+str(self.lineEdit_44.text())+
                                                    #"', TEST_DATE='"+str(self.label_18.text())+
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
                                      
                                      
                                      
                                      cursor.execute("INSERT INTO TEST_MST_EXPANSION (TEST_ID,NOMINAL_OUTER_DIA_MM,GREAD, NOMINAL_WALL_THICKNESS_MM,SPECIFIED_YEILD_STRENGTH,"
                                                    "SAMPLE_IDENTIFICATION_NO,SAMPLE_DESCRIPTION,MILL_HYDROTEST_PRESSURE, "
                                                    "PRESSURE_TRANDUSER_NO,FORCE_SAPN_ON_PDSC, LAST_CAL_DATE_1,"
                                                    "EXTENSOMETER_NO,POSITION_SPAN_ON_PDSC,LAST_CAL_DATE_2,YEILD_STRENGTH,MODULUS_OF_ELASTICITY, REVIEWED_BY,"
                                                    "TESTED_BY,GRAPH_TYPE)"
                                                    "VALUES("
                                                           "'"+str(self.label_12.text())+"',"   #TEST_ID
                                                                "'"+str(self.lineEdit_9.text())+"'," #NOMINAL_OUTER_DIA_MM
                                                                "'"+str(self.lineEdit_11.text())+"'," #GREAD
                                                                "'"+str(self.lineEdit_3.text())+"'," #NOMINAL_WALL_THICKNESS_MM
                                                                "'"+str(self.lineEdit_14.text())+"'," #SPECIFIED_YEILD_STRENGTH
                                                                "'"+str(self.lineEdit_16.text())+"'," #SAMPLE_IDENTIFICATION_NO
                                                                "'"+str(self.lineEdit_17.text())+"'," #SAMPLE_DESCRIPTION
                                                                "'"+str(self.lineEdit_18.text())+"'," #MILL_HYDROTEST_PRESSURE
                                                                "'"+str(self.lineEdit_19.text())+"'," #PRESSURE_TRANDUSER_NO
                                                                "'"+str(self.lineEdit_20.text())+"'," #FORCE_SAPN_ON_PDSC
                                                                "'"+str(self.lineEdit_21.text())+"'," #LAST_CAL_DATE_1
                                                                "'"+str(self.lineEdit_22.text())+"'," #EXTENSOMETER_NO
                                                                "'"+str(self.lineEdit_23.text())+"'," #POSITION_SPAN_ON_PDSC
                                                                "'"+str(self.lineEdit_24.text())+"'," #LAST_CAL_DATE_2                                                               
                                                                "0,"  
                                                                "0," 
                                                                "'"+str(self.lineEdit_44.text())+"'," #REVIEWED_BY
                                                                #"'"+str(self.label_18.text())+"'," #TEST_DATE
                                                                "'"+str(self.lineEdit_15.text())+"'," #TESTED_BY
                                                                "'"+self.graph_type+"')" #GRAPH_TYPE
                                                                )
                                      print("inserted OK ")


                              except Exception as e:
                                              print("INSERT  SQL Error-TEST_MST_EXPANSION No- 2:"+str(e))
                                              connection.commit();

                              try:
                                    cursor.execute("UPDATE  TEST_MST_TMP SET TEST_ID='"+str(self.label_12.text())+
                                                    "',NOMINAL_OUTER_DIA_MM='"+str(self.lineEdit_9.text())+
                                                    "',GREAD='"+str(self.lineEdit_11.text())+
                                                    "', NOMINAL_WALL_THICKNESS_MM='"+str(self.lineEdit_3.text())+
                                                    "', SPECIFIED_YEILD_STRENGTH='"+str(self.lineEdit_14.text())+
                                                    "', SAMPLE_IDENTIFICATION_NO='"+str(self.lineEdit_16.text())+
                                                    "', SAMPLE_DESCRIPTION='"+str(self.lineEdit_17.text())+
                                                    "', MILL_HYDROTEST_PRESSURE='"+str(self.lineEdit_18.text())+
                                                    "', PRESSURE_TRANDUSER_NO='"+str(self.lineEdit_19.text())+
                                                    "', FORCE_SAPN_ON_PDSC='"+str(self.lineEdit_20.text())+
                                                    "', LAST_CAL_DATE_1='"+str(self.lineEdit_21.text())+
                                                    "', EXTENSOMETER_NO='"+str(self.lineEdit_22.text())+
                                                    "', POSITION_SPAN_ON_PDSC='"+str(self.lineEdit_23.text())+
                                                    "', LAST_CAL_DATE_2='"+str(self.lineEdit_24.text())+                                                   
                                                    "', YEILD_STRENGTH=0"+
                                                    ", MODULUS_OF_ELASTICITY=0"+
                                                    ", REVIEWED_BY='"+str(self.lineEdit_44.text())+
                                                    #"', TEST_DATE='"+str(self.label_18.text())+                                                   
                                                    "' ")
                                    print("updated  OK ")

                              except Exception as e:
                                              print("UPDATE SQL Error-TEST_MST_TMP No- 4:"+str(e))
                                              connection.commit();

                              cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_AREA=(SELECT  (SAMPLE_WIDTH_MM * T_AV)*0.1*0.1 FROM TEST_MST_TMP)")
                           
                        connection.commit();
                        connection.close()
                        
    def mannual_stop(self):
                self.sc_new.save_data_flg="Yes"
                self.reset()
                self.save_graph_data()
                self.sc_new.save_data_flg=""
                self.label_22.show()
                self.label_22.setText("Data Saved Successfully.")
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                if(self.graph_type == "STRESS_VS_STRAIN"):
                        self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q)))        
                        self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p_strain)))   #length                        
                    
                else:    
                        self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q)))        
                        self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p)))   #length
                        
                self.label_22.setText("")
    
    def reset(self):        
            if(self.timer3.isActive()): 
                  self.timer3.stop()      
            
            if(self.sc_new.timer1.isActive()): 
                  self.sc_new.timer1.stop()            
           
            self.lcdNumber.setProperty("value", 0.0)
            self.lcdNumber_2.setProperty("value", 0.0)
            
    def show_load_cell_val(self):        
            if(self.graph_type == "STRESS_VS_STRAIN"):                
                            self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q)))        
                            self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p_strain)))   #length
            else:    
                            self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q)))        
                            self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p)))   #length           
            self.label_22.setText("Running.....")
            if(str(self.sc_new.save_data_flg) =="Yes"):            
                    self.reset()
                    self.save_graph_data()
                    self.sc_new.save_data_flg=""
                    self.label_22.show()
                    self.label_22.setText("Data Saved Successfully.")
                    #self.go_to_next=self.go_to_next+1
                    self.pushButton_5.setEnabled(True)
                    self.pushButton_6.setEnabled(True)
                    self.pushButton_7.setEnabled(True)
                    self.pushButton_8.setEnabled(True)
                    
                    if(self.graph_type == "STRESS_VS_STRAIN"):
                            self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q)))        
                            self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p_strain)))   #length                        
                        
                    else:    
                            self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q)))        
                            self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p)))   #length
                            
                    self.label_22.setText("")    
                    
    def save_graph_data(self):         
         if (len(self.sc_new.arr_p) > 1):            
            
            #self.cycle_num=int(str(self.label_67.text()))+1
            
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)):                     
                        cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM_N,Y_NUM_LB,Y_NUM_MPA,X_STRAIN) VALUES ('"+str(float(self.sc_new.arr_p[g]))+"','"+str(float(self.sc_new.arr_q[g]))+"','"+str(self.sc_new.arr_p_cm[g])+"','"+str(self.sc_new.arr_p_inch[g])+"','"+str(self.sc_new.arr_q_n[g])+"','"+str(self.sc_new.arr_q_lb[g])+"','"+str(float(self.sc_new.arr_q_mpa[g]))+"','"+str(float(self.sc_new.arr_p_strain[g]))+"')")
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
                           

                          cursor.execute("UPDATE TEST_MST_EXPANSION SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL")                          
                          cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM,X_NUM_CM,Y_NUM_N,Y_NUM_MPA,X_NUM_STRAIN) SELECT X_NUM,Y_NUM,X_NUM_CM,Y_NUM_N,Y_NUM_MPA,X_STRAIN FROM STG_GRAPH_MST")                  
                          cursor.execute("UPDATE GRAPH_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL") 
                          cursor.execute("UPDATE TEST_MST_EXPANSION SET GRAPH_STATUS='LOADED GRAPH'  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")                  
                          cursor.execute("UPDATE TEST_MST_EXPANSION SET GRAPH_SCAL_X_LENGTH=(SELECT GRAPH_SCALE_CELL_2 FROM SETTING_MST),GRAPH_SCAL_Y_LOAD=(SELECT GRAPH_SCALE_CELL_1 FROM SETTING_MST)  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                          cursor.execute("UPDATE TEST_MST_EXPANSION SET YEILD_STRENGTH=(SELECT YEILD_STRENGTH FROM TEST_MST_TMP),MODULUS_OF_ELASTICITY=(SELECT MODULUS_OF_ELASTICITY FROM TEST_MST_TMP)  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                    
                          #cursor.execute("UPDATE TEST_MST_EXPANSION SET GRAPH_SCAL_X_LENGTH=(SELECT GRAPH_SCALE_CELL_2 FROM SETTING_MST),GRAPH_SCAL_Y_LOAD=(SELECT GRAPH_SCALE_CELL_1 FROM SETTING_MST)  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                    
                  
                  #update max load , yead strength , modulus 
                  
                  except Exception as e:
                          print("SQL Error:"+str(e))
                          connection.commit();
                          
            connection.commit();
            connection.close()            
            print("Data Saved Ok in STG_GRAPH_MST")           
            #self.show_grid_data_PROOF()
     
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("select printf(\"%.2f\", YEILD_STRENGTH),printf(\"%.2f\", MODULUS_OF_ELASTICITY) FROM TEST_MST_EXPANSION WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")                 
            for x in results:                
                    self.lineEdit_42.setText(str(x[0])) #YEILD_STRENGTH
                    self.lineEdit_43.setText(str(x[1])) #MODULUS_OF_ELASTICITY    
            connection.close() 
            
    def print_file(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POP_TEST_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_pdf(self):
        self.sc_data =PlotCanvas(self,width=8, height=4,dpi=80) 
        self.create_pdf_expansion() 
        
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
        results=connection.execute("SELECT TEST_DATE,TESTED_BY,SAMPLE_IDENTIFICATION_NO,SAMPLE_DESCRIPTION,MILL_HYDROTEST_PRESSURE,REMARK FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(int(self.label_12.text()))+"'")
        for x in results:
            summary_data=[["Parameter","Value","Prarameter","Value"],["Date: ",str(x[0]),"Tested By: ",str(x[1])],["Test Report File Name : ",str("Report_of_test_"+self.label_12.text()),"Sample Identification #: ",str(x[2])],["Sample Description:  ",str(x[3]),"Mill Hydrotest Pressure(MPa):",str(x[4])]]
            self.remark=str(x[5])        
        connection.close() 
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT NOMINAL_OUTER_DIA_MM, GREAD,NOMINAL_WALL_THICKNESS_MM,SPECIFIED_YEILD_STRENGTH   FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(int(self.label_12.text()))+"'")
        for x in results:
            #summary_data2=[["Nominal Outer Dia.(mm): ",str(x[0]),"Grade: ",str(x[1])],["Nominal Wall Thickness(mm) : ",str(x[2]),"Specified Yield Strength(MPa)",str(x[3])]]
            #self.remark=str(x[5])
            summary_data.append(["Nominal Outer Dia.(mm): ",str(x[0]),"Grade: ",str(x[1])])
            summary_data.append(["Nominal Wall Thickness(mm) : ",str(x[2]),"",""])
            summary_data.append(["Specified Yield Strength(MPa)",str(x[3]),"",""])
        connection.close() 
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT PRESSURE_TRANDUSER_NO,PRELOAD_PERC,FORCE_SAPN_ON_PDSC,PRELOAD_PRESSURE__MPA,LAST_CAL_DATE_1,NEVER_EXCEED_TEST_PRESSURE,EXTENSOMETER_NO,EXTENSOMETER_CHAIN_LENGTH,POSITION_SPAN_ON_PDSC,MAX_EXTENSION,LAST_CAL_DATE_2,MAX_ELONGATION_PRC,EXTENSION_RATE   FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(int(self.label_12.text()))+"'")
        for x in results:
            summary_data.append(["Pressure Transducer No: ",str(x[0]),"Preload Percentage: ",str(x[1])])
            summary_data.append(["Force Span on PDSC : ",str(x[2])," "," "])
            summary_data.append(["Pre-load Pressure(Mpa): ",str(x[3]),"Last Calibration Date1: ",str(x[4])])
            summary_data.append(["NEVER EXCEED Test Pressure (MPa) : ",str(x[5]),"Extensometer :",str(x[6])])
            summary_data.append(["Extensometer Chain length(Links): ",str(x[7]),"Position Span On PDSC: ",str(x[8])])
            summary_data.append(["Max Extension : ",str(x[9]),"Last Calibration Date2 :",str(x[10])])
            summary_data.append(["Extension Rate (mm/min): ",str(x[12]),"Max Elongation Percentage: ",str(x[11])])
        connection.close() 
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT THICKNESS_1,THICKNESS_2,THICKNESS_3,THICKNESS_4,THICKNESS_5,THICKNESS_6,PRELOAD_PRESSURE_MPA,DIAMETER_1,DIAMETER_2,DIAMETER_3,SAMPLE_WIDTH_MM,IS_TESTED,D_AV,T_AV  FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(int(self.label_12.text()))+"'")
        for x in results:
            summary_data.append(["Thinckness_1 (mm): ",str(x[0]),"Preload Pressure (MPa): ",str(x[6])])
            summary_data.append(["Thinckness_2 (mm) : ",str(x[1]),"",""])
            summary_data.append(["Thinckness_3 (mm): ",str(x[2]),"Diameter_1(mm): ",str(x[7])])
            summary_data.append(["Thinckness_4 (mm) : ",str(x[3]),"Sample Width (mm) ",str(x[10])])
            summary_data.append(["Thinckness_5 (mm) ",str(x[4]),"Diameter_2(mm): ",str(x[8])])
            summary_data.append(["Thinckness_6 (mm): ",str(x[5]),"Diameter_3(mm): ",str(x[9])])
            summary_data.append([" ","","Tested ? : ",str(x[11])])
            summary_data.append(["D_AV (mm) : ",str(x[12]),"T_AV (mm): ",str(x[13])])
        connection.close() 
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT MIN_EXT,printf(\"%.2f\", YEILD_STRENGTH),MAX_EXT,printf(\"%.2f\", MODULUS_OF_ELASTICITY),MAX_PRESSURE_MPA,REVIEWED_BY,TEST_DATE  FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(int(self.label_12.text()))+"'")
        for x in results:
            summary_data2=[["Parameter","Value","Prarameter","Value"]]
            summary_data2.append(["Min Ext.(mm): ",str(x[0]),"0.5 % TE Yeild Strength(MPa): ",str(x[1])])
            summary_data2.append(["Max Ext.(mm) : ",str(x[2]),"Modulud of Elasticity (GPa)",str(x[3])])
            summary_data2.append(["Max Pressure (MPa): ",str(x[4]),"Reviewed By: ",str(x[5])])
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
         
        f2=Table(summary_data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 8),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
#        
#        f3=Table(summary_data3)
#        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 8),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
#        
#        f4=Table(summary_data4)
#        f4.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 8),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
#        
         
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        #Elements=[Title,Title2,Spacer(1,12),f4,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,blank,blank,blank,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        Elements=[Title,Title2,Spacer(1,12),f,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
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
        
#        ax1 = self.figure.add_subplot(212)
#       
#        ax1.set_facecolor('#CCFFFF')   
#        ax1.minorticks_on()
#        
#        ax1.grid(which='major', linestyle='-', linewidth='0.5', color='red')
#        ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
#        
#        ax1.set_xlabel('Elongation (mm)')
#        ax1.set_ylabel('Pressure (MPa)')  
        
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
        
        
        
        
        self.unit_type="Kgf/mm"
        ### Univarsal change for  Graphs #####################
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT FLOW_TIME_X_AXIS,FLOW_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS, VOLUMN_TIME_Y_AXIS FROM OTER_INFO") 
        for x in results:             
                 
                 if(self.graph_type == "STRESS_VS_STRAIN"):
                         ax.set_xlim(0,float(x[2]))
                         ax.set_ylim(0,float(x[3]))
                 else:
                         ax.set_xlim(0,float(x[0]))
                         ax.set_ylim(0,float(x[1]))
                         
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_ID,SAMPLE_IDENTIFICATION_NO ,TEST_DATE FROM TEST_MST_EXPANSION WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
             ax.set_title('Sample ID :'+str(x[1])+" Date:"+str(x[2])[0:10]+"") 
             self.graph_ids.append(x[0])             
        connection.close()
        
        
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
            self.x1_num=[0.0]
            self.y1_num=[0.0]
            print(" Unit Type :"+str(self.unit_type))
            
            
            if(self.graph_type == "STRESS_VS_STRAIN"):
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT X_NUM_CM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    ax.set_xlabel('Strain (%)')
                    ax.set_ylabel('Stress (MPa)')
                    for k in results:        
                                        self.x_num.append(float(k[0])/float(self.cs_area))
                                        self.y_num.append(float(k[1]))
                    connection.close() 
            else:
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    ax.set_xlabel(' Elongation(mm)')
                    ax.set_ylabel('Pressure (MPa)')
                    for k in results:        
                                        self.x_num.append(float(k[0]))
                                        self.y_num.append(float(k[1]))
                    connection.close()
              
            
            ax.plot(self.x_num,self.y_num, 'b',label="Sample No:1")
            #ax1.plot(self.x1_num,self.y1_num, 'b',label="Sample No:1")
            
        print("self.test_type:"+str(self.test_type))
        
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
        
#        self.axes1 = fig.add_subplot(212)
#        
#        self.axes1.set_facecolor('#CCFFFF')  
#        self.axes1.minorticks_on()
#        
#        self.axes1.grid(which='major', linestyle='-', linewidth='0.5', color='red')
#        self.axes1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
#        
        
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
        
        
        
        
        self.arr_p=[0.0]
        self.arr_p_cm=[0.0]
        self.arr_p_inch=[0.0]
        self.arr_p_strain=[0.0]
        
        
        self.arr_q=[0.0]
        self.arr_q_n=[0.0]
        self.arr_q_lb=[0.0]
        self.arr_q_mpa=[0.0]
        
        
        
        
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
        self.graph_type=""       
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
    
    def plot_auto(self):
        self.line_cnt, = self.axes.plot([0,0], [0,0], lw=2)
        #self.line_cnt2, = self.axes1.plot([0,0], [0,0], lw=2)
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                cursor = connection.cursor()                            
                cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
        connection.commit();
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_IDENTIFICATION_NO,CURRENT_TIMESTAMP ,(SAMPLE_WIDTH_MM * T_AV)*0.1*0.1 as CS_AREA_CM,GRAPH_TYPE FROM TEST_MST_TMP") 
        for x in results:
                        self.axes.set_title('Sample ID :'+str(x[0])+" Date :"+str(x[1])[0:10]+"")
                        self.cs_area=float(x[2])
                        self.graph_type=str(x[3])
        connection.close()
        if(self.graph_type=='STRESS_VS_STRAIN'):
                    self.axes.set_xlabel('Strain (%)')
                    self.axes.set_ylabel('Stress (MPa)')                
        else:
                    self.axes.set_xlabel('Elongation (mm)')
                    self.axes.set_ylabel('Pressure (MPa)') 
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
            
             
             self.proof_max_load=int(str("9999"))
             self.proof_max_length=float(str(x[8]))
             self.test_time_sec=int(str(x[9]))
             
        connection.close()
        print(" xxx     gfgf self.unit_type:"+str(self.unit_type))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:  
                     #self.axes1.set_xlim(0,float(x[0]))
                     #self.axes1.set_ylim(0,float(x[1]))
                     #self.flexural_max_load=int(x[1])
                     self.xlim=float(x[0])
                     self.ylim=float(x[1])
                      
                     self.auto_rev_time_off=int(x[2])
                     self.break_sence=int(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT FLOW_TIME_X_AXIS,FLOW_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS, VOLUMN_TIME_Y_AXIS FROM OTER_INFO") 
        for x in results:             
                 
                 if(self.graph_type == "STRESS_VS_STRAIN"):
                         self.axes.set_xlim(0,float(x[2]))
                         self.axes.set_ylim(0,float(x[3]))
                 else:
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
                 
                 
                 
                 
                 
                self.q=abs(float(self.buff[0])) #fix val
                self.t=abs(float(self.buff[3]))
                self.p=abs(float(self.buff[4])) #fix val
                
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
                
                self.arr_p_strain.append(float(self.p_cm)/float(self.cs_area))
                
                
                self.q=float(self.q)
                self.q_n=float(self.q)*9.81
                self.arr_q_n.append(float(self.q_n))
                
                self.q_lb=float(self.q)*2.20462
                self.arr_q_lb.append(float(self.q_lb))
                
                if(float(self.cs_area) > 0.0):
                        self.q_mpa=float((float(self.q)/float(self.cs_area))*0.0980665)
                else:
                        self.q_mpa=0.0
                
                self.arr_q_mpa.append(float(self.q_mpa))
                
                
                
                
                
                
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                print(" Timer P:"+str(self.p)+" q:"+str(self.q))
                
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
        if(self.graph_type=='STRESS_VS_STRAIN'):    
            self.line_cnt.set_data(self.arr_p_strain,self.arr_q)
        else:
            self.line_cnt.set_data(self.arr_p,self.arr_q)
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
       
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_TYPE from TEST_MST_TMP") 
        for x in results:
                self.graph_type=str(x[0]) 
        connection.close() 
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT FLOW_TIME_X_AXIS,FLOW_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS, VOLUMN_TIME_Y_AXIS FROM OTER_INFO") 
        for x in results:             
                 
                 if(self.graph_type == "STRESS_VS_STRAIN"):
                         ax.set_xlabel('Strain (%)')
                         ax.set_ylabel('Stress (MPa)')
                         ax.set_xlim(0,float(x[2]))
                         ax.set_ylim(0,float(x[3]))
                 else:
                         ax.set_xlabel('Elongation (mm)')
                         ax.set_ylabel('Pressure (MPa)')
                         ax.set_xlim(0,float(x[0]))
                         ax.set_ylim(0,float(x[1]))
                         

                         
                         
                              
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])
        
        
        ax.plot(self.x,self.y,'b')
        
        ########
        '''
       
        self.x1=[0,0,0,0,0,0,0,0]
        self.y1=[0,0,0,0,0,0,0,0]
        
        self.p1=list()
        self.q1=list()
        
        ax1 = self.figure.add_subplot(212)
        ax1.set_facecolor('#CCFFFF')
        ax1.minorticks_on()
        ax1.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:             
                 ax1.set_xlim(0,float(x[0]))
                 ax1.set_ylim(0,float(x[1]))
                 ax1.set_xlabel('Elongation (mm)')
                 ax1.set_ylabel('Pressure (MPa) ')        
        connection.close()
        
        for i in range(len(self.x1)):
              self.p1.append(self.x1[i])
              self.q1.append(self.y1[i])
        
        ax1.plot(self.x1,self.y1,'b')
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
       
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_TYPE from TEST_MST_TMP") 
        for x in results:
                self.graph_type=str(x[0]) 
        connection.close() 
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT FLOW_TIME_X_AXIS,FLOW_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS, VOLUMN_TIME_Y_AXIS FROM OTER_INFO") 
        for x in results:             
                         ax.set_xlabel('Time (sec)')
                         ax.set_ylabel('Expansion (mm)')
                         ax.set_xlim(0,float(x[0]))
                         ax.set_ylim(0,float(x[1]))
        
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])
        
        
        ax.plot(self.x,self.y,'b')
        
        ########
        
        '''
        self.x1=[0,0,0,0,0,0,0,0]
        self.y1=[0,0,0,0,0,0,0,0]
        
        self.p1=list()
        self.q1=list()
        
        ax1 = self.figure.add_subplot(212)
        ax1.set_facecolor('#CCFFFF')
        ax1.minorticks_on()
        ax1.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:             
                 ax1.set_xlim(0,float(x[0]))
                 ax1.set_ylim(0,float(x[1]))
                 ax1.set_xlabel('Time (sec)')
                 ax1.set_ylabel('Pressure (MPa) ')        
        connection.close()
        
        for i in range(len(self.x1)):
              self.p1.append(self.x1[i])
              self.q1.append(self.y1[i])
        
        ax1.plot(self.x1,self.y1,'b')
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
       
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_TYPE from TEST_MST_TMP") 
        for x in results:
                self.graph_type=str(x[0]) 
        connection.close() 
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT FLOW_TIME_X_AXIS,FLOW_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS, VOLUMN_TIME_Y_AXIS FROM OTER_INFO") 
        for x in results:             
                         ax.set_xlabel('Time (sec)')
                         ax.set_ylabel('Stress (MPa)')
                         ax.set_xlim(0,float(x[0]))
                         ax.set_ylim(0,float(x[1]))
        
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])
        
        
        ax.plot(self.x,self.y,'b')
        
        ########
        
        '''
        self.x1=[0,0,0,0,0,0,0,0]
        self.y1=[0,0,0,0,0,0,0,0]
        
        self.p1=list()
        self.q1=list()
        
        ax1 = self.figure.add_subplot(121)
        ax1.set_facecolor('#CCFFFF')
        ax1.minorticks_on()
        ax1.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:             
                 ax1.set_xlim(0,float(x[0]))
                 ax1.set_ylim(0,float(x[1]))
                 ax1.set_xlabel('Time (sec)')
                 ax1.set_ylabel('Strain (%) ')        
        connection.close()
        
        for i in range(len(self.x1)):
              self.p1.append(self.x1[i])
              self.q1.append(self.y1[i])
        
        ax1.plot(self.x1,self.y1,'b')
        '''
        self.draw() 



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
