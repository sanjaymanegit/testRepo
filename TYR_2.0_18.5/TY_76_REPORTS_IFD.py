

from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow
from comment_popup import comment_Ui_MainWindow
from TY_07_UTM_MANNUAL_CONTROL_3 import  TY_07_3_Ui_MainWindow
from pop_graph_data import pop_graph_data_Ui_MainWindow
from pop_graph_data_radial import pop_graph_data_radial_Ui_MainWindow

import datetime
import platform
import shutil
import sqlite3
import subprocess
import statistics
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.Qt import QTableWidgetItem
#### PDF creation Libs ########
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY 
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import portrait,landscape, letter,inch,A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Line, Drawing
import os
class TY_76_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.load_unit = ""
        self.initial_values = []
        self.Kg_to_N = []
        self.N_to_Kg = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 756)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 1321, 701))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 200, 1321, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(1160, 10, 141, 21))
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
        self.pushButton_6.setGeometry(QtCore.QRect(1160, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setStyleSheet("#pushButton_6 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));\n"
"    \n"
"\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_6:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_6:pressed {\n"
"background-color: rgb(198, 198, 198);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 270, 1281, 421))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(810, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_7.setStyleSheet("#pushButton_7 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 0, 0), stop:1  rgb(158, 3, 3));\n"
"    \n"
"    \n"
"\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_7:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(158, 3, 3), stop:1  rgb(255, 0, 0));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_7:pressed {\n"
"background-color: rgb(255, 0, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setGeometry(QtCore.QRect(810, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_11.setStyleSheet("#pushButton_11 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(85, 255, 0), stop:1  rgb(7, 240, 151));\n"
"    \n"
"\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_11:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(7, 240, 151), stop:1  rgb(85, 255, 0));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_11:pressed {\n"
"background-color: rgb(85, 255, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(810, 110, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_12.setStyleSheet("#pushButton_12 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"    \n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_12:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_12:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_13.setGeometry(QtCore.QRect(810, 310, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_13.setStyleSheet("#pushButton_13 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"    \n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_13:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_13:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_14.setGeometry(QtCore.QRect(810, 260, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_14.setStyleSheet("#pushButton_14 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(85, 255, 255), stop:1  rgb(44, 69, 211));\n"
"    \n"
"    \n"
"\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_14:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(85, 255, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_14:pressed {\n"
"background-color: rgb(85, 255, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_14.setFlat(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_15.setGeometry(QtCore.QRect(810, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_15.setStyleSheet("#pushButton_15 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"    \n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_15:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_15:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_15.setFlat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(930, 20, 341, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_16.setGeometry(QtCore.QRect(810, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_16.setStyleSheet("#pushButton_16 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"    \n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_16:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_16:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_16.setFlat(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber.setGeometry(QtCore.QRect(940, 280, 231, 51))
        self.lcdNumber.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_41 = QtWidgets.QLabel(self.frame_3)
        self.label_41.setGeometry(QtCore.QRect(1180, 290, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("")
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber_2.setGeometry(QtCore.QRect(940, 350, 231, 51))
        self.lcdNumber_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_42 = QtWidgets.QLabel(self.frame_3)
        self.label_42.setGeometry(QtCore.QRect(1190, 350, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("")
        self.label_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_49.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.gridLayout.addWidget(self.label_49, 0, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_18.setGeometry(QtCore.QRect(810, 360, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_18.setStyleSheet("#pushButton_18 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"    \n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_18:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_18:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_18.setFlat(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(1160, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_8.setStyleSheet("#pushButton_8 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(85, 255, 0), stop:1  rgb(7, 240, 151));\n"
"    \n"
"\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_8:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(7, 240, 151), stop:1  rgb(85, 255, 0));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_8:pressed {\n"
"background-color: rgb(85, 255, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 160, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_9.setStyleSheet("#pushButton_9 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(12, 146, 158), stop:1  rgb(97, 242, 255));\n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_9:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(97, 242, 255), stop:1  rgb(12, 146, 158));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_9:pressed {\n"
"background-color: rgb(97, 242, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(80, 10, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(910, 160, 51, 41))
#         self.comboBox.setStyleSheet("background-color: rgb(217, 217, 217);\n"
# "border: 1px solid rgba(131,131,131,255);\n"
# "border-radius: 8px;")
        self.comboBox.setStyleSheet("background-color: rgb(170, 255, 255);\n color: rgb(0, 0, 0);")
        self.comboBox.setMaxVisibleItems(8)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(160, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(160, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(140, 0, 20, 211))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(490, 0, 20, 211))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(980, 0, 20, 211))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(670, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(500, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(590, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(740, 0, 20, 211))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(510, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("")
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_12.setGeometry(QtCore.QRect(590, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(10, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("")
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 60, 51, 31))
#         self.comboBox_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
# "border: 1px solid rgba(131,131,131,255);\n"
# "border-radius: 8px;")
        self.comboBox_2.setStyleSheet("background-color: rgb(170, 255, 255);\n color: rgb(0, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(10, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("")
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 110, 51, 41))
#         self.comboBox_3.setStyleSheet("background-color: rgb(217, 217, 217);\n"
# "border: 1px solid rgba(131,131,131,255);\n"
# "border-radius: 8px;")
        self.comboBox_3.setStyleSheet("background-color: rgb(170, 255, 255);\n color: rgb(0, 0, 0);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(1140, 0, 20, 211))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(990, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("")
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_13.setGeometry(QtCore.QRect(1050, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(990, 90, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("")
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(1050, 90, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(1000, 150, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_10.setStyleSheet("#pushButton_10 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 38, 154), stop:1  rgb(226, 102, 135));\n"
"    \n"
"\n"
"\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_10:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(226, 102, 135), stop:1  rgb(255, 38, 154));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_10:pressed {\n"
"background-color: rgb(255, 38, 154);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(160, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("")
        self.label_35.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(280, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(160, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("")
        self.label_36.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(280, 130, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_45 = QtWidgets.QLabel(self.frame)
        self.label_45.setGeometry(QtCore.QRect(1010, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("")
        self.label_45.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(0, 250, 1321, 21))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.label_46 = QtWidgets.QLabel(self.frame)
        self.label_46.setGeometry(QtCore.QRect(510, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("")
        self.label_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setGeometry(QtCore.QRect(590, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(500, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("")
        self.label_50.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_18.setGeometry(QtCore.QRect(590, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(680, 110, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("")
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_19.setGeometry(QtCore.QRect(300, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(1160, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_17.setStyleSheet("#pushButton_17 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(253, 169, 0), stop:1  rgb(206, 221, 71));\n"
"    \n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_17:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(206, 221, 71), stop:1  rgb(253, 169, 0));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_17:pressed {\n"
"background-color: rgb(253, 169, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_17.setFlat(False)
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_63 = QtWidgets.QLabel(self.frame)
        self.label_63.setGeometry(QtCore.QRect(1110, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("")
        self.label_63.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_63.setObjectName("label_63")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(1110, 40, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("")
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(180, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(850, 59, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(750, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(760, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("")
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setGeometry(QtCore.QRect(850, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(910, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("")
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setGeometry(QtCore.QRect(760, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_19.setStyleSheet("#pushButton_19 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 0), stop:1  rgb(217, 200, 64));\n"
"    \n"
"\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_19:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(217, 200, 64), stop:1  rgb(255, 255, 0));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_19:pressed {\n"
"background-color: rgb(255, 255, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_19.setFlat(False)
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_90 = QtWidgets.QLabel(self.frame)
        self.label_90.setGeometry(QtCore.QRect(10, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_90.setFont(font)
        self.label_90.setStyleSheet("")
        self.label_90.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_90.setObjectName("label_90")
        self.label_91 = QtWidgets.QLabel(self.frame)
        self.label_91.setGeometry(QtCore.QRect(120, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_91.setFont(font)
        self.label_91.setStyleSheet("")
        self.label_91.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_91.setObjectName("label_91")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_37.setGeometry(QtCore.QRect(70, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_37.setFont(font)
        self.lineEdit_37.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(280, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(280, 50, 191, 31))
#         self.comboBox_4.setStyleSheet("background-color: rgb(217, 217, 217);\n"
# "border: 1px solid rgba(131,131,131,255);\n"
# "border-radius: 8px;")
        self.comboBox_4.setStyleSheet("background-color: rgb(170, 255, 255);\n color: rgb(0, 0, 0);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(1000, 220, 311, 31))
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
        self.label_38 = QtWidgets.QLabel(self.frame)
        self.label_38.setGeometry(QtCore.QRect(680, 60, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("")
        self.label_38.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.frame)
        self.label_39.setGeometry(QtCore.QRect(680, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("")
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_92 = QtWidgets.QLabel(self.frame)
        self.label_92.setGeometry(QtCore.QRect(170, 220, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_92.setFont(font)
        self.label_92.setStyleSheet("")
        self.label_92.setAlignment(QtCore.Qt.AlignCenter)
        self.label_92.setObjectName("label_92")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setGeometry(QtCore.QRect(240, 210, 20, 51))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setGeometry(QtCore.QRect(490, 210, 20, 51))
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.frame)
        self.line_11.setGeometry(QtCore.QRect(740, 210, 20, 51))
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.frame)
        self.line_12.setGeometry(QtCore.QRect(980, 210, 20, 51))
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setObjectName("line_12")
        self.label_93 = QtWidgets.QLabel(self.frame)
        self.label_93.setGeometry(QtCore.QRect(410, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_93.setFont(font)
        self.label_93.setStyleSheet("")
        self.label_93.setAlignment(QtCore.Qt.AlignCenter)
        self.label_93.setObjectName("label_93")
        self.label_94 = QtWidgets.QLabel(self.frame)
        self.label_94.setGeometry(QtCore.QRect(370, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_94.setFont(font)
        self.label_94.setStyleSheet("")
        self.label_94.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_94.setObjectName("label_94")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_38.setGeometry(QtCore.QRect(320, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_38.setFont(font)
        self.lineEdit_38.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.label_95 = QtWidgets.QLabel(self.frame)
        self.label_95.setGeometry(QtCore.QRect(260, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_95.setFont(font)
        self.label_95.setStyleSheet("")
        self.label_95.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_95.setObjectName("label_95")
        self.label_96 = QtWidgets.QLabel(self.frame)
        self.label_96.setGeometry(QtCore.QRect(660, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_96.setFont(font)
        self.label_96.setStyleSheet("")
        self.label_96.setAlignment(QtCore.Qt.AlignCenter)
        self.label_96.setObjectName("label_96")
        self.label_97 = QtWidgets.QLabel(self.frame)
        self.label_97.setGeometry(QtCore.QRect(620, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_97.setFont(font)
        self.label_97.setStyleSheet("")
        self.label_97.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_97.setObjectName("label_97")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_39.setGeometry(QtCore.QRect(570, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_39.setFont(font)
        self.lineEdit_39.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.label_98 = QtWidgets.QLabel(self.frame)
        self.label_98.setGeometry(QtCore.QRect(510, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_98.setFont(font)
        self.label_98.setStyleSheet("")
        self.label_98.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_98.setObjectName("label_98")
        self.label_99 = QtWidgets.QLabel(self.frame)
        self.label_99.setGeometry(QtCore.QRect(910, 220, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_99.setFont(font)
        self.label_99.setStyleSheet("")
        self.label_99.setAlignment(QtCore.Qt.AlignCenter)
        self.label_99.setObjectName("label_99")
        self.label_100 = QtWidgets.QLabel(self.frame)
        self.label_100.setGeometry(QtCore.QRect(870, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_100.setFont(font)
        self.label_100.setStyleSheet("")
        self.label_100.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_100.setObjectName("label_100")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_40.setGeometry(QtCore.QRect(820, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_40.setFont(font)
        self.lineEdit_40.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.label_101 = QtWidgets.QLabel(self.frame)
        self.label_101.setGeometry(QtCore.QRect(760, 220, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_101.setFont(font)
        self.label_101.setStyleSheet("")
        self.label_101.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_101.setObjectName("label_101")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(750, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("")
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_11.setGeometry(QtCore.QRect(850, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(131,131,131,255);\n"
"border-radius: 8px;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(910, 110, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("")
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_47.setText(_translate("MainWindow", "05 Aug 2020 14:23:00"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.pushButton_7.setText(_translate("MainWindow", "Stop"))
        self.pushButton_11.setText(_translate("MainWindow", "Start"))
        self.pushButton_12.setText(_translate("MainWindow", "All Graphs"))
        self.pushButton_13.setText(_translate("MainWindow", "View Report"))
        self.pushButton_14.setText(_translate("MainWindow", "Email"))
        self.pushButton_15.setText(_translate("MainWindow", "Comment"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Def. % (mm)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Load  (Kgf)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Rec# "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sample #"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sample #"))
        item = self.tableWidget.horizontalHeaderItem(5)
        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_16.setText(_translate("MainWindow", "Print"))
        self.label_41.setText(_translate("MainWindow", "Kgf."))
        self.label_42.setText(_translate("MainWindow", "Mm"))
        self.label_49.setText(_translate("MainWindow", "Data Saved Successfully ......"))
        self.pushButton_18.setText(_translate("MainWindow", "Data"))
        self.pushButton_8.setText(_translate("MainWindow", "Go For Test"))
        self.pushButton_9.setText(_translate("MainWindow", "Reset"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "0001"))
        self.comboBox.setItemText(0, _translate("MainWindow", "02"))
        self.comboBox.setItemText(1, _translate("MainWindow", "03"))
        self.comboBox.setItemText(2, _translate("MainWindow", "04"))
        self.label_14.setText(_translate("MainWindow", "Specimen Name:"))
        self.label_15.setText(_translate("MainWindow", "LoadCell. Capacity :"))
        self.label_20.setText(_translate("MainWindow", "(mm/min)"))
        self.label_21.setText(_translate("MainWindow", "Test Speed: "))
        self.label_27.setText(_translate("MainWindow", "Length :"))
        self.label_29.setText(_translate("MainWindow", "Load Unit:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Kg"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "N"))
        self.label_30.setText(_translate("MainWindow", "Deflection \n"
" Unit:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Mm"))
        self.label_31.setText(_translate("MainWindow", "X-axis: "))
        self.label_32.setText(_translate("MainWindow", "Y-axis: "))
        self.pushButton_10.setText(_translate("MainWindow", "Set Graph"))
        self.label_35.setText(_translate("MainWindow", "Job Name :"))
        self.label_36.setText(_translate("MainWindow", "Batch Number :"))
        self.label_45.setText(_translate("MainWindow", "Graph Scale "))
        self.label_46.setText(_translate("MainWindow", "Thickness:"))
        self.label_50.setText(_translate("MainWindow", "Width:"))
        self.label_34.setText(_translate("MainWindow", "(Mm)"))
        self.pushButton_17.setText(_translate("MainWindow", "Set Pre Load"))
        self.label_63.setText(_translate("MainWindow", "(Kg)"))
        self.label_37.setText(_translate("MainWindow", "(Mm)"))
        self.label_16.setText(_translate("MainWindow", "Test Name :"))
        self.label_26.setText(_translate("MainWindow", "01"))
        self.label_28.setText(_translate("MainWindow", "Spec. Count:"))
        self.label_23.setText(_translate("MainWindow", "Rev Speed: "))
        self.label_25.setText(_translate("MainWindow", "(mm/min)"))
        self.pushButton_19.setText(_translate("MainWindow", "Set Def. Points"))
        self.label_90.setText(_translate("MainWindow", "Def.(1):"))
        self.label_91.setText(_translate("MainWindow", "(%)"))
        self.label_13.setText(_translate("MainWindow", "IFD Report"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "MRF"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "ABC"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "XYZ"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "XXX"))
        self.label_10.setText(_translate("MainWindow", "Graph set Done."))
        self.label_38.setText(_translate("MainWindow", "(Mm)"))
        self.label_39.setText(_translate("MainWindow", "(Mm)"))
        self.label_92.setText(_translate("MainWindow", "( 25 mm )"))
        self.label_93.setText(_translate("MainWindow", "( 25 mm )"))
        self.label_94.setText(_translate("MainWindow", "(%)"))
        self.label_95.setText(_translate("MainWindow", "Def.(2):"))
        self.label_96.setText(_translate("MainWindow", "( 25 mm )"))
        self.label_97.setText(_translate("MainWindow", "(%)"))
        self.label_98.setText(_translate("MainWindow", "Def.(3):"))
        self.label_99.setText(_translate("MainWindow", "( 25 mm )"))
        self.label_100.setText(_translate("MainWindow", "(%)"))
        self.label_101.setText(_translate("MainWindow", "Def.(4):"))
        self.label_24.setText(_translate("MainWindow", "Pre Load:"))
        self.label_33.setText(_translate("MainWindow", "(Kg)"))
        self.pushButton_11.hide()
        self.pushButton_7.hide()
        self.timer1=QtCore.QTimer()
        self.timer1.start(1)
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.setDateAndTime)
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.label_10.hide()
        self.load_data()
        self.readOnly_fields()
        self.set_load_points()
        # self.load_unit_on_change()
        self.show_grid_data()
        self.pushButton_9.clicked.connect(self.readWrite_fields)
        self.comboBox_2.currentTextChanged.connect(self.load_unit_on_change)
        self.pushButton_8.clicked.connect(self.go_for_report)
        self.pushButton_13.clicked.connect(self.open_pdf)
        
        
        self.pushButton_16.clicked.connect(self.print_file)
        self.pushButton_14.clicked.connect(self.open_email_report)
        self.pushButton_15.clicked.connect(self.open_comment_popup)
        self.pushButton_12.clicked.connect(self.show_all_specimens)
        self.pushButton_18.clicked.connect(self.open_graph_data)
        
        self.go_for_report()
        # self.comboBox.currentTextChanged.connect(self.set_load_points)
        
    
    def print_file(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)
        self.create_pdf_Tear()
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POP_TEST_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_email_report(self):
        #self.test_id=(self.tableWidget.item(row, 1).text() )
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)
        self.create_pdf_Tear()
        print(" test_id :"+str(self.test_id))  
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("update global_var set EMAIL_TEST_ID=TEST_ID")                 
        connection.commit()
        connection.close()
            
        self.window = QtWidgets.QMainWindow()
        self.ui=popup_email_test_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def show_all_specimens(self):        
        #self.pushButton_3.setDisabled(True) ### save
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                       cursor = connection.cursor()                
                       cursor.execute("UPDATE GLOBAL_VAR2 SET GRAPH_TYPE=''")                                   
        connection.commit()
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)    
        self.gridLayout.addWidget(self.sc_data, 1,0,1,1)
        
        
    def open_comment_popup(self):
        
        #print(" test_id :"+str(self.test_id))  
        connection = sqlite3.connect("tyr.db")        
        with connection:        
                    cursor = connection.cursor()                
                    cursor.execute("update global_var set EMAIL_TEST_ID=TEST_ID")                 
        connection.commit()
        connection.close()
            
        self.window = QtWidgets.QMainWindow()
        self.ui=comment_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_graph_data(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=pop_graph_data_radial_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def readWrite_fields(self):
        self.pushButton_8.setEnabled(True)
        self.frame_3.hide()
        fields = [self.comboBox_2, self.lineEdit_15, self.lineEdit_16, self.lineEdit_19, self.lineEdit_12, 
                  self.lineEdit_9, self.lineEdit_17, self.lineEdit_18, self.lineEdit_10, self.lineEdit_13, self.lineEdit_14, self.lineEdit_37, self.lineEdit_39, 
                  self.lineEdit_38, self.lineEdit_39, self.lineEdit_40, self.lineEdit_11
                ]
        self.indx=0
        for field in fields:
                if ( int(self.indx) <= 0 ):
                      field.setEnabled(True)
                else:
                
                      field.setReadOnly(True)
                self.indx = self.indx + 1
        
    
    def go_for_report(self):
        self.show_grid_data()    
        self.readOnly_fields()
        self.frame_3.show()
        self.label_49.setText("All Graphs")
        self.sc_blank = PlotCanvas(self)  
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        connection = sqlite3.connect("tyr.db")              
        with connection:
                cursor = connection.cursor() 
                cursor.execute("UPDATE TEST_MST SET PRE_LOAD = '"+str(self.lineEdit_11.text())+"', LAST_UNIT_LOAD = '"+str(self.comboBox_2.currentText())+"' WHERE  TEST_ID = '"+str(int(self.label_12.text()))+"'")                 
                cursor.execute("UPDATE TEST_DATA_RADIAL SET LOAD_UNIT = '"+str(self.comboBox_2.currentText())+"' WHERE  TEST_ID = '"+str(int(self.label_12.text()))+"'")
                cursor.execute("UPDATE SETTING_MST SET GRAPH_SCALE_CELL_2 = '"+str(self.lineEdit_14.text())+"'")

                if str(self.comboBox_2.currentText()) == "Kgf":
                      cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_Y_LOAD = '"+str(self.lineEdit_14.text())+"' WHERE  TEST_ID = '"+str(int(self.label_12.text()))+"' ")
                else:
                      cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_Y_LOAD_N = '"+str(self.lineEdit_14.text())+"' WHERE  TEST_ID = '"+str(int(self.label_12.text()))+"' ")
                            

        connection.commit()
        connection.close()
    def load_data(self):
        # hiding the load fields initially
        widgets = [
            self.lineEdit_39 ,self.label_96, self.lineEdit_40, self.label_97, self.label_98, self.label_99,
            self.label_101, self.label_100, 
              
                ]
        for widget in widgets:
             widget.hide()  

        self.pushButton_8.setDisabled(True)
        self.pushButton_17.setDisabled(True)
        self.pushButton_10.setDisabled(True)

        # Selecting the test id from global var
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TEST_ID FROM GLOBAL_VAR")       
        for x in results:  
                self.test_id=str(x[0])         
                self.label_12.setText(str(x[0]).zfill(4))
        connection.close()  

        self.comboBox_4.clear()
        self.comboBox.clear()   
        connection = sqlite3.connect("tyr.db")
        print("SELECT LOAD_POINTS, IFNULL(D1_PER,0), D1, IFNULL(D2_PER,0), D2, IFNULL(D3_PER,0), D3, IFNULL(D4_PER,0), D4 FROM TEST_DATA_RADIAL WHERE TEST_ID = '"+str(int(self.label_12.text()))+"' LIMIT 1") 
       
        results = connection.execute("SELECT LOAD_POINTS, IFNULL(D1_PER,0), D1, IFNULL(D2_PER,0), D2, IFNULL(D3_PER,0), D3, IFNULL(D4_PER,0), D4 FROM TEST_DATA_RADIAL WHERE TEST_ID = '"+str(int(self.label_12.text()))+"' LIMIT 1") 
        for x in results:
             self.comboBox.addItem(str(x[0]).zfill(2))
             self.lineEdit_37.setText(str(x[1]))
             self.label_92.setText(str(x[2]))
             self.lineEdit_38.setText(str(x[3]))
             self.label_93.setText(str(x[4]))
             self.lineEdit_39.setText(str(x[5]))
             self.label_96.setText(str(x[6]))
             self.lineEdit_40.setText(str(x[7]))
             self.label_99.setText(str(x[8]))
             

        connection.close() 

        # Selecting the specimen name from SPECIMEN_MST
        # connection = sqlite3.connect("tyr.db") 
        # results = connection.execute("SELECT DISTINCT SPECIMEN_NAME FROM SPECIMEN_MST WHERE SPECIMEN_NAME IS NOT NULL")
        # for x in results:
        #     specimen_name = x[0]
        #     self.comboBox_4.addItem(specimen_name)
        # connection.close()    

        
        connection = sqlite3.connect("tyr.db") 
        results = connection.execute("SELECT SPECIMEN_NAME, MOTOR_REV_SPEED, MOTOR_SPEED, PRE_LOAD, FINAL_WIDTH, IFNULL(FINAL_THICKNESS, 0), GUAGE_LENGTH, JOB_NAME, BATCH_ID, LAST_UNIT_LOAD, GRAPH_SCAL_X_LENGTH, GRAPH_SCAL_Y_LOAD, IFNULL(GRAPH_SCAL_Y_LOAD_N, 0)  FROM TEST_MST WHERE TEST_ID = '"+str(self.label_12.text())+"'") 
        for column in results:
             self.comboBox_4.addItem(str(column[0]))
             self.lineEdit_10.setText(str(column[1])) 
             self.lineEdit_9.setText(str(column[2]))
             self.lineEdit_11.setText(str(column[3])) 
             self.lineEdit_18.setText(str(column[4])) 
             self.lineEdit_17.setText(str(column[5]))
             self.lineEdit_12.setText(str(column[6]))
             self.lineEdit_15.setText(str(column[7]))
             self.lineEdit_16.setText(str(column[8]))
             print("See the Units : ", str(column[9]))
             if str(column[9]) == "Kgf":
                self.comboBox_2.setCurrentIndex(0)
                self.lineEdit_14.setText(str(column[11]))
             else:
                self.comboBox_2.setCurrentIndex(1)
                self.lineEdit_14.setText(str(column[11]))
             self.lineEdit_13.setText(str(column[10]))
             
                       



             
        connection.close() 

        # # Selecting the graph scale from SETTING_MST
        # connection = sqlite3.connect("tyr.db") 
        # results = connection.execute("SELECT GRAPH_SCALE_CELL_1, GRAPH_SCALE_CELL_2 FROM SETTING_MST") 
        # for scale in results:
        #      self.lineEdit_13.setText(str(scale[0]))
        #      self.lineEdit_14.setText(str(scale[1]))
        # connection.close() 

        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LOAD_CELL FROM SPECIMEN_MST WHERE SPECIMEN_NAME = '"+str(self.comboBox_4.currentText())+"'")       
        for x in results:         
                self.lineEdit_19.setText(str(x[0]))
        connection.close() 

        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT COUNT(*) FROM TEST_DATA_RADIAL WHERE TEST_ID = '"+str(self.label_12.text())+"'")       
        for x in results:         
                self.label_26.setText(str(x[0]).zfill(2))
        connection.close() 

        self.initial_unit = self.comboBox_2.currentText()
        print("initial unit :", self.initial_unit)
        self.preLoad_and_y_ax_widget = [self.lineEdit_11, self.lineEdit_14]
        self.preLoad_and_y_ax_value = [line_Edit.text() for line_Edit in self.preLoad_and_y_ax_widget]
        print("preLoad_and_y_ax_value :", self.preLoad_and_y_ax_value)
        
    # Updating the graph scale into the SETTING_MST                                   
    def graph_scale_on_change(self):
        connection = sqlite3.connect("tyr.db") 
        with connection:
                cursor = connection.cursor()
                cursor.execute("UPDATE SETTING_MST SET GRAPH_SCALE_CELL_1='"+str(self.lineEdit_13.text())+"', GRAPH_SCALE_CELL_2 ='"+str(self.lineEdit_14.text())+"'") 
        connection.commit()
        connection.close()
        self.label_10.setText("Graph Scale Updated...") 
        self.label_10.show()

    def load_unit_on_change(self):
        unit = str(self.comboBox_2.currentText())  
        load_unit_widgets = [self.label_33, self.label_63] 
        if (unit == "Kg"):
             self.current_unit = "Kg"  
             for label in load_unit_widgets:
                label.setText("(" + str(unit) + ")")
        #      self.comboBox_3.setCurrentIndex(0)
        else:
                self.current_unit = "N"  
                for label in load_unit_widgets:
                        label.setText("(" + str(unit) + ")")
        #       self.comboBox_3.setCurrentIndex(0)

        if self.initial_unit == "Kg":
             for x in self.preLoad_and_y_ax_value:
                if x.strip():
                        self.Kg_to_N.append(float(x) * 9.81)
                        print("load unit :", self.Kg_to_N) 
        else:
              for x in self.preLoad_and_y_ax_value:
                if x.strip():
                        self.N_to_Kg.append(float(x) * 0.10197)

        if (self.initial_unit == "Kg" and self.current_unit == "N"):
                self.updateConvertedValue(self.Kg_to_N, self.preLoad_and_y_ax_widget)
                connection = sqlite3.connect("tyr.db")              
                with connection:
                        cursor = connection.cursor() 
                        cursor.execute("UPDATE TEST_DATA_RADIAL SET L1 = printf(\"%.2f\",L1 * 9.81), L2 = printf(\"%.2f\",L2 * 9.81), L3 = printf(\"%.2f\",L3 * 9.81), L4 = printf(\"%.2f\",L4 * 9.81) WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
                connection.commit()
                connection.close() 
        elif (self.initial_unit == "Kg" and self.current_unit == "Kg"):
                for x in self.Kg_to_N:
                        self.N_to_Kg.append(float(x) * 0.10197)
                self.updateConvertedValue(self.N_to_Kg, self.preLoad_and_y_ax_widget)
                connection = sqlite3.connect("tyr.db")              
                with connection:
                        cursor = connection.cursor() 
                        cursor.execute("UPDATE TEST_DATA_RADIAL SET L1 = printf(\"%.2f\",L1 * 0.10197), L2 = printf(\"%.2f\",L2 * 0.10197), L3 = printf(\"%.2f\",L3 * 0.10197), L4 = printf(\"%.2f\",L4 * 0.10197) WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
                connection.commit()
                connection.close()  
        elif (self.initial_unit == "N" and self.current_unit == "Kg"):
                self.updateConvertedValue(self.N_to_Kg, self.preLoad_and_y_ax_widget) 
                connection = sqlite3.connect("tyr.db")              
                with connection:
                        cursor = connection.cursor() 
                        cursor.execute("UPDATE TEST_DATA_RADIAL SET L1 = printf(\"%.2f\",L1 * 0.10197), L2 = printf(\"%.2f\",L2 * 0.10197), L3 = printf(\"%.2f\",L3 * 0.10197), L4 = printf(\"%.2f\",L4 * 0.10197) WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
                connection.commit()
                connection.close() 
        elif (self.initial_unit == "N" and self.current_unit == "N"):
                for x in self.N_to_Kg:
                        self.Kg_to_N.append(float(x) * 9.81)
                self.updateConvertedValue(self.Kg_to_N, self.preLoad_and_y_ax_widget) 
                connection = sqlite3.connect("tyr.db")              
                with connection:
                        cursor = connection.cursor() 
                        cursor.execute("UPDATE TEST_DATA_RADIAL SET L1 = printf(\"%.2f\",L1 * 9.81), L2 = printf(\"%.2f\",L2 * 9.81), L3 = printf(\"%.2f\",L3 * 9.81), L4 = printf(\"%.2f\",L4 * 9.81) WHERE TEST_ID = '"+str(self.label_12.text())+"' ")       
                connection.commit()
                connection.close()         
        else:
              pass

             

    def updateConvertedValue(self, values, widgets):
        for value, widget in zip(values, widgets):
                if (value != ""):
                        float_value = float(value)
                        formatted_value = "{:.2f}".format(float_value)
                        widget.setText(str(formatted_value))
                else:
                        print("Empty string in arrey")  
                     
    def set_load_points(self):
        set_value = str(self.comboBox.currentText())
        load_points = {
        "03": [self.label_98, self.lineEdit_39, self.label_96, self.label_97],
        "04": [self.label_98, self.lineEdit_39, self.label_96, self.label_97, self.label_101, self.lineEdit_40, self.label_100, self.label_99],
        }
      
        for widgets_list in load_points.values():
                for widget in widgets_list:
                        widget.hide()
                               
        if set_value in load_points:
                for widget in load_points[set_value]:
                        widget.show()
        else:
             print("set value is not valide")

    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)       
    def readOnly_fields(self):
        fields = [self.comboBox, self.comboBox_2, self.comboBox_3, self.comboBox_4, self.lineEdit_15, self.lineEdit_16, self.lineEdit_19, self.lineEdit_12, 
                  self.lineEdit_9, self.lineEdit_17, self.lineEdit_18, self.lineEdit_10, self.lineEdit_13, self.lineEdit_14, self.lineEdit_37, self.lineEdit_39, 
                  self.lineEdit_38, self.lineEdit_39, self.lineEdit_40, self.lineEdit_11
                ]
        self.indx=0
        for field in fields:
                if ( int(self.indx) <= 3 ):
                      field.setEnabled(False)
                else:
                      field.setReadOnly(True)
                self.indx = self.indx + 1
    
    def show_grid_data(self):
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)        
        
        if(int(str(self.comboBox.currentText())) == 3):       
                self.tableWidget.setColumnCount(5)
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setColumnWidth(1, 100)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.setColumnWidth(3, 100) 
                self.tableWidget.setColumnWidth(4, 100)                
                self.tableWidget.setHorizontalHeaderLabels(['Sample # ','Thickness \n'+str(self.lineEdit_17.text())+' ( mm )','IFD@ '+str(self.lineEdit_37.text())+' % \n ('+str(self.comboBox_2.currentText())+')', 'IFD@ '+str(self.lineEdit_38.text())+' % \n ('+str(self.comboBox_2.currentText())+')', 'IFD@ '+str(self.lineEdit_39.text())+' % \n ('+str(self.comboBox_2.currentText())+')'])
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.2f\",STIFFNESS),printf(\"%.2f\",L1) ,printf(\"%.2f\",L2),printf(\"%.2f\",L3) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
   
        elif(int(str(self.comboBox.currentText())) == 4):       
                self.tableWidget.setColumnCount(6)
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setColumnWidth(1, 100)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.setColumnWidth(3, 100)
                self.tableWidget.setColumnWidth(4, 100)
                self.tableWidget.setColumnWidth(5, 100)                
                self.tableWidget.setHorizontalHeaderLabels(['Sample #','Thickness \n'+str(self.lineEdit_17.text())+' ( mm )','IFD@ '+str(self.lineEdit_37.text())+' % \n ('+str(self.comboBox_2.currentText())+')', 'IFD@ '+str(self.lineEdit_38.text())+' % \n ('+str(self.comboBox_2.currentText())+')', 'IFD@ '+str(self.lineEdit_39.text())+' % \n ('+str(self.comboBox_2.currentText())+')', 'IFD@ '+str(self.lineEdit_40.text())+' % \n ('+str(self.comboBox_2.currentText())+')'])
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.2f\",STIFFNESS),printf(\"%.2f\",L1) ,printf(\"%.2f\",L2),printf(\"%.2f\",L3),printf(\"%.2f\",L4) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
   
        else:
                self.tableWidget.setColumnCount(4)
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setColumnWidth(1, 100)
                self.tableWidget.setColumnWidth(2, 100)
                self.tableWidget.setColumnWidth(3, 100)                
                self.tableWidget.setHorizontalHeaderLabels(['Sample #','Thickness \n'+str(self.lineEdit_17.text())+' ( mm )','IFD@ '+str(self.lineEdit_37.text())+' % \n ('+str(self.comboBox_2.currentText())+')', 'IFD@ '+str(self.lineEdit_38.text())+' % \n ('+str(self.comboBox_2.currentText())+')'])
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID),printf(\"%.2f\",STIFFNESS),printf(\"%.2f\",L1) ,printf(\"%.2f\",L2) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
   
        


        for row_number, row_data in enumerate(results):            
             self.tableWidget.insertRow(row_number)
             for column_number, data in enumerate(row_data):
                         self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
                 #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close() 



    def setDateAndTime(self):
        self.label_47.setText(datetime.datetime.now().strftime("%d %b %Y %H : %M : %S"))
    def get_usb_storage_id(self):
        if platform.system() == "Linux":
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
        elif platform.system() == "Windows":
                try:
                        subprocess.run(["Del", "connected_usb_device.txt"], shell=True, check=True)
                except subprocess.CalledProcessError as error:
                        print("file not deleted :", error)       
                try:
                        subprocess.run("wmic path Win32_USBControllerDevice get Dependent", stdout=open("connected_usb_device.txt", "w"), shell=True, check=True)
                        with open("connected_usb_device.txt", "r", encoding="utf-16") as usb_name_file:
                                print(usb_name_file)  # Just for debugging
                                product_id = 'ERROR'
                                for LINE in usb_name_file:
                                        # print(LINE)  # Just for debugging
                                        # print(LINE.strip())  # Remove leading/trailing whitespace and newlines
                                        if "SANDISK" in LINE:  
                                                product_id = 'SANDISK'
                                                # print(product_id, ": Found in LINE")
                                                break
                                        # else:
                                        #         print("SANDISK not found in : line")
                except subprocess.CalledProcessError as error:
                        print("unable to run the command :", error)
        else:
               print("platform is macOS....")
        return product_id
    def open_pdf(self):
        self.sc_data = PlotCanvas(self, width=8, height=5, dpi=90) 
        #self.pushButton_4_2.setEnabled(True)
        #self.pushButton_4_3.setEnabled(True)
        self.create_pdf_Tear()
        
        if platform.system() == "Linux":
                os.system("xpdf ./reports/test_report.pdf")
                product_id = self.get_usb_storage_id()
                if product_id != "ERROR":
                        os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                        os.system("cp ./reports/test_report.pdf /media/usb/Report_of_test_"+str(self.test_id)+".pdf")
                        os.system("sudo umount /media/usb")
                else:
                        print("Please connect USB storage device")
                
        elif platform.system() == "Windows":
                os.system("start ./reports/test_report.pdf")
                product_id = self.get_usb_storage_id()
                if product_id != "ERROR":
                        shutil.copy("./reports/test_report.pdf", "E:/")  # Destination directory
                        print("Report copied to USB drive.")
                else:
                        print("Please connect USB storage device")
        else:
               print("platform is macOS....")

    
               
    def create_pdf_Tear(self):
        self.remark=""
        self.login_user_name=""
        self.unit_typex="Kg/Cm"
        data2= []
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_UNIT_LOAD,LAST_UNIT_DISP,TEST_ID,TESTED_BY from TEST_MST  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ") 
        for x in results:
              self.last_load_unit=str(x[0])
              self.last_disp_unit=str(x[1])
              self.test_id=str(x[2])
              self.tested_by=str(x[3])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT A.CREATED_ON,A.TEST_ID,B.LOAD_CELL,A.BATCH_ID,A.FINAL_THICKNESS,A.HARDNESS,A.TEST_TYPE,A.MACHINE_NO,B.PARTY_NAME,A.MOTOR_REV_SPEED,A.MATERIAL,datetime(current_timestamp,'localtime'),A.COMMENTS,A.OPERATOR,A.MOTOR_SPEED   FROM TEST_MST A, SPECIMEN_MST B WHERE A.SPECIMEN_NAME=B.SPECIMEN_NAME AND A.TEST_ID in (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            summary_data=[["Tested Date-Time: ",str(x[0]),"Test No: ",str(x[1])],["Thickness:  ",str(x[4]),"Batch ID: ",str(x[3])],["Test Type:",str(x[6]),"Load Cell Cap. : ",str(x[2])],["Customer Name :",str(x[8]),"Report Date-Time: ",str(x[11])],["Test Speed (min/min) :",str(x[14]),"Rev. Speed (min/min) :",str(x[9])],["Operator :",str(x[13]), " ", " "]]
            self.remark=str(x[12]) 
        connection.close()
        
        
        if(int(str(self.comboBox.currentText())) == 2) :
                  connection = sqlite3.connect("tyr.db")
                  data2= [['Spec.','Thickness'+' \n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')', ' Def \n @ '+str(self.lineEdit_37.text())+ ' % ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' % ('+str(self.comboBox_2.currentText())+')']]
                #   print(data2)
                  results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID), printf(\"%.2f\",STIFFNESS), printf(\"%.2f\",L1), printf(\"%.2f\",L2) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for x in results:
                                data2.append(x)
                                # print(data2)
                  connection.close()
                  
                  if int(self.label_26.text()) > 1:

                        stddev = ['Stddev']
                        varianc = ['Variance']
                        CV = ['CV']
                        mean_Stiffness = []
                        stddev_Stiffness = []
                        varianc_Stiffness = []
                        stddev_L1 = []
                        stddev_L2 = []
                        
                        varianc_L1 = []
                        varianc_L2 = []
                        mean_L1 = []
                        mean_L2 = []
                        
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT printf(\"%.2f\",STIFFNESS) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        
                        for x in results:
                                stddev_Stiffness.append(float(x[0])) 
                                varianc_Stiffness.append(float(x[0])) 
                        print("SEE THE STIFFNESS :", stddev_Stiffness)            
                        std_dev = statistics.stdev(stddev_Stiffness)
                        _varianc = statistics.variance(varianc_Stiffness)
                        stddev.append(f"{std_dev:.2f}")
                        varianc.append(f"{_varianc:.2f}")

                        results=connection.execute("SELECT printf(\"%.2f\",L1) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                stddev_L1.append(float(x[0])) 
                                varianc_L1.append(float(x[0])) 
                                
                        std_dev = statistics.stdev(stddev_L1)
                        _varianc = statistics.variance(varianc_L1)
                        stddev.append(f"{std_dev:.2f}")
                        varianc.append(f"{_varianc:.2f}")
                        results=connection.execute("SELECT printf(\"%.2f\",L2) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                stddev_L2.append(float(x[0])) 
                                varianc_L2.append(float(x[0])) 
                                   
                        std_dev = statistics.stdev(stddev_L2)
                        _varianc = statistics.variance(varianc_L2)
                        stddev.append(f"{std_dev:.2f}")
                        varianc.append(f"{_varianc:.2f}")
                        
                        connection.close()
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT 'Avg', printf(\"%.2f\",avg(STIFFNESS)), printf(\"%.2f\",avg(L1)) , printf(\"%.2f\",avg(L2)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                        data2.append(x)
                                        # print(data2)
                        connection.close()
                        
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT 'Max', printf(\"%.2f\",Max(STIFFNESS)), printf(\"%.2f\",max(L1)) ,printf(\"%.2f\",max(L2)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                        data2.append(x)
                                        # print(data2)
                        connection.close()
                        
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT 'Min', printf(\"%.2f\",Min(STIFFNESS)), printf(\"%.2f\",min(L1)) ,printf(\"%.2f\",min(L2)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                data2.append(x)
                        connection.close()


                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT printf(\"%.2f\",avg(STIFFNESS)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_Stiffness.append(float(x[0])) 
                        results=connection.execute("SELECT printf(\"%.2f\",avg(L1)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_L1.append(float(x[0])) 
                        results=connection.execute("SELECT printf(\"%.2f\",avg(L2)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_L2.append(float(x[0]))         
                        connection.close()
                        print("stddev :", stddev)
                        print("mean_L1 :", mean_L1[0])
                        CV.append(f"{(float(stddev[1]) / float(mean_Stiffness[0])):.2f}")
                        CV.append(f"{(float(stddev[2]) / float(mean_L1[0])):.2f}")
                        CV.append(f"{(float(stddev[3]) / float(mean_L2[0])):.2f}")
                        data2.append(stddev)
                        data2.append(varianc)
                        data2.append(CV)

        elif(int(str(self.comboBox.currentText())) == 3) :
                   
                  
                  
                  connection = sqlite3.connect("tyr.db")
                  data2= [['Spec.','Thickness'+' \n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')', ' Def \n @ '+str(self.lineEdit_37.text())+' % ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' % ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_39.text())+' % ('+str(self.comboBox_2.currentText())+') ']]
                #   print(data2)
                  results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID), printf(\"%.2f\",STIFFNESS), printf(\"%.2f\",L1), printf(\"%.2f\",L2), printf(\"%.2f\",L3) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                  for x in results:
                                
                                data2.append(x)
                                # print(data2)
                  connection.close()
                  #print("see the spec number :", int(self.label_26.text()))
                  if int(self.label_26.text()) > 1:

                        # connection = sqlite3.connect("tyr.db")
                        # results=connection.execute("SELECT 'Stddev', printf(\"%.2f\",STIFFNESS), printf(\"%.2f\",L1), printf(\"%.2f\",L2), printf(\"%.2f\",L3) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        
                        # # results=connection.execute("SELECT 'Stddev', printf(\"%.2f\",avg(STIFFNESS)), printf(\"%.2f\",avg(L1)) , printf(\"%.2f\",avg(L2)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        # for x in results:
                        #                 data2.append(x)
                        #                 # print(data2)
                        # connection.close() 
                        # print("see the data2 value : ", data2) 
                        stddev = ['Stddev']
                        varianc = ['Variance']
                        CV = ['CV']
                        mean_Stiffness = []
                        stddev_Stiffness = []
                        varianc_Stiffness = []
                        stddev_L1 = []
                        stddev_L2 = []
                        stddev_L3 = []
                        varianc_L1 = []
                        varianc_L2 = []
                        varianc_L3 = []
                        mean_L1 = []
                        mean_L2 = []
                        mean_L3 = []
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT printf(\"%.2f\",STIFFNESS) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        
                        for x in results:
                                stddev_Stiffness.append(float(x[0])) 
                                varianc_Stiffness.append(float(x[0])) 
                        print("SEE THE STIFFNESS :", stddev_Stiffness)            
                        std_dev = statistics.stdev(stddev_Stiffness)
                        _varianc = statistics.variance(varianc_Stiffness)

                        stddev.append(f"{std_dev:.2f}")
                        varianc.append(f"{_varianc:.2f}")

                        results=connection.execute("SELECT printf(\"%.2f\",L1) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        # results=connection.execute("SELECT printf(\"%.2f\",L1) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        
                        for x in results:
                                stddev_L1.append(float(x[0])) 
                                varianc_L1.append(float(x[0]))         
                        print("see the stddev :", stddev_L1)
                        std_dev = statistics.stdev(stddev_L1)
                        _varianc = statistics.variance(varianc_L1)
                        stddev.append(f"{std_dev:.2f}")
                        varianc.append(f"{_varianc:.2f}")
                        results=connection.execute("SELECT printf(\"%.2f\",L2) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        # results=connection.execute("SELECT printf(\"%.2f\",avg(L2)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        
                        for x in results:
                                stddev_L2.append(float(x[0])) 
                                varianc_L2.append(float(x[0])) 
                                   
                        std_dev = statistics.stdev(stddev_L2)
                        _varianc = statistics.variance(varianc_L2)
                        stddev.append(f"{std_dev:.2f}")
                        varianc.append(f"{_varianc:.2f}")
                        results=connection.execute("SELECT printf(\"%.2f\",L3) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                stddev_L3.append(float(x[0])) 
                                varianc_L3.append(float(x[0]))   
                        std_dev = statistics.stdev(stddev_L3)
                        _varianc = statistics.variance(varianc_L3)
                        stddev.append(f"{std_dev:.2f}")
                        varianc.append(f"{_varianc:.2f}")
                        
                        connection.close()
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT printf(\"%.2f\",avg(STIFFNESS)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_Stiffness.append(float(x[0])) 
                        results=connection.execute("SELECT printf(\"%.2f\",avg(L1)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_L1.append(float(x[0])) 
                        results=connection.execute("SELECT printf(\"%.2f\",avg(L2)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_L2.append(float(x[0]))         
                        results=connection.execute("SELECT printf(\"%.2f\",avg(L3)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_L3.append(float(x[0])) 
                        connection.close()
                        print("stddev :", stddev)
                        print("mean_L1 :", mean_L1[0])
                        CV.append(f"{(float(stddev[1]) / float(mean_Stiffness[0])):.2f}")
                        CV.append(f"{(float(stddev[2]) / float(mean_L1[0])):.2f}")
                        CV.append(f"{(float(stddev[3]) / float(mean_L2[0])):.2f}")
                        CV.append(f"{(float(stddev[3]) / float(mean_L3[0])):.2f}")


                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT 'Avg', printf(\"%.2f\",avg(STIFFNESS)), printf(\"%.2f\",avg(L1)) ,printf(\"%.2f\",avg(L2)), printf(\"%.2f\",avg(L3)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for y in results:
                                        data2.append(y)
                                        # print(data2)
                        connection.close()
                        
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT 'Max', printf(\"%.2f\",Max(STIFFNESS)), printf(\"%.2f\",max(L1)), printf(\"%.2f\",max(L2)), printf(\"%.2f\",max(L3)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for z in results:
                                        data2.append(z)
                        connection.close()
                        
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT 'Min',printf(\"%.2f\",Min(STIFFNESS)), printf(\"%.2f\",min(L1)), printf(\"%.2f\",min(L2)), printf(\"%.2f\",min(L3)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for n in results:
                                data2.append(n)
                        connection.close()
                        data2.append(stddev)
                        data2.append(varianc)
                        data2.append(CV)
        elif(int(str(self.comboBox.currentText())) == 4) :                  
                  connection = sqlite3.connect("tyr.db")
                  data2= [['Spec.','Thickness'+' \n ('+str(self.comboBox_2.currentText())+' / '+str(self.comboBox_3.currentText())+')', ' Def \n @ '+str(self.lineEdit_37.text())+' % ('+str(self.comboBox_2.currentText())+') ',' Def \n @ '+str(self.lineEdit_38.text())+' % ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_39.text())+' % ('+str(self.comboBox_2.currentText())+')', ' Def \n @ '+str(self.lineEdit_40.text())+' % ('+str(self.comboBox_2.currentText())+')']]
                #   print(data2)
                  results=connection.execute("SELECT printf(\"%.2f\",SPEC_ID), printf(\"%.2f\",STIFFNESS), printf(\"%.2f\",L1) ,printf(\"%.2f\",L2), printf(\"%.2f\",L3), printf(\"%.2f\",L4) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(int(self.comboBox.currentText()))+"'")
                  for x in results:
                                data2.append(x)
                                # print(data2)
                  connection.close()
                  print(" spec count :"+str(int(self.label_26.text())))
                  if int(self.label_26.text()) > 1:
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT 'Avg', printf(\"%.2f\",avg(STIFFNESS)), printf(\"%.2f\",avg(L1)) ,printf(\"%.2f\",avg(L2)), printf(\"%.2f\",avg(L3)), printf(\"%.2f\",avg(L4)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for y in results:
                                data2.append(y)
                                # print(data2)
                        connection.close()
                        
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT 'Max', printf(\"%.2f\",Max(STIFFNESS)), printf(\"%.2f\",max(L1)) ,printf(\"%.2f\",max(L2)), printf(\"%.2f\",max(L3)), printf(\"%.2f\",max(L4)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for z in results:
                                data2.append(z)
                        connection.close()
                        
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT 'Min', printf(\"%.2f\",Min(STIFFNESS)), printf(\"%.2f\",min(L1)) ,printf(\"%.2f\",min(L2)), printf(\"%.2f\",min(L3)), printf(\"%.2f\",min(L4)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for n in results:
                                data2.append(n)
                        connection.close()
                        connection = sqlite3.connect("tyr.db")
                        results=connection.execute("SELECT printf(\"%.2f\",avg(STIFFNESS)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_Stiffness.append(float(x[0])) 
                        results=connection.execute("SELECT printf(\"%.2f\",avg(L1)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_L1.append(float(x[0])) 
                        results=connection.execute("SELECT printf(\"%.2f\",avg(L2)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_L2.append(float(x[0]))         
                        results=connection.execute("SELECT printf(\"%.2f\",avg(L3)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_L3.append(float(x[0])) 
                        results=connection.execute("SELECT printf(\"%.2f\",avg(L4)) FROM TEST_DATA_RADIAL WHERE TEST_ID='"+str(int(self.label_12.text()))+"' and LOAD_POINTS='"+str(self.comboBox.currentText())+"'")
                        for x in results:
                                mean_L4.append(float(x[0])) 
                        
                        connection.close()
                        print("stddev :", stddev)
                        print("mean_L1 :", mean_L1[0])
                        CV.append(f"{(float(stddev[1]) / float(mean_Stiffness[0])):.2f}")
                        CV.append(f"{(float(stddev[2]) / float(mean_L1[0])):.2f}")
                        CV.append(f"{(float(stddev[3]) / float(mean_L2[0])):.2f}")
                        CV.append(f"{(float(stddev[4]) / float(mean_L3[0])):.2f}")
                        CV.append(f"{(float(stddev[5]) / float(mean_L4[0])):.2f}")
                        data2.append(stddev)
                        data2.append(varianc)
                        data2.append(CV)
        else:
           print("Invalid Def Points")
        
        
        
               
        
        y=300
        Elements=[]
        
        
        print("data2 : "+str(data2))
        
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select COMPANY_NAME,ADDRESS1 from SETTING_MST ") 
        for x in results:            
            Title = Paragraph(str(x[0]), styles["Title"])
        #     Title = [Cell(str(x[0]), styles["Title"], ln = 1)]
            #Title2 = Paragraph(str(x[1]), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
            
            
            
        connection.close()
        
        blank=Paragraph("                                                                                          ", styles["Normal"])
        #comments = Paragraph("Remark : ______________________________________________________________________________", styles["Normal"])
        if(str(self.remark) == "None"):
                comments = Paragraph("    <b> Remark : </b>______________________________________________________________________________", styles["Normal"])
        else:
                comments = Paragraph("   <b>  Remark :  </b> "+str(self.remark), styles["Normal"])
        footer_2= Paragraph(" <b> Authorised and Signed By : </b> _________________.", styles["Normal"])
        
        linea_firma = Line(0, 30, 525, 30)
        d = Drawing(100, 1)
        d.add(linea_firma)
        
        f2=Table(data2)
        f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
       
       
        
          
         
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1.00, colors.black), ('BACKGROUND', (0, 0), (0, 0), colors.lightgrey), ('BACKGROUND', (0, 2), (0, 2), colors.lightgrey), ('BACKGROUND', (0, 4), (0, 4), colors.lightgrey), ('BACKGROUND', (2, 0), (2, 0), colors.lightgrey), ('BACKGROUND', (2, 2), (2, 2), colors.lightgrey), ('BACKGROUND', (2, 4), (2, 4), colors.lightgrey),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.red), ('FONT', (0, 0), (-1, -1), "Helvetica", 10),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'), ('COLWIDTHS', (0, 0), (-1, -1), [50,100,50,100]), ('ALIGN', (1,0), (1,-1), 'CENTER'), ('ALIGN', (3,0), (3,-1), 'CENTER')]))       
        
        #self.show_all_specimens()
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img,
                        6 * inch, 4* inch)
        report_logo_img="./images/companylogo.jpg"        
        pdf_logo_img = Image(report_logo_img,
                        1 * inch, 1 * inch)
        header = [[pdf_logo_img], [Title, Title2]]
        col_widths = [1.2 * inch, 4.5 * inch]
        f1 = Table([header], colWidths=col_widths)
         
        f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1.00, colors.white), ('INNERGRID', (0, 0), (-1, -1), 0.50, colors.white), ('ALIGN', (0, 0), (-1,-1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])) 

        Elements=[Spacer(1,12),f1,Spacer(1,40),d,f3,Spacer(1,12),pdf_img,Spacer(1,12),Spacer(1,12),f2,Spacer(1,12),blank,comments,Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12)]
        
        try:
               
                doc = SimpleDocTemplate('./reports/test_report.pdf', pagesize=A4, rightMargin=20,
                                        leftMargin=30,
                                        topMargin=10,
                                        bottomMargin=10)
                doc.build(Elements)
        except PermissionError as error:
               print("Alredy Report :", error)        
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
        results=connection.execute("SELECT DISTINCT GRAPH_ID FROM TEST_DATA_RADIAL WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
              self.graph_ids.append(x[0])            
              print("Grph IDs :"+str(x[0]))
        connection.close()
        

        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_UNIT_LOAD,LAST_UNIT_DISP,GRAPH_SCAL_X_LENGTH,GRAPH_SCAL_Y_LOAD from TEST_MST  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ") 
        for x in results:
              self.last_load_unit=str(x[0])
              self.last_disp_unit=str(x[1])
              ax.set_xlim(0,float(x[2]))
              ax.set_ylim(0,float(x[3]))  
        connection.close()
        
        
        
        
        
        self.graph_type="Load Vs Deflection"
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
            connection = sqlite3.connect("tyr.db")
            if(self.graph_type=="Load Vs Deflection"):
                    if(self.last_load_unit=="Kgf" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Kgf" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Kgf" and self.last_disp_unit=="Inch"):
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
                    results=connection.execute("SELECT T_SEC,Y_NUM FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
         
            else:
                #     results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                pass
            for k in results:        
                self.x_num.append(k[0])
                self.y_num.append(k[1])
            connection.close()
           
            if(g < 8 ):
                ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
        
        print("self.graph_type :"+str(self.graph_type))
        if(self.graph_type=="Load Vs Travel"):
                ax.set_xlabel('Deflection ('+str(self.last_disp_unit)+')')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        
        elif(self.graph_type=="Load Vs Time"):
                ax.set_xlabel('Time (sec)')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        else:
                ax.set_xlabel('Deflection ('+str(self.last_disp_unit)+')')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        #self.connect('motion_notify_event', mouse_move)
        ax.legend()        
        self.draw()
        self.figure.savefig('last_graph.png',dpi=100)
        
        #ax.connect('motion_notify_event', mouse_move)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_76_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
