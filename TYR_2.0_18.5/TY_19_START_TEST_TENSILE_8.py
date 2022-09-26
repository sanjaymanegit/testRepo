


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from print_test_popup import P_POP_TEST_Ui_MainWindow
from email_popup_test_report import popup_email_test_Ui_MainWindow
from comment_popup import comment_Ui_MainWindow


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




class TY_19_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1341, 711))
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
        self.label_20.setGeometry(QtCore.QRect(1100, 10, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 450, 571, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 1341, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(0, 100, 571, 20))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 160, 571, 20))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(0, 220, 571, 20))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(0)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(0, 270, 571, 20))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(0)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(0, 330, 571, 20))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(0)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(0, 390, 571, 20))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(0)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.frame)
        self.line_9.setGeometry(QtCore.QRect(253, 60, 20, 651))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setGeometry(QtCore.QRect(560, 60, 20, 651))
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setObjectName("line_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(100, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(70, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(60, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)
        self.lineEdit.setValidator(input_validator)
        self.lineEdit.setStyleSheet("color: rgb(170, 0, 127);")
        self.lineEdit.setGeometry(QtCore.QRect(300, 70, 81, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_2)
        self.lineEdit_2.setValidator(input_validator)
        self.lineEdit_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 70, 81, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(410, 80, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
        self.lineEdit_3.setValidator(input_validator)
        self.lineEdit_3.setStyleSheet("color: rgb(170, 0, 127);")
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 130, 81, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(60, 190, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_4)
        self.lineEdit_4.setValidator(input_validator)
        self.lineEdit_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 190, 81, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(50, 240, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(300, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(40, 300, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        #self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.label_17)
        self.label_17.setValidator(input_validator)
        self.label_17.setGeometry(QtCore.QRect(300, 300, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(50, 660, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(360, 660, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(410, 600, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_7)
        self.lineEdit_7.setValidator(input_validator)
        self.lineEdit_7.setStyleSheet("color: rgb(170, 0, 127);")
        self.lineEdit_7.setGeometry(QtCore.QRect(450, 590, 101, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(280, 660, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(490, 660, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(160, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        
        self.label_31_1 = QtWidgets.QLabel(self.frame)
        self.label_31_1.setGeometry(QtCore.QRect(260, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_31_1.setFont(font)
        self.label_31_1.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_31_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31_1.setObjectName("label_31_1")
        
        self.lineEdit_31_2 = QtWidgets.QLineEdit(self.frame) 
        self.lineEdit_31_2.setGeometry(QtCore.QRect(370, 10, 101, 31))
        self.lineEdit_31_2.setObjectName("lineEdit_31_2")
        
        self.label_31_3 = QtWidgets.QLabel(self.frame)
        self.label_31_3.setGeometry(QtCore.QRect(480, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_31_3.setFont(font)
        self.label_31_3.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_31_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31_3.setObjectName("label_31_3")
        
        self.lineEdit_31_3 = QtWidgets.QLineEdit(self.frame)       
        self.lineEdit_31_3.setGeometry(QtCore.QRect(570, 10, 101, 31))
        self.lineEdit_31_3.setObjectName("lineEdit_31_3")
        
        self.line_12 = QtWidgets.QFrame(self.frame)
        self.line_12.setGeometry(QtCore.QRect(0, 510, 571, 20))
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(0)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.frame)
        self.line_13.setGeometry(QtCore.QRect(0, 570, 571, 20))
        self.line_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_13.setLineWidth(0)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.frame)
        self.line_14.setGeometry(QtCore.QRect(0, 630, 571, 20))
        self.line_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_14.setLineWidth(0)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setObjectName("line_14")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(50, 360, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLineEdit(self.frame)
        self.label_34.setGeometry(QtCore.QRect(290, 350, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(50, 420, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLineEdit(self.frame)
        self.label_27.setGeometry(QtCore.QRect(290, 420, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(50, 480, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_5)
        self.lineEdit_5.setValidator(input_validator)
        self.lineEdit_5.setStyleSheet("color: rgb(170, 0, 127);")
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 470, 101, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(50, 540, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(290, 530, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(50, 590, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_6)
        self.lineEdit_6.setValidator(input_validator)
        self.lineEdit_6.setStyleSheet("color: rgb(170, 0, 127);")
        self.lineEdit_6.setGeometry(QtCore.QRect(280, 590, 101, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(1110, 670, 81, 31))
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setProperty("value", 100.0)
        self.lcdNumber.setProperty("intValue", 100)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(1110, 630, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_2.setGeometry(QtCore.QRect(990, 670, 71, 31))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_2.setProperty("intValue", 100)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(990, 630, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 670, 81, 31))
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
        self.pushButton_4.setGeometry(QtCore.QRect(590, 630, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(700, 630, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(870, 670, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(700, 670, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(870, 630, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(580, 80, 741, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_35 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(750, 10, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)        
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        #self.comboBox_2.addItem("")
        
        
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(1220, 650, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.goAhead="Yes"
        self.test_id_exist="No"
        self.timer3=QtCore.QTimer()
        self.sc_blank=""
        self.yeild_strength=""
        self.shape=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", datetime.datetime.now().strftime("%B  %d , %Y %I:%M ")+""))
        self.label_11.setText(_translate("MainWindow", "TEST ID :"))
        self.label_12.setText(_translate("MainWindow", "001"))
        self.label_9.setText(_translate("MainWindow", "Initial Size (mm)"))
        self.label_10.setText(_translate("MainWindow", "Initial Area (mm2)"))
        self.label_8.setText(_translate("MainWindow", "*"))
        self.label_13.setText(_translate("MainWindow", "Gauge Length (mm)"))
        self.label_14.setText(_translate("MainWindow", "Tensile Strength (Mpa)"))
        self.label_15.setText(_translate("MainWindow", "0.00"))
        self.label_16.setText(_translate("MainWindow", "Yeild Strength (Mpa)"))
        self.label_17.setText(_translate("MainWindow", "0.00"))
        self.label_24.setText(_translate("MainWindow", "Final Area (mm²)"))
        self.label_25.setText(_translate("MainWindow", "Reduction Area % :"))
        self.label_28.setText(_translate("MainWindow", "*"))
        self.label_30.setText(_translate("MainWindow", "12.47"))
        self.label_32.setText(_translate("MainWindow", "53.14"))
        self.label_31.setText(_translate("MainWindow", "(Rectangle)"))
        self.label_31_1.setText(_translate("MainWindow", "Sr.No :"))
        self.label_31_3.setText(_translate("MainWindow", "Location :"))
        
        self.label_33.setText(_translate("MainWindow", "Item Description :"))
        self.label_34.setText(_translate("MainWindow", ""))
        self.label_26.setText(_translate("MainWindow", "Coil.ID"))
        self.label_27.setText(_translate("MainWindow", "")) #coid ID
        self.label_21.setText(_translate("MainWindow", "Final Length (mm)"))
        self.label_22.setText(_translate("MainWindow", "Elongation %"))
        self.label_29.setText(_translate("MainWindow", "25"))
        self.label_23.setText(_translate("MainWindow", "Final Size (mm)"))
        self.label_18.setText(_translate("MainWindow", "Stress (MPa) :"))
        self.label_19.setText(_translate("MainWindow", "Strain (%) :"))
        self.pushButton_3.setText(_translate("MainWindow", "E-Mail"))
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.pushButton_13.setText(_translate("MainWindow", "View Report"))
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setText(_translate("MainWindow", "Save"))
        
        self.pushButton_15.setText(_translate("MainWindow", "Print Report"))
        self.pushButton_15.setDisabled(True)
        self.pushButton_16.setText(_translate("MainWindow", "Remark"))
        self.pushButton_16.setDisabled(True)
        self.label_35.setText(_translate("MainWindow", "Please click on START button to start test"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Mechanical Testing Report - Cylinder Parent Material"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Mechanical Testing Report - Welding Sample"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Mechanical Testing Report - Raw Material"))
        #self.comboBox_2.setItemText(3, _translate("MainWindow", "MPa/mm"))
        self.pushButton_17.setText(_translate("MainWindow", "RETURN"))
        self.pushButton_17.clicked.connect(MainWindow.close)
        
        self.pushButton_13.clicked.connect(self.open_pdf)
        self.pushButton_15.clicked.connect(self.print_file)
        self.pushButton_3.clicked.connect(self.open_email_report)
        self.pushButton_16.clicked.connect(self.open_comment_popup)
        self.pushButton_14.clicked.connect(self.validation)
        
        self.reset()
        self.load_data()
        if(self.label_31.text() == "(Rectangle)"):
                self.thickness_onChange()
                self.lineEdit.textChanged.connect(self.thickness_onChange)
                self.lineEdit_2.textChanged.connect(self.width_onChange)
                self.f_thickness_onChange()
                self.lineEdit_6.textChanged.connect(self.f_thickness_onChange)
                self.lineEdit_7.textChanged.connect(self.f_width_onChange)
        else:
                self.diameter_onChange()
                self.lineEdit.textChanged.connect(self.diameter_onChange)
                self.f_diameter_onChange()
                self.lineEdit_6.textChanged.connect(self.f_diameter_onChange)
                
        
        self.final_length_onChange()
        self.lineEdit_5.textChanged.connect(self.final_length_onChange)
        self.lineEdit_4.textChanged.connect(self.final_length_onChange)
        self.pushButton_4.clicked.connect(self.start_test_tensile_8)
        self.comboBox_2.currentTextChanged.connect(self.onchage_combo)
    
    def onchage_combo(self):                      
        if(self.comboBox_2.currentText() == "Mechanical Testing Report - Raw Material"):
                self.label_31_1.setText("Heat Number :")
                self.label_31_3.setText("Supplier :")        
        else:
                self.label_31_1.setText("Sr.No :")
                self.label_31_3.setText("Location :")
                
        
    def reset(self):        
        if(self.timer3.isActive()): 
           self.timer3.stop() 
        
        self.sc_blank =PlotCanvas_blank(self) 
        self.gridLayout.addWidget(self.sc_blank, 1, 0, 1, 1)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber_2.setProperty("value", 0.0)
        
    
    def load_data(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  NEW_TEST_SPE_SHAPE,IFNULL(NEW_TEST_THICKNESS,0),IFNULL(NEW_TEST_WIDTH,0),IFNULL(NEW_TEST_DIAMETER,0),IFNULL(NEW_TEST_GUAGE_MM,0),NEW_TEST_SPECIMEN_NAME FROM GLOBAL_VAR") 
        for x in results:
            self.shape=str(x[0])
            self.label_31.setText("("+str(x[0])+")")
            if(self.label_31.text() == "(Rectangle)"):
                    self.lineEdit.setText(str(x[1]))
                    self.lineEdit_6.setText(str(x[1]))
            else:       
                    self.lineEdit.setText(str(x[3]))
                    self.lineEdit_6.setText(str(x[3]))
            self.lineEdit_2.setText(str(x[2]))
            self.lineEdit_4.setText(str(x[4]))
            self.lineEdit_5.setText(str(x[4]))
            
           
            self.lineEdit_7.setText(str(x[2]))
            #self.label_27.setText(str(x[5]))
            
            
        connection.close()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select seq from sqlite_sequence WHERE name = 'TEST_MST'")       
        for x in results:           
                 self.label_12.setText(str(x[0]).zfill(3))
                 self.test_id=str(x[0])
        connection.close()
        
        
    def thickness_onChange(self):
        self.thickness=""
        self.width=""
        
        try:
            self.thickness=int(self.lineEdit.text())
        except ValueError as e:
            try:
                self.thickness=float(self.lineEdit.text())
            except ValueError as e:
                self.lineEdit_3.setText("0.00")    
                
        
        try:
            self.width=int(self.lineEdit_2.text())
        except ValueError as e:
            try:
                self.width=float(self.lineEdit_2.text())
            except ValueError as e:
                self.lineEdit_3.setText("0.00")  
        
        #print(" thickness :"+str(type(self.thickness))+" width:"+str(type(self.width)))
        #self.lineEdit_3.setText(str(float(float(int(self.thickness))*float(int(self.width)))))
        try:
            self.lineEdit_3.setText(str(round(float(self.thickness * self.width),2)))
        except ValueError as e:
            #self.lineEdit_3.setText("0.00")
            print("Caluculation error1");
        except TypeError as e:
            print("Caluculation error2");
        except:
            print("Caluculation error3");
        
        self.f_thickness_onChange()    
            
            
    def width_onChange(self):
        self.thickness=""
        self.width=""        
        try:
            self.thickness=int(self.lineEdit.text())
        except ValueError as e:
            try:
                self.thickness=float(self.lineEdit.text())
            except ValueError as e:
                self.lineEdit_3.setText("0.00") 
        try:
            self.width=int(self.lineEdit_2.text())
        except ValueError as e:
            try:
                self.width=float(self.lineEdit_2.text())
            except ValueError as e:
                self.lineEdit_3.setText("0.00")
        try:
            self.lineEdit_3.setText(str(round(float(self.thickness * self.width),2)))
        except ValueError as e:
            #self.lineEdit_3.setText("0.00")
            print("Caluculation error4");
        except TypeError as e:
            print("Caluculation error5");
        except:
            print("Caluculation error6");
        
        self.f_width_onChange()   
            
    def diameter_onChange(self):
        self.label_8.hide()
        self.label_28.hide()
        self.lineEdit_2.hide()
        self.lineEdit_7.hide()
        self.diameter="0.0"
        try:
            self.diameter=int(self.lineEdit.text())
        except ValueError as e:
            try:
                self.diameter=float(self.lineEdit.text())
            except ValueError as e:
                self.lineEdit_3.setText("0.00")
                
        try:
            self.lineEdit_3.setText(str(round(float((self.diameter * self.diameter * 3.14)/4),2)))
        except ValueError as e:
            #self.lineEdit_3.setText("0.00")
            print("Caluculation error7");
        except TypeError as e:
            print("Caluculation error8");
        except:
            print("Caluculation error9");
       
        self.f_diameter_onChange()
    
    def f_thickness_onChange(self):
        self.thickness=""
        self.width=""
        
        try:
            self.thickness=int(self.lineEdit_6.text())
        except ValueError as e:
            try:
                self.thickness=float(self.lineEdit_6.text())
            except ValueError as e:
                self.label_30.setText("0.00")    
                
        
        try:
            self.width=int(self.lineEdit_7.text())
        except ValueError as e:
            try:
                self.width=float(self.lineEdit_7.text())
            except ValueError as e:
                self.label_30.setText("0.00")  
        
        #print(" thickness :"+str(type(self.thickness))+" width:"+str(type(self.width)))
        #self.lineEdit_3.setText(str(float(float(int(self.thickness))*float(int(self.width)))))
        try:
            self.label_30.setText(str(round(float(self.thickness * self.width),2)))
        except ValueError as e:
            #self.lineEdit_3.setText("0.00")
            print("Caluculation error10");
        except TypeError as e:
            print("Caluculation error11");
        except:
            print("Caluculation error12");
        
        self.f_reduced_area_prc()
            
    def f_width_onChange(self):
        self.thickness=""
        self.width=""        
        try:
            self.thickness=int(self.lineEdit_6.text())
        except ValueError as e:
            try:
                self.thickness=float(self.lineEdit_6.text())
            except ValueError as e:
                self.label_30.setText("0.00") 
        try:
            self.width=int(self.lineEdit_7.text())
        except ValueError as e:
            try:
                self.width=float(self.lineEdit_7.text())
            except ValueError as e:
                self.label_30.setText("0.00")
        try:
            self.label_30.setText(str(round(float(self.thickness * self.width),2)))
        except ValueError as e:
            #self.lineEdit_3.setText("0.00")
            print("Caluculation error13");
        except TypeError as e:
            print("Caluculation error14");
        except:
            print("Caluculation error15");
        
        self.f_reduced_area_prc()
            
            
    def f_diameter_onChange(self):
        self.label_8.hide()
        self.lineEdit_2.hide()
        self.diameter="0.0"
        try:
            self.diameter=int(self.lineEdit_6.text())
        except ValueError as e:
            try:
                self.diameter=float(self.lineEdit_6.text())
            except ValueError as e:
                self.label_30.setText("0.00")
                
        try:
            self.label_30.setText(str(round(float((self.diameter * self.diameter * 3.14)/4),2)))
        except ValueError as e:
            #self.lineEdit_3.setText("0.00")
            print("Caluculation error16");
        except TypeError as e:
            print("Caluculation error17");
        except:
            print("Caluculation error18");
        self.f_reduced_area_prc()
    
    def f_reduced_area_prc(self):
        self.initial_area=self.lineEdit_3.text()
        self.final_area=self.label_30.text()
        if (float(self.initial_area) > float(self.final_area)):
                self.reduced_area=float(self.initial_area)-float(self.final_area)
                self.reduced_area_prc=float(float(self.reduced_area)*100/float(self.initial_area))
                self.label_32.setText(str(round(self.reduced_area_prc,0)))
                print("intial area:"+str(self.initial_area)+" finala area :"+str(self.final_area))
        else:
                self.label_32.setText("0")
    
    def final_length_onChange(self):
        self.final_length=self.lineEdit_5.text()
        self.guage_length=self.lineEdit_4.text()
        self.prc_elongation=0        
        try:
            self.final_length=int(self.lineEdit_5.text())
        except ValueError as e:
            try:
                self.final_length=float(self.lineEdit_5.text())
            except ValueError as e:
                    #self.lineEdit_3.setText("0.00")
                    print("Caluculation error19");
            except TypeError as e:
                    print("Caluculation error20");
            except:
                    print("Caluculation error21");
                
        
        try:
            self.guage_length=int(self.lineEdit_4.text())
        except ValueError as e:
            try:
                self.guage_length=float(self.lineEdit_4.text())
            except ValueError as e:                   
                    print("Caluculation error22");
            except TypeError as e:
                    print("Caluculation error23");
            except:
                    print("Caluculation error24");
                
                
                
                
        try:        
            self.elongation=self.final_length-self.guage_length
        except ValueError as e:                   
                    print("Caluculation error25");
        except TypeError as e:
                    print("Caluculation error26");
        except:
                    print("Caluculation error27");   
        
        try:
            self.prc_elongation=(self.elongation*100)/self.guage_length
            self.label_29.setText(str(round(self.prc_elongation,0))+" % ")
        
        except ValueError as e:                   
                    print("Caluculation error28");
        except TypeError as e:
                    print("Caluculation error29");
        except:
                    print("Caluculation error30");   
        
        
            
    def print_file(self):        
        #os.system("gnome-open /home/pi/TYR_2.0_18.5/reports/Reportxxx.pdf")
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POP_TEST_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
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
        
    def show_load_cell_val(self):        
        #self.label_34.setText(str(max(self.sc_new.arr_q)))   #load
        self.lcdNumber.setProperty("value", str(max(self.sc_new.arr_q)))
        
        self.lcdNumber_2.setProperty("value",str(max(self.sc_new.arr_p)))   #length
        
        if(str(self.sc_new.save_data_flg) =="Yes"):
                self.save_graph_data()
                self.sc_new.save_data_flg=""
                self.label_35.setText("Data Saved Successfully.")
                self.label_35.show()
                
    def save_graph_data(self):
         if (len(self.sc_new.arr_p) > 1):             
            connection = sqlite3.connect("tyr.db")
            with connection:        
              cursor = connection.cursor()
              for g in range(len(self.sc_new.arr_p)):                     
                        cursor.execute("INSERT INTO STG_GRAPH_MST(X_NUM,Y_NUM) VALUES ('"+str(self.sc_new.arr_p[g])+"','"+str(self.sc_new.arr_q[g])+"')")
            connection.commit();
            connection.close()
            
            self.yeild_strength="0.00"
            self.get_defarmetion_point()
            self.label_15.setText(str(round(max(self.sc_new.arr_q),2)))
            self.label_17.setText(str(self.yeild_strength))
            
            connection = sqlite3.connect("tyr.db")              
            with connection:        
                  cursor = connection.cursor()
                  #print("ok1")
                  cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"'")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_PEAK_LOAD_KG=(SELECT MAX(Y_NUM) FROM STG_GRAPH_MST)")
                  cursor.execute("UPDATE GLOBAL_VAR SET STG_E_AT_PEAK_LOAD_MM=(SELECT X_NUM FROM STG_GRAPH_MST WHERE Y_NUM=(SELECT STG_PEAK_LOAD_KG FROM GLOBAL_VAR))")
                  
                  #print("ok2")
                  cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM) SELECT X_NUM,Y_NUM FROM STG_GRAPH_MST")                  
                  cursor.execute("UPDATE GRAPH_MST SET GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0))+1 FROM GRAPH_MST) WHERE GRAPH_ID IS NULL") 
                  cursor.execute("UPDATE TEST_MST SET STATUS='LOADED GRAPH' ,GRAPH_ID=(SELECT MAX(IFNULL(GRAPH_ID,0)) FROM GRAPH_MST) WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")                  
                  cursor.execute("UPDATE TEST_MST SET GRAPH_SCAL_X_LENGTH=(SELECT GRAPH_SCALE_CELL_2 FROM SETTING_MST),GRAPH_SCAL_Y_LOAD=(SELECT GRAPH_SCALE_CELL_1 FROM SETTING_MST)  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
                  cursor.execute("UPDATE TEST_MST SET TENSILE_STRENGTH='"+str(round(max(self.sc_new.arr_q),2))+"', YEILD_STRENGTH='"+str(self.yeild_strength)+"'  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")                  
                  
            connection.commit();
            connection.close()
            print("Data Saved Ok in STG_GRAPH_MST")
            
            
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("select STG_E_AT_PEAK_LOAD_MM from GLOBAL_VAR") 
            for x in results:
                    guage_length=""
                    f_guage_length=""
                    guage_length=str(self.lineEdit_4.text())
                    f_guage_length=str((((round(float(x[0]),2))*float(guage_length))/100))
                    print("Strain :"+str(x[0])+" guage_length:"+str(guage_length)+"    converted length :"+str(f_guage_length)+" Final Length : "+str(round((float(guage_length)+float(f_guage_length)),2)))
                    self.lineEdit_5.setText(str(round((float(guage_length)+float(f_guage_length)),2)))
            connection.close()
                
    
    def get_defarmetion_point(self):
        c=0.0
        def_point=-1.00
        def_point_x=-1.00
        def_point_y=-1.00
        def_buffer_6_prc=0.0
        self.yeild_strength=""
        self.max_load_rec_id=0
#        connection = sqlite3.connect("tyr.db")        
#        results=connection.execute("SELECT max(Y_NUM) FROM STG_GRAPH_MST where X_NUM > 0 order by REC_ID ASC")
#        for x in results:
#            def_buffer_6_prc=float(x[0])*0.25            
#        connection.close()
#        
#        if(float(def_buffer_6_prc) > 0):
#               print("def_buffer_6_prc :"+str(def_buffer_6_prc))     
#        else:
#               def_buffer_6_prc=6.0

        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT max(Y_NUM) FROM STG_GRAPH_MST where X_NUM > 0 order by REC_ID ASC")
        for x in results:
            def_buffer_6_prc=float(x[0])*0.30
            self.max_load=float(x[0])
        connection.close()
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT rec_id FROM STG_GRAPH_MST where Y_NUM = '"+str(self.max_load)+"'  order by REC_ID ASC")
        for x in results:            
            self.max_load_rec_id=int(x[0])
        connection.close()

        print(" 30(p) of Max Load :"+str(round(def_buffer_6_prc,2))+"   Max Load:"+str(round(self.max_load,2))+" Max Rec ID :"+str(self.max_load_rec_id))
        
        print(" ===================================")
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT round(X_NUM,2),round(Y_NUM,2),REC_ID FROM STG_GRAPH_MST where Y_NUM >  "+str(def_buffer_6_prc)+" and rec_id < '"+str(self.max_load_rec_id)+"' order by REC_ID ASC")
        for x in results:
            print("Rec Id :"+str(x[2])+"  x_num :"+str(x[0])+"   y_num:"+str(x[1]))
            
            if (float(c)==0):                
                c=float(round(x[1],2))
            else:    
                if(float(x[1]) > float(c)):
                    c=float(x[1])
                    continue
                elif(float(x[1]) == float(c)):
                    def_point=float(x[0])
                    def_point_y=float(x[1])
                    print("Break 1 Point :"+str(def_point_y))
                    break
                elif(float(x[1]) <  float(c)):
                    def_point=float(x[0])
                    def_point_y=float(x[1])
                    print("Break 2 Point :"+str(def_point_y))
                    break
                else:
                    c=float(x[1])
                    def_point=float(x[0])
                    def_point_y=float(x[1])
                    print("Break 3 Point :"+str(def_point_y))
                    break                    
        connection.close()        
        
        self.yeild_strength=str(round(def_point_y,2))
        connection = sqlite3.connect("tyr.db")              
        with connection:
                cursor = connection.cursor()
                if(float(def_point) > 0):
                    cursor.execute("UPDATE GLOBAL_VAR SET DEF_POINT = '"+str(def_point)+"'")
                else:                    
                    cursor.execute("UPDATE GLOBAL_VAR SET DEF_POINT = 0")
                    
        connection.commit();
        connection.close()
    def start_test_tensile_8(self):
        self.label_35.setText("")
        self.validation()
        if(self.goAhead=="Yes"):                
                ### Update global var
                connection = sqlite3.connect("tyr.db")              
                with connection:        
                  cursor = connection.cursor()                  
                  cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID='"+str(self.label_12.text())+"', NEW_TEST_AREA='"+str(self.lineEdit_3.text())+"'")
                connection.commit();
                connection.close()
                
                
                self.sc_new =PlotCanvas_Auto(self,width=5, height=4, dpi=80)
                self.gridLayout.addWidget(self.sc_new, 1, 0, 1, 1)
                
                connection = sqlite3.connect("tyr.db")
                results=connection.execute("SELECT COUNT(*) FROM STG_GRAPH_MST")
                rows=results.fetchall()
                connection.close()
                
                #self.label_4.setText(str(rows[0][0]))
                #print("count of stg records :"+str(rows[0][0]))
                if(int(rows[0][0]) > -2 ):
                    
                    self.timer3.setInterval(1000)        
                    self.timer3.timeout.connect(self.show_load_cell_val)
                    self.timer3.start(1) 
                
                
                
                
        else:
                print("validation Error")
        
        
    def validation(self):
        self.goAhead="No"
        if(str(self.lineEdit.text()) == ""):
               self.label_35.setText("Initail Size Parameters  1 should not be NULL.")
               self.label_35.show()
        elif(str(self.lineEdit_2.text()) == "" and self.label_31.text() == "(Rectangle)"):
               self.label_35.setText("Initail Size Parameters  2 should not be NULL.")
               self.label_35.show()
        elif(str(self.lineEdit_3.text()) == ""):
               self.label_35.setText("Inital Area should not be NULL.")
               self.label_35.show()
        elif(str(self.lineEdit_4.text()) == ""):
               self.label_35.setText("Guage Length Should not be NULL")
               self.label_35.show()
        elif(str(self.lineEdit_5.text()) == ""):
               self.label_35.setText("Final Lenght Should not be NULL")
               self.label_35.show()
        elif(str(self.lineEdit_6.text()) == ""):
               self.label_35.setText("Final Size Parameters  1 should not be NULL.")
               self.label_35.show()
        elif(str(self.lineEdit_7.text()) == "" and self.label_31.text() == "(Rectangle)"):
               self.label_35.setText("Size Parameters  2 should not be NULL.")
               self.label_35.show()
        else:
               self.goAhead="Yes"
               
               connection = sqlite3.connect("tyr.db")
               results=connection.execute("select count(*) from TEST_MST WHERE TEST_ID = '"+str(self.label_12.text())+"'")       
               for x in results:           
                 if(int(x[0]) > 0):
                       self.test_id_exist="Yes"
                 else:
                       self.test_id_exist="No"                     
               connection.close() 
               
               if(self.test_id_exist=="Yes"):                   
                   connection = sqlite3.connect("tyr.db")
                   with connection:        
                       cursor = connection.cursor()
                       cursor.execute("UPDATE TEST_MST SET SPEC_DTLS='"+str(self.label_34.text())+"',INI_THICKNESS='"+str(self.lineEdit.text())+"',INI_WIDTH='"+str(self.lineEdit_2.text())+"',INI_DIAMETER='"+str(self.lineEdit.text())+"',INI_AREA='"+str(self.lineEdit_3.text())+"',REDUCED_AREA_PRC='"+str(self.label_32.text())+
                        "',TENSILE_STRENGTH='"+str(self.label_15.text())+"',YEILD_STRENGTH='"+str(self.label_17.text())+"',FINAL_LENGTH='"+str(self.lineEdit_5.text())+"',ELONGATION_PERC='"+str(self.label_29.text())+"',FINAL_THICKNESS='"+str(self.lineEdit_6.text())+"',FINAL_WIDTH='"+str(self.lineEdit_7.text())+"',FINAL_DIAMETER='"+str(self.lineEdit.text())+
                        "',COIL_ID='"+str(self.label_27.text())+"', SR_ID='"+str(self.lineEdit_31_2.text())+"',LOCATION='"+str(self.lineEdit_31_3.text())+"',SUPPLIER='"+str(self.lineEdit_31_3.text())+"',HEAT_NO='"+str(self.lineEdit_31_2.text())+
                        "',SAMPLE_TYPE='"+str(self.comboBox_2.currentText())+
                        "',FINAL_AREA='"+str(self.label_30.text())+"', SHAPE='"+str(self.shape)+"'      WHERE  TEST_ID = '"+str(self.label_12.text())+"'")
                       
                   connection.commit();
                   connection.close()
                   print("Record updated  in TEST_MST:")
                   #self.label_35.setText("Test Data Saved Successfully")
                   self.pushButton_13.setEnabled(True)
                   self.pushButton_15.setEnabled(True)
                   self.pushButton_16.setEnabled(True)
                   self.pushButton_3.setEnabled(True)
                   
               else:
                   print("Record is not updated  in TEST_MST:")
                   self.label_35.setText("Test Data is not Saved Successfully")
                   
                   
    def open_pdf(self):
        self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90) 
        self.create_pdf_tensile_8()
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
    
    def create_pdf_tensile_8(self):
        self.sample_type=""
        self.remark="______________________________________________________________________________"
        y=300
        Elements=[]
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT A.SAMPLE_TYPE,A.TEST_ID,A.CREATED_ON,A.COIL_ID,A.SR_ID,A.LOCATION,A.SPEC_DTLS,A.COMMENTS  FROM TEST_MST A where A.TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:                    
                    self.sample_type=str(x[0])                    
                    if(str(x[0]) == "Mechanical Testing Report - Raw Material"):                
                                self.summary_data=[["Test No: ",str(x[1]),"Tested Date: ",str(x[2])],["Coil ID : : ",str(x[3]),"Heat Number : ",str(x[4])],["Supplier : ",str(x[5]),"Item Description :",str(x[6])]]
                    else:
                                self.summary_data=[["Test No: ",str(x[1]),"Tested Date: ",str(x[2])],["Coil ID : : ",str(x[3]),"Serial Number: ",str(x[4])],["Sample Location : ",str(x[5]),"Item Description :",str(x[6])]]
                    
                    self.remark=str(x[7])
        connection.close()
        
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        
        
        self.star=" * "
        if(self.label_31.text() == "(Rectangle)"):
                self.star=" * "
        else:
                self.star="  "
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT INI_THICKNESS,INI_WIDTH,INI_AREA,FINAL_THICKNESS,FINAL_WIDTH,FINAL_AREA,REDUCED_AREA_PRC,GUAGE_LENGTH,FINAL_LENGTH,ELONGATION_PERC,TENSILE_STRENGTH,YEILD_STRENGTH FROM TEST_MST  where TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ") 
        for x in results:
            ptext2 = "<font name=Helvetica size=14> <b>Parameters : </b> </font>"            
            Title3 = Paragraph(str(ptext2), styles["Normal"])
            if(self.sample_type == "Mechanical Testing Report - Welding Sample"):
                    
                    self.param_data=[["Initial Size (mm)  : ",str(x[0])+str(self.star)+str(x[1]),"Initial Area (mm2) : ",str(x[2])],["Final Size (mm)    :",str(x[3])+str(self.star)+str(x[4]),"Final Area (mm2) : ",str(x[5])]]
                    self.param_data.append(["Reduced Area (%)   : ",str(x[6])," "," "])
                    #self.param_data.append(["Guage Length(mm)    : ",str(x[7]),"Final Length (mm)   :",str(x[8])])
                    #self.param_data.append(["Elongation (%)   : ",str(x[9])," "," "])
                    self.param_data.append(["Tensile Strength (MPa)    : ",str(x[10]),"",""])                
                
            else:    
                    self.param_data=[["Initial Size (mm)  : ",str(x[0])+str(self.star)+str(x[1]),"Initial Area (mm2) : ",str(x[2])],["Final Size (mm)    :",str(x[3])+str(self.star)+str(x[4]),"Final Area (mm2) : ",str(x[5])]]
                    self.param_data.append(["Reduced Area (%)   : ",str(x[6])," "," "])
                    self.param_data.append(["Guage Length(mm)    : ",str(x[7]),"Final Length (mm)   :",str(x[8])])
                    self.param_data.append(["Elongation (%)   : ",str(x[9])," "," "])
                    self.param_data.append(["Tensile Strength (MPa)    : ",str(x[10]),"Yeild   Strength (MPa) :",str(x[11])])
                   
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select COMPANY_NAME,ADDRESS1 from SETTING_MST ") 
        for x in results:            
            Title = Paragraph(str(x[0]), styles["Title"])
            ptext = "<font name=Helvetica size=11>"+str(x[1])+" </font>"            
            Title2 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        
        blank=Paragraph("                                                                                          ", styles["Normal"])
        comments = Paragraph("<font name=Helvetica size=14><b>  Remark : </b></font>"+str(self.remark), styles["Normal"])        
        
        footer_2= Paragraph("<font name=Helvetica size=14><b>   Tested By: _________________                    Approved  By:_________________  </b></font>",styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
        
        #f1=Table(data)
        #f1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
        
        #TEST_DETAILS = Paragraph("----------------------------------------------------------------------------------------------------------------------------------------------------", styles["Normal"])
        TS_STR = Paragraph("<font name=Helvetica size=11>"+str(self.sample_type)+" </font>", styles["Title"])
        #f2=Table(data2)
        #f2.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9),('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')]))       
         
        f3=Table(self.summary_data)
        f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
        f4=Table(self.param_data)
        f4.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 11),('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold')]))       
        
        report_gr_img="last_graph.png"        
        pdf_img= Image(report_gr_img, 6 * inch, 4 * inch)
        
        
        Elements=[Title,Title2,TS_STR,Spacer(1,12),Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),Title3,Spacer(1,12),Spacer(1,12),f4,Spacer(1,12),Spacer(1,12),Spacer(1,12),Spacer(1,12),footer_2,Spacer(1,12),Spacer(1,12),blank,blank,blank,Spacer(1,12),Spacer(1,12),comments,Spacer(1,12),Spacer(1,12),Spacer(1,12)]
        
        
        doc = SimpleDocTemplate('./reports/test_report.pdf', rightMargin=10,
                                leftMargin=20,
                                topMargin=10,
                                bottomMargin=30,)
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
        
        self.plot()        
        
        
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
        self.test_type="Tensile"
        self.color=['b','r','g','y','k','c','m','b']
        #ax.set_title('Test Id=32         Samples=3       BreakLoad(Kg)=110        Length(mm)=3')         
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_ID FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
             self.graph_ids.append(x[0])             
        connection.close()
        
        ### Univarsal change for  Graphs #####################
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
        for x in results:
             ax.set_xlim(0,float(x[0]))
             ax.set_ylim(0,float(x[1]))          
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME FROM GLOBAL_VAR") 
        for x in results:
             self.test_type=str(x[0])            
        connection.close()
        
        
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
        
            connection = sqlite3.connect("tyr.db")
            if(self.test_type=="Compress" or self.test_type=="Flexural"):
                results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE GRAPH_ID='"+str(self.graph_ids[g])+"'")
            else:   
                results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            for k in results:        
                self.x_num.append(k[0])
                self.y_num.append(k[1])
            connection.close() 
        
            if(g < 8 ):
                ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
        
        print("self.test_type:"+str(self.test_type))
        if(str(self.test_type)=="Compress"):
            ax.set_xlabel('Compression (mm)')        
        else:
            ax.set_xlabel('Strain (%)')
        ax.set_ylabel('Stress (MPa)')
        #self.connect('motion_notify_event', mouse_move)
        ax.legend()        
        self.draw()
        self.figure.savefig('last_graph.png',dpi=100)
        
        #ax.connect('motion_notify_event', mouse_move)

class PlotCanvas_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=5, height=4, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = fig.add_subplot(111)
        #self.axes = plt.axes(xlim=(0, 100), ylim=(0, 100))
        self.axes.set_facecolor('#CCFFFF')  
        self.axes.minorticks_on()
        self.test_type="Tensile"
        
        
#        connection = sqlite3.connect("tyr.db")
#        results=connection.execute("SELECT NEW_TEST_NAME,TEST_ID,NEW_TEST_JOB_NAME,NEW_TEST_BATCH_ID ,(SELECT COUNT(CYCLE_ID)+1 as x FROM CYCLES_MST B WHERE B.TEST_ID = TEST_ID) as CycleNo   FROM GLOBAL_VAR") 
#        for x in results:
#             self.test_type=str(x[0])
#             #self.axes.set_title("Test Id="+str(x[1])+", Cycle No="+str(x[4])+", Job Name="+str(x[2])+", Batch Id="+str(x[3]))  
#        connection.close()
        
        if(self.test_type=="Compress"):
            self.axes.set_xlabel('Compression (mm)')
        elif(self.test_type=="COF"):
            self.axes.set_xlabel('Length (mm)') 
        else:        
            self.axes.set_xlabel('Strain (%)')
          
        self.axes.set_ylabel('Stress (MPa)') 
        self.axes.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)        
        ###
        self.playing = False
        self.p =0
        self.q =0
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
        results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1,AUTO_REV_TIME_OFF,BREAKING_SENCE from SETTING_MST") 
        for x in results:
             self.axes.set_xlim(0,int(x[0]))
             self.axes.set_ylim(0,int(x[1]))
             self.flexural_max_load=int(x[1])
             self.xlim=int(x[0])
             self.ylim=int(x[1])
             self.auto_rev_time_off=int(x[2])
             self.break_sence=int(x[3])
        connection.close()
        
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_GUAGE_MM,NEW_TEST_NAME,IFNULL(NEW_TEST_MAX_LOAD,0),IFNULL(NEW_TEST_MAX_LENGTH,0),IFNULL(TEST_LENGTH_MM,0),IFNULL(NEW_TEST_AREA,0) from GLOBAL_VAR") 
        for x in results:            
             self.test_guage_mm=int(x[0])
             if(str(x[1]) == "Flexural"):
                 self.test_type="Compress"
             else:
                  self.test_type=str(x[1])
             self.max_load=int(x[2])
             #self.max_load=100
             self.max_length=float(float(x[0])-float(x[3]))
             self.flex_max_length=float(x[3])
             self.cof_max_length=float(x[4])
             self.test_cs_area=float(x[5])
             
             print("Max Load :"+str(self.max_load).zfill(5)+"  CoF Max length :"+str(int(self.cof_max_length)).zfill(5))
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
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                          self.command_str="*S2E%04d"%self.flexural_max_load+" %04d"%self.max_length+"\r"
                    else:
                          self.command_str="*S1E%04d"%self.flexural_max_load+" %04d"%self.max_length+"\r"
                    
                    print("self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)                 
                else:
                    print("Compress test not started ")               
                               
            elif(self.test_type=="Flexural"):
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                            #self.ser.write(b'*S2E0599 200\r')
                            self.command_str="*S2C%04d"%self.flexural_max_load+" %04d"%self.flexural_max_load+"\r"
                            #self.command_str="*S2E%04d"%self.flexural_max_load+" 0000\r"
                    else:
                            #self.command_str="*S1E%04d"%self.flexural_max_load+" 0000\r"
                            self.command_str="*S1C%04d"%self.flexural_max_load+" %04d"%self.flexural_max_load+"\r"
                            
                    print("self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    print("fluexural test started ")
                else:
                    print("fluexural test not started ")
            elif(self.test_type=="COF"):                
                if(len(self.ybuff) > 8):
                    if(str(self.ybuff[6])=="2"):
                        self.command_str="*S2F%04d"%self.cof_max_length+"_000.0\r"                        
                    else:
                        self.command_str="*S1F%04d"%self.cof_max_length+"_000.0\r"
                        
                    print("COF self.command_str:"+str(self.command_str))
                    b = bytes(self.command_str, 'utf-8')
                    self.ser.write(b)
                    print("COF test started ")   
                        
                else:
                    print("Error :Serial O/P is not getting ")               
                
                
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
            
        
        
                 
        
        self.timer1.setInterval(1000)     
        self.timer1.timeout.connect(self.update_graph)
        self.timer1.start(1)
        
        self.on_ani_start()
    
    def update_graph(self):       
        if(self.IO_error_flg==0):
            '''
            
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
            
            if (len(self.check_R) > 0 and len(self.check_OK) ==0):
                
                
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
                    self.p=int(self.test_guage_mm)-self.p
                    #print("self.p :"+str(self.p))
                elif(self.test_type=="Flexural"):
                    #self.p=self.p
                    self.p=int(self.test_guage_mm)-self.p
                else:
                    self.p=self.p
                    
                #### Convert ro stress and Streain
                self.kg_to_Newton=float(9.81)
                #self.x_num.append((self.p/float(test_guage_mm.guage))*100)
                #self.y_num.append((self.q*self.kg_to_Newton/float(self.self.test_cs_area)))
                self.p=float(self.p)/float(self.test_guage_mm)*100
                self.q=float(self.q)*self.kg_to_Newton/float(self.test_cs_area)  
                self.arr_p.append(float(self.p))
                self.arr_q.append(float(self.q))
                
                print(" Timer P:"+str(float(self.p))+" q:"+str(float(self.q)))
               
                #print(" test_guage_mm:"+str(self.test_guage_mm)+" test_cs_area:"+str(self.test_cs_area))

                if(int(self.q) > int(self.ylim)):
                   self.ylim=(int(self.q)+100)
                   self.ylim_update='YES'                   
                   
                              
                if(self.p > self.xlim):
                   self.xlim=(int(self.p)+100)
                   self.xlim_update='YES'                   
                
                self.save_data_flg="No"
            else:                
               
                self.save_data_flg="Yes"
                self.on_ani_stop()
                
                    
                
       
                    
                
               
     
          
    def plot_grah_only(self,i):       
        
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
                 
                 self.command_str="*P%04d"%self.calc_speed+"_%04d"%self.break_sence+"\r"
                 print("Morot Speed and Breaking speed Command  :"+str(self.command_str))                 
            else:
                 print(" not Ok ")
                 
        else:
            print(" not Ok ")
                      
    

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
             ax.set_xlim(0,int(x[0]))
             ax.set_ylim(0,int(x[1]))          
        connection.close()
               
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])  
              
        ax.plot(self.x,self.y,'b')
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME,TEST_ID,NEW_TEST_JOB_NAME,NEW_TEST_BATCH_ID ,(SELECT COUNT(CYCLE_ID)+1 as x FROM CYCLES_MST B WHERE B.TEST_ID = TEST_ID) as CycleNo   FROM GLOBAL_VAR") 
        for x in results:
             self.test_type=str(x[0])
             #self.axes.set_title("Test Id="+str(x[1])+", Cycle No="+str(x[4])+", Job Name="+str(x[2])+", Batch Id="+str(x[3]))  
        connection.close()
        
        
        ax.set_ylabel('Stress  (MPa)')
        
        
        if(self.test_type=="Compress"):
            ax.set_xlabel('Compression (mm)')       
        else:
            ax.set_xlabel(' Strain (%)')
        self.draw() 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_19_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
