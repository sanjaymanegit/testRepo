
from DEF_05_NEW_TEST import def_05_Ui_MainWindow
from DEF_02_RUNNING_TEST import def_02_Ui_MainWindow
from DEF_03_Report import def_03_Ui_MainWindow
from DEF_04_Admin import def_04_Ui_MainWindow


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import re
import os,sys
import serial,time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 1301, 691))
        self.frame.setStyleSheet("background-color: rgb(217, 255, 235);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(510, 180, 221, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 205, 209);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 180, 221, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 205, 209);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(1080, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(890, 180, 241, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 205, 209);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(140, 440, 221, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 205, 209);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 40, 341, 101))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(300, 500))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        
        
        self.label_39 = QtWidgets.QLabel(self.frame)
        self.label_39.setGeometry(QtCore.QRect(800, 80, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        
        
        
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1030, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(1160, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.p=0
        self.q=0
        self.arr_p=[]
        self.arr_q=[]
        self.IO_error_flg=0
        self.xstr0=""
        self.xstr1=""
        self.xstr2=""
        self.xstr3=""
        self.xstr4=0
        self.buff=[]
        self.i1=0
        self.j1=0
        self.job_initialted=0
        self.mod=0
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.elapsed_time=0
        self.data_log_time=0
        self.first_record_add=0
        self.max_time="0.0"
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "NEW TEST"))
        self.pushButton_3.setText(_translate("MainWindow", "RUNNING TEST"))
        self.label.setText(_translate("MainWindow", "09 Feb 2021 11:34"))
        self.pushButton_5.setText(_translate("MainWindow", "REPORT"))
        self.pushButton_8.setText(_translate("MainWindow", "ADMIN"))
        self.pushButton_6.setText(_translate("MainWindow", "Shutdown"))
        self.pushButton_7.setText(_translate("MainWindow", "Reboot"))
        self.pushButton.clicked.connect(self.open_new_window)
        self.pushButton_3.clicked.connect(self.open_new_window2)
        self.pushButton_5.clicked.connect(self.open_new_window3)
        self.pushButton_8.clicked.connect(self.open_new_window4)
        self.pushButton_6.clicked.connect(self.shutdown_system)
        self.pushButton_7.clicked.connect(self.reboot_system)
        self.anydesk_open()
        
        self.timer6=QtCore.QTimer()
        self.timer7=QtCore.QTimer()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        self.timer2=QtCore.QTimer()
        self.timer2.setInterval(5000)        
        self.timer2.timeout.connect(self.check_test_status)
        self.timer2.start(1000)
        #self.start_job()
        
    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def shutdown_system(self):
        os.system("sudo shutdown -P 0")
        
    def reboot_system(self):
        os.system("sudo reboot")
        
    def anydesk_open(self):
        self.anydesk_id =0
        os.system("rm -rf anydes_id_f.txt")
        os.system("anydesk --get-id >> anydes_id_f.txt")
        f = open('anydes_id_f.txt','r')
        for line in f:                 
                    self.anydesk_id = line[0:9]
        print("self.anydesk_id:"+str(self.anydesk_id))
        self.label_39.setText("AnyDesk ID:"+str(self.anydesk_id))    
        f.close()
        
    def check_test_status(self):
        self.test_cnt=0
        connection = sqlite3.connect("def.db")
        results=connection.execute("SELECT COUNT(TEST_ID),TEST_START_ON,(IFNULL(DATA_LOG_TIME,5)*60),IFNULL(MAX_TIME,'0.0') FROM TEST_MST WHERE STATUS='RUNNING'") 
        for x in results:
            self.test_cnt=str(x[0])
            self.data_log_time=int(x[2])
            self.max_time=str(x[3])
            if(int(self.test_cnt) > 0):
                self.start_time = datetime.datetime.strptime(str(x[1]), '%Y-%m-%d %H:%M:%S')
            else:
                pass            
        connection.close()
        if(int(self.test_cnt)==0):            
            self.pushButton.setEnabled(True)
            self.pushButton_3.setDisabled(True)
            self.on_stop()
        else:
            self.pushButton.setDisabled(True)  # New Test
            self.pushButton_3.setEnabled(True) ## Runnung
            
            if(self.job_initialted==1):
                self.on_restart()
            else:
                self.intiate_job()
                
            if(float(self.elapsed_time) > float(self.max_time)):
                connection = sqlite3.connect("def.db")
                with connection:        
                        cursor = connection.cursor()
                        cursor.execute("UPDATE TEST_MST SET STATUS = 'AUTO-STOPPED'  WHERE STATUS='RUNNING' ")
                        cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM) SELECT X_NUM,Y_NUM FROM GRAPH_MST_TMP")
                        cursor.execute("UPDATE GRAPH_MST SET GRAPHI_ID=(SELECT MAX(IFNULL(GRAPHI_ID,0))+1 FROM GRAPH_MST) WHERE GRAPHI_ID IS NULL")
                        cursor.execute("UPDATE TEST_MST SET GRAPHI_ID=(SELECT MAX(IFNULL(GRAPHI_ID,0)) FROM GRAPH_MST) WHERE GRAPHI_ID IS NULL")                        
                connection.commit();                    
                connection.close()                
            else:
                pass
        #print("running test count :"+str(self.test_cnt))
    
    def intiate_job(self):        
        #self.axes.set_facecolor('#CCFFFF')        
        self.p=0
        self.q=0
        
        self.arr_p1=[]
        self.arr_q1=[]
        
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
            self.line = self.ser.readline(15)
            #print("o/p:"+str(self.line))
            self.timer6.setInterval(5000)        
            self.timer6.timeout.connect(self.load_arr)
            self.timer6.start(1000)
            self.job_initialted=1
            '''
            self.timer7.setInterval(15000)        
            self.timer7.timeout.connect(self.load_db)
            self.timer7.start(1)
            '''
        except IOError:
            print("IO Errors-load cell connections error")
            self.IO_error_flg=1           
           
        
    def on_restart(self):
        if(not self.timer6.isActive()): 
                self.timer6.start(10)                                                                                                      
                print("Time 6 has been started ")         
        else:
            pass
        
        
    def on_stop(self):        
        if(self.timer6.isActive()): 
                   self.timer6.stop()                                                                                                      
                   print("Time 6 has been stopped ")
                   
        else:
            pass
        
    def load_arr(self):         
         self.elapsed_time=0
         if(self.IO_error_flg==0):
            try:
                self.line = self.ser.readline()
                #print(" raw o/p:"+str(self.line))
                #print("self.line:"+str(self.line,'utf-8'))
                self.xstr0=str(self.line,'utf-8')
                self.xstr1=self.xstr0.replace("\r","")
                self.xstr2=self.xstr1.replace("\n","")
                self.buff=self.xstr2.split("_")
                #self.last_value=self.current_value 
                if(len(self.buff)> 1):                        
                            self.xstr2=str(self.buff[0])
                            try:
                                    self.xstr4=float(self.xstr2)                                    
                            except ValueError:                        
                                    print("Value Error"+str(self.xstr2))
                                    self.xstr4=0
                            try:
                                    self.end_time = datetime.datetime.now()
                                    self.elapsed_time=self.end_time-self.start_time
                                    self.elapsed_time =self.elapsed_time.days * 24 * 3600 + self.elapsed_time.seconds                                    
                                    #self.mod=int(self.elapsed_time) % 10
                                    if(int(self.data_log_time) > 0):
                                        self.mod=int(self.elapsed_time) % int(self.data_log_time)
                                    else:
                                        self.mod=0
                                    print("Mod::"+str(int(self.mod))+" self.elapsed_time: "+str(self.elapsed_time)+" self.data_log_time : "+str(self.data_log_time)+" Weight :"+str(self.xstr4))
                                    self.elapsed_time=float((int(self.elapsed_time)/60)/60)
                                    
                            except ValueError:                        
                                    print("Elapsed Time")        
                            
                            if(int(self.mod)==0 and float(self.elapsed_time) > 0 ):
                                    connection = sqlite3.connect("def.db")              
                                    with connection:        
                                        cursor = connection.cursor()                                
                                        cursor.execute("INSERT INTO GRAPH_MST_TMP(X_NUM,Y_NUM) VALUES('"+str(float(self.elapsed_time))+"','"+str(self.xstr4)+"')")                         
                                    connection.commit();
                                    connection.close()
                                    print("Inserted Record :self.elapsed_time :"+str(self.elapsed_time)+" Weight :"+str(self.xstr4))
                                    '''
                                    
                                    print("self.start time:"+str(self.start_time))
                                    print("self.End_time:"+str(self.end_time))
                                    print("self.elapsed_time:"+str(int(self.elapsed_time)))
                                    print("Mod::"+str(int(self.mod)))
                                    print("Weight :"+str(int(self.xstr4)))
                                    '''
                            else:
                                #print("self.job_initialted:"+str(self.job_initialted)+"self.first_record_add :"+str(self.first_record_add)+"Weight :"+str(int(self.xstr4)))
                                if(int(self.job_initialted)==1):
                                    if(int(self.first_record_add)==0):
                                        if(float(self.xstr4) > 0):
                                                '''
                                                connection = sqlite3.connect("def.db")              
                                                with connection:        
                                                    cursor = connection.cursor()                                
                                                    cursor.execute("INSERT INTO GRAPH_MST_TMP(X_NUM,Y_NUM) VALUES('0','"+str(self.xstr4)+"')")                         
                                                connection.commit();
                                                connection.close()
                                                self.first_record_add=1
                                                print("FIRST RECORD ADDED !!!!")
                                                print("self.data_log_time :"+str(self.data_log_time))
                                                '''
                                                pass
                                        else:
                                             print("Weight :"+str(float(self.xstr4)))
                                
                                    
                            
                            
                else:
                    #print("Now Weight Data Evaluated :"+str(len(self.buff)))
                    pass
                
            except IOError:
                print("IO Errors : Data Read Error") 
                self.IO_error_flg=1
                
    ''' 
    def load_db(self):
        self.arr_p1=self.arr_p
        self.arr_q1=self.arr_q        
        self.on_stop()
        connection = sqlite3.connect("def.db")              
        with connection:        
                 cursor = connection.cursor()
                 for d in range(len(self.arr_p1)):
                         cursor.execute("INSERT INTO GRAPH_MST_TMP(X_NUM,Y_NUM) VALUES('"+str(self.arr_p1[d])+"','"+str(self.arr_q1[d])+"')")
                         
        connection.commit();
        connection.close()
        self.on_restart()
    '''  
                            
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
    
    def open_new_window(self):
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
                self.window = QtWidgets.QMainWindow()
                self.ui=def_05_Ui_MainWindow()
                self.ui.setupUi(self.window)           
                self.window.show()
        else:
             pass
    
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=def_02_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window3(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=def_03_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window4(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=def_04_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
