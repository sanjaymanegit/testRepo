

from PyQt5 import QtCore, QtGui, QtWidgets
from COMPANY_DETAILS import CompanyDetails
from TY_16_email_setup import ty_16_Ui_MainWindow
from usb_bakp import usb_bkp_Ui_MainWindow
from pop_factory_reset import  factory_reset_Ui_MainWindow
from SPEED_SETUP_POPUP import spped_setup_Ui_MainWindow
from date_time_set import date_time_Ui_MainWindow
from CONFIGURE_TEST import ConfigurTest



import sqlite3, shutil, datetime
from PyQt5.QtGui import QPixmap
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 1341, 721))
        self.frame.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border: 2px solid black;\n"
"border-radius:50px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(390, 30, 551, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("#label{\n"
"\n"
"border:1px solid red;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:30px;\n"
"background:None;\n"
"background-color: rgb(206, 206, 206);}\n"
"#label:hover{\n"
"border:1px solid black;\n"
"color: rgb(255, 85, 0);\n"
"background-color: rgb(231, 231, 231);}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 101, 101))
        # self.label_2.setPixmap(QtGui.QPixmap("C:/Users/win 10/Desktop/qt designer/python_company_logo.png"))
        self.label_2.setStyleSheet("background-image: url( ./images/STARR LOGO.jpg); border:1px solid; border-radius:opx;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(255, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(540, 150, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton:hover {border: 1px solid green; color: rgb(0, 255, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));padding-bottom: 5px;padding-right: 5px;}#pushButton:pressed {background-color: rgb(255, 255, 255);padding-top: 5px;padding-left: 5px;}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(170, 150, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        #self.lineEdit.setStyleSheet("#lineEdit {background:None;background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px;}#lineEdit:hover {background-color: rgb(220, 220, 220);border: 3px solid;    border-color: rgb(255, 255, 255);border-radius: 20px;}#lineEdit:focus{background-color: rgb(255, 255, 255);border: 1px solid rgba(131,131,131,255);border-radius: 20px}")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(1040, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:None;\n"
"border:None;\n"
"\n"
"color: rgb(255, 85, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(980, 160, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background:None;\n"
"border:None;\n"
"color: rgb(0, 85, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 220, 1261, 16))
        self.label_6.setStyleSheet("background:None;\n"
"border-radius:8px;\n"
"background-color: rgb(91, 91, 91);\n"
"border:None;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 150, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2 {color: rgb(255, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_2:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_2:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(1100, 60, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("#pushButton_3 {background:None;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"    \n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_3:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_3:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(100, 280, 1121, 401))
        self.frame_2.setStyleSheet("background:None;\n"
"background-color: rgb(240, 240, 240);\n"
"\n"
"border-radius:30px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(750, 170, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("#pushButton_9 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:35px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_9:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_9:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 30, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("#pushButton_4 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:35px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_4:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_4:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(750, 30, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("#pushButton_6{color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:35px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_6:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_6:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 30, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("#pushButton_5 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:35px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_5:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_5:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 170, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("#pushButton_8{color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:35px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_8:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_8:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 170, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("#pushButton_7 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:35px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_7:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_7:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(90, 300, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("#pushButton_10 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:35px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_10:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_10:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(420, 300, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("#pushButton_11 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:35px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_11:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_11:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_12.setGeometry(QtCore.QRect(760, 300, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("#pushButton_12 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:35px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_12:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_12:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Setting"))
        self.label_3.setText(_translate("MainWindow", "Password :"))
        self.pushButton.setText(_translate("MainWindow", "Procced"))
        self.label_4.setText(_translate("MainWindow", "23 May 2024 15:05:09"))
        self.label_5.setText(_translate("MainWindow", "Error : Massages "))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        self.pushButton_9.setText(_translate("MainWindow", "Date Time Setting"))
        self.pushButton_4.setText(_translate("MainWindow", "Company Details"))
        self.pushButton_6.setText(_translate("MainWindow", "Factory Reset"))
        self.pushButton_5.setText(_translate("MainWindow", "Configure Test"))
        self.pushButton_8.setText(_translate("MainWindow", "Report Setting"))
        self.pushButton_7.setText(_translate("MainWindow", "Email Setup"))
        self.pushButton_10.setText(_translate("MainWindow", "Copy PDF Report to USB"))
        self.pushButton_11.setText(_translate("MainWindow", "Speed Setup"))
        self.pushButton_12.setText(_translate("MainWindow", "Break App"))
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)  
        self.timer1.start(1)      
        self.timer1.timeout.connect(self.device_date)
        self.label_5.hide()
        self.frame_2.hide()
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.reset_field)
        self.pushButton_4.clicked.connect(self.CompanyDetails)
        self.pushButton_7.clicked.connect(self.open_new_window4)
        self.pushButton_10.clicked.connect(self.open_new_window6)
        self.pushButton_6.clicked.connect(self.open_new_window2)
        self.pushButton_11.clicked.connect(self.open_new_window)
        self.pushButton_9.clicked.connect(self.open_new_window7)
        self.pushButton_12.clicked.connect(self.break_app)
        self.pushButton_5.clicked.connect(self.ConfigurTest)
        
        self.pushButton.clicked.connect(self.check_pass)
        self.load_data()
    def device_date(self):
        self.label_4.setText(datetime.datetime.now().strftime("%d %B %Y %H:%M:%S"))
    
    def break_app(self):
        os.systbem("edxit")
        
    def load_data(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT COM_LOGO FROM GLOBAL_VAR")              
        
        for x in results:
                pixmap = QPixmap(x[0]) 
        connection.commit()                    
        connection.close() 
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)  
    def reset_field(self):
        self.lineEdit.setText("")
        self.frame_2.hide()    
        self.label_5.hide()
    def check_pass(self):
        password = str(1000)
        if (password == str(self.lineEdit.text())):
            self.frame_2.show()
        else:
            self.frame_2.hide()
            self.label_5.setText("Incorrect Password")
            self.label_5.show()
            print("incorrect password....")    
    
    def CompanyDetails(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = CompanyDetails()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def open_new_window(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=spped_setup_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def open_new_window4(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=ty_16_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show() 
        
    def open_new_window6(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=usb_bkp_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=factory_reset_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    
    def open_new_window7(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=date_time_Ui_MainWindow()               
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def ConfigurTest(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ConfigurTest()
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
