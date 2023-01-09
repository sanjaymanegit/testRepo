


from MDR_06_REPORT_MDR import mdr_06_Ui_MainWindow
from print_sr_popup import SR_P_POPUi_MainWindow


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem
import datetime
import sqlite3
from PyQt5.QtCore import QDate
import os,sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import landscape, letter,inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak,Spacer, PageTemplate
from reportlab.lib import colors
import os,sys
from reportlab.rl_config import defaultPageSize
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import landscape, letter,inch,A4


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






LastStateRole = QtCore.Qt.UserRole 

class mdr_05_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
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
        self.label_20.setGeometry(QtCore.QRect(1100, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(950, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(200, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(300, 20, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(340, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(440, 20, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(470, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
#        self.comboBox_2.addItem("")
#        self.comboBox_2.addItem("")
#        self.comboBox_2.addItem("")
#        self.comboBox_2.addItem("")
#        self.comboBox_2.addItem("")
#        self.comboBox_2.addItem("")
        self.comboBox_7 = QtWidgets.QComboBox(self.frame)
        self.comboBox_7.setGeometry(QtCore.QRect(470, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
#        self.comboBox_7.setObjectName("comboBox_7")
#        self.comboBox_7.addItem("")
#        self.comboBox_7.addItem("")
#        self.comboBox_7.addItem("")
#        self.comboBox_7.addItem("")
#        self.comboBox_7.addItem("")
#        self.comboBox_7.addItem("")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(300, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(440, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame)
        self.comboBox_8.setGeometry(QtCore.QRect(340, 80, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_8.setObjectName("comboBox_8")
#        self.comboBox_8.addItem("")
#        self.comboBox_8.addItem("")
#        self.comboBox_8.addItem("")
#        self.comboBox_8.addItem("")
#        self.comboBox_8.addItem("")
#        self.comboBox_8.addItem("")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(990, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        #self.pushButton_13.setStyleSheet("background-color: rgb(90, 90, 134);\n""color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/print4.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_13.setObjectName("pushButton_13")
        
        
        self.pushButton_13_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13_1.setGeometry(QtCore.QRect(1050, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13_1.setFont(font)
        #self.pushButton_13.setStyleSheet("background-color: rgb(90, 90, 134);\n""color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/delete2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13_1.setIcon(icon1)
        self.pushButton_13_1.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_13_1.setObjectName("pushButton_13_1")
        
        
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(110, 250, 341, 231))
        self.calendarWidget.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget_2.setGeometry(QtCore.QRect(480, 250, 341, 231))
        self.calendarWidget_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.calendarWidget_2.setGridVisible(True)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 130, 1331, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 160, 1301, 541))
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
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 6, item)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(680, 80, 180, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        #self.comboBox_3.setStyleSheet("background-color: rgb(170, 255, 255);\n color: rgb(0, 0, 0);")
        self.comboBox_3.setObjectName("comboBox_3")       
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(680, 20, 180, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        #self.comboBox_4.setStyleSheet("background-color: rgb(170, 255, 255);\n color: rgb(0, 0, 0);")
        self.comboBox_4.setObjectName("comboBox_4")
        
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(1230, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(880, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(880, 52, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(560, 76, 91, 41))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(560, 10, 91, 51))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_20.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        self.pushButton_8.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_12.raise_()
        self.label_5.raise_()
        self.comboBox.raise_()
        self.label_6.raise_()
        self.comboBox_2.raise_()
        self.comboBox_7.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.comboBox_8.raise_()
        self.pushButton_13.raise_()
        self.line.raise_()
        self.tableWidget.raise_()
        self.calendarWidget.raise_()
        self.calendarWidget_2.raise_()
        self.comboBox_3.raise_()
        self.comboBox_4.raise_()
        self.pushButton_14.raise_()
        self.checkBox.raise_()
        self.label_21.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
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
                  
        
        
        self.test_ids=[]
        self.length=""
        self.test_id="0"
        self.test_id_type=""
        self.email_flg="N"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00"))
        self.pushButton_3.setText(_translate("MainWindow", "Search"))
        self.pushButton_4.setText(_translate("MainWindow", "View Pdf (Selected Tests)"))
        self.lineEdit.setText(_translate("MainWindow", "2020-10-14"))
        self.label_3.setText(_translate("MainWindow", "FROM:"))
        self.pushButton_8.setText(_translate("MainWindow", "DATE"))
        self.label_4.setText(_translate("MainWindow", "TO:"))
        self.lineEdit_2.setText(_translate("MainWindow", "2020-10-14"))
        self.pushButton_12.setText(_translate("MainWindow", "DATE"))
        self.label_5.setText(_translate("MainWindow", "HH:"))
        self.i=0        
        for x in range(24):            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str("%02d"%x))            
            self.i=self.i+1
        self.i=0 
        self.label_6.setText(_translate("MainWindow", "MI:"))
        for x in range(60):            
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        self.i=0        
        for x in range(60):            
            self.comboBox_7.addItem("")
            self.comboBox_7.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        self.label_11.setText(_translate("MainWindow", "HH:"))
        self.label_12.setText(_translate("MainWindow", "MI:"))
        self.i=0  
        for x in range(24):            
            self.comboBox_8.addItem("")
            self.comboBox_8.setItemText(self.i,str("%02d"%x))            
            self.i=self.i+1
            
        #self.pushButton_13.setText(_translate("MainWindow", "Print"))
        self.tableWidget.setSortingEnabled(True)
        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.comboBox_3.setItemText(0, _translate("MainWindow", "--- All Methods ---"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Method1"))
        
        self.pushButton_14.setText(_translate("MainWindow", "Return"))
        self.checkBox.setText(_translate("MainWindow", "ALL"))
        self.label_21.setText(_translate("MainWindow", "No Data Found"))
        self.label_21.hide()
        self.calendarWidget.hide()
        self.calendarWidget_2.hide()
        self.pushButton_14.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.select_all_tests)
        self.checkBox.clicked.connect(self.check_uncheck_all_records)
        self.pushButton_4.clicked.connect(self.open_all_recds_pdf)
        self.pushButton_13.setDisabled(True)
        self.pushButton_13.clicked.connect(self.print_file)
        self.pushButton_13_1.clicked.connect(self.del_tests)
        
        
        
        self.comboBox.setCurrentText("00")
        self.comboBox.setCurrentText("00")
        self.comboBox_8.setCurrentText("23")
        self.comboBox_7.setCurrentText("59")
        self.radioButton.setChecked(True)
        self.radioButton.setText("Method:")
        self.radioButton_2.setText("Batch:")
        
        self.startx()
        
        self.radioButton.clicked.connect(self.onRadiobutton_click)
        self.radioButton_2.clicked.connect(self.onRadiobutton_click)
        self.onRadiobutton_click()
        
    def onRadiobutton_click(self):
        if(self.radioButton.isChecked()):
            print("1")
            self.comboBox_3.setEnabled(True)
            self.comboBox_4.setDisabled(True)
        elif(self.radioButton_2.isChecked()):
            print("2")
            self.comboBox_3.setDisabled(True)
            self.comboBox_4.setEnabled(True)       
        else:
            self.comboBox_3.setEnabled(True)
            self.comboBox_4.setDisabled(True)
    
    def startx(self):
        self.calendarWidget.hide()
        self.calendarWidget_2.hide()
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        self.pushButton_8.clicked.connect(self.from_on_click1)
        self.pushButton_12.clicked.connect(self.to_on_click2)
        
       
        self.calendarWidget.clicked.connect(self.calendar1_on_click)
        self.calendarWidget_2.clicked.connect(self.calendar2_on_click)
        
        
        self.lineEdit.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.lineEdit_2.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        
        #self.select_all_lost_bags()
        self.i=0
        self.comboBox_3.clear()
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("SELECT DISTINCT METHOD_NAME FROM TEST_MST_MDR ") 
        for x in results:            
            self.comboBox_3.addItem("")
            self.comboBox_3.setItemText(self.i,str(x[0]))
            #print("i :"+str(x[0]))
            self.i=self.i+1
        connection.close()
        
        
        self.i=0
        self.comboBox_4.clear()
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("SELECT DISTINCT BATCH_ID FROM TEST_MST_MDR ") 
        for x in results:            
            self.comboBox_4.addItem("")
            self.comboBox_4.setItemText(self.i,str(x[0]))           
            self.i=self.i+1
        connection.close()
       
       
        self.pushButton_4.clicked.connect(self.select_all_tests)
        self.tableWidget.doubleClicked.connect(self.open_doubleClick_report)
        #self.checkBox.clicked.connect(self.check_uncheck_all_records)
        #self.pushButton_14_2.clicked.connect(self.del_cheked)
       
        
        self.select_all_tests()
    
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    
    def from_on_click1(self):
        self.calendarWidget.show()
    
    def to_on_click2(self):
        self.calendarWidget_2.show()
        
    def calendar1_on_click(self):
        temp_var = self.calendarWidget.selectedDate() 
        var_name = temp_var.toPyDate()        
        #self.from_dt=str(var_name)
        self.lineEdit.setText(str(self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)))
        self.calendarWidget.hide()
        
    
    def calendar2_on_click(self):
        temp_var = self.calendarWidget_2.selectedDate() 
        var_name = temp_var.toPyDate()        
        #self.to_dt=str(var_name)
        self.lineEdit_2.setText(str(self.calendarWidget_2.selectedDate().toString(QtCore.Qt.ISODate)))
        self.calendarWidget_2.hide()
    
    def select_all_tests(self):
        #self.pushButton_14_1.setEnabled(True)
        self.from_dt=self.lineEdit.text()+" "+str(self.comboBox.currentText())+":"+str(self.comboBox_2.currentText())+":00"
        self.to_dt=self.lineEdit_2.text()+" "+str(self.comboBox_8.currentText())+":"+str(self.comboBox_7.currentText())+":00"
        self.party_name=str(self.comboBox_3.currentText())
        self.specimen_name=str(self.comboBox_4.currentText())
        #self.unit_type=str(self.comboBox_5.currentText())
        
        print("frm:"+str(self.from_dt)+"   to:"+str(self.to_dt))
        self.specimen_shape=""
        
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        #font.setBold(True)
        #font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 250)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 150)
        self.tableWidget.setColumnWidth(7, 150)
        
      
       
        #self.tableWidget.setColumnWidth(5, 150)
        #print("whr_sql2 :"+str(self.whr_sql2))
        self.tableWidget.setHorizontalHeaderLabels(['Test No.','Test Date','Spec.No','Batch ID.','Method Name','Max.Torque (N)','Test.Time (Min)','Max.Temparature (.C)'])        
         
        connection = sqlite3.connect("mdr.db")  
        if(self.radioButton.isChecked()):
                print("r1")
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.SPECIMEN_NUM,B.batch_id,B.METHOD_NAME,B.TRQ,B.TEST_TIME_MIN,B.TEST_TEMP,B.ARC FROM TEST_MST_MDR B where B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' AND B.METHOD_NAME = '"+str(self.comboBox_3.currentText())+"'")                        
        elif(self.radioButton_2.isChecked()):
                print("r2")
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.SPECIMEN_NUM,B.batch_id,B.METHOD_NAME,B.TRQ,B.TEST_TIME_MIN,B.TEST_TEMP,B.ARC FROM TEST_MST_MDR B where B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' AND B.BATCH_ID = '"+str(self.comboBox_4.currentText())+"'")                        
        else:
                print("r3")
                results=connection.execute("SELECT B.TEST_ID,B.CREATED_ON,B.SPECIMEN_NUM,B.batch_id,B.METHOD_NAME,B.TRQ,B.TEST_TIME_MIN,B.TEST_TEMP,B.ARC FROM TEST_MST_MDR B where B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' AND B.METHOD_NAME = '"+str(self.comboBox_3.currentText())+"'")                        
      
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if(int(column_number) == 0):
                    #print("data-column_number :"+str(column_number))
                    item = QtWidgets.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(not QtCore.Qt.Checked)
                    item.setText(str(data))
                    self.tableWidget.setItem(row_number,column_number,item)
                    #self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                else:
                    self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                #self.lineEdit.setText("")
        connection.close()   
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
        connection = sqlite3.connect("mdr.db")          
        with connection:        
                cursor = connection.cursor()
                cursor.execute("DELETE FROM TEST_IDS")
                if(self.radioButton.isChecked()):
                    cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,'NA'  FROM TEST_MST_MDR B  where B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' and B.METHOD_NAME = '"+str(self.comboBox_3.currentText())+"'") 
                elif(self.radioButton_2.isChecked()):        
                    cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,'NA'  FROM TEST_MST_MDR B  where B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' and B.BATCH_ID = '"+str(self.comboBox_4.currentText())+"'") 
                else:
                    print("checked tests id issue")
        connection.commit();
        connection.close()
        
     
    def print_file(self):
        test_count=0
        connection = sqlite3.connect("mdr.db")        
        results=connection.execute("SELECT count(TEST_ID) FROM TEST_IDS ")        
        for x in results:
                test_count=str(x[0])                
        connection.close()
        
        if(int(test_count) > 0):                         
                self.window = QtWidgets.QMainWindow()
                self.ui=SR_P_POPUi_MainWindow()
                self.ui.setupUi(self.window)           
                self.window.show()
            
        
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1            
            self.tableWidget.removeRow(i)
            
    
    def open_all_recds_pdf(self):
        self.del_uncheked()
        self.sc_blank =PlotCanvas(self,width=8, height=5,dpi=100)  
        self.create_all_rec_pdf()
        self.pushButton_13.setEnabled(True)
        os.system("xpdf ./reports/all_records.pdf")
    
    
    def create_all_rec_pdf(self):
        self.del_uncheked()
        #self.load_reports()
        self.specimen_shape=""
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        test_type=""
        test_count=0
        
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("select COMPANY_NAME,ADDRESS1 from SETTING_MST ") 
        for x in results:            
            Title = Paragraph(str(x[0]), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        if(self.radioButton.isChecked()):
             self.name="Method Name"
             self.name_str=str(self.comboBox_3.currentText())           
        else:
             self.name="Batch Id"
             self.name_str=str(self.comboBox_4.currentText())
        
        
        
        summary_data=[["From Date:",str(self.from_dt),"To Date: ",str(self.to_dt) , str(self.name),str(self.name_str), "Report Date: ",str(datetime.datetime.now().strftime("%d %b %Y %H:%M"))]]
       
           
        
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),('FONTNAME', (4, 0), (4, -1), 'Helvetica-Bold'),('FONTNAME', (6, 0), (6, -1), 'Helvetica-Bold')]))       
        
        report_gr_img="all_graphs.png"        
        pdf_img= Image(report_gr_img, 10* inch, 6 * inch)
        #pdf_img= Image(report_gr_img)
        
       
        
        connection = sqlite3.connect("mdr.db")        
        results=connection.execute("SELECT count(TEST_ID) FROM TEST_IDS ")        
        for x in results:
                test_count=str(x[0])                
        connection.close()
        
        childs_data=[]        
        if(int(test_count) > 0):
            childs_data.append(['Test Id','Spec.No.','S_ML','S_MH','S2_ML','S2_MH','T_S1','T_S2','T_S5','TC_10','TC_50','TC_90','Tan at ML','Tan at MH','OC','CR','End Temp.','Trend','RT'])  
            connection = sqlite3.connect("mdr.db")
            results=connection.execute("SELECT TEST_ID,SPECIMEN_NUM,printf(\"%.2f\", S_ML),printf(\"%.2f\", S_MH),printf(\"%.2f\", S2_ML),printf(\"%.2f\", S2_MH),printf(\"%.2f\", T_S1),printf(\"%.2f\", T_S2),printf(\"%.2f\", T_S5),printf(\"%.2f\", TC_10),printf(\"%.2f\", TC_50),printf(\"%.2f\", TC_90),printf(\"%.2f\", TAN_AT_ML),printf(\"%.2f\", TAN_AT_MH),printf(\"%.2f\", OC),printf(\"%.2f\", CR),printf(\"%.2f\", END_TEMP),TREAND,printf(\"%.2f\", RT)   FROM TEST_MST_MDR WHERE TEST_ID IN ( SELECT TEST_ID FROM TEST_IDS )")
            for k in results:
                        childs_data.append(k)
            connection.close()
        else:
            print("Please Select Tests.")
        
        Elements = [Title,Spacer(1,12),Title2,Spacer(1,12),f3,Spacer(1,12),Spacer(1,12),pdf_img,Spacer(1,12),Spacer(1,12)]
        
        
        if(int(test_count) > 0):
            f=Table(childs_data)
            f.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
            Elements.append(f) 
            
            
        doc = SimpleDocTemplate('./reports/all_records.pdf',pagesize=A4 ,rightMargin=10,
                                leftMargin=20,
                                topMargin=10,
                                bottomMargin=10,)
        doc.pagesize = landscape(A4)
        doc.build(Elements)
    
    
    def del_tests(self):
        self.del_uncheked()
        test_count=0
        connection = sqlite3.connect("mdr.db")        
        results=connection.execute("SELECT count(TEST_ID) FROM TEST_IDS ")        
        for x in results:
                test_count=str(x[0])                
        connection.close()        
        if(int(test_count) > 0):
                        close = QMessageBox()
                        close.setText("Deleteting test which are checked. Please Confirm !!!")
                        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                        close = close.exec()                                
                        if close == QMessageBox.Yes: 
                                    connection = sqlite3.connect("mdr.db")
                                    with connection:        
                                            cursor = connection.cursor()                                        
                                            cursor.execute("delete from TEST_MST_MDR WHERE  TEST_ID IN (SELECT TEST_ID FROM TEST_IDS)")                                            
                                    connection.commit();
                                    connection.close()
                                    self.select_all_tests()
                                    print("deleted  test ID:"+str(self.test_id))
                        else:
                                    print(" Cancled Delete.")                                
        else:
                print(" Do not Delete this test id")
                    
    def del_uncheked(self):
        i = self.tableWidget.rowCount()
        records_cnt=int(i)    
        while (i > 0):
            i=i-1
            item = self.tableWidget.item(i, 0)
            #print("test id  :"+str(item.text()))
            currentState = item.checkState()
            if(currentState == QtCore.Qt.Checked):
                    print("Checked test ID:"+str(item.text()))
                    connection = sqlite3.connect("mdr.db")          
                    with connection:        
                            cursor = connection.cursor()                            
                            cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,'NA'  FROM TEST_MST_MDR B WHERE B.TEST_ID='"+str(item.text())+"' AND B.TEST_ID NOT IN (SELECT TEST_ID FROM TEST_IDS)") 
                    connection.commit();
                    connection.close()                    
            else:
                    print("Un-Checked test ID:"+str(item.text()))
                    connection = sqlite3.connect("mdr.db")          
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM TEST_IDS WHERE TEST_ID = '"+str(item.text())+"'")                             
                    connection.commit();
                    connection.close()
        
    def open_doubleClick_report(self):
        row = self.tableWidget.currentRow()
        if(row != -1 ):
            self.test_id=(self.tableWidget.item(row, 0).text() )
            print(" test_id :"+str(self.test_id))        
        
            connection = sqlite3.connect("mdr.db")
            with connection:        
                  cursor = connection.cursor()                                        
                  cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID = '"+str(self.test_id)+"'")              
            connection.commit();
            connection.close() 
        
        self.window = QtWidgets.QMainWindow()
        self.ui=mdr_06_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()   
            
    def check_uncheck_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            item = self.tableWidget.item(i, 0)
            if(self.checkBox.isChecked()):
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(not QtCore.Qt.Checked)
        

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
#        ax2 = ax.twinx()
#        color = 'tab:green'
#        ax2.set_ylabel('TEMP (.C)', color = color)
#        ax2.set_ylim(0,200)
        
        ax.grid(which='major', linestyle='-', linewidth='0.30', color='black')
        ax.grid(which='minor', linestyle=':', linewidth='0.30', color='black')
        
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
        connection.close()
        
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("SELECT GRAPH_ID FROM TEST_MST_MDR WHERE TEST_ID IN (SELECT TEST_ID FROM TEST_IDS)") 
        for x in results:
             self.graph_ids.append(x[0])             
        connection.close()
        
        
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
        
            connection = sqlite3.connect("mdr.db")               
            results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            for k in results:        
                self.x_num.append(k[0])
                self.y_num.append(k[1])
                #self.r_num.append(k[2])
            connection.close() 
        
            if(g < 8 ):
                ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1),linewidth=0.60)
                #ax2.plot(self.x_num,self.r_num, 'g',label="Temparature")
            else:
                ax.plot(self.x_num,self.y_num, 'b',label="Specimen_"+str(g+1),linewidth=0.56)
        
        ax.set_xlabel('TIME (Min)')
        ax.set_ylabel('TORQUE(N)')
        
         #self.connect('motion_notify_event', mouse_move)
        ax.legend()
        #ax2.legend() 
        self.draw()
        self.figure.savefig('all_graphs.png',dpi=100)
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mdr_05_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
