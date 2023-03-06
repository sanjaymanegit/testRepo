

from AE_Admin_02 import AE_02_Ui_MainWindow
from TY_07_UTM_MANNUAL_CONTROL import TY_07_Ui_MainWindow
from TY_05_SPECIMEN import TY_05_Ui_MainWindow
from TY_01_TEST_BATCH import TY_01_Ui_MainWindow
#from TY_01_TEST_BATCH import TY_01_Ui_MainWindow
from TY_01_TEST_BATCH_QLSS import TY_01_qlss_Ui_MainWindow
from TY_01_TEST_BATCH_ILSS import TY_01_ilss_Ui_MainWindow
from TY_01_TEST_BATCH_FLXURL import TY_01_fluxurl_Ui_MainWindow
from TY_11_START_TEST_COF import TY_11_Ui_MainWindow
from TY_22_TEST_BATCH_TENSILE_8 import TY_01_T8_Ui_MainWindow
from TY_23_START_TEST_PEELOFF import TY_23_PEELOFF_Ui_MainWindow
from TY_26_START_TEST_FOUND_BRK_TEST import TY_26_Ui_MainWindow
from TY_29_START_TEST_PROOF import ty_29_Ui_MainWindow
from TY_32_START_TEST_CYCLICK import TY_32_Ui_MainWindow

from TY_03_REPORTS import TY_03_Ui_MainWindow
from TY_21_SP_REPORT_TENSILE_8 import TY_13_T8_Ui_MainWindow
from TY_24_SP_REPORT_PEELOFF import TY_24_PEEL_OFF_Ui_MainWindow
from TY_27_SP_REPORT_FOUND_BRK_TEST import TY_27_FBST_Ui_MainWindow
from TY_30_SP_REPORT_PROOF import TY_30_Ui_MainWindow
from TY_33_SP_REPORT_CYCLICK import TY_33_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
import sys,os


class AE_01_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 769)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1301, 709))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("background-color: rgb(215, 255, 252);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(550, 210, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 180, 188);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 210, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 180, 188);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 470, 495, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 180, 188);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(850, 340, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 180, 188);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 340, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 180, 188);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(500, 30, 81, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./images/AE_LOGO.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(600, 30, 371, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.label_47 = QtWidgets.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(1060, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_47.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_47.setObjectName("label_47")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(50, 100, 341, 541))
        self.listWidget.setStyleSheet("background-color: rgb(253, 239, 255);")
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        item = QtWidgets.QListWidgetItem()

        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()

        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()

        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()

        self.listWidget.addItem(item)
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(50, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(0, 170, 127);")
        self.label_50.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_50.setObjectName("label_50")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1090, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setStyleSheet("background-color: rgb(159, 170, 166);")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(480, 140, 811, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(470, 10, 20, 690))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Test"))
        self.pushButton_2.setText(_translate("MainWindow", "Reports"))
        self.pushButton_3.setText(_translate("MainWindow", "Manual Control"))
        self.pushButton_4.setText(_translate("MainWindow", "Specimens"))
        self.pushButton_5.setText(_translate("MainWindow", "Admin"))
        self.label_2.setText(_translate("MainWindow", "Asian Test Equipments"))
        self.label_47.setText(_translate("MainWindow", "05 Aug 2020 14:23:00"))
        '''
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Tensile (01)"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Compression(02)"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Tear(03)"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Flexural(04)"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        '''
        self.label_50.setText(_translate("MainWindow", "Test List :"))
        self.pushButton_6.setText(_translate("MainWindow", "Log Out"))
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_5.clicked.connect(self.open_new_window_admin)
        self.pushButton_3.clicked.connect(self.open_new_window_motor)
        self.pushButton_4.clicked.connect(self.open_new_window_specimen)
        #self.pushButton.clicked.connect(self.open_new_window_Tensile)
        self.pushButton.clicked.connect(self.validate_Register)
        self.pushButton_2.clicked.connect(self.open_new_report_win)
        
        self.listWidget.doubleClicked.connect(self.selected_record)
        self.listWidget.clicked.connect(self.selected_record)
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.load_data()
        
    def device_date(self):     
        self.label_47.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        

    def load_data(self):
        self.listWidget.clear() 
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  TEST_TYPE_NAME||'('||TEST_TYPE_ID||')' FROM TEST_TYPE_MST WHERE ACTIVE_Y_N = 'Y'") 
        for x in results:
            self.listWidget.addItem(str(x[0]))
        connection.close()
        self.listWidget.setCurrentRow(0)
        self.selected_record()
        #self.load_modbus_port()
        self.load_login_dtls()
        
        
   
    def selected_record(self):
        self.test_type_id=""        
        self.list_type=self.listWidget.currentItem().text()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  TEST_TYPE_NAME,TEST_TYPE_DTLS,TEST_TYPE_IMG_FILE,ACTIVE_Y_N,TEST_TYPE_ID FROM TEST_TYPE_MST WHERE ACTIVE_Y_N = 'Y' and TEST_TYPE_NAME||'('||TEST_TYPE_ID||')' = '"+str(self.list_type)+"'")
        for x in results:
            self.test_type_id=str(x[4])                       
        connection.close()
    
    
    def open_new_window_admin(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=AE_02_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_motor(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_07_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_specimen(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_05_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_Tensile(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_01_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def validate_Register(self):        
        f = open("/var/local/devid", "r")
        dev_id=f.read()
        f.close()
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select DEVICE_SERIAL_NO from GLOBAL_REPORTS_PARAM") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))
           if(serial_no == str(x[0])):
               self.go_ahead="Yes"
           else:
               self.go_ahead="No"
        connection.close()
        if(self.go_ahead=="Yes"):  
            if(dev_id =='201910:0003'):
                self.open_new_test_win()       
            else:
                #print("dev id :"+str(dev_id))
                self.label_9021.setText("<font color=black> Registration Problem.</font>")
        else:
           print("Device Invalid :"+str(serial_no))    
        
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
                
    def open_new_test_win(self):
        
        if(str(self.test_type_id) == "1"):
            self.save_test_tensile()
            self.open_new_window()
        elif(str(self.test_type_id) == "2"):
            self.save_test_compress()
            self.open_new_window()
        elif(str(self.test_type_id) == "3"):
            self.save_test_tear()
            self.open_new_window()
        elif(str(self.test_type_id) == "4"):
            self.save_test_flexural()
            self.open_new_window_flexurl()
        elif(str(self.test_type_id) == "5"):
            self.save_test_cof()
            self.open_new_window_cof()
        elif(str(self.test_type_id) == "6"):
            self.save_test_ilss()
            self.open_new_window_ilss()
        elif(str(self.test_type_id) == "7"):
            self.save_test_qlss ()
            self.open_new_window_qlss()
        elif(str(self.test_type_id) == "8"):
            self.save_test_tensile_8()
            self.open_new_window_tensile_8()
        elif(str(self.test_type_id) == "14"):
            self.save_test_peeloff()
            self.open_new_window_peeloff()
        elif(str(self.test_type_id) == "15"):
            self.save_test_FBST()
            self.open_new_window_FBST()
        elif(str(self.test_type_id) == "16"):
            self.save_test_PROOF()
            self.open_new_window_PROOF()
        elif(str(self.test_type_id) == "17"):
            self.save_test_CYCLICK()
            self.open_new_window_CYCLICK()
        else:
            print("Invalid Test ID")
            
    def open_new_report_win(self):
        
        if(str(self.test_type_id) == "1"):
            self.save_test_tensile()
            self.open_report_window()
        elif(str(self.test_type_id) == "2"):
            self.save_test_compress()
            self.open_report_window()
        elif(str(self.test_type_id) == "3"):
            self.save_test_tear()
            self.open_report_window()
        elif(str(self.test_type_id) == "4"):
            self.save_test_flexural()
            self.open_report_window_flexurl()
        elif(str(self.test_type_id) == "5"):
            self.save_test_cof()
            self.open_report_window_cof()
        elif(str(self.test_type_id) == "6"):
            self.save_test_ilss()
            self.open_report_window_ilss()
        elif(str(self.test_type_id) == "7"):
            self.save_test_qlss ()
            self.open_report_window_qlss()
        elif(str(self.test_type_id) == "8"):
            self.save_test_tensile_8()
            self.open_report_window_tensile_8()
        elif(str(self.test_type_id) == "14"):
            self.save_test_peeloff()
            self.open_report_window_peeloff()
        elif(str(self.test_type_id) == "15"):
            self.save_test_FBST()
            self.open_report_window_FBST()
        elif(str(self.test_type_id) == "16"):
            self.save_test_PROOF()
            self.open_report_window_PROOF()
        elif(str(self.test_type_id) == "17"):
            self.save_test_CYCLICK()
            self.open_report_window_CYCLICK()
        else:
            print("Invalid Test ID")    
        
    def save_test_tensile(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Tensile'")                    
        connection.commit();
        connection.close()
        
        
        
        
        
    def save_test_tensile_8(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Tensile_8'")                    
        connection.commit();
        connection.close()
        
        
        
        
    def save_test_compress(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Compress'")            
        connection.commit();
        connection.close()    
        
        
        
    def save_test_tear(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Tear'")            
        connection.commit();
        connection.close()    
        
        
    def save_test_flexural(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Flexural'")            
        connection.commit();
        connection.close()    
        
        
    def save_test_qlss(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='QLSS'")            
        connection.commit();
        connection.close()    
        
    
    def save_test_ilss(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='ILSS'")            
        connection.commit();
        connection.close()    
        
    
    def save_test_cof(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='COF'")            
        connection.commit();
        connection.close()    
        
    
    def save_test_peeloff(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='PEELOFF'")            
        connection.commit();
        connection.close()    
        
     
    def save_test_FBST(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='FBST'")            
        connection.commit();
        connection.close()    
        
    
    def save_test_PROOF(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='PROOF'")            
        connection.commit();
        connection.close()    
        
    
    
    def save_test_CYCLICK(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='CYCLICK'")            
        connection.commit();
        connection.close()    
        
        
    def open_new_window_FBST(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_26_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()    
    
    
    def open_new_window_peeloff(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_23_PEELOFF_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()    
    
    
    def open_new_window(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_01_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()    
   

    def open_new_window_qlss(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_01_qlss_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_ilss(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_01_ilss_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_flexurl(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_01_fluxurl_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_cof(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_11_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window_tensile_8(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_01_T8_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window_PROOF(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=ty_29_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_CYCLICK(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_32_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    #===== Reports ========================
    
    def open_report_window(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_03_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()    
   

    def open_report_window_qlss(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_03_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_window_ilss(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_03_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_window_flexurl(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_03_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_window_cof(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_03_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_report_window_tensile_8(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_13_T8_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_window_peeloff(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_24_PEEL_OFF_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_window_FBST(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_27_FBST_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    
    def open_report_window_PROOF(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_30_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_report_window_CYCLICK(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_33_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def load_login_dtls(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select login_user_id,login_user_role,login_user_name from global_var")       
        for x in results:           
                 self.login_user_id=str(x[0])
                 self.login_user_role=str(x[1])
                 self.login_user_name=str(x[2])
        connection.close()
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(1000, 40, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_21.setText("Login By : "+str(self.login_user_name))
        
        
        
        self.pushButton_902 = QtWidgets.QPushButton(self.frame)
        self.pushButton_902.setGeometry(QtCore.QRect(550, 590, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_902.setFont(font)
        self.pushButton_902.setStyleSheet("color: rgb(244, 244, 0); background-color: rgb(170, 0, 0);")
        
        self.pushButton_902.setObjectName("pushButton_902")
        self.pushButton_905 = QtWidgets.QPushButton(self.frame)
        self.pushButton_905.setGeometry(QtCore.QRect(720, 590, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_905.setFont(font)
        self.pushButton_905.setStyleSheet("color: rgb(244, 244, 0);  background-color: rgb(170, 0, 0);")
        self.pushButton_905.setObjectName("pushButton_905")
        self.label_9021 = QtWidgets.QLabel(self.frame)
        self.label_9021.setGeometry(QtCore.QRect(880, 580, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_9021.setFont(font)
        self.label_9021.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9021.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9021.setObjectName("label_9021")
        
        self.pushButton_902.setText("SHUT DOWN")
        self.pushButton_905.setText("REBOOT")
        self.pushButton_902.clicked.connect(self.shutdown_system)
        self.pushButton_905.clicked.connect(self.reboot_system)
        self.anydesk_open()
        
    
    def shutdown_system(self):
        os.system("sudo shutdown -P 0")
        
    def reboot_system(self):
        os.system("sudo reboot")
        
    def anydesk_open(self):
        self.anydesk_id =0
        os.system("rm -rf anydes_id_f.txt")
        os.system("anydesk --get-alias >> anydes_id_f.txt")
        f = open('anydes_id_f.txt','r')
        for line in f:                 
                    self.anydesk_id = line[0:29]
        print("self.anydesk_id:"+str(self.anydesk_id))
        self.label_9021.setText("<font color=blue> AnyDesk ID:  </font> <font color=green>"+str(self.anydesk_id)+"</font>")
        f.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AE_01_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
