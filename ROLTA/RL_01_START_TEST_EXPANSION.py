

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

class RL_01_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1374, 770)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 1341, 711))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
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
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(1050, 490, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 240, 1341, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(870, 490, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
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
        self.label_12.setGeometry(QtCore.QRect(120, 20, 51, 21))
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
        self.lcdNumber.setGeometry(QtCore.QRect(770, 590, 91, 41))
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("value", 100.0)
        self.lcdNumber.setProperty("intValue", 100)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(650, 540, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 260, 611, 431))
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
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(120, 50, 181, 21))
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
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(10, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
        self.lineEdit_3.setValidator(input_validator)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_49 = QtWidgets.QLabel(self.frame)
        self.label_49.setGeometry(QtCore.QRect(1150, 50, 161, 31))
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
        self.pushButton_5.setGeometry(QtCore.QRect(1190, 90, 121, 31))
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
        self.pushButton_6.setGeometry(QtCore.QRect(1190, 210, 121, 31))
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
        self.pushButton_7.setGeometry(QtCore.QRect(1190, 130, 121, 31))
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
        self.pushButton_8.setGeometry(QtCore.QRect(1190, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(217, 255, 227);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_60 = QtWidgets.QLabel(self.frame)
        self.label_60.setGeometry(QtCore.QRect(10, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
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
        self.lineEdit_9.setGeometry(QtCore.QRect(170, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_63 = QtWidgets.QLabel(self.frame)
        self.label_63.setGeometry(QtCore.QRect(230, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_63.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_63.setObjectName("label_63")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(1250, 490, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(650, 590, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_2.setGeometry(QtCore.QRect(770, 540, 91, 41))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setProperty("value", 100.0)
        self.lcdNumber_2.setProperty("intValue", 100)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.line_17 = QtWidgets.QFrame(self.frame)
        self.line_17.setGeometry(QtCore.QRect(310, 0, 20, 251))
        self.line_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_17.setLineWidth(3)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setObjectName("line_17")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_11.setGeometry(QtCore.QRect(170, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_72 = QtWidgets.QLabel(self.frame)
        self.label_72.setGeometry(QtCore.QRect(10, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_72.setFont(font)
        self.label_72.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_72.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_72.setObjectName("label_72")
        self.label_74 = QtWidgets.QLabel(self.frame)
        self.label_74.setGeometry(QtCore.QRect(220, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_74.setFont(font)
        self.label_74.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_74.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_74.setObjectName("label_74")
        self.label_76 = QtWidgets.QLabel(self.frame)
        self.label_76.setGeometry(QtCore.QRect(10, 200, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_76.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_76.setObjectName("label_76")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(200, 200, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_77 = QtWidgets.QLabel(self.frame)
        self.label_77.setGeometry(QtCore.QRect(260, 200, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_77.setFont(font)
        self.label_77.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_77.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_77.setObjectName("label_77")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(330, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(470, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_78 = QtWidgets.QLabel(self.frame)
        self.label_78.setGeometry(QtCore.QRect(330, 60, 141, 31))
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
        self.lineEdit_16.setGeometry(QtCore.QRect(470, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setGeometry(QtCore.QRect(470, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_79 = QtWidgets.QLabel(self.frame)
        self.label_79.setGeometry(QtCore.QRect(330, 100, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_79.setFont(font)
        self.label_79.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_79.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.frame)
        self.label_80.setGeometry(QtCore.QRect(330, 140, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_80.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_80.setObjectName("label_80")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_18)
        self.lineEdit_18.setValidator(input_validator)
        self.lineEdit_18.setGeometry(QtCore.QRect(470, 140, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_81 = QtWidgets.QLabel(self.frame)
        self.label_81.setGeometry(QtCore.QRect(530, 140, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)
        self.label_81.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_81.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_81.setObjectName("label_81")
        self.line_18 = QtWidgets.QFrame(self.frame)
        self.line_18.setGeometry(QtCore.QRect(600, 0, 20, 251))
        self.line_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_18.setLineWidth(3)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setObjectName("line_18")
        self.label_82 = QtWidgets.QLabel(self.frame)
        self.label_82.setGeometry(QtCore.QRect(620, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_82.setFont(font)
        self.label_82.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_82.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_82.setObjectName("label_82")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_19.setGeometry(QtCore.QRect(770, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_83 = QtWidgets.QLabel(self.frame)
        self.label_83.setGeometry(QtCore.QRect(620, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_83.setFont(font)
        self.label_83.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_83.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_83.setObjectName("label_83")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_20)
        self.lineEdit_20.setValidator(input_validator)
        self.lineEdit_20.setGeometry(QtCore.QRect(770, 50, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_84 = QtWidgets.QLabel(self.frame)
        self.label_84.setGeometry(QtCore.QRect(820, 50, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_84.setFont(font)
        self.label_84.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_84.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_84.setObjectName("label_84")
        self.label_85 = QtWidgets.QLabel(self.frame)
        self.label_85.setGeometry(QtCore.QRect(620, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_85.setFont(font)
        self.label_85.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_85.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_85.setObjectName("label_85")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_21.setGeometry(QtCore.QRect(770, 90, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_86 = QtWidgets.QLabel(self.frame)
        self.label_86.setGeometry(QtCore.QRect(620, 130, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_86.setFont(font)
        self.label_86.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_86.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_86.setObjectName("label_86")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_22)
        self.lineEdit_22.setValidator(input_validator)
        self.lineEdit_22.setGeometry(QtCore.QRect(770, 130, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_87 = QtWidgets.QLabel(self.frame)
        self.label_87.setGeometry(QtCore.QRect(620, 170, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_87.setFont(font)
        self.label_87.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_87.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_87.setObjectName("label_87")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_23)
        self.lineEdit_23.setValidator(input_validator)
        self.lineEdit_23.setGeometry(QtCore.QRect(770, 170, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_88 = QtWidgets.QLabel(self.frame)
        self.label_88.setGeometry(QtCore.QRect(820, 170, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_88.setFont(font)
        self.label_88.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_88.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_88.setObjectName("label_88")
        self.label_89 = QtWidgets.QLabel(self.frame)
        self.label_89.setGeometry(QtCore.QRect(620, 210, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_89.setFont(font)
        self.label_89.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_89.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_89.setObjectName("label_89")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_24.setGeometry(QtCore.QRect(770, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_90 = QtWidgets.QLabel(self.frame)
        self.label_90.setGeometry(QtCore.QRect(900, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_90.setFont(font)
        self.label_90.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_90.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_90.setObjectName("label_90")
        self.line_19 = QtWidgets.QFrame(self.frame)
        self.line_19.setGeometry(QtCore.QRect(880, 0, 20, 251))
        self.line_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_19.setLineWidth(3)
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setObjectName("line_19")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_25)
        self.lineEdit_25.setValidator(input_validator)
        self.lineEdit_25.setGeometry(QtCore.QRect(1010, 10, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.label_91 = QtWidgets.QLabel(self.frame)
        self.label_91.setGeometry(QtCore.QRect(1060, 10, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_91.setFont(font)
        self.label_91.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_91.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_91.setObjectName("label_91")
        self.label_92 = QtWidgets.QLabel(self.frame)
        self.label_92.setGeometry(QtCore.QRect(900, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_92.setFont(font)
        self.label_92.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_92.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_92.setObjectName("label_92")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_26)
        self.lineEdit_26.setValidator(input_validator)
        self.lineEdit_26.setGeometry(QtCore.QRect(1010, 50, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.label_93 = QtWidgets.QLabel(self.frame)
        self.label_93.setGeometry(QtCore.QRect(1060, 50, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_93.setFont(font)
        self.label_93.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_93.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_93.setObjectName("label_93")
        self.label_94 = QtWidgets.QLabel(self.frame)
        self.label_94.setGeometry(QtCore.QRect(900, 90, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_94.setFont(font)
        self.label_94.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_94.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_94.setObjectName("label_94")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_27)
        self.lineEdit_27.setValidator(input_validator)
        self.lineEdit_27.setGeometry(QtCore.QRect(1070, 90, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_27.setFont(font)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label_95 = QtWidgets.QLabel(self.frame)
        self.label_95.setGeometry(QtCore.QRect(1130, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_95.setFont(font)
        self.label_95.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_95.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_95.setObjectName("label_95")
        self.label_96 = QtWidgets.QLabel(self.frame)
        self.label_96.setGeometry(QtCore.QRect(900, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_96.setFont(font)
        self.label_96.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_96.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_96.setObjectName("label_96")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_28)
        self.lineEdit_28.setValidator(input_validator)
        self.lineEdit_28.setGeometry(QtCore.QRect(1070, 130, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_28.setFont(font)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.label_97 = QtWidgets.QLabel(self.frame)
        self.label_97.setGeometry(QtCore.QRect(1130, 130, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_97.setFont(font)
        self.label_97.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_97.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_97.setObjectName("label_97")
        self.label_98 = QtWidgets.QLabel(self.frame)
        self.label_98.setGeometry(QtCore.QRect(900, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_98.setFont(font)
        self.label_98.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_98.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_98.setObjectName("label_98")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_29)
        self.lineEdit_29.setValidator(input_validator)
        self.lineEdit_29.setGeometry(QtCore.QRect(1000, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.label_75 = QtWidgets.QLabel(self.frame)
        self.label_75.setGeometry(QtCore.QRect(1050, 170, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_75.setFont(font)
        self.label_75.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_75.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_75.setObjectName("label_75")
        self.label_99 = QtWidgets.QLabel(self.frame)
        self.label_99.setGeometry(QtCore.QRect(900, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_99.setFont(font)
        self.label_99.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_99.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_99.setObjectName("label_99")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_30)
        self.lineEdit_30.setValidator(input_validator)
        self.lineEdit_30.setGeometry(QtCore.QRect(1000, 200, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_30.setFont(font)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.label_100 = QtWidgets.QLabel(self.frame)
        self.label_100.setGeometry(QtCore.QRect(1050, 200, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_100.setFont(font)
        self.label_100.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_100.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_100.setObjectName("label_100")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(650, 260, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_101 = QtWidgets.QLabel(self.frame)
        self.label_101.setGeometry(QtCore.QRect(650, 290, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_101.setFont(font)
        self.label_101.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_101.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_101.setObjectName("label_101")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_4)
        self.lineEdit_4.setValidator(input_validator)
        self.lineEdit_4.setGeometry(QtCore.QRect(740, 290, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_102 = QtWidgets.QLabel(self.frame)
        self.label_102.setGeometry(QtCore.QRect(790, 290, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_102.setFont(font)
        self.label_102.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_102.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_102.setObjectName("label_102")
        self.label_103 = QtWidgets.QLabel(self.frame)
        self.label_103.setGeometry(QtCore.QRect(790, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_103.setFont(font)
        self.label_103.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_103.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_103.setObjectName("label_103")
        self.label_104 = QtWidgets.QLabel(self.frame)
        self.label_104.setGeometry(QtCore.QRect(650, 330, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_104.setFont(font)
        self.label_104.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_104.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_104.setObjectName("label_104")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_5)
        self.lineEdit_5.setValidator(input_validator)
        self.lineEdit_5.setGeometry(QtCore.QRect(740, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_105 = QtWidgets.QLabel(self.frame)
        self.label_105.setGeometry(QtCore.QRect(790, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_105.setFont(font)
        self.label_105.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_105.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_105.setObjectName("label_105")
        self.label_106 = QtWidgets.QLabel(self.frame)
        self.label_106.setGeometry(QtCore.QRect(650, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_106.setFont(font)
        self.label_106.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_106.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_106.setObjectName("label_106")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_6)
        self.lineEdit_6.setValidator(input_validator)
        self.lineEdit_6.setGeometry(QtCore.QRect(740, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_107 = QtWidgets.QLabel(self.frame)
        self.label_107.setGeometry(QtCore.QRect(790, 410, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_107.setFont(font)
        self.label_107.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_107.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_107.setObjectName("label_107")
        self.label_108 = QtWidgets.QLabel(self.frame)
        self.label_108.setGeometry(QtCore.QRect(650, 410, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_108.setFont(font)
        self.label_108.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_108.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_108.setObjectName("label_108")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_7)
        self.lineEdit_7.setValidator(input_validator)
        self.lineEdit_7.setGeometry(QtCore.QRect(740, 410, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_109 = QtWidgets.QLabel(self.frame)
        self.label_109.setGeometry(QtCore.QRect(790, 450, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_109.setFont(font)
        self.label_109.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_109.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_109.setObjectName("label_109")
        self.label_110 = QtWidgets.QLabel(self.frame)
        self.label_110.setGeometry(QtCore.QRect(650, 450, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_110.setFont(font)
        self.label_110.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_110.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_110.setObjectName("label_110")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_8)
        self.lineEdit_8.setValidator(input_validator)
        self.lineEdit_8.setGeometry(QtCore.QRect(740, 450, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_111 = QtWidgets.QLabel(self.frame)
        self.label_111.setGeometry(QtCore.QRect(790, 490, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_111.setFont(font)
        self.label_111.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_111.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_111.setObjectName("label_111")
        self.label_112 = QtWidgets.QLabel(self.frame)
        self.label_112.setGeometry(QtCore.QRect(650, 490, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_112.setFont(font)
        self.label_112.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_112.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_112.setObjectName("label_112")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_10)
        self.lineEdit_10.setValidator(input_validator)
        self.lineEdit_10.setGeometry(QtCore.QRect(740, 490, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_113 = QtWidgets.QLabel(self.frame)
        self.label_113.setGeometry(QtCore.QRect(870, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_113.setFont(font)
        self.label_113.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_113.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_113.setObjectName("label_113")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_31)
        self.lineEdit_31.setValidator(input_validator)
        self.lineEdit_31.setGeometry(QtCore.QRect(990, 290, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.label_114 = QtWidgets.QLabel(self.frame)
        self.label_114.setGeometry(QtCore.QRect(1050, 290, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_114.setFont(font)
        self.label_114.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_114.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_114.setObjectName("label_114")
        self.label_115 = QtWidgets.QLabel(self.frame)
        self.label_115.setGeometry(QtCore.QRect(870, 330, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_115.setFont(font)
        self.label_115.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_115.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_115.setObjectName("label_115")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_32)
        self.lineEdit_32.setValidator(input_validator)
        self.lineEdit_32.setGeometry(QtCore.QRect(990, 330, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.label_116 = QtWidgets.QLabel(self.frame)
        self.label_116.setGeometry(QtCore.QRect(1050, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_116.setFont(font)
        self.label_116.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_116.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_116.setObjectName("label_116")
        self.label_117 = QtWidgets.QLabel(self.frame)
        self.label_117.setGeometry(QtCore.QRect(870, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_117.setFont(font)
        self.label_117.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_117.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_117.setObjectName("label_117")
        self.label_118 = QtWidgets.QLabel(self.frame)
        self.label_118.setGeometry(QtCore.QRect(1050, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_118.setFont(font)
        self.label_118.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_118.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_118.setObjectName("label_118")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_33)
        self.lineEdit_33.setValidator(input_validator)
        self.lineEdit_33.setGeometry(QtCore.QRect(990, 370, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_33.setFont(font)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.label_119 = QtWidgets.QLabel(self.frame)
        self.label_119.setGeometry(QtCore.QRect(870, 410, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_119.setFont(font)
        self.label_119.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_119.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_119.setObjectName("label_119")
        self.label_120 = QtWidgets.QLabel(self.frame)
        self.label_120.setGeometry(QtCore.QRect(1050, 410, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_120.setFont(font)
        self.label_120.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_120.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_120.setObjectName("label_120")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_34)
        self.lineEdit_34.setValidator(input_validator)
        self.lineEdit_34.setGeometry(QtCore.QRect(990, 410, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_34.setFont(font)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.label_121 = QtWidgets.QLabel(self.frame)
        self.label_121.setGeometry(QtCore.QRect(870, 450, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_121.setFont(font)
        self.label_121.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_121.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_121.setObjectName("label_121")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_35)
        self.lineEdit_35.setValidator(input_validator)
        self.lineEdit_35.setGeometry(QtCore.QRect(990, 450, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_35.setFont(font)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.label_122 = QtWidgets.QLabel(self.frame)
        self.label_122.setGeometry(QtCore.QRect(1050, 450, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_122.setFont(font)
        self.label_122.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_122.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_122.setObjectName("label_122")
        self.label_123 = QtWidgets.QLabel(self.frame)
        self.label_123.setGeometry(QtCore.QRect(1110, 290, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_123.setFont(font)
        self.label_123.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_123.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_123.setObjectName("label_123")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_36.setGeometry(QtCore.QRect(1180, 290, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_36.setFont(font)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.label_124 = QtWidgets.QLabel(self.frame)
        self.label_124.setGeometry(QtCore.QRect(1120, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_124.setFont(font)
        self.label_124.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_124.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_124.setObjectName("label_124")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_37)
        self.lineEdit_37.setValidator(input_validator)
        self.lineEdit_37.setGeometry(QtCore.QRect(1180, 330, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_37.setFont(font)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.label_125 = QtWidgets.QLabel(self.frame)
        self.label_125.setGeometry(QtCore.QRect(1240, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_125.setFont(font)
        self.label_125.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_125.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_125.setObjectName("label_125")
        self.label_126 = QtWidgets.QLabel(self.frame)
        self.label_126.setGeometry(QtCore.QRect(1120, 370, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_126.setFont(font)
        self.label_126.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_126.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_126.setObjectName("label_126")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_38)
        self.lineEdit_38.setValidator(input_validator)
        self.lineEdit_38.setGeometry(QtCore.QRect(1180, 370, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_38.setFont(font)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.label_127 = QtWidgets.QLabel(self.frame)
        self.label_127.setGeometry(QtCore.QRect(1240, 370, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_127.setFont(font)
        self.label_127.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_127.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_127.setObjectName("label_127")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(1220, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(640, 520, 701, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_20 = QtWidgets.QFrame(self.frame)
        self.line_20.setGeometry(QtCore.QRect(880, 530, 20, 181))
        self.line_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_20.setLineWidth(3)
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setObjectName("line_20")
        self.label_128 = QtWidgets.QLabel(self.frame)
        self.label_128.setGeometry(QtCore.QRect(1120, 410, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_128.setFont(font)
        self.label_128.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_128.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_128.setObjectName("label_128")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_12)
        self.lineEdit_12.setValidator(input_validator)
        self.lineEdit_12.setGeometry(QtCore.QRect(1180, 410, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_129 = QtWidgets.QLabel(self.frame)
        self.label_129.setGeometry(QtCore.QRect(1120, 450, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_129.setFont(font)
        self.label_129.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_129.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_129.setObjectName("label_129")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_13)
        self.lineEdit_13.setValidator(input_validator)
        self.lineEdit_13.setGeometry(QtCore.QRect(1180, 450, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(1150, 490, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(900, 530, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_130 = QtWidgets.QLabel(self.frame)
        self.label_130.setGeometry(QtCore.QRect(900, 560, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_130.setFont(font)
        self.label_130.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_130.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_130.setObjectName("label_130")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_39.setGeometry(QtCore.QRect(950, 560, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_39.setFont(font)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.label_131 = QtWidgets.QLabel(self.frame)
        self.label_131.setGeometry(QtCore.QRect(1000, 560, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_131.setFont(font)
        self.label_131.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_131.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_131.setObjectName("label_131")
        self.label_132 = QtWidgets.QLabel(self.frame)
        self.label_132.setGeometry(QtCore.QRect(900, 600, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_132.setFont(font)
        self.label_132.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_132.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_132.setObjectName("label_132")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_40.setGeometry(QtCore.QRect(950, 600, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_40.setFont(font)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.label_133 = QtWidgets.QLabel(self.frame)
        self.label_133.setGeometry(QtCore.QRect(1000, 600, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_133.setFont(font)
        self.label_133.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_133.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_133.setObjectName("label_133")
        self.label_134 = QtWidgets.QLabel(self.frame)
        self.label_134.setGeometry(QtCore.QRect(900, 640, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_134.setFont(font)
        self.label_134.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_134.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_134.setObjectName("label_134")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_41.setGeometry(QtCore.QRect(950, 670, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_41.setFont(font)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.label_135 = QtWidgets.QLabel(self.frame)
        self.label_135.setGeometry(QtCore.QRect(1000, 670, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_135.setFont(font)
        self.label_135.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_135.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_135.setObjectName("label_135")
        self.label_136 = QtWidgets.QLabel(self.frame)
        self.label_136.setGeometry(QtCore.QRect(1060, 560, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_136.setFont(font)
        self.label_136.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_136.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_136.setObjectName("label_136")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_42.setGeometry(QtCore.QRect(1200, 560, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_42.setFont(font)
        self.lineEdit_42.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.label_137 = QtWidgets.QLabel(self.frame)
        self.label_137.setGeometry(QtCore.QRect(1280, 560, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_137.setFont(font)
        self.label_137.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_137.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_137.setObjectName("label_137")
        self.label_138 = QtWidgets.QLabel(self.frame)
        self.label_138.setGeometry(QtCore.QRect(1060, 600, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_138.setFont(font)
        self.label_138.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_138.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_138.setObjectName("label_138")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_43.setGeometry(QtCore.QRect(1200, 600, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_43.setFont(font)
        self.lineEdit_43.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit_43.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.label_139 = QtWidgets.QLabel(self.frame)
        self.label_139.setGeometry(QtCore.QRect(1280, 600, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_139.setFont(font)
        self.label_139.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_139.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_139.setObjectName("label_139")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(1100, 640, 81, 31))
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
        self.lineEdit_44.setGeometry(QtCore.QRect(1200, 640, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_44.setFont(font)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(1140, 680, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(1200, 680, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(460, 220, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 220, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(650, 650, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_3.setGeometry(QtCore.QRect(770, 650, 91, 41))
        self.lcdNumber_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_3.setSmallDecimalPoint(False)
        self.lcdNumber_3.setProperty("value", 100.0)
        self.lcdNumber_3.setProperty("intValue", 100)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        
        
        '''
        self.label_140 = QtWidgets.QLabel(self.frame)
        self.label_140.setGeometry(QtCore.QRect(770, 550, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_140.setFont(font)
        self.label_140.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_140.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_140.setObjectName("label_140")
        '''
        
        self.label_141 = QtWidgets.QLabel(self.frame)
        self.label_141.setGeometry(QtCore.QRect(330, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_141.setFont(font)
        self.label_141.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_141.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_141.setObjectName("label_141")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_45)
        self.lineEdit_45.setValidator(input_validator)
        self.lineEdit_45.setGeometry(QtCore.QRect(470, 180, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_45.setFont(font)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.label_142 = QtWidgets.QLabel(self.frame)
        self.label_142.setGeometry(QtCore.QRect(530, 180, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_142.setFont(font)
        self.label_142.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_142.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_142.setObjectName("label_142")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(960, 260, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1374, 21))
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
        #self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00"))
        self.label_20.setText(_translate("MainWindow", datetime.datetime.now().strftime("%B  %d , %Y %I:%M ")+""))
        
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.label_21.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", "Spec.Name :"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "001"))
        self.label_13.setText(_translate("MainWindow", "Pressure (MPa) :"))
        self.label_22.setText(_translate("MainWindow", ""))
        self.comboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(4, _translate("MainWindow", "New Item"))
        self.comboBox.setDisabled(True)
        self.label_48.setText(_translate("MainWindow", "Gread:"))
        self.lineEdit_3.setText(_translate("MainWindow", "5.40"))
        self.label_49.setText(_translate("MainWindow", "Expansion Test"))
        self.pushButton_5.setText(_translate("MainWindow", "Email"))
        self.pushButton_6.setText(_translate("MainWindow", "Remark"))
        self.pushButton_7.setText(_translate("MainWindow", "Report View"))
        self.pushButton_8.setText(_translate("MainWindow", "Report Print"))
        self.label_60.setText(_translate("MainWindow", "Nominal Outer Dia :"))
        self.lineEdit_9.setText(_translate("MainWindow", "219.00"))
        self.label_63.setText(_translate("MainWindow", "(mm)"))
        self.pushButton_15.setText(_translate("MainWindow", "Return"))
        self.label_14.setText(_translate("MainWindow", "Elongation (mm):"))
        self.lineEdit_11.setText(_translate("MainWindow", "X42 PSL 2"))
        self.label_72.setText(_translate("MainWindow", "Nominal Wall Thickness : "))
        self.label_74.setText(_translate("MainWindow", "(mm)"))
        self.label_76.setText(_translate("MainWindow", "Specified Yeild Strength (SMYS) :"))
        self.lineEdit_14.setText(_translate("MainWindow", "290-495"))
        self.label_77.setText(_translate("MainWindow", "(MPa)"))
        self.label_8.setText(_translate("MainWindow", "Tested By :"))
        self.lineEdit_15.setText(_translate("MainWindow", "DB"))
        self.label_78.setText(_translate("MainWindow", "Sample Identification # :"))
        self.lineEdit_16.setText(_translate("MainWindow", "31489517"))
        self.lineEdit_17.setText(_translate("MainWindow", "EGP Pipeline Project"))
        self.label_79.setText(_translate("MainWindow", "Sample Decscription:"))
        self.label_80.setText(_translate("MainWindow", "Mill Hydrotest Pressure:"))
        self.lineEdit_18.setText(_translate("MainWindow", "0.00"))
        self.label_81.setText(_translate("MainWindow", "(MPa)"))
        self.label_82.setText(_translate("MainWindow", "Pressure Transducer # :"))
        self.lineEdit_19.setText(_translate("MainWindow", "4136608-008"))
        self.label_83.setText(_translate("MainWindow", "\"Force Span\" On PDSC :"))
        self.lineEdit_20.setText(_translate("MainWindow", "50.50"))
        self.label_84.setText(_translate("MainWindow", "(%)"))
        self.label_85.setText(_translate("MainWindow", "Last Calibration Date :"))
        self.lineEdit_21.setText(_translate("MainWindow", "18/02/2015"))
        self.label_86.setText(_translate("MainWindow", "Extensometer No :"))
        self.lineEdit_22.setText(_translate("MainWindow", "1"))
        self.label_87.setText(_translate("MainWindow", "\"Position Span\" On PDSC :"))
        self.lineEdit_23.setText(_translate("MainWindow", "111.48"))
        self.label_88.setText(_translate("MainWindow", "(%)"))
        self.label_89.setText(_translate("MainWindow", "Last Calibration Date :"))
        self.lineEdit_24.setText(_translate("MainWindow", "18/02/2015"))
        self.label_90.setText(_translate("MainWindow", "Max Elongation %:"))
        self.lineEdit_25.setText(_translate("MainWindow", "0.50"))
        self.label_91.setText(_translate("MainWindow", "(%)"))
        self.label_92.setText(_translate("MainWindow", "Preload  %:"))
        self.lineEdit_26.setText(_translate("MainWindow", "111.48"))
        self.label_93.setText(_translate("MainWindow", "(%)"))
        self.label_94.setText(_translate("MainWindow", "NEVER EXCEED Test Pressure :"))
        self.lineEdit_27.setText(_translate("MainWindow", "21.44"))
        self.label_95.setText(_translate("MainWindow", "(MPa)"))
        self.label_96.setText(_translate("MainWindow", "Extensometer Chain Length :"))
        self.lineEdit_28.setText(_translate("MainWindow", "28.5"))
        self.label_97.setText(_translate("MainWindow", "Links"))
        self.label_98.setText(_translate("MainWindow", "Max extension:"))
        self.lineEdit_29.setText(_translate("MainWindow", "3.44"))
        self.label_75.setText(_translate("MainWindow", "(mm)"))
        self.label_99.setText(_translate("MainWindow", "Extension Rate:"))
        self.lineEdit_30.setText(_translate("MainWindow", "3.44"))
        self.label_100.setText(_translate("MainWindow", "(mm/min)"))
        self.label_15.setText(_translate("MainWindow", "Sample Measurements  (After Preload, If Required)"))
        self.label_101.setText(_translate("MainWindow", "Thickness 1 :"))
        self.lineEdit_4.setText(_translate("MainWindow", "5.39"))
        self.label_102.setText(_translate("MainWindow", "(mm)"))
        self.label_103.setText(_translate("MainWindow", "(mm)"))
        self.label_104.setText(_translate("MainWindow", "Thickness 2 :"))
        self.lineEdit_5.setText(_translate("MainWindow", "5.43"))
        self.label_105.setText(_translate("MainWindow", "(mm)"))
        self.label_106.setText(_translate("MainWindow", "Thickness 3 :"))
        self.lineEdit_6.setText(_translate("MainWindow", "5.40"))
        self.label_107.setText(_translate("MainWindow", "(mm)"))
        self.label_108.setText(_translate("MainWindow", "Thickness 4 :"))
        self.lineEdit_7.setText(_translate("MainWindow", "5.48"))
        self.label_109.setText(_translate("MainWindow", "(mm)"))
        self.label_110.setText(_translate("MainWindow", "Thickness 5 :"))
        self.lineEdit_8.setText(_translate("MainWindow", "5.48"))
        self.label_111.setText(_translate("MainWindow", "(mm)"))
        self.label_112.setText(_translate("MainWindow", "Thickness 6 :"))
        self.lineEdit_10.setText(_translate("MainWindow", "5.44"))
        self.label_113.setText(_translate("MainWindow", "PreLoad Pressure :"))
        self.lineEdit_31.setText(_translate("MainWindow", "13.60"))
        self.label_114.setText(_translate("MainWindow", "(MPa)"))
        self.label_115.setText(_translate("MainWindow", "Diameter 1 :"))
        self.lineEdit_32.setText(_translate("MainWindow", "219.49"))
        self.label_116.setText(_translate("MainWindow", "(mm)"))
        self.label_117.setText(_translate("MainWindow", "Diameter 2 :"))
        self.label_118.setText(_translate("MainWindow", "(mm)"))
        self.lineEdit_33.setText(_translate("MainWindow", "219.46"))
        self.label_119.setText(_translate("MainWindow", "Diameter 3 :"))
        self.label_120.setText(_translate("MainWindow", "(mm)"))
        self.lineEdit_34.setText(_translate("MainWindow", "219.45"))
        self.label_121.setText(_translate("MainWindow", "Sample Width :"))
        self.lineEdit_35.setText(_translate("MainWindow", "75.82"))
        self.label_122.setText(_translate("MainWindow", "(mm)"))
        self.label_123.setText(_translate("MainWindow", "Tested ?:"))
        self.lineEdit_36.setText(_translate("MainWindow", "YES"))
        self.label_124.setText(_translate("MainWindow", "D.Avg:"))
        self.lineEdit_37.setText(_translate("MainWindow", "219.47"))
        self.label_125.setText(_translate("MainWindow", "(mm)"))
        self.label_126.setText(_translate("MainWindow", "T.Avg:"))
        self.lineEdit_38.setText(_translate("MainWindow", "5.44"))
        self.label_127.setText(_translate("MainWindow", "(mm)"))
        self.label_16.setText(_translate("MainWindow", "OK to Test !"))
        self.label_128.setText(_translate("MainWindow", "Y-Axis :"))
        self.lineEdit_12.setText(_translate("MainWindow", "1000"))
        self.label_129.setText(_translate("MainWindow", "X-Axis :"))
        self.lineEdit_13.setText(_translate("MainWindow", "100"))
        self.pushButton_16.setText(_translate("MainWindow", "Set Graph"))
        self.label_17.setText(_translate("MainWindow", "Selected Elastic Zone Data Points :"))
        self.label_130.setText(_translate("MainWindow", "Min Ext:"))
        self.lineEdit_39.setText(_translate("MainWindow", "0.35"))
        self.label_131.setText(_translate("MainWindow", "(mm)"))
        self.label_132.setText(_translate("MainWindow", "Max Ext:"))
        self.lineEdit_40.setText(_translate("MainWindow", "0.75"))
        self.label_133.setText(_translate("MainWindow", "(mm)"))
        self.label_134.setText(_translate("MainWindow", "Max. Pressure:"))
        self.lineEdit_41.setText(_translate("MainWindow", "36.00"))
        self.label_135.setText(_translate("MainWindow", "(MPa)"))
        self.label_136.setText(_translate("MainWindow", "0.5 % TE Yeild Strength:"))
        self.lineEdit_42.setText(_translate("MainWindow", "355"))
        self.label_137.setText(_translate("MainWindow", "(MPa)"))
        self.label_138.setText(_translate("MainWindow", "Modulus of Elasticity :"))
        self.lineEdit_43.setText(_translate("MainWindow", "209.1"))
        self.label_139.setText(_translate("MainWindow", "(GPa)"))
        self.label_9.setText(_translate("MainWindow", "Reviewd  By :"))
        self.lineEdit_44.setText(_translate("MainWindow", "lan Duncan"))
        self.label_10.setText(_translate("MainWindow", "Date :"))
        #self.label_18.setText(_translate("MainWindow", "05 Aug 2020"))
        self.label_18.setText(_translate("MainWindow", datetime.datetime.now().strftime("%B  %d ,%Y")+""))
        self.radioButton.setText(_translate("MainWindow", "Pressure Vs Extension"))
        self.radioButton_2.setText(_translate("MainWindow", "Stress Vs Strain"))
        self.label_23.setText(_translate("MainWindow", "Pressure(MPa):"))
        self.label_23.hide()
        #self.label_140.setText(_translate("MainWindow", "Preload  %:"))
        self.label_141.setText(_translate("MainWindow", "Preload Pressure:"))
        self.lineEdit_45.setText(_translate("MainWindow", "13.58"))
        self.label_142.setText(_translate("MainWindow", "(MPa)"))
        self.label_24.setText(_translate("MainWindow", "Report File Name : expansion_test_001.pdf"))
        self.label_24.hide()
        self.lcdNumber_3.hide()
        self.pushButton_15.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(self.start_test_expansion)
        self.pushButton_16.clicked.connect(self.set_data)
        
        
        self.pushButton_5.clicked.connect(self.open_email_report)    
        self.pushButton_7.clicked.connect(self.open_pdf)
        self.pushButton_6.clicked.connect(self.open_comment_popup)
        self.pushButton_8.clicked.connect(self.print_file)
        self.radioButton.clicked.connect(self.graph_type_change)
        self.radioButton_2.clicked.connect(self.graph_type_change)
        
        self.lineEdit_32.textChanged.connect(self.avg_dia_calc)
        self.lineEdit_33.textChanged.connect(self.avg_dia_calc)
        self.lineEdit_34.textChanged.connect(self.avg_dia_calc)
        
        self.lineEdit_4.textChanged.connect(self.avg_thickness_calc)
        self.lineEdit_5.textChanged.connect(self.avg_thickness_calc)
        self.lineEdit_6.textChanged.connect(self.avg_thickness_calc)
        self.lineEdit_7.textChanged.connect(self.avg_thickness_calc)
        self.lineEdit_8.textChanged.connect(self.avg_thickness_calc)
        self.lineEdit_10.textChanged.connect(self.avg_thickness_calc)
        
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        
                
#        self.sc_blank =PlotCanvas_blank(self)          
#        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_3.setProperty("value", 0.0)
        
        self.load_data()
        self.graph_type_change()
        
    
    def avg_dia_calc(self):
        self.d1=""
        self.d2=""
        self.d3=""
        self.av_d=""
        if(self.lineEdit_32.text() != ""):
            try:
                        self.d1=int(self.lineEdit_32.text())
            except ValueError as e:
                        try:
                                self.d1=float(self.lineEdit_32.text())
                        except ValueError as e:
                                self.lineEdit_37.setText("0.00")
            try:
                        self.d2=int(self.lineEdit_33.text())
            except ValueError as e:
                        try:
                                self.d2=float(self.lineEdit_33.text())
                        except ValueError as e:
                                self.lineEdit_37.setText("0.00")
            try:
                        self.d3=int(self.lineEdit_34.text())
            except ValueError as e:
                        try:
                                self.d3=float(self.lineEdit_34.text())
                        except ValueError as e:
                                self.lineEdit_37.setText("0.00")
            try:
                        self.av_d=float(self.d1 + self.d2 + self.d3)/3
                        self.lineEdit_37.setText(str(round(self.av_d,2)))
            except ValueError as e:                    
                    print("Caluculation error1");
                    self.lineEdit_37.setText(str("0"))
            except TypeError as e:
                    print("Caluculation error2");
                    self.lineEdit_37.setText(str("0"))
            except:
                    print("Caluculation error3");
                    self.lineEdit_37.setText(str("0"))
        
        else:
              self.lineEdit_37.setText("0.00")
    
    def avg_thickness_calc(self):
        self.T1=""
        self.T2=""
        self.T3=""
        self.T4=""
        self.T5=""
        self.T6=""
        self.av_T=""
        if(self.lineEdit_4.text() != ""):
            try:
                       #try:
                        self.T1=int(self.lineEdit_4.text())
            except ValueError as e:
                        try:
                                self.T1=float(self.lineEdit_4.text())
                        except ValueError as e:
                                self.lineEdit_38.setText("0.00")
            try:
                        self.T2=int(self.lineEdit_5.text())
            except ValueError as e:
                        try:
                                self.T2=float(self.lineEdit_5.text())
                        except ValueError as e:
                                self.lineEdit_38.setText("0.00")
            try:
                        self.T3=int(self.lineEdit_6.text())
            except ValueError as e:
                        try:
                                self.T3=float(self.lineEdit_6.text())
                        except ValueError as e:
                                self.lineEdit_38.setText("0.00")
                                
            try:
                       #try:
                        self.T4=int(self.lineEdit_7.text())
            except ValueError as e:
                        try:
                                self.T4=float(self.lineEdit_7.text())
                        except ValueError as e:
                                self.lineEdit_38.setText("0.00")
            try:
                        self.T5=int(self.lineEdit_8.text())
            except ValueError as e:
                        try:
                                self.T5=float(self.lineEdit_8.text())
                        except ValueError as e:
                                self.lineEdit_38.setText("0.00")
            try:
                        self.T6=int(self.lineEdit_10.text())
            except ValueError as e:
                        try:
                                self.T6=float(self.lineEdit_10.text())
                        except ValueError as e:
                                self.lineEdit_38.setText("0.00")
                                
                                
            try:
                        self.av_T=float(self.T1 + self.T2 + self.T3+self.T4 + self.T5 + self.T6)/6
                        self.lineEdit_38.setText(str(round(self.av_T,2)))
            except ValueError as e:
                    #self.lineEdit_3.setText("0.00")
                    print("Caluculation error1");
                    self.lineEdit_38.setText(str("0"))
            except TypeError as e:
                    print("Caluculation error2");
                    self.lineEdit_38.setText(str("0"))
            except:
                    print("Caluculation error3");
                    self.lineEdit_38.setText(str("0"))
        
        else:
              self.lineEdit_38.setText("0.00")
       
        
    def graph_type_change(self):
        #self.graph_type="STRESS_VS_STRAIN"
        if(self.radioButton_2.isChecked()):
             self.graph_type="STRESS_VS_STRAIN"
             self.label_13.setText("Stress(Mpa)")
             self.label_14.setText("Strain(%)")
             connection = sqlite3.connect("tyr.db")        
             with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='"+str(self.graph_type)+"'")                 
             connection.commit()
             connection.close()
             
        elif(self.radioButton.isChecked()):
             self.graph_type="LOAD_VS_LENGTH"
             self.label_13.setText("Pressure(Mpa)")
             self.label_14.setText("Elongation(mm)")
             connection = sqlite3.connect("tyr.db")        
             with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("update TEST_MST_TMP set GRAPH_TYPE='"+str(self.graph_type)+"'")                 
             connection.commit()
             connection.close()
        else:     
             self.graph_type="STRESS_VS_STRAIN"
             self.label_13.setText("Stress(Mpa)")
             self.label_14.setText("Strain(%):")
             
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
                                   "LAST_CAL_DATE_1,EXTENSOMETER_NO,POSITION_SPAN_ON_PDSC,LAST_CAL_DATE_2,MAX_ELONGATION_PRC,PRELOAD_PERC,PRELOAD_PRESSURE__MPA,"
                                   "NEVER_EXCEED_TEST_PRESSURE , EXTENSOMETER_CHAIN_LENGTH ,MAX_EXTENSION,EXTENSION_RATE,THICKNESS_1,THICKNESS_2,THICKNESS_3,"
                                   "THICKNESS_4,THICKNESS_5,THICKNESS_6,PRELOAD_PRESSURE_MPA,DIAMETER_1,DIAMETER_2,DIAMETER_3,SAMPLE_WIDTH_MM,IS_TESTED,"
                                   "D_AV,T_AV,SAMPLE_STATUS,MIN_EXT,MAX_EXT,MAX_PRESSURE_MPA,YEILD_STRENGTH,MODULUS_OF_ELASTICITY,REVIEWED_BY,TEST_DATE,TESTED_BY FROM TEST_MST_TMP")                 
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
                    self.lineEdit_25.setText(str(x[15])) #MAX_ELONGATION_PRC
                    self.lineEdit_26.setText(str(x[16])) #PRELOAD_PERC
                    self.lineEdit_45.setText(str(x[17])) #PRELOAD_PRESSURE__MPA
                    self.lineEdit_27.setText(str(x[18])) #NEVER_EXCEED_TEST_PRESSURE
                    self.lineEdit_28.setText(str(x[19])) #EXTENSOMETER_CHAIN_LENGTH
                    self.lineEdit_29.setText(str(x[20])) #MAX_EXTENSION
                    self.lineEdit_30.setText(str(x[21])) #EXTENSION_RATE
                    self.lineEdit_4.setText(str(x[22])) #THICKNESS_1
                    self.lineEdit_5.setText(str(x[23])) #THICKNESS_2
                    self.lineEdit_6.setText(str(x[24])) #THICKNESS_3
                    self.lineEdit_7.setText(str(x[25])) #THICKNESS_4
                    self.lineEdit_8.setText(str(x[26])) #THICKNESS_5
                    self.lineEdit_10.setText(str(x[27])) #THICKNESS_6
                    self.lineEdit_31.setText(str(x[28])) #PRELOAD_PRESSURE_MPA
                    self.lineEdit_32.setText(str(x[29])) #DIAMETER_1
                    self.lineEdit_33.setText(str(x[30])) #DIAMETER_2
                    self.lineEdit_34.setText(str(x[31])) #DIAMETER_3
                    self.lineEdit_35.setText(str(x[32])) #SAMPLE_WIDTH_MM
                    
                    self.lineEdit_36.setText(str(x[33])) #IS_TESTED
                    self.lineEdit_37.setText(str(x[34])) #D_AV
                    self.lineEdit_38.setText(str(x[35])) #T_AV
                    self.label_16.setText(str(x[36])) #SAMPLE_STATUS
                    self.lineEdit_39.setText(str(x[37])) #MIN_EXT
                    self.lineEdit_40.setText(str(x[38])) #MAX_EXT
                    self.lineEdit_41.setText(str(x[39])) #MAX_PRESSURE_MPA
                    self.lineEdit_42.setText("0") #YEILD_STRENGTH
                    self.lineEdit_43.setText("0") #MODULUS_OF_ELASTICITY
                    self.lineEdit_44.setText(str(x[42])) #REVIEWED_BY
                    #self.label_18.setText(str(x[43])) #TEST_DATE
                    self.lineEdit_15.setText(str(x[44]))#TESTED_BY
                    
            
            
            
            
        connection.close()
    
    
    def set_data(self):
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                       cursor = connection.cursor()                
                       cursor.execute("UPDATE SETTING_MST SET GRAPH_SCALE_CELL_1 = '"+str(self.lineEdit_12.text())+"', GRAPH_SCALE_CELL_2= '"+str(self.lineEdit_13.text())+"' ")                                        
        connection.commit();
        connection.close()
        
        
        
        self.label_21.setText("Graph Set Done !")
        self.sc_blank =PlotCanvas_blank(self)          
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        
    
    
    
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
                    self.label_21.show()
                    self.label_21.setText("Nominal Outer Dia. Should not Empty.")                    
        elif(self.lineEdit_11.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("Gread Should not Empty.")               
        elif(self.lineEdit_3.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("Nominal Wall Thickness Should not Empty. ")
        elif(self.lineEdit_14.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("SMYS Should not Empty .")
        elif(self.lineEdit_35.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("Sample Width Empty .")
        #elif(self.lineEdit_35.text() != ""): #    
        elif(float(self.lineEdit_35.text()) ==0):
                            self.label_21.show()
                            self.label_21.setText("Sample Width Zero .")           
        elif(self.lineEdit_37.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("A.Diameter Empty .")
        #elif(self.lineEdit_37.text() != ""): #    
        elif(float(self.lineEdit_37.text()) ==0):
                            self.label_21.show()
                            self.label_21.setText("A.Diameter Zero .") 
        
        elif(self.lineEdit_38.text() == ""): #    
                    self.label_21.show()
                    self.label_21.setText("A.Thickness Empty .")        
        #elif(self.lineEdit_38.text() != ""): #    
        elif(float(self.lineEdit_38.text()) ==0):
                            self.label_21.show()
                            self.label_21.setText("A.Thickness Zero .")             
                    
        else:
               self.goAhead="Yes"
               connection = sqlite3.connect("tyr.db")
               results=connection.execute("select count(*) from TEST_MST_EXPANSION WHERE TEST_ID = '"+str(int(self.label_12.text()))+"'")       
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
                                                    "', MAX_ELONGATION_PRC='"+str(self.lineEdit_25.text())+
                                                    "', PRELOAD_PERC='"+str(self.lineEdit_26.text())+
                                                    "', PRELOAD_PRESSURE__MPA='"+str(self.lineEdit_45.text())+
                                                    "', NEVER_EXCEED_TEST_PRESSURE='"+str(self.lineEdit_27.text())+
                                                    "', EXTENSOMETER_CHAIN_LENGTH='"+str(self.lineEdit_28.text())+
                                                    "', MAX_EXTENSION='"+str(self.lineEdit_29.text())+
                                                    "', EXTENSION_RATE='"+str(self.lineEdit_30.text())+
                                                    "', THICKNESS_1='"+str(self.lineEdit_4.text())+
                                                    "', THICKNESS_2='"+str(self.lineEdit_5.text())+
                                                    "', THICKNESS_3='"+str(self.lineEdit_6.text())+
                                                    "', THICKNESS_4='"+str(self.lineEdit_7.text())+
                                                    "', THICKNESS_5='"+str(self.lineEdit_8.text())+
                                                    "', THICKNESS_6='"+str(self.lineEdit_10.text())+
                                                    "', PRELOAD_PRESSURE_MPA='"+str(self.lineEdit_31.text())+
                                                    "', DIAMETER_1='"+str(self.lineEdit_32.text())+
                                                    "', DIAMETER_2='"+str(self.lineEdit_33.text())+
                                                    "', DIAMETER_3='"+str(self.lineEdit_34.text())+
                                                    "', SAMPLE_WIDTH_MM='"+str(self.lineEdit_35.text())+
                                                    "', IS_TESTED='"+str(self.lineEdit_36.text())+
                                                    "', D_AV='"+str(self.lineEdit_37.text())+
                                                    "', T_AV='"+str(self.lineEdit_38.text())+
                                                    "', SAMPLE_STATUS='"+str(self.label_16.text())+
                                                    "', MIN_EXT='"+str(self.lineEdit_39.text())+
                                                    "', MAX_EXT='"+str(self.lineEdit_40.text())+
                                                    "', MAX_PRESSURE_MPA='"+str(self.lineEdit_41.text())+
                                                    "', YEILD_STRENGTH='0'"
                                                    "', MODULUS_OF_ELASTICITY='0'"
                                                    "', REVIEWED_BY='"+str(self.lineEdit_44.text())+
                                                   # "', TEST_DATE='"+str(self.label_18.text())+
                                                    "', GRAPH_TYPE='"+str(self.graph_type)+
                                                    "' ")

                            except Exception as e:
                                              print("UPDATE SQL Error-TEST_MST_TMP No- 1:"+str(e))
                                              connection.commit();
                            cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_AREA=( SELECT  (SAMPLE_WIDTH_MM * T_AV)*0.1*0.1 FROM TEST_MST_TMP)")
                                              
                            try:
                                    cursor.execute("UPDATE  TEST_MST_EXPANSION SET TEST_ID='"+str(self.label_12.text())+
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
                                                    "', MAX_ELONGATION_PRC='"+str(self.lineEdit_25.text())+
                                                    "', PRELOAD_PERC='"+str(self.lineEdit_26.text())+
                                                    "', PRELOAD_PRESSURE__MPA='"+str(self.lineEdit_45.text())+
                                                    "', NEVER_EXCEED_TEST_PRESSURE='"+str(self.lineEdit_27.text())+
                                                    "', EXTENSOMETER_CHAIN_LENGTH='"+str(self.lineEdit_28.text())+
                                                    "', MAX_EXTENSION='"+str(self.lineEdit_29.text())+
                                                    "', EXTENSION_RATE='"+str(self.lineEdit_30.text())+
                                                    "', THICKNESS_1='"+str(self.lineEdit_4.text())+
                                                    "', THICKNESS_2='"+str(self.lineEdit_5.text())+
                                                    "', THICKNESS_3='"+str(self.lineEdit_6.text())+
                                                    "', THICKNESS_4='"+str(self.lineEdit_7.text())+
                                                    "', THICKNESS_5='"+str(self.lineEdit_8.text())+
                                                    "', THICKNESS_6='"+str(self.lineEdit_10.text())+
                                                    "', PRELOAD_PRESSURE_MPA='"+str(self.lineEdit_31.text())+
                                                    "', DIAMETER_1='"+str(self.lineEdit_32.text())+
                                                    "', DIAMETER_2='"+str(self.lineEdit_33.text())+
                                                    "', DIAMETER_3='"+str(self.lineEdit_34.text())+
                                                    "', SAMPLE_WIDTH_MM='"+str(self.lineEdit_35.text())+
                                                    "', IS_TESTED='"+str(self.lineEdit_36.text())+
                                                    "', D_AV='"+str(self.lineEdit_37.text())+
                                                    "', T_AV='"+str(self.lineEdit_38.text())+
                                                    "', SAMPLE_STATUS='"+str(self.label_16.text())+
                                                    "', MIN_EXT='"+str(self.lineEdit_39.text())+
                                                    "', MAX_EXT='"+str(self.lineEdit_40.text())+
                                                    "', MAX_PRESSURE_MPA='"+str(self.lineEdit_41.text())+
                                                    "', YEILD_STRENGTH='0"
                                                    "', MODULUS_OF_ELASTICITY='0"
                                                    "', REVIEWED_BY='"+str(self.lineEdit_44.text())+
                                                    #"', TEST_DATE='"+str(self.label_18.text())+
                                                    "', GRAPH_TYPE='"+str(self.graph_type)+
                                                    "' ")

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
                              cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"'")
                              try:
                                      
                                      print("INSERT INTO TEST_MST_EXPANSION (TEST_ID,NOMINAL_OUTER_DIA_MM,GREAD, NOMINAL_WALL_THICKNESS_MM,SPECIFIED_YEILD_STRENGTH,"
                                                    "SAMPLE_IDENTIFICATION_NO,SAMPLE_DESCRIPTION,MILL_HYDROTEST_PRESSURE, "
                                                    "PRESSURE_TRANDUSER_NO,FORCE_SAPN_ON_PDSC, LAST_CAL_DATE_1,"
                                                    "EXTENSOMETER_NO,POSITION_SPAN_ON_PDSC,LAST_CAL_DATE_2,MAX_ELONGATION_PRC,"
                                                    "PRELOAD_PERC,PRELOAD_PRESSURE__MPA,NEVER_EXCEED_TEST_PRESSURE,EXTENSOMETER_CHAIN_LENGTH,MAX_EXTENSION,"
                                                    "EXTENSION_RATE,THICKNESS_1,THICKNESS_2,THICKNESS_3,THICKNESS_4,THICKNESS_5,"
                                                    "THICKNESS_6,PRELOAD_PRESSURE_MPA,DIAMETER_1,DIAMETER_2,DIAMETER_3,SAMPLE_WIDTH_MM,"
                                                    "IS_TESTED,D_AV,T_AV,SAMPLE_STATUS,MIN_EXT, MAX_EXT,MAX_PRESSURE_MPA, YEILD_STRENGTH,MODULUS_OF_ELASTICITY, REVIEWED_BY,"
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
                                                                "'"+str(self.lineEdit_25.text())+"'," #MAX_ELONGATION_PRC
                                                                "'"+str(self.lineEdit_26.text())+"'," #PRELOAD_PERC
                                                                "'"+str(self.lineEdit_45.text())+"'," #PRELOAD_PRESSURE__MPA
                                                                "'"+str(self.lineEdit_27.text())+"'," #NEVER_EXCEED_TEST_PRESSURE
                                                                "'"+str(self.lineEdit_28.text())+"'," #EXTENSOMETER_CHAIN_LENGTH
                                                                "'"+str(self.lineEdit_29.text())+"'," #MAX_EXTENSION
                                                                "'"+str(self.lineEdit_30.text())+"'," #EXTENSION_RATE
                                                                "'"+str(self.lineEdit_4.text())+"'," #THICKNESS_1
                                                                "'"+str(self.lineEdit_5.text())+"'," #THICKNESS_2
                                                                "'"+str(self.lineEdit_6.text())+"'," #THICKNESS_3
                                                                "'"+str(self.lineEdit_7.text())+"'," #THICKNESS_4
                                                                "'"+str(self.lineEdit_8.text())+"'," #THICKNESS_5
                                                                "'"+str(self.lineEdit_10.text())+"'," #THICKNESS_6
                                                                "'"+str(self.lineEdit_31.text())+"'," #PRELOAD_PRESSURE_MPA
                                                                "'"+str(self.lineEdit_32.text())+"'," #DIAMETER_1
                                                                "'"+str(self.lineEdit_33.text())+"'," #DIAMETER_2
                                                                "'"+str(self.lineEdit_34.text())+"'," #DIAMETER_3
                                                                "'"+str(self.lineEdit_35.text())+"'," #SAMPLE_WIDTH_MM
                                                                "'"+str(self.lineEdit_36.text())+"'," #IS_TESTED
                                                                "'"+str(self.lineEdit_37.text())+"'," #D_AV
                                                                "'"+str(self.lineEdit_38.text())+"'," #T_AV
                                                                "'"+str(self.label_16.text())+"'," #SAMPLE_STATUS
                                                                "'"+str(self.lineEdit_39.text())+"'," #MIN_EXT
                                                                "'"+str(self.lineEdit_40.text())+"'," #MAX_EXT
                                                                "'"+str(self.lineEdit_41.text())+"'," #MAX_PRESSURE_MPA
                                                                "'0',"   
                                                                "'0',"
                                                                "'"+str(self.lineEdit_44.text())+"'," #REVIEWED_BY
                                                                #"'"+str(self.label_18.text())+"'," #TEST_DATE
                                                                "'"+str(self.lineEdit_15.text())+"'" #TESTED_BY
                                                                "'"+str(self.graph_type)+"')" #GRAPH_TYPE
                                                                )
                                      
                                      cursor.execute("INSERT INTO TEST_MST_EXPANSION (TEST_ID,NOMINAL_OUTER_DIA_MM,GREAD, NOMINAL_WALL_THICKNESS_MM,SPECIFIED_YEILD_STRENGTH,"
                                                    "SAMPLE_IDENTIFICATION_NO,SAMPLE_DESCRIPTION,MILL_HYDROTEST_PRESSURE, "
                                                    "PRESSURE_TRANDUSER_NO,FORCE_SAPN_ON_PDSC, LAST_CAL_DATE_1,"
                                                    "EXTENSOMETER_NO,POSITION_SPAN_ON_PDSC,LAST_CAL_DATE_2,MAX_ELONGATION_PRC,"
                                                    "PRELOAD_PERC,PRELOAD_PRESSURE__MPA,NEVER_EXCEED_TEST_PRESSURE,EXTENSOMETER_CHAIN_LENGTH,MAX_EXTENSION,"
                                                    "EXTENSION_RATE,THICKNESS_1,THICKNESS_2,THICKNESS_3,THICKNESS_4,THICKNESS_5,"
                                                    "THICKNESS_6,PRELOAD_PRESSURE_MPA,DIAMETER_1,DIAMETER_2,DIAMETER_3,SAMPLE_WIDTH_MM,"
                                                    "IS_TESTED,D_AV,T_AV,SAMPLE_STATUS,MIN_EXT, MAX_EXT,MAX_PRESSURE_MPA, YEILD_STRENGTH,MODULUS_OF_ELASTICITY, REVIEWED_BY,"
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
                                                                "'"+str(self.lineEdit_25.text())+"'," #MAX_ELONGATION_PRC
                                                                "'"+str(self.lineEdit_26.text())+"'," #PRELOAD_PERC
                                                                "'"+str(self.lineEdit_45.text())+"'," #PRELOAD_PRESSURE__MPA
                                                                "'"+str(self.lineEdit_27.text())+"'," #NEVER_EXCEED_TEST_PRESSURE
                                                                "'"+str(self.lineEdit_28.text())+"'," #EXTENSOMETER_CHAIN_LENGTH
                                                                "'"+str(self.lineEdit_29.text())+"'," #MAX_EXTENSION
                                                                "'"+str(self.lineEdit_30.text())+"'," #EXTENSION_RATE
                                                                "'"+str(self.lineEdit_4.text())+"'," #THICKNESS_1
                                                                "'"+str(self.lineEdit_5.text())+"'," #THICKNESS_2
                                                                "'"+str(self.lineEdit_6.text())+"'," #THICKNESS_3
                                                                "'"+str(self.lineEdit_7.text())+"'," #THICKNESS_4
                                                                "'"+str(self.lineEdit_8.text())+"'," #THICKNESS_5
                                                                "'"+str(self.lineEdit_10.text())+"'," #THICKNESS_6
                                                                "'"+str(self.lineEdit_31.text())+"'," #PRELOAD_PRESSURE_MPA
                                                                "'"+str(self.lineEdit_32.text())+"'," #DIAMETER_1
                                                                "'"+str(self.lineEdit_33.text())+"'," #DIAMETER_2
                                                                "'"+str(self.lineEdit_34.text())+"'," #DIAMETER_3
                                                                "'"+str(self.lineEdit_35.text())+"'," #SAMPLE_WIDTH_MM
                                                                "'"+str(self.lineEdit_36.text())+"'," #IS_TESTED
                                                                "'"+str(self.lineEdit_37.text())+"'," #D_AV
                                                                "'"+str(self.lineEdit_38.text())+"'," #T_AV
                                                                "'"+str(self.label_16.text())+"'," #SAMPLE_STATUS
                                                                "'"+str(self.lineEdit_39.text())+"'," #MIN_EXT
                                                                "'"+str(self.lineEdit_40.text())+"'," #MAX_EXT
                                                                "'"+str(self.lineEdit_41.text())+"'," #MAX_PRESSURE_MPA
                                                                "'0',"  
                                                                "'0'," 
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
                                                    "', MAX_ELONGATION_PRC='"+str(self.lineEdit_25.text())+
                                                    "', PRELOAD_PERC='"+str(self.lineEdit_26.text())+
                                                    "', PRELOAD_PRESSURE__MPA='"+str(self.lineEdit_45.text())+
                                                    "', NEVER_EXCEED_TEST_PRESSURE='"+str(self.lineEdit_27.text())+
                                                    "', EXTENSOMETER_CHAIN_LENGTH='"+str(self.lineEdit_28.text())+
                                                    "', MAX_EXTENSION='"+str(self.lineEdit_29.text())+
                                                    "', EXTENSION_RATE='"+str(self.lineEdit_30.text())+
                                                    "', THICKNESS_1='"+str(self.lineEdit_4.text())+
                                                    "', THICKNESS_2='"+str(self.lineEdit_5.text())+
                                                    "', THICKNESS_3='"+str(self.lineEdit_6.text())+
                                                    "', THICKNESS_4='"+str(self.lineEdit_7.text())+
                                                    "', THICKNESS_5='"+str(self.lineEdit_8.text())+
                                                    "', THICKNESS_6='"+str(self.lineEdit_10.text())+
                                                    "', PRELOAD_PRESSURE_MPA='"+str(self.lineEdit_31.text())+
                                                    "', DIAMETER_1='"+str(self.lineEdit_32.text())+
                                                    "', DIAMETER_2='"+str(self.lineEdit_33.text())+
                                                    "', DIAMETER_3='"+str(self.lineEdit_34.text())+
                                                    "', SAMPLE_WIDTH_MM='"+str(self.lineEdit_35.text())+
                                                    "', IS_TESTED='"+str(self.lineEdit_36.text())+
                                                    "', D_AV='"+str(self.lineEdit_37.text())+
                                                    "', T_AV='"+str(self.lineEdit_38.text())+
                                                    "', SAMPLE_STATUS='"+str(self.label_16.text())+
                                                    "', MIN_EXT='"+str(self.lineEdit_39.text())+
                                                    "', MAX_EXT='"+str(self.lineEdit_40.text())+
                                                    "', MAX_PRESSURE_MPA='"+str(self.lineEdit_41.text())+
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
                        
                        
    
    def show_load_cell_val(self):
        
        if(self.graph_type == "STRESS_VS_STRAIN"):                
                        self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q_mpa)))        
                        self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p_strain)))   #length
        else:    
                        self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q_mpa)))        
                        self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p)))   #length           
        self.label_22.setText("Running.....")
        if(str(self.sc_new.save_data_flg) =="Yes"):            
                self.reset()
                self.save_graph_data()
                self.sc_new.save_data_flg=""
                self.label_21.show()
                self.label_21.setText("Data Saved Successfully.")
                #self.go_to_next=self.go_to_next+1
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
                
                if(self.graph_type == "STRESS_VS_STRAIN"):
                        self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q_mpa)))        
                        self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p_strain)))   #length                        
                    
                else:    
                        self.lcdNumber_2.setProperty("value", str(max(self.sc_new.arr_q_mpa)))        
                        self.lcdNumber.setProperty("value",str(max(self.sc_new.arr_p)))   #length
                        
                self.label_22.setText("")
                
    def save_graph_data(self):         
         if (len(self.sc_new.arr_p) > 1):            
            
            #self.cycle_num=int(str(self.label_67.text()))+1
            
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)):                     
                        cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM_N,Y_NUM_LB,Y_NUM_MPA,X_STRAIN) VALUES ('"+str(float(self.sc_new.arr_p[g]))+"','"+str(float(self.sc_new.arr_q[g]))+"','"+str(self.sc_new.arr_p_cm[g])+"','"+str(self.sc_new.arr_p_inch[g])+"','"+str(self.sc_new.arr_q_n[g])+"','"+str(self.sc_new.arr_q_lb[g])+"','"+str(self.sc_new.arr_q_mpa[g])+"','"+str(self.sc_new.arr_p_strain[g])+"')")
            connection.commit();
            connection.close()
            
            #self.update_status()
            #self.cycle_num=self.cycle_num+1
            connection = sqlite3.connect("tyr.db")              
            with connection:        
                  cursor = connection.cursor()
                  #print("ok1")
                  try:
                          cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"'")                          
                          cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM) FROM STG_GRAPH_MST)") 
                          cursor.execute("UPDATE TEST_MST_TMP SET YEILD_STRENGTH=(SELECT MAX(Y_NUM_MPA) FROM STG_GRAPH_MST)") 
                          cursor.execute("UPDATE GLOBAL_VAR SET LENGTH_AT_MAX_MPA=(SELECT MAX(X_STRAIN) FROM STG_GRAPH_MST WHERE Y_NUM_MPA=(SELECT YEILD_STRENGTH FROM TEST_MST_TMP))")
                          cursor.execute("UPDATE TEST_MST_TMP SET MODULUS_OF_ELASTICITY=((YEILD_STRENGTH) / ( SELECT LENGTH_AT_MAX_MPA FROM GLOBAL_VAR))") 
                           

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
    
    def reset(self):        
        if(self.timer3.isActive()): 
           self.timer3.stop()
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
    
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
        
    
     
    def create_pdf_expansion(self):
        self.remark=""
        #self.unit_typex=self.comboBox_2.currentText()
        self.unit_typex = "N/mm"
        
             
        y=300
        Elements=[]
        summary_data=[]
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TEST_DATE,TESTED_BY,SAMPLE_IDENTIFICATION_NO,SAMPLE_DESCRIPTION,MILL_HYDROTEST_PRESSURE,REMARK FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(self.label_12.text())+"'")
        for x in results:
            summary_data=[["Parameter","Value","Prarameter","Value"],["Date: ",str(x[0]),"Tested By: ",str(x[1])],["Test Report File Name : ",str("Report_of_test_"+self.label_12.text()),"Sample Identification #: ",str(x[2])],["Sample Description:  ",str(x[3]),"Mill Hydrotest Pressure(MPa):",str(x[4])]]
            self.remark=str(x[5])        
        connection.close() 
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT NOMINAL_OUTER_DIA_MM, GREAD,NOMINAL_WALL_THICKNESS_MM,SPECIFIED_YEILD_STRENGTH   FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(self.label_12.text())+"'")
        for x in results:
            summary_data2=[["Nominal Outer Dia.(mm): ",str(x[0]),"Grade: ",str(x[1])],["Nominal Wall Thickness(mm) : ",str(x[2]),"Specified Yield Strength(MPa)",str(x[3])]]
            #self.remark=str(x[5])        
        connection.close() 
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT PRESSURE_TRANDUSER_NO,PRELOAD_PERC,FORCE_SAPN_ON_PDSC,PRELOAD_PRESSURE__MPA,LAST_CAL_DATE_1,NEVER_EXCEED_TEST_PRESSURE,EXTENSOMETER_NO,EXTENSOMETER_CHAIN_LENGTH,POSITION_SPAN_ON_PDSC,MAX_EXTENSION,LAST_CAL_DATE_2,MAX_ELONGATION_PRC,EXTENSION_RATE   FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(self.label_12.text())+"'")
        for x in results:
            summary_data.append(["Pressure Transducer No: ",str(x[0]),"Preload Percentage: ",str(x[1])])
            summary_data.append(["Force Span on PDSC : ",str(x[2]),"x","x"])
            summary_data.append(["Pre-load Pressure(Mpa): ",str(x[3]),"Last Calibration Date: ",str(x[4])])
            summary_data.append(["NEVER EXCEED Test Pressure (MPa) : ",str(x[5]),"Extensometer :",str(x[6])])
            summary_data.append(["Extensometer Chain length(Links): ",str(x[7]),"Position Span On PDSC: ",str(x[8])])
            summary_data.append(["Max Extension : ",str(x[9]),"Callibration Date :",str(x[10])])
            summary_data.append(["Extension Rate (mm/min): ",str(x[12]),"Max Elongation Percentage: ",str(x[11])])
        connection.close() 
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT THICKNESS_1,THICKNESS_2,THICKNESS_3,THICKNESS_4,THICKNESS_5,THICKNESS_6,PRELOAD_PRESSURE_MPA,DIAMETER_1,DIAMETER_2,DIAMETER_3,SAMPLE_WIDTH_MM,IS_TESTED,D_AV,T_AV  FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(self.label_12.text())+"'")
        for x in results:
            summary_data.append(["Thinckness_1 (mm): ",str(x[0]),"Preload Pressure (MPa): ",str(x[6])])
            summary_data.append(["Thinckness_2 (mm) : ",str(x[1]),"",""])
            summary_data.append(["Thinckness_3 (mm): ",str(x[2]),"Diameter_1(mm): ",str(x[7])])
            summary_data.append(["Thinckness_4 (mm) : ",str(x[3]),"Sample Width (mm) ",str(x[10])])
            summary_data.append(["Thinckness_5 (mm) ",str(x[4]),"Diameter_2(mm): ",str(x[8])])
            summary_data.append(["Thinckness_6 (mm): ",str(x[9]),"Tested ? :",str(x[11])])
            summary_data.append(["Thinckness_4 (mm): ",str(x[12]),"Diameter_3(mm): ",str(x[9])])
            summary_data.append(["D_AV (mm) : ",str(x[12]),"T_AV (mm): ",str(x[13])])
        connection.close() 
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT MIN_EXT,printf(\"%.2f\", YEILD_STRENGTH),MAX_EXT,printf(\"%.2f\", MODULUS_OF_ELASTICITY),MAX_PRESSURE_MPA,REVIEWED_BY,TEST_DATE  FROM TEST_MST_EXPANSION WHERE TEST_ID ='"+str(self.label_12.text())+"'")
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
        results=connection.execute("SELECT PROOF_TEST_BY FROM GLOBAL_VAR") 
        for x in results:
            self.proof_test_by=str(x[0])
            if(self.graph_type=="STRESS_VS_STRAIN"):
                     ax.set_xlabel('Strain (%)')
                     ax.set_ylabel('Stress (MPa)')               
            else:
                     ax.set_xlabel('Elongation (mm)')
                     ax.set_ylabel('Pressure (MPa)') 
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_IDENTIFICATION_NO,TEST_DATE,GRAPH_TYPE,(SAMPLE_WIDTH_MM * T_AV)*0.1*0.1 as CS_AREA_CM  FROM TEST_MST_TMP") 
        for x in results:
                        ax.set_title('Sample ID :'+str(x[0])+" Date:"+str(x[1])+"") 
                        self.graph_type= str(x[2])   
                        self.cs_area=float(x[3])                        
        connection.close()
        
        
        
        
        self.unit_type="Kgf/mm"
        ### Univarsal change for  Graphs #####################
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
            if(self.unit_type == "N/mm"):
                 ax.set_xlim(0,int(x[0]))
                 ax.set_ylim(0,int(x[1]))
                 
            if(self.unit_type == "Kgf/mm"):
                 ax.set_xlim(0,int(x[0]))
                 ax.set_ylim(0,int(x[1]))
                 
            else:     
                 ax.set_xlim(0,int(x[0]))
                 ax.set_ylim(0,int(x[1]))
                 
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_ID FROM TEST_MST_EXPANSION WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
             self.graph_ids.append(x[0])             
        connection.close()
        
        
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
            print(" Unit Type :"+str(self.unit_type))
            
            if(self.graph_type=="STRESS_VS_STRAIN"):
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT X_NUM,Y_NUM_MPA FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                        ax.set_xlabel('Strain (%)')
                        ax.set_ylabel('Stress (MPa)')
                        for k in results:        
                                self.x_num.append(float(k[0])/float(self.cs_area))
                                self.y_num.append(float(k[1]))
                        connection.close()                        
            elif(self.graph_type=="LOAD_VS_LENGTH"):
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT X_NUM,Y_NUM_MPA FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                        ax.set_xlabel('Elongation (mm)')
                        ax.set_ylabel('Pressure (MPa)') 
                        for k in results:        
                                self.x_num.append(k[0])
                                self.y_num.append(k[1])
                        connection.close()   
            else:
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT X_NUM,Y_NUM_MPA FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                        ax.set_xlabel('Elongation (mm)')
                        ax.set_ylabel('Pressure (MPa)') 
                        for k in results:        
                                self.x_num.append(k[0])
                                self.y_num.append(k[1])
                        connection.close() 
               
            
            if(g < 8 ):
                    ax.plot(self.x_num,self.y_num, self.color[g],label="Sample No:"+str(g+1))
            
        print("self.test_type:"+str(self.test_type))
        
        ax.legend()        
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
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                cursor = connection.cursor()                            
                cursor.execute("DELETE FROM STG_GRAPH_MST ")                            
        connection.commit();
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SAMPLE_IDENTIFICATION_NO,TEST_DATE ,(SAMPLE_WIDTH_MM * T_AV)*0.1*0.1 as CS_AREA_CM,GRAPH_TYPE FROM TEST_MST_TMP") 
        for x in results:
                        self.axes.set_title('Sample ID :'+str(x[0])+" Date :"+str(x[1])+"")
                        self.cs_area=float(x[2])
                        self.graph_type=str(x[3])
        connection.close()
        if(self.graph_type=="STRESS_VS_STRAIN"):
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
             if(self.unit_type == "Kgf/mm"):
                     self.axes.set_xlim(0,int(x[0]))
                     self.axes.set_ylim(0,int(x[1]))
                     #self.flexural_max_load=int(x[1])/9.81
                     self.xlim=int(x[0])
                     self.ylim=int(x[1])
            
             elif(self.unit_type == "N/mm"):
                     self.axes.set_xlim(0,int(x[0]))
                     self.axes.set_ylim(0,int(x[1]))
                     #self.flexural_max_load=int(x[1])/9.81
                     self.xlim=int(x[0])
                     self.ylim=int(x[1])
                              
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
                    
                
                self.p=float(self.p)
                self.p_cm=float(self.p)/10
                self.arr_p_cm.append(float(self.p_cm))
                
                self.p_inch=float(self.p)*0.0393701
                self.arr_p_inch.append(float(self.p_inch))
                
                self.arr_p_strain.append(float(self.p)/float(self.cs_area))
                
                
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
        if(self.graph_type == "STRESS_VS_STRAIN"):
            self.line_cnt.set_data(self.arr_p_strain,self.arr_q_mpa)
            return [self.line_cnt]
            #return self.line_cnt,       
        else:    
           self.line_cnt.set_data(self.arr_p,self.arr_q_mpa)
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
    def __init__(self, parent=None, width=8, height=5, dpi=100):
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
        self.test_type="Tensile"
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
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:             
                 ax.set_xlim(0,int(x[0]))
                 ax.set_ylim(0,int(x[1]))                               
                 
                 if(self.graph_type == "STRESS_VS_STRAIN"):
                         ax.set_xlabel('Strain (%)')
                         ax.set_ylabel('Stress (MPa) ')  
                 elif(self.graph_type == "LOAD_VS_LENGTH"):
                         ax.set_xlabel('Elongation (mm)')
                         ax.set_ylabel('Pressure (MPa) ') 
                 else:
                         ax.set_xlabel('Elongation (mm)')
                         ax.set_ylabel('Pressure (MPa) ')             
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
    ui = RL_01_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
