#from fci_04_batch_issues_submenu import fci_04_Ui_MainWindow
from AE_Main_01 import AE_01_Ui_MainWindow
import urllib.request
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
import sys,os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        #MainWindow.setStyleSheet("background-color: rgb(47, 141, 255);\n"
#"border-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1291, 711))
        #self.frame.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame.setStyleSheet("background-color: rgb(215, 255, 252);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, 60, 681, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(244, 244, 0); background-color: rgb(170, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(990, 60, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        #self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 590, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius:20px;\n"
        "color: rgb(244, 244, 0); background-color: rgb(170, 0, 0);"
        "border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")        
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(650, 590, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-radius:20px;\n"
        "color: rgb(244, 244, 0);  background-color: rgb(170, 0, 0);"
        "border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(810, 580, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(270, 190, 681, 331))
        self.frame_2.setStyleSheet("color: rgb(0, 0, 0); \n background-color: rgb(255, 242, 249);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(210, 50, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 150, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 240, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 200, 158);\n"
"color: rgb(0, 0, 0);"
    "border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 240, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 200, 158);\n"
"color: rgb(0, 0, 0);"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(400, 130, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        #self.label_4.setStyleSheet("color: rgb(85, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(20, 590, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.go_ahead="Failed"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ASIAN TEST EQUIPMENT"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00"))
        self.pushButton_2.setText(_translate("MainWindow", "SHUT DOWN"))
        self.pushButton_5.setText(_translate("MainWindow", "REBOOT"))
        self.label_21.setText(_translate("MainWindow", "AnyDesk Id: 456533323"))
        self.label_2.setText(_translate("MainWindow", "Login ID. :"))
        self.label_3.setText(_translate("MainWindow", "Password  :"))
        self.pushButton_3.setText(_translate("MainWindow", "Login"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset"))
        self.label_4.setText(_translate("MainWindow", "Failed to Login !"))
        self.label_22.setText(_translate("MainWindow", "Assistance:9773540255"))
        
        self.label_4.hide()
        self.anydesk_open()
        #self.check_internet_connection()
        self.pushButton_2.clicked.connect(self.shutdown_system)
        self.pushButton_5.clicked.connect(self.reboot_system)
        self.pushButton_4.clicked.connect(self.reset_fun)
        self.pushButton_3.clicked.connect(self.login_check) 
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def reset_fun(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label_4.hide()
        
    def connect(self):
        try:
            urllib.request.urlopen('http://google.com') #Python 3.x
            return True
        except:
            return False
    
    def check_internet_connection(self):  
        if (self.connect()):
              self.toolButton.setText("On")
              #self.label_22.show()
              self.toolButton.setStyleSheet("background-color: rgb(0, 170, 0);")
    
        else:
              self.toolButton.setText("Off")              
              #self.label_22.show()
              self.toolButton.setStyleSheet("background-color: rgb(170, 0, 0);")
    
    
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
        self.label_21.setText("<font color=blue> AnyDesk ID:  </font> <font color=green>"+str(self.anydesk_id)+"</font>")
        f.close()
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
        
    def login_check(self):
        self.go_ahead="success"     
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        if(str(username) != ""):            
            print(" user name :"+str(username)+" password :"+str(password))
            connection = sqlite3.connect("tyr.db")
            print("select first_name,last_name,role,user_id from users_mst where login_id='"+str(username)+"' and pwd='"+str(password)+"'")
            results=connection.execute("select first_name,last_name,role,user_id from users_mst where login_id='"+str(username)+"' and pwd='"+str(password)+"'")        
            rows=results.fetchall()
            if(len(rows)>0 and self.go_ahead=="success") :
                #self.log_audit(rows[0][3],"Login","Login into to System.")
                f_name=rows[0][0]
                l_name=rows[0][1]   
                u_role=rows[0][2]        
                self.save_username_role(f_name,l_name,u_role,rows[0][3])
                self.reset_fun()
                self.open_new_window()
                
            else :
                self.save_username_role("NA","NA","NA","0")           
                self.label_4.setText("Login Failed!")
                self.label_4.show()
            connection.close()
        else:
            self.label_4.setText("Login Id  is Empty.")
            self.label_4.show()
        

    
    def save_username_role(self,f_name,l_name,u_role,user_id):
        login_user_name = f_name+" "+l_name+" ["+u_role+"]"
        #print(login_user_name)
        connection = sqlite3.connect("tyr.db")
        with connection:        
            cursor = connection.cursor()       
            cursor.execute("""update global_var set LOGIN_USER_NAME=?, LOGIN_USER_ID=?, LOGIN_USER_ROLE=?""", [login_user_name,user_id,u_role])                
        connection.commit();
        connection.close()
        
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=AE_01_Ui_MainWindow()
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
