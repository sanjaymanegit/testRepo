from setting_01 import B_01_Ui_MainWindow
from print_popup import P_POPUi_MainWindow
from calibration_Page import calibration_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
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
import serial
import time
#import array  as arr
import numpy as np
import sqlite3

import serial,time
import array  as arr
import numpy as np
import sys
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 40, 711, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 181, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(252, 210, 255);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 110, 171, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(119, 170, 125);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 260, 171, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(151, 151, 176);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 260, 181, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(188, 125, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 260, 181, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(144, 151, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 110, 181, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 152, 183);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(290, 20, 101, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./images/nms.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(480, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
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
        self.et=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.pushButton_3.setText(_translate("MainWindow", "Print"))
        self.pushButton_4.setText(_translate("MainWindow", "Calibration"))
        self.pushButton_5.setText(_translate("MainWindow", "Reset"))
        self.pushButton_6.setText(_translate("MainWindow", "Setting"))
        self.label_2.setText(_translate("MainWindow", "28 Mar 2023 3:12:24"))
        self.label_3.setText(_translate("MainWindow", "Started !!"))
        self.label_3.hide()
        self.pushButton.clicked.connect(self.start_test)
        self.pushButton_2.clicked.connect(self.stop_test)
        self.pushButton_5.clicked.connect(self.reset_test)
        self.pushButton_3.clicked.connect(self.print_file)
        self.pushButton_6.clicked.connect(self.open_win_setting)
        self.pushButton_4.clicked.connect(self.open_win_calibration)
      
        
        
        self.pushButton_2.setDisabled(True)
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)

    def device_date(self):     
        self.label_2.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def open_win_setting(self):       
        self.window = QtWidgets.QMainWindow()        
        self.ui=B_01_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_win_calibration(self):       
        self.window = QtWidgets.QMainWindow()        
        self.ui=calibration_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
        
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
            
            self.pushButton.setDisabled(True)
            self.pushButton_2.setEnabled(True)
            
            self.start_plot =PlotCanvas_Auto(self,width=5, height=4, dpi=80)
            #self.gridLayout.addWidget(self.start_plot, 0, 0, 1, 1)           
           
            
            self.label_3.setText("Running.")
            self.label_3.show()
            self.timer3=QtCore.QTimer()
            self.timer3.setInterval(1000)        
            self.timer3.timeout.connect(self.show_progress_bar)
            self.timer3.start(1)
        else:
                 self.label_3.setText("Registration.")
                 self.label_3.show()
                 
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
    
    
    
    def stop_test(self):
        self.pushButton.setEnabled(True)        
        self.label_3.setText("Stopped.")
        self.label_3.show()
        self.start_plot.on_stop()
        if(self.timer3.isActive()): 
                   self.timer3.stop()                                                                                                      
                   print("Time 3 has been stopped ")
                   self.save_test_data_tmp()
                   self.save_data()
        
    def reset_test(self):
        self.pushButton.setEnabled(True)
        self.pushButton_2.setDisabled(True)
        self.label_3.hide()
    
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
            
    def show_progress_bar(self):
        #print(" inside progress bar  length of arr_p:"+str(len(self.start_plot.arr_p)))        
        if(len(self.start_plot.arr_p) > 0):
                if(int(self.start_plot.curr_vol) > 0 ):
                    per_val=(int(self.start_plot.curr_vol)/1000)*100
                    #self.progressBar.setValue(per_val)
#                     self.lcdNumber.setProperty("value", int(self.start_plot.flow_val))
#                     self.lcdNumber_2.setProperty("value",int(self.start_plot.curr_vol))                     
                else:
                    #self.progressBar.setValue(0)
#                     self.lcdNumber.setProperty("value", 0)
#                     self.lcdNumber_2.setProperty("value",0)
                    print("no ok")
                    
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
                self.et=str(self.start_plot.elap_time)
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
                cursor.execute("UPDATE GLOBAL_VAR_TEST SET TEST_ID='"+str(self.test_id)+"',ELAPSED_TIME='"+str(self.et)+"',MAX_FLOW='"+str(self.max_flow)+"'")
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
        results=connection.execute("SELECT TEST_ID,TEST_START_ON,DR_NAME,current_timestamp FROM TEST_MST ORDER BY TEST_ID DESC LIMIT 1 ")
        for x in results:
            summary_data=[["Test No:        ",str(x[0]).zfill(6),"Tested Date:        ",str(x[1])[0:10]]]
            self.test_id=str(x[0])
            self.dr_name=str(x[2])
            summary_data.append(["Patient Name : ","                        ","Age: ","   "])           
            summary_data.append(["Doctors Name:","                              ","Gender:","   "])
            self.report_date=str(x[3])[0:16]
        connection.close()
        
        
#         connection = sqlite3.connect("ur.db")        
#         results=connection.execute("SELECT NAME_INITIALS||' '||F_NAME||' '||M_NAME||' '||L_NAME,GENDER,AGE,current_timestamp FROM PATIENT_MST WHERE P_ID IN (SELECT P_ID FROM GLOBAL_VAR_TEST)")
#         for x in results:
#             summary_data.append(["Patient Name : ","                        ","Age: ","   "])
#             self.p_name=str(x[0])
#             summary_data.append(["Doctors Name:","                              ","Gender:","   "])
#             #summary_data.append(["Report Date: ",str(x[3])[0:10],"",""])
#             
#         
#         connection.close()
        test_data=[["  Parameters      ","        Value      ","          Standard Deviation %                   "]]
        connection = sqlite3.connect("ur.db")        
        results=connection.execute("SELECT round(MAX_FLOW,2),round(MAX_FLOW_DEV,2),round(AVG_FLOW,2),round(AVG_FLOW_DEV,2),round(VOIDING_TIME,2),"+
                                   "round(VOIDING_TIME_DEV,2),round(FLOW_TIME,2),round(TIME_TO_MAX_FLOW,2),round(TIME_TO_MAX_FLOW_DEV,2),round(VOIDED_VOL,2),round(FLOW_AT_2_SEC,2),round(ACCEL,2),"+
                                   "round(TOTAL_VOLUMN,2) ,DR_COMMNETS,HESITANCY_TIME FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_TEST)")
        for x in results:
                  '''
                  test_data.append(["Max. Flow (ml/sec)    ",str(x[0]),"Vol  SD (%): "+str(x[1])   ])
                  test_data.append(["Avg. Flow (ml/sec)    ",str(x[2]),"Flow SD (%): "+str(x[3])   ])
                  test_data.append(["Voiding Time(sec)     ",str(x[4]),"--"    ])
                  test_data.append(["Flow Time (sec)       ",str(x[6]),"--"   ])
                  test_data.append(["Time to Max Flow(sec) ",str(x[7]),"--"    ])
                  test_data.append(["Voided Vol (ml)       ",str(x[9]),"--"   ])
                  test_data.append(["Flow at 2 sec.        ",str(x[10]),"--"   ])
                  test_data.append(["Accelaration     ",str(x[11]),"-- "   ])
                  test_data.append(["Hesitancy Time (sec)    ",str(x[14]),"-- "   ])
                  self.remark="xxxx"
                  '''
                  
                  test_data.append(["Voided Vol (ml)    ",str(x[9]),"Vol  SD (%): "+str(x[1])   ])
                  test_data.append(["Max. Flow (ml/sec)    ",str(x[0]),"Flow SD (%): "+str(x[3])   ])
                  test_data.append(["Avg. Flow (ml/sec)     ",str(x[2]),"--"    ])
                  test_data.append(["Flow Time (sec)       ",str(x[6]),"--"   ])
                  test_data.append(["Voiding Time(sec)  ",str(x[4]),"--"    ])
                  test_data.append(["Time to Max Flow(sec)      ",str(x[7]),"--"   ])
                  test_data.append(["Flow at 2 sec.        ",str(x[10]),"--"   ])
                  test_data.append(["Accelaration     ",str(x[11]),"-- "   ])
                  test_data.append(["Hesitancy Time (sec)  ",str(x[14]),"-- "   ])
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
            ptext = "\n <font name=Helvetica size=16> <b> Report as on "+str(self.label_2.text())+" </b></font>"            
            Title3 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        
        line=Paragraph("           ___________________________________________________________________________________________", styles["Normal"])
        spaceline=Paragraph("  \n", styles["Normal"])
        blank=Paragraph(" --------------------------------------------------------------------------------------------------------------------------------------------------     \n", styles["Normal"])
        ptext = "<font name=Helvetica size=10>         Remark : </font>"           
           
        comments = Paragraph(str(ptext)+" ------------------------------------------------------------------------------------------------------------------------------- -\n", styles["Normal"])
        
        footer_2= Paragraph("\n ........................", styles["Normal"])
        
        linea_firma = Line(2, 90, 670, 90)
        d = Drawing(50, 1)
        d.add(linea_firma)
       
        
        if(len(summary_data) > 0):
            f3=Table(summary_data)
            f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10)]))       
            
            f4=Table(test_data)
            f4.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.50, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
            
            report_gr_img="last_graph.png"        
            pdf_img= Image(report_gr_img, 7 * inch, 5 * inch)
            
            
            Elements=[Title3,line,Spacer(1,12),Spacer(1,12),f3,Spacer(1,12),pdf_img,Spacer(1,12),f4,Spacer(1,12),comments,blank,Spacer(1,12),footer_2,Spacer(1,12)]
            
            
            
            doc = SimpleDocTemplate('./reports/ur_reports.pdf', rightMargin=10,
                                    leftMargin=30,
                                    topMargin=10,
                                    bottomMargin=10)
            doc.build(Elements)
        #print("Done")

    def print_file(self):        
        #self.create_pdf()
        self.open_pdf()
        self.window = QtWidgets.QMainWindow()
        self.ui=P_POPUi_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def open_pdf(self):
        self.create_pdf()
        #os.system("xpdf ./reports/ur_reports.pdf")
        os.system("cp ./reports/ur_reports.pdf ./reports/reports_"+str(self.test_id)+".pdf")
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
    
    
    def save_data(self):
        self.intials="x"
        self.f_name="x"
        self.m_name="x"
        self.l_name="x"
        self.gender="12"            
        self.p_id=1
        self.age=1
        self.dob_str="1"
        self.last_test_id="1"
        
#         connection = sqlite3.connect("ur.db")              
#         with connection:        
#                      cursor = connection.cursor()                                
#                      cursor.execute("insert INTO PATIENT_MST (NAME_INITIALS,F_NAME,M_NAME,L_NAME,GENDER,AGE,DOB_STR,LAST_TEST_ID,CREATED_ON) VALUES ('"+self.intials+"','"+self.f_name+"','"+self.m_name+"','"+self.l_name+"','"+self.gender+"','"+self.age+"','"+self.dob_str+"','"+self.last_test_id+"',current_timestamp)")                                
#         connection.commit();
#         connection.close()
        connection = sqlite3.connect("ur.db")              
        with connection:        
                        cursor = connection.cursor()
                        cursor.execute("UPDATE GLOBAL_VAR_TEST SET   p_id='1', DR_NAME='default'")                          
        connection.commit();
        connection.close() 
        
              
        connection = sqlite3.connect("ur.db")              
        with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("INSERT INTO TEST_MST(DR_NAME,TEST_START_ON,TEST_END_ON,ELAPSED_TIME,MAX_FLOW,MAX_FLOW_DEV,"+
                                       "AVG_FLOW,AVG_FLOW_DEV,VOIDING_TIME,VOIDING_TIME_DEV,FLOW_TIME,TIME_TO_MAX_FLOW,TIME_TO_MAX_FLOW_DEV,"+
                                       "VOIDED_VOL,FLOW_AT_2_SEC,ACCEL,VOLUMN_TIME_X,VOLUMN_TIME_Y,FLOW_TIME_X,FLOW_TIME_Y,TOTAL_VOLUMN,P_ID,HESITANCY_TIME) "+
                                       "SELECT DR_NAME,TEST_START_ON,TEST_END_ON,ELAPSED_TIME,MAX_FLOW,MAX_FLOW_DEV,AVG_FLOW,AVG_FLOW_DEV,VOIDING_TIME,"+
                                       "VOIDING_TIME_DEV,FLOW_TIME,TIME_TO_MAX_FLOW,TIME_TO_MAX_FLOW_DEV,VOIDED_VOL,FLOW_AT_2_SEC,ACCEL,VOLUMN_TIME_X,"+
                                       "VOLUMN_TIME_Y,FLOW_TIME_X,FLOW_TIME_Y,TOTAL_VOLUMN,P_ID,HESITANCY_TIME FROM GLOBAL_VAR_TEST")
        connection.commit();
        connection.close()
        print("TEST_MST - Populated.")
        connection = sqlite3.connect("ur.db")              
        with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM) SELECT X_NUM,Y_NUM FROM GRAPH_MST_TMP")
                        cursor.execute("INSERT INTO GRAPH_MST2(X_NUM,Y_NUM) SELECT X_NUM,Y_NUM FROM GRAPH_MST_TMP2")
                        cursor.execute("UPDATE PATIENT_MST SET LAST_TEST_ID = (SELECT MAX(TEST_ID) FROM TEST_MST) WHERE LAST_TEST_ID IS NULL")
        connection.commit();
        connection.close()
        print("GRAPH_MST,GRAPH_MST2 - Populated.") 
                 
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT IFNULL(max(GRAPHI_ID),0)+1 FROM GRAPH_MST") 
        for x in results:
                    self.graph_id=str(x[0])                   
        connection.close()
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT IFNULL(max(GRAPHI_ID),0)+1 FROM GRAPH_MST2") 
        for x in results:
                    self.graph_id2=str(x[0])
        connection.close()
                
                
                
                #print("self.dr_id :"+str(self.dr_id))
        connection = sqlite3.connect("ur.db")              
        with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("UPDATE GRAPH_MST SET GRAPHI_ID='"+str(self.graph_id)+"' WHERE GRAPHI_ID IS NULL")
                        cursor.execute("UPDATE GRAPH_MST2 SET GRAPHI_ID='"+str(self.graph_id2)+"' WHERE GRAPHI_ID IS NULL")
                        cursor.execute("UPDATE TEST_MST SET GRAPHI_ID='"+str(self.graph_id)+"',  GRAPHI_ID2='"+str(self.graph_id2)+"', DR_ID='"+str("1")+"', DR_NAME='default' WHERE TEST_ID  in (SELECT MAX(TEST_ID) FROM TEST_MST)")
        connection.commit();
        connection.close()
                
    
        self.graph_plot =PlotCanvas_blank(self,width=8, height=6,dpi=80)

     
        
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
        results=connection.execute("SELECT GRAPHI_ID, GRAPHI_ID2 FROM TEST_MST ORDER BY TEST_ID DESC LIMIT 1") 
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
        
        
        ax.set_title('Uroflowmetry Report')
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
            '''
            self.ser = serial.Serial(
                port='/dev/ttyUSB0',
                baudrate=19200,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                xonxoff=False,
                timeout = 0.25
            )
            '''
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
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
