from TY_46_EXPORT_SPEC import TY_46_Ui_MainWindow
from TY_47_IMPORT_SPECS import TY_47_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import QTableWidgetItem
import sqlite3
import datetime
import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class TY_05_SPECI_6_ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1361, 669)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1311, 601))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(255, 237, 250);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 30, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 85, 127);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(1100, 40, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 530, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 530, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 641, 481))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(226, 255, 225);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
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
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(10, item)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 10, item)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(490, 30, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(1000, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(680, 380, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(680, 430, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(1130, 380, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(810, 430, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(950, 530, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(1070, 530, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(1130, 170, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(1000, 380, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(1000, 170, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(810, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(690, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setGeometry(QtCore.QRect(810, 290, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(1190, 530, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_12.setGeometry(QtCore.QRect(1130, 120, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(1000, 290, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(1130, 290, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(1000, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(690, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(670, 89, 631, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(690, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(810, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(900, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(690, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(810, 230, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(900, 230, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.label_39 = QtWidgets.QLabel(self.frame)
        self.label_39.setGeometry(QtCore.QRect(900, 290, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_41 = QtWidgets.QLabel(self.frame)
        self.label_41.setGeometry(QtCore.QRect(1230, 380, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(1130, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        '''
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(1130, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        '''
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(850, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(980, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(680, 340, 621, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.line_3.setFont(font)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(890, 430, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(1000, 430, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(1130, 430, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(680, 490, 621, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.line_4.setFont(font)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_15.setGeometry(QtCore.QRect(810, 380, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_42 = QtWidgets.QLabel(self.frame)
        self.label_42.setGeometry(QtCore.QRect(1230, 290, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_42.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1361, 21))
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
        self.label.setText(_translate("MainWindow", "Specimen Information(6)"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00"))
        self.pushButton_2.setText(_translate("MainWindow", "Add"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Spec.ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Part Number"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Part Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Test Speed"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Test Type"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Max .Deflection"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Max. Load"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Operator Name"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Pre. Load"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Hardness"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Test Method"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "w"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "we"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "ee"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("MainWindow", "e"))
        item = self.tableWidget.item(0, 8)
        item.setText(_translate("MainWindow", "222ewe"))
        item = self.tableWidget.item(0, 9)
        item.setText(_translate("MainWindow", "22"))
        item = self.tableWidget.item(0, 10)
        item.setText(_translate("MainWindow", "23"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_21.setText(_translate("MainWindow", "Please select the record to Edit."))
        self.label_22.setText(_translate("MainWindow", "Part Number :"))
        self.label_24.setText(_translate("MainWindow", "Operator Name :"))
        self.label_25.setText(_translate("MainWindow", "Hardness:"))
        self.lineEdit.setText(_translate("MainWindow", "2"))
        self.lineEdit_3.setText(_translate("MainWindow", "1"))
        self.pushButton_4.setText(_translate("MainWindow", "Delete"))
        self.pushButton_5.setText(_translate("MainWindow", "Reset"))
        self.lineEdit_7.setText(_translate("MainWindow", "Part Name"))
        self.label_31.setText(_translate("MainWindow", "Pre. Load:"))
        self.label_33.setText(_translate("MainWindow", "Part Name:"))
        self.lineEdit_4.setText(_translate("MainWindow", "200"))
        self.label_34.setText(_translate("MainWindow", "Max Deflection:"))
        self.lineEdit_10.setText(_translate("MainWindow", "0.1"))
        self.pushButton_9.setText(_translate("MainWindow", "Return"))
        self.lineEdit_12.setText(_translate("MainWindow", "35655"))
        self.label_27.setText(_translate("MainWindow", "Max. Load:"))
        self.lineEdit_6.setText(_translate("MainWindow", "50"))
        self.label_26.setText(_translate("MainWindow", "Material:"))
        self.label_35.setText(_translate("MainWindow", "Test Speed:"))
        self.label_23.setText(_translate("MainWindow", "Spect.ID:"))
        self.label_2.setText(_translate("MainWindow", "0001"))
        self.label_28.setText(_translate("MainWindow", "(mm/min)"))
        self.label_36.setText(_translate("MainWindow", "Test Type:"))
        self.lineEdit_5.setText(_translate("MainWindow", "Axiel"))
        self.label_37.setText(_translate("MainWindow", "(mm/min)"))
        self.label_39.setText(_translate("MainWindow", "(mm)"))
        self.label_41.setText(_translate("MainWindow", "(kg)"))
        '''
        
        '''
        self.pushButton_6.setText(_translate("MainWindow", "Export"))
        self.pushButton_7.setText(_translate("MainWindow", "Import"))
        self.label_47.setText(_translate("MainWindow", "Test Method:"))
        self.radioButton.setText(_translate("MainWindow", "Tensile"))
        self.radioButton_2.setText(_translate("MainWindow", "Compression"))
        self.lineEdit_15.setText(_translate("MainWindow", "Operator Name"))
        self.label_42.setText(_translate("MainWindow", "(kg)"))
        self.pushButton_9.clicked.connect(MainWindow.close)
        self.lineEdit_5.setText("")
        #self.label_35_1.setText("Rev.Test Speed:")
        self.pushButton_9.clicked.connect(MainWindow.close)
        
        #self.comboBox_2.currentTextChanged.connect(self.specimen_diamentions)
        
       
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        self.c_select_all_data()
        self.c_rest_fun()
        self.tableWidget.doubleClicked.connect(self.c_fetch_data_from_tw)
        self.pushButton_2.clicked.connect(self.c_add_click) 
        self.pushButton_3.clicked.connect(self.c_edit_click)       
        self.pushButton_4.clicked.connect(self.c_delete_click)
        self.pushButton_5.clicked.connect(self.c_rest_fun)
        self.pushButton_6.clicked.connect(self.open_new_window)
        self.pushButton_7.clicked.connect(self.open_new_window2)
    
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
       
    
    
    
   
           
    
   
    
    
    #Contractors            
    def c_fetch_data_from_tw(self):        
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.dr_id=str(self.tableWidget.item(row, 0).text())
            self.label_2.setText(str(self.tableWidget.item(row, 0).text()).zfill(3)) 
            self.lineEdit_12.setText(str(self.tableWidget.item(row, 1).text())) #Part No           
            self.lineEdit_7.setText(str(self.tableWidget.item(row, 2).text())) #Part Name
            self.lineEdit_5.setText(str(self.tableWidget.item(row, 3).text())) # Test Type
            self.lineEdit_15.setText(str(self.tableWidget.item(row, 4).text())) #Operator Name
            self.textEdit.setText(str(self.tableWidget.item(row, 5).text())) #Material
            self.lineEdit_3.setText(str(self.tableWidget.item(row, 6).text())) #Hardness
            self.lineEdit_6.setText(str(self.tableWidget.item(row, 7).text())) #Max Load
            self.lineEdit_10.setText(str(self.tableWidget.item(row, 8).text())) #Max . Deflection
            self.lineEdit.setText(str(self.tableWidget.item(row, 9).text())) #pre load
            self.lineEdit_4.setText(str(self.tableWidget.item(row, 10).text())) # test speed
            self.pushButton_2.setDisabled(True) #add
            self.pushButton_3.setEnabled(True)  #save
            self.pushButton_4.setEnabled(True) #delete           
            #self.pushButton_5.setEnabled(True) #reset
            if(str(self.tableWidget.item(row, 11).text()) == "Tensile"):
                self.radioButton.setChecked(True)
                self.radioButton_2.setChecked(False)
                self.test_mode="Tensile"                
            elif(str(self.tableWidget.item(row, 11).text()) == "Compression"): 
                self.radioButton_2.setChecked(True)
                self.radioButton.setChecked(False)
                self.test_mode="Compression"
            else:    
                self.radioButton.setChecked(True)
                self.radioButton_2.setChecked(False)
                self.test_mode="Tensile"
            
        else:    
            self.label_2.setText("Please Select the record.")
            self.label_2.show()
            
           
    def c_rest_fun(self):
        self.label_2.setText("")
        self.lineEdit_12.setText("")
        self.textEdit.setText("")
        self.lineEdit_7.setText("")
       
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("") #Rev Speed.
        self.lineEdit_10.setText("")
            
        self.lineEdit.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_6.setText("")
            
        #self.lineEdit_8.setText("")
        #self.lineEdit_11.setText("")
        #self.lineEdit_13.setText("")
        #self.lineEdit_14.setText("")
        
        self.pushButton_2.setEnabled(True) #add
        self.pushButton_3.setDisabled(True)  #save
        self.pushButton_4.setDisabled(True) #delete           
        self.pushButton_5.setEnabled(True) #reset
        
        self.label_21.hide()
        self.c_select_all_data()
        self.label_2.setText("01")
  
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'SPECIMEN_MST'")       
        for x in results:           
                 self.label_2.setText(str(x[0]).zfill(3))            
        connection.close()         
            
   
    def c_load_data(self):        
        if(self.operation_flg=="ADD"):
                #print("inside Add ")
                self.c_add_data()
        elif(self.operation_flg=="EDIT"):
                #print("inside edit ")
                self.c_edit_data()
        elif(self.operation_flg=="DELETE"):
                #print("inside delete ")
                self.c_delete_data()
        else:
                print("Invalid Operation.")
         
    def c_add_click(self):
        self.operation_flg="ADD"       
        self.c_load_data()
        
    def c_add_data(self):
        self.validations()
        self.check_for_dup_spec_name_add()
        if(self.dup_spec_name_flag == "Y"):
              self.label_21.setText("Product Name is already exist.")           
              self.label_21.show()
        else:                
            if(self.label_2.text() != ""):            
                if(self.go_ahead=="Yes"):
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("INSERT INTO SPECIMEN_MST(PART_NO,PART_NAME,TEST_TYPE,OPERATOR,MATERIAL,HARDNESS,MAX_LOAD,MAX_DEFLECTION,PRE_LOAD,MOTOR_SPEED,TEST_MODE) VALUES('"+str(self.part_no)+"','"+str(self.part_name)+"','"+str(self.test_type)+"','"+str(self.operator)+"','"+str(self.material)+"','"+str(self.hardness)+"','"+str(self.max_load)+"','"+str(self.max_deflection)+"','"+str(self.pre_load)+"','"+str(self.test_speed)+"','"+str(self.test_mode)+"')")                    
                    connection.commit();                    
                    connection.close()  
              
                    self.label_21.setText("Record Added Successfully.")           
                    self.label_21.show()
            else :
                self.label_21.setText("Id is Empty.")
                self.label_21.show()
            
        self.c_select_all_data()
    
    def c_edit_click(self):        
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="EDIT"
            self.c_load_data()
        else:    
            self.label_21.setText("Please Select the record.")
            self.label_21.show() 
    
    def c_edit_data(self):
        self.validations()
        self.check_for_dup_spec_name_upd()
        if(self.dup_spec_name_flag == "Y"):
              self.label_21.setText("Spec. Name is already exist.")           
              self.label_21.show()
        else:
              if(self.label_2.text() != "" and self.go_ahead == 'Yes'):
                connection = sqlite3.connect("tyr.db")
                with connection:        
                        cursor = connection.cursor()
                        cursor.execute("UPDATE SPECIMEN_MST SET PART_NO='"+str(self.part_no)+"',PART_NAME='"+str(self.part_name)+"',MATERIAL='"+str(self.material)+"',MAX_DEFLECTION='"+str(self.max_deflection)+"', MAX_LOAD='"+str(self.max_load)+"',MOTOR_SPEED='"+str(self.test_speed)+"',PRE_LOAD='"+str(self.pre_load)+"' ,HARDNESS='"+str(self.hardness)+"', TEST_TYPE='"+str(self.test_type)+"' , OPERATOR='"+str(self.operator)+"',TEST_MODE='"+str(self.test_mode)+"'  WHERE  SPECIMEN_ID ='"+str(self.dr_id)+"'")                    
                connection.commit();                    
                connection.close()
                self.label_21.setText("Record Saved Successfully.")       
                self.label_21.show()
                self.c_select_all_data()
    
    def validations(self):
        self.part_no=""
        self.part_name=""
        self.max_deflection=""
        self.max_load=""
        self.test_speed=""
        self.pre_load=""
        self.hardness=""
        self.test_type=""
        self.material=""
        self.operator=""
        self.test_mode=""
        self.go_ahead="No"
        if(self.lineEdit_12.text() == ""):
             self.label_21.setText("Part Number is Empty.")
             self.label_21.show()  
        elif(self.lineEdit_7.text()== ""):
             self.label_21.setText("Part Name is Empty.")
             self.label_21.show()
        elif(self.lineEdit_10.text()== ""):
             self.label_21.setText("Max. Deflection is Empty.")
             self.label_21.show()        
        elif(self.lineEdit_4.text() == ""):
             self.label_21.setText("Test Speed Should not null.")
             self.label_21.show()         
        elif(self.lineEdit_6.text() == ""):
             self.label_21.setText("Max Load is Empty.")
             self.label_21.show() 
        elif(self.lineEdit_15.text() == ""):
             self.label_21.setText("Operator Name is Empty.")
             self.label_21.show()
        elif(self.lineEdit.text() == ""):
             self.label_21.setText("Pre Load is Empty.")
             self.label_21.show()
        elif(self.lineEdit_3.text() == ""):
             self.label_21.setText("Hardness is Empty.")
             self.label_21.show()
        elif(self.lineEdit_5.text() == ""):
             self.label_21.setText("Test Type is Empty.")
             self.label_21.show()
        else:
             self.part_no=str(self.lineEdit_12.text())
             self.part_name=str(self.lineEdit_7.text())
             self.max_deflection=str(self.lineEdit_10.text())
             self.max_load=str(self.lineEdit_6.text())
             self.test_speed=str(self.lineEdit_4.text())
             self.pre_load=str(self.lineEdit.text())
             self.hardness=str(self.lineEdit_3.text())
             self.test_type=str(self.lineEdit_5.text())
             self.material=self.textEdit.toPlainText()
             self.operator=str(self.lineEdit_15.text())
             if(self.radioButton.isChecked()):
                  self.test_mode="Tensile"   
             elif(self.radioButton_2.isChecked()):
                  self.test_mode="Compression"   
             else:
                  self.test_mode="Tensile"
             self.go_ahead="Yes"
        
    def check_for_dup_spec_name_add(self):
        self.dup_spec_name_flag="N"
        if(self.lineEdit_12.text() != ""):
             connection = sqlite3.connect("tyr.db")
             results=connection.execute("select count(*) from SPECIMEN_MST WHERE PART_NO = '"+str(self.lineEdit_12.text())+"'")       
             for x in results:           
                     if(int(x[0]) > 0):
                          self.dup_spec_name_flag="Y"
                     else:
                          self.dup_spec_name_flag="N"                         
             connection.close()
        else:
             print("Spec Name is Empty.")
    
    
    def check_for_dup_spec_name_upd(self):
        self.dup_spec_name_flag="N"
        if(self.lineEdit_12.text() != ""):
             connection = sqlite3.connect("tyr.db")
             print("select count(*) from SPECIMEN_MST WHERE PART_NO = '"+str(self.lineEdit_12.text())+"' and SPECIMEN_ID !='"+str(self.dr_id)+"'") 
             results=connection.execute("select count(*) from SPECIMEN_MST WHERE PART_NO = '"+str(self.lineEdit_12.text())+"' and SPECIMEN_ID !='"+str(self.dr_id)+"'")       
             for x in results:           
                     if(int(x[0]) > 0):
                          self.dup_spec_name_flag="Y"
                     else:
                          self.dup_spec_name_flag="N"                         
             connection.close()
        else:
             print("Spec Name is Empty.")
        
        
    
    def c_delete_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="DELETE"
            self.c_load_data()
        else:    
            self.label_21.setText("Please Select the record.")
            self.label_21.show()        
     
      
    def c_delete_data(self):
        if(self.label_2.text() != ""):
            close = QMessageBox()
            close.setText("Confirm Deleteing Specimen ID : "+str(self.dr_id))
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM SPECIMEN_MST WHERE SPECIMEN_ID ='"+str(self.dr_id)+"'")                    
                    connection.commit();                    
                    connection.close()
                    
                    self.label_21.setText("Record Deleted Successfully.")                   
                    self.label_21.show()                    
                    self.c_select_all_data()
            else:
                    self.label_21.setText("Canceled Delete..")                   
                    self.label_21.show()
            
         
    def c_select_all_data(self):     
        self.c_delete_all_records()        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)       
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(12)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)        
        self.tableWidget.setHorizontalHeaderLabels(['Spec.Id.','Part No', 'Part Name',' Test Type ','Operator',' Material  ','Hardness','Max. Load','Max. Deflection','Pre Load','Test Speed','Test Method'] )       
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select SPECIMEN_ID,PART_NO,PART_NAME,TEST_TYPE,OPERATOR,MATERIAL,HARDNESS,MAX_LOAD,MAX_DEFLECTION,PRE_LOAD,MOTOR_SPEED,TEST_MODE FROM SPECIMEN_MST")                        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))                
        connection.close()   
        #self.tableWidget.resizeColumnsToContents()
        
        
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
    
    def c_delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
    
    def open_new_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_46_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_47_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_05_SPECI_6_ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
