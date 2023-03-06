
from AE_Register import Register_Ui_MainWindow
from pop_factory_reset import  factory_reset_Ui_MainWindow
from TY_15_ADD_EDIT_TEST_TYPE import TY_15_Ui_MainWindow
from TY_16_email_setup import ty_16_Ui_MainWindow
from TY_17_calbration_extentio_mtr import TY_17_Ui_MainWindow
from usb_bakp import usb_bkp_Ui_MainWindow
from user_management import users_Ui_MainWindow
from date_time_set import date_time_set_Ui_MainWindow
from SPEED_SETUP_POPUP import spped_setup_Ui_MainWindow
from change_password import change_pwd_Ui_MainWindow
from AE_MASTER_INFO import Master_info_Ui_MainWindow
from AE_LOAD_CELL_SELECTION import load_cell_set_Ui_MainWindow


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
import sys,os

class AE_02_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 769)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 40, 1301, 700))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("background-color: rgb(215, 255, 252);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(540, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(105, 210, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(540, 10, 300, 51))
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
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1080, 80, 151, 41))
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
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(180, 90, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        self.lineEdit.setFont(font)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.lineEdit.setText("12345")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(720, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 180, 188);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 190, 1221, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(40, 260, 1221, 381))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 30, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 30, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(650, 30, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(940, 30, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 120, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(350, 120, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(650, 120, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(940, 120, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_12.setGeometry(QtCore.QRect(650, 210, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_13.setGeometry(QtCore.QRect(70, 210, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_14.setGeometry(QtCore.QRect(940, 210, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_15.setGeometry(QtCore.QRect(350, 210, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_16.setGeometry(QtCore.QRect(70, 300, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_17.setGeometry(QtCore.QRect(350, 300, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_18.setGeometry(QtCore.QRect(650, 300, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_19.setGeometry(QtCore.QRect(940, 300, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color: rgb(91, 113, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./images/AE_LOGO.jpg"))
        self.label_4.setObjectName("label_4")
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
        self.pushButton.setText(_translate("MainWindow", "Procced"))
        self.label_2.setText(_translate("MainWindow", "Administration"))
        self.label_47.setText(_translate("MainWindow", "05 Aug 2020 14:23:00"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.pushButton_7.setText(_translate("MainWindow", "Reset"))
        self.pushButton_4.setText(_translate("MainWindow", "Master Information"))
        self.pushButton_2.setText(_translate("MainWindow", "Configure Test"))
        self.pushButton_5.setText(_translate("MainWindow", "Factory Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "DateTime Setting"))
        self.pushButton_8.setText(_translate("MainWindow", "Email Setup"))
        self.pushButton_9.setText(_translate("MainWindow", "Callibration"))
        self.pushButton_10.setText(_translate("MainWindow", "USB Reports Backup"))
        self.pushButton_11.setText(_translate("MainWindow", "Speed Setup"))
        self.pushButton_12.setText(_translate("MainWindow", "Change Password"))
        self.pushButton_14.setText(_translate("MainWindow", "Break App"))
        self.pushButton_13.setText(_translate("MainWindow", "User Management"))
        self.pushButton_15.setText(_translate("MainWindow", "Load Cell Selection"))
        self.pushButton_19.setText(_translate("MainWindow", "Register"))
        #self.pushButton_14.hide()
        self.pushButton_16.hide()
        self.pushButton_17.hide()
        self.pushButton_18.hide()
        #self.pushButton_19.hide()
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_19.clicked.connect(self.open_new_window)
        self.pushButton_2.clicked.connect(self.open_new_window2)
        self.pushButton_5.clicked.connect(self.open_new_window3)
        self.pushButton_8.clicked.connect(self.open_new_window4)
        self.pushButton_10.clicked.connect(self.open_new_window5)
        self.pushButton_13.clicked.connect(self.open_new_window6)
        self.pushButton_3.clicked.connect(self.open_new_window7)
        self.pushButton_11.clicked.connect(self.open_new_window8)
        self.pushButton_12.clicked.connect(self.open_new_window9)
        self.pushButton_4.clicked.connect(self.open_new_window10)
        self.pushButton_15.clicked.connect(self.open_new_window11)
        self.pushButton_14.clicked.connect(self.break_app)
        
        
        self.frame_2.hide()
        self.pushButton.clicked.connect(self.show_icons)
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.register_button()
        self.load_login_dtls()
        
        
    def device_date(self):     
        self.label_47.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
        
    def show_icons(self):
        self.go_ahead="success"     
        #username=self.lineEdit.text()
        password=self.lineEdit.text()
        if(str(password) != ""):            
            #print(" user name :"+str(username)+" password :"+str(password))
            connection = sqlite3.connect("tyr.db")            
            results=connection.execute("select pwd from users_mst where user_id in (select login_user_id from global_var)")        
            rows=results.fetchall()
            if(str(password) == str(rows[0][0])):                   
                  self.frame_2.show()  
            else :
                   self.frame_2.hide()
                   self.go_ahead="No"               
            connection.close()
        else:
           self.frame_2.hide()
        
        
    
    def register_button(self):
        serial_no=self.getserial()
        #print("current serial No : "+str(serial_no))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select DEVICE_SERIAL_NO from GLOBAL_REPORTS_PARAM") 
        for x in results:
           #print("Device Serial No :"+str(x[0]))
           if(serial_no == str(x[0])):
               #self.go_ahead="Yes"
               self.pushButton_19.hide()
           else:
               #self.go_ahead="No"
               self.pushButton_19.show()
        connection.close()
        
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
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=Register_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
  
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=TY_15_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
   
    def open_new_window3(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=factory_reset_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
 
    def open_new_window4(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=ty_16_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
  
    def open_new_window5(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=usb_bkp_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
      
    def open_new_window6(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=users_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window7(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=date_time_set_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()

    def open_new_window8(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=spped_setup_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window9(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=change_pwd_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()  
   
    def open_new_window10(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=Master_info_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window11(self):       
        self.window = QtWidgets.QMainWindow()
        #self.window=myWindow()
        self.ui=load_cell_set_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def break_app(self):
        os.systbem("edxit")
        
    
    def load_login_dtls(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select login_user_id,login_user_role,login_user_name from global_var")       
        for x in results:           
                 self.login_user_id=str(x[0])
                 self.login_user_role=str(x[1])
                 self.login_user_name=str(x[2])
                 if(str(x[1]) == 'OPERATOR'):
                       self.pushButton_8.setDisabled(True)
                       self.pushButton_13.setDisabled(True)
                       self.pushButton_5.setDisabled(True)
                 
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AE_02_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
