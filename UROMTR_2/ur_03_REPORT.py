# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ur_02_TEST_P3.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
#from ur_01_TEST_P1 import ur_01_Ui_MainWindow
from ur_07_patients_dtls import ur_07_Ui_Form
from print_popup import P_POPUi_MainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


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

class ur_03_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1341, 711))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graph_id=""
        self.graph_id2=""
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(20, 620, 101, 71))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/backword1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(100, 100))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(140, 620, 101, 71))
        self.toolButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/forword1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_2.setObjectName("toolButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 650, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 650, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(840, 650, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(610, 50, 701, 581))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(20, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(380, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(490, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(20, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(140, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(20, 480, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setGeometry(QtCore.QRect(20, 70, 541, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setGeometry(QtCore.QRect(20, 130, 541, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(30, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(410, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(230, 90, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        self.label_31.setGeometry(QtCore.QRect(240, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        self.label_32.setGeometry(QtCore.QRect(410, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(20, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_33 = QtWidgets.QLabel(self.groupBox_2)
        self.label_33.setGeometry(QtCore.QRect(240, 200, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox_2)
        self.label_34.setGeometry(QtCore.QRect(410, 200, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(20, 240, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("")
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_35 = QtWidgets.QLabel(self.groupBox_2)
        self.label_35.setGeometry(QtCore.QRect(240, 240, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(20, 280, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(20, 320, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(20, 360, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(20, 400, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_36 = QtWidgets.QLabel(self.groupBox_2)
        self.label_36.setGeometry(QtCore.QRect(20, 440, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("")
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.groupBox_2)
        self.label_37.setGeometry(QtCore.QRect(240, 280, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_2)
        self.label_38.setGeometry(QtCore.QRect(240, 320, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_38.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.groupBox_2)
        self.label_39.setGeometry(QtCore.QRect(240, 360, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.groupBox_2)
        self.label_40.setGeometry(QtCore.QRect(240, 400, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_40.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.groupBox_2)
        self.label_41.setGeometry(QtCore.QRect(240, 440, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.groupBox_2)
        self.label_42.setGeometry(QtCore.QRect(410, 240, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_42.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.groupBox_2)
        self.label_43.setGeometry(QtCore.QRect(410, 310, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_43.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.groupBox_2)
        self.label_44.setGeometry(QtCore.QRect(410, 270, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.groupBox_2)
        self.label_45.setGeometry(QtCore.QRect(410, 350, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_45.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.groupBox_2)
        self.label_46.setGeometry(QtCore.QRect(410, 430, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.groupBox_2)
        self.label_47.setGeometry(QtCore.QRect(410, 390, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.groupBox_2)
        self.label_48.setGeometry(QtCore.QRect(470, 310, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_48.setText("")
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_48.setObjectName("label_48")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(170, 490, 401, 61))
        self.textEdit.setObjectName("textEdit")
        self.label_49 = QtWidgets.QLabel(self.groupBox_2)
        self.label_49.setGeometry(QtCore.QRect(220, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.groupBox_2)
        self.label_50.setGeometry(QtCore.QRect(70, 30, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(1120, 0, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 581, 591))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 2)
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
        self.pushButton_3.setText(_translate("MainWindow", "Print Report"))
        self.pushButton_4.setText(_translate("MainWindow", "Save Comments"))
        self.pushButton_5.setText(_translate("MainWindow", "View Report"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Test Report"))
        self.label_21.setText(_translate("MainWindow", "Max. Flow (ml/sec):"))
        self.label_23.setText(_translate("MainWindow", "Elapsed Time:"))
        self.label_28.setText(_translate("MainWindow", "00:03:45"))
        self.label_15.setText(_translate("MainWindow", "Test Id:"))
        self.label_17.setText(_translate("MainWindow", "Tested On:"))
        self.label_29.setText(_translate("MainWindow", "Doctors. Comment :"))
        self.label_16.setText(_translate("MainWindow", "Parameter"))
        self.label_18.setText(_translate("MainWindow", "Deviation (%)"))
        self.label_22.setText(_translate("MainWindow", "Value"))
        self.label_31.setText(_translate("MainWindow", " yymaxflow"))
        self.label_32.setText(_translate("MainWindow", "yymxflowdev%"))
        self.label_24.setText(_translate("MainWindow", "Avg. Flow (ml/sec):"))
        self.label_33.setText(_translate("MainWindow", "yyavgflow"))
        self.label_34.setText(_translate("MainWindow", "yyavgflow%"))
        self.label_20.setText(_translate("MainWindow", "Voiding Time (sec)"))
        self.label_35.setText(_translate("MainWindow", "xxvoidingtime"))
        self.label_25.setText(_translate("MainWindow", "Flow Time (sec)"))
        self.label_19.setText(_translate("MainWindow", "Time To Max Flow(sec)"))
        self.label_26.setText(_translate("MainWindow", "Voided Volumn(ml)"))
        self.label_27.setText(_translate("MainWindow", "Flow @ 2 Second"))
        self.label_36.setText(_translate("MainWindow", "Acceleration"))
        self.label_37.setText(_translate("MainWindow", "xxflowtimexx"))
        self.label_38.setText(_translate("MainWindow", "xxtimetomaxflow"))
        self.label_39.setText(_translate("MainWindow", "xxvoidedvol"))
        self.label_40.setText(_translate("MainWindow", "xxFlow @ 2 "))
        self.label_41.setText(_translate("MainWindow", "xx15"))
        self.label_42.setText(_translate("MainWindow", "%vodT"))
        self.label_43.setText(_translate("MainWindow", "%tmaxflw"))
        self.label_44.setText(_translate("MainWindow", "%flwT"))
        self.label_45.setText(_translate("MainWindow", "%vodvol"))
        self.label_46.setText(_translate("MainWindow", "%accel"))
        self.label_47.setText(_translate("MainWindow", "%fl2sec"))
        self.label_49.setText(_translate("MainWindow", "16-10-2020 12:14"))
        self.label_50.setText(_translate("MainWindow", " 00099"))
        self.label_30.setText(_translate("MainWindow", "16 Jan 2020 12:14:15"))
        self.pushButton_2.setText(_translate("MainWindow", "View Patients Details"))
        self.label_2.setText(_translate("MainWindow", " Comment Saved Successfully ...."))
        self.toolButton_2.hide()
        self.label_2.hide()
        self.graph_plot =PlotCanvas_blank(self,width=8, height=6,dpi=80)                
        self.gridLayout.addWidget(self.graph_plot, 1, 0, 1, 2)
        self.toolButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.open_new_window3)
        self.pushButton_4.clicked.connect(self.save_commnets)
        self.pushButton_5.clicked.connect(self.open_pdf)
        self.pushButton_3.clicked.connect(self.print_file)        
        self.load_data()
        self.create_pdf()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
    
    def device_date(self):     
        self.label_30.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))    
        
        
        
    def load_data(self):
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT TEST_ID,TEST_START_ON,ELAPSED_TIME,round(MAX_FLOW,2),round(MAX_FLOW_DEV,2),round(AVG_FLOW,2),round(AVG_FLOW_DEV,2),round(VOIDING_TIME,2),"+
                                   "round(VOIDING_TIME_DEV,2),round(FLOW_TIME,2),round(TIME_TO_MAX_FLOW,2),round(TIME_TO_MAX_FLOW_DEV,2),round(VOIDED_VOL,2),round(FLOW_AT_2_SEC,2),round(ACCEL,2),"+
                                   "round(TOTAL_VOLUMN,2) ,DR_COMMNETS FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_TEST)") 
        for x in results:
            self.label_50.setText(str(x[0]).zfill(5))  #TEST_ID
            self.label_49.setText(str(x[1])[0:10]) #TEST_START_ON
            self.label_28.setText(str(x[2])) #ELAPSED_TIME
            self.label_31.setText(str(x[3]))#MAX_FLOW
            self.label_32.setText(str(x[4])) #MAX_FLOW_DEV
            self.label_33.setText(str(x[5]))#AVG_FLOW
            self.label_34.setText(str(x[6])) #AVG_FLOW_DEV
            self.label_35.setText(str(x[7])) #VOIDING_TIME
            self.label_37.setText(str(x[9])) #FLOW_TIME
            self.label_38.setText(str(x[10]))  #TIME_TO_MAX_FLOW
            self.label_39.setText(str(x[12])) # VOIDED_VOL
            self.label_40.setText(str(x[13])) #FLOW_AT_2_SEC
            self.label_41.setText(str(x[14])) #ACCEL
            
            # deviation values
            self.label_42.setText("--") #VOIDING_TIME_DEV
            self.label_43.setText("--") #TIME_TO_MAX_FLOW_DEV
             
            self.label_44.setText("--") #LOW TIME DEV
            self.label_45.setText("--") #VOIDED_VOL DEV
            self.label_46.setText("--")  # ACCEL DEV
            self.label_47.setText("--")  # FLOW_AT_2_SEC DEV
            self.textEdit.setText(str(x[16]))
        connection.close()
        
    def save_commnets(self):
        connection = sqlite3.connect("ur.db")              
        with connection:        
                cursor = connection.cursor()                
                cursor.execute("UPDATE TEST_MST SET DR_COMMNETS='"+self.textEdit.toPlainText()+"' ,DR_COMMENT_UPDATED_ON=current_timestamp WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_TEST)")               
        connection.commit();
        connection.close()
        print("comment saved !!")
        self.label_2.show()
        
        
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()       
        self.ui=ur_01_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window3(self):       
        self.window = QtWidgets.QMainWindow()       
        self.ui=ur_07_Ui_Form()
        self.ui.setupUi(self.window)           
        self.window.show()

 
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
        results=connection.execute("SELECT TEST_ID,TEST_START_ON,DR_NAME FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_TEST)")
        for x in results:
            summary_data=[["Test No:        ",str(x[0]).zfill(6),"Tested Date:        ",str(x[1])[0:10]]]
            self.test_id=str(x[0])
            self.dr_name=str(x[2])
        connection.close()
        
        
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT NAME_INITIALS||' '||F_NAME||' '||M_NAME||' '||L_NAME,GENDER,AGE,current_timestamp FROM PATIENT_MST WHERE P_ID IN (SELECT P_ID FROM GLOBAL_VAR_TEST)")
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
                                   "round(TOTAL_VOLUMN,2) ,DR_COMMNETS FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_TEST)")
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
        
        
        
        doc = SimpleDocTemplate('./reports/ur_reports.pdf', rightMargin=10,
                                leftMargin=30,
                                topMargin=30,
                                bottomMargin=20)
        doc.build(Elements)
        #print("Done")

    def print_file(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POPUi_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def open_pdf(self):        
        os.system("xpdf ./reports/ur_reports.pdf") 
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                os.system("cp ./reports/ur_reports.pdf /media/usb/ur_reports_"+str(self.test_id)+".pdf")
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
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT GRAPHI_ID, GRAPHI_ID2 FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_TEST)") 
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
        results=connection.execute("SELECT NAME_INITIALS||' '||F_NAME||' '||M_NAME||' '||L_NAME,GENDER,AGE,current_timestamp FROM PATIENT_MST WHERE P_ID IN (SELECT P_ID FROM GLOBAL_VAR_TEST)")
        for x in results:            
            self.p_name=str(x[0])
        connection.close()  
        
        
        ax.set_title('Urometry Report of '+str(self.p_name))
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
    ui = ur_03_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
