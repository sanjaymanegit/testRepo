'''


from urmini_06_menu_list import urmini_06_Ui_MainWindow

'''
from urmini_11_patient_save import Urmini_11_MainWindow
from urmini_15_scales import urmini_15_MainWindow
from urmini_07_report_list import urmini_07_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt
'''
from ur_03_ADMIN_MENU import ur_03_A_Ui_MainWindow
from ur_06_pop_graph_scales import ur_06_Ui_MainWindow
from ur_12_admin_reports import ur_12_Ui_MainWindow
'''
import datetime
import serial
import time
#import array  as arr
import numpy as np
import sqlite3


class Urmini_01_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 640)
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 981, 571))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(830, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(270, 50, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(3)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_2.setGeometry(QtCore.QRect(490, 50, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_2.setLineWidth(3)
        self.lcdNumber_2.setDigitCount(3)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 140, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 210, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 85, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 280, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"")
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 350, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setDefault(True)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 490, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(231, 154, 115);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(270, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(490, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 420, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(270, 120, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(710, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_6.setObjectName("label_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(850, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(231, 154, 115);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(710, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(231, 154, 115);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 160, 801, 406))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 211, 111))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("./images/ARK LOGO.jpg"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(840, 120, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
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
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.pushButton_5.setText(_translate("MainWindow", "Reset"))
        self.pushButton_6.setText(_translate("MainWindow", "Menu"))
        self.label_3.setText(_translate("MainWindow", "Flow (ml/sec)"))
        self.label_4.setText(_translate("MainWindow", "Volume (ml)"))
        self.pushButton_7.setText(_translate("MainWindow", "Zero"))
        self.label_5.setText(_translate("MainWindow", "Pleasse start test."))
        self.label_6.setText(_translate("MainWindow", "Elapsed Time (sec):"))
        self.pushButton_8.setText(_translate("MainWindow", "Reports"))
        self.pushButton_9.setText(_translate("MainWindow", "Scales"))
        self.label_2.setText(_translate("MainWindow", "Results :"))
        self.label_8.setText(_translate("MainWindow", "30.9"))
        
        self.pushButton_2.clicked.connect(self.start_test)
        self.pushButton_3.clicked.connect(self.stop_test)
        self.pushButton_4.clicked.connect(self.open_new_window)
        self.pushButton_5.clicked.connect(self.blank_graph)
        self.pushButton_7.clicked.connect(self.set_low_fun)
        self.pushButton_8.clicked.connect(self.open_new_window2)
        self.pushButton_6.clicked.connect(self.open_new_window3)
        self.pushButton_9.clicked.connect(self.open_new_window4)
        self.blank_graph()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)

    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def blank_graph(self):
        self.graph_blank =PlotCanvas_blank(self,width=5, height=2)
        self.gridLayout.addWidget(self.graph_blank, 0, 0, 1, 1)       
       
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        #self.pushButton_3_1.setEnabled(True)
        #self.label_34.setText("0")
        #self.label_32.setText("0")
        self.label_5.setText("Ready to start test")
        #self.label_2.show()
        #self.progressBar.setValue(0)
        #self.label_31.hide()
        #self.label_32.hide()
        self.label_2.setText("")
        self.label_8.setText("")
        
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
    
    def start_test(self):         
        #print ("self.radioButton_5.isChecked :"+str(self.radioButton_5.isChecked()))
        serial_no=self.getserial()
        self.go_ahead="No"
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
            self.pushButton_2.setDisabled(True)        
            #self.pushButton_3_1.setDisabled(True)
            
            self.start_plot =PlotCanvas_Auto(self,width=5, height=4, dpi=80)
            self.gridLayout.addWidget(self.start_plot, 0, 0, 1, 1)
            self.pushButton_3.setEnabled(True)
            
            self.timer3=QtCore.QTimer()
            self.timer3.setInterval(1000)        
            self.timer3.timeout.connect(self.show_progress_bar)
            self.timer3.start(1)
            
            self.label_5.setText("Running........")
            self.label_5.show()
        else:
                 self.label_5.setText("Registration invalid.")
                 self.label_5.show()
    
    def stop_test(self):
        self.pushButton_3.setDisabled(True)
        self.start_plot.on_stop()
        self.label_5.setText("Test Stopped. Save/Reset Test.")
        self.label_5.show()
        self.pushButton_2.setDisabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        if(self.timer3.isActive()): 
                   self.timer3.stop()                                                                                                      
                   print("Time 3 has been stopped ")
                   self.save_test_data_tmp()

    def show_progress_bar(self):
        #print(" inside progress bar  length of arr_p:"+str(len(self.start_plot.arr_p)))        
        if(len(self.start_plot.arr_p) > 0):
                if(int(self.start_plot.curr_vol) > 0 ):
                    per_val=(int(self.start_plot.curr_vol)/1000)*100
                    #self.progressBar.setValue(per_val)
                    self.lcdNumber.setProperty("value", int(self.start_plot.flow_val))
                    self.lcdNumber_2.setProperty("value",int(self.start_plot.curr_vol))                     
                else:
                    #self.progressBar.setValue(0)
                    self.lcdNumber.setProperty("value", 0)
                    self.lcdNumber_2.setProperty("value",0) 
                    
                self.test_start_date=self.start_plot.start_time
                #self.elap_time=datetime.datetime.now()-self.start_plot.start_time
                self.test_end_date=datetime.datetime.now()
                '''
                if(float(len(self.start_plot.arr_q)) > 0):
                    #if(round(float(max(self.start_plot.arr_p))) > 0):
                        self.avg_flow=str(round(float(max(self.start_plot.arr_q2)))/round(float(max(self.start_plot.arr_p))))
                    #else:
                        #self.avg_flow=0
                else:
                    self.avg_flow=0
                '''
                self.label_8.setText(str(self.start_plot.elap_time))
                self.hesitancy_time=str(self.start_plot.h_time) 
                
                
                if(len(self.start_plot.arr_q2) > 0):
                    self.max_flow=str(round(float(max(self.start_plot.arr_q2))))
                    #self.max_flow=str(self.label_2.text())            
                else:
                    #self.label_2.setText("0")
                    self.max_flow=0
                
                
                if(len(self.start_plot.arr_q) > 0):
                    self.voided_vol=str(round(float(max(self.start_plot.arr_q))))
                else:
                    #self.label_2.setText("0")
                    self.voided_vol=0
                
                
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
                        cursor.execute("UPDATE GLOBAL_VAR_TEST SET MAX_FLOW_DEV='',AVG_FLOW_DEV='',VOIDING_TIME_DEV='',TIME_TO_MAX_FLOW_DEV='', HESITANCY_TIME=''")                        
     
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
        #self.hesitancy_time=self.h_time #Hesitancy Time – Time of initiation of urination process to the start of the urine stream
        self.second_min_flow_val=0
        
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
                                     print("MAx flow indx :"+str(self.max_flow_idx)+" Max Flow :"+str(self.start_plot.arr_q2[self.max_flow_idx]))
                                     
                                     
              
               self.voiding_time=float(self.start_plot.arr_p2[self.stop_flow_idx]) - float(self.start_plot.arr_p2[self.start_flow_idx])               
               self.time_to_max_flow=float(self.start_plot.arr_p2[self.max_flow_idx])- float(self.start_plot.arr_p2[self.start_flow_idx])
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
                                                          
        '''
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT MIN(Y_NUM) FROM GRAPH_MST_TMP where Y_NUM > 0")
        for x in results:
              print(" Second Minimum Volum  :"+str(x[0]))
              self.second_min_flow_val=float(x[0])
        connection.close()
        
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT MIN(X_NUM) FROM GRAPH_MST_TMP where Y_NUM ='"+str(self.second_min_flow_val)+"'")
        for x in results:
              print(" Hesitancy Time  :"+str(x[0]))
              self.hesitancy_time=float(x[0])
        connection.close()
        '''
        
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
                cursor.execute("UPDATE GLOBAL_VAR_TEST SET TEST_ID='"+str(self.test_id)+"',ELAPSED_TIME='"+str(self.label_8.text())+"',MAX_FLOW='"+str(self.max_flow)+"'")
                cursor.execute("UPDATE GLOBAL_VAR_TEST SET TEST_START_ON='"+str(self.test_start_date)+"',TEST_END_ON='"+str(self.test_end_date)+"', AVG_FLOW='"+str(self.avg_flow)+"' ,VOIDING_TIME='"+str(self.voiding_time)+"' ")
                #cursor.execute("UPDATE GLOBAL_VAR_TEST SET TEST_START_ON='"+str(self.test_start_date)+"',TEST_END_ON='"+str(self.test_end_date)+"', AVG_FLOW='"+str(self.time_to_max_flow)+"' ,VOIDING_TIME='"+str(self.voiding_time)+"' ")
                cursor.execute("UPDATE GLOBAL_VAR_TEST SET FLOW_TIME='"+str(self.flow_time)+"',TIME_TO_MAX_FLOW='"+str(self.time_to_max_flow)+"', VOIDED_VOL='"+str(self.voided_vol)+"' , FLOW_AT_2_SEC='"+str(self.flow_at_2_sec)+"' ,ACCEL='"+str(self.accel)+"', TOTAL_VOLUMN='"+str(self.total_vol)+"'")                  
                cursor.execute("UPDATE GLOBAL_VAR_TEST SET MAX_FLOW_DEV='"+str(self.volumn_sd)+"',AVG_FLOW_DEV='"+str(self.flow_sd)+"',VOIDING_TIME_DEV='"+str(self.voiding_time_dev)+"',TIME_TO_MAX_FLOW_DEV='"+str(self.time_to_max_flow_dev)+"', HESITANCY_TIME='"+str(self.hesitancy_time)+"' ")                  
                
        connection.commit()
        connection.close()
        #self.start_plot.axes2.set_title('Max Flow:'+str(self.max_flow)+" Avg. Flow :"+str(self.avg_flow))
        #self.start_plot.axes2.set_title('Max Flow: Avg. Flow :')
        
        self.label_2.setText("Flow Time: <font color=blue>"+str(round(self.flow_time,2))+" sec.</font>  Voided Time:<font color=blue>"+str(round(self.voiding_time,2))+" sec.</font> Voided Vol:<font color=blue> "+str(self.voided_vol)+" ml. </font>"+"Max.Flow:<font color=blue>"+str(round(self.max_flow,2))+" ml/sec </font>  Avg.Flow: <font color=blue>"+str(round(self.avg_flow,2))+"ml/sec </font>")
        #self.label_2.setText("Max.Flow:<font color=blue>"+str(round(self.max_flow,2))+" ml/sec </font>  Avg.Flow: <font color=blue>"+str(round(self.avg_flow,2))+"ml/sec </font>")
        #self.label_2.setText("Donne")
        #self.label_31.show()
        #self.label_32.show()
        
        print("Calculations are populated.")
     
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
            self.command_str="T"
            print("Start Command : "+str(self.command_str))
            b = bytes(self.command_str, 'utf-8')
            self.ser.write(b)
            self.lcdNumber.setProperty("value", 0)
            self.lcdNumber_2.setProperty("value",0)
            self.label_2.setText("")
        except IOError:
            print("IO Errors")
            
    
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=Urmini_11_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=urmini_07_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window3(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=urmini_06_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window4(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=urmini_15_MainWindow()
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
        
        self.figure.savefig('last_graph.png',dpi=80)
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
            self.xstr1_1=self.xstr0.replace("\r","")
            self.xstr1=self.xstr1_1.replace("0\x000000","")
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
                                self.p=float(self.elap_time)                            
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
                                print(" Array Q2:"+str(self.arr_q2))
                                
                                '''
                                print(" length Array P:"+str(len(self.arr_p)))
                                print(" length Array Q:"+str(len(self.arr_q)))
                                
                                print(" length Array P2:"+str(len(self.arr_p2)))
                                print(" length Array Q2:"+str(len(self.arr_q2)))
                                '''
                        else:
                                
                                self.h_time=float(self.buff[2])
                                print(" not Running status and h_time :"+str(self.h_time))
                                
                                  
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




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Urmini_01_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

