# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ur_01_TEST_P1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from ur_02_PATIENTS import ur_02_Ui_MainWindow
from ur_03_ADMIN_MENU import ur_03_A_Ui_MainWindow
from ur_06_pop_graph_scales import ur_06_Ui_MainWindow
from ur_12_admin_reports import ur_12_Ui_MainWindow
import datetime
import serial
import time
#import array  as arr
import numpy as np
import sqlite3

class ur_01_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 767)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1340, 726))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.frame.setFont(font)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        
        self.t_var=0.001
        self.voiding_time=""
        self.voiding_time_dev=""        
        self.voided_vol=""        
        self.time_to_max_flow=""
        self.time_to_max_flow_dev=""        
        self.flow_at_2_sec=""
        self.accel=""
        self.total_vol="0"        
        self.max_flow=""
        self.max_flow_dev=""        
        self.avg_flow_dev=""
        self.flow_time=""
        self.hesitancy_time="" #Hesitancy Time – Time of initiation of urination process to the start of the urine stream
        self.second_min_flow_val=""
        
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(300, 10, 201, 91))
        self.groupBox.setObjectName("groupBox")
        self.toolButton_4 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_4.setGeometry(QtCore.QRect(10, 30, 51, 41))
        self.toolButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/stop1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_4.setObjectName("toolButton_4")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QtCore.QRect(90, 40, 71, 31))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 40, 81, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        
        
        self.label_2_2 = QtWidgets.QLabel(self.frame)
        self.label_2_2.setGeometry(QtCore.QRect(790, 5, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_2_2.setFont(font)
        self.label_2_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)       
        self.label_2_2.setObjectName("label_2_2")
        self.label_2_2.setText("UROFLOWMETRY")
        
        
         
        self.label_2_3 = QtWidgets.QLabel(self.frame)
        self.label_2_3.setGeometry(QtCore.QRect(10, 410, 119, 34))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2_3.setFont(font)
        self.label_2_3.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2_3.setObjectName("label_2_3")
        self.label_2_3.setText("Volumn (1000 ml)")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 450, 109, 34))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 500, 109, 34))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(800, 40, 451, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
       
        
        
        self.label_3_1 = QtWidgets.QLabel(self.frame)
        self.label_3_1.setGeometry(QtCore.QRect(540, 10, 89, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_3_1.setFont(font)
        #self.label_3_1.setStyleSheet("background-color: rgb(0, 0, 0);\n color: rgb(170, 0, 0);")
        self.label_3_1.setObjectName("label_3_1")
        self.label_3_1.setText("Flow (ml/sec) ")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(540, 40, 80, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n color: rgb(255, 0, 0);")
        self.lcdNumber.setMidLineWidth(2)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        #self.lcdNumber.hide()
        
      
        
        
        self.label_4_1 = QtWidgets.QLabel(self.frame)
        self.label_4_1.setGeometry(QtCore.QRect(640, 10, 80, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_4_1.setFont(font)
        self.label_4_1.setObjectName("label_4")
        self.label_4_1.setText("Volumn (ml)")
        
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_2.setGeometry(QtCore.QRect(640, 40, 80, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);\n color: rgb(255, 0, 0);")
        self.lcdNumber_2.setMidLineWidth(2)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        
        
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 610, 109, 34))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_3_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3_1.setGeometry(QtCore.QRect(20, 660, 109, 34))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3_1.setFont(font)
        self.pushButton_3_1.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_3_1.setObjectName("pushButton_3_1")
        
        
        
        
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 221, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("color: rgb(0, 0, 255);")
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(130, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setStyleSheet("color: rgb(0, 0, 255);")
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(760, 90, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1200, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_6_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6_1.setGeometry(QtCore.QRect(1200, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6_1.setFont(font)
        self.pushButton_6_1.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_6_1.setObjectName("pushButton_6_1")
        
        self.pushButton_6_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6_2.setGeometry(QtCore.QRect(1200, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6_2.setFont(font)
        self.pushButton_6_2.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_6_2.setObjectName("pushButton_6_2")
       
        self.pushButton_6_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6_3.setGeometry(QtCore.QRect(980, 15, 200, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/ARK LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6_3.setIcon(icon)
        self.pushButton_6_3.setIconSize(QtCore.QSize(230, 210))
        self.pushButton_6_3.setFont(font)        
        self.pushButton_6_3.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_6_3.setObjectName("pushButton_6_3")
       
        
        
        
        
        
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 560, 109, 34))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 410, 109, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(60, 130, 26, 261))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(150, 130, 1181, 571))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget1)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 4)
        self.label_31 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 1, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 1, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 1, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 1, 3, 1, 1)
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
        self.groupBox.setTitle(_translate("MainWindow", "Machine State"))
        self.radioButton.setText(_translate("MainWindow", "On"))
        self.radioButton_2.setText(_translate("MainWindow", "Off"))
       
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.pushButton_5.setText(_translate("MainWindow", "Stop"))
        self.label_2.setText(_translate("MainWindow", "    Test Started Successfully ...."))
        self.label_2.hide()
        self.pushButton_3.setText(_translate("MainWindow", "Discard"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Switch"))
        #self.label_2_1.setText("UROMETRY MACHINE")
        self.radioButton_5.setText(_translate("MainWindow", "On"))
        self.radioButton_6.setText(_translate("MainWindow", "Off"))
        self.label_30.setText(_translate("MainWindow", "16 Jan 2020 12:14:15"))
        self.pushButton_6.setText(_translate("MainWindow", "Admin"))
        self.pushButton_6_1.setText("Graph Scales")
        self.pushButton_7.setText(_translate("MainWindow", "Save"))
        self.pushButton_8.setText(_translate("MainWindow", "Set all 0"))
        self.label_31.setText(_translate("MainWindow", "Max Flow(ml/sec):"))
        self.label_32.setText(_translate("MainWindow", "0                                                                                                                             "))
        self.label_33.setText(_translate("MainWindow", "Elapsed Time (Sec.):"))
        self.label_34.setText(_translate("MainWindow", "00.0000"))
        self.pushButton_6_2.setText("Reports")
        self.pushButton_3_1.setText("Zero")
       
        self.pushButton_3.clicked.connect(self.blank_graph)
        self.pushButton_4.clicked.connect(self.start_test)
        self.pushButton_5.clicked.connect(self.stop_test)
        self.pushButton_7.clicked.connect(self.open_new_window)
        self.radioButton_5.clicked.connect(self.ON_set)
        self.radioButton_6.clicked.connect(self.OFF_set)
        self.pushButton_6.clicked.connect(self.open_new_window2)
        self.pushButton_6_1.clicked.connect(self.open_new_window3)
        self.pushButton_6_2.clicked.connect(self.open_new_window7)
        self.pushButton_3_1.clicked.connect(self.set_low_fun)
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.timer8=QtCore.QTimer()
        self.timer9=QtCore.QTimer()
        
        
               
        self.blank_graph()
        self.pushButton_3.setDisabled(True)
        self.pushButton_3_1.setDisabled(True)
        
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setDisabled(True)
        self.progressBar.setDisabled(True)
        self.pushButton_8.hide()

    def device_date(self):     
        self.label_30.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def set_low_fun(self):
        try:
            self.ser = serial.Serial(
                                port='/dev/ttyAMA0',
                                baudrate=115200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.05
                            )        
            self.ser.flush()           
            #=======
            self.command_str="Z"
            print("Start Command : "+str(self.command_str))
            b = bytes(self.command_str, 'utf-8')
            self.ser.write(b)
            self.progressBar.setValue(0)
            self.lcdNumber.setProperty("value", 0)
            self.lcdNumber_2.setProperty("value",0) 
            
        except IOError:
            print("IO Errors")
            
    
    def open_new_window7(self):       
        self.window = QtWidgets.QMainWindow()      
        self.ui=ur_12_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def blank_graph(self):
        self.graph_blank =PlotCanvas_blank(self,width=5, height=2)                
        self.gridLayout.addWidget(self.graph_blank, 0, 0, 1, 4)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_7.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_3_1.setEnabled(True)
        self.label_34.setText("0")
        self.label_32.setText("0")
        self.label_2.setText("Ready to start test")
        self.label_2.show()
        self.progressBar.setValue(0)
        self.label_31.hide()
        self.label_32.hide()
        
        
    def check_machine_status(self):
        m_connection = ""
        try:
            self.ser = serial.Serial(
                                port='/dev/ttyAMA0',
                                baudrate=115200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.05
                            )
            '''
            self.line_chk = self.ser.readline()
            print("self.line_chk:"+str(self.line_chk))
            if(str(self.line_chk)=="b''") :
                m_connection = 'DEACTIVE'  
            else:
            '''
            m_connection = 'ACTIVE'
        except IOError:                
                print("IO Error")
                m_connection = 'DEACTIVE'  
        
        if(m_connection == 'ACTIVE'):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("./images/on_button.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.toolButton_4.setIcon(icon)
                self.radioButton.setChecked(True)
                self.radioButton_2.setChecked(False)
        else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("./images/stop1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.toolButton_4.setIcon(icon)
                self.radioButton.setChecked(False)
                self.radioButton_2.setChecked(True)
        
        m_connection = ""
                
    def check_load_cell_status(self):
        l_connection = ""        
        try:
            self.ser = serial.Serial(
                                port='/dev/ttyUSB0',
                                baudrate=115200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.05
                            )
            '''
            for i in range(10):
                self.ser.flush()           
                self.xz = self.ser.readline()
                self.xstr01=str(self.xz,'utf-8')
                self.xstr11=self.xstr01.replace("'\\r","")
                self.xstr21=self.xstr11.replace("'\\n","")
                if(len(self.xstr21) > 2):
                    if(int(self.xstr21) >= 0):
                        l_connection = "ACTIVE"
                    else:
                        l_connection = "DEACTIVE"
                else:
                        l_connection = "DEACTIVE"
            '''
            l_connection = "ACTIVE"
        except IOError:                
                l_connection = 'DEACTIVE' 
        
        icon1 = QtGui.QIcon()
        if(l_connection == 'ACTIVE'):           
             icon1.addPixmap(QtGui.QPixmap("./images/connected.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
             #self.toolButton_5.setIcon(icon1)
             #self.radioButton_3.setChecked(True)
             #self.radioButton_4.setChecked(False)
        else:            
             icon1.addPixmap(QtGui.QPixmap("./images/off_loadcell.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
             #self.toolButton_5.setIcon(icon1)
             #self.radioButton_3.setChecked(True)
             #self.radioButton_4.setChecked(False)
        print("l_connection : "+str(l_connection))
        l_connection = ""   
    #def stop_basic_timers(self):
    
    
    #def stop_graph_timers(self):
    
     
    
    
    def start_test(self):         
        self.check_machine_status()
        self.check_load_cell_status()       
        self.pushButton_4.setDisabled(True)        
        self.pushButton_3_1.setDisabled(True)
        
        self.start_plot =PlotCanvas_Auto(self,width=5, height=4, dpi=80)
        self.gridLayout.addWidget(self.start_plot, 0, 0, 1, 4)
        self.pushButton_5.setEnabled(True)
       
        
        
        self.timer3=QtCore.QTimer()
        self.timer3.setInterval(1000)        
        self.timer3.timeout.connect(self.show_progress_bar)
        self.timer3.start(1)
        
        self.label_2.setText("Test started.")
        self.label_2.show()
 
    def stop_test(self):
        self.pushButton_5.setDisabled(True)
        self.start_plot.on_stop()
        self.label_2.setText("Test stopped. Save/Discard Test data ")
        self.label_2.show()
        self.pushButton_3.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        if(self.timer3.isActive()): 
                   self.timer3.stop()                                                                                                      
                   print("Time 3 has been stopped ")
                   self.save_test_data_tmp()
                   
    def save_test_data_tmp(self):
        if(len(self.start_plot.arr_p) > 0 ):            
            connection = sqlite3.connect("ur.db")              
            with connection:        
                        cursor = connection.cursor()                                
                        cursor.execute("DELETE FROM GRAPH_MST_TMP")
                        cursor.execute("DELETE FROM GRAPH_MST_TMP2")
                        cursor.execute("UPDATE GLOBAL_VAR_TEST SET TEST_ID='0',ELAPSED_TIME='',MAX_FLOW=''")
                        cursor.execute("UPDATE GLOBAL_VAR_TEST SET TEST_START_ON='',TEST_END_ON='', AVG_FLOW='' ,VOIDING_TIME=''")
                        cursor.execute("UPDATE GLOBAL_VAR_TEST SET FLOW_TIME='',TIME_TO_MAX_FLOW='', VOIDED_VOL='' , FLOW_AT_2_SEC='' ,ACCEL='', TOTAL_VOLUMN=''")
                        cursor.execute("UPDATE GLOBAL_VAR_TEST SET MAX_FLOW_DEV='',AVG_FLOW_DEV='',VOIDING_TIME_DEV='',TIME_TO_MAX_FLOW_DEV='', HESITANCY_TIME='' ")                        
     
            connection.commit();
            connection.close() 
            
            connection = sqlite3.connect("ur.db")              
            with connection:        
                        cursor = connection.cursor()  
                        for i in range(len(self.start_plot.arr_p)):
                                 cursor.execute("INSERT INTO GRAPH_MST_TMP(X_NUM,Y_NUM) VALUES ('"+str(self.start_plot.arr_p[i])+"','"+str(self.start_plot.arr_q[i])+"')")                                
                        for i in range(len(self.start_plot.arr_p2)):                                 
                                 cursor.execute("INSERT INTO GRAPH_MST_TMP2(X_NUM,Y_NUM) VALUES ('"+str(self.start_plot.arr_p2[i])+"','"+str(self.start_plot.arr_q2[i])+"')")
            connection.commit();
            connection.close()
              
            print(" temp tables populated !!!")
            self.test_calcs()
            
            print("Calculations populated !!!")
        else:
            print("Arrays are not yet populated.")
            
    def test_calcs(self):
        self.test_id="1"
        connection = sqlite3.connect("ur.db")
        results=connection.execute("select seq+1 from sqlite_sequence where name = 'TEST_MST'")
        for x in results:           
                 #self.label_2.setText(str(x[0]).zfill(3))
                 self.test_id=str(x[0]).zfill(7)
        connection.close()
        
         
        
        self.start_flow_idx=0
        self.stop_flow_idx=0
        self.max_flow_idx=0
        self.voiding_time=0
        
        self.voiding_time=0
        self.time_to_max_flow=0
        self.total_vol=0
        self.flow_time=0
        
        self.flow_sd=0
        self.flow_time_sd=0
        self.volumn_sd=0
        self.volumn_time_sd=0
        self.flow_at_2_sec=0
        self.rev_cnt=0
        self.max_flow=0
        self.accel="0"
        self.avg_flow=0
        
        if(len(self.start_plot.arr_q2) > 0 and len(self.start_plot.arr_q) > 0 ):
               #self.max_flow=float(max(self.start_plot.arr_q2))
               self.flow_sd=np.std(self.start_plot.arr_q2)
               self.flow_time_sd=np.std(self.start_plot.arr_p2)
               self.volumn_sd=np.std(self.start_plot.arr_q)
               self.volumn_time_sd=np.std(self.start_plot.arr_p)
               
               for x in range(len(self.start_plot.arr_q2)):
                    if(float(self.start_plot.arr_q2[x]) > 0  and int(self.start_flow_idx) == 0) :
                                    self.start_flow_idx=int(x)            
               for x in reversed(self.start_plot.arr_q2):
                    self.rev_cnt=self.rev_cnt+1
                    if(float(x) > 0  and int(self.stop_flow_idx) == 0) :
                              self.stop_flow_idx=len(self.start_plot.arr_q2)-int(self.rev_cnt)
               
               for y in range(len(self.start_plot.arr_q2)):                   
                    if(float(self.start_plot.arr_q2[y]) == float(self.max_flow) and  int(self.max_flow_idx) == 0):
                                     self.max_flow_idx=int(y)
                                     print("Max flow indx :"+str(self.max_flow_idx)+" Max Flow :"+str(self.start_plot.arr_q2[self.max_flow_idx])+" Max flow time :"+str(self.start_plot.arr_p2[self.max_flow_idx]))
                                     
                                     
              
               self.voiding_time=float(self.start_plot.arr_p2[self.stop_flow_idx]) - float(self.start_plot.arr_p2[self.start_flow_idx])               
               self.time_to_max_flow=float(self.start_plot.arr_p2[self.max_flow_idx])
               #print(" max flow :")
               if(float(self.time_to_max_flow) < 0):
                   self.time_to_max_flow=self.time_to_max_flow*(-1)
               self.total_vol=float(self.voided_vol)
               #self.flow_time=float(self.voiding_time)
               
               print("Start flow Time :"+str(float(self.start_plot.arr_p2[self.start_flow_idx])))
               print("Stop flow Time :"+str(float(self.start_plot.arr_p2[self.stop_flow_idx]))) 
               
               
               
               
               started_time=""
               flow_x_time="0"
               started_time="0"
               stoped_time="0"
               flow_x_time_curr="0"
               flow_x_time="0"

               connection = sqlite3.connect("ur.db")        
               results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST_TMP2 order by REC_ID ASC")
               for x in results:
                     #print(str(x[0])+":"+str(x[1]))
                     if(float(x[1]) > 0 ):
                                #print(str(x[0])+":"+str(x[1]))
                                status="started"
                                stoped_time="0"
                                if(started_time == "0"):
                                        started_time=str(x[0])
                                                  
                     else:
                                #print(str(x[0])+":"+str(x[1]))
                                status="stopped"                                 
                                if(stoped_time == "0"):
                                        stoped_time=str(x[0])

                     #print("started_time: "+str(started_time)+" stoped_time:"+str(stoped_time))
                     if( float(started_time) > 0 and float(stoped_time) > 0):
                                        flow_x_time_curr=float(str(stoped_time))-float(str(started_time))
                                        flow_x_time=float(flow_x_time)+float(flow_x_time_curr)
                                        #print("flow_x_time_curr :"+str(float(flow_x_time_curr))+"started_time: "+str(float(started_time))+" stoped_time:"+str(float(stoped_time)))
                                        started_time="0"
                                        stoped_time="0"
               connection.close()
               print("Total flow_time  Time :"+str(flow_x_time))
               self.flow_time=float(flow_x_time)
               connection = sqlite3.connect("ur.db")        
               results=connection.execute("SELECT MAX(Y_NUM),AVG(Y_NUM) FROM GRAPH_MST_TMP2 where Y_NUM > 0")
               for x in results:
                      print(" Max Flow :"+str(x[0])+"   Avg Flow :"+str(x[1]))
                      self.max_flow=float(x[0])     
                      self.avg_flow=float(x[1]) 
               connection.close()
               
               connection = sqlite3.connect("ur.db")        
               results=connection.execute("SELECT IFNULL(X_NUM,0),Y_NUM FROM GRAPH_MST_TMP2 where Y_NUM ='"+str(self.max_flow)+"'")
               for x in results:
                      print(" Max Flow xxx :"+str(x[1])+"   Time To Max Flow xxx:"+str(x[0]))
                      self.time_to_max_flow=float(x[0])
               connection.close()
        else:
               print("Data is not populated") 
                                                          

        
        
        print(" Voiding Time:"+str(self.voiding_time))        
       
        if(int(self.voiding_time) > int(self.flow_time_sd)):             
             self.voiding_time_dev=float(self.voiding_time)-float(self.flow_time_sd)
             self.voiding_time_dev=(float(self.voiding_time_dev)/float(self.flow_time_sd))*100             
        else:     
             self.voiding_time_dev=float(self.flow_time_sd)-float(self.voiding_time)
             self.voiding_time_dev=(float(self.voiding_time_dev)/float(self.flow_time_sd))*100
        
        
        if(int(self.time_to_max_flow) > int(self.flow_time_sd)):             
             self.time_to_max_flow_dev=float(self.time_to_max_flow)-float(self.flow_time_sd)
             self.time_to_max_flow_dev=(float(self.time_to_max_flow_dev)/float(self.flow_time_sd))*100             
        else:     
             self.time_to_max_flow_dev=float(self.flow_time_sd)-float(self.time_to_max_flow)
             self.time_to_max_flow_dev=(float(self.time_to_max_flow_dev)/float(self.flow_time_sd))*100
        
        
        if(int(self.max_flow) > int(self.flow_sd)):             
             self.max_flow_dev=float(self.max_flow)-float(self.flow_sd)
             self.max_flow_dev=(float(self.max_flow_dev)/float(self.flow_sd))*100             
        else:     
             self.max_flow_dev=float(self.flow_sd)-float(self.max_flow)
             self.max_flow_dev=(float(self.max_flow_dev)/float(self.flow_sd))*100
             
        if(float(self.avg_flow) > float(self.flow_sd)):             
             self.avg_flow_dev=float(self.avg_flow)-float(self.flow_sd)
             self.avg_flow_dev=(float(self.avg_flow_dev)/float(self.flow_sd))*100             
        else:     
             self.avg_flow_dev=float(self.flow_sd)-float(self.avg_flow)
             self.avg_flow_dev=(float(self.avg_flow_dev)/float(self.flow_sd))*100
              
        if(len(self.start_plot.arr_p2) > 0):
            connection = sqlite3.connect("ur.db")        
            results=connection.execute("SELECT count(REC_ID) FROM GRAPH_MST_TMP2 WHERE X_NUM <= '"+str(float((self.start_plot.arr_p2[self.start_flow_idx])+2))+"'")
            for x in results:
                    print(" i :"+str(x[0])+" length of arr_q2 :"+str(len(self.start_plot.arr_p2)))
                    self.flow_at_2_sec=str(float(self.start_plot.arr_p2[int(x[0]-1)]))        
            connection.close()
            if(int(self.time_to_max_flow) > 0):
                self.accel=(float(max(self.start_plot.arr_q2)))/int(self.time_to_max_flow)
            else:
                self.accel="0"    
        
        connection = sqlite3.connect("ur.db")              
        with connection:        
                cursor = connection.cursor()                                
                cursor.execute("UPDATE GLOBAL_VAR_TEST SET TEST_ID='"+str(self.test_id)+"',ELAPSED_TIME='"+str(self.label_34.text())+"',MAX_FLOW='"+str(self.label_32.text())+"'")
                cursor.execute("UPDATE GLOBAL_VAR_TEST SET TEST_START_ON='"+str(self.test_start_date)+"',TEST_END_ON='"+str(self.test_end_date)+"', AVG_FLOW='"+str(self.avg_flow)+"' ,VOIDING_TIME='"+str(self.voiding_time)+"' ")
                #cursor.execute("UPDATE GLOBAL_VAR_TEST SET TEST_START_ON='"+str(self.test_start_date)+"',TEST_END_ON='"+str(self.test_end_date)+"', AVG_FLOW='"+str(self.time_to_max_flow)+"' ,VOIDING_TIME='"+str(self.voiding_time)+"' ")
                cursor.execute("UPDATE GLOBAL_VAR_TEST SET FLOW_TIME='"+str(self.flow_time)+"',TIME_TO_MAX_FLOW='"+str(self.time_to_max_flow)+"', VOIDED_VOL='"+str(self.voided_vol)+"' , FLOW_AT_2_SEC='"+str(self.flow_at_2_sec)+"' ,ACCEL='"+str(self.accel)+"', TOTAL_VOLUMN='"+str(self.total_vol)+"'")                  
                cursor.execute("UPDATE GLOBAL_VAR_TEST SET MAX_FLOW_DEV='"+str(self.volumn_sd)+"',AVG_FLOW_DEV='"+str(self.flow_sd)+"',VOIDING_TIME_DEV='"+str(self.voiding_time_dev)+"',TIME_TO_MAX_FLOW_DEV='"+str(self.time_to_max_flow_dev)+"' , HESITANCY_TIME='"+str(self.hesitancy_time)+"' ")                  
                
        connection.commit()
        connection.close()
        #self.start_plot.axes2.set_title('Max Flow:'+str(self.max_flow)+" Avg. Flow :"+str(self.avg_flow))
        #self.start_plot.axes2.set_title('Max Flow: Avg. Flow :')
        self.label_31.setText("  Flow Time: <font color=blue>"+str(round(self.flow_time,2))+" sec.</font>  Voided Time:<font color=blue>"+str(round(self.voiding_time,2))+" sec.</font> Voided Vol:<font color=blue> "+str(self.voided_vol)+" ml. </font>")
        self.label_32.setText("  Max.Flow:<font color=blue>"+str(round(self.max_flow,2))+" ml/sec </font>  Avg.Flow: <font color=blue>"+str(round(self.avg_flow,2))+"ml/sec </font>")
        self.label_31.show()
        self.label_32.show()
        
        print("Calculations are populated.")
        
    def show_progress_bar(self):
        #print(" inside progress bar  length of arr_p:"+str(len(self.start_plot.arr_p)))        
        if(len(self.start_plot.arr_p) > 0):
                if(int(self.start_plot.curr_vol) > 0 ):
                    per_val=(int(self.start_plot.curr_vol)/1000)*100
                    self.progressBar.setValue(per_val)
                    self.lcdNumber.setProperty("value", int(self.start_plot.flow_val))
                    self.lcdNumber_2.setProperty("value",int(self.start_plot.curr_vol))                     
                else:
                    self.progressBar.setValue(0)
                    self.lcdNumber.setProperty("value", 0)
                    self.lcdNumber_2.setProperty("value",0) 
                    
                self.test_start_date=self.start_plot.start_time
                #self.elap_time=datetime.datetime.now()-self.start_plot.start_time
                self.test_end_date=datetime.datetime.now()
                self.hesitancy_time=str(self.start_plot.h_time) 
                '''
                if(int(len(self.start_plot.arr_q)) > 0):
                    self.avg_flow=str(round(float(max(self.start_plot.arr_q2)))/round(float(max(self.start_plot.arr_p))))
                else:
                    self.avg_flow=0
                '''    
                self.label_34.setText(str(self.start_plot.elap_time))
                
                if(len(self.start_plot.arr_q2) > 0):
                    self.label_32.setText(str(round(float(max(self.start_plot.arr_q2)))))
                    self.max_flow=str(self.label_32.text())            
                else:
                    self.label_32.setText("0")
                    
                if(len(self.start_plot.arr_q) > 0):
                    self.voided_vol=str(round(float(max(self.start_plot.arr_q))))
                else:
                    self.label_32.setText("0")    
    
    def getserial(self):
        # Extract serial from cpuinfo file
        cpuserial = "0000000000000000"
        try:
           f = open('/proc/cpuinfo','r')
           for line in f:
                if line[0:6]=='Serial':
                   cpuserial = line[10:26]
           f.close()
        except:
           cpuserial = "ERROR000000000"
        return cpuserial
 
    def ON_set(self): 
        #print ("self.radioButton_5.isChecked :"+str(self.radioButton_5.isChecked()))
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("services.db")
        results=connection.execute("select DEVICE_SERIAL_NO from DAT_MST") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))       
           if(serial_no == str(x[0])):
               self.go_ahead="Yes"
           else:
               self.go_ahead="No"
        connection.close()       
        if(self.go_ahead =="Yes"):
                 if(self.radioButton_5.isChecked()):
                    
                    self.radioButton_5.setChecked(True) #on
                    self.radioButton_6.setChecked(False) #off
                    #self.pushButton_3.setEnabled(True)
                    self.pushButton_4.setEnabled(True)
                    self.pushButton_3_1.setEnabled(True)
                    #self.pushButton_5.setEnabled(True)
                    #self.pushButton_7.setEnabled(True)
                    self.pushButton_8.setEnabled(True)
                    self.progressBar.setEnabled(True)
                    self.check_machine_status()
                    self.check_load_cell_status()
                    self.label_2.setText("Ready to start test")
                    self.label_2.show() 
                   
                 else:
                    self.radioButton_5.setChecked(True) #on
                    self.radioButton_6.setChecked(False) #off
                    self.pushButton_3.setDisabled(True)            
                    self.pushButton_4.setDisabled(True)
                    self.pushButton_3_1.setDisabled(True)
                    self.pushButton_5.setDisabled(True)
                    self.pushButton_7.setDisabled(True)
                    self.pushButton_8.setDisabled(True)
                    self.progressBar.setDisabled(True)
        else:
                 self.label_2.setText("Registration invalid.")
                 self.label_2.show()
            
           
            
    def OFF_set(self):
        #print ("self.radioButton_6.isChecked :"+str(self.radioButton_6.isChecked()))
        self.blank_graph()
        if(self.radioButton_6.isChecked()):            
            self.radioButton_6.setChecked(True) #off
            self.radioButton_5.setChecked(False) #on
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setDisabled(True)
            self.pushButton_3_1.setDisabled(True)
            self.pushButton_5.setDisabled(True)
            self.pushButton_7.setDisabled(True)
            self.pushButton_8.setDisabled(True)
            self.progressBar.setDisabled(True)            
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("./images/stop1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.toolButton_4.setIcon(icon)
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            
            
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("./images/off_loadcell.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            #self.toolButton_5.setIcon(icon1)
            #self.radioButton_3.setChecked(False)
            #self.radioButton_4.setChecked(True)
            self.label_2.setText("System is offline now")
            self.label_2.show()
            
           
           
        else:
            
            #self.radioButton_5.setChecked(True) #off
            self.radioButton_6.setChecked(False) #on
            #self.pushButton_3.setEnabled(True)  
            self.pushButton_4.setEnabled(True)
            self.pushButton_3_1.setEnabled(True)
            #self.pushButton_5.setEnabled(True)
            #self.pushButton_7.setEnabled(True)
            self.pushButton_8.setEnabled(True)
            self.progressBar.setEnabled(True)
            self.check_machine_status()
            self.check_load_cell_status()
            self.label_2.setText("Ready to start test")
            self.label_2.show() 
            
       
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=ur_02_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=ur_03_A_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window3(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=MyWindow()
        self.ui=ur_06_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        



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
        self.plot_blank()        
        
    def plot_blank(self):                
        
        connection = sqlite3.connect("ur.db")              
        with connection:        
                cursor = connection.cursor()                            
                cursor.execute("DELETE FROM GRAPH_MST_TMP ")                            
        connection.commit()
        connection.close()
        
        self.x=[0,0,0,0,0,0,0,0]
        self.y=[0,0,0,0,0,0,0,0]
        
        self.p=list()
        self.q=list()
      
        ax = self.figure.add_subplot(211)
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
        
        
        
       
        for i in range(len(self.x)):
              self.p.append(self.x[i])
              self.q.append(self.y[i])  
              
        ax.plot(self.x,self.y,'b')
        ax.set_ylabel('Flow (ml/sec)')
        ax.set_xlabel('Time (sec)')
        
        
        #------------------------------------
        
        self.x1=[0,0,0,0,0,0,0,0]
        self.y1=[0,0,0,0,0,0,0,0]
        
        self.p1=list()
        self.q1=list()
       
        ax = self.figure.add_subplot(212)
        #ax.set_facecolor('#CCFFFF')
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth='0.2', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.2', color='black')
        
        connection = sqlite3.connect("ur.db")
        #results=connection.execute("SELECT FLOW_TIME_Y_AXIS,VOLUMN_TIME_Y_AXIS,FLOW_TIME_X_AXIS,VOLUMN_TIME_X_AXIS FROM OTER_INFO")
        results=connection.execute("SELECT VOLUMN_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS FROM OTER_INFO")
        rows=results.fetchall()
        ax.set_xlim(0,int(rows[0][1]))
        ax.set_ylim(0,int(rows[0][0]))
        connection.close()
        
       
       
        for i in range(len(self.x1)):
              self.p1.append(self.x[i])
              self.q1.append(self.y[i])  
              
        ax.plot(self.x1,self.y1,'b')
        ax.set_ylabel('Volumn (ml)')
        ax.set_xlabel('Time (sec)')
        
        
        self.draw() 

class PlotCanvas_Auto(FigureCanvas):     
    def __init__(self, parent=None, width=5, height=4, dpi=80):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(212)
        self.axes2 = fig.add_subplot(211)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)
        self.start_time = datetime.datetime.now()
        
        self.timer6=QtCore.QTimer()
       
        self.flow_val=0
        self.curr_vol=0
        self.h_time=0
        self.plot_auto()
         
    def compute_initial_figure(self):
        pass
      
    def xupdate_graph(self):       
        try:
            self.v_cnt=self.v_cnt+1           
            self.ser.flush()           
            self.line = self.ser.readline()
            print("self.line:"+str(self.line,'utf-8'))
            self.xstr0=str(self.line,'utf-8')
            self.xstr1=self.xstr0.replace("\r","")
            self.xstr2=self.xstr1.replace("\n","")
            self.buff=self.xstr2.split("_")
            #print(" array :"+str(self.buff))
            
            #print("ok  xx   :"+str(self.xstr2))           
            if(self.IO_error_flg==0):                
                if(len(self.buff)> 2):
                        if(str(self.buff[3]) == 'R'): 
                                #print("o/p xx:"+str(self.xstr3))
                                self.xstr3=str(self.buff[0])
                                #print("o/p xx:"+str(self.xstr3))
                                  
                                self.elap_time=float(self.buff[2])
                                self.p=float( self.elap_time)                               
                                self.q=float(self.buff[0])
                                self.q2=float(self.buff[1])
                                        
                                self.arr_p.append(self.p)                                
                                self.arr_q.append(self.q)
                                        
                                self.flow_val=float(self.buff[1])
                                self.curr_vol=float(self.buff[0])
                                        
                                self.arr_p2.append(float(self.p))
                                self.arr_q2.append(float(self.q2))
                                        
                                #print(" Array P:"+str(self.arr_p))
                                #print(" Array Q:"+str(self.arr_q))
                                
                                #print(" Array P2:"+str(self.arr_p2))
                                #print(" Array Q2:"+str(self.arr_q2))
                                
                                '''
                                print(" length Array P:"+str(len(self.arr_p)))
                                print(" length Array Q:"+str(len(self.arr_q)))
                                
                                print(" length Array P2:"+str(len(self.arr_p2)))
                                print(" length Array Q2:"+str(len(self.arr_q2)))
                                '''
                        else:
                                print(" not Running status ")
                                self.h_time=float(self.buff[2])
                                  
        except IOError:
                    print("IO Errors") 
        
       
     
    def plot_auto(self):        
        #self.axes.set_facecolor('#CCFFFF')
        self.v_cnt=0
        self.t=0
        self.xstr3=""
        self.playing = False
        self.IO_error_flg=0
        self.IO_error_flg2=0
        self.axes.minorticks_on()
        self.axes.set_xlabel('Time (sec)')
        self.axes.set_ylabel('Volumn (ml)')
        self.axes.set_autoscale_on(True)
        
        connection = sqlite3.connect("ur.db")
        #results=connection.execute("SELECT FLOW_TIME_Y_AXIS,VOLUMN_TIME_Y_AXIS,FLOW_TIME_X_AXIS,VOLUMN_TIME_X_AXIS FROM OTER_INFO")
        results=connection.execute("SELECT VOLUMN_TIME_Y_AXIS,VOLUMN_TIME_X_AXIS FROM OTER_INFO")
        rows=results.fetchall()
        self.axes.set_xlim(0,int(rows[0][1]))
        self.axes.set_ylim(0,int(rows[0][0]))
        connection.close()
        #self.axes.set_xlim(0,120)
        #self.axes.set_ylim(0,1000)
        
        
        self.axes.grid(which='major', linestyle='-', linewidth='0.2', color='red')
        self.axes.grid(which='minor', linestyle=':', linewidth='0.2', color='black')
        self.line_cnt, = self.axes.plot([], [], animated=True, lw=1.5,color='#04756A')
        self.p=0
        self.q=0
        self.arr_p=[]
        self.arr_q=[]
        self.xlim=0
        self.ylim=120
        #print("Weight Started ....")
        #########
        self.axes2.minorticks_on()
        self.axes2.set_xlabel('Time (sec)')
        self.axes2.set_ylabel('Flow (ml/sec)')
        connection = sqlite3.connect("ur.db")       
        results=connection.execute("SELECT FLOW_TIME_Y_AXIS,FLOW_TIME_X_AXIS FROM OTER_INFO")        
        for x in results:
                self.axes2.set_xlim(0,int(x[1]))
                self.axes2.set_ylim(0,int(x[0]))
        connection.close()
        
        #self.axes2.set_xlim(0,120)
        #self.axes2.set_ylim(0,60)
        #self.axes2.set_title('Flow Graph')
        self.axes2.grid(which='major', linestyle='-', linewidth='0.2', color='red')
        self.axes2.grid(which='minor', linestyle=':', linewidth='0.2', color='black')        
        self.line_cnt2, = self.axes2.plot(0, 0, animated=True, lw=1.5 , color='#04756A')
        self.p2=0
        self.q2=0        
        self.p2_prv=0
        self.q2_prv=0
        self.arr_p2=[]
        self.arr_q2=[]
        self.x2lim=0
        self.y2lim=0
        try:
            self.ser = serial.Serial(
                                port='/dev/ttyAMA0',
                                baudrate=115200,
                                bytesize=serial.EIGHTBITS,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                xonxoff=False,
                                timeout = 0.05
                            )
        
            self.ser.flush()
           
            #=======
            self.command_str="T"
            print("Start Command : "+str(self.command_str))
            b = bytes(self.command_str, 'utf-8')
            self.ser.write(b)
           
            #=======
            self.command_str="S"
            print("Start Command : "+str(self.command_str))
            b = bytes(self.command_str, 'utf-8')
            self.ser.write(b)
            #======
            #self.axes.plot(self.arr_p,self.arr_q)
            self.line = self.ser.readline()
            print("o/p:"+str(self.line))
            #self.axes.plot(self.arr_p,self.arr_q)
            self.start_time = datetime.datetime.now()
            #self.t_var=0.1
            self.timer6.setInterval(10)        
            self.timer6.timeout.connect(self.xupdate_graph)
            self.timer6.start(10)
            self.on_start()
            
            
        except IOError:
            print("IO Errors")
            self.IO_error_flg=1
            self.IO_error_flg2=1  
    
        
    def on_start(self):    
        if self.playing:
            pass
        else:
            self.playing = True
            self.ani = animation.FuncAnimation(
                self.figure,
                self.plot_grah_only,
                blit=True, interval=10
                    )
            print("Done1")
           
            self.ani_2 = animation.FuncAnimation(
                self.figure,
                self.plot2_grah_only,
                blit=True, interval=10
                    )
            print("Done2")
           
    
    def plot_grah_only(self,i):        
        self.line_cnt.set_data(self.arr_p,self.arr_q) 
        return [self.line_cnt]
    
    def plot2_grah_only(self,i):
        self.line_cnt2.set_data(self.arr_p2,self.arr_q2) 
        return [self.line_cnt2]
    
    
        
        
    def on_stop(self):
        if self.playing:
            
            self.command_str="T"
            print("Stop Command : "+str(self.command_str))
            b = bytes(self.command_str, 'utf-8')
            self.ser.write(b)
            
            self.playing = False
            self.end_time = time.time()
            self.ani._stop()
            self.ani_2._stop()
            print("ani stopped !!!")
            if(self.timer6.isActive()): 
                   self.timer6.stop()                                                                                                      
                   print("Time 6 has been stopped ")
                   
        else:
            pass
        
        
    
    def print_fun(self):        
        self.t_var=float(self.t_var)+0.1
        
    
    def actual_plot_graph(self):
        self.axes.plot(self.arr_p,self.arr_q)
        self.axes.set_ylim(0,self.ylim)
        self.axes.relim()
        self.draw()


  
class MyWindow(QtWidgets.QMainWindow):       
        def closeEvent(self,event):
            self.show()
            event.accept()

        def r_fresh(self):
            self.refresh()
            
            
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ur_01_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
