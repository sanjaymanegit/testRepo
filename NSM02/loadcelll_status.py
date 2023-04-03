



from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
import sqlite3
import serial


class loadcell_status_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 402)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 491, 311))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(360, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(170, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 230, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./images/nms.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(170, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(260, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(270, 50, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_2.setGeometry(QtCore.QRect(270, 140, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
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
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44:09"))
        self.label_2.setText(_translate("MainWindow", "Done."))
        self.label_3.setText(_translate("MainWindow", "Count :"))
        self.pushButton_8.setText(_translate("MainWindow", "Close"))
        self.label_5.setText(_translate("MainWindow", "Weight:"))
        self.pushButton_9.setText(_translate("MainWindow", "Set Zero"))
        self.pushButton_9.clicked.connect(self.set_zero)
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.timer2=QtCore.QTimer()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.start_wt()        
       
        
    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def set_zero(self):
        self.green_counter=15
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
                #=============
                self.command_str="Z"
                print("Tare Command : "+str(self.command_str))
                b = bytes(self.command_str, 'utf-8')
                self.ser.write(b)
                #=============
                #self.groupBox_7.show()
                self.label_2.setText("Set Zero Done." )  
                self.label_2.show()
                
                
                
        except IOError:
                print("IO Errors")
                self.label_2.setText("IO Errors" )  
                self.label_2.show()
        
    def start_wt(self):
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
            print("IO Errors-load cell connections error")
            self.IO_error_flg=1
            self.groupBox_7.show()
            self.label_2.show()
            self.label_2.setText("LOAD CELL CONNECTION ERROR.")
            
            
    def display_lcd_val(self):               
        #print(" inside display_lcd_val:"+str(self.IO_error_flg))
        self.label_2.hide()
        if(self.green_counter > 0):
                self.pushButton_9.setStyleSheet("background-color: rgb(0, 170, 0);")
                self.lcdNumber_2.setStyleSheet("color: rgb(255, 255, 0);\n background-color: rgb(0, 0, 0);")               
                self.green_counter=self.green_counter-1
        else:
                self.pushButton_9.setStyleSheet("background-color: rgb(170, 0, 0);")
        if(self.IO_error_flg==0):
            try:
                self.line = self.ser.readline()
                print(" raw o/p:"+str(self.line))
                print("self.line:"+str(self.line,'utf-8'))
                self.xstr0=str(self.line,'utf-8')
                self.xstr1=self.xstr0.replace("\r","")
                self.xstr2=self.xstr1.replace("\n","")
                self.buff=self.xstr2.split("_")
                self.last_value=self.current_value 
                if(len(self.buff)> 1):
                       # if(str(self.buff[3]) == 'R'): 
                                self.xstr2=str(self.buff[0])
                                try:
                                     self.xstr4=int(self.xstr2)
                                except ValueError:                        
                                    print("Value Error"+str(self.xstr2))
                                    self.xstr4=0
                                    self.c1_count=0
                                self.c1_count=str(self.buff[1])
                                self.lcdNumber_2.setProperty("value", str(self.xstr4))
                                self.lcdNumber.setProperty("value", str(self.xstr4)) 
                                #self.lcdNumber.setProperty("value", str(self.c1_count))
                                #print("self.c1_count :"+str(self.c1_count)+" Weight : "+str(self.xstr4))
                               
                    
            except IOError:
                print("IO Errors : Data Read Error") 
                self.IO_error_flg=1                
                self.label_2.show()
                self.label_2.setText("IO Errors .")
        
    def stop_timer(self):
       if(self.timer2.isActive()):
           self.timer2.stop()  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = loadcell_status_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
