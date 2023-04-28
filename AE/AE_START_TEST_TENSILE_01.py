
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import QTableWidgetItem

import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import datetime
import random
import serial,time
import array  as arr
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation





class AE_START_TEST_TENSILE_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 769)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 1321, 691))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 190, 1321, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 121, 31))
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
        self.label_47.setGeometry(QtCore.QRect(1170, 10, 141, 41))
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
        self.pushButton_6.setGeometry(QtCore.QRect(1170, 70, 131, 41))
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
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 210, 1301, 471))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(670, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setGeometry(QtCore.QRect(670, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_11.setStyleSheet("border-radius:20px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(148, 255, 166);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_12.setGeometry(QtCore.QRect(670, 140, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_12.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_13.setGeometry(QtCore.QRect(800, 320, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_13.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_14.setGeometry(QtCore.QRect(670, 320, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_14.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_14.setFlat(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_15.setGeometry(QtCore.QRect(670, 260, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_15.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_15.setFlat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_33 = QtWidgets.QLabel(self.frame_3)
        self.label_33.setGeometry(QtCore.QRect(940, 330, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("")
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.buttongroup = QtWidgets.QButtonGroup()
        self.buttongroup_2 = QtWidgets.QButtonGroup()
        
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton.setGeometry(QtCore.QRect(840, 20, 101, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setGeometry(QtCore.QRect(960, 20, 101, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        
        self.buttongroup.addButton(self.radioButton, 1)
        self.buttongroup.addButton(self.radioButton_2, 2)
        
        
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_3.setGeometry(QtCore.QRect(1080, 20, 81, 31))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_4.setGeometry(QtCore.QRect(1180, 20, 111, 31))
        self.radioButton_4.setObjectName("radioButton_4")
        
        self.buttongroup_2.addButton(self.radioButton_3, 1)
        self.buttongroup_2.addButton(self.radioButton_4, 2)
        
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(20, 380, 1261, 81))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
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
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 6, item)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_16.setGeometry(QtCore.QRect(670, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_16.setStyleSheet("background-color: rgb(169, 202, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_16.setFlat(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_39 = QtWidgets.QLabel(self.frame_3)
        self.label_39.setGeometry(QtCore.QRect(800, 80, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("")
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame_3)
        self.label_40.setGeometry(QtCore.QRect(810, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("")
        self.label_40.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber.setGeometry(QtCore.QRect(940, 80, 261, 61))
        self.lcdNumber.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_41 = QtWidgets.QLabel(self.frame_3)
        self.label_41.setGeometry(QtCore.QRect(1230, 90, 41, 31))
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
        self.lcdNumber_2.setGeometry(QtCore.QRect(940, 160, 261, 61))
        self.lcdNumber_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_42 = QtWidgets.QLabel(self.frame_3)
        self.label_42.setGeometry(QtCore.QRect(1230, 180, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("")
        self.label_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_3)
        self.label_43.setGeometry(QtCore.QRect(790, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("")
        self.label_43.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber_3.setGeometry(QtCore.QRect(940, 240, 261, 61))
        self.lcdNumber_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_44 = QtWidgets.QLabel(self.frame_3)
        self.label_44.setGeometry(QtCore.QRect(1220, 260, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("")
        self.label_44.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_4.setGeometry(QtCore.QRect(1050, 330, 231, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.widget = QtWidgets.QWidget(self.frame_3)
        self.widget.setGeometry(QtCore.QRect(20, 10, 641, 361))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_49 = QtWidgets.QLabel(self.widget)
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
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(1170, 140, 131, 41))
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
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 140, 111, 41))
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
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 50, 61, 31))
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
        self.label_12.setGeometry(QtCore.QRect(80, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(140, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(280, 10, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(150, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_48 = QtWidgets.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(280, 50, 201, 31))
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
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(180, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(280, 170, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(130, 0, 20, 201))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(490, 0, 20, 201))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(760, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_7)
        self.lineEdit_7.setValidator(input_validator)
        self.lineEdit_7.setGeometry(QtCore.QRect(870, 160, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(940, 160, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("")
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(980, 0, 20, 201))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_8)
        self.lineEdit_8.setValidator(input_validator)
        self.lineEdit_8.setGeometry(QtCore.QRect(590, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(500, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(650, 10, 71, 31))
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
        self.label_21.setGeometry(QtCore.QRect(500, 50, 81, 31))
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
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_9)
        self.lineEdit_9.setValidator(input_validator)
        self.lineEdit_9.setGeometry(QtCore.QRect(590, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(650, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("")
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(740, 0, 20, 201))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(760, 10, 81, 31))
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
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_10)
        self.lineEdit_10.setValidator(input_validator)
        self.lineEdit_10.setGeometry(QtCore.QRect(850, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(920, 10, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("")
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(750, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("")
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_11)
        self.lineEdit_11.setValidator(input_validator)
        self.lineEdit_11.setGeometry(QtCore.QRect(850, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(920, 50, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("")
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(750, 90, 241, 20))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(760, 120, 71, 31))
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
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_12)
        self.lineEdit_12.setValidator(input_validator)
        self.lineEdit_12.setGeometry(QtCore.QRect(840, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(940, 120, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("")
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(500, 100, 141, 31))
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
        self.comboBox_2.setGeometry(QtCore.QRect(670, 100, 61, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(510, 150, 141, 31))
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
        self.comboBox_3.setGeometry(QtCore.QRect(670, 150, 61, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(1140, 0, 20, 201))
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
        self.lineEdit_13.setGeometry(QtCore.QRect(1050, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
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
        self.lineEdit_14.setGeometry(QtCore.QRect(1050, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(1000, 140, 131, 41))
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
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(150, 90, 111, 31))
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
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(150, 130, 111, 31))
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
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(10, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame)
        self.label_38.setGeometry(QtCore.QRect(80, 90, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(85, 0, 0);")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.label_45 = QtWidgets.QLabel(self.frame)
        self.label_45.setGeometry(QtCore.QRect(990, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("")
        self.label_45.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.shape=""
        self.thickness=""
        self.width=""
        self.diameter=""
        self.cs_area=""
        self.out_dia=""
        self.inn_dia=""
        self.thickness=0
        self.width=0
        self.inn_dia=0
        self.out_dia=0
        self.diameter=0
        self.cs_area=0
        self.load100_guage=0
        self.load200_guage=0
        self.load300_guage=0
        self.guage_length_mm=0
        self.goAhead="No"
        self.test_type=""
        self.test_id="1"
        self.remark=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Tensile Test"))
        self.label_47.setText(_translate("MainWindow", "05 Aug 2020 14:23:00"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.pushButton_7.setText(_translate("MainWindow", "Stop"))
        self.pushButton_11.setText(_translate("MainWindow", "Start"))
        self.pushButton_12.setText(_translate("MainWindow", "All Graphs"))
        self.pushButton_13.setText(_translate("MainWindow", "View Report"))
        self.pushButton_14.setText(_translate("MainWindow", "Email"))
        self.pushButton_15.setText(_translate("MainWindow", "Comment"))
        self.label_33.setText(_translate("MainWindow", "Show Graph :"))
        self.radioButton.setText(_translate("MainWindow", "Hi-Load cell"))
        self.radioButton_2.setText(_translate("MainWindow", "Low-Load cell"))
        self.radioButton_3.setText(_translate("MainWindow", "Encoder"))
        self.radioButton_4.setText(_translate("MainWindow", "Exentiometer"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Spec.No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Max.Load"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CS.Area"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Displacement."))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "% Displacement."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Tensile Strength"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Cycle.No"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "123.8"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "1"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_16.setText(_translate("MainWindow", "Print"))
        self.label_39.setText(_translate("MainWindow", "Load:"))
        self.label_40.setText(_translate("MainWindow", "Displacement:"))
        self.label_41.setText(_translate("MainWindow", "Kgf."))
        self.label_42.setText(_translate("MainWindow", "Mm."))
        self.label_43.setText(_translate("MainWindow", "Current Test Speed:"))
        self.label_44.setText(_translate("MainWindow", "Mm/Min"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Load Vs Displacement."))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Stress Vs Strain"))
        self.label_49.setText(_translate("MainWindow", "Data Saved Successfully ......"))
        self.pushButton_8.setText(_translate("MainWindow", "Go For Test"))
        self.pushButton_9.setText(_translate("MainWindow", "Reset"))
        self.label_11.setText(_translate("MainWindow", "Test ID:"))
        self.label_12.setText(_translate("MainWindow", "0001"))
        self.label_13.setText(_translate("MainWindow", "Speciment Name:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Speciment 1 XXXXXXXXXXXXXX"))
        self.label_14.setText(_translate("MainWindow", "Party Name:"))
        self.label_48.setText(_translate("MainWindow", "Panakj Polymerst Pvt. Ltd."))
        self.label_15.setText(_translate("MainWindow", "Shape:"))
        self.label_16.setText(_translate("MainWindow", "Rectangular"))
        self.label_17.setText(_translate("MainWindow", "Guage Length:"))
        self.label_18.setText(_translate("MainWindow", "(mm)"))
        self.label_19.setText(_translate("MainWindow", "Test Speed:"))
        self.label_20.setText(_translate("MainWindow", "(mm/min)"))
        self.label_21.setText(_translate("MainWindow", "Rev. Speed:"))
        self.label_22.setText(_translate("MainWindow", "(mm/min)"))
        self.label_23.setText(_translate("MainWindow", "Thickness:"))
        self.label_24.setText(_translate("MainWindow", "(mm)"))
        self.label_25.setText(_translate("MainWindow", "Width:"))
        self.label_26.setText(_translate("MainWindow", "(mm)"))
        self.label_27.setText(_translate("MainWindow", "CS.Area:"))
        self.label_28.setText(_translate("MainWindow", "(mm2)"))
        self.label_29.setText(_translate("MainWindow", "Load Unit:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Kg."))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Lb."))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "N."))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "KN."))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Mpa."))
        self.label_30.setText(_translate("MainWindow", "Displacement.  Unit:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Mm."))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Cm"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Inch."))
        self.label_31.setText(_translate("MainWindow", "X-axis: "))
        self.label_32.setText(_translate("MainWindow", "Y-axis: "))
        self.pushButton_10.setText(_translate("MainWindow", "Set Graph"))
        self.label_35.setText(_translate("MainWindow", "Job Name:"))
        self.label_36.setText(_translate("MainWindow", "Batch ID:"))
        self.label_37.setText(_translate("MainWindow", "  Spec.Count:"))
        self.label_38.setText(_translate("MainWindow", "0"))
        self.label_45.setText(_translate("MainWindow", "Graph Scale "))
        self.comboBox.currentTextChanged.connect(self.onchage_combo)
        self.lineEdit_10.textChanged.connect(self.cs_area_calculation)
        self.lineEdit_11.textChanged.connect(self.cs_area_calculation)
        self.pushButton_8.clicked.connect(self.open_frame3)
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_9.clicked.connect(self.load_data)
        self.pushButton_10.clicked.connect(self.set_graph_scale)
        self.pushButton_11.clicked.connect(self.start_test)
        
        
        
        self.load_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
    
    def device_date(self):     
        self.label_47.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
        
    def load_data(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'TEST_MST'")       
        for x in results:           
                 self.label_12.setText(str(x[0]).zfill(3))
                 self.test_id=str(x[0])
                 self.lineEdit_15.setText("Job_Name__"+str(x[0]).zfill(3))
                 self.lineEdit_16.setText("Batch_"+str(x[0]).zfill(3))
        connection.close()
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
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 FROM SETTING_MST") 
        for x in results:            
            self.lineEdit_13.setText(str(x[0]))
            self.lineEdit_14.setText(str(x[1]))
        connection.close()
        
        self.sc_blank =PlotCanvas_blank(self) 
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        
        self.onchage_combo()
        self.frame_3.hide()
    
    def validations(self):        
        self.go_ahead="No"
        self.msg=""
        if(self.lineEdit_15.text() == ""):
             self.msg="Job Name is Empty."            
        elif(self.lineEdit_16.text()== ""):
             self.msg="Batch ID is Empty."             
        elif(self.lineEdit_8.text()== ""):
             self.msg="Test Speed is Empty."            
        elif(self.lineEdit_9.text() == ""):
             self.msg="Rev.Speed is Empty"
        elif(self.lineEdit_12.text()== ""):
             self.msg="CS Area is Empty."             
        elif(self.lineEdit_7.text()== ""):
             self.msg="Guage Length is Empty."
        else:
              self.msg="Confirm to start Test."
              self.go_ahead="Yes"
    
    def open_frame3(self):
        self.validations()        
        close = QMessageBox()
        close.setText("Message: "+str(self.msg))
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:
                 if(self.go_ahead=="Yes"):                         
                         self.frame_3.show()
                         self.sc_blank =PlotCanvas_blank(self) 
                         self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
                         
                         try:
                                self.serial_3 = serial.Serial(
                                                            port='/dev/ttyUSB0',
                                                            baudrate=19200,
                                                            bytesize=serial.EIGHTBITS,
                                                            parity=serial.PARITY_NONE,
                                                            stopbits=serial.STOPBITS_ONE,
                                                            xonxoff=False,
                                                            timeout = 0.05
                                                        )
                                self.timer4=QtCore.QTimer()
                                self.timer4.setInterval(5000)        
                                self.timer4.timeout.connect(self.loadcell_encoder_status)
                                self.timer4.start(1)
                         except IOError:
                                    print("IO Errors") 
                        
                 else:
                         self.frame_3.hide()
    
    
    def loadcell_encoder_status(self):         
        try:                
            self.serial_3.flush()
            self.serial_3.write(b'*D\r')
            self.line_3 = self.serial_3.readline()
            print("encoder_status:o/p:"+str(self.line_3))
        except IOError:
            print("IO Errors")    
                
        xstr3=str(self.line_3)        
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
            print("Load Cell No... :"+str(self.buff[7]))
            print("Encoder No.. :"+str(self.buff[6]))
            if(str(self.buff[6])=="2"):
                self.load_cell_hi=0
                self.load_cell_lo=1
            else:
                self.load_cell_hi=1
                self.load_cell_lo=0
                    
            if(str(self.buff[7])=="2"):
                self.extiometer=1
                self.encoder=0
            else:
                self.extiometer=0
                self.encoder=1
                
           
            
            
            if(self.load_cell_hi==1):
                self.radioButton.setChecked(True)
                self.radioButton_2.setDisabled(True)
                self.radioButton_2.setChecked(False)
                self.radioButton.setEnabled(True)
            elif(self.load_cell_lo==1):
                self.radioButton_2.setChecked(True)
                self.radioButton.setDisabled(True)
                self.radioButton.setChecked(False)
                self.radioButton_2.setEnabled(True)
         
        
            if(self.extiometer==1):
                self.radioButton_4.setChecked(True)
                self.radioButton_3.setDisabled(True)
                self.radioButton_3.setChecked(False)
                self.radioButton_4.setEnabled(True)            
            elif(self.encoder==1):
                self.radioButton_3.setChecked(True)
                self.radioButton_4.setDisabled(True)
                self.radioButton_4.setChecked(False)
                self.radioButton_3.setEnabled(True)
                                   
    
    
    def onchage_combo(self):                      
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select C_A_AREA,GUAGE_LENGTH_MM,MOTOR_SPEED,PARTY_NAME,THICKNESS,WIDTH,DIAMETER,SHAPE ,IN_DIAMETER_MM,OUTER_DIAMETER_MM,REV_MOTOR_SPEED FROM SPECIMEN_MST WHERE SPECIMEN_NAME='"+self.comboBox.currentText()+"'")                 
        for x in results:
            self.lineEdit_7.setText(str(x[1])) # GUAGE LENGTH
            self.lineEdit_8.setText(str(x[2])) # SPEED
            self.label_48.setText(str(x[3])) # Party Name
            self.label_16.setText(str(x[7])) #shape
            self.shape=str(x[7])
            self.lineEdit_9.setText(str(x[10])) #rev. speed 
            if(str(x[7]) == "Rectangle"):
                   self.lineEdit_10.setText(str(x[4]))#THICKNESS
                   self.lineEdit_11.setText(str(x[5]))#WIDTH
                   self.label_23.setText("Thickness")                
                   self.label_25.setText("Width.") 
                   self.lineEdit_10.show()
                   self.lineEdit_11.show()
                   self.label_23.show()
                   self.label_25.show()
                   self.label_24.show()
                   self.label_26.show()
                   
            elif(str(x[7]) == "Pipe"):
                     self.label_23.setText("Inn.Diam.")                
                     self.label_25.setText("Out.Diam.")
                     self.lineEdit_10.setText(str(x[8]))#INN Diameter
                     self.lineEdit_11.setText(str(x[9]))#OUT.DIAMETER
                     self.lineEdit_10.show()
                     self.lineEdit_11.show()
                     self.label_23.show()
                     self.label_25.show()
                     self.label_24.show()
                     self.label_26.show()
            elif(str(x[7]) == "Cylindrical"):
                     self.label_23.setText("Diameter.")
                     self.lineEdit_10.setText(str(x[6]))# Diameter                    
                     self.lineEdit_10.show()
                     self.label_23.show()
                     self.label_25.hide()
                     self.lineEdit_11.hide()
                     self.label_24.show()
                     self.label_26.hide()
                     #self.label_62.hide()
            elif(str(x[7]) == "DirectValue"):
                    self.label_23.hide()
                    self.lineEdit_10.hide()
                    self.label_25.hide()
                    self.lineEdit_10.hide()
                    self.label_24.hide()
                    self.label_26.hide()
            else:
                    #self.label_21.setText("Invalid:"+str(x[7]))
                    print("Invalid ....")
        
        connection.close()
        #self.click_onRadiobutt()
        self.cs_area_calculation()
        
    
    def cs_area_calculation(self):
        #self.shape=""
        self.thickness=""
        self.width=""
        self.diameter=""
        self.cs_area=""
        self.out_dia=""
        self.inn_dia=""
        
        #self.shape=self.label_16.text()
        if(self.shape== "Rectangle"):
            if(self.lineEdit_10.text() != ""):
                try:
                        self.thickness=int(self.lineEdit_10.text())
                except ValueError as e:
                        try:
                                self.thickness=float(self.lineEdit_10.text())
                        except ValueError as e:
                                self.lineEdit_12.setText("0.00") 
                try:
                        self.width=int(self.lineEdit_11.text())
                except ValueError as e:
                        try:
                                self.width=float(self.lineEdit_11.text())
                        except ValueError as e:
                                self.lineEdit_12.setText("0.00")
                                
                try:
                        self.lineEdit_12.setText(str(round(float(self.thickness * self.width),3)))
                except ValueError as e:
                    #self.lineEdit_3.setText("0.00")
                    print("Caluculation error1");
                    self.lineEdit_12.setText(str("0"))
                except TypeError as e:
                    print("Caluculation error2");
                    self.lineEdit_12.setText(str("0"))
                except:
                    print("Caluculation error3");
                    self.lineEdit_12.setText(str("0"))
            else:
                    self.lineEdit_12.setText(str("0"))
        elif(self.shape== "Cylindrical"):
                try:
                    self.diameter=int(self.lineEdit_10.text())
                except ValueError as e:
                        try:
                            self.diameter=float(self.lineEdit_10.text())
                        except ValueError as e:
                            self.lineEdit_12.setText("0.00")
                
                try:
                            self.lineEdit_12.setText(str(round(float((self.diameter * self.diameter * 3.14)/4),2)))
                except ValueError as e:
                            #self.lineEdit_3.setText("0.00")
                            print("Caluculation error4");
                            self.lineEdit_12.setText(str("0"))
                except TypeError as e:
                            print("Caluculation error5");
                            self.lineEdit_12.setText(str("0"))
                except:
                            print("Caluculation error6");
                            self.lineEdit_12.setText(str("0"))                           
        
        elif(self.shape== "Pipe"):
                try:
                        self.inn_dia=int(self.lineEdit_10.text())
                except ValueError as e:
                        try:
                                self.inn_dia=float(self.lineEdit_10.text())
                        except ValueError as e:
                                self.lineEdit_12.setText("0.00") 
                try:
                        self.out_dia=int(self.lineEdit_11.text())
                except ValueError as e:
                        try:
                            self.out_dia=float(self.lineEdit_11.text())
                        except ValueError as e:
                                self.lineEdit_12.setText("0.00")
                                
                try:
                        self.cs_area=((float(self.out_dia)*float(self.out_dia)*3.14)/4)-((float(self.inn_dia)*float(self.inn_dia)*3.14)/4) 
                        self.lineEdit_12.setText(str(float(self.cs_area)))
                except ValueError as e:
                    #self.lineEdit_3.setText("0.00")
                    print("Caluculation error7");
                    self.lineEdit_12.setText(str("0"))
                except TypeError as e:
                    print("Caluculation error8");
                    self.lineEdit_12.setText(str("0"))
                except:
                    print("Caluculation error9");
                    self.lineEdit_12.setText(str("0"))
        else:
            self.lineEdit_12.setText(str("0"))
        
    def set_graph_scale(self):
        self.x_axis_val="0.0"
        self.y_axis_val="0.0"        
        try:
                self.x_axis_val=int(self.lineEdit_13.text())
        except ValueError as e:
                try:
                       self.x_axis_val=float(self.lineEdit_13.text())
                except ValueError as e:
                       self.lineEdit_13.setText("0.00") 
        try:
                self.y_axis_val=int(self.lineEdit_14.text())
        except ValueError as e:
                try:
                        self.y_axis_val=float(self.lineEdit_14.text())
                except ValueError as e:
                        self.lineEdit_14.setText("0.00")
        
        connection = sqlite3.connect("tyr.db")
        with connection:        
           cursor = connection.cursor()
           cursor.execute("UPDATE SETTING_MST SET GRAPH_SCALE_CELL_2='"+str(self.x_axis_val)+"', GRAPH_SCALE_CELL_1='"+str(self.y_axis_val)+"'")
           print("Graph Scale set Ok !!")
           print("x:"+str(self.x_axis_val)+" y:"+str(self.y_axis_val))
           self.frame_3.hide()
        connection.commit();
        connection.close()
        
    def reset(self):
        if(self.sc_new.timer1.isActive()): 
           self.sc_new.timer1.stop()
           
        if(self.timer3.isActive()): 
           self.timer3.stop()     

    def start_test(self):
        self.sc_new =PlotCanvas_Auto(self,width=8, height=5, dpi=90)
        self.gridLayout.addWidget(self.sc_new, 1, 0, 1, 1)
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT COUNT(*) FROM STG_GRAPH_MST")
        rows=results.fetchall()
        connection.close()               
        print("Test Strated.")       
        #self.label_4.setText(str(rows[0][0]))
        #print("count of stg records :"+str(rows[0][0]))
        if(int(rows[0][0]) > -2 ):
                    self.timer3=QtCore.QTimer()
                    self.timer3.setInterval(1000)        
                    self.timer3.timeout.connect(self.show_load_cell_val)
                    self.timer3.start(1)
                    #self.pushButton_4_5.setEnabled(True)
    
    def show_load_cell_val(self):        
        #self.label_34.setText(str(max(self.sc_new.arr_q)))   #load
        self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q)))
        self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))   #length        
        if(str(self.sc_new.save_data_flg) =="Yes"):
                self.reset()
                #self.save_graph_data()
                self.sc_new.save_data_flg=""
                self.label_49.setText("Data Saved Successfully.")
                self.label_49.show()
        


class PlotCanvas_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="Tensile"
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME from GLOBAL_VAR") 
        for x in results:
            self.test_type=str(x[0])
        connection.close()
        
        if(self.test_type=="Compress"):
            self.axes.set_xlabel('Compression (mm)')        
        else:        
            self.axes.set_xlabel('Elongation (mm)')
          
        self.axes.set_ylabel('Load (Kgf)') 
        self.axes.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.q =0
        self.p_old=0
        self.arr_p=[0.0]
        self.arr_q=[0.0]
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
        self.input_rev_speed_val=""
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
        self.modbus_flag=""
        self.modbus_port=""
        self.non_modbus_port=""
        
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
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE,ISACTIVE_MODBUS,MODBUS_PORT,NON_MODBUS_PORT from SETTING_MST") 
        for x in results:
             self.axes.set_xlim(0,int(x[0]))
             self.axes.set_ylim(0,int(x[1]))
             self.flexural_max_load=int(x[1])
             self.xlim=int(x[0])
             self.ylim=int(x[1])
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
             self.modbus_flag=str(x[4])
             self.modbus_port=str(x[5])
             self.non_modbus_port=str(x[6])
        connection.close()
        
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0) from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=int(x[0])
             self.test_type=str(x[1])
             self.max_load=int(x[2])
             #self.max_load=100
             self.max_length=float(float(x[0])-float(x[3]))
             #self.max_load=str(self.max_load).zfill(5)
             #self.max_length=str(int(self.max_length)).zfill(5)
             #self.max_length=float(x[3])
             print("Max Load :"+str(self.max_load).zfill(5)+" Max length :"+str(int(self.max_length)).zfill(5))
        connection.close()
        
        try:
            print("indicatior -Modbus Flag :"+str(self.modbus_flag))
            if(self.modbus_flag == 'Y'):
                print("indicatior  non_modbus_port:"+str(self.non_modbus_port))
                if(self.non_modbus_port=="/dev/ttyUSB1"):
                        self.ser = serial.Serial(
                                    port='/dev/ttyUSB1',
                                    baudrate=19200,
                                    bytesize=serial.EIGHTBITS,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    xonxoff=False,
                                    timeout = 0.05
                                )
                else:
                        self.ser = serial.Serial(
                                    port='/dev/ttyUSB0',
                                    baudrate=19200,
                                    bytesize=serial.EIGHTBITS,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    xonxoff=False,
                                    timeout = 0.05
                                )
            else:
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
                self.test_guage_mm=0
                self.command_str="*G0.00\r"
            else:
                self.command_str="*G%.2f"%self.test_guage_mm+"\r"
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
                print("started with default motor speed . Not gohead ")
            #self.ser.write(b'*D\r\n')
                
            #time.sleep(2)
            #========Final Motor start Command =========    
            self.ser.flush()
            if(self.test_type=="Compress"):
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                          self.command_str="*S2C%04d"%self.max_load+" %04d"%self.max_length+"\r"
                    else:
                          self.command_str="*S1C%04d"%self.max_load+" %04d"%self.max_length+"\r"
                    
                    print("self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)                 
                else:
                    print("Compress test not started ")               
                               
            elif(self.test_type=="Flexural"):
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                            #self.ser.write(b'*S2E0599 200\r')
                            self.command_str="*S2E%04d"%self.flexural_max_load+" 0000\r"
                    else:
                            self.command_str="*S1E%04d"%self.flexural_max_load+" 0000\r"
                    print("self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    print("fluexural test started ")
                else:
                    print("fluexural test not started ")
            else:
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
            
        
        
        #self.axes.set_autoscale_on(False)
        #self.axes.autoscale(tight=True)
        #self.axes.autoscale(True, 'both', True)
        #self.axes.plot(self.arr_p,self.arr_q)
        #Create Timer here          
        
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
            #print("Running")
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
                    #self.p=int(self.test_guage_mm)-self.p                    
                    if(float(self.test_guage_mm) > float(self.p)):
                        self.p=float(self.test_guage_mm) - float(self.p)
                    else:
                         self.p=self.p-float(self.test_guage_mm)
                    #self.p=self.p-int(self.test_guage_mm)
                    #print("actual self.p :"+str(self.p))
                elif(self.test_type=="Flexural"):
                    self.p=self.p
                else:                    
                    self.p=self.p-int(self.test_guage_mm)
                    if(self.p_old > self.p):
                         self.p=self.p_old                                            
                    self.p_old=self.p
                    #self.p_new=self.p-int(self.test_guage_mm)
                    
                    #self.p=int(self.test_guage_mm)-self.p
                    #self.p=self.p   
                    
                '''
                elif(self.test_type=="Tensile"):
                    self.p=self.p-int(self.test_guage_mm)
                    if(int(len(self.arr_p)) > 0):
                        self.p=float(max(self.arr_p))
                        print("ARRY-P      : XXX "+str(self.arr_p))
                        print("MAX-P      : XXX "+str(self.p))
                        
                        #self.p=float(int(self.p)-int(self.test_guage_mm))
                        print("Length : XXX  "+str(int(len(self.arr_p))))
                        print("P      : XXX "+str(self.p))
                    else:
                        self.p=self.p-int(self.test_guage_mm)
                '''   
                
                
                self.arr_p.append(self.p)
                self.arr_q.append(self.q)
                print(" Timer P:"+str(self.p)+" q:"+str(self.q))
                print("final P :::"+str(self.p)+", guage lengt :"+str(int(self.test_guage_mm)))
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
            else:                
                if(self.test_type=="Compress"):
                    self.p=abs(float(self.buff[4])) #+random.randint(0,50)
                    self.q=abs(float(self.buff[1])) #+random.randint(0,50)
                    #self.p=int(self.test_guage_mm)-self.p
                    if(float(self.test_guage_mm) > float(self.p)):
                        self.p=float(self.test_guage_mm) - float(self.p)
                    else:
                         self.p=self.p-float(self.test_guage_mm)
                    #print("final P :::"+str(self.p)+", guage lengt :"+str(int(self.test_guage_mm)))
                    self.arr_p.append(self.p)
                    self.arr_q.append(self.q)
                    self.save_data_flg="Yes"
                    #self.on_ani_stop()
                elif(self.test_type=="Flexural"):
                    self.p=abs(float(self.buff[4])) #+random.randint(0,50)
                    self.q=abs(float(self.buff[1])) #+random.randint(0,50)
                    #self.p=int(self.test_guage_mm)-self.p
                    print("final P :::"+str(self.p))
                    self.arr_p.append(self.p)
                    self.arr_q.append(self.q)
                    self.save_data_flg="Yes"
                
                else:
                
                    self.save_data_flg="Yes"
                
       
                    
                
               
     
          
    def plot_grah_only(self,i):        
        #self.arr_p1.append(self.p)
        #self.arr_q1.append(self.q)
        #print("Animation :"+str(i))
        #print(" ANI _P:"+str(self.p)+" q:"+str(self.q))
        #print("data :"+str(self.arr_p1[0]))
        '''
        if(self.xlim_update=='YES'):
             self.axes.set_xlim(0,int(self.xlim))
             self.xlim_update='NO'
             self.axes.relim()
             #time.sleep(1)
        if(self.ylim_update=='YES'): 
             self.axes.set_ylim(0,int(self.ylim))
             self.ylim_update='NO'
             self.axes.relim()
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
           #print("Time 1 has been stopped ")
        #if(self.timer3.isActive()): 
           #self.timer3.stop()                                                                                      
           #print("Time 2 has been stopped ")
           
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
        results=connection.execute("SELECT IFNULL(NEW_TEST_MOTOR_SPEED,0), IFNULL(NEW_TEST_MOTOR_REV_SPEED,0) from GLOBAL_VAR") 
        for x in results:
             self.input_speed_val=str(x[0])
             self.input_rev_speed_val=str(x[1])
        connection.close()
        
        if(self.input_speed_val != ""):
            if(float(self.input_speed_val) <= float(self.speed_val)):
                 #print(" Ok ")
                 self.goahead_flag=1
                 self.calc_speed=(float(self.input_speed_val)/float(self.speed_val))*1000                 
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
         
        print("test type :"+str(self.test_type))
        print("Modbus Flag :"+str(self.modbus_flag))
        print("Modbus Port :"+str(self.modbus_port))
        if(self.modbus_flag=='Y' and self.modbus_port != "" ):
            if(self.test_type=="Compress"):        
                v=0
                try:
                    v=float(self.input_rev_speed_val) 
                    v=v*40
                    if(float(v) < 1 ):
                        v=1.0
                    elif(float(v)== 1 ):
                        v=1.0
                    else:
                        v=round(v,0)
                        
                    print("compress :int part :%d"%v)
                    print("compress :decial part:%.2f"%v)
                    #v=v*100
                    if(self.modbus_port=="/dev/ttyUSB0"):
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) #
                    else:
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) # port name, slave address (in decimal)                
                    
                    instrument.serial.timeout = 1
                    instrument.serial.baudrate = 9600 
                    instrument.write_register(4098,v,0) ###self.input_speed_val RPM
                    instrument.write_register(4099,0,0) ###self.input_speed_val RPM
                    print(" write1 :"+str(v))
                except IOError as e:
                    print("Forward-Write Modbus IO Error -Motor start : "+str(e))
                
                print("Forward speed : "+str(v))
            
                v=0
                try:     
                    v=float(self.input_speed_val)
                    #v=float(self.input_rev_speed_val)            
                    v=v*40
                    if(float(v) < 1 ):
                        v=1.0
                    elif(float(v)== 1 ):
                        v=1.0
                    else:
                        v=round(v,0)
                    print("int part :%d"%v)
                    print("decial part:%.2f"%v)         
                    print("self.modbus_port :"+str(self.modbus_port))
                    if(self.modbus_port=="/dev/ttyUSB0"):
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) #
                    elif(self.modbus_port=="/dev/ttyUSB1"):
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) #
                    else:
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) #                        
                   
                    instrument.serial.timeout = 1
                    instrument.serial.baudrate = 9600 
                    instrument.write_register(4096,v,0) ###self.input_speed_val RPM
                    instrument.write_register(4097,0,0) ###self.input_speed_val RPM
                    print(" write2 :"+str(v))
                except IOError as e:
                    print("Reverse-Write Modbus IO Error -Motor start : "+str(e))
                
                print("Reverse speed : "+str(v))
            
            
            
            else:   
                print("inside tesnsile part .....")
                v=0
                try:
                    v=float(self.input_speed_val)
                    v=v*40
                    if(float(v) < 1 ):
                        v=1.0
                    elif(float(v)== 1 ):
                        
                        v=1.0
                    else:
                        v=round(v,0)
                        
                    #print("int part :%d"%v)
                    #print("decial part:%.2f"%v)
                    #v=v*100
                    print("self.modbus_port :"+str(self.modbus_port))
                    if(self.modbus_port=="/dev/ttyUSB1"):
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) #                
                    else:
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) #
                                
                    instrument.serial.timeout = 1
                    instrument.serial.baudrate = 9600            
                    instrument.write_register(4098,v,0) ###self.input_speed_val RPM
                    instrument.write_register(4099,0,0) ###self.input_speed_val RPM
                    print(" write1 :"+str(v))
                except IOError as e:
                    print("Forward-Write Modbus IO Error -Motor start : "+str(e))
                
                print("Forward speed : "+str(v))
            
                v=0
                try:     
                    
                    v=float(self.input_rev_speed_val)            
                    v=v*40
                    if(float(v) < 1 ):
                        v=1.0
                    elif(float(v)== 1 ):
                        v=1.0
                    else:
                        v=round(v,0)
                    print("int part :%d"%v)
                    print("decial part:%.2f"%v)         
                    print("self.modbus_port:"+str(self.modbus_port))
                    if(self.modbus_port=="/dev/ttyUSB1"):
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1) #                       
                    else:
                                instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) #
                    instrument.serial.timeout = 1
                    instrument.serial.baudrate = 9600            
                    instrument.write_register(4096,v,0) ###self.input_speed_val RPM
                    instrument.write_register(4097,0,0) ###self.input_speed_val RPM
                    print(" write2 :"+str(v))
                except IOError as e:
                    print("Reverse-Write Modbus IO Error -Motor start : "+str(e))
                
                print("Reverse speed : "+str(v))
            
 

    
 
        
class PlotCanvas_blank(FigureCanvas):
    def __init__(self, parent=None, width=1, height=0.1, dpi=80):
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
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
             ax.set_xlim(0,float(x[0]))
             ax.set_ylim(0,float(x[1]))          
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])  
              
        ax.plot(self.x,self.y,'b')
        ax.set_ylabel('Load  (Kgf)')
        ax.set_xlabel(' Displacement (Mm)')
        
        
        self.draw()       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AE_START_TEST_TENSILE_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
