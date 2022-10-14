
from print_sr_popup import SR_P_POPUi_MainWindow
from email_multiple_files import email_multi_Ui_MainWindow

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


class TY_10_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 1331, 691))
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
        self.label_20.setGeometry(QtCore.QRect(1140, 20, 171, 31))
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
        self.pushButton_3.setGeometry(QtCore.QRect(990, 80, 81, 31))
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
        self.pushButton_4.setGeometry(QtCore.QRect(880, 80, 81, 31))
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
#        font.setBold(True)
#        font.setWeight(75)
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
        #font.setBold(True)
        #font.setWeight(75)
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
        self.comboBox.setGeometry(QtCore.QRect(350, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        #font.setBold(True)
        #font.setWeight(75)
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
        self.comboBox_2.setGeometry(QtCore.QRect(490, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        #font.setBold(True)
        #font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        
        self.comboBox_7 = QtWidgets.QComboBox(self.frame)
        self.comboBox_7.setGeometry(QtCore.QRect(490, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        #font.setBold(True)
        #font.setWeight(75)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_7.setObjectName("comboBox_7")
        
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
        self.comboBox_8.setGeometry(QtCore.QRect(350, 80, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        #font.setBold(True)
        #font.setWeight(75)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_8.setObjectName("comboBox_8")
        
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(1100, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
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
        self.tableWidget.setGeometry(QtCore.QRect(10, 160, 1301, 511))
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
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(560, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(630, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        #font.setBold(True)
        #font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_3.setObjectName("comboBox_3")
        #self.comboBox_3.addItem("")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(820, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(930, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        #font.setBold(True)
        #font.setWeight(75)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_4.setObjectName("comboBox_4")       
        
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(1210, 60, 81, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        
        self.pushButton_14_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14_1.setGeometry(QtCore.QRect(1210, 100, 81, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14_1.setFont(font)
        self.pushButton_14_1.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_14_1.setObjectName("pushButton_14_1")
        
        
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(780, 80, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(560, 80, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame)
        self.comboBox_5.setGeometry(QtCore.QRect(630, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        #font.setBold(True)
        #font.setWeight(75)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_5.setObjectName("comboBox_5")
       
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(880, 51, 421, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
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
        self.label_7.raise_()
        self.comboBox_3.raise_()
        self.label_8.raise_()
        self.comboBox_4.raise_()
        self.pushButton_14.raise_()
        self.checkBox.raise_()
        self.label_9.raise_()
        self.comboBox_5.raise_()
        self.label_21.raise_()
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
                  
        self.kg_to_lb=float(2.20462)
        self.mm_to_inch=float(0.0393701)
        self.kg_to_Newton=float(9.81)
        self.kgCm2_toMPA=float(0.0980665)
        
        self.test_ids=[]
        self.length=""
        self.test_id=""
        self.test_id_type=""
        self.email_flg="N"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00"))
        self.pushButton_4.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton_3.setText(_translate("MainWindow", "VIEW"))
        self.lineEdit.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "FROM:"))
        self.pushButton_8.setText(_translate("MainWindow", "DATE"))
        self.label_4.setText(_translate("MainWindow", "TO:"))
        self.lineEdit_2.setText(_translate("MainWindow", ""))
        self.pushButton_12.setText(_translate("MainWindow", "DATE"))
        self.label_5.setText(_translate("MainWindow", "HH:"))
        self.i=0        
        for x in range(24):            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        
        self.label_6.setText(_translate("MainWindow", "MI:"))
        self.i=0  
        for x in range(60):            
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        self.label_11.setText(_translate("MainWindow", "HH:"))
        self.label_12.setText(_translate("MainWindow", "MI:"))
        self.i=0  
        for x in range(24):            
            self.comboBox_8.addItem("")
            self.comboBox_8.setItemText(self.i,str("%02d"%x))            
            self.i=self.i+1
            
        
        self.i=0        
        for x in range(60):            
            self.comboBox_7.addItem("")
            self.comboBox_7.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        self.pushButton_13.setText(_translate("MainWindow", "PRINT"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TEST.NO"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TEST.NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "BATCH.ID"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "NO.OF.CYCLES"))
        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1212"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "PARTY :"))
        #self.comboBox_3.setItemText(0, _translate("MainWindow", "MRF"))
        self.label_8.setText(_translate("MainWindow", "SPECIMEN :"))
        
        self.pushButton_14.setText(_translate("MainWindow", "RETURN"))
        self.pushButton_14_1.setText(_translate("MainWindow", "EMAIL"))
        #self.pushButton_14_1.setDisabled(True)
        self.checkBox.setText(_translate("MainWindow", "ALL"))
        
        self.label_9.setText(_translate("MainWindow", "UNIT    :"))
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Kg/Cm"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "MPA"))
        self.label_21.setText(_translate("MainWindow", "No Data Found"))
        self.label_21.hide()
        self.calendarWidget.hide()
        self.calendarWidget_2.hide()
        self.pushButton_14.clicked.connect(MainWindow.close)
        self.pushButton_14_1.clicked.connect(self.email_click)
        self.comboBox.setCurrentText("00")
        self.comboBox.setCurrentText("00")
        self.comboBox_8.setCurrentText("23")
        self.comboBox_7.setCurrentText("59")
        self.startx()
    
    def startx(self):
        self.calendarWidget.hide()
        self.calendarWidget_2.hide()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.pushButton_8.clicked.connect(self.from_on_click1)
        self.pushButton_12.clicked.connect(self.to_on_click2)
        self.pushButton_13.clicked.connect(self.print_file)
       
        self.calendarWidget.clicked.connect(self.calendar1_on_click)
        self.calendarWidget_2.clicked.connect(self.calendar2_on_click)
        #
        #self.pushButton_3.clicked.connect(self.select_all_lost_bags)
        #self.pushButton_4.clicked.connect(self.select_all_edited)
        
        self.lineEdit.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.lineEdit_2.setText(datetime.datetime.now().strftime("%Y-%m-%d"))
        
        #self.select_all_lost_bags()
        self.i=0
        self.comboBox_3.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT PARTY_NAME FROM SPECIMEN_MST") 
        for x in results:            
            self.comboBox_3.addItem("")
            self.comboBox_3.setItemText(self.i,str(x[0]))
            #print("i :"+str(x[0]))
            self.i=self.i+1
        connection.close()
        self.comboBox_3.currentTextChanged.connect(self.onchage_party)
        self.pushButton_3.clicked.connect(self.open_pdf)
        self.pushButton_4.clicked.connect(self.select_all_tests)
        self.checkBox.clicked.connect(self.check_uncheck_all_records)
        self.onchage_party()
        self.select_all_tests()
        
    def onchage_party(self):
        self.i=0
        self.comboBox_4.clear()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT SPECIMEN_NAME FROM SPECIMEN_MST where  PARTY_NAME='"+self.comboBox_3.currentText()+"'") 
        for x in results:            
            self.comboBox_4.addItem("")
            self.comboBox_4.setItemText(self.i,str(x[0]))
            #print("i :"+str(x[0]))
            self.i=self.i+1
        connection.close()
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def email_click(self):
        os.system("sudo rm ./reports/emailed/multiple/Report*.pdf")
        self.email_flg="Y"
        self.del_uncheked()
        self.load_reports()
        self.window = QtWidgets.QMainWindow()
        self.ui=email_multi_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()    
          
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
        self.unit_type=str(self.comboBox_5.currentText())
        
        print("frm:"+str(self.from_dt)+"   to:"+str(self.to_dt))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SHAPE FROM SPECIMEN_MST  WHERE SPECIMEN_NAME ='"+str(self.specimen_name)+"' LIMIT 1") 
        for x in results:
            self.specimen_shape=str(x[0])         
        connection.close()
        
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        #font.setBold(True)
        #font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 200)
        self.tableWidget.setColumnWidth(6, 250)
        #self.tableWidget.setColumnWidth(5, 150)
        #print("whr_sql2 :"+str(self.whr_sql2))
        self.tableWidget.setHorizontalHeaderLabels(['TEST NO.','NO.OF.CYCLES.','CREATED-ON','TEST-TYPE','SPEC. SHAPE','SPEC-NAME','PARTY'])        
         
        connection = sqlite3.connect("tyr.db")  
        print("SELECT B.TEST_ID,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.CREATED_ON,B.TEST_TYPE,'"+str(self.specimen_shape)+"','"+str(self.specimen_name)+"','"+str(self.party_name)+"' FROM TEST_MST B where B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"'")                        
        results=connection.execute("SELECT B.TEST_ID,(SELECT COUNT(*) as cnt FROM CYCLES_MST A WHERE A.TEST_ID=B.TEST_ID) as CYCLES_CNT,B.CREATED_ON,B.TEST_TYPE,'"+str(self.specimen_shape)+"','"+str(self.specimen_name)+"','"+str(self.party_name)+"' FROM TEST_MST B where B.TEST_ID IN (SELECT TEST_ID FROM CYCLES_MST) AND B.TEST_TYPE IN (SELECT NEW_TEST_NAME  FROM GLOBAL_VAR) AND B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' and SPECIMEN_NAME='"+str(self.specimen_name)+"'")                        
       
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
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
        connection = sqlite3.connect("tyr.db")          
        with connection:        
                cursor = connection.cursor()
                cursor.execute("UPDATE GLOBAL_VAR SET SR_FROM_DT='"+str(self.from_dt)+"', SR_TO_DT='"+str(self.to_dt)+"', SR_PARTY_NAME='"+str(self.party_name)+"',SR_SPECIMENT_NAME='"+str(self.specimen_name)+"',SR_UNIT_TYPE='"+str(self.unit_type)+"'")
                cursor.execute("DELETE FROM TEST_IDS")
                cursor.execute("INSERT INTO TEST_IDS SELECT B.TEST_ID,B.TEST_TYPE  FROM TEST_MST B  where B.TEST_ID IN (SELECT TEST_ID FROM CYCLES_MST) AND B.TEST_TYPE IN (SELECT NEW_TEST_NAME  FROM GLOBAL_VAR) AND B.CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' and SPECIMEN_NAME='"+str(self.specimen_name)+"'") 
        connection.commit();
        connection.close()
        
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1            
            self.tableWidget.removeRow(i)
    
    def check_uncheck_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            item = self.tableWidget.item(i, 0)
            if(self.checkBox.isChecked()):
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(not QtCore.Qt.Checked)
    
    def load_reports(self):        
            self.unit_type=""
            self.def_flg=""
            self.kg_to_lb=float(2.20462)
            self.mm_to_inch=float(0.0393701)
            self.kg_to_Newton=float(9.81)
            self.kgCm2_toMPA=float(0.0980665)
            self.test_ids=[]
            self.unit_type=self.comboBox_5.currentText()
            #print("Graph Type :"+str(self.comboBox.currentText()))
            connection = sqlite3.connect("tyr.db")        
            with connection:        
                            cursor = connection.cursor()                
                            cursor.execute("DELETE FROM REPORT_MST")
                            cursor.execute("DELETE FROM REPORT_MST_II")
                            cursor.execute("DELETE FROM REPORT_MST_III")
                            
            connection.commit();
            connection.close()
            
            connection = sqlite3.connect("tyr.db")  
            results=connection.execute("SELECT B.TEST_ID  FROM TEST_IDS B ")
            for x in results:
                self.test_ids.append(str(x[0]))
            connection.close()
            
            #for x in self.test_ids:
            for x in range(len(self.test_ids)):
                    self.test_id=str(self.test_ids[x])
                    self.test_id_type=""
                    
                    
                    connection = sqlite3.connect("tyr.db")        
                    with connection:        
                            cursor = connection.cursor()                
                            cursor.execute("UPDATE GLOBAL_VAR SET NEW_REPORT_TEST_ID='"+str(self.test_id)+"'")                                    
                            cursor.execute("INSERT INTO REPORT_MST (TEST_ID,REPORT_TYPE,REPORT_UNIT,MOD_AT_ANY) VALUES('"+str(self.test_id)+"','','"+str(self.unit_type)+"','')")
                            cursor.execute("UPDATE REPORT_MST SET GUAGE_MM = (SELECT GUAGE_LENGTH FROM TEST_MST WHERE TEST_ID  = '"+str(self.test_id)+"')")
                            cursor.execute("UPDATE REPORT_MST SET TEST_NAME = (SELECT TEST_TYPE FROM TEST_MST WHERE TEST_ID  = '"+str(self.test_id)+"')")
                           
                            if (self.unit_type == "Kg/Cm"):                       
                                    cursor.execute("INSERT INTO REPORT_MST_II(REPORT_ID,CYCLE_ID,THICKNESS,WIDTH,CS_AREA,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,DIAMETER,INN_DIAMETER,OUT_DIAMTER,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH, TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN,ULT_SHEAR_STRENGTH_KG_CM,ULT_SHEAR_STRAIN_KG_CM,SHEAR_STRAIN_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_NAME_KG_CM,BREAK_MODE,TEMPERATURE,SPAN,TEST_METHOD,def_yeild_strg) SELECT B.REPORT_ID,A.CYCLE_ID,A.THINCKNESS*0.1,A.WIDTH*0.1,A.CS_AREA*0.01,A.PEAK_LOAD_KG,A.E_AT_PEAK_LOAD_MM*0.1,A.PRC_E_AT_PEAK,A.DIAMETER*0.1,A.INNER_DIAMETER*0.1,A.OUTER_DIAMETER*0.1,A.BREAK_LOAD_KG,A.E_AT_BREAK_MM*0.1,A.PRC_E_AT_BREAK,A.STG_TENSILE_STRENGTH_KG_CM,((A.PEAK_LOAD_KG/round(A.THINCKNESS,2))*10),A.FLEXURAL_STRENGTH_KG_CM,A.SPAN*0.1,A.ULT_SHEAR_STRENGTH_KG_CM,A.ULT_SHEAR_STRAIN_KG_CM,A.SHEAR_STRAIN_COLUMN_VALUE_KG_CM,A.SHEAR_MOD_COLUMN_VALUE_KG_CM,A.SHEAR_MOD_COLUMN_NAME_KG_CM ,A.BREAK_MODE,A.TEMPERATURE,A.SPAN,A.TEST_METHOD,((A.DEF_LOAD)/(A.CS_AREA*0.1*0.1)) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                
                                    cursor.execute("INSERT INTO REPORT_MST_III(REPORT_ID,CYCLE_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,CS_AREA,GUAGE_MM,GRAPH_ID,MOD_AT_ANY) SELECT B.REPORT_ID,A.CYCLE_ID,A.TENSILE_STRENGTH,A.MODULUS_100,A.MODULUS_200,A.MODULUS_300,B.MOD_AT_ANY,A.CS_AREA,B.GUAGE_MM,A.GRAPH_ID,IFNULL(A.MODULUS_ANY,0) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                                
                                    ### update load At Any 
                                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_REPORT_ID = (SELECT REPORT_ID FROM REPORT_MST WHERE STATUS='PENDING_GRAPH' AND TEST_ID='"+str(self.test_id)+"')")                                
                                    cursor.execute("UPDATE REPORT_MST_III  SET SET_LOW = (SELECT BREAKING_SENCE FROM SETTING_MST ) WHERE report_id IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")               
                            elif(self.unit_type == "Lb/Inch"):    
                                    self.kg_to_lb=float(2.20462)
                                    self.mm_to_inch=float(0.0393701)                                                        
                                    cursor.execute("INSERT INTO REPORT_MST_II(REPORT_ID,CYCLE_ID,THICKNESS,WIDTH,CS_AREA,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,DIAMETER,INN_DIAMETER,OUT_DIAMTER,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN,ULT_SHEAR_STRENGTH_KG_CM,ULT_SHEAR_STRAIN_KG_CM,SHEAR_STRAIN_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_NAME_KG_CM,BREAK_MODE,TEMPERATURE,SPAN,TEST_METHOD,def_yeild_strg) SELECT B.REPORT_ID,A.CYCLE_ID,(A.THINCKNESS*'"+str(self.mm_to_inch)+"'),(A.WIDTH*'"+str(self.mm_to_inch)+"'),(A.CS_AREA*'"+str(self.mm_to_inch)+"'*'"+str(self.mm_to_inch)+"'),(A.PEAK_LOAD_KG*'"+str(self.kg_to_lb)+"'),A.E_AT_PEAK_LOAD_MM,A.PRC_E_AT_PEAK,A.DIAMETER*'"+str(self.mm_to_inch)+"',A.INNER_DIAMETER*'"+str(self.mm_to_inch)+"',A.OUTER_DIAMETER*'"+str(self.mm_to_inch)+"',A.BREAK_LOAD_KG,A.E_AT_BREAK_MM*'"+str(self.mm_to_inch)+"',A.PRC_E_AT_BREAK,A.STG_TENSILE_STRENGTH_LB_INCH,(A.PEAK_LOAD_KG*('"+str(self.kg_to_lb)+"')/(A.THINCKNESS *'"+str(self.mm_to_inch)+"')),A.FLEXURAL_STRENGTH_LB_INCH,A.SPAN*'"+str(self.mm_to_inch)+"',A.ULT_SHEAR_STRENGTH_LB_INCH,A.ULT_SHEAR_STRAIN_LB_INCH,A.SHEAR_STRAIN_COLUMN_VALUE_LB_INCH,A.SHEAR_MOD_COLUMN_VALUE_LB_INCH,A.SHEAR_MOD_COLUMN_NAME_LB_INCH,A.BREAK_MODE,A.TEMPERATURE,A.SPAN,A.TEST_METHOD,(A.DEF_LOAD*2.20462)/(A.CS_AREA*0.0393701*0.0393701) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                
                                    cursor.execute("INSERT INTO REPORT_MST_III(REPORT_ID,CYCLE_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,CS_AREA,GUAGE_MM,GRAPH_ID,MOD_AT_ANY) SELECT B.REPORT_ID,A.CYCLE_ID,(A.peak_load_kg*'"+str(self.kg_to_lb)+"')/(A.cs_area*('"+str(self.mm_to_inch)+"'*'"+str(self.mm_to_inch)+"')),(A.Load100_guage*'"+str(self.kg_to_lb)+"')/(A.cs_area*('"+str(self.mm_to_inch)+"'*'"+str(self.mm_to_inch)+"')),(A.Load200_guage*'"+str(self.kg_to_lb)+"')/(A.cs_area*('"+str(self.mm_to_inch)+"'*'"+str(self.mm_to_inch)+"')),(A.Load300_guage*'"+str(self.kg_to_lb)+"')/(A.cs_area*('"+str(self.mm_to_inch)+"'*'"+str(self.mm_to_inch)+"')),B.MOD_AT_ANY,A.CS_AREA,B.GUAGE_MM,A.GRAPH_ID,IFNULL(A.MODULUS_ANY,0) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                                
                                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_REPORT_ID = (SELECT REPORT_ID FROM REPORT_MST WHERE STATUS='PENDING_GRAPH' AND TEST_ID='"+str(self.test_id)+"')")                                
                                    cursor.execute("UPDATE REPORT_MST_III  SET SET_LOW = (SELECT BREAKING_SENCE FROM SETTING_MST ) WHERE report_id IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")               
                            
                            elif(self.unit_type == "Newton/Mm"):
                                    self.kg_to_Newton=float(9.81)
                                    cursor.execute("INSERT INTO REPORT_MST_II(REPORT_ID,CYCLE_ID,THICKNESS,WIDTH,CS_AREA,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,DIAMETER,INN_DIAMETER,OUT_DIAMTER,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN,ULT_SHEAR_STRENGTH_KG_CM,ULT_SHEAR_STRAIN_KG_CM,SHEAR_STRAIN_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_NAME_KG_CM,BREAK_MODE,TEMPERATURE,SPAN,TEST_METHOD,def_yeild_strg) SELECT B.REPORT_ID,A.CYCLE_ID,A.THINCKNESS,A.WIDTH,A.CS_AREA,A.PEAK_LOAD_KG*'"+str(self.kg_to_Newton)+"',A.E_AT_PEAK_LOAD_MM,A.PRC_E_AT_PEAK,A.DIAMETER,A.INNER_DIAMETER,A.OUTER_DIAMETER,A.BREAK_LOAD_KG*'"+str(self.kg_to_Newton)+"',A.E_AT_BREAK_MM,A.PRC_E_AT_BREAK,A.STG_TENSILE_STRENGTH_N_MM,((A.PEAK_LOAD_KG*'"+str(self.kg_to_Newton)+"')/A.THINCKNESS),A.FLEXURAL_STRENGTH_N_MM,A.SPAN ,A.ULT_SHEAR_STRENGTH_N_MM,A.ULT_SHEAR_STRAIN_N_MM,A.SHEAR_STRAIN_COLUMN_VALUE_N_MM,A.SHEAR_MOD_COLUMN_VALUE_N_MM,A.SHEAR_MOD_COLUMN_NAME_N_MM,A.BREAK_MODE,A.TEMPERATURE,A.SPAN,A.TEST_METHOD,(A.DEF_LOAD*9.81)/A.CS_AREA  FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                
                                    cursor.execute("INSERT INTO REPORT_MST_III(REPORT_ID,CYCLE_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,CS_AREA,GUAGE_MM,GRAPH_ID,MOD_AT_ANY) SELECT B.REPORT_ID,A.CYCLE_ID,(A.peak_load_kg*'"+str(self.kg_to_Newton)+"')/(A.cs_area),(A.Load100_guage*'"+str(self.kg_to_Newton)+"')/(A.cs_area),(A.Load200_guage*'"+str(self.kg_to_Newton)+"')/(A.cs_area),(A.Load300_guage*'"+str(self.kg_to_Newton)+"')/(A.cs_area),B.MOD_AT_ANY,A.CS_AREA,B.GUAGE_MM,A.GRAPH_ID,IFNULL(A.MODULUS_ANY,0) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                                
                                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_REPORT_ID = (SELECT REPORT_ID FROM REPORT_MST WHERE STATUS='PENDING_GRAPH' AND TEST_ID='"+str(self.test_id)+"')")                                
                                    cursor.execute("UPDATE REPORT_MST_III  SET SET_LOW = (SELECT BREAKING_SENCE FROM SETTING_MST ) WHERE report_id IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
                            elif(self.unit_type == "MPA"):
                                    self.kgCm2_toMPA=float(0.0980665)
                                    self.kg_to_Newton=float(9.81)
                                    cursor.execute("INSERT INTO REPORT_MST_II(REPORT_ID,CYCLE_ID,THICKNESS,WIDTH,CS_AREA,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,DIAMETER,INN_DIAMETER,OUT_DIAMTER,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN,ULT_SHEAR_STRENGTH_KG_CM,ULT_SHEAR_STRAIN_KG_CM,SHEAR_STRAIN_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_NAME_KG_CM,BREAK_MODE,TEMPERATURE,SPAN,TEST_METHOD,def_yeild_strg) SELECT B.REPORT_ID,A.CYCLE_ID,A.THINCKNESS,A.WIDTH,A.CS_AREA,A.PEAK_LOAD_KG*'"+str(self.kg_to_Newton)+"',A.E_AT_PEAK_LOAD_MM,A.PRC_E_AT_PEAK,A.DIAMETER,A.INNER_DIAMETER,A.OUTER_DIAMETER,A.BREAK_LOAD_KG*'"+str(self.kg_to_Newton)+"',A.E_AT_BREAK_MM,A.PRC_E_AT_BREAK,A.STG_TENSILE_STRENGTH_MPA,((((A.PEAK_LOAD_KG*'"+str(self.kg_to_Newton)+"')/A.THINCKNESS)*10)*0.0980665),A.FLEXURAL_STRENGTH_MPA,A.SPAN,A.ULT_SHEAR_STRENGTH_MPA,A.ULT_SHEAR_STRAIN_MPA,A.SHEAR_STRAIN_COLUMN_VALUE_MPA,A.SHEAR_MOD_COLUMN_VALUE_MPA,A.SHEAR_MOD_COLUMN_NAME_MPA,A.BREAK_MODE,A.TEMPERATURE,A.SPAN,A.TEST_METHOD,A.DEF_YEILD_STRG*0.0980665 FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                
                                    #print("INSERT INTO REPORT_MST_III(REPORT_ID,CYCLE_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,CS_AREA,GUAGE_MM,GRAPH_ID,MOD_AT_ANY) SELECT B.REPORT_ID,A.CYCLE_ID,(A.TENSILE_STRENGTH*'"+str(self.kgCm2_toMPA)+"'),(A.MODULUS_100*'"+str(self.kgCm2_toMPA)+"'),(A.MODULUS_200*'"+str(self.kgCm2_toMPA)+"',(A.MODULUS_300*'"+str(self.kgCm2_toMPA)+"'),(B.MOD_AT_ANY*'"+str(self.kgCm2_toMPA)+"'),A.CS_AREA,B.GUAGE_MM,A.GRAPH_ID,IFNULL(A.MODULUS_ANY,0) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH'")
                                    cursor.execute("INSERT INTO REPORT_MST_III(REPORT_ID,CYCLE_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,CS_AREA,GUAGE_MM,GRAPH_ID,MOD_AT_ANY) SELECT B.REPORT_ID,A.CYCLE_ID,(A.TENSILE_STRENGTH*'"+str(self.kgCm2_toMPA)+"'),(A.MODULUS_100*'"+str(self.kgCm2_toMPA)+"'),(A.MODULUS_200*'"+str(self.kgCm2_toMPA)+"'),(A.MODULUS_300*'"+str(self.kgCm2_toMPA)+"'),(B.MOD_AT_ANY*'"+str(self.kgCm2_toMPA)+"'),A.CS_AREA,B.GUAGE_MM,A.GRAPH_ID,IFNULL(A.MODULUS_ANY,0) FROM CYCLES_MST A, REPORT_MST B WHERE B.TEST_ID='"+str(self.test_id)+"' AND A.TEST_ID=B.TEST_ID AND B.STATUS='PENDING_GRAPH' order by A.GRAPH_ID")                                
                                    
                                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_REPORT_ID = (SELECT REPORT_ID FROM REPORT_MST WHERE STATUS='PENDING_GRAPH' AND TEST_ID='"+str(self.test_id)+"')")                                
                                    cursor.execute("UPDATE REPORT_MST_III  SET SET_LOW = (SELECT BREAKING_SENCE FROM SETTING_MST ) WHERE report_id IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")               
                                
                            else:
                                    print("Invalid Unit Found.")
                            
                            print("Test ID :"+str(self.test_id))
                            print("INSERT INTO REPORT_II_AGGR(TYPE_STR,REPORT_ID,THICKNESS,WIDTH,CS_AREA,DIAMETER,INN_DIAMETER,OUT_DIAMTER,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN,ULT_SHEAR_STRENGTH_KG_CM,ULT_SHEAR_STRAIN_KG_CM,SHEAR_STRAIN_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_VALUE_KG_CM,def_yeild_strg) SELECT 'AVG',REPORT_ID,avg(THICKNESS),avg(WIDTH),avg(CS_AREA),avg(DIAMETER),AVG(INN_DIAMETER),avg(OUT_DIAMTER),avg(PEAK_LOAD),avg(E_PAEK_LOAD),avg(PREC_E_AT_PEAK),avg(BREAK_LOAD),avg(E_BREAK_LOAD),avg(PREC_E_AT_BREAK),avg(COMPRESSIVE_STRENGTH),avg(TEAR_STRENGTH),avg(FLEXURAL_STRENGTH),avg(SPAN),avg(ULT_SHEAR_STRENGTH_KG_CM),avg(ULT_SHEAR_STRAIN_KG_CM),avg(SHEAR_STRAIN_COLUMN_VALUE_KG_CM),avg(SHEAR_MOD_COLUMN_VALUE_KG_CM), avg(def_yeild_strg) FROM REPORT_MST_II WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")               
                            
                            cursor.execute("INSERT INTO REPORT_II_AGGR(TYPE_STR,REPORT_ID,THICKNESS,WIDTH,CS_AREA,DIAMETER,INN_DIAMETER,OUT_DIAMTER,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN,ULT_SHEAR_STRENGTH_KG_CM,ULT_SHEAR_STRAIN_KG_CM,SHEAR_STRAIN_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_VALUE_KG_CM,def_yeild_strg) SELECT 'AVG',REPORT_ID,avg(THICKNESS),avg(WIDTH),avg(CS_AREA),avg(DIAMETER),AVG(INN_DIAMETER),avg(OUT_DIAMTER),avg(PEAK_LOAD),avg(E_PAEK_LOAD),avg(PREC_E_AT_PEAK),avg(BREAK_LOAD),avg(E_BREAK_LOAD),avg(PREC_E_AT_BREAK),avg(COMPRESSIVE_STRENGTH),avg(TEAR_STRENGTH),avg(FLEXURAL_STRENGTH),avg(SPAN),avg(ULT_SHEAR_STRENGTH_KG_CM),avg(ULT_SHEAR_STRAIN_KG_CM),avg(SHEAR_STRAIN_COLUMN_VALUE_KG_CM),avg(SHEAR_MOD_COLUMN_VALUE_KG_CM), avg(def_yeild_strg) FROM REPORT_MST_II WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")               
                            cursor.execute("INSERT INTO REPORT_II_AGGR(TYPE_STR,REPORT_ID,THICKNESS,WIDTH,CS_AREA,DIAMETER,INN_DIAMETER,OUT_DIAMTER,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN,ULT_SHEAR_STRENGTH_KG_CM,ULT_SHEAR_STRAIN_KG_CM,SHEAR_STRAIN_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_VALUE_KG_CM,def_yeild_strg) SELECT 'MAX',REPORT_ID, max(THICKNESS),max(WIDTH),max(CS_AREA),max(DIAMETER),max(INN_DIAMETER),max(OUT_DIAMTER),max(PEAK_LOAD),max(E_PAEK_LOAD),max(PREC_E_AT_PEAK),max(BREAK_LOAD),max(E_BREAK_LOAD),max(PREC_E_AT_BREAK),max(COMPRESSIVE_STRENGTH),max(TEAR_STRENGTH),max(FLEXURAL_STRENGTH),max(SPAN),max(ULT_SHEAR_STRENGTH_KG_CM),max(ULT_SHEAR_STRAIN_KG_CM),max(SHEAR_STRAIN_COLUMN_VALUE_KG_CM),max(SHEAR_MOD_COLUMN_VALUE_KG_CM), max(def_yeild_strg) FROM REPORT_MST_II WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                
                            cursor.execute("INSERT INTO REPORT_II_AGGR(TYPE_STR,REPORT_ID,THICKNESS,WIDTH,CS_AREA,DIAMETER,INN_DIAMETER,OUT_DIAMTER,PEAK_LOAD,E_PAEK_LOAD,PREC_E_AT_PEAK,BREAK_LOAD,E_BREAK_LOAD,PREC_E_AT_BREAK,COMPRESSIVE_STRENGTH,TEAR_STRENGTH,FLEXURAL_STRENGTH,SPAN,ULT_SHEAR_STRENGTH_KG_CM,ULT_SHEAR_STRAIN_KG_CM,SHEAR_STRAIN_COLUMN_VALUE_KG_CM,SHEAR_MOD_COLUMN_VALUE_KG_CM,def_yeild_strg) SELECT 'MIN',REPORT_ID, min(THICKNESS),min(WIDTH),min(CS_AREA),min(DIAMETER),min(INN_DIAMETER),min(OUT_DIAMTER),min(PEAK_LOAD),min(E_PAEK_LOAD),min(PREC_E_AT_PEAK),min(BREAK_LOAD),min(E_BREAK_LOAD),min(PREC_E_AT_BREAK),min(COMPRESSIVE_STRENGTH),min(TEAR_STRENGTH),min(FLEXURAL_STRENGTH),min(SPAN),min(ULT_SHEAR_STRENGTH_KG_CM),min(ULT_SHEAR_STRAIN_KG_CM),min(SHEAR_STRAIN_COLUMN_VALUE_KG_CM),min(SHEAR_MOD_COLUMN_VALUE_KG_CM), min(def_yeild_strg) FROM REPORT_MST_II WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
                            cursor.execute("INSERT INTO REPORT_III_AGGR(TYPE_STR,REPORT_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,PECENTG_MODULUS,MOD_AT_ANY) SELECT 'AVG',REPORT_ID,avg(TENSILE_STRENGTH),avg(MODULUS_100),avg(MODULUS_200),avg(MODULUS_300),avg(MODULUS_400),avg(PECENTG_MODULUS),avg(MOD_AT_ANY) FROM REPORT_MST_III WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
                            cursor.execute("INSERT INTO REPORT_III_AGGR(TYPE_STR,REPORT_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,PECENTG_MODULUS,MOD_AT_ANY) SELECT 'MAX',REPORT_ID,max(TENSILE_STRENGTH),max(MODULUS_100),max(MODULUS_200),max(MODULUS_300),max(MODULUS_400),max(PECENTG_MODULUS),max(MOD_AT_ANY) FROM REPORT_MST_III WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
                            cursor.execute("INSERT INTO REPORT_III_AGGR(TYPE_STR,REPORT_ID,TENSILE_STRENGTH,MODULUS_100,MODULUS_200,MODULUS_300,MODULUS_400,PECENTG_MODULUS,MOD_AT_ANY) SELECT 'MIN',REPORT_ID,min(TENSILE_STRENGTH),min(MODULUS_100),min(MODULUS_200),min(MODULUS_300),min(MODULUS_400),min(PECENTG_MODULUS),min(MOD_AT_ANY) FROM REPORT_MST_III WHERE REPORT_ID in (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                
                            
                            cursor.execute("UPDATE REPORT_MST SET STATUS='REPORT_LOADED_SUCCESS' WHERE TEST_ID='"+str(self.test_id)+"' and STATUS='PENDING_GRAPH'")
                            #print("ok5")
                                     
                    connection.commit();
                    connection.close()
                    self.sc =PlotCanvas(self,width=8, height=5,dpi=90) 
                    connection = sqlite3.connect("tyr.db")  
                    results=connection.execute("SELECT TEST_TYPE,DEF_FLG FROM TEST_MST WHERE TEST_ID  = '"+str(self.test_id)+"'")
                    for x in results:
                        self.test_id_type=str(x[0])
                        self.def_flg=str(x[1])
                    connection.close()
                    
                    if(self.email_flg=="Y"):                        
                        
                        if(str(self.test_id_type)=="Compress"):
                               self.create_pdf_compress()
                        elif(str(self.test_id_type)=="Tear"):           
                               self.create_pdf_tear()
                        elif(str(self.test_id_type)=="Flexural"):    
                               self.create_pdf_flexural()
                        elif(str(self.test_id_type)=="QLSS"):    
                               self.create_pdf_qlss()
                        elif(str(self.test_id_type)=="ILSS"):    
                               self.create_pdf_ilss()
                        else:
                               if(self.def_flg=="Y"):
                                   self.guage_create_pdf_new()
                               else:
                                   self.create_pdf_new()
        
    '''    
    def create_email_pdfs_files(self):
        self.del_uncheked()
        self.load_reports()
    '''    
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
            
    def print_file(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.window = QtWidgets.QMainWindow()
        self.ui=SR_P_POPUi_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()       
             
            
    def open_pdf(self):        
        self.create_report_pdf()
        os.system("xpdf ./reports/sr_report.pdf")
        
    #def create_multiple_reports(self):    
        
        
    
    def create_report_pdf(self):
        self.del_uncheked()
        self.load_reports()
        self.specimen_shape=""
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        test_type=""
        test_count=0
        #styles.add(ParagraphStyle(name="x", fontSize=12, leading = 7, alignment=TA_LEFT))
        #styles.add(ParagraphStyle(name="x2", fontSize=10, leading = 7, alignment=TA_LEFT))
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select COMPANY_NAME,ADDRESS1 from SETTING_MST ") 
        for x in results:            
            Title = Paragraph(str(x[0]), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SHAPE FROM SPECIMEN_MST  WHERE SPECIMEN_NAME ='"+str(self.specimen_name)+"' LIMIT 1") 
        for x in results:
            self.specimen_shape=str(x[0])         
        connection.close()
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TEST_TYPE FROM TEST_IDS LIMIT 1 ")        
        for x in results:
                test_type=str(x[0])                
        connection.close()
        
        summary_data=[["From Date:",str(self.from_dt),"To Date: ",str(self.to_dt) , "Party Name: ",str(self.party_name), "Report Date: ",str(datetime.datetime.now().strftime("%d %b %Y %H:%M"))]]
        summary_data.append(["Specimen Name: ",str(self.specimen_name),"Unit-Type: ",str(self.unit_type) , " Shape : ",str(self.specimen_shape)," Test Type :",str(test_type)])
        
        
        
        
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),('FONTNAME', (4, 0), (4, -1), 'Helvetica-Bold'),('FONTNAME', (6, 0), (6, -1), 'Helvetica-Bold')]))       
        
        Elements = [Title,Spacer(1,12),Title2,Spacer(1,12),f3,Spacer(1,12),Spacer(1,12)]
        
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT count(TEST_ID) FROM TEST_IDS ")        
        for x in results:
                test_count=str(x[0])                
        connection.close()
        
        childs_data=[]
        childs_data=[['Test ID.','Cycle Id', ' Thickness ','Width' ,' cs. Area']]
        if(int(test_count) > 0):
            if(test_type == "Tensile"):
                
                
                if (self.specimen_shape=="Rectangle"):
                    childs_data=[]
                    if(self.unit_type=="Lb/Inch"):
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)',' Thick-\n ness \n (Inch) ', ' Width \n (Inch) ', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak','E@Break \n (Inch)','% E@Break','Tensile Strength \n (Lb/Inch2)','Mod@100% \n (Lb/Inch2)','Mod@200% \n (Lb/Inch2)','Mod@300% \n (Lb/Inch2)'])        
                    elif(self.unit_type == "Newton/Mm"):
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)',' Thick-\n ness  \n (mm) ', ' Width \n (mm) ', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (N/Mm2)','Mod@100% \n (N/Mm2)','Mod@200% \n (N/Mm2)','Mod@300% \n (N/Mm2)'])
                    elif(self.unit_type == "MPA"):
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)',' Thick-\n ness  \n (mm) ', ' Width \n (mm) ', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (MPA)','Mod@100% \n (MPA)','Mod@200% \n (MPA)','Mod@300% \n (MPA)'])
                    else:    
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)',' Thick-\n ness  \n (cm) ', ' Width \n (cm) ', 'CS.Area \n (cm2)','Force at Peak \n (Kgf)' ,'E@Peak \n (cm)','% E@Peak','E@Break \n (cm)','% E@Break','Tensile Strength \n (Kgf/Cm2)','Mod@100% \n (Kgf/Cm2)','Mod@200% \n (Kgf/Cm2)','Mod@300% \n (Kgf/Cm2)'])        
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT (SELECT X.TEST_ID FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as TEST_ID,((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,(SELECT X.GUAGE100 FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as GUAGE,printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD) ,printf(\"%.2f\", PREC_E_AT_BREAK) ,printf(\"%.2f\", TENSILE_STRENGTH) ,printf(\"%.2f\", MODULUS_100) ,printf(\"%.2f\", MODULUS_200),printf(\"%.2f\", MODULUS_300) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID,round(TENSILE_STRENGTH,2),round(MODULUS_100,2),round(MODULUS_200,2),round(MODULUS_300,2) FROM REPORT_PART_2 group by REPORT_ID ) B WHERE A.REPORT_ID=B.REPORT_ID ")       
                    for k in results:
                        childs_data.append(k)
                    connection.close()
                elif(self.specimen_shape=="Cylindrical"):
                    childs_data=[]
                    if(self.unit_type=="Lb/Inch"):
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)','Diameter \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak','E@Break \n (Inch)','% E@Break','Tensile Strength \n (Lb/Inch2)','Mod@100% \n (Lb/Inch2)','Mod@200% \n (Lb/Inch2)','Mod@300% \n (Lb/Inch2)'])
                    elif(self.unit_type == "Newton/Mm"):
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)', 'Diameter \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (N/Mm2)','Mod@100% \n (N/Mm2)','Mod@200% \n (N/Mm2)','Mod@300% \n (N/Mm2)'])
                    elif(self.unit_type == "MPA"):
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)', 'Diameter \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (MPA)','Mod@100% \n (MPA)','Mod@200% \n (MPA)','Mod@300% \n (MPA)'])
                    else: 
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)', 'Diameter \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (Kg)' ,'E@Peak \n (cm)','% E@Peak','E@Break \n (cm)','% E@Break','Tensile Strength \n (Kg/Cm2)','Mod@100% \n (Kg/Cm2)','Mod@200% \n (Kg/Cm2)','Mod@300% \n (Kg/Cm2)'])
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT (SELECT X.TEST_ID FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as TEST_ID,((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,(SELECT X.GUAGE100 FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as GUAGE,printf(\"%.2f\", A.DIAMETER),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", BREAK_LOAD),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", TENSILE_STRENGTH),printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200),printf(\"%.2f\", MODULUS_300) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_PART_2 group by REPORT_ID ) B WHERE A.REPORT_ID=B.REPORT_ID ")
                    for k in results:
                        childs_data.append(k)
                    connection.close()
                elif(self.specimen_shape=="Pipe"):
                    childs_data=[]
                    if(self.unit_type=="Lb/Inch"):
                           childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)', 'Inn.Diameter \n (Inch)', 'Out. Diameter \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak','E@Break \n (Inch)','% E@Break','Tensile Strength \n (Lb/Inch2)','Mod@100% \n (Lb/Inch2)','Mod@200% \n (Lb/Inch2)','Mod@300% \n (Lb/Inch2)'])
                    elif(self.unit_type == "Newton/Mm"):
                           childs_data.append(['Test. \n Id.','Spec.\n No.','Guage \n Length \n (mm)','Inn.Diameter \n (Inch)', 'Out. Diameter \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (N)' ,'E@Peak \n (Inch)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (N/Mm2)','Mod@100% \n (N/Mm2)','Mod@200% \n (N/Mm2)','Mod@300% \n (N/Mm2)']) 
                    elif(self.unit_type == "MPA"):
                           childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)', 'Inn.Diameter \n (mm)', 'Out. Diameter \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (MPA)','Mod@100% \n (MPA)','Mod@200% \n (MPA)','Mod@300% \n (MPA)']) 
                    else:
                           childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)', 'Inn.Diameter \n (cm)', 'Out. Diameter \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (Kgf)' ,'E@Peak \n (cm)','% E@Peak','E@Break \n (cm)','% E@Break','Tensile Strength \n (Kgf/Cm2)','Mod@100% \n (Kgf/Cm2)','Mod@200% \n (Kgf/Cm2)','Mod@300% \n (Kgf/Cm2)'])
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT (SELECT X.TEST_ID FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as TEST_ID,((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,(SELECT X.GUAGE100 FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as GUAGE,printf(\"%.2f\", A.INN_DIAMETER),printf(\"%.2f\", A.OUT_DIAMTER),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", TENSILE_STRENGTH),printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200),printf(\"%.2f\", MODULUS_300) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_PART_2 group by REPORT_ID ) B WHERE A.REPORT_ID=B.REPORT_ID ")       
        
                    for k in results:
                        childs_data.append(k)
                    connection.close()       
                    
                elif(self.specimen_shape=="DirectValue"):
                    childs_data=[]
                    if(self.unit_type=="Lb/Inch"):                
                            childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)','CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak','E@Break \n (Inch)','% E@Break','Tensile Strength \n (Lb/Inch2)','Mod@100% \n (Lb/Inch2)','Mod@200% \n (Lb/Inch2)','Mod@300% \n (Lb/Inch2)'])           
                    elif(self.unit_type == "Newton/Mm"):
                            childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)','CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (N/Mm2)','Mod@100% \n (N/Mm2)','Mod@200% \n (N/Mm2)','Mod@300% \n (N/Mm2)'])
                    elif(self.unit_type == "MPA"):
                            childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)','CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak','E@Break \n (mm)','% E@Break','Tensile Strength \n (MPA)','Mod@100% \n (MPA)','Mod@200% \n (MPA)','Mod@300% \n (MPA)'])
                    else:   
                            childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)','CS.Area \n (cm2)','Force at Peak \n (Kg)' ,'E@Peak \n (cm)','% E@Peak','E@Break \n (cm)','% E@Break','Tensile Strength \n (Kg/Cm2)','Mod@100% \n (Kg/Cm2)','Mod@200% \n (Kg/Cm2)','Mod@300% \n (Kg/Cm2)'])           
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT (SELECT X.TEST_ID FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as TEST_ID,((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,(SELECT X.GUAGE100 FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as GUAGE,printf(\"%.2f\", A.INN_DIAMETER),printf(\"%.2f\", A.OUT_DIAMTER),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", TENSILE_STRENGTH),printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200),printf(\"%.2f\", MODULUS_300) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_PART_2 group by REPORT_ID ) B WHERE A.REPORT_ID=B.REPORT_ID")       
                    for k in results:
                        childs_data.append(k)
                    connection.close() 
                    
                else:
                    print("Invalid Specimen Shape")
                    
                    
                    
                    
            elif(test_type == "Compress"):
                childs_data=[]
                if(self.unit_type == "Kg/Cm"):
                        childs_data.append(['Test.Id.','Spec.No.','Guage \n Length \n (mm)','CS Area \n (cm2)', 'Force at Peak\n (Kgf)', 'Compression \n (cm)', 'Compressive Strength \n (Kgf/Cm2)','% Compression \n'])
                elif(self.unit_type == "Lb/Inch"):
                        childs_data.append(['Test.Id.','Spec.No.','Guage \n Length \n (mm)','CS Area \n (Inch2)', 'Force at Peak\n (Lb)', 'Compression \n (Inch)', 'Compressive Strength \n (Lb/Inch2)','% Compression \n'])           
                elif(self.unit_type == "Newton/Mm"):
                        childs_data.append(['Test.Id.','Spec.No.','Guage \n Length \n (mm)','CS Area \n (mm2)', 'Force at Peak\n (N)', 'Compression \n (mm)', 'Compressive Strength \n (N/mm2)','% Compression \n'])            
                elif(self.unit_type == "MPA"):
                        childs_data.append(['Test.Id.','Spec.No.','Guage \n Length \n (mm)','CS Area \n (mm2)', 'Force at Peak\n (N)', 'Compression \n (mm)', 'Compressive Strength \n (MPA)','% Compression \n'])           
                else:
                        childs_data.append(['Test.Id.','Spec.No.','Guage \n Length \n (mm)','CS Area \n (mm2)', 'Force at Peak\n (MPA)', 'Compression \n (mm)', 'Compressive Strength \n (MPA)','% Compression \n'])
          
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT (SELECT X.TEST_ID FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as TEST_ID,((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,(SELECT X.GUAGE100 FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as GUAGE,printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", A.COMPRESSIVE_STRENGTH),printf(\"%.2f\", A.PREC_E_AT_BREAK) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II group by REPORT_ID ) B WHERE A.REPORT_ID=B.REPORT_ID") 
                for k in results:
                        childs_data.append(k)
                connection.close()        
            elif(test_type == "Tear"):
                childs_data=[]
                if(self.unit_type == "Kg/Cm"):
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)','Thickness \n (cm)', 'Force at Peak\n (Kgf)', 'Tear Strength \n (Kgf/Cm)'])
                elif(self.unit_type == "Lb/Inch"):
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)','Thickness \n (Inch)', 'Force at Peak\n (Lb)', 'Tear Strength \n (Lb/Inch)'])           
                elif(self.unit_type == "Newton/Mm"):
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)','Thickness\n (mm)', 'Force at Peak\n (N)', 'Tear Strength \n (N/mm)'])            
                elif(self.unit_type == "MPA"):
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)','Thickness\n (mm)', 'Force at Peak\n (N)', 'Tear Strength \n (MPA)'])           
                else:
                        childs_data.append(['Test.\n Id.','Spec.\n No.','Guage \n Length \n (mm)','Thickness \n (mm)', 'Force at Peak\n (MPA)', 'Tear Strength \n (MPA)'])
          
                connection = sqlite3.connect("tyr.db")               
                results=connection.execute("SELECT (SELECT X.TEST_ID FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as TEST_ID,((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,(SELECT X.GUAGE100 FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as GUAGE,printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.TEAR_STRENGTH)  FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II group by REPORT_ID ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        
                for k in results:
                        childs_data.append(k)
                connection.close()  
            
            elif(test_type == "Flexural"):
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT IFNULL(GUAGE_MM,0) FROM REPORT_MST WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                        
                for x in results:
                        self.length=str(x[0])
                connection.close()    
                childs_data=[]
                if(self.unit_type == "Kg/Cm"):
                    self.length=float(int(self.length)*0.1)
                    childs_data.append(['Test.Id.','Spec.No.','Length  \n (cm)','Thickness  \n (cm)','Width  \n (cm)','Support \n Span  \n (cm)', 'Max. \n Displ. \n (cm)', 'Force \n at Peak \n (Kgf)', 'Flexural \n Strength \n (Kgf/cm2) ','Failure \n Mode','Test \n Method'])
                elif(self.unit_type == "Lb/Inch"):
                    self.length=float(int(self.length)*0.0393701)
                    childs_data.append(['Test.Id.','Spec.No.','Length  \n (Inch)','Thickness  \n (Inch)','Width  \n (Inch)','Support \n Span  \n (Inch)', 'Max. \n Displ. \n (Inch)', 'Force \n  at Peak\n (Lb)', 'Flexural \n  Strength \n (Lb/Inch2)  ','Failure \n Mode','Test \n Method'])           
                elif(self.unit_type == "Newton/Mm"):
                    childs_data.append(['Test.Id.','Spec.No.','Length  \n (mm)','Thickness  \n (mm)','Width  \n (mm)','Support \n Span  \n (mm)', 'Max. \n Displ. \n (mm)', 'Force \n  at Peak\n (N)', 'Flexural \n  Strength \n (N/mm2)','Failure \n Mode','Test \n Method'])            
                elif(self.unit_type == "MPA"):
                    childs_data.append(['Test.Id.','Spec.No.','Length  \n (mm)','Thickness  \n (mm)','Width  \n (mm)','Support \n Span  \n (mm)', 'Max. \n Displ. \n (mm)', 'Force \n  at Peak\n (N)', 'Flexural \n  Strength \n (MPA)','Failure \n Mode','Test \n Method'])           
                else:
                    childs_data.append(['Test.Id.','Spec.No.','Length  \n (mm)', 'Thickness  \n (mm)','Width  \n (mm)','Support \n Span  \n (mm)','Max. \n Displ. \n (mm)', 'Force \n  at Peak\n (Kgf)', 'Flexural\n   Strength \n (MPA)','Failure \n Mode','Test \n Method'])
          
                connection = sqlite3.connect("tyr.db")
                #print("SELECT (SELECT X.TEST_ID FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as TEST_ID,(A.REC_ID-B.MIN_REC_ID)+1 as SPECIMEN_NO,"+str(self.length)+",printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.2f\", A.SPAN),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.FLEXURAL_STRENGTH),A.BREAK_MODE,A.TEST_METHOD FROM REPORT_MST_II A ,(SELECT MIN(REC_ID) AS MIN_REC_ID,REPORT_ID FROM REPORT_MST_II group by REPORT_ID) B WHERE B.REPORT_ID =A.REPORT_ID  ") 
                
                
                results=connection.execute("SELECT (SELECT X.TEST_ID FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as TEST_ID,(A.REC_ID-B.MIN_REC_ID)+1 as SPECIMEN_NO,"+str(self.length)+",printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.2f\", A.SPAN),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.FLEXURAL_STRENGTH),A.BREAK_MODE,A.TEST_METHOD FROM REPORT_MST_II A ,(SELECT MIN(REC_ID) AS MIN_REC_ID,REPORT_ID FROM REPORT_MST_II group by REPORT_ID) B WHERE B.REPORT_ID =A.REPORT_ID  ") 
                
                for k in results:
                        childs_data.append(k)
                connection.close() 
            
            elif(test_type == "QLSS"):
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT MOD_AT_ANY FROM REPORT_MST WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                        
                for x in results:            
                    self.shear_mod_ip=str(x[0]) 
                connection.close()    
         
                if(self.shear_mod_ip == ""):
                       self.shear_mod_ip=100
                else:
                       pass
                childs_data=[]
                if(self.unit_type == "Kg/Cm"):
                        childs_data.append(['Test.Id.','Spec.No.','Guage \n Length \n (mm)','Width \n (Cm)','Thickness \n (Cm)','CS Area \n (Cm2)','Max. Force \n (Kgf)',' Max. \n Disp.(Cm) ','Ult. Shear\n Strength \n (Kgf/Cm2)','Ult. Shear \n Strain %','Shear Strain \n @ Ult. Shear Stress','Shear Modulus \n @ Ult. Shear Stress \n (Kg/Cm2)','Shear Modulus \n @ '+str(self.shear_mod_ip)+'\n (Kg/Cm2) Shear Stress'])        
                elif(self.unit_type == "Lb/Inch"):
                        childs_data.append(['Test.Id.','Spec.No.','Guage \n Length \n (mm)','Width \n (Inch)','Thickness \n (Inch)','CS Area \n (Inch2)','Max. Force \n (Lb)',' Max. \n Disp.(Inch) ','Ult. Shear\n Strength \n (Lb\Inch2)','Ult. Shear \n Strain %','Shear Strain \n @ Ult. Shear Stress','Shear Modulus \n @ Ult. Shear Stress \n (Lb/Inch2)','Shear Modulus \n @ '+str(self.shear_mod_ip)+'\n (Lb/Inch2) Shear Stress'])        
                elif(self.unit_type == "Newton/Mm"):
                        childs_data.append(['Test.Id.','Spec.No.','Guage \n Length \n (mm)','Width \n (Mm)','Thickness \n (Mm)','CS Area \n (Mm2)','Max. Force \n (N)',' Max. \n Disp.(Mm) ','Ult. Shear\n Strength \n (N/Mm2)','Ult. Shear \n Strain %','Shear Strain \n @ Ult. Shear Stress','Shear Modulus \n @ Ult. Shear Stress \n (N/Mm2)','Shear Modulus \n @ '+str(self.shear_mod_ip)+' \n (N/Mm2) Shear Stress'])        
                elif(self.unit_type == "MPA"):
                        childs_data.append(['Test.Id.','Spec.No.','Guage \n Length \n (mm)','Width \n (Mm)','Thickness \n (Mm)','CS Area \n (Mm2)','Max. Force \n (N)',' Max. \n Disp.(Mm) ','Ult. Shear\n Strength \n (MPA)','Ult. Shear \n Strain %','Shear Strain \n @ Ult. Shear Stress','Shear Modulus \n @ Ult. Shear Stress','Shear Modulus \n @ '+str(self.shear_mod_ip)+' Shear Stress'])        
                else:
                        childs_data.append(['Test.Id.','Spec.No.','Guage \n Length \n (mm)','Width \n (Mm)','Thickness \n (Mm)','CS Area \n (Mm2)','Max. Force \n (Kgf)',' Max. \n Disp.(Mm) ','Ult. Shear\n Strength','Ult. Shear \n Strain %','Shear Strain \n @ Ult. Shear Stress','Shear Modulus \n @ Ult. Shear Stress','Shear Modulus \n @ '+str(self.shear_mod_ip)+' Shear Stress'])        
        
                connection = sqlite3.connect("tyr.db")               
                results=connection.execute("SELECT (SELECT X.TEST_ID FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as TEST_ID,((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,(SELECT X.GUAGE100 FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as GUAGE,printf(\"%.2f\", A.WIDTH),printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.ULT_SHEAR_STRENGTH_KG_CM),printf(\"%.2f\", A.ULT_SHEAR_STRAIN_KG_CM),printf(\"%.2f\", A.SHEAR_STRAIN_COLUMN_VALUE_KG_CM)||'@ '||printf(\"%.2f\", A.SHEAR_MOD_COLUMN_NAME_KG_CM),printf(\"%.2f\", A.SHEAR_MOD_COLUMN_VALUE_KG_CM)||'@ '||printf(\"%.2f\", A.SHEAR_MOD_COLUMN_NAME_KG_CM),printf(\"%.2f\",(("+str(self.shear_mod_ip)+")/(A.SHEAR_STRAIN_COLUMN_VALUE_KG_CM))) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II group by REPORT_ID ) B WHERE A.REPORT_ID=B.REPORT_ID") 
                
                for k in results:
                        childs_data.append(k)
                connection.close()                 
            
            elif(test_type == "ILSS"):
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT MOD_AT_ANY,IFNULL(GUAGE_MM,0) FROM REPORT_MST WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                        
                for x in results:            
                        self.shear_mod_ip=str(x[0])
                        self.length=str(x[1])
                connection.close()    
         
                if(self.shear_mod_ip == ""):
                        self.shear_mod_ip=100
                else:
                    pass
                childs_data=[]
                if(self.unit_type == "Kg/Cm"):
                        self.length=float(int(self.length)*0.1)
                        childs_data.append(['Test.Id.','Spec.No.','Length \n (Cm)','Width \n (Cm)','Thickness \n (Cm)','Max. Force \n (Kgf)',' Max. \n Disp.(Cm) ',' Shear\n Strength \n (Kgf/Cm2)','Support \n SPAN (Cm)',' Failure \n Mode','Test \n Method'])        
                elif(self.unit_type == "Lb/Inch"):
                        self.length=float(int(self.length)*0.0393701)
                        childs_data.append(['Test.Id.','Spec.No.','Length \n (Inch)','Width \n (Inch)','Thickness \n (Inch)','Max. Force \n (Lb)',' Max. \n Disp.(Inch) ',' Shear\n Strength \n (Lb\Inch2)','Support \n SPAN (Inch)',' Failure \n Mode','Test \n Method'])        
                elif(self.unit_type == "Newton/Mm"):
                        childs_data.append(['Test.Id.','Spec.No.','Length \n (Mm)','Width \n (Mm)','Thickness \n (Mm)','Max. Force \n (N)',' Max. \n Disp.(Mm) ',' Shear\n Strength \n (N/Mm2)','Support \n SPAN (Mm)',' Failure \n Mode','Test \n Method'])        
                elif(self.unit_type == "MPA"):
                        childs_data.append(['Test.Id.','Spec.No.','Length \n (Mm)','Width \n (Mm)','Thickness \n (Mm)','Max. Force \n (N)',' Max. \n Disp.(Mm) ',' Shear\n Strength \n (MPA)','Support \n SPAN (Mm)',' Failure \n Mode','Test \n Method'])        
                else:
                        childs_data.append(['Test.Id.','Spec.No.','Length \n (Mm)','Width \n (Mm)','Thickness \n (Mm)','Max. Force \n (Kgf)',' Max. \n Disp.(Mm) ',' Shear\n Strength','Support \n SPAN (Mm)',' Failure \n Mode','Test \n Method'])        
                
                connection = sqlite3.connect("tyr.db")               
                results=connection.execute("SELECT (SELECT X.TEST_ID FROM CYCLES_MST X WHERE X.CYCLE_ID=A.CYCLE_ID) as TEST_ID,((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,"+str(self.length)+",printf(\"%.2f\", A.WIDTH),printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.ULT_SHEAR_STRENGTH_KG_CM),printf(\"%.2f\", A.SPAN),A.BREAK_MODE,A.TEST_METHOD FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II group by REPORT_ID ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        
                for k in results:
                        childs_data.append(k)
                connection.close()  
            
            else:
                self.label_21.show()
                self.label_21.setText("Invalid Test")
        else:
            pass
                
        
        #f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10)]))       
        
        
        f=Table(childs_data)
        f.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        Elements.append(f)
        
        doc = SimpleDocTemplate('./reports/sr_report.pdf',pagesize=A4)
        doc.pagesize = landscape(A4)
        doc.build(Elements)
        print("Done")
        self.filter_col_name=""
        
 
    def create_pdf_ilss(self):
        self.length=0
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
        for x in results:
            self.graph_typex=x[0]
            self.unit_typex=x[1]
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT MOD_AT_ANY FROM REPORT_MST WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                        
        for x in results:            
                self.shear_mod_ip=str(x[0]) 
        connection.close()
        
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime'),A.TEMPERATURE  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Specmen Shape:",str(x[9])],["Test Type:",str(x[3]),"Specmen Specs:",str(x[0])],["Party Name :",str(x[7]),"Motor Speed :",str(x[5])],["Guage Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", "Stech engineers testing machine","Temp.(C)",str(x[12])]]
            self.length=str(x[6])
        
        connection.close()
         
        if(self.shear_mod_ip == ""):
            self.shear_mod_ip=100
        else:
            pass
        
        if(self.unit_typex == "Kg/Cm"):
            self.length=float(int(self.length)*0.1)
            #data2= [ ['Spec. \n No', 'Thickness  \n (cm)','Width  \n (cm)','Span  \n (cm)','Length at Peak \n (cm)', 'Force at Peak\n (Kgf)', 'Flexural Strength \n (Kgf/cm2)']]
            data2= [['Spec. \n No','Length \n (Cm)','Width \n (Cm)','Thickness \n (Cm)','Max. Force \n (Kgf)',' Max. \n Disp. \n (Cm) ','Shear\n Strength \n (Kg/Cm2)','Support \n SPAN \n (Cm)','Failure \n Mode','Test \n Method.']]        
            #data3= [['Spec. \n No','Shear Modulus \n@ Utl. \n Shear Stress \n (Kg/Cm2)','Shear Modulus \n@ '+str(self.shear_mod_ip)+' \n (Kg/Cm2) Shear Stress']]
              
        elif(self.unit_typex == "Lb/Inch"):
            self.length=float(int(self.length)*0.0393701)
            data2= [ ['Spec. \n No','Length \n (Inch)','Width \n (Inch)','Thickness \n (Inch)','Max. Force \n (Lb)',' Max. \n Disp.  \n (Inch) ',' Shear\n Strength \n (Lb/Inch2)','Support \n SPAN \n (Inch)','Failure \n Mode','Test \n Method.']]        
            #data3= [['Spec. \n No','Shear Modulus \n@ Utl. \n Shear Stress \n (Lb/Inch2)','Shear Modulus \n@ '+str(self.shear_mod_ip)+' \n (Lb/Inch2) Shear Stress']]
            #data2= [ ['Spec. \n No', 'Thickness  \n (Inch)','Width  \n (Inch)','Span  \n (Inch)','Length at Peak \n (Inch)', 'Force at Peak\n (Lb)', 'Flexural Strength \n (Lb/Inch2)']]           
        elif(self.unit_typex == "Newton/Mm"):
            data2= [ ['Spec. \n No','Length \n (Mm)','Width \n (Mm)','Thickness \n (Mm)','Max. Force \n (N)',' Max. \n Disp.  \n (Mm) ',' Shear\n Strength \n (N/Mm2)','Support \n SPAN \n (Mm)','Failure \n Mode','Test \n Method.']]        
            #data3= [['Spec. \n No','Shear Modulus \n@ Utl. \n Shear Stress \n (Newton/Mm2)','Shear Modulus \n@ '+str(self.shear_mod_ip)+' \n (Newton/Mm2) Shear Stress']] 
            #data2= [ ['Spec. \n No', 'Thickness  \n (mm)','Width  \n (mm)','Span  \n (mm)','Length at Peak \n (mm)', 'Force at Peak\n (N)', 'Flexural Strength \n (N/mm2)']]            
        elif(self.unit_typex == "MPA"):
            data2= [ ['Spec. \n No','Length \n (Mm)','Width \n (Mm)','Thickness \n (Mm)','Max. Force \n (N)',' Max. \n Disp.  \n (Mm) ',' Shear\n Strength \n (MPA)','Support \n SPAN \n (Mm)','Failure \n Mode','Test \n Method.']]        
            #data3= [['Spec. \n No','Shear Modulus \n@ Utl. \n Shear Stress \n (MPA)','Shear Modulus \n@ '+str(self.shear_mod_ip)+'\n (MPA) Shear Stress']]
            #data2= [ ['Spec. \n No', 'Thickness  \n (mm)','Width  \n (mm)','Span  \n (mm)','Length at Peak \n (mm)', 'Force at Peak\n (Kg)', 'Flexural Strength \n (MPA)']]           
        else:
            data2= [['Spec. \n No','Length \n (Mm)','Width \n (Mm)','Thickness \n (Mm)','Max. Force \n (Kgf)',' Max. \n Disp.  \n (Mm) ',' Shear\n Strength \n (Kg/Cm2)','Support \n SPAN \n (Mm)','Failure \n Mode','Test \n Method.']]        
            #data3= [['Shear Modulus \n@ Utl. \n Shear Stress \n (Kg/Cm2)','Shear Modulus \n@ '+str(self.shear_mod_ip)+' \n (Kg/Cm2) Shear Stress']]
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,"+str(self.length)+",printf(\"%.2f\", A.WIDTH),printf(\"%.4f\", A.THICKNESS),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.4f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.ULT_SHEAR_STRENGTH_KG_CM),printf(\"%.2f\", A.SPAN),A.BREAK_MODE,A.TEST_METHOD  FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        for x in results:
                data2.append(x)
        connection.close()
        
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TYPE_STR,"+str(self.length)+",printf(\"%.2f\", WIDTH),printf(\"%.2f\", THICKNESS),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", ULT_SHEAR_STRENGTH_KG_CM),printf(\"%.2f\", SPAN),BREAK_MODE,TEMPERATURE  FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        
        
        
        
        y=300
        Elements=[]
        
        
         
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
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
          
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/emailed/multiple/Report'+str(self.test_id).zfill(4)+'.pdf', rightMargin=10,
                                leftMargin=30,
                                topMargin=20,
                                bottomMargin=20,)
        doc.build(Elements)
        #print("Done"
        
    def create_pdf_qlss(self):        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
        for x in results:
            self.graph_typex=x[0]
            self.unit_typex=x[1]
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT MOD_AT_ANY FROM REPORT_MST WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")                        
        for x in results:            
                self.shear_mod_ip=str(x[0]) 
        connection.close()    
         
        if(self.shear_mod_ip == ""):
            self.shear_mod_ip=100
        else:
            pass
        
        if(self.unit_typex == "Kg/Cm"):
            #data2= [ ['Spec. \n No', 'Thickness  \n (cm)','Width  \n (cm)','Span  \n (cm)','Length at Peak \n (cm)', 'Force at Peak\n (Kgf)', 'Flexural Strength \n (Kgf/cm2)']]
            data2= [['Spec. \n No','Width \n (Cm)','Thickness \n (Cm)','CS Area \n (Cm2)','Max. Force \n (Kgf)',' Max. \n Disp. \n (Cm) ','Utl. Shear\n Strength \n (Kg/Cm2)','Ultimate Shear \n Strain %','Shear Strain \n @ Utl. \n Shear Stress']]        
            data3= [['Spec. \n No','Shear Modulus \n@ Utl. \n Shear Stress \n (Kg/Cm2)','Shear Modulus \n@ '+str(self.shear_mod_ip)+' \n (Kg/Cm2) Shear Stress']]
              
        elif(self.unit_typex == "Lb/Inch"):
            data2= [ ['Spec. \n No','Width \n (Inch)','Thickness \n (Inch)','CS Area \n (Inch2)','Max. Force \n (Lb)',' Max. \n Disp.  \n (Inch) ','Utl. Shear\n Strength \n (Lb/Inch2)','Utl. Shear \n Strain %','Shear Strain \n @ Utl. Shear Stress']]        
            data3= [['Spec. \n No','Shear Modulus \n@ Utl. \n Shear Stress \n (Lb/Inch2)','Shear Modulus \n@ '+str(self.shear_mod_ip)+' \n (Lb/Inch2) Shear Stress']]
            #data2= [ ['Spec. \n No', 'Thickness  \n (Inch)','Width  \n (Inch)','Span  \n (Inch)','Length at Peak \n (Inch)', 'Force at Peak\n (Lb)', 'Flexural Strength \n (Lb/Inch2)']]           
        elif(self.unit_typex == "Newton/Mm"):
            data2= [ ['Spec. \n No','Width \n (Mm)','Thickness \n (Mm)','CS Area \n (Mm2)','Max. Force \n (N)',' Max. \n Disp.  \n (Mm) ','Utl. Shear\n Strength \n (N/Mm2)','Utl. Shear \n Strain %','Shear Strain \n @ Utl. \n Shear Stress']]        
            data3= [['Spec. \n No','Shear Modulus \n@ Utl. \n Shear Stress \n (Newton/Mm2)','Shear Modulus \n@ '+str(self.shear_mod_ip)+' \n (Newton/Mm2) Shear Stress']] 
            #data2= [ ['Spec. \n No', 'Thickness  \n (mm)','Width  \n (mm)','Span  \n (mm)','Length at Peak \n (mm)', 'Force at Peak\n (N)', 'Flexural Strength \n (N/mm2)']]            
        elif(self.unit_typex == "MPA"):
            data2= [ ['Spec. \n No','Width \n (Mm)','Thickness \n (Mm)','CS Area \n (Mm2)','Max. Force \n (N)',' Max. \n Disp.  \n (Mm) ','Utl. Shear\n Strength \n (MPA)','Utl. Shear \n Strain %','Shear Strain \n @ Utl. \n Shear Stress']]        
            data3= [['Spec. \n No','Shear Modulus \n@ Utl. \n Shear Stress \n (MPA)','Shear Modulus \n@ '+str(self.shear_mod_ip)+'\n (MPA) Shear Stress']]
            #data2= [ ['Spec. \n No', 'Thickness  \n (mm)','Width  \n (mm)','Span  \n (mm)','Length at Peak \n (mm)', 'Force at Peak\n (Kg)', 'Flexural Strength \n (MPA)']]           
        else:
            data2= [['Spec. \n No','Width \n (Mm)','Thickness \n (Mm)','CS Area \n (Mm2)','Max. Force \n (Kgf)',' Max. \n Disp.  \n (Mm) ','Utl. Shear\n Strength \n (Kg/Cm2)','Utl. Shear \n Strain %','Shear Strain \n @ Utl. \n Shear Stress']]        
            data3= [['Shear Modulus \n@ Utl. \n Shear Stress \n (Kg/Cm2)','Shear Modulus \n@ '+str(self.shear_mod_ip)+' \n (Kg/Cm2) Shear Stress']]
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.WIDTH),printf(\"%.4f\", A.THICKNESS),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.4f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.ULT_SHEAR_STRENGTH_KG_CM),printf(\"%.2f\", A.ULT_SHEAR_STRAIN_KG_CM),printf(\"%.2f\", A.SHEAR_STRAIN_COLUMN_VALUE_KG_CM)||'@ '||printf(\"%.2f\", A.SHEAR_MOD_COLUMN_NAME_KG_CM)  FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        for x in results:
                data2.append(x)
        connection.close()
        
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", WIDTH),printf(\"%.2f\", THICKNESS),printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", ULT_SHEAR_STRENGTH_KG_CM),printf(\"%.2f\", ULT_SHEAR_STRAIN_KG_CM),printf(\"%.2f\", SHEAR_STRAIN_COLUMN_VALUE_KG_CM) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.SHEAR_MOD_COLUMN_VALUE_KG_CM)||'@ '||printf(\"%.2f\", A.SHEAR_MOD_COLUMN_NAME_KG_CM),printf(\"%.2f\",(("+str(self.shear_mod_ip)+")/(A.SHEAR_STRAIN_COLUMN_VALUE_KG_CM)))  FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        for x in results:
                data3.append(x)
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", SHEAR_MOD_COLUMN_VALUE_KG_CM),printf(\"%.2f\",(("+str(self.shear_mod_ip)+")/(SHEAR_STRAIN_COLUMN_VALUE_KG_CM))) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
        for x in results:
                data3.append(x)
        connection.close()
        
        y=300
        Elements=[]
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime')  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Specmen Shape:",str(x[9])],["Test Type:",str(x[3]),"Specmen Specs:",str(x[0])],["Party Name :",str(x[7]),"Motor Speed :",str(x[5])],["Guage Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", "","",""]]
      
        
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
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
        f4=Table(data3)
        f4.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
      
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),f4,Spacer(1,12),comments,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/emailed/multiple/Report'+str(self.test_id).zfill(4)+'.pdf', rightMargin=10,
                                leftMargin=30,
                                topMargin=20,
                                bottomMargin=20,)
        doc.build(Elements)
        #print("Done")
    

    def create_pdf_flexural(self):
        self.length=0
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT STG_GRAPH_TYPE,STG_UNIT_TYPE FROM GLOBAL_REPORTS_PARAM") 
        for x in results:
            self.graph_typex=x[0]
            self.unit_typex=x[1]
        connection.close()
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime'),A.TEMPERATURE  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date: ",str(x[10]),"Test No: ",str(x[0])],["Job Name : ",str(x[1]),"Batch ID: ",str(x[2])],["Specimen Name:  ",str(x[4]),"Specmen Shape:",str(x[9])],["Test Type:",str(x[3]),"Specmen Specs:",str(x[0])],["Party Name :",str(x[7]),"Motor Speed :",str(x[5])],[" Length(mm):",str(x[6]),"Report Date: ",str(x[11])],["Tested By :", "Stech engineers testing machine"," Temp.(C) :",str(x[12])]]
            self.length=str(x[6])        
        connection.close()
        
        if(self.unit_typex == "Kg/Cm"):
            self.length=float(int(self.length)*0.1)
            data2= [ ['Spec. \n No', 'Length \n (cm)','Thickness  \n (cm)','Width  \n (cm)','Support \n Span  \n (cm)','Max.\n Displ. \n (cm)', 'Force  \n @  Peak\n (Kgf)', 'Flexural \n Strength \n (Kgf/cm2)','Flexural \n Modulus \n','Flexural \n Strain \n at Break (%)','Flexural \n Strain \n at Input (%)']]
        elif(self.unit_typex == "Lb/Inch"):
            self.length=float(int(self.length)*0.0393701)
            data2= [ ['Spec. \n No', 'Length \n (Inch)','Thickness  \n (Inch)','Width  \n (Inch)','Support \n Span  \n (Inch)','Max.\n Displacement \n (Inch)', 'Force \n @ Peak\n (Lb)', 'Flexural \n Strength \n (Lb/Inch2)','Flexural \n Modulus \n','Flexural \n Strain \n at Break (%)','Flexural \n Strain \n at Input (%)']]           
        elif(self.unit_typex == "Newton/Mm"):
            data2= [ ['Spec. \n No','Length \n (mm)', 'Thickness  \n (mm)','Width  \n (mm)','Support \n Span  \n (mm)','Max.\n Displ. \n (mm)', 'Force \n @  Peak\n (N)', 'Flexural \n Strength \n (N/mm2)','Flexural \n Modulus \n','Flexural \n Strain \n at Break (%)','Flexural \n Strain \n at Input (%)']]            
        elif(self.unit_typex == "MPA"):
            data2= [ ['Spec. \n No','Length \n (mm)', 'Thickness  \n (mm)','Width  \n (mm)','Support \n Span  \n (mm)','Max.\n Displ. \n (mm)', 'Force \n @  Peak\n (N)', 'Flexural \n Strength \n (MPa)','Flexural \n Modulus \n','Flexural \n Strain \n at Break (%)','Flexural \n Strain \n at Input (%)']]           
        else:
            data2= [ ['Spec. \n No','Length \n (mm)', 'Thickness \n (mm)','Width \n (mm)','Support \n Span  \n (mm)','Max.\n Displ. \n (mm)', 'Force \n @  Peak\n (N)', 'Flexural \n  Strength \n (MPa)','Flexural \n Modulus \n','Flexural \n Strain \n at Break (%)','Flexural \n Strain \n at Input (%)']]
          
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,"+str(self.length)+",printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.2f\", A.SPAN),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.4f\", A.PEAK_LOAD),printf(\"%.2f\", A.FLEXURAL_STRENGTH),printf(\"%.2f\", A.flexural_mod_kg_cm),printf(\"%.2f\", A.per_strain_at_break),printf(\"%.2f\", A.per_strain_at_input) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TYPE_STR,"+str(self.length)+",printf(\"%.2f\", THICKNESS),printf(\"%.2f\", WIDTH),printf(\"%.2f\", SPAN),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%.4f\", PEAK_LOAD),printf(\"%.2f\", FLEXURAL_STRENGTH),printf(\"%.2f\", flexural_mod_kg_cm),printf(\"%.2f\", per_strain_at_break),printf(\"%.2f\", per_strain_at_input) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close() 
        
        
        
        if(self.unit_typex == "Kg/Cm"):
            #self.length=float(int(self.length)*0.1)
            data3= [ ['Spec. \n No', 'Test Speed \n (mm/min)', 'Load Radious \n (cm)','Support Radious \n (cm)','Failure \n Mode','Test \n Method']]
        elif(self.unit_typex == "Lb/Inch"):
            self.length=float(int(self.length)*0.0393701)
            data3= [ ['Spec. \n No', 'Test Speed \n (mm/min)', 'Load Radious \n (Inch)','Support Radious \n (Inch)', 'Failure \n Mode','Test \n Method']]           
        elif(self.unit_typex == "Newton/Mm"):
            data3= [ ['Spec. \n No','Test Speed \n (mm/min)','Load Radious \n (mm)','Support Radious \n (mm)','Failure \n Mode','Test \n Method']]            
        elif(self.unit_typex == "MPA"):
            data3= [ ['Spec. \n No', 'Test Speed \n (mm/min)','Load Radious \n (mm)','Support Radious \n (mm)','Failure \n Mode','Test \n Method']]           
        else:
            data3= [ ['Spec. \n No', 'Test Speed \n (mm/min)','Load Radious \n (mm)','Support Radious \n (mm)','Failure \n Mode','Test \n Method']]
          
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.speed_rpm),printf(\"%.2f\", A.load_radious),printf(\"%.2f\", A.support_radious),A.BREAK_MODE,A.TEST_METHOD FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
        for x in results:
                data3.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", speed_rpm),null,null FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
        for x in results:
                data3.append(x)
        connection.close() 
        
        y=300
        Elements=[]
        
        
        
        
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
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f4=Table(data3)
        f4.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
         
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),f4,Spacer(1,12),comments,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/emailed/multiple/Report'+str(self.test_id).zfill(4)+'.pdf', rightMargin=10,
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
            data2= [ ['Spec. \n No', 'Thickness \n (mm)', 'Force at Peak\n (N)', 'Tear Strength \n (MPA)']]           
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
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime')  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)")
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
        #f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
        
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
         
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,Spacer(1,12),Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f2,Spacer(1,12),Spacer(1,12),Spacer(1,12),comments,blank,blank,blank,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        #Elements.append(f1,Spacer(1,12))        
        #Elements.append(f2,Spacer(1,12))
        
        doc = SimpleDocTemplate('./reports/emailed/multiple/Report'+str(self.test_id).zfill(4)+'.pdf', rightMargin=10,
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
            data2= [ ['Spec. \n No', 'CS Area \n (mm2)', 'Force at Peak\n (N)', 'Compression \n (mm)', 'Compressive Strength \n (MPA)',' % Compression \n']]           
        else:
            data2= [ ['Spec. \n No', 'CS Area \n (mm2)', 'Force at Peak\n (Kg)', 'Compression \n (mm)', 'Compressive Strength \n (MPA)',' % Compression \n']]
          
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.COMPRESSIVE_STRENGTH),printf(\"%.2f\", A.PREC_E_AT_BREAK) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ") 
        for x in results:
                data2.append(x)
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TYPE_STR,printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", COMPRESSIVE_STRENGTH),printf(\"%.2f\", PREC_E_AT_BREAK) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
        for x in results:
                data2.append(x)
        connection.close() 
        
        y=300
        Elements=[]
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime')  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)")
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
        
        doc = SimpleDocTemplate('./reports/emailed/multiple/Report'+str(self.test_id).zfill(4)+'.pdf', rightMargin=10,
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
                    data= [['Spec. \n No.', 'Thickness \n (mm)', 'Width \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]
          
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", A.PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.PREC_E_AT_BREAK)  FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", THICKNESS),printf(\"%.2f\", WIDTH),printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
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
                data= [['Spe. \n No.', 'Diameter \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]

            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.DIAMETER),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", A.PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.PREC_E_AT_BREAK) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", DIAMETER),printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
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
                data= [['Spec. \n No.', 'Inn.Dia \n (mm)', 'Out. Dia \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']]
            
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.INN_DIAMETER),printf(\"%.2f\", A.OUT_DIAMTER),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD), printf(\"%.2f\", A.PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.PREC_E_AT_BREAK) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", INN_DIAMETER),printf(\"%.2f\", OUT_DIAMTER),printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD) ,printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
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
                data= [['Spec.\n No.', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n']] 
                
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", A.PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.PREC_E_AT_BREAK) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
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
                data2[0].append("Mod@"+str(rows[0])+"% \n (Kgf/Cm2)")
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
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime')  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)")
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
        f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
        
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
         
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
        doc = SimpleDocTemplate('./reports/emailed/multiple/Report'+str(self.test_id).zfill(4)+'.pdf', pagesize=A4,rightMargin=20,
                                leftMargin=30,
                                topMargin=30,
                                bottomMargin=30)
        doc.build(Elements)
        #print("Done")
       
        
    def guage_create_pdf_new(self):        
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
                    data= [['Spec. \n No.', 'Thickness \n (cm)', 'Width \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n',' Yeild Strength \n (Kgf/Cm2)','E@Yeild \n Strength \n (Cm)']]
            elif(self.unit_typex == "Lb/Inch"):
                    data= [['Spec. \n No.', 'Thickness \n (Inch)', 'Width \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak \n','E@Break \n (Inch)','%E@Break \n',' Yeild Strength \n (Lb/Inch2)','E@Yeild \n Strength \n(Inch)']]
            elif(self.unit_typex == "Newton/Mm"):
                    data= [['Spec. \n No.', 'Thickness \n (mm)', 'Width \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','E@Peak \n %','E@Break \n (mm)','E@Break \n %',' Yeild Strength \n (N/mm2)','E@Yeild \n Strength \n(Mm)']]
            else:        
                    data= [['Spec. \n No.', 'Thickness \n (mm)', 'Width \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n',' Yeild Strength \n (N/Cm2)','E@Yeild \n Strength \n (Cm)']]
          
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", A.PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.PREC_E_AT_BREAK),printf(\"%.2f\", A.def_yeild_strg),printf(\"%.2f\", A.def_point)  FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", THICKNESS),printf(\"%.2f\", WIDTH),printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", def_yeild_strg),printf(\"%.2f\", def_point) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()            
                  
        elif (self.shape=="Cylindrical"):
            if(self.unit_typex == "Kg/Cm"):    
                data= [['Spe. \n No.', 'Diameter \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n',' Yeild Strength \n (Kg/Cm2)']]
            elif(self.unit_typex == "Lb/Inch"):                
                data= [['Spe. \n No.', 'Diameter \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak \n','E@Break \n (Inch)','%E@Break \n',' Yeild Strength \n (Lb/Inch2)']]
            elif(self.unit_typex == "Newton/Mm"):
                data= [['Spe. \n No.', 'Diameter \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n',' Yeild Strength \n (N/mm2)']]
            else:    
                data= [['Spe. \n No.', 'Diameter \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n',' Yeild Strength \n (N/mm2)']]

            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.DIAMETER),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", A.PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.PREC_E_AT_BREAK),printf(\"%.2f\", A.def_yeild_strg) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", DIAMETER),printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", def_yeild_strg) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()            
            
        elif (self.shape=="Pipe"):            
            if(self.unit_typex == "Kg/Cm"):                
                data= [['Spec. \n No.', 'Inn.Dia \n (cm)', 'Out. Dia \n (cm)', 'CS.Area \n (cm2)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n',' Yeild Strength \n (Kg/Cm2)']]
            elif(self.unit_typex == "Lb/Inch"):                 
                data= [['Spec. \n No.', 'Inn.Dia \n (Inch)', 'Out. Dia \n (Inch)', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak \n','E@Break \n (Inch)','%E@Break \n',' Yeild Strength \n (Lb/Inch2)']]
            elif(self.unit_typex == "Newton/Mm"):
                data= [['Spec. \n No.', 'Inn.Dia \n (mm)', 'Out. Dia \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n',' Yeild Strength \n (N/mm2)']]
            else:                
                data= [['Spec. \n No.', 'Inn.Dia \n (mm)', 'Out. Dia \n (mm)', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n',' Yeild Strength \n (N/mm2)']]
            
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.INN_DIAMETER),printf(\"%.2f\", A.OUT_DIAMTER),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD), printf(\"%.2f\", A.PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.PREC_E_AT_BREAK),printf(\"%.2f\", A.def_yeild_strg) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,printf(\"%.2f\", INN_DIAMETER),printf(\"%.2f\", OUT_DIAMTER),printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD) ,printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", def_yeild_strg) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()            
            
        elif (self.shape=="DirectValue"):
            if(self.unit_typex == "Kg/Cm"):    
                data= [['Spec.\n No.', 'CS.Area \n (cm)','Force at Peak \n (kgf)' ,'E@Peak \n (cm)','% E@Peak \n','E@Break \n (cm)','%E@Break \n',' Yeild Strength \n (Kg/Cm2)']]
            elif(self.unit_typex == "Lb/Inch"):
                data= [['Spec.\n No.', 'CS.Area \n (Inch2)','Force at Peak \n (Lb)' ,'E@Peak \n (Inch)','% E@Peak \n','E@Break \n (Inch)','%E@Break \n',' Yeild Strength \n (Lb/Inch2)']]
            elif(self.unit_typex == "Newton/Mm"):
                data= [['Spec.\n No.', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n',' Yeild Strength \n (N/mm2)']]
            else:                
                data= [['Spec.\n No.', 'CS.Area \n (mm2)','Force at Peak \n (N)' ,'E@Peak \n (mm)','% E@Peak \n','E@Break \n (mm)','%E@Break \n',' Yeild Strength \n (N/mm2)']] 
                
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", A.PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.PREC_E_AT_BREAK),printf(\"%.2f\", A.def_yeild_strg) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
            for x in results:
                data.append(x)
            connection.close()  
        
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("SELECT TYPE_STR,printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", def_yeild_strg) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
            for x in results:
                data.append(x)
            connection.close()  
        
        else:
           data= [['Spec. \n No.', 'Thickness (mm)', 'Width (mm)', 'CS.Area (mm2)','Peak Load (kgf)' ,'% E@Peak \n','Break Load (Kg)','E@Break (mm)','%E@Break \n']]
          
           connection = sqlite3.connect("tyr.db")
           results=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,A.THICKNESS,A.WIDTH,printf(\"%.4f\", A.CS_AREA),A.PEAK_LOAD,A.E_PAEK_LOAD,round(A.PREC_E_AT_PEAK,2),round(A.E_BREAK_LOAD,2),round(A.PREC_E_AT_BREAK,2),printf(\"%.2f\", A.def_yeild_strg) FROM REPORT_MST_II A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_MST_II WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID") 
           for x in results:
                data.append(x)
           connection.close()  
 
           connection = sqlite3.connect("tyr.db")
           results=connection.execute("SELECT TYPE_STR,round(THICKNESS,2),round(WIDTH,2),printf(\"%.4f\", CS_AREA),PEAK_LOAD,round(E_PAEK_LOAD,2),PREC_E_AT_BREAK,printf(\"%.2f\", def_yeild_strg) FROM REPORT_II_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)") 
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
                data2[0].append("Mod@"+str(rows[0])+"% \n (Kgf/Cm2)")
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
        results=connection.execute("SELECT A.TEST_ID,A.JOB_NAME,A.BATCH_ID,A.TEST_TYPE,A.SPECIMEN_NAME,B.MOTOR_SPEED,B.GUAGE_LENGTH_MM,A.PARTY_NAME,B.SPECIMEN_SPECS,B.SHAPE,A.CREATED_ON,datetime(current_timestamp,'localtime')  FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)")
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
        f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
        
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        #TS_STR = Paragraph("Tensile Strength and Modulus Details :", styles["Normal"])
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
         
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
        doc = SimpleDocTemplate('./reports/emailed/multiple/Report'+str(self.test_id).zfill(4)+'.pdf', pagesize=A4,rightMargin=20,
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
        self.thickness=0
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
        results=connection.execute("SELECT GRAPH_ID,TEST_ID,SHAPE,CS_AREA,IFNULL(GUAGE100,0),THINCKNESS FROM CYCLES_MST WHERE TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
                self.graph_ids.append(x[0])             
                ax.set_title("Test Id="+str(x[1]))
                self.cs_area=(x[3])
                self.guage=(x[4])
                self.thickness=str(x[5])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TEST_NAME FROM REPORT_MST LIMIT 1") 
        for x in results:                
                self.test_type=(x[0])              
        connection.close()
        
        
        
        
        if (self.graph_type == "Load Vs Elongation"):
                
                ### Univarsal change for  Graphs ####################
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT GRAPH_SCAL_X_LENGTH,GRAPH_SCAL_Y_LOAD from TEST_MST where TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)") 
                for x in results:
                     if(self.unit_type == "Lb/Inch"):
                         #int_inch=x[0]*
                         ax.set_xlim(0,int((float(x[0])*0.0393701)))
                         ax.set_ylim(0,int((float(x[1])*2.20462)))
                     elif(self.unit_type == "Newton/Mm"):
                         ax.set_xlim(0,int((float(x[0]))))
                         ax.set_ylim(0,int((float(x[1])*9.81)))                     
                     elif(self.unit_type == "MPA"):
                         ax.set_xlim(0,int(x[0]))
                         ax.set_ylim(0,int((float(x[1])*9.81))) 
                     else:
                         ax.set_xlim(0,int(int(x[0])*0.1))
                         ax.set_ylim(0,int(x[1]))
    
                
                for g in range(len(self.graph_ids)):
                    #print("graph id :"+str(self.graph_ids[g]))
                    self.x_num=[0]
                    self.y_num=[0]
                    connection = sqlite3.connect("tyr.db")
                    if(self.test_type=="Compress"):                        
                            results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    else:
                        if(self.unit_type == "Lb/Inch"):    
                            self.kg_to_lb=float(2.20462)
                            self.mm_to_inch=float(0.0393701) 
                            results=connection.execute("SELECT X_NUM*'"+str(self.mm_to_inch)+"',Y_NUM*'"+str(self.kg_to_lb)+"'FROM GRAPH_MST WHERE X_NUM > 0 AND GRAPH_ID='"+str(self.graph_ids[g])+"'")
                        elif(self.unit_type == "Newton/Mm"):
                            self.kg_to_Newton=float(9.81)                                
                            results=connection.execute("SELECT X_NUM,Y_NUM*'"+str(self.kg_to_Newton)+"'FROM GRAPH_MST WHERE X_NUM > 0 AND GRAPH_ID='"+str(self.graph_ids[g])+"'")
                        elif(self.unit_type == "MPA"):
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
                    elif(self.unit_type == "MPA"):
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
                if(self.test_type !="QLSS"):
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    for k in results:                    
                        self.x_num.append((k[0]/float(self.guage))*100)
                        self.y_num.append((k[1]/float(self.cs_area)*100))
                    connection.close() 
                    print("self.cs_area:"+str(self.cs_area))
                    if (g < 8):
                        ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
                else:
                    connection = sqlite3.connect("tyr.db")
                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    for k in results:                    
                        self.x_num.append(((k[0]/(2*float(self.thickness))))*100)
                        self.y_num.append((k[1]/float(self.cs_area)*100))
                    connection.close() 
                    print("self.cs_area:"+str(self.cs_area))
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
    ui = TY_10_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
