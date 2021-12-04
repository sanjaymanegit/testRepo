# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TY_01_TEST_BATCH.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from TY_02_START_TEST import TY_02_Ui_MainWindow
from TY_02_START_TEST_FLEXUR import TY_02f_Ui_MainWindow
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class TY_01_fluxurl_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        MainWindow.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1301, 709))
        self.frame.setStyleSheet("")
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.frame.setObjectName("frame")
        
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 20, 261, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 350, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(84, 82, 82); color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(870, 350, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(84, 82, 82); color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        
        self.label_1_1 = QtWidgets.QLabel(self.frame)
        self.label_1_1.setGeometry(QtCore.QRect(650, 450, 145, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_1_1.setFont(font)
        self.label_1_1.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_1_1.setObjectName("label_1_1")        
        
        
        self.lineEdit_1_1 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_1_1)
        self.lineEdit_1_1.setValidator(input_validator)
        self.lineEdit_1_1.setGeometry(QtCore.QRect(810, 450, 80, 41))
        self.lineEdit_1_1.setMaxLength(6)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_1_1.setFont(font)
        self.lineEdit_1_1.setText("0")
        self.lineEdit_1_1.setObjectName("lineEdit_1_1")
        self.lineEdit_1_1.hide()
        
        self.label_2_1 = QtWidgets.QLabel(self.frame)
        self.label_2_1.setGeometry(QtCore.QRect(960, 450, 176, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2_1.setFont(font)
        self.label_2_1.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_2_1.setObjectName("label_2_1")        
        
        
        self.lineEdit_2_1 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_2_1)
        self.lineEdit_2_1.setValidator(input_validator)
        self.lineEdit_2_1.setGeometry(QtCore.QRect(1140, 450, 80, 41))
        self.lineEdit_2_1.setMaxLength(6)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_2_1.setFont(font)
        self.lineEdit_2_1.setText("0")
        self.lineEdit_2_1.setObjectName("lineEdit_2_1")
        self.lineEdit_2_1.hide()
        
        
        
        
        
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(50, 330, 511, 300))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 471, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 2, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 2, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 2, 1, 2)
        
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 200, 511, 121))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 471, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 1, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 1, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 1, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 0, 1, 1, 1)
      
        
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(670, 130, 421, 161))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 30, 351, 111))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(1040, 350, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        
        self.pushButton_8.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(186, 19, 19);\n")
        
        self.pushButton_8.setObjectName("pushButton_8")
        
        
        self.layoutWidget3 = QtWidgets.QWidget(self.frame)
        self.layoutWidget3.setGeometry(QtCore.QRect(70, 90, 341, 61))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        
        
        
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox.setStyleSheet("background-color: rgb(221, 255, 234) ; color: rgb(0, 0, 0);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(690, 40, 551, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_23.setObjectName("label_23")
        
        
        
        
        self.groupBox_3_1 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3_1.setGeometry(QtCore.QRect(670, 515, 282, 161))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.groupBox_3_1.setFont(font)
        self.groupBox_3_1.setObjectName("groupBox_3_1")
        self.layoutWidget2_1 = QtWidgets.QWidget(self.groupBox_3_1)
        self.layoutWidget2_1.setGeometry(QtCore.QRect(10, 30, 251, 111))
        self.layoutWidget2_1.setObjectName("layoutWidget2_1")
        self.gridLayout_4_1 = QtWidgets.QGridLayout(self.layoutWidget2_1)
        self.gridLayout_4_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4_1.setObjectName("gridLayout_4")
        self.label_21_1 = QtWidgets.QLabel(self.layoutWidget2_1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_21_1.setFont(font)
        self.label_21_1.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_21_1.setObjectName("label_21_1")
        self.gridLayout_4_1.addWidget(self.label_21_1, 0, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.layoutWidget2_1)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_1)
        self.lineEdit_1.setValidator(input_validator)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout_4_1.addWidget(self.lineEdit_1, 0, 1, 1, 1)
        self.label_22_1 = QtWidgets.QLabel(self.layoutWidget2_1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_22_1.setFont(font)
        self.label_22_1.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_22_1.setObjectName("label_22_1")
        self.gridLayout_4_1.addWidget(self.label_22_1, 1, 0, 1, 1)
        
        self.lineEdit_2_1_1 = QtWidgets.QLineEdit(self.layoutWidget2_1)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_2_1_1)
        self.lineEdit_2_1_1.setValidator(input_validator)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_2_1_1.setFont(font)
        self.lineEdit_2_1_1.setObjectName("lineEdit_2_1_1")
        self.gridLayout_4_1.addWidget(self.lineEdit_2_1_1, 1, 1, 1, 1)
        
        #3self.gridLayout_4_1.addWidget(self.lineEdit_1, 0, 1, 1, 1)
        #self.label_22_2 = QtWidgets.QLabel(self.layoutWidget2_1)
        
        self.label_22_2 = QtWidgets.QLabel(self.frame)
        self.label_22_2.setGeometry(QtCore.QRect(1150, 415, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_22_2.setFont(font)
        self.label_22_2.setStyleSheet("color: rgb(0, 0, 255);")       
        self.label_22_2.setText("4mm")
        self.label_22_2.setObjectName("label_22_2")
        #elf.gridLayout_4_1.addWidget(self.label_22_2, 1, 0, 1, 1)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.goAhead="No"
        self.shape=0
        self.thickness=0
        self.width=0
        self.diameter=0
        self.cs_area=0
        self.inn_dia=0
        self.out_dia=0
        self.party_name=0
        self.guage_mm=0
        self.pre_load=0
        self.motor_speed=0
        self.specs=0        
        self.test_type=""
        
        
        self.inut_strain_mm=0
        self.per_strain_mm=0
        self.span=0
        self.max_length=0
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Test Details"))
        self.pushButton_3.setText(_translate("MainWindow", "GO TO TEST"))
        self.pushButton_7.setText(_translate("MainWindow", "RESET"))
        self.groupBox.setTitle(_translate("MainWindow", "Specimen Details"))
        self.label_4.setText(_translate("MainWindow", "Speciment Shape:"))
        self.label_5.setText(_translate("MainWindow", "Rectangle"))
        self.label_7.setText(_translate("MainWindow", "Spec.  Specifications"))
        self.label_8.setText(_translate("MainWindow", "Specs XXXXXXX"))
        self.label_10.setText(_translate("MainWindow", "MRF"))
        self.label_9.setText(_translate("MainWindow", "Party:"))
        self.label_11.setText(_translate("MainWindow", "Test Speed (RPM):"))
        self.label_12.setText(_translate("MainWindow", "200"))
        self.label_13.setText(_translate("MainWindow", "Guage Length(mm) :"))
        self.label_14.setText(_translate("MainWindow", "60"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Specimen Diamentions"))
        self.label_15.setText(_translate("MainWindow", "CS.Area(mm2):"))
        self.label_17.setText(_translate("MainWindow", "Thickness(Mm):"))
        self.label_18.setText(_translate("MainWindow", "5"))
        self.label_19.setText(_translate("MainWindow", "Width(mm):"))
        self.label_20.setText(_translate("MainWindow", "15"))
        self.label_16.setText(_translate("MainWindow", "75000"))
        self.groupBox_3.setTitle(_translate("MainWindow", " Batch Details"))
        self.label_21.setText(_translate("MainWindow", "Job Name:"))
        self.label_22.setText(_translate("MainWindow", "Batch Id:"))
        
        self.groupBox_3_1.setTitle(_translate("MainWindow", " Graph Scale"))
        self.label_21_1.setText(_translate("MainWindow", "Max. Load ( Kgf ):"))
        self.label_22_1.setText(_translate("MainWindow", "Max. Elongation ( Mm ):"))
        
        self.pushButton_8.setText(_translate("MainWindow", "RETURN"))
        self.label_2.setText(_translate("MainWindow", "Test Type :"))
        self.label_3.setText(_translate("MainWindow", "Tensile"))
        self.label.setText(_translate("MainWindow", "Specimen Name:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Rabur-Rectangle"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Pipes-Jian"))
        self.label_23.setText(_translate("MainWindow", "Error : Batch Id and Job Id should not null."))
        self.label_23.hide()
        self.label_1_1.setText("Comp.Max.Load (Kgf):")
        self.label_1_1.hide()
        self.label_2_1.setText("Compressive.Length(mm):")
        self.label_2_1.hide()
        self.comboBox.currentTextChanged.connect(self.onchage_combo)
        self.pushButton_7.clicked.connect(self.reset_job)
        self.pushButton_3.clicked.connect(self.open_window)
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.lineEdit_1_1.textChanged.connect(self.make_zero_on_null)
        self.lineEdit_2_1.textChanged.connect(self.make_zero_on_null)
        self.lineEdit_1_1.textChanged.connect(self.on_change_input_strain)
        self.lineEdit_2_1.textChanged.connect(self.on_change_input_strain)
        self.load_data() 
     
    
    
    def on_change_input_strain(self):
        self.inut_strain_mm=0
        self.per_strain_mm=0
        self.span=self.lineEdit_1_1.text()
        self.max_length=0
        
        if(self.lineEdit_2_1.text() == ""):
             self.lineEdit_2_1.setText("0")
        else:
            print("% : "+str(self.label_2_1.text()))
            self.per_strain_mm=self.lineEdit_2_1.text()
            if(int(self.lineEdit_2_1.text()) > 0 ):
                    self.inut_strain_mm=float((int(self.per_strain_mm)/100)*int(self.span))
                    self.label_22_2.setText(str(round(self.inut_strain_mm,2))+" mm ")
                    self.max_length=str(round(self.inut_strain_mm,2))
        
    
    def make_zero_on_null(self):
        if(str(self.lineEdit_1_1.text()) == ""):
            self.lineEdit_1_1.setText("0")            
        else:
            print("ok")
            
        if(str(self.lineEdit_2_1.text()) == ""):
            self.lineEdit_2_1.setText("5")
        else:
            print("ok")
            
            
     
    def load_data(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT NEW_TEST_NAME FROM GLOBAL_VAR")
        rows=results.fetchall()        
        self.label_3.setText(rows[0][0])
        self.test_type=str(rows[0][0])
        if(str(rows[0][0])=="Compress"):
             self.label_1_1.show()
             self.lineEdit_1_1.show()
             self.label_2_1.show()
             self.lineEdit_2_1.show()
        elif(str(rows[0][0])=="Flexural"):
            self.label_1_1.setText("Span (mm) :")
            self.label_1_1.show()
            self.lineEdit_1_1.show()
            self.label_2_1.setText("Input Strain (%) :")
            self.label_2_1.show()
            self.lineEdit_2_1.show()
            self.load_flexural_data()
        else:
             self.label_1_1.hide()
             self.lineEdit_1_1.hide()
             self.label_2_1.hide()
             self.lineEdit_2_1.hide()
             
        connection.close()
        self.i=0
        connection = sqlite3.connect("tyr.db")
        if(self.test_type=="Tear" or self.test_type=="Flexural"):
            results=connection.execute("SELECT SPECIMEN_NAME FROM SPECIMEN_MST where  SHAPE='Rectangle'") 
        else:   
            results=connection.execute("SELECT SPECIMEN_NAME FROM SPECIMEN_MST") 
        for x in results:            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str(x[0]))
            #print("i :"+str(x[0]))
            self.i=self.i+1
        connection.close()  
        
        #print("curr text :"+str(self.comboBox.currentText()))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SHAPE,THICKNESS,WIDTH,DIAMETER,round(C_A_AREA,2),IN_DIAMETER_MM,OUTER_DIAMETER_MM,PARTY_NAME,GUAGE_LENGTH_MM,PRE_LOAD,MOTOR_SPEED,SPECIMEN_SPECS FROM SPECIMEN_MST WHERE SPECIMEN_NAME='"+self.comboBox.currentText()+"'")         
        for x in results:        
           self.label_5.setText(str(x[0]))
           self.label_8.setText(str(x[11]))  #specs
           self.label_10.setText(str(x[7])) #party
           self.label_12.setText(str(x[10])) #motor speed 
           self.label_14.setText(str(x[8])) #guage
           self.label_16.setText(str(x[4])) #cs area
           
           #if(self.test_type=="Flexural"):
                   #self.lineEdit_1_1.setText(str(x[8]))

           self.shape=str(x[0])
           self.thickness=str(x[1])
           self.width=str(x[2])
           self.diameter=str(x[3])
           self.cs_area=int(x[4])
           self.inn_dia=str(x[5])
           self.out_dia=str(x[6])
           self.party_name=str(x[7])
           self.guage_mm=str(x[8])
           self.pre_load=str(x[9])
           self.motor_speed=str(x[10])
           self.specs=str(x[11])           
           #print(" cccc:"+str(x[0]))
           if (x[0]=="Rectangle"):
               self.label_17.setText("Thickness(mm):")
               self.label_18.setText(str(x[1]))
               if(self.test_type != "Tear"):
                       self.label_19.setText("Width(mm):")               
                       self.label_20.setText(str(x[2]))
           elif(x[0]=="Pipe"):    
               self.label_17.setText("In.Dia(mm):")
               self.label_18.setText(str(x[5]))
               self.label_19.setText("Out.Dia(mm):")  
               self.label_20.setText(str(x[6]))                            
           elif(x[0]=="Cylindrical"):    
               self.label_17.setText("Diameter(mm):")
               self.label_18.setText(str(x[3]))
               self.label_19.hide()
               self.label_20.hide()                                            
           elif(x[0]=="DirectValue"):    
               self.label_17.setText("CS.Area(mm2): ")
               self.label_18.setText(str(x[4]))
               self.label_19.hide()
               self.label_20.hide()
               
        connection.close()
        self.reset_job()
    
     
    def load_flexural_data(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select IFNULL(SPAN,0), IFNULL(PER_STRAIN_AT_INPUT,0) FROM GLOBAL_VAR")                 
        for x in results:
           self.lineEdit_1_1.setText(str(x[0]))       
           self.lineEdit_2_1.setText(str(x[1]))
        connection.close()     
        print("inside")
        
    def onchage_combo(self):
        self.label_8.show()
        self.lineEdit_2.show()                
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select SHAPE,THICKNESS,WIDTH,DIAMETER,round(C_A_AREA,2),IN_DIAMETER_MM,OUTER_DIAMETER_MM,PARTY_NAME,GUAGE_LENGTH_MM,PRE_LOAD,MOTOR_SPEED,SPECIMEN_SPECS FROM SPECIMEN_MST WHERE SPECIMEN_NAME='"+self.comboBox.currentText()+"'")                 
        for x in results:
           self.cs_area=int(x[4])        
           self.label_5.setText(x[0])
           
           self.shape=str(x[0])
           self.thickness=str(x[1])
           self.width=str(x[2])
           self.diameter=str(x[3])
           self.cs_area=str(x[4])
           self.inn_dia=str(x[5])
           self.out_dia=str(x[6])
           self.party_name=str(x[7])
           self.guage_mm=str(x[8])
           self.pre_load=str(x[9])
           self.motor_speed=str(x[10])
           self.specs=str(x[11])           
           
           self.label_8.setText(str(x[11]))  #specs
           self.label_10.setText(str(x[7])) #party
           self.label_12.setText(str(x[10])) #motor speed 
           self.label_14.setText(str(x[8])) #guag
           self.label_16.setText(str(x[4])) #cs area
           
           #if(self.test_type=="Flexural"):
                       #self.lineEdit_1_1.setText(str(x[8]))
           
           self.label_15.show()
           self.label_16.show()
           self.label_17.show()
           self.label_18.show()
           self.label_19.show()
           self.label_20.show()           
           
           if (x[0]=="Rectangle"):
               self.label_19.show()
               self.label_20.show()
               self.label_17.setText("Thickness:")
               self.label_18.setText(str(x[1]))
               if(self.test_type != "Tear"):
                       self.label_19.setText("Width:")               
                       self.label_20.setText(str(x[2]))
               else:
                       self.label_19.hide()               
                       self.label_20.hide()
                       self.label_15.hide()               
                       self.label_16.hide()
           elif(x[0]=="Pipe"):    
               self.label_17.setText("In.Diameter:")
               self.label_18.setText(str(x[5]))
               self.label_19.setText("Out.Diameter:")  
               self.label_20.setText(str(x[6]))                            
           elif(x[0]=="Cylindrical"):    
               self.label_17.setText("Diameter:")
               self.label_18.setText(str(x[3]))
               self.label_19.hide()
               self.label_20.hide()                                            
           elif(x[0]=="DirectValue"):    
               self.label_17.hide()
               self.label_18.hide()
               self.label_19.hide()
               self.label_20.hide()
               
        connection.close()
        
        
        
    def reset_job(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        if(self.test_type != "Flexural"):
                self.lineEdit_1_1.setText("0")
                self.lineEdit_2_1.setText("0")
        self.lineEdit_2_1_1.setText("0")
        self.lineEdit_1.setText("0")
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_SCALE_CELL_1,GRAPH_SCALE_CELL_2 FROM SETTING_MST")
        rows=results.fetchall()
        connection.close()
        
        self.lineEdit_1.setText(str(rows[0][0])) #GRAPH_SCALE_CELL_1
        self.lineEdit_2_1_1.setText(str(rows[0][1])) #GRAPH_SCALE_CELL_2
        self.label_23.hide()
    
    def validation(self):
        self.goAhead="No"
        if (self.lineEdit.text() == ""):
            self.label_23.setText(" Job Name Should not Emplty ")    
            self.label_23.show()
        elif(self.comboBox.currentText() == ""):
            self.label_23.setText(" Specimen Name Should not Emplty ")    
            self.label_23.show()
        elif(self.lineEdit_2.text() == ""):
            self.label_23.setText(" Batch Id Should not Emplty ")    
            self.label_23.show()
        elif(self.lineEdit_1.text() == ""):
            self.label_23.setText(" Graph Scale Max Load Should not Emplty ")    
            self.label_23.show()
        elif(self.lineEdit_2_1_1.text() == ""):
            self.label_23.setText(" Graph Scale Max Elongation  Should not Emplty ")    
            self.label_23.show()   
        elif(self.test_type=='Compress'):
                if(self.lineEdit_2_1.text() == ""):
                    self.label_23.setText(" Compressive Length Should not Emplty ")    
                    self.label_23.show()
                elif(int(self.lineEdit_2_1.text() ) <=  0):
                    self.label_23.setText(" Compressive Length Should not be 0 ")    
                    self.label_23.show()
                elif(int(self.lineEdit_2_1.text() ) > int(self.guage_mm)):
                    self.label_23.setText(" Compressive Length Should not be Greater than Guage Length ")    
                    self.label_23.show()                
                elif(self.lineEdit_1_1.text() == ""):
                    self.label_23.setText(" Max Load Should not Emplty ")    
                    self.label_23.show()
                elif(int(self.lineEdit_1_1.text() ) <=  0):
                    self.label_23.setText(" Max Load Should not be 0 ")    
                    self.label_23.show()
                else:
                    self.goAhead="Yes"
        
        elif(self.test_type=='Flexural'):
            if(self.lineEdit_1_1.text() == ""):
                    self.label_23.setText(" Span Should not Emplty ")                    
                    self.label_23.show()
            elif(int(self.lineEdit_1_1.text() ) <=  0):
                    self.label_23.setText(" Span Should not be 0 ")    
                    self.label_23.show()
            else:
                    self.goAhead="Yes"
        else:
             self.goAhead="Yes" 
            
    def open_window(self): 
        #print("Thickness :"+str(self.thickness))
        #print("Width :"+str(self.width))
        #print("cs area :"+str(self.cs_area))
        self.validation()                   
        if(self.goAhead=="Yes"):        
            connection = sqlite3.connect("tyr.db")          
            with connection:        
                cursor = connection.cursor()                    
                cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_MAX_LOAD='"+str(self.lineEdit_1_1.text())+"',NEW_TEST_MAX_LENGTH='"+str(self.max_length)+"',NEW_TEST_SPECIMEN_NAME='"+self.comboBox.currentText()+"',NEW_TEST_SPE_SHAPE='"+self.shape+"', NEW_TEST_THICKNESS='"+self.thickness+"',NEW_TEST_WIDTH='"+self.width+"',NEW_TEST_DIAMETER='"+self.diameter+"',NEW_TEST_INN_DIAMETER='"+self.inn_dia+"',NEW_TEST_OUTER_DIAMETER='"+self.out_dia+"',NEW_TEST_AREA='"+str(self.cs_area)+"',NEW_TEST_PARTY_NAME='"+str(self.party_name)+"',NEW_TEST_MOTOR_SPEED='"+str(self.motor_speed)+"',NEW_TEST_PER_LOAD='"+str(self.pre_load)+"',NEW_TEST_GUAGE_MM='"+str(self.guage_mm)+"',NEW_TEST_JOB_NAME='"+str(self.lineEdit.text())+"',NEW_TEST_BATCH_ID='"+self.lineEdit_2.text()+"',PER_STRAIN_AT_INPUT='"+str(self.lineEdit_2_1.text())+"',SPAN='"+str(self.lineEdit_1_1.text())+"'") 
            connection.commit();
            connection.close()   
            self.load_test_data()
            self.window = QtWidgets.QMainWindow()
            if(self.test_type=='Flexural'):
                    self.ui=TY_02f_Ui_MainWindow()
            else:
                    self.ui=TY_02_Ui_MainWindow()
            self.ui.setupUi(self.window)           
            self.window.show()       
         
    def load_test_data(self):
        
        connection = sqlite3.connect("tyr.db")              
        with connection:        
              cursor = connection.cursor()                                
              cursor.execute("INSERT INTO TEST_MST(TEST_TYPE,SPECIMEN_NAME,JOB_NAME,BATCH_ID,GUAGE_LENGTH,PARTY_NAME,NEW_TEST_MAX_LOAD,NEW_TEST_MAX_LENGTH) SELECT NEW_TEST_NAME,NEW_TEST_SPECIMEN_NAME,NEW_TEST_JOB_NAME,NEW_TEST_BATCH_ID,NEW_TEST_GUAGE_MM,NEW_TEST_PARTY_NAME,NEW_TEST_MAX_LOAD,NEW_TEST_MAX_LENGTH FROM GLOBAL_VAR")                                
        connection.commit();
        connection.close()  
        
        
        connection = sqlite3.connect("tyr.db")
        with connection:        
              cursor = connection.cursor()                                        
              cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID = (SELECT IFNULL(MAX(TEST_ID),1) FROM TEST_MST)")
              cursor.execute("UPDATE SETTING_MST SET GRAPH_SCALE_CELL_1='"+self.lineEdit_1.text()+"',GRAPH_SCALE_CELL_2='"+self.lineEdit_2_1_1.text()+"'")
              cursor.execute("DELETE FROM STG_GRAPH_MST")
        connection.commit();
        connection.close()     
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_01_fluxurl_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
