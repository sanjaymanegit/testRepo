# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TY_03_REPORTS.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from TY_06_REPORT_PART_2 import TY_06_Ui_MainWindow
from print_popup import P_POPUi_MainWindow
from PyQt5.Qt import QTableWidgetItem
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
import serial,time
from PyQt5.QtCore import QDate
import datetime

#from reportlab.lib import colors
#from reportlab.lib.pagesizes import letter, inch , A4
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

class TY_03_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1321, 681))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.from_date=""
        self.to_date=""
        self.graph_type=""
        self.unti_type=""
        self.kg_to_lb=0
        self.mm_to_inch=0
        self.kg_to_Newton=0
        self.kgCm2_toMPA=0
        self.test_id=0
        self.shape=""
        self.firstbatchid=""
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 640, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 640, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        
        self.pushButton_7_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7_1.setGeometry(QtCore.QRect(560, 640, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7_1.setFont(font)
        self.pushButton_7_1.setObjectName("pushButton_7_1")
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 70, 711, 261))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(100, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(290, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setChecked(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(410, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(100, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(240, 210, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(340, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 70, 531, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        #self.comboBox_2.addItem("")
        #self.comboBox_2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_2, 0, 3, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        #self.comboBox_5.addItem("")
        #self.comboBox_5.addItem("")
        #self.comboBox_5.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_5, 1, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        #self.comboBox_4.addItem("")
        #self.comboBox_4.addItem("")
        #self.comboBox_4.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_4, 1, 3, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        #self.comboBox_3.addItem("")
        #self.comboBox_3.addItem("")
        #self.comboBox_3.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("")
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 2, 2, 1, 2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(0, 85, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 2, 4, 1, 1)
        
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(410, 640, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        
        self.pushButton_8_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8_1.setGeometry(QtCore.QRect(560, 640, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8_1.setFont(font)
        self.pushButton_8_1.setObjectName("pushButton_8_1")
        
        
        
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(30, 340, 711, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 6, item)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(770, 10, 311, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget_2.setGeometry(QtCore.QRect(440, 420, 296, 183))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.calendarWidget_2.setFont(font)
        self.calendarWidget_2.setGridVisible(True)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(70, 430, 296, 183))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(770, 60, 521, 201))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 3, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 3, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 4, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 4, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 3, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 4, 4, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 4, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 5, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 1, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 1, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 1, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 3, 1, 1, 2)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(1070, 20, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(760, 290, 531, 381))
        self.layoutWidget1.setObjectName("layoutWidget1")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
       
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget1)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 3)
        
        
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)
       
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")        
        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)
        
        self.pushButton_5_1 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5_1.setFont(font)
        self.pushButton_5_1.setObjectName("pushButton_5_1")        
        self.gridLayout_2.addWidget(self.pushButton_5_1, 1, 2, 1, 1)
        
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(40, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(510, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)       
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reports"))
        self.pushButton_3.setText(_translate("MainWindow", "Search"))
        self.pushButton_7.setText(_translate("MainWindow", "View"))
        self.pushButton_7_1.setText("Delete Test")
        self.groupBox_2.setTitle(_translate("MainWindow", "Search Parameters"))
        self.radioButton_3.setText(_translate("MainWindow", "Date Range (All data)"))
        self.radioButton_4.setText(_translate("MainWindow", "By Party "))
        self.radioButton_5.setText(_translate("MainWindow", "By Batch ID"))
        self.label_5.setText(_translate("MainWindow", "From Date:"))
        self.pushButton.setText(_translate("MainWindow", "Date"))
        self.label_6.setText(_translate("MainWindow", "To Date:"))
        self.pushButton_2.setText(_translate("MainWindow", "Date"))
        self.label.setText(_translate("MainWindow", "Report Type:"))
        self.label_27.setText(_translate("MainWindow", "Batch Id:"))
        #self.comboBox.setItemText(0, _translate("MainWindow", "Load Vs Elongation"))
        #self.comboBox.setItemText(1, _translate("MainWindow", "Stress Vs Strain"))
        #self.comboBox_2.setItemText(0, _translate("MainWindow", "Kg/Cm"))
        #self.comboBox_2.setItemText(1, _translate("MainWindow", "Lb/Inch"))
        self.label_2.setText(_translate("MainWindow", "Unit Type:"))
        #self.comboBox_5.setItemText(0, _translate("MainWindow", "112"))
        #self.comboBox_5.setItemText(1, _translate("MainWindow", "113"))
        #self.comboBox_5.setItemText(2, _translate("MainWindow", "114"))
        #self.comboBox_4.setItemText(0, _translate("MainWindow", "B_1123"))
        #self.comboBox_4.setItemText(1, _translate("MainWindow", "B_2234"))
        #self.comboBox_4.setItemText(2, _translate("MainWindow", "B_1234"))
        self.label_4.setText(_translate("MainWindow", "Test ID:"))
        self.label_3.setText(_translate("MainWindow", "Party :"))
        #self.comboBox_3.setItemText(0, _translate("MainWindow", "MRF India Pvt Ltd"))
        #self.comboBox_3.setItemText(1, _translate("MainWindow", "Hero Cycles"))
        #self.comboBox_3.setItemText(2, _translate("MainWindow", "Tata Motors"))
        self.label_28.setText(_translate("MainWindow", "Modulus (%):"))
        self.lineEdit_4.setText(_translate("MainWindow", "100"))
        self.pushButton_8.setText(_translate("MainWindow", "Return"))
        self.pushButton_8_1.setText(_translate("MainWindow", "Reset"))
        self.pushButton_8_1.hide()
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Batch Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Test Id"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Party"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Spec. Shape"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Specs. Count"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Guage Length (Mm)"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Created Dt"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)        
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "B_1001"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "122"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "MRF"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Rectangle"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "60"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "Please Select record !!!!"))
        self.groupBox.setTitle(_translate("MainWindow", "Report Details"))
        self.label_23.setText(_translate("MainWindow", "Batch ID:"))
        self.label_24.setText(_translate("MainWindow", "B_1110"))
        self.label_19.setText(_translate("MainWindow", "Guage Length(Mm):"))
        self.label_20.setText(_translate("MainWindow", "60"))
        self.label_9.setText(_translate("MainWindow", "Tested Date:"))
        self.label_13.setText(_translate("MainWindow", "Spec. Name :"))
        self.label_25.setText(_translate("MainWindow", "Job Name:"))
        self.label_15.setText(_translate("MainWindow", "Specimen Shape :"))
        self.label_21.setText(_translate("MainWindow", "Test Speed (RPM):"))
        self.label_30.setText(_translate("MainWindow", "Test Type:"))
        self.label_31.setText(_translate("MainWindow", "Tensile"))
        self.label_11.setText(_translate("MainWindow", "Test Id:"))
        self.label_12.setText(_translate("MainWindow", "112"))
        self.label_17.setText(_translate("MainWindow", "Party:"))
        self.label_18.setText(_translate("MainWindow", "MRF India"))
        self.label_10.setText(_translate("MainWindow", "2019-09-12 12:17:33 "))
        self.label_14.setText(_translate("MainWindow", "XXXXXXXXX"))
        self.label_16.setText(_translate("MainWindow", "Rectangle"))
        self.label_22.setText(_translate("MainWindow", "200"))
        self.label_26.setText(_translate("MainWindow", "Job_1110"))
        self.label_8.setText(_translate("MainWindow", datetime.datetime.now().strftime("%B  %d , %Y %I:%M ")+""))
        self.pushButton_4.setText(_translate("MainWindow", "Part II"))
        self.pushButton_5.setText(_translate("MainWindow", "Print Report"))
        self.pushButton_5_1.setText(_translate("MainWindow", "View Print"))
        self.radioButton.setText(_translate("MainWindow", "Report - 1"))
        self.radioButton_2.setText(_translate("MainWindow", "Report - 2"))
        self.label_29.setText(_translate("MainWindow", "Reports"))
        self.calendarWidget_2.hide()
        self.calendarWidget.hide()
        self.label_7.hide()
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.set_default_resport_setting()
        self.radioButton_2.clicked.connect(self.report_2_setting)
        self.radioButton_3.clicked.connect(self.report_2_setting)
        self.radioButton.clicked.connect(self.set_default_resport_setting)         
        self.pushButton_3.clicked.connect(self.list_test)
        self.pushButton_5.clicked.connect(self.print_file)
        self.pushButton_5_1.clicked.connect(self.open_pdf)
        
        self.groupBox.hide()
        self.graphicsView.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.pushButton_5_1.hide()
        self.pushButton_7.clicked.connect(self.open_report)
        self.pushButton_7_1.clicked.connect(self.delete_test)        
        self.pushButton_4.clicked.connect(self.open_report_part_2)
        
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.load_data()
        self.comboBox_5.currentTextChanged.connect(self.batch_id_onchagne)
        self.comboBox_2.currentTextChanged.connect(self.open_report)
        self.comboBox.currentTextChanged.connect(self.open_report)
        self.pushButton.clicked.connect(self.from_dt_onclick)
        self.pushButton_2.clicked.connect(self.to_dt_onclick)
        self.calendarWidget.clicked.connect(self.date_dd_click_from)
        self.calendarWidget_2.clicked.connect(self.date_dd_click_to)
        self.radioButton_4.clicked.connect(self.by_party_radio)
        self.radioButton_5.clicked.connect(self.by_batch_radio)
        self.default_dates()
    '''  
    def grpbox_hide(self):
        self.groupBox.hide()        
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.pushButton_5_1.hide()
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 3)
        self.graphicsView.hide()
        self.sc=None
    '''
    def by_party_radio(self):
        self.comboBox_3.setEnabled(True)
        self.comboBox_4.setDisabled(True)    
        self.comboBox_5.setDisabled(True)
        
    def by_batch_radio(self):
        self.comboBox_4.setEnabled(True)    
        self.comboBox_5.setEnabled(True)
        self.comboBox_3.setDisabled(True)
        
    def default_dates(self):
        temp_var =QDate.currentDate()
        var_name = temp_var.toPyDate()
        self.from_date=str(var_name)
        self.to_date=str(var_name) 
        self.lineEdit.setText(str(QDate.currentDate().toString()))
        self.lineEdit_2.setText(str(QDate.currentDate().toString()))
        
    def from_dt_onclick(self):
        self.calendarWidget.show()
        
    def to_dt_onclick(self):
        self.calendarWidget_2.show()
        
    def date_dd_click_from(self):        
        temp_var = self.calendarWidget.selectedDate() 
        var_name = temp_var.toPyDate()        
        self.from_date=str(var_name)        
        self.lineEdit.setText(str(self.calendarWidget.selectedDate().toString()))
        self.calendarWidget.hide()
        
    def date_dd_click_to(self):        
        temp_var = self.calendarWidget_2.selectedDate() 
        var_name = temp_var.toPyDate()        
        self.to_date=str(var_name)
        self.lineEdit_2.show()
        self.lineEdit_2.setText(str(self.calendarWidget_2.selectedDate().toString()))
        self.calendarWidget_2.hide()   
        
     
    def load_data(self):
        self.i=0
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT BATCH_ID FROM TEST_MST WHERE STATUS != 'PENDING GRAPH' ORDER BY TEST_ID DESC ") 
        for x in results:
            if(self.i==0):
                self.firstbatchid=str(x[0])
                
            self.comboBox_5.addItem("")
            self.comboBox_5.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        print("firstbatchid :"+self.firstbatchid)
        
        self.i=0
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  TEST_ID FROM TEST_MST WHERE BATCH_ID = '"+str(self.firstbatchid)+"' AND STATUS != 'PENDING GRAPH' ORDER BY BATCH_ID DESC ") 
        for x in results:            
            self.comboBox_4.addItem("")
            self.comboBox_4.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
    
       
        self.i=0
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT PARTY_NAME FROM TEST_MST WHERE STATUS != 'PENDING GRAPH' ORDER BY TEST_ID DESC") 
        for x in results:            
            self.comboBox_3.addItem("")
            self.comboBox_3.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "Kg/Cm")
        self.comboBox_2.setItemText(1, "Lb/Inch")
        self.comboBox_2.setItemText(2, "Newton/Mm")
        self.comboBox_2.setItemText(3, "MPA")
        
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "Load Vs Elongation")
        self.comboBox.setItemText(1, "Stress Vs Strain")
        self.delete_all_records()
        #self.lineEdit.setText('250')
        self.clean_report_tables()    
    
    def batch_id_onchagne(self):
        self.i=0
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TEST_ID FROM TEST_MST WHERE STATUS != 'PENDING GRAPH' AND BATCH_ID='"+self.comboBox_5.currentText()+"' ORDER BY TEST_ID DESC") 
        for x in results:            
            self.comboBox_4.addItem("")
            self.comboBox_4.setItemText(self.i,str(x[0]))            
            self.i=self.i+1
        connection.close()
        
    def clean_report_tables(self):
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                cursor = connection.cursor()
                cursor.execute("DELETE FROM  REPORT_MST")
                cursor.execute("DELETE FROM  REPORT_MST_II")
                cursor.execute("DELETE FROM  REPORT_MST_III")
                cursor.execute("DELETE FROM  REPORT_II_AGGR")
                cursor.execute("DELETE FROM  REPORT_III_AGGR")
        connection.commit();
        connection.close() 
    
    def load_report_data(self):            
            #print("Unit Type :"+str(self.comboBox_2.currentText()))
            self.unit_type=self.comboBox_2.currentText()
            #print("Graph Type :"+str(self.comboBox.currentText()))
            self.graph_type=self.comboBox.currentText() 
            
            connection = sqlite3.connect("tyr.db")        
            with connection:        
                 cursor = connection.cursor()                
                 cursor.execute("UPDATE GLOBAL_REPORTS_PARAM SET STG_GRAPH_TYPE='"+str(self.graph_type)+"' , STG_UNIT_TYPE='"+str(self.unit_type)+"' ")            
            connection.commit();
            connection.close()  
            self.update_load_at_any(str(self.test_id),self.lineEdit_4.text())
            connection = sqlite3.connect("tyr.db")        
            with connection:        
                    cursor = connection.cursor()                
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_REPORT_TEST_ID='"+str(self.test_id)+"'")                                    
                    cursor.execute("INSERT INTO REPORT_MST (TEST_ID,REPORT_TYPE,REPORT_UNIT,MOD_AT_ANY) VALUES('"+str(self.test_id)+"','"+self.comboBox.currentText()+"','"+self.comboBox_2.currentText()+"','"+self.lineEdit_4.text()+"')")
                    cursor.execute("UPDATE REPORT_MST SET GUAGE_MM = (SELECT GUAGE_LENGTH FROM TEST_MST WHERE TEST_ID  = '"+str(self.test_id)+"')")
                    cursor.execute("UPDATE REPORT_MST SET TEST_NAME = (SELECT TEST_TYPE FROM TEST_MST WHERE TEST_ID  = '"+str(self.test_id)+"')")
                   
                    if (self.unit_type == "Kg/Cm"):                       
                            cursor.execute("INSERT INTO REPORT_MST_II(REPORT_ID,CYCLE_ID,THICKNESS,WIDTH,CS_AREA,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,DIAMETER,INN_DIAMETER,OUT_DIAMTER,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH, TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN) SELECT B.REPORT_ID,A.CYCLE_ID,A.THINCKNESS*0.1,A.WIDTH*0.1,A.CS_AREA*0.01,A.PEAK_LOAD_KG,A.E_AT_PEAK_LOAD_MM*0.1,A.PRC_E_AT_PEAK,A.DIAMETER*0.1,A.INNER_DIAMETER*0.1,A.OUTER_DIAMETER*0.1,A.BREAK_LOAD_KG,A.E_AT_BREAK_MM*0.1,A.PRC_E_AT_BREAK,A.STG_TENSILE_STRENGTH_KG_CM,((A.PEAK_LOAD_KG/round(A.THINCKNESS,2))*10),A.FLEXURAL_STRENGTH_KG_CM,A.SPAN*0.1  FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                
                            cursor.execute("INSERT INTO REPORT_MST_III(REPORT_ID,CYCLE_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,CS_AREA,GUAGE_MM,GRAPH_ID,MOD_AT_ANY) SELECT B.REPORT_ID,A.CYCLE_ID,A.TENSILE_STRENGTH,A.MODULUS_100,A.MODULUS_200,A.MODULUS_300,B.MOD_AT_ANY,A.CS_AREA,B.GUAGE_MM,A.GRAPH_ID,IFNULL(A.MODULUS_ANY,0) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                                
                            ### update load At Any 
                            cursor.execute("UPDATE GLOBAL_VAR SET NEW_REPORT_ID = (SELECT REPORT_ID FROM REPORT_MST WHERE STATUS='PENDING_GRAPH' AND TEST_ID='"+str(self.test_id)+"')")                                
                            cursor.execute("UPDATE REPORT_MST_III  SET SET_LOW = (SELECT BREAKING_SENCE FROM SETTING_MST ) WHERE report_id IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")               
                    elif(self.unit_type == "Lb/Inch"):    
                            self.kg_to_lb=float(2.20462)
                            self.mm_to_inch=float(0.0393701)                                                        
                            cursor.execute("INSERT INTO REPORT_MST_II(REPORT_ID,CYCLE_ID,THICKNESS,WIDTH,CS_AREA,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,DIAMETER,INN_DIAMETER,OUT_DIAMTER,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN) SELECT B.REPORT_ID,A.CYCLE_ID,(A.THINCKNESS*'"+str(self.mm_to_inch)+"'),(A.WIDTH*'"+str(self.mm_to_inch)+"'),(A.CS_AREA*'"+str(self.mm_to_inch)+"'*'"+str(self.mm_to_inch)+"'),(A.PEAK_LOAD_KG*'"+str(self.kg_to_lb)+"'),A.E_AT_PEAK_LOAD_MM,A.PRC_E_AT_PEAK,A.DIAMETER*'"+str(self.mm_to_inch)+"',A.INNER_DIAMETER*'"+str(self.mm_to_inch)+"',A.OUTER_DIAMETER*'"+str(self.mm_to_inch)+"',A.BREAK_LOAD_KG,A.E_AT_BREAK_MM*'"+str(self.mm_to_inch)+"',A.PRC_E_AT_BREAK,A.STG_TENSILE_STRENGTH_LB_INCH,(A.PEAK_LOAD_KG*('"+str(self.kg_to_lb)+"')/(A.THINCKNESS *'"+str(self.mm_to_inch)+"')),A.FLEXURAL_STRENGTH_LB_INCH,A.SPAN*'"+str(self.mm_to_inch)+"' FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                
                            cursor.execute("INSERT INTO REPORT_MST_III(REPORT_ID,CYCLE_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,CS_AREA,GUAGE_MM,GRAPH_ID,MOD_AT_ANY) SELECT B.REPORT_ID,A.CYCLE_ID,(A.peak_load_kg*'"+str(self.kg_to_lb)+"')/(A.cs_area*('"+str(self.mm_to_inch)+"'*'"+str(self.mm_to_inch)+"')),(A.Load100_guage*'"+str(self.kg_to_lb)+"')/(A.cs_area*('"+str(self.mm_to_inch)+"'*'"+str(self.mm_to_inch)+"')),(A.Load200_guage*'"+str(self.kg_to_lb)+"')/(A.cs_area*('"+str(self.mm_to_inch)+"'*'"+str(self.mm_to_inch)+"')),(A.Load300_guage*'"+str(self.kg_to_lb)+"')/(A.cs_area*('"+str(self.mm_to_inch)+"'*'"+str(self.mm_to_inch)+"')),B.MOD_AT_ANY,A.CS_AREA,B.GUAGE_MM,A.GRAPH_ID,IFNULL(A.MODULUS_ANY,0) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                                
                            cursor.execute("UPDATE GLOBAL_VAR SET NEW_REPORT_ID = (SELECT REPORT_ID FROM REPORT_MST WHERE STATUS='PENDING_GRAPH' AND TEST_ID='"+str(self.test_id)+"')")                                
                            cursor.execute("UPDATE REPORT_MST_III  SET SET_LOW = (SELECT BREAKING_SENCE FROM SETTING_MST ) WHERE report_id IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")               
                    
                    elif(self.unit_type == "Newton/Mm"):
                            self.kg_to_Newton=float(9.81)
                            cursor.execute("INSERT INTO REPORT_MST_II(REPORT_ID,CYCLE_ID,THICKNESS,WIDTH,CS_AREA,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,DIAMETER,INN_DIAMETER,OUT_DIAMTER,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN) SELECT B.REPORT_ID,A.CYCLE_ID,A.THINCKNESS,A.WIDTH,A.CS_AREA,A.PEAK_LOAD_KG*'"+str(self.kg_to_Newton)+"',A.E_AT_PEAK_LOAD_MM,A.PRC_E_AT_PEAK,A.DIAMETER,A.INNER_DIAMETER,A.OUTER_DIAMETER,A.BREAK_LOAD_KG*'"+str(self.kg_to_Newton)+"',A.E_AT_BREAK_MM,A.PRC_E_AT_BREAK,A.STG_TENSILE_STRENGTH_N_MM,((A.PEAK_LOAD_KG*'"+str(self.kg_to_Newton)+"')/A.THINCKNESS),A.FLEXURAL_STRENGTH_N_MM,A.SPAN FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                
                            cursor.execute("INSERT INTO REPORT_MST_III(REPORT_ID,CYCLE_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,CS_AREA,GUAGE_MM,GRAPH_ID,MOD_AT_ANY) SELECT B.REPORT_ID,A.CYCLE_ID,(A.peak_load_kg*'"+str(self.kg_to_Newton)+"')/(A.cs_area),(A.Load100_guage*'"+str(self.kg_to_Newton)+"')/(A.cs_area),(A.Load200_guage*'"+str(self.kg_to_Newton)+"')/(A.cs_area),(A.Load300_guage*'"+str(self.kg_to_Newton)+"')/(A.cs_area),B.MOD_AT_ANY,A.CS_AREA,B.GUAGE_MM,A.GRAPH_ID,IFNULL(A.MODULUS_ANY,0) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                                
                            cursor.execute("UPDATE GLOBAL_VAR SET NEW_REPORT_ID = (SELECT REPORT_ID FROM REPORT_MST WHERE STATUS='PENDING_GRAPH' AND TEST_ID='"+str(self.test_id)+"')")                                
                            cursor.execute("UPDATE REPORT_MST_III  SET SET_LOW = (SELECT BREAKING_SENCE FROM SETTING_MST ) WHERE report_id IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
                    elif(self.unit_type == "MPA"):
                            self.kgCm2_toMPA=float(0.0980665) 
                            cursor.execute("INSERT INTO REPORT_MST_II(REPORT_ID,CYCLE_ID,THICKNESS,WIDTH,CS_AREA,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,DIAMETER,INN_DIAMETER,OUT_DIAMTER,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN) SELECT B.REPORT_ID,A.CYCLE_ID,A.THINCKNESS,A.WIDTH,A.CS_AREA,A.PEAK_LOAD_KG,A.E_AT_PEAK_LOAD_MM,A.PRC_E_AT_PEAK,A.DIAMETER,A.INNER_DIAMETER,A.OUTER_DIAMETER,A.BREAK_LOAD_KG,A.E_AT_BREAK_MM,A.PRC_E_AT_BREAK,A.STG_TENSILE_STRENGTH_MPA,(((A.PEAK_LOAD_KG/A.THINCKNESS)*10)*0.0980665),A.FLEXURAL_STRENGTH_MPA,A.SPAN FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                
                            #print("INSERT INTO REPORT_MST_III(REPORT_ID,CYCLE_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,CS_AREA,GUAGE_MM,GRAPH_ID,MOD_AT_ANY) SELECT B.REPORT_ID,A.CYCLE_ID,(A.TENSILE_STRENGTH*'"+str(self.kgCm2_toMPA)+"'),(A.MODULUS_100*'"+str(self.kgCm2_toMPA)+"'),(A.MODULUS_200*'"+str(self.kgCm2_toMPA)+"',(A.MODULUS_300*'"+str(self.kgCm2_toMPA)+"'),(B.MOD_AT_ANY*'"+str(self.kgCm2_toMPA)+"'),A.CS_AREA,B.GUAGE_MM,A.GRAPH_ID,IFNULL(A.MODULUS_ANY,0) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH'")
                            cursor.execute("INSERT INTO REPORT_MST_III(REPORT_ID,CYCLE_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,CS_AREA,GUAGE_MM,GRAPH_ID,MOD_AT_ANY) SELECT B.REPORT_ID,A.CYCLE_ID,(A.TENSILE_STRENGTH*'"+str(self.kgCm2_toMPA)+"'),(A.MODULUS_100*'"+str(self.kgCm2_toMPA)+"'),(A.MODULUS_200*'"+str(self.kgCm2_toMPA)+"'),(A.MODULUS_300*'"+str(self.kgCm2_toMPA)+"'),(B.MOD_AT_ANY*'"+str(self.kgCm2_toMPA)+"'),A.CS_AREA,B.GUAGE_MM,A.GRAPH_ID,IFNULL(A.MODULUS_ANY,0) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                                
                            cursor.execute("UPDATE GLOBAL_VAR SET NEW_REPORT_ID = (SELECT REPORT_ID FROM REPORT_MST WHERE STATUS='PENDING_GRAPH' AND TEST_ID='"+str(self.test_id)+"')")                                
                            cursor.execute("UPDATE REPORT_MST_III  SET SET_LOW = (SELECT BREAKING_SENCE FROM SETTING_MST ) WHERE report_id IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")               
                        
                    else:
                            print("Invalid Unit Found.")
                             
                    cursor.execute("INSERT INTO REPORT_II_AGGR(TYPE_STR,REPORT_ID,THICKNESS,WIDTH,CS_AREA,DIAMETER,INN_DIAMETER,OUT_DIAMTER,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN) SELECT 'AVG',REPORT_ID,avg(THICKNESS),avg(WIDTH),avg(CS_AREA),avg(DIAMETER),AVG(INN_DIAMETER),avg(OUT_DIAMTER),avg(PEAK_LOAD),avg(E_PAEK_LOAD),avg(PREC_E_AT_PEAK),avg(BREAK_LOAD),avg(E_BREAK_LOAD),avg(PREC_E_AT_BREAK),avg(COMPRESSIVE_STRENGTH),avg(TEAR_STRENGTH),avg(FLEXURAL_STRENGTH),avg(SPAN) FROM REPORT_MST_II WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")               
                    cursor.execute("INSERT INTO REPORT_II_AGGR(TYPE_STR,REPORT_ID,THICKNESS,WIDTH,CS_AREA,DIAMETER,INN_DIAMETER,OUT_DIAMTER,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN) SELECT 'MAX',REPORT_ID, max(THICKNESS),max(WIDTH),max(CS_AREA),max(DIAMETER),max(INN_DIAMETER),max(OUT_DIAMTER),max(PEAK_LOAD),max(E_PAEK_LOAD),max(PREC_E_AT_PEAK),max(BREAK_LOAD),max(E_BREAK_LOAD),max(PREC_E_AT_BREAK),max(COMPRESSIVE_STRENGTH),max(TEAR_STRENGTH),max(FLEXURAL_STRENGTH),max(SPAN) FROM REPORT_MST_II WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                
                    cursor.execute("INSERT INTO REPORT_II_AGGR(TYPE_STR,REPORT_ID,THICKNESS,WIDTH,CS_AREA,DIAMETER,INN_DIAMETER,OUT_DIAMTER,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN) SELECT 'MIN',REPORT_ID, min(THICKNESS),min(WIDTH),min(CS_AREA),min(DIAMETER),min(INN_DIAMETER),min(OUT_DIAMTER),min(PEAK_LOAD),min(E_PAEK_LOAD),min(PREC_E_AT_PEAK),min(BREAK_LOAD),min(E_BREAK_LOAD),min(PREC_E_AT_BREAK),min(COMPRESSIVE_STRENGTH),min(TEAR_STRENGTH),min(FLEXURAL_STRENGTH),min(SPAN) FROM REPORT_MST_II WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
                    cursor.execute("INSERT INTO REPORT_III_AGGR(TYPE_STR,REPORT_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,PECENTG_MODULUS,MOD_AT_ANY) SELECT 'AVG',REPORT_ID,avg(TENSILE_STRENGTH),avg(MODULUS_100),avg(MODULUS_200),avg(MODULUS_300),avg(MODULUS_400),avg(PECENTG_MODULUS),avg(MOD_AT_ANY) FROM REPORT_MST_III WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
                    cursor.execute("INSERT INTO REPORT_III_AGGR(TYPE_STR,REPORT_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,PECENTG_MODULUS,MOD_AT_ANY) SELECT 'MAX',REPORT_ID,max(TENSILE_STRENGTH),max(MODULUS_100),max(MODULUS_200),max(MODULUS_300),max(MODULUS_400),max(PECENTG_MODULUS),max(MOD_AT_ANY) FROM REPORT_MST_III WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
                    cursor.execute("INSERT INTO REPORT_III_AGGR(TYPE_STR,REPORT_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,PECENTG_MODULUS,MOD_AT_ANY) SELECT 'MIN',REPORT_ID,min(TENSILE_STRENGTH),min(MODULUS_100),min(MODULUS_200),min(MODULUS_300),min(MODULUS_400),min(PECENTG_MODULUS),min(MOD_AT_ANY) FROM REPORT_MST_III WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                
                    cursor.execute("UPDATE REPORT_MST SET STATUS='REPORT_LOADED_SUCCESS' WHERE TEST_ID='"+str(self.test_id)+"' and STATUS='PENDING_GRAPH'")
                    #print("ok5")
                             
            connection.commit();
            connection.close()    
    
    def update_load_at_any(self,test_id,mod_at_any_input):
        #print(" test id is :"+str(test_id)+"  mod_at any input val :"+str(mod_at_any_input))
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select GUAGE_LENGTH from test_mst where test_id = '"+str(test_id)+"'") 
        for x in results:
            guage_length=str(x[0])  
        
        #print(" guage_length is :"+str(guage_length))
        connection.close() 
        calc_guage_length=(float(guage_length)*(float(mod_at_any_input)/100))
        
        #print(" Calculated guage_length is :"+str(guage_length))
        load_at_any=0
        #Get all cycles using test id , guage_lenght, grpahidi , test cs  area
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select cycle_id,graph_id,CS_AREA from CYCLES_MST where test_id = '"+str(test_id)+"'") 
        for x in results:
              load_at_any=0
              results_2=connection.execute("select x_num,y_num from graph_mst where graph_id='"+str(x[1])+"'") 
              for y in results_2:
                if(int(y[0]) >= int(calc_guage_length)):
                     load_at_any=int(y[1])
                     print("load_at_any:"+str(load_at_any))
                     break;
              with connection:        
                    cursor = connection.cursor()
                    if (self.unit_type == "Kg/Cm"):
                            cursor.execute("UPDATE CYCLES_MST SET GUAGEANY='"+str(calc_guage_length)+"',LOADANY_GUAGE='"+str(load_at_any)+"' WHERE CYCLE_ID = '"+str(x[0])+"' and test_id = '"+str(test_id)+"'")
                            cursor.execute("UPDATE CYCLES_MST SET MODULUS_ANY=(cast(LOADANY_GUAGE as real)/cast(CS_AREA as real))*100 WHERE CYCLE_ID = '"+str(x[0])+"' and test_id = '"+str(test_id)+"'")
                    elif(self.unit_type == "Lb/Inch"):
                            self.kg_to_lb=float(2.20462)
                            self.mm_to_inch=float(0.0393701) 
                            cursor.execute("UPDATE CYCLES_MST SET GUAGEANY='"+str(calc_guage_length)+"',LOADANY_GUAGE='"+str(load_at_any)+"' WHERE CYCLE_ID = '"+str(x[0])+"' and test_id = '"+str(test_id)+"'")
                            cursor.execute("UPDATE CYCLES_MST SET MODULUS_ANY=(((cast(LOADANY_GUAGE as real) *'"+str(self.kg_to_lb)+"')/(cast(CS_AREA as real) *'"+str(self.mm_to_inch)+"'*'"+str(self.mm_to_inch)+"'))) WHERE CYCLE_ID = '"+str(x[0])+"' and test_id = '"+str(test_id)+"'")
                    elif(self.unit_type == "Newton/Mm"):
                            self.kg_to_Newton=float(9.81) 
                            cursor.execute("UPDATE CYCLES_MST SET GUAGEANY='"+str(calc_guage_length)+"',LOADANY_GUAGE='"+str(load_at_any)+"' WHERE CYCLE_ID = '"+str(x[0])+"' and test_id = '"+str(test_id)+"'")
                            cursor.execute("UPDATE CYCLES_MST SET MODULUS_ANY=(((cast(LOADANY_GUAGE as real) *'"+str(self.kg_to_Newton)+"')/(cast(CS_AREA as real)))) WHERE CYCLE_ID = '"+str(x[0])+"' and test_id = '"+str(test_id)+"'")        
                    elif(self.unit_type == "MPA"):
                            self.kgCm2_toMPA=float(0.0980665) 
                            cursor.execute("UPDATE CYCLES_MST SET GUAGEANY='"+str(calc_guage_length)+"',LOADANY_GUAGE='"+str(load_at_any)+"' WHERE CYCLE_ID = '"+str(x[0])+"' and test_id = '"+str(test_id)+"'")
                            cursor.execute("UPDATE CYCLES_MST SET MODULUS_ANY=(cast(LOADANY_GUAGE as real)/cast(CS_AREA as real))*100*'"+str(self.kgCm2_toMPA)+"' WHERE CYCLE_ID = '"+str(x[0])+"' and test_id = '"+str(test_id)+"'")
                    else:
                            print(" Invalid Unit ..")
                        
        connection.commit();
        connection.close()              
                     
                     
      
        
        
        
        
        
        
    def load_report_main_data(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,B.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
             self.label_12.setText(str(x[0]))
             self.label_26.setText(str(x[1]))   ##job name
             self.label_24.setText(str(x[2]))   ##batch Id
             self.label_31.setText(str(x[3]))  ## test type
             self.label_14.setText(str(x[4])) ## specimen name
             #self.label_15.setText(str(x[7])) ## specimen specs
             self.label_18.setText(str(x[7])) ## party Name
             self.label_22.setText(str(x[5])) ## mtor speed
             self.label_20.setText(str(x[6])) ## GUAGE LENGTH
             self.label_16.setText(str(x[9])) ## shape                         
             self.label_10.setText(str(x[10])) ##test date
        connection.close()
    
    def delete_test(self):
        self.label_7.hide() 
        row = self.tableWidget.currentRow()
        if(row != -1 ):
            self.test_id=(self.tableWidget.item(row, 1).text() )
            print(" test_id :"+str(self.test_id))             
            close = QMessageBox()
            close.setText("Confirm Deleteing test id : "+str(self.test_id))
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Yes:
                 print("Yes")
                 connection = sqlite3.connect("tyr.db")        
                 with connection:        
                    cursor = connection.cursor()                
                    cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID='"+str(self.test_id)+"'")                 
                 connection.commit()
                 connection.close()
                 self.label_7.setText("Test Id :"+str(self.test_id)+" Deleted successfully !!!.")
                 self.label_7.show()
                 self.list_test()
            else:
                 print("No")         
            
           
        else:    
            self.label_7.setText("Please Select the test record  to delete.")
            self.label_7.show()
    
    def open_report(self):   
        row = self.tableWidget.currentRow()
        if(row != -1 ):
           self.test_id=(self.tableWidget.item(row, 1).text() )
           print(" test_id :"+str(self.test_id)) 
            
           self.load_report_data()
           print("ok 2")
           self.load_report_main_data()
           print("ok 3")
           self.show_report_details()
           #print("ok 4 : reproty type :"+str(self.label_31.text()))
           
           if(str(self.label_31.text())=="Compress"):
               self.create_pdf_compress()
           elif(str(self.label_31.text())=="Tear"):           
               self.create_pdf_tear()
           elif(str(self.label_31.text())=="Flexural"):    
               self.create_pdf_flexural()
           else:
               self.create_pdf_new()
           
           self.label_7.hide() 
        else:    
            self.label_7.setText("Please Select the record.")
            self.label_7.show()    
    
    def open_report_part_2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_06_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    
    def print_file(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POPUi_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_pdf(self):        
        os.system("xpdf ./reports/Reportxxx.pdf")        
        #os.system("cp ./reports/Reportxxx.pdf /media/pi/003B-E2B4")
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                os.system("cp ./reports/Reportxxx.pdf /media/usb/Report_of_test_"+str(self.test_id)+".pdf")
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
    
    
    
    def show_report_details(self):
        self.groupBox.show()
        self.graphicsView.show()
        self.pushButton_4.show()
        self.pushButton_5.show()
        self.pushButton_5_1.show()         
        self.sc =PlotCanvas(self,width=8, height=5,dpi=90)        
        self.gridLayout_2.addWidget(self.sc, 0, 0, 1, 3)
        print("ok 3.1")
        #self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 2)
            
    def set_default_resport_setting(self):
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.radioButton_5.setChecked(False)
        
        self.radioButton_3.setDisabled(True)
        self.radioButton_4.setDisabled(True)
        self.radioButton_5.setDisabled(True)
        
        self.comboBox_3.setDisabled(True)
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        
        self.comboBox_4.setEnabled(True)
        self.comboBox_5.setEnabled(True)
        
    def report_2_setting(self):
        self.radioButton.setChecked(False)
        self.radioButton_3.setEnabled(True)
        self.radioButton_4.setEnabled(True)
        self.radioButton_5.setEnabled(True)
        self.radioButton_2.setChecked(True)
        self.radioButton_3.setChecked(True)
        self.radioButton_4.setChecked(False)
        self.radioButton_5.setChecked(False)
        
        self.comboBox_4.setDisabled(True)
        self.comboBox_5.setDisabled(True)
        self.comboBox_3.setDisabled(True)
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)

    def  list_test(self):
        if (self.radioButton.isChecked()):
            #print( "report 1 ")
            self.list_report_1()
        elif(self.radioButton_2.isChecked()):        
            #print( "report 2 ")      
            self.list_report_2()      
        else:            
            print( "report -NANNA ")
    
    def list_report_1(self):
        print("test id :"+str(self.comboBox_5.currentText()))
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT BATCH_ID,TEST_ID,PARTY_NAME,(select SHAPE FROM SPECIMEN_MST WHERE SPECIMEN_MST.SPECIMEN_NAME=TEST_MST.SPECIMEN_NAME ) as SHAPE,(SELECT COUNT(*) FROM CYCLES_MST WHERE CYCLES_MST.TEST_ID=TEST_MST.TEST_ID) as CNT,GUAGE_LENGTH,CREATED_ON FROM TEST_MST where TEST_ID = '"+str(self.comboBox_4.currentText())+"' AND BATCH_ID= '"+str(self.comboBox_5.currentText())+"' AND TEST_ID IN (SELECT TEST_ID FROM CYCLES_MST) order by TEST_ID DESC ")                        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)   
        
        connection.close()
        
    def list_report_2(self):
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        connection = sqlite3.connect("tyr.db")        
        #self.from_date=str(self.lineEdit.text())
        #self.to_date=str(self.lineEdit_2.text())
        
        print ("from_date :"+str(self.from_date)+" to_date :"+str(self.to_date));
        
        if(self.radioButton_3.isChecked()):
            results=connection.execute("SELECT BATCH_ID,TEST_ID,PARTY_NAME,(select SHAPE FROM SPECIMEN_MST WHERE SPECIMEN_MST.SPECIMEN_NAME=TEST_MST.SPECIMEN_NAME ) as SHAPE,(SELECT COUNT(*) FROM CYCLES_MST WHERE CYCLES_MST.TEST_ID=TEST_MST.TEST_ID) as CN,GUAGE_LENGTH,CREATED_ON FROM TEST_MST where strftime('%Y-%m-%d',CREATED_ON) BETWEEN '"+str(self.from_date)+"' and '"+str(self.to_date)+"' AND TEST_ID IN (SELECT TEST_ID FROM CYCLES_MST) order by TEST_ID DESC ")
        elif(self.radioButton_4.isChecked()):
            results=connection.execute("SELECT BATCH_ID,TEST_ID,PARTY_NAME,(select SHAPE FROM SPECIMEN_MST WHERE SPECIMEN_MST.SPECIMEN_NAME=TEST_MST.SPECIMEN_NAME ) as SHAPE,(SELECT COUNT(*) FROM CYCLES_MST WHERE CYCLES_MST.TEST_ID=TEST_MST.TEST_ID) as CN,GUAGE_LENGTH,CREATED_ON FROM TEST_MST where strftime('%Y-%m-%d',CREATED_ON) BETWEEN '"+str(self.from_date)+"' and '"+str(self.to_date)+"'  AND PARTY_NAME = '"+str(self.comboBox_3.currentText())+"' AND TEST_ID IN (SELECT TEST_ID FROM CYCLES_MST) order by TEST_ID DESC ")            
        elif(self.radioButton_5.isChecked()):
            results=connection.execute("SELECT BATCH_ID,TEST_ID,PARTY_NAME,(select SHAPE FROM SPECIMEN_MST WHERE SPECIMEN_MST.SPECIMEN_NAME=TEST_MST.SPECIMEN_NAME ) as SHAPE,(SELECT COUNT(*) FROM CYCLES_MST WHERE CYCLES_MST.TEST_ID=TEST_MST.TEST_ID) as CN,GUAGE_LENGTH,CREATED_ON FROM TEST_MST where strftime('%Y-%m-%d',CREATED_ON) BETWEEN '"+str(self.from_date)+"' and '"+str(self.to_date)+"' AND  TEST_ID = '"+str(self.comboBox_4.currentText())+"' AND BATCH_ID= '"+str(self.comboBox_5.currentText())+"' AND TEST_ID IN (SELECT TEST_ID FROM CYCLES_MST) order by TEST_ID DESC ")    
        else:              
            results=connection.execute("SELECT BATCH_ID,TEST_ID,PARTY_NAME,(select SHAPE FROM SPECIMEN_MST WHERE SPECIMEN_MST.SPECIMEN_NAME=TEST_MST.SPECIMEN_NAME ) as SHAPE,(SELECT COUNT(*) FROM CYCLES_MST WHERE CYCLES_MST.TEST_ID=TEST_MST.TEST_ID) as CN,GUAGE_LENGTH,CREATED_ON FROM TEST_MST where TEST_ID = '"+str(self.comboBox_4.currentText())+"' AND BATCH_ID= '"+str(self.comboBox_5.currentText())+"' AND TEST_ID IN (SELECT TEST_ID FROM CYCLES_MST) order by TEST_ID DESC ")
        
        
                                
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()    
        
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)      
    
    def create_pdf_flexural(self):        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
        for x in results:
            self.graph_typex=x[0]
            self.unit_typex=x[1]
        connection.close()
        
        if(self.unit_typex == "Kg/Cm"):
            data2= [ ['Spec. \n No', 'Thickness  \n (cm)','Width  \n (cm)','Span  \n (cm)','Length at Peak \n (cm)', 'Force at Peak\n (Kgf)', 'Flexural Strength \n (Kgf/cm2)']]
        elif(self.unit_typex == "Lb/Inch"):
            data2= [ ['Spec. \n No', 'Thickness  \n (Inch)','Width  \n (Inch)','Span  \n (Inch)','Length at Peak \n (Inch)', 'Force at Peak\n (Lb)', 'Flexural Strength \n (Lb/Inch2)']]           
        elif(self.unit_typex == "Newton/Mm"):
            data2= [ ['Spec. \n No', 'Thickness  \n (mm)','Width  \n (mm)','Span  \n (mm)','Length at Peak \n (mm)', 'Force at Peak\n (N)', 'Flexural Strength \n (N/mm2)']]            
        elif(self.unit_typex == "MPA"):
            data2= [ ['Spec. \n No', 'Thickness  \n (mm)','Width  \n (mm)','Span  \n (mm)','Length at Peak \n (mm)', 'Force at Peak\n (Kg)', 'Flexural Strength \n (MPA)']]           
        else:
            data2= [ ['Spec. \n No', 'Thickness \n (mm)','Width \n (mm)','Span  \n (mm)','Length at Peak \n (mm)', 'Force at Peak\n (Kg)', 'Flexural Strength \n (MPA)']]
          
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.2f\", A.SPAN),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.FLEXURAL_STRENGTH) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", THICKNESS),printf(\"%.2f\", WIDTH),printf(\"%.2f\", SPAN),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", FLEXURAL_STRENGTH) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close() 
        
        y=300
        Elements=[]
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,CURRENT_TIMESTAMP  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)")
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
        comments = Paragraph("Remark : ______________________________________________________________________________", styles["Normal"])
        
        footer_2= Paragraph("Authorised and Signed By : _________________.", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
       
        
        #f1=Table(data)
        #f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
        
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11)]))       
        
         
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/Reportxxx.pdf', rightMargin=10,
                                leftMargin=30,
                                topMargin=20,
                                bottomMargin=20,)
        doc.build(Elements)
        #print("Done")
        
    def create_pdf_tear(self):        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
        for x in results:
            self.graph_typex=x[0]
            self.unit_typex=x[1]
        connection.close()
        
        if(self.unit_typex == "Kg/Cm"):
            data2= [ ['Spec. \n No', 'Thickness \n (cm)', 'Force at Peak\n (Kgf)', 'Tear Strength \n (Kgf/cm)']]
        elif(self.unit_typex == "Lb/Inch"):
            data2= [ ['Spec. \n No', 'Thickness \n (Inch)', 'Force at Peak\n (Lb)', 'Tear Strength \n (Lb/Inch)']]           
        elif(self.unit_typex == "Newton/Mm"):
            data2= [ ['Spec. \n No', 'Thickness \n (mm)', 'Force at Peak\n (N)', 'Tear Strength \n (N/mm)']]            
        elif(self.unit_typex == "MPA"):
            data2= [ ['Spec. \n No', 'Thickness \n (mm)', 'Force at Peak\n (Kg)', 'Tear Strength \n (MPA)']]           
        else:
            data2= [ ['Spec. \n No', 'Thickness \n (mm)', 'Force at Peak\n (Kg)', 'Tear Strength \n (Kg/cm)']]
          
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.TEAR_STRENGTH) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", THICKNESS),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", TEAR_STRENGTH) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close() 
        
        y=300
        Elements=[]
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,CURRENT_TIMESTAMP  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)")
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
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11)]))       
        
         
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,blank,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/Reportxxx.pdf', rightMargin=10,
                                leftMargin=20,
                                topMargin=50,
                                bottomMargin=20,)
        doc.build(Elements)
        #print("Done")
                
    def create_pdf_compress(self):        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
        for x in results:
            self.graph_typex=x[0]
            self.unit_typex=x[1]
        connection.close()
        
        if(self.unit_typex == "Kg/Cm"):
            data2= [ ['Spec. \n No', 'CS Area \n (cm2)', 'Force at Peak\n (Kgf)', 'Compression \n (cm)', 'Compressive Strength \n (Kgf/Cm2)',' % Compression \n']]
        elif(self.unit_typex == "Lb/Inch"):
            data2= [ ['Spec. \n No', 'CS Area \n (Inch2)', 'Force at Peak\n (Lb)', 'Compression \n (Inch)', 'Compressive Strength \n (Lb/Inch2)',' % Compression \n']]           
        elif(self.unit_typex == "Newton/Mm"):
            data2= [ ['Spec. \n No', 'CS Area \n (mm2)', 'Force at Peak\n (N)', 'Compression \n (mm)', 'Compressive Strength \n (N/mm2)',' % Compression \n']]            
        elif(self.unit_typex == "MPA"):
            data2= [ ['Spec. \n No', 'CS Area \n (mm2)', 'Force at Peak\n (Kg)', 'Compression \n (mm)', 'Compressive Strength \n (MPA)',' % Compression \n']]           
        else:
            data2= [ ['Spec. \n No', 'CS Area \n (mm2)', 'Force at Peak\n (Kg)', 'Compression \n (mm)', 'Compressive Strength \n (MPA)',' % Compression \n']]
          
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.COMPRESSIVE_STRENGTH),printf(\"%3d\", A.PREC_E_AT_BREAK) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TYPE_STR,printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", COMPRESSIVE_STRENGTH),printf(\"%3d\", PREC_E_AT_BREAK) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close() 
        
        y=300
        Elements=[]
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,CURRENT_TIMESTAMP  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)")
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
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11)]))       
        
         
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,blank,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/Reportxxx.pdf', rightMargin=10,
                                leftMargin=20,
                                topMargin=20,
                                bottomMargin=30,)
        doc.build(Elements)
        #print("Done")
       
        
        
        
        
        
        
        
        
 
    def create_pdf_new(self):        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
        for x in results:
            self.graph_typex=x[0]
            self.unit_typex=x[1]
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SHAPE FROM SPECIMEN_MST WHERE SPECIMEN_NAME IN ( SELECT SPECIMEN_NAME FROM TEST_MST WHERE TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR))") 
        for x in results:
            self.shape=x[0]
        connection.close()
        
        if (self.shape=="Rectangle"):
            
            if(self.unit_typex == "Kg/Cm"):            
                    data= [['Spec. \n No.', 'Thickness \n (cm)', 'Width \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n']]
            elif(self.unit_typex == "Lb/Inch"):
                    data= [['Spec. \n No.', 'Thickness \n (Inch)', 'Width \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak \n','E@Break \n (Inch)','%E@Break \n']]
            elif(self.unit_typex == "Newton/Mm"):
                    data= [['Spec. \n No.', 'Thickness \n (mm)', 'Width \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','E@Peak \n %','E@Break \n (mm)','E@Break \n %']]
            else:        
                    data= [['Spec. \n No.', 'Thickness \n (mm)', 'Width \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (kg)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]
          
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%3d\", A.PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%3d\", A.PREC_E_AT_BREAK)  FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", THICKNESS),printf(\"%.2f\", WIDTH),printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%3d\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%3d\", PREC_E_AT_BREAK) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()            
            
                    
        elif (self.shape=="Cylindrical"):
            if(self.unit_typex == "Kg/Cm"):    
                data= [['Spe. \n No.', 'Diameter \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n']]
            elif(self.unit_typex == "Lb/Inch"):                
                data= [['Spe. \n No.', 'Diameter \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak \n','E@Break \n (Inch)','%E@Break \n']]
            elif(self.unit_typex == "Newton/Mm"):
                data= [['Spe. \n No.', 'Diameter \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]
            else:    
                data= [['Spe. \n No.', 'Diameter \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (kgf)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]

            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,round(A.DIAMETER,2),printf(\"%.4f\", A.CS_AREA),round(A.PEAK_LOAD,0),round(A.E_PAEK_LOAD,2),round(A.PREC_E_AT_PEAK,2),round(A.E_BREAK_LOAD,2),round(A.PREC_E_AT_BREAK,2) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,round(DIAMETER,2),printf(\"%.4f\", CS_AREA),round(PEAK_LOAD,0),round(E_PAEK_LOAD,0),round(PREC_E_AT_PEAK,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()            
            
        elif (self.shape=="Pipe"):            
            if(self.unit_typex == "Kg/Cm"):                
                data= [['Spec. \n No.', 'Inn.Dia \n (cm)', 'Out. Dia \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n']]
            elif(self.unit_typex == "Lb/Inch"):                 
                data= [['Spec. \n No.', 'Inn.Dia \n (Inch)', 'Out. Dia \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak \n','E@Break \n (Inch)','%E@Break \n']]
            elif(self.unit_typex == "Newton/Mm"):
                data= [['Spec. \n No.', 'Inn.Dia \n (mm)', 'Out. Dia \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]
            else:                
                data= [['Spec. \n No.', 'Inn.Dia \n (mm)', 'Out. Dia \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (kgf)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]
            
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.INN_DIAMETER),printf(\"%.2f\", A.OUT_DIAMTER),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD), printf(\"%3d\", A.PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%3d\", A.PREC_E_AT_BREAK) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", INN_DIAMETER),printf(\"%.2f\", OUT_DIAMTER),printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD) ,printf(\"%3d\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%3d\", PREC_E_AT_BREAK) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()            
            
        elif (self.shape=="DirectValue"):
            if(self.unit_typex == "Kg/Cm"):    
                data= [['Spec.\n No.', 'CS.Area \n (cm)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n']]
            elif(self.unit_typex == "Lb/Inch"):
                data= [['Spec.\n No.', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak \n','E@Break \n (Inch)','%E@Break \n']]
            elif(self.unit_typex == "Newton/Mm"):
                data= [['Spec.\n No.', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]
            else:                
                data= [['Spec.\n No.', 'CS.Area \n (mm2)','Force at Peak \n (kgf)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']] 
                
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.4f\", A.CS_AREA),round(A.PEAK_LOAD,2),round(A.E_PAEK_LOAD,2),round(A.PREC_E_AT_PEAK,2),round(A.E_BREAK_LOAD,2),round(A.PREC_E_AT_BREAK,2) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,printf(\"%.4f\", CS_AREA),round(PEAK_LOAD,2),round(E_PAEK_LOAD,2),round(PREC_E_AT_PEAK,2),round(E_BREAK_LOAD,2),round(PREC_E_AT_BREAK,2) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()            
                       
        else:
           data= [['Spec. \n No.', 'Thickness (mm)', 'Width (mm)', 'CS.Area (mm2)','Peak Load (kgf)' ,'% E@Peak \n','Break Load (Kg)','E@Break (mm)','%E@Break \n']]
          
           connection = sqlite3.connect("tyr.db")
           results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,A.THICKNESS,A.WIDTH,printf(\"%.4f\", A.CS_AREA),A.PEAK_LOAD,A.E_PAEK_LOAD,round(A.PREC_E_AT_PEAK,2),round(A.E_BREAK_LOAD,2),round(A.PREC_E_AT_BREAK,2) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
           for x in results:
                data.append(x)
           connection.close()  
 
           connection = sqlite3.connect("tyr.db")
           results=connection.execute("SELECT TYPE_STR,round(THICKNESS,2),round(WIDTH,2),printf(\"%.4f\", CS_AREA),PEAK_LOAD,round(E_PAEK_LOAD,2),PREC_E_AT_BREAK FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
           for x in results:
               data.append(x)
           connection.close()            

           
           
        if(self.unit_typex == "Kg/Cm"):
            data2= [ ['Spec. \n No', 'TensileStrength \n (Kgf/Cm2)', 'Mod@100% \n (Kgf/Cm2)', 'Mod@200% \n (Kgf/Cm2)', 'Mod@300% \n (Kgf/Cm2)']]
        elif(self.unit_typex == "Lb/Inch"):
            data2= [ ['Spec. \n No', 'TensileStrength \n (Lb/Inch2)', 'Mod@100% \n (Lb/Inch2)', 'Mod@200% \n (Lb/Inch2)', 'Mod@300% \n (Lb/Inch2)']]
        elif(self.unit_typex == "Newton/Mm"):
            data2= [ ['Spec. \n No', 'TensileStrength \n (N/Mm2)', 'Mod@100% \n (N/Mm2)', 'Mod@200% \n (N/Mm2)', 'Mod@300% \n (N/Mm2)']]
        elif(self.unit_typex == "MPA"):
            data2= [ ['Spec. \n No', 'TensileStrength \n (MPA)', 'Mod@100% \n (MPA)', 'Mod@200% \n (MPA)', 'Mod@300% \n (MPA)']]    
        else:
            data2= [ ['Spec. \n No', 'TensileStrength \n (Kg/Cm2)', 'Mod@100% \n (Kg/Cm2)', 'Mod@200% \n (Kg/Cm2)', 'Mod@300% \n (Kg/Cm2)']]
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT MOD_AT_ANY FROM REPORT_MST WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                        
        for rows in results:
            if(self.unit_typex == "Lb/Inch"):
                data2[0].append("Mod@"+str(rows[0])+"% \n (Lb/Inch2)")
            elif(self.unit_typex == "Newton/Mm"):
                data2[0].append("Mod@"+str(rows[0])+"% \n (N/Mm2)")
            elif(self.unit_typex == "MPA"):
                data2[0].append("Mod@"+str(rows[0])+"% \n (MPA)")    
            else:    
                data2[0].append("Mod@"+str(rows[0])+"% \n (Kg/Cm2)")
        connection.close()
                   
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select ((A.REC_ID-B.MIN_REC_ID)+1) as SPECIMEN_NUM,printf(\"%.2f\", A.TENSILE_STRENGTH),printf(\"%.2f\", A.MODULUS_100),printf(\"%.2f\", A.MODULUS_200) ,printf(\"%.2f\", A.MODULUS_300),printf(\"%.2f\", A.MOD_AT_ANY) FROM REPORT_MST_III A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_III WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)) B WHERE A.REPORT_ID =B.REPORT_ID") 
        for x in results:
            data2.append(x)
        connection.close()  
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select TYPE_STR,printf(\"%.2f\", TENSILE_STRENGTH),printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200) ,printf(\"%.2f\", MODULUS_300),printf(\"%.2f\", MOD_AT_ANY) from REPORT_III_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
        for x in results:
            data2.append(x)
        connection.close()           
        
        
        y=300
        Elements=[]
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,CURRENT_TIMESTAMP  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Specmen Shape:",str(x[9])],["Test Type:",str(x[3]),"Specmen Specs:",str(x[0])],["Party Name :",str(x[7]),"Motor Speed :",str(x[5])],["Guage Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", "Stech engineers testing machine","",""]]
      
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
        comments = Paragraph("Remark : ______________________________________________________________________________", styles["Normal"])
        
        footer_2= Paragraph("Authorised and Signed By : _________________.", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
       
        
        f1=Table(data)
        f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
        
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10)]))       
        
         
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4* inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f1,Spacer(1,12),Spacer(1,12),f2,Spacer(1,12),blank,comments,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        '''
        doc = SimpleDocTemplate('./reports/Reportxxx.pdf', pagesize=A4, rightMargin=10,
                                leftMargin=40,
                                topMargin=30,
                                bottomMargin=30,)
        '''
        doc = SimpleDocTemplate('./reports/Reportxxx.pdf', pagesize=A4,rightMargin=20,
                                leftMargin=30,
                                topMargin=30,
                                bottomMargin=30)
        doc.build(Elements)
        #print("Done")
       
        
        
        
            

 
 
 
 
 
 
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)        
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.graph_type=""
        self.unit_type=""
        self.cs_area=0
        self.guage=0
        self.test_type=""
        self.plot()        
        
    def plot(self):
        #data = [random.random() for i in range(25)]
                
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#CCFFFF')
        #ax.setStyleSheet("background-color: rgb(255, 239, 242);")
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM ") 
        for x in results:
            self.graph_type=str(x[0])
            self.unit_type=str(x[1])          
        connection.close()        
        self.graph_ids=[]    
        self.x_num=[0]
        self.y_num=[0] 
        self.color=['b','r','g','y','k','c','m','b']
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_ID,TEST_ID,SHAPE,CS_AREA,IFNULL(GUAGE100,0) FROM CYCLES_MST WHERE TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
                self.graph_ids.append(x[0])             
                ax.set_title("Test Id="+str(x[1]))
                self.cs_area=(x[3])
                self.guage=(x[4])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TEST_NAME FROM REPORT_MST LIMIT 1") 
        for x in results:                
                self.test_type=(x[0])              
        connection.close()
        
        
        
        
        if (self.graph_type == "Load Vs Elongation"):       
                for g in range(len(self.graph_ids)):
                    #print("graph id :"+str(self.graph_ids[g]))
                    self.x_num=[0]
                    self.y_num=[0]
                    connection = sqlite3.connect("tyr.db")
                    if(self.test_type=="Compress" or self.test_type=="Flexural"):                        
                            results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    else:
                        if(self.unit_type == "Lb/Inch"):    
                            self.kg_to_lb=float(2.20462)
                            self.mm_to_inch=float(0.0393701) 
                            results=connection.execute("SELECT X_NUM*'"+str(self.mm_to_inch)+"',Y_NUM*'"+str(self.kg_to_lb)+"'FROM GRAPH_MST WHERE X_NUM > 0 AND GRAPH_ID='"+str(self.graph_ids[g])+"'")
                        elif(self.unit_type == "Newton/Mm"):
                            self.kg_to_Newton=float(9.81)                                
                            results=connection.execute("SELECT X_NUM,Y_NUM*'"+str(self.kg_to_Newton)+"'FROM GRAPH_MST WHERE X_NUM > 0 AND GRAPH_ID='"+str(self.graph_ids[g])+"'")
                            
                        else:
                            results=connection.execute("SELECT X_NUM*0.1,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    for k in results:
                        self.x_num.append(k[0])
                        self.y_num.append(k[1])
                    connection.close() 
                    if (g < 8):
                         ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
                if(self.test_type=="Compress"):
                    if(self.unit_type == "Lb/Inch"):  
                         ax.set_xlabel('Compression(Inch)')
                         ax.set_ylabel('Load(Lb)')
                    elif(self.unit_type == "Newton/Mm"):
                         ax.set_xlabel('Compression(mm)')
                         ax.set_ylabel('Load(N)')      
                    else:
                         ax.set_xlabel('Compression(cm)')
                         ax.set_ylabel('Load(Kg)')    
                else:
                    if(self.unit_type == "Lb/Inch"):  
                         ax.set_xlabel('Elongation(Inch)')
                         ax.set_ylabel('Load(Lb)')
                    elif(self.unit_type == "Newton/Mm"):
                         ax.set_xlabel('Elongation(mm)')
                         ax.set_ylabel('Load(N)')  
                    else:
                         ax.set_xlabel('Elongation(cm)')
                         ax.set_ylabel('Load(Kgf)')    
                
                ax.legend()
                ax.minorticks_on()
                ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
                self.draw()
                self.figure.savefig('last_graph.png',dpi=100)
                
        elif(self.graph_type == "Stress Vs Strain"):
            #print("Graph Type :"+str(self.graph_type)) 
            for g in range(len(self.graph_ids)):
                #print("graph id :"+str(self.graph_ids[g]))
                self.x_num=[0]
                self.y_num=[0]
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                for k in results:                    
                    self.x_num.append((k[0]/float(self.guage))*100)
                    self.y_num.append((k[1]/float(self.cs_area)))
                connection.close() 
            
                if (g < 8):
                    ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
                
                ax.set_xlabel('Strain(%)')
                ax.set_ylabel('Stress')    
                ax.legend()
                ax.minorticks_on()
                ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
                ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
                self.draw()
                self.figure.savefig('last_graph.png',dpi=100)
        else:
            print("Incorrect Graph Type !!!")   
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_03_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
