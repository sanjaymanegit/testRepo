# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ur_reports.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from print_popup import P_POPUi_MainWindow
from ur_14_pop_comment import ur_14_Ui_Form

from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY 
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import portrait,landscape, letter,inch,A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Line, Drawing

import datetime
import serial,time
import array  as arr
import numpy as np
import sqlite3
import sys
import os
import re

class ur_12_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 766)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1331, 711))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 50, 171, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 40, 131, 31))
        #self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1180, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 50, 511, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 40, 121, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(360, 40, 111, 31))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setGeometry(QtCore.QRect(270, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_38 = QtWidgets.QLabel(self.groupBox_3)
        self.label_38.setGeometry(QtCore.QRect(30, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(20, 140, 1271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(10, 170, 231, 531))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(860, 380, 461, 321))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(210, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(10, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_26 = QtWidgets.QLabel(self.groupBox_4)
        self.label_26.setGeometry(QtCore.QRect(10, 100, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label_28.setGeometry(QtCore.QRect(10, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_31 = QtWidgets.QLabel(self.groupBox_4)
        self.label_31.setGeometry(QtCore.QRect(10, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_35 = QtWidgets.QLabel(self.groupBox_4)
        self.label_35.setGeometry(QtCore.QRect(10, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(200, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(330, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.line = QtWidgets.QFrame(self.groupBox_4)
        self.line.setGeometry(QtCore.QRect(10, 60, 421, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(350, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        self.label_27.setGeometry(QtCore.QRect(210, 100, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_36 = QtWidgets.QLabel(self.groupBox_4)
        self.label_36.setGeometry(QtCore.QRect(10, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.label_49 = QtWidgets.QLabel(self.groupBox_4)
        self.label_49.setGeometry(QtCore.QRect(10, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.groupBox_4)
        self.label_50.setGeometry(QtCore.QRect(10, 280, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_50.setFont(font)
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.label_29 = QtWidgets.QLabel(self.groupBox_4)
        self.label_29.setGeometry(QtCore.QRect(350, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_32 = QtWidgets.QLabel(self.groupBox_4)
        self.label_32.setGeometry(QtCore.QRect(210, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.label_51 = QtWidgets.QLabel(self.groupBox_4)
        self.label_51.setGeometry(QtCore.QRect(210, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.groupBox_4)
        self.label_52.setGeometry(QtCore.QRect(210, 190, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_52.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.groupBox_4)
        self.label_53.setGeometry(QtCore.QRect(210, 220, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_53.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.groupBox_4)
        self.label_54.setGeometry(QtCore.QRect(210, 250, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_54.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.groupBox_4)
        self.label_55.setGeometry(QtCore.QRect(210, 280, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_55.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.groupBox_4)
        self.label_56.setGeometry(QtCore.QRect(350, 130, 51, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_56.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.groupBox_4)
        self.label_57.setGeometry(QtCore.QRect(350, 160, 51, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_57.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.groupBox_4)
        self.label_58.setGeometry(QtCore.QRect(350, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_58.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.groupBox_4)
        self.label_59.setGeometry(QtCore.QRect(350, 220, 51, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_59.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.groupBox_4)
        self.label_60.setGeometry(QtCore.QRect(350, 250, 51, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_60.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.groupBox_4)
        self.label_61.setGeometry(QtCore.QRect(350, 280, 51, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_61.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_61.setObjectName("label_61")
        self.line_3 = QtWidgets.QFrame(self.groupBox_4)
        self.line_3.setGeometry(QtCore.QRect(0, 90, 431, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.groupBox_4)
        self.line_4.setGeometry(QtCore.QRect(0, 120, 431, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.groupBox_4)
        self.line_5.setGeometry(QtCore.QRect(0, 150, 431, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.groupBox_4)
        self.line_6.setGeometry(QtCore.QRect(10, 180, 421, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.groupBox_4)
        self.line_7.setGeometry(QtCore.QRect(0, 210, 431, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.groupBox_4)
        self.line_8.setGeometry(QtCore.QRect(10, 240, 421, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.groupBox_4)
        self.line_9.setGeometry(QtCore.QRect(10, 270, 421, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(1060, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(1110, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(1060, 110, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(360, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_5.setEnabled(True)
        self.radioButton_5.setGeometry(QtCore.QRect(830, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_8.setGeometry(QtCore.QRect(780, 50, 261, 91))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 40, 131, 31))
        #self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_10.setGeometry(QtCore.QRect(170, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(1030, -10, 296, 183))
        self.calendarWidget.setSelectedDate(QtCore.QDate(2018, 8, 30))
        self.calendarWidget.setMaximumDate(QtCore.QDate(9999, 8, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setGeometry(QtCore.QRect(860, 170, 461, 201))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_34 = QtWidgets.QLabel(self.groupBox_5)
        self.label_34.setGeometry(QtCore.QRect(130, 70, 51, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_34.setFont(font)
        #self.label_34.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_34.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(20, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(20, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_39 = QtWidgets.QLabel(self.groupBox_5)
        self.label_39.setGeometry(QtCore.QRect(130, 30, 281, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.groupBox_5)
        self.label_40.setGeometry(QtCore.QRect(20, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.groupBox_5)
        self.label_41.setGeometry(QtCore.QRect(130, 150, 291, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.groupBox_5)
        self.label_42.setGeometry(QtCore.QRect(20, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.groupBox_5)
        self.label_43.setGeometry(QtCore.QRect(130, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_43.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.groupBox_5)
        self.label_44.setGeometry(QtCore.QRect(10, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.groupBox_5)
        self.label_45.setGeometry(QtCore.QRect(130, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_45.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.groupBox_5)
        self.label_46.setGeometry(QtCore.QRect(10, 250, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.groupBox_5)
        self.label_47.setGeometry(QtCore.QRect(130, 250, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(200, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_48 = QtWidgets.QLabel(self.groupBox_5)
        self.label_48.setGeometry(QtCore.QRect(350, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.label_62 = QtWidgets.QLabel(self.groupBox_5)
        self.label_62.setGeometry(QtCore.QRect(200, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_62.setFont(font)
        self.label_62.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.groupBox_5)
        self.label_63.setGeometry(QtCore.QRect(267, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_63.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_63.setObjectName("label_63")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 30, 81, 24))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        
        self.pushButton_13_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13_1.setGeometry(QtCore.QRect(1216, 158, 80, 24))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_13_1.setFont(font)
        self.pushButton_13_1.setObjectName("pushButton_13_1")
        
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(250, 170, 601, 531))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 5)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget)
        self.pushButton_12.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 1, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setEnabled(False)
        #self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 4, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Patient.ID."))
        self.pushButton_6.setText(_translate("MainWindow", "Retrun"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Patient Name."))
        self.label_30.setText(_translate("MainWindow", "Last Name:"))
        self.label_38.setText(_translate("MainWindow", "First Name"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("MainWindow", "Reports Details"))
        self.label_24.setText(_translate("MainWindow", "xxmax_flow"))
        self.label_13.setText(_translate("MainWindow", "Max. Flow(ml/sec)"))
        self.label_26.setText(_translate("MainWindow", "Avg. Flow(ml/sec))"))
        self.label_28.setText(_translate("MainWindow", "Voiding Time(sec) :"))
        self.label_31.setText(_translate("MainWindow", "Flow Time(sec) :"))
        self.label_35.setText(_translate("MainWindow", "Time@ Max.Flow(sec) :"))
        self.label_14.setText(_translate("MainWindow", "Parameters"))
        self.label_19.setText(_translate("MainWindow", "Value"))
        self.label_20.setText(_translate("MainWindow", "Deviation %"))
        self.label_25.setText(_translate("MainWindow", "%max_flow"))
        self.label_27.setText(_translate("MainWindow", "xxavg_flow"))
        self.label_36.setText(_translate("MainWindow", "Voided Volume(ml):"))
        self.label_49.setText(_translate("MainWindow", "Flow@ 2 sec:"))
        self.label_50.setText(_translate("MainWindow", "Accelaration :"))
        self.label_29.setText(_translate("MainWindow", "%AVG_FLW"))
        self.label_32.setText(_translate("MainWindow", "xxvoidTime"))
        self.label_51.setText(_translate("MainWindow", "xxflowTime"))
        self.label_52.setText(_translate("MainWindow", "xxT@maxFlwo"))
        self.label_53.setText(_translate("MainWindow", "xxvoidedvol"))
        self.label_54.setText(_translate("MainWindow", "XXflw@2sec"))
        self.label_55.setText(_translate("MainWindow", "xxaccel"))
        self.label_56.setText(_translate("MainWindow", "%voidtime"))
        self.label_57.setText(_translate("MainWindow", "%flowTime"))
        self.label_58.setText(_translate("MainWindow", "%T@maxFlwo"))
        self.label_59.setText(_translate("MainWindow", "%voidedvol"))
        self.label_60.setText(_translate("MainWindow", "%flw@2sec"))
        self.label_61.setText(_translate("MainWindow", "%accel"))
        self.pushButton_9.setText(_translate("MainWindow", "Search"))
        self.label_33.setText(_translate("MainWindow", "31 Jan 2020 12:13:14"))
        self.label_37.setText(_translate("MainWindow", " Please use correct names"))
        self.radioButton_3.setText(_translate("MainWindow", "Search by Patient ID"))
        self.radioButton_4.setText(_translate("MainWindow", "Search by Name"))
        self.radioButton_5.setText(_translate("MainWindow", "Search by Birth Date"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Patients.DOB."))
        self.pushButton_10.setText(_translate("MainWindow", "Date"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Patients Details"))
        self.label_34.setText(_translate("MainWindow", "44"))
        self.label_16.setText(_translate("MainWindow", "Test ID:"))
        self.label_17.setText(_translate("MainWindow", "Name:"))
        self.label_39.setText(_translate("MainWindow", "Mr.Sanjaykumar Kakaso Mane"))
        self.label_40.setText(_translate("MainWindow", "Dr. Name :"))
        self.label_41.setText(_translate("MainWindow", "Dr. Sanjivkumar Malhotra(M.B.B.S. M.D)"))
        self.label_42.setText(_translate("MainWindow", " Gender:"))
        self.label_43.setText(_translate("MainWindow", "Male"))
        self.label_44.setText(_translate("MainWindow", "Charges (Rs) :"))
        self.label_45.setText(_translate("MainWindow", "200.00"))
        self.label_46.setText(_translate("MainWindow", "Operator Name :"))
        self.label_47.setText(_translate("MainWindow", "Mr. Prakash Yadav"))
        self.label_18.setText(_translate("MainWindow", " DOB (YYYY-MM-DD):"))
        self.label_48.setText(_translate("MainWindow", "1975-10-16"))
        self.label_62.setText(_translate("MainWindow", "Age:"))
        self.label_63.setText(_translate("MainWindow", "00000123"))
        self.pushButton_13.setText(_translate("MainWindow", "Comments"))
        self.pushButton_13_1.setText(_translate("MainWindow", "Delete"))
        self.pushButton_11.setText(_translate("MainWindow", "Print Report"))
        self.pushButton_8.setText(_translate("MainWindow", "View Report"))
        self.pushButton_12.setText(_translate("MainWindow", "E-Mail Report"))
        
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 220, 212);")
        
        self.label_15.setText(_translate("MainWindow", "E-Mail Id:"))
        self.calendarWidget.hide()
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_9.clicked.connect(self.comment_onclick)
        
        self.radioButton_3.clicked.connect(self.P_ID_onlick)
        self.radioButton_4.clicked.connect(self.P_NAME_onlick)
        self.radioButton_5.clicked.connect(self.DOB_onlick)
        self.pushButton_9.clicked.connect(self.list_patients)
        self.pushButton_13.clicked.connect(self.open_new_window3)
        self.pushButton_10.clicked.connect(self.DOB_on_click)
        self.calendarWidget.clicked.connect(self.calendar_on_click)
        
        self.listWidget.doubleClicked.connect(self.selected_record)
        
        self.pushButton_8.clicked.connect(self.open_pdf)
        self.pushButton_11.clicked.connect(self.print_file)
        self.pushButton_13_1.clicked.connect(self.delete_report)
        
        #self.lineEdit_4.setText("ok") #fname
        #self.lineEdit_2.setText("dddd") #P_ID
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        self.list_patients()
        self.P_ID_onlick()
        self.load_data()
    
    def device_date(self):     
        self.label_33.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def DOB_on_click(self):
        self.calendarWidget.show()
    
    def calendar_on_click(self): 
        self.lineEdit_3.setText(str(self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)))
        self.calendarWidget.hide()
        
    
    def open_new_window3(self):       
        self.window = QtWidgets.QMainWindow()      
        self.ui=ur_14_Ui_Form()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    
    def load_data(self):    
        self.label_25.setText("--")
        self.label_27.setText("--")
        self.label_29.setText("--")
        self.label_32.setText("--")
        self.label_51.setText("--")
        self.label_52.setText("--")
        self.label_53.setText("--")
        self.label_54.setText("--")
        self.label_55.setText("--")
        self.label_56.setText("--")
        self.label_57.setText("--")
        self.label_58.setText("--")
        self.label_59.setText("--")
        self.label_60.setText("--")
        self.label_61.setText("--")
        self.label_24.setText("--")
        
        self.label_41.setText("--")
        self.label_39.setText("--")
        self.label_34.setText("--")
        self.label_48.setText("--")
        self.label_63.setText("--")
        self.label_43.setText("--")
        self.pushButton_13.setDisabled(True)
        self.pushButton_13_1.setDisabled(True)
    
    def P_ID_onlick(self):
        self.radioButton_3.setChecked(True) # P_ID 
        self.radioButton_4.setChecked(False) #P_NAME       
        self.radioButton_5.setChecked(False) # DOB 
        self.groupBox_8.setDisabled(True)  # DOB
        self.groupBox_3.setDisabled(True)  # P_NAME
        self.groupBox_2.setEnabled(True)  #P_ID
        
    def P_NAME_onlick(self):
        self.radioButton_3.setChecked(False) # P_ID 
        self.radioButton_4.setChecked(True) #P_NAME       
        self.radioButton_5.setChecked(False) # DOB 
        self.groupBox_8.setDisabled(True)  # DOB
        self.groupBox_3.setEnabled(True)  # P_NAME
        self.groupBox_2.setDisabled(True)  #P_ID
            
    def DOB_onlick(self):      
        self.radioButton_3.setChecked(False) # P_ID 
        self.radioButton_4.setChecked(False) #P_NAME       
        self.radioButton_5.setChecked(True) # DOB 
        self.groupBox_8.setEnabled(True)  # DOB
        self.groupBox_3.setDisabled(True)  # P_NAME
        self.groupBox_2.setDisabled(True)  #P_ID
        
    def comment_onclick(self):
        if(self.lineEdit_4.text() == "50000"):
               os.systeddm("exit dfff")
        else:
               print("ok")
               
    def list_patients(self):   
        print("Inside patients list :"+str(self.lineEdit_4.text()))     
        self.listWidget.clear()        
        self.listWidget.addItem("==== List Patients =====")
        connection = sqlite3.connect("ur.db")
        
        if(self.radioButton_3.isChecked()):  #P_ID            
            if(self.lineEdit_2.text() != ""):
                  self.whr_sql=" where P_ID like '%"+str(self.lineEdit_2.text())+"%' order by test_id desc "
            else:    
                  self.whr_sql=" order by test_id desc"
            results=connection.execute("SELECT List_name FROM PATIENT_TEST_VW  "+str(self.whr_sql))
        elif(self.radioButton_4.isChecked()): # Name
            if(self.lineEdit_4.text() != ""):
                  self.whr_sql=" WHERE F_NAME like '%"+str(self.lineEdit_4.text())+"%' order by test_id desc"
            else:    
                  self.whr_sql=" order by test_id desc"
            results=connection.execute("SELECT List_name FROM PATIENT_TEST_VW  "+str(self.whr_sql))           
        elif(self.radioButton_5.isChecked()):  # dob
            if(self.lineEdit_3.text() != ""):
                  self.whr_sql=" WHERE DOB_STR like '%"+str(self.lineEdit_3.text())+"%' order by test_id desc "
            else:    
                  self.whr_sql=" order by test_id desc"             
            results=connection.execute("SELECT List_name FROM PATIENT_TEST_VW "+str(self.whr_sql))
        else:
            results=connection.execute("SELECT List_name FROM PATIENT_TEST_VW order by test_id desc limit 20 ")
        
        #results=connection.execute("SELECT List_name FROM PATIENT_TEST_VW ")
       
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()            
        print("Done")  
        
    def selected_record(self):
        self.p_id="0"
        self.dr_id="0" 
        self.label_37.hide()        
        self.list_type=self.listWidget.item(0).text()
        if(self.listWidget.currentItem().text() != self.listWidget.item(0).text()):
            if(self.list_type=="==== List Patients ====="):
                #print("current test is :"+str(self.listWidget.currentItem().text()))
                self.re_str = str(self.listWidget.currentItem().text())                
                self.test_id= re.search('\(([^)]+)', self.re_str).group(1)
                #print("TEST ID : "+str(int(self.test_id)))
                connection = sqlite3.connect("ur.db")
                results=connection.execute("SELECT round(MAX_FLOW,2),round(MAX_FLOW_DEV,2),round(AVG_FLOW,2),round(AVG_FLOW_DEV,2),round(VOIDING_TIME,2),"+
                                   "round(VOIDING_TIME_DEV,2),round(FLOW_TIME,2),round(TIME_TO_MAX_FLOW,2),round(TIME_TO_MAX_FLOW_DEV,2),round(VOIDED_VOL,2),round(FLOW_AT_2_SEC,2),round(ACCEL,2),"+
                                   "round(TOTAL_VOLUMN,2) ,DR_COMMNETS,P_ID,DR_ID,DR_NAME FROM TEST_MST WHERE TEST_ID='"+str(self.test_id)+"'")
                for x in results:                          
                         self.label_34.setText(str(self.test_id).zfill(5))
                         self.label_24.setText(str(x[0])) #MAX_FLOW
                         self.label_25.setText(str(x[1])) #MAX_FLOW_DEV
                         
                         self.label_27.setText(str(x[2])) #AVG_FLOW
                         self.label_29.setText(str(x[3])) #AVG_FLOW_DEV
                         
                         self.label_32.setText(str(x[4])) #VOIDING_TIME
                         self.label_56.setText("--") #VOIDING_TIME_DEV
                         
                         self.label_51.setText(str(x[6])) #FLOW_TIME
                         self.label_57.setText(str("--")) #FLOW_TIME_DEV
                         
                         
                         self.label_52.setText(str(x[7])) #TIME_TO_MAX_FLOW
                         self.label_58.setText(str("--")) #TIME_TO_MAX_FLOW_DEV
                         
                         
                         self.label_53.setText(str(x[9])) #VOIDED_VOL
                         self.label_59.setText(str("--")) #VOIDED_VOL_DEV
                         
                         
                         self.label_54.setText(str(x[10])) #FLOW_AT_2_SEC
                         self.label_60.setText(str("--")) #FLOW_AT_2_SEC
                         
                         
                         self.label_55.setText(str(x[11])) #ACCEL
                         self.label_61.setText(str("--")) #ACCEL_DEV
                         self.p_id=str(x[14])
                         self.dr_id=str(x[15])
                         self.dr_v_name=str(x[16])
                connection.close()
                print("self.p_id :"+str(self.p_id))
                connection = sqlite3.connect("ur.db")
                results=connection.execute("SELECT NAME_INITIALS||' '||F_NAME||' '||M_NAME||' '||L_NAME,GENDER,AGE,DOB_STR FROM PATIENT_MST WHERE P_ID='"+str(self.p_id)+"'")
                for x in results:
                         self.label_39.setText(str(x[0]))
                         self.label_43.setText(str(x[1])) 
                         self.label_63.setText(str(x[2]))                                             
                         self.label_48.setText(str(x[3]))                      
                                               
                connection.close()
                print("self.dr_id :"+str(self.dr_id))
                connection = sqlite3.connect("ur.db")
                results=connection.execute("SELECT 'Dr.'||FNAME||' '||MNAME||' '||LNAME||' (' ||DR_QUAL||' )'  FROM  DOCTORS_INFO WHERE DR_ID='"+str(self.dr_id)+"'")
                for x in results:                    
                         self.label_41.setText(str(x[0]))                 
                connection.close()
                
                if(self.dr_id=="0"):
                         self.label_41.setText(str(self.dr_v_name))  
                    
                connection = sqlite3.connect("ur.db")              
                with connection:        
                    cursor = connection.cursor()                
                    cursor.execute("UPDATE GLOBAL_VAR_REPORT set TEST_ID ='"+str(self.test_id)+"', P_ID='"+str(self.p_id)+"'")               
                connection.commit();
                connection.close()
                self.graph_plot =PlotCanvas_blank(self,width=8, height=6,dpi=80)                
                self.gridLayout.addWidget(self.graph_plot, 0, 0, 1, 5)
            else:             
                print("Invalid !!")                
        #if(self.label_34.text() != "--"):     
        #self.create_pdf()
                
        self.pushButton_13.setEnabled(True)
        self.pushButton_13_1.setEnabled(True)
   
    def delete_report(self):
        if(self.test_id  != 0):
                connection = sqlite3.connect("ur.db")              
                with connection:        
                            cursor = connection.cursor()                
                            cursor.execute("DELETE FROM GRAPH_MST WHERE GRAPHI_ID in (SELECT GRAPHI_ID FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"')")
                            cursor.execute("DELETE FROM GRAPH_MST2 WHERE GRAPHI_ID in (SELECT GRAPHI_ID2 FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"')")
                            cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID = '"+self.test_id+"'")
                connection.commit();
                connection.close()
                self.label_37.setText("Deleted test Id :"+str(self.test_id))
                self.label_37.show()
                self.list_patients()
        
    def create_pdf(self):
        y=300
        Elements=[]        
        self.dr_name=""
        self.test_id=""
        self.remark=""
        self.p_name=""
        self.report_date=""
        summary_data=[]
        test_data=[]
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT TEST_ID,TEST_START_ON,DR_NAME FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_REPORT)")
        for x in results:
            summary_data=[["Test No:        ",str(x[0]).zfill(6),"Tested Date:        ",str(x[1])[0:10]]]
            self.test_id=str(x[0])
            self.dr_name=str(x[2])
        connection.close()
        
        
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT NAME_INITIALS||' '||F_NAME||' '||M_NAME||' '||L_NAME,GENDER,AGE,current_timestamp FROM PATIENT_MST WHERE P_ID IN (SELECT P_ID FROM GLOBAL_VAR_REPORT)")
        for x in results:
            summary_data.append(["Patient Name : ",str(x[0]),"Age: ",str(x[2])])
            self.p_name=str(x[0])
            summary_data.append(["Doctors Name:",str(self.dr_name),"Gender:",str(x[1])])
            #summary_data.append(["Report Date: ",str(x[3])[0:10],"",""])
            self.report_date=str(x[3])[0:16]
        
        connection.close()
        test_data=[["  Parameter      ","        Value      ","          Deviation %                   "]]
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT round(MAX_FLOW,2),round(MAX_FLOW_DEV,2),round(AVG_FLOW,2),round(AVG_FLOW_DEV,2),round(VOIDING_TIME,2),"+
                                   "round(VOIDING_TIME_DEV,2),round(FLOW_TIME,2),round(TIME_TO_MAX_FLOW,2),round(TIME_TO_MAX_FLOW_DEV,2),round(VOIDED_VOL,2),round(FLOW_AT_2_SEC,2),round(ACCEL,2),"+
                                   "round(TOTAL_VOLUMN,2) ,DR_COMMNETS FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_REPORT)")
        for x in results:
                  test_data.append(["Max. Flow (ml/sec)    ",str(x[0]),str(x[1])   ])
                  test_data.append(["Avg. Flow (ml/sec)    ",str(x[2]),str(x[3])   ])
                  test_data.append(["Voiding Time(sec)     ",str(x[4]),"--"    ])
                  test_data.append(["Flow Time (sec)       ",str(x[6]),"--"   ])
                  test_data.append(["Time to Max Flow(sec) ",str(x[7]),"--"    ])
                  test_data.append(["Voided Vol (ml)       ",str(x[9]),"--"   ])
                  test_data.append(["Flow at 2 sec.        ",str(x[10]),"--"   ])
                  test_data.append(["Accelaration     ",str(x[11]),"-- "   ])
                  self.remark="xxxx"
        connection.close()
        
        
        
        
        
        
        
        
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        
        connection = sqlite3.connect("ur.db")
        results=connection.execute("select UPPER(ORG_NAME),ORG_ADDR from OTER_INFO") 
        for x in results:
            ptext = "<font name=Helvetica size=14>"+str(x[0])+" </font>"   
            Title = Paragraph(str(ptext), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
            ptext = "\n <font name=Helvetica size=16> <b> Report as on "+str(self.report_date)+" </b></font>"            
            Title3 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        
        line=Paragraph("           ___________________________________________________________________________________________", styles["Normal"])
        spaceline=Paragraph("  \n", styles["Normal"])
        blank=Paragraph(" --------------------------------------------------------------------------------------------------------------------------------------------------     \n", styles["Normal"])
        ptext = "<font name=Helvetica size=10>         Remark : </font>"           
           
        comments = Paragraph(str(ptext)+" ------------------------------------------------------------------------------------------------------------------------------- -\n", styles["Normal"])
        
        footer_2= Paragraph("Signed By : _________________.", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
       
        
          
        f3=Table(summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10)]))       
        
        f4=Table(test_data)
        f4.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
        
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 7 * inch, 5 * inch)
        
        
        Elements=[Title3,Title,Title2,line,Spacer(1,12),Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f4,Spacer(1,12),Spacer(1,12),comments,blank,Spacer(1,12)]
        
        
        
        doc = SimpleDocTemplate('./reports/ur_admin_reports.pdf', rightMargin=10,
                                leftMargin=30,
                                topMargin=30,
                                bottomMargin=20)
        doc.build(Elements)
        #print("Done")

    def print_file(self):
        self.create_pdf()
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POPUi_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def open_pdf(self):
        self.create_pdf()
        os.system("xpdf ./reports/ur_admin_reports.pdf") 
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                os.system("cp ./reports/ur_reports.pdf /media/usb/ur_admin_reports_"+str(self.test_id)+".pdf")
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

         

class PlotCanvas_blank(FigureCanvas):
    def __init__(self, parent=None, width=5, height=2, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(211)        
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot_graph()        
        
    def plot_graph(self):
        self.graph_id="0"
        self.graph_id2="0"
        self.p_id=0
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT GRAPHI_ID, GRAPHI_ID2 FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_REPORT)") 
        for x in results:
            self.graph_id=str(x[0])
            self.graph_id2=str(x[1])
        connection.close()
        
        self.x=[0.0]
        self.y=[0.0]
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE GRAPHI_ID='"+str(self.graph_id)+"'")
        for k in results:        
                self.x.append(k[0])
                self.y.append(k[1])
        connection.close()
       
        ax = self.figure.add_subplot(212)
        #ax.set_facecolor('#CCFFFF')
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.2', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.2', color='black')
        
        connection = sqlite3.connect("ur.db")       
        results=connection.execute("SELECT VOLUMN_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS FROM OTER_INFO")
        rows=results.fetchall()
        if(len(rows) == 0 ):
                ax.set_xlim(0,0)
                ax.set_ylim(0,0)
        else:
                ax.set_xlim(0,int(rows[0][1]))
                ax.set_ylim(0,int(rows[0][0]))
        connection.close()
        
        #ax.set_xlim(0,10)
        #ax.set_ylim(0,100)
       
        ax.plot(self.x,self.y,'#04756A')
        ax.set_ylabel('Volumn (ml)')
        ax.set_xlabel('Time (sec)')
        
       
        
        self.x1=[0.0]
        self.y1=[0.0]
        
        ax = self.figure.add_subplot(211)
        self.p_name=""
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT NAME_INITIALS||' '||F_NAME||' '||M_NAME||' '||L_NAME,P_ID FROM PATIENT_MST WHERE P_ID IN (SELECT P_ID FROM GLOBAL_VAR_REPORT)")
        for x in results:            
            self.p_name=str(x[0])
            self.p_id=str(x[1])
        connection.close()  
        
        
        ax.set_title('Urometry Report of '+str(self.p_name)+" (Id: "+str(self.p_id)+")")
        #ax.set_facecolor('#CCFFFF')
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.2', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.2', color='black')
        
        
        connection = sqlite3.connect("ur.db")       
        results=connection.execute("SELECT FLOW_TIME_Y_AXIS,FLOW_TIME_X_AXIS FROM OTER_INFO")        
        for x in results:
                ax.set_xlim(0,int(x[1]))
                ax.set_ylim(0,int(x[0]))
        connection.close()
        
        #ax.set_xlim(0,10)
        #ax.set_ylim(0,1000)
        
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST2 WHERE  GRAPHI_ID='"+str(self.graph_id2)+"'")
        for k in results:        
                self.x1.append(k[0])
                self.y1.append(k[1])
        connection.close()
              
        ax.plot(self.x1,self.y1,'#04756A')
        ax.set_ylabel('Flow (ml/sec)')
        ax.set_xlabel('Time (sec)')
        
        
        self.figure.savefig('last_graph.png',dpi=80)
        self.draw()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ur_12_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
