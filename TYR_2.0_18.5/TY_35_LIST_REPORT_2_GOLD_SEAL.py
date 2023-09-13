
from TY_36_REPORTS_COMPRESS_02 import TY_36_REPORT_COMPR_02_Ui_MainWindow
from TY_38_REPORTS_TEAR_03 import TY_38_REPORT_TEAR_Ui_MainWindow
from TY_41_REPORTS_WEBBING import TY_41_Ui_MainWindow
from TY_42_REPORTS_SHEAR_STRENGTH import TY_42_Ui_MainWindow
from TY_44_REPORTS_PEEL_STRENGTH import TY_44_Ui_MainWindow
from TY_52_REPORT_PULL_ON_FORCE import TY_52_Ui_MainWindow
from TY_54_REPORT_PUSH_ON_FORCE import TY_54_Ui_MainWindow
from TY_56_REPORT_TRUNKLIDSEAL import TY_56_Ui_MainWindow
from TY_60_REPORT_TRUNKLIDSEAL2 import TY_60_Ui_MainWindow
from TY_58_REPORT_TEAR_PEAK_LOAD import TY_58_REPORT_TEAR_Ui_MainWindow



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton


import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem
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



class TY_35_LIST_Ui_MainWindow_GOLD_SEAL(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 769)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1301, 709))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(720, 50, 601, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 10, 161, 41))
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
        self.label_47.setGeometry(QtCore.QRect(1150, 10, 161, 41))
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
        self.pushButton_6.setGeometry(QtCore.QRect(410, 620, 131, 51))
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
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(570, 620, 131, 51))
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
        
        
        
        
        self.pushButton_8_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8_1.setGeometry(QtCore.QRect(560, 550, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8_1.setFont(font)
        self.pushButton_8_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_8_1.setStyleSheet("background-color: rgb(148, 255, 166);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_8_1.setFlat(False)
        self.pushButton_8_1.setObjectName("pushButton_8_1")
        
        
        
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(420, 500, 271, 31))
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
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(710, 0, 20, 707))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(220, 10, 350, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 60, 651, 151))
        self.frame_2.setStyleSheet("background-color: rgb(255, 240, 220);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(150, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 30, 111, 41))
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
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(330, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_11.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(460, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(10, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(150, 100, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        ### This is radio button for Job Id 
        self.label_15 = QtWidgets.QRadioButton(self.frame)
        self.label_15.setGeometry(QtCore.QRect(80, 260, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")        
        self.label_15.setObjectName("label_15")
        
        
        
        
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 260, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(380, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setGeometry(QtCore.QRect(490, 160, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 310, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(30, 360, 351, 121))
        self.frame_3.setStyleSheet("background-color: rgb(255, 238, 244);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(10, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_4.setGeometry(QtCore.QRect(120, 40, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 490, 121, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(30, 550, 341, 101))
        self.frame_5.setStyleSheet("background-color: rgb(255, 238, 244);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(10, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_6.setGeometry(QtCore.QRect(120, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox_6.setObjectName("comboBox_6")
        
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(420, 360, 261, 121))
        self.frame_6.setStyleSheet("background-color: rgb(255, 238, 244);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        self.label_20.setGeometry(QtCore.QRect(30, 40, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(350, 70, 351, 101))
        self.frame_7.setStyleSheet("background-color: rgb(255, 238, 244);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setLineWidth(2)
        self.frame_7.setObjectName("frame_7")
        self.label_21 = QtWidgets.QLabel(self.frame_7)
        self.label_21.setGeometry(QtCore.QRect(10, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame_7)
        self.comboBox_8.setGeometry(QtCore.QRect(110, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox_8.setObjectName("comboBox_8")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_6)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_17)
        self.lineEdit_17.setValidator(input_validator)
        self.lineEdit_17.setGeometry(QtCore.QRect(120, 40, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(470, 310, 211, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(700, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(1030, 10, 91, 41))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(410, 550, 121, 51))
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
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(730, 70, 561, 625))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
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
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(770, 230, 312, 183))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget_2.setGeometry(QtCore.QRect(770, 440, 312, 183))
        self.calendarWidget_2.setGridVisible(True)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.from_dt=""
        self.to_dt=""
        self.party_name=""
        self.specimen_name=""
        self.unit_type=""
                  
#         self.kg_to_lb=float(2.20462)
#         self.mm_to_inch=float(0.0393701)
#         self.kg_to_Newton=float(9.81)
#         self.kgCm2_toMPA=float(0.0980665)
        
        self.test_ids=[]
        self.length=""
        self.test_id=""
        self.test_id_type=""
        self.email_flg="N"
        self.new_test_name=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Search Report"))
        self.label_47.setText(_translate("MainWindow", "05 Aug 2020 14:23:00"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.pushButton_8.setText(_translate("MainWindow", "Search"))
        self.pushButton_8_1.setText(_translate("MainWindow", "Summery Report"))
        self.label_48.setText(_translate("MainWindow", " ")) #message ..................
        
        self.radioButton.setText(_translate("MainWindow", "By Date Range [Tensile Test] "))
        self.pushButton_9.setText(_translate("MainWindow", "From Date :"))
        self.pushButton_11.setText(_translate("MainWindow", "To Date.:"))
        self.label_14.setText(_translate("MainWindow", "Customer Name:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MRF"))
        self.comboBox.setItemText(1, _translate("MainWindow", "NISHIGANDHA Polymer"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.label_15.setText(_translate("MainWindow", "Job.Id:"))
        #self.label_15.setDisabled(True)
        self.comboBox_2.setDisabled(True)
        self.label_16.setText(_translate("MainWindow", "Job Name:"))
        self.label_16.setDisabled(True)
        #self.comboBox_3.setDisabled(True)
        
        self.radioButton_2.setText(_translate("MainWindow", "By Tested By "))
        self.label_17.setText(_translate("MainWindow", "Tested By:"))
        self.radioButton_3.setText(_translate("MainWindow", "By Batch Id."))
        
        
        self.label_19.setText(_translate("MainWindow", "Batch ID:"))
        self.label_20.setText(_translate("MainWindow", "Test ID:"))
        self.label_21.setText(_translate("MainWindow", "Customer Name:"))
        self.radioButton_4.setText(_translate("MainWindow", "By Test ID / Serial No :"))
        self.label_11.setText(_translate("MainWindow", "Double Click on record to see detail report"))
        self.checkBox.setText(_translate("MainWindow", "Select All"))
        self.checkBox.hide()
        self.pushButton_10.setText(_translate("MainWindow", " Delete "))

        
        #### Default setting ######
        self.calendarWidget.hide()
        self.calendarWidget_2.hide()
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        
        self.frame_2.setEnabled(True)
        self.frame_3.setDisabled(True)
        self.frame_5.setDisabled(True)
        self.frame_6.setDisabled(True)
        
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_16.setReadOnly(True)
        self.pushButton_11.setDisabled(True)
        
        
        
        #self.pushButton_10.setDisabled(True)
        
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.radioButton.clicked.connect(self.date_range_radiobutt_on_click)
        self.radioButton_2.clicked.connect(self.party_radiobutt_on_click)
        self.radioButton_3.clicked.connect(self.batch_radiobutt_on_click)
        self.radioButton_4.clicked.connect(self.jobname_radiobutt_on_click)
        self.label_15.clicked.connect(self.jobname_radiobutt_on_click)
       
        self.lineEdit_15.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.lineEdit_16.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        
        self.pushButton_9.clicked.connect(self.from_on_click1)
        self.pushButton_11.clicked.connect(self.to_on_click2)
        self.calendarWidget.clicked.connect(self.calendar1_on_click)
        self.calendarWidget_2.clicked.connect(self.calendar2_on_click)
        
        #self.comboBox.currentTextChanged.connect(self.load_batchids_1)
        #self.comboBox_2.currentTextChanged.connect(self.load_jobname_1)
        
        self.pushButton_8.clicked.connect(self.list_tests) #open_summery_pdf
        self.pushButton_8_1.clicked.connect(self.open_summery_pdf)
        
        
        self.tableWidget.doubleClicked.connect(self.open_doubleClick_report)
        self.pushButton_10.clicked.connect(self.delete_tests)
        
        self.new_test_name=""
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME FROM GLOBAL_VAR")         
        for x in results:
                self.new_test_name=str(x[0])
                self.radioButton.setText("By Date Range ["+str(self.new_test_name)+" Test] ")
        connection.close()
        
        
        
        
        
        self.load_party_names_1()
        self.load_party_names_2()
        
        self.load_batchids_2()
        
        self.list_tests()
        
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        
    def device_date(self):     
        self.label_47.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))  
        
     
    def date_range_radiobutt_on_click(self):
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        
        self.frame_2.setEnabled(True)
        self.frame_3.setDisabled(True)
        self.frame_5.setDisabled(True)
        self.frame_6.setDisabled(True)
    
    def party_radiobutt_on_click(self):
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(True)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        
        self.frame_2.setDisabled(True)
        self.frame_3.setEnabled(True)
        self.frame_5.setDisabled(True)
        self.frame_6.setDisabled(True)
        
    def batch_radiobutt_on_click(self):
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(True)
        self.radioButton_4.setChecked(False)
        
        self.frame_2.setDisabled(True)
        self.frame_3.setDisabled(True)
        self.frame_5.setEnabled(True)
        self.frame_6.setDisabled(True)

    def jobname_radiobutt_on_click(self):
        self.frame_2.setDisabled(True)
        self.frame_3.setDisabled(True)
        self.frame_5.setDisabled(True)
        self.frame_6.setDisabled(True)
        self.comboBox_2.setEnabled(True)
        self.load_jobname_1()
        
        
    def from_on_click1(self):
        self.calendarWidget.show()
    
    def to_on_click2(self):
        self.calendarWidget_2.show()
        
    def calendar1_on_click(self):
        temp_var = self.calendarWidget.selectedDate() 
        var_name = temp_var.toPyDate()        
        #self.from_dt=str(var_name)
        self.lineEdit_15.setText(str(self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)))
        self.calendarWidget.hide()
        self.pushButton_11.setEnabled(True)
        
    
    def calendar2_on_click(self):
        temp_var = self.calendarWidget_2.selectedDate() 
        var_name = temp_var.toPyDate()        
        #self.to_dt=str(var_name)
        self.lineEdit_16.setText(str(self.calendarWidget_2.selectedDate().toString(QtCore.Qt.ISODate)))
        self.calendarWidget_2.hide()
        self.load_party_names_1()
        
    def load_party_names_1(self):
        self.i=0
        self.comboBox.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT PARTY_NAME FROM TEST_MST WHERE TEST_TYPE='"+str(self.new_test_name)+"' order by TEST_ID DESC") 
        for x in results:            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str(x[0]))           
            self.i=self.i+1
        connection.close()
    
    def load_party_names_2(self):
        self.i=0
        self.comboBox_4.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT TESTED_BY FROM TEST_MST WHERE TEST_TYPE='"+str(self.new_test_name)+"' order by TEST_ID DESC")
        print("SELECT DISTINCT TESTED_BY FROM TEST_MST WHERE TEST_TYPE='"+str(self.new_test_name)+"' order by TEST_ID DESC") 
       
        for x in results:            
            self.comboBox_4.addItem("")
            self.comboBox_4.setItemText(self.i,str(x[0]))           
            self.i=self.i+1
        connection.close()
        
#     def load_batchids_1(self):
#         self.j=0
#         self.comboBox_2.clear()
#         connection = sqlite3.connect("tyr.db")
#         results=connection.execute("SELECT DISTINCT BATCH_ID FROM TEST_MST WHERE TEST_TYPE='"+str(self.new_test_name)+"' and PARTY_NAME='"+str(self.comboBox.currentText())+"' order by TEST_ID DESC")
#         #print("SELECT DISTINCT BATCH_ID FROM TEST_MST WHERE TEST_TYPE='Tensile' and PARTY_NAME='"+str(self.comboBox.currentText())+"'") 
#         
#         for x in results:            
#             self.comboBox_2.addItem("")
#             self.comboBox_2.setItemText(self.j,str(x[0]))           
#             self.j=self.j+1
#         connection.close()
        
    def load_batchids_2(self):
        self.j=0
        self.comboBox_6.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT BATCH_ID FROM TEST_MST WHERE TEST_TYPE='"+str(self.new_test_name)+"' order by TEST_ID DESC")
          
        for x in results:            
            self.comboBox_6.addItem("")
            self.comboBox_6.setItemText(self.j,str(x[0]))           
            self.j=self.j+1
        connection.close()
        
    def load_jobname_1(self):
        self.k=0
        self.comboBox_2.clear()
        connection = sqlite3.connect("tyr.db")
        print("SELECT DISTINCT JOB_NAME FROM TEST_MST WHERE TEST_TYPE='"+str(self.new_test_name)+"' order by TEST_ID DESC")
        results=connection.execute("SELECT DISTINCT JOB_NAME FROM TEST_MST WHERE TEST_TYPE='"+str(self.new_test_name)+"' order by TEST_ID DESC")         
        #results=connection.execute("SELECT DISTINCT JOB_NAME FROM TEST_MST order by TEST_ID DESC")        
        #print("SELECT DISTINCT JOB_NAME FROM TEST_MST order by TEST_ID DESC")
        for x in results:            
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(self.k,str(x[0]))         
            self.k=self.k+1
            print("j_id:"+str(x[0]))
        connection.close()
        
    def list_tests(self):
        
        #self.pushButton_14_1.setEnabled(True)
        self.from_dt=self.lineEdit_15.text()
        self.to_dt=self.lineEdit_16.text()
        #self.party_name=str(self.comboBox_3.currentText())
        #self.specimen_name=str(self.comboBox_4.currentText())
        #self.unit_type=str(self.comboBox_5.currentText())
        
        print("frm:"+str(self.from_dt)+"   to:"+str(self.to_dt))
        self.specimen_shape=""
        
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
       
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 200)
        self.tableWidget.setColumnWidth(6, 200)
       
        
        self.tableWidget.setHorizontalHeaderLabels(['Test ID.','CreatedOn','Customer Name','Spec.Counts','Batch ID.','Product Name','Comments'])
        
         
        connection = sqlite3.connect("tyr.db")
        if(self.radioButton.isChecked()):
                print("date Range -select")
                #results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where date(B.CREATED_ON) between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' and B.TEST_TYPE='"+str(self.new_test_name)+"' and  B.PARTY_NAME = '"+str(self.comboBox.currentText())+"' and B.BATCH_ID = '"+str(self.comboBox_2.currentText())+"' and B.JOB_NAME='"+str(self.comboBox_3.currentText())+"' order by TEST_ID DESC")                        
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where date(B.CREATED_ON) between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' and B.TEST_TYPE='"+str(self.new_test_name)+"' and  B.PARTY_NAME = '"+str(self.comboBox.currentText())+"'  order by TEST_ID DESC")                        
                
        elif(self.radioButton_2.isChecked()):
                print("Search by Tested By.....")
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.TEST_TYPE='"+str(self.new_test_name)+"' and  B.TESTED_BY = '"+str(self.comboBox_4.currentText())+"' order by TEST_ID DESC")                        
        elif(self.radioButton_3.isChecked()):
                print("by batch id -select")
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.TEST_TYPE='"+str(self.new_test_name)+"' and  B.BATCH_ID = '"+str(self.comboBox_6.currentText())+"' order by TEST_ID DESC ")                        
        elif(self.radioButton_4.isChecked()):
                if(self.lineEdit_17.text() != ""):
                    print("by Test Id / Serial No -select")
                    results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.TEST_TYPE='"+str(self.new_test_name)+"' and  B.TEST_ID='"+str(self.lineEdit_17.text())+"' order by TEST_ID DESC")                        
                else:
                    results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.TEST_TYPE='"+str(self.new_test_name)+"' order by TEST_ID DESC")                        
            
        elif(self.label_15.isChecked()):
                print("by Job id -select")
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.TEST_TYPE='"+str(self.new_test_name)+"' and  B.JOB_NAME = '"+str(self.comboBox_2.currentText())+"' order by TEST_ID DESC ")                        
        else:
                print("by else part-select")
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.PARTY_NAME,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.BATCH_ID,B.SPECIMEN_NAME,COMMENTS FROM TEST_MST B where B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' and B.TEST_TYPE='"+str(self.new_test_name)+"' and  B.PARTY_NAME = '"+str(self.comboBox.currentText())+"'")                        
      
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if(int(column_number) == 0):
                    #print("data-column_number :"+str(column_number))
                    item = QtWidgets.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(QtCore.Qt.Checked)
                    item.setText(str(data))
                    self.tableWidget.setItem(row_number,column_number,item)
                    #self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                else:
                    self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                #self.lineEdit.setText("")
        connection.close()   
        self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.label_48.setText("")                   
        self.label_48.show()
       
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1            
            self.tableWidget.removeRow(i)
    
    
    def open_doubleClick_report(self):
        row = self.tableWidget.currentRow()
        if(row != -1 ):
            self.test_id=(self.tableWidget.item(row, 0).text() )
            print(" test_id :"+str(self.test_id))        
        
            connection = sqlite3.connect("tyr.db")
            with connection:        
                  cursor = connection.cursor()                                        
                  cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID = '"+str(self.test_id)+"'")              
            connection.commit();
            connection.close()            
            
            if(str(self.new_test_name) == "Webbing"):
                            self.open_report_webbing()
            elif(str(self.new_test_name) == "COMPRESS_2"):
                            self.open_report_compress()
            elif(str(self.new_test_name) == "DOT_TEAR_TEST"):               
                            self.open_report_dot_tear_test()
            elif(str(self.new_test_name) == "Shear Strength"):               
                            self.open_report_shear_strength()
            elif(str(self.new_test_name) == "Peel Strength"):               
                            self.open_report_peel_strength()
            elif(str(self.new_test_name) == "PULL_ON_FORCE"):               
                            self.open_report_pull_on_force()
            elif(str(self.new_test_name) == "PUSH_ON_FORCE"):               
                            self.open_report_push_on_force()
            elif(str(self.new_test_name) == "VWSK_TRUNKLIDSEAL_CLD"):               
                            self.open_report_CLD()
            elif(str(self.new_test_name) == "TEAR_PEAK_LOAD"):               
                            self.open_report_tear_peak_load()
            else:
                            self.open_report_tensile()
            
        
    def open_report_tear_peak_load(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_58_REPORT_TEAR_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_CLD(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_56_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_report_pull_on_force(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_52_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_push_on_force(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_54_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_compress(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_36_REPORT_COMPR_02_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_dot_tear_test(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_38_REPORT_TEAR_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_webbing(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_41_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_shear_strength(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_42_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_peel_strength(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_44_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    
    
    def delete_tests(self):
        self.del_uncheked()
        close = QMessageBox()
        close.setText("Confirm Deleteing TEST ID.")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE from GRAPH_MST WHERE GRAPH_ID in (SELECT GRAPH_ID FROM  CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM TEST_IDS))") 
                            cursor.execute("DELETE FROM CYCLES_MST WHERE TEST_ID IN (SELECT TEST_ID FROM TEST_IDS)")  
                            cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM TEST_IDS)")                           
                            self.label_48.setText("Record(s) Deleted Successfully.")                   
                            self.label_48.show()
                           
                    connection.commit();                    
                    connection.close()
                    self.list_tests()
                    
                    
        
    
    def del_uncheked(self):
        i = self.tableWidget.rowCount()       
        while (i > 0):
            i=i-1
            item = self.tableWidget.item(i, 0)
            #print("test id  :"+str(item.text()))
            currentState = item.checkState()
            if(currentState == QtCore.Qt.Checked):
                    print("Checked test ID:"+str(item.text()))
                    connection = sqlite3.connect("tyr.db")          
                    with connection:        
                            cursor = connection.cursor()                            
                            cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,B.TEST_TYPE  FROM TEST_MST B WHERE B.TEST_ID='"+str(item.text())+"' AND B.TEST_ID NOT IN (SELECT TEST_ID FROM TEST_IDS)") 
                    connection.commit();
                    connection.close()                    
            else:
                    print("Un-Checked test ID:"+str(item.text()))
                    connection = sqlite3.connect("tyr.db")          
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM TEST_IDS WHERE TEST_ID = '"+str(item.text())+"'")                             
                    connection.commit();
                    connection.close()
       
                
    def open_summery_pdf(self):
        connection = sqlite3.connect("tyr.db")          
        with connection:        
                      cursor = connection.cursor()
                      cursor.execute("DELETE FROM TEST_IDS")                             
        connection.commit();
        connection.close()
        
        self.del_uncheked()
        if(str(self.new_test_name) == "PULL_ON_FORCE"):
                    self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)
                    self.create_pdf_Pull_ON_Force()
        else:
                    self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)
                    self.create_pdf_Pull_ON_Force()
                    
        #self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)                
        os.system("xpdf ./reports/summery_report.pdf")        
        #os.system("cp ./reports/Reportxxx.pdf /media/pi/003B-E2B4")
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                os.system("cp ./reports/summery_report.pdf /media/usb/summery_report_"+str(self.new_test_name)+".pdf")
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
    
    def create_pdf_Pull_ON_Force(self):
        self.remark=""
        self.login_user_name=""
        self.unit_typex="Kg/Cm"
        self.tested_by=""
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_UNIT_LOAD,LAST_UNIT_DISP,TEST_ID,TESTED_BY from TEST_MST  WHERE TEST_ID IN (SELECT TEST_ID FROM TEST_IDS) LIMIT 1") 
        for x in results:
              self.last_load_unit=str(x[0])
              self.last_disp_unit=str(x[1])
              self.test_id=str(x[2])
              self.tested_by=str(x[3])
        connection.close()
        
        data2= [ ['Test ID','Spec. \n No', 'Force at Peak\n ('+str(self.last_load_unit)+')']]
        
        connection = sqlite3.connect("tyr.db")
        print("SELECT TEST_ID,CYCLE_NUM,printf(\"%.2f\", A.PEAK_LOAD_KG) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM TEST_IDS)") 
       
        results=connection.execute("SELECT TEST_ID,CYCLE_NUM,printf(\"%.2f\", A.PEAK_LOAD_KG) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM TEST_IDS)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'AVG','',printf(\"%.2f\", avg(A.PEAK_LOAD_KG)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM TEST_IDS)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MAX','',printf(\"%.2f\", max(A.PEAK_LOAD_KG)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM TEST_IDS)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT 'MIN','',printf(\"%.2f\", min(A.PEAK_LOAD_KG)) FROM CYCLES_MST A WHERE A.TEST_ID IN (SELECT TEST_ID FROM TEST_IDS)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        y=300
        Elements=[]
        
        
        summary_data=[]
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
         
        #f3=Table(summary_data)
        #f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
        #self.show_all_specimens()
        report_gr_img="summary_last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4* inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),pdf_img,Spacer(1,12),Spacer(1,12),Spacer(1,12),f2,Spacer(1,12),blank,comments,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        '''
        doc = SimpleDocTemplate('./reports/Reportxxx.pdf', pagesize=A4, rightMargin=10,
                                leftMargin=40,
                                topMargin=30,
                                bottomMargin=30,)
        '''
        doc = SimpleDocTemplate('./reports/summery_report.pdf', pagesize=A4,rightMargin=20,
                                leftMargin=30,
                                topMargin=10,
                                bottomMargin=10)
        doc.build(Elements)
        #print("Done")



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
            
            elif(self.graph_type=="Load Vs Time"):
                    #print("SELECT T_SEC,Y_NUM FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
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
                ax.set_xlabel('Travel ('+str(self.last_disp_unit)+')')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        elif(self.graph_type=="Load Vs Time"):
                ax.set_xlabel('Time (sec)')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        else:
                ax.set_xlabel('Strain %')
                ax.set_ylabel('Stress')
        #self.connect('motion_notify_event', mouse_move)
        ax.legend()        
        self.draw()
        self.figure.savefig('summary_last_graph.png',dpi=100)
        
        #ax.connect('motion_notify_event', mouse_move)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_35_LIST_Ui_MainWindow_GOLD_SEAL()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

