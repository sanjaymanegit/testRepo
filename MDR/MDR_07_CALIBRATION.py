
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3


import serial

class mdr_07_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1196, 676)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 1141, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(890, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(50, 80, 461, 421))
        self.frame_2.setStyleSheet("background-color: rgb(136, 181, 149);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_6.setGeometry(QtCore.QRect(130, 30, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_5.setGeometry(QtCore.QRect(40, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_6.setGeometry(QtCore.QRect(150, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(10, 30, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(20, 170, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_7.setGeometry(QtCore.QRect(130, 170, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_7.setGeometry(QtCore.QRect(40, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setChecked(False)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_8.setGeometry(QtCore.QRect(150, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setChecked(True)
        self.radioButton_8.setObjectName("radioButton_8")
        self.label_25 = QtWidgets.QLabel(self.frame_2)
        self.label_25.setGeometry(QtCore.QRect(30, 310, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_8.setGeometry(QtCore.QRect(130, 310, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_9.setGeometry(QtCore.QRect(40, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setChecked(False)
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_10.setGeometry(QtCore.QRect(150, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setChecked(True)
        self.radioButton_10.setObjectName("radioButton_10")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(50, 20, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(580, 80, 511, 421))
        self.frame_3.setStyleSheet("background-color: rgb(244, 163, 244);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(340, 30, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_29 = QtWidgets.QLabel(self.frame_3)
        self.label_29.setGeometry(QtCore.QRect(20, 30, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 30, 121, 61))
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(3)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_31 = QtWidgets.QLabel(self.frame_3)
        self.label_31.setGeometry(QtCore.QRect(20, 150, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber_2.setGeometry(QtCore.QRect(180, 150, 121, 61))
        self.lcdNumber_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_2.setLineWidth(3)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber_3.setGeometry(QtCore.QRect(180, 270, 121, 61))
        self.lcdNumber_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_3.setLineWidth(3)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_33 = QtWidgets.QLabel(self.frame_3)
        self.label_33.setGeometry(QtCore.QRect(10, 270, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 150, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 270, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(10, 350, 491, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame_3)
        self.line_2.setGeometry(QtCore.QRect(10, 110, 491, 21))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setGeometry(QtCore.QRect(10, 230, 491, 21))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 370, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(590, 20, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(1000, 550, 91, 31))
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
        self.pushButton_15.setGeometry(QtCore.QRect(840, 550, 141, 31))
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
        self.pushButton_16.setGeometry(QtCore.QRect(570, 550, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(580, 510, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1196, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ld_flag="No"
        self.capacity_flag="No"
        self.off_position_flag="No"
        self.flag="No"
        self.ser =""
        self.line =""                   
       
        self.xstr0=""
        self.xstr1=""
        self.xstr2=""
        self.buff=[]
        
        self.IO_error_flg=0
        self.xstr3=""
        self.xstr2=""
        self.xstr4=""
        self.current_value=0
        self.green_counter=0
        
        self.last_value=0
        self.current_value=0
        self.enable_buttons_flag="No"
        self.enable_counter=0
        self.weighing_crosses_min_wt_lim="No"
        self.weighing_crosses_max_wt_lim="No"
        self.wt_min_limit=0
        self.wt_max_limit=0      
        self.c1_count=0
        
        self.ld_set=0
        self.mod_val=0
        
        self.last_display_val=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00 "))
        self.radioButton_5.setText(_translate("MainWindow", "On"))
        self.radioButton_6.setText(_translate("MainWindow", "Off"))
        self.label_23.setText(_translate("MainWindow", "Motor :"))
        self.label_24.setText(_translate("MainWindow", "Sheild :"))
        self.radioButton_7.setText(_translate("MainWindow", "Open"))
        self.radioButton_8.setText(_translate("MainWindow", "Close"))
        self.label_25.setText(_translate("MainWindow", "Die:"))
        self.radioButton_9.setText(_translate("MainWindow", "Open"))
        self.radioButton_10.setText(_translate("MainWindow", "Close"))
        self.label_21.setText(_translate("MainWindow", "Manual Status :"))
        self.label_29.setText(_translate("MainWindow", "Torque (lb in) :"))
        self.label_31.setText(_translate("MainWindow", "Temp (UPPER) :"))
        self.label_33.setText(_translate("MainWindow", "Temp (LOWER) :"))
        self.pushButton_4.setText(_translate("MainWindow", "Set "))
        self.label_22.setText(_translate("MainWindow", "Calibration :"))
        self.pushButton_14.setText(_translate("MainWindow", "Close"))
        self.pushButton_15.setText(_translate("MainWindow", "Stop Motor"))
        self.pushButton_16.setText(_translate("MainWindow", "Print Calibration Certificate"))
        self.label_27.setText(_translate("MainWindow", "Please Set the Toqtue Proper."))
        self.pushButton_14.clicked.connect(MainWindow.close)
        self.timer2=QtCore.QTimer()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        
       
        self.start_reading()        
       
    
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
        
    def start_reading(self):
        #print("Weight Started ....")
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
            print("o/p:"+str(self.line))
             
            self.timer2.setInterval(1000)        
            self.timer2.timeout.connect(self.display_lcd_val)
            self.timer2.start(1)
        
        except IOError:
                    print("IO Errors")      
   
                
    def display_lcd_val(self):               
            #print(" inside display_lcd_val:"+str(self.IO_error_flg))
            self.label_27.hide()
            if(self.IO_error_flg==0):            
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
                    self.p=self.p                 
                    self.r=170.00
                    self.arr_p.append(float(self.p))
                    self.arr_q.append(float(self.q))
                    self.arr_r.append(float(self.r))
                    print(" Timer P:"+str(self.p)+" q:"+str(self.q))
                    self.lcdNumber_2.setProperty("value", str(self.arr_p))
                    self.lcdNumber.setProperty("value", str(self.q)) 
                    

                
            
        
    def stop_timer(self):
       if(self.timer2.isActive()):
           self.timer2.stop() 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mdr_07_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
