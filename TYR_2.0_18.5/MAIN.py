from TY_12_TEST_LIST import TY_12_LIST_Ui_MainWindow
from TY_50_TEST_LIST_SPECS import TY_50_LIST_Ui_MainWindow
from TY_18_TEST_TYPE_REPORTS import TY_18_TEST_TYPE_REPORTS_Ui
from TY_07_UTM_MANNUAL_CONTROL_2 import TY_07_Ui_MainWindow
#from TY_04_SETTING import TY_04_Ui_MainWindow
from SETTINGS import setting_Ui_MainWindow
from TY_03_REPORTS import TY_03_Ui_MainWindow


from PyQt5 import QtCore, QtGui, QtWidgets
import os, subprocess


class MAIN_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 769)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(29, 29, 1311, 711))
        self.frame.setStyleSheet("border:3px solid black;\n"
"border-radius:60px;\n"
"background-color: rgb(230, 230, 230);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 400, 201, 191))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton{\n"
"border:0px solid black;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:100px;\n"
"background:None;\n"
"background-color: rgb(255, 255, 255);\n"
"image: url(logo-images/setting.png);\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"#pushButton:hover{\n"
"border:0px solid black;\n"
"\n"
"color: rgb(255, 85, 0);\n"
"background-color: rgb(255, 255, 255);image: url(:/backg/qt designer/setting_turn.png);background-color: rgb(230, 230, 230);\n"
"    image: url(logo-images/setting_turn.png);\n"
"}\n"
"#pushButton:pressed{image: url(logo-images/setting.png);\n"
"\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 100, 181, 181))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"border:0px solid black;\n"
"border-radius:30px;\n"
"background:None;\n"
"background-color: rgb(206, 206, 206);\n"
"image: url(logo-images/test.png);\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"#pushButton_2:hover{\n"
"border:0px solid black;\n"
"background-color: rgb(206, 206, 206);\n"
"image: url(logo-images/test_turn.png);\n"
"    background-color: rgb(230, 230, 230);\n"
"\n"
"}\n"
"#pushButton_2:pressed{image:url(logo-images/test.png);}\n"
"\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 80, 211, 221))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"border:0px solid black;\n"
"border-radius:100px;\n"
"background:None;\n"
"image: url(logo-images/report3.png);\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"#pushButton_3:hover{\n"
"border:0px solid black;\n"
"image: url(logo-images/report3_turn.png);\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"#pushButton_3:pressed{image: url(logo-images/report3.png);}\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(930, 70, 231, 241))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("#pushButton_4{\n"
"border:0px solid black;\n"
"border-radius:100px;\n"
"background:None;\n"
"image: url(logo-images/motor.png);\n"
"    background-color: rgb(230, 230, 230);\n"
"\n"
"}\n"
"#pushButton_4:hover{\n"
"border:0px solid black;\n"
"image: url(logo-images/motor_turn.png);\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"#pushButton_4:pressed{image: url(logo-images/motor.png);}\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 400, 201, 191))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("#pushButton_5{\n"
"border:0px solid black;\n"
"border-radius:100px;\n"
"background:None;\n"
"    image: url(logo-images/sample.png);\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"#pushButton_5:hover{\n"
"border:0px solid black;\n"
"    image: url(logo-images/sample_turn.png);\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"#pushButton_5:pressed{    image: url(logo-images/sample.png);}\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_5.setStyleSheet("#label_5{background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; color: rgb(0, 0, 255);\n"
"    }\n"
"#label_5:hover{\n"
"    font: italic 18pt \"Arial\";\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(610, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_9.setStyleSheet("#label_9{background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; \n"
"color: rgb(0, 0, 255);}\n"
"#label_9:hover{\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(1010, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_10.setStyleSheet("#label_10{background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; \n"
"color: rgb(0, 0, 255);}\n"
"#label_10:hover{\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(610, 620, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_11.setStyleSheet("#label_11{background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; \n"
"color: rgb(0, 0, 255);}\n"
"#label_11:hover{\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(150, 620, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_12.setStyleSheet("#label_12{background-color:rgb(255, 255, 255); border:1px solid black; border-radius: 15px; \n"
"color: rgb(0, 0, 255);}\n"
"#label_12:hover{\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(890, 620, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("#pushButton_6 {color: rgb(0, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_6:hover {border: 1px solid green; color: rgb(0, 0, 255);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));padding-bottom: 5px;padding-right: 5px;}#pushButton_6 :pressed {background-color: rgb(255, 255, 255);padding-top: 5px;padding-left: 5px;}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(1110, 620, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("#pushButton_7 {color: rgb(255, 0, 0);background:None;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));border-radius:20px;border-color: rgb(0, 0, 0);border-style:outset;border-width:1px;}#pushButton_7:hover { border: 1px solid red;color: rgb(0, 0, 0);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));padding-bottom: 5px;padding-right: 5px;}#pushButton_7:pressed {background-color: rgb(198, 198, 198);padding-top: 5px;padding-left: 5px;}\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_4_1 = QtWidgets.QLabel(self.frame)
        self.label_4_1.setGeometry(QtCore.QRect(490, 30, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4_1.setFont(font)
        self.label_4_1.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_4_1.setStyleSheet("background-color:rgb(255, 255, 255); border:None; border-radius: 15px; \n"
"color: rgb(0, 170, 0);")
        self.label_4_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4_1.setObjectName("label_19")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(960, 400, 201, 181))
        self.label.setStyleSheet("border:none;\n"
"image: url(logo-images/STARR LOGO.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4_1.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_9.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()      # setting
        self.pushButton_2.raise_()    # test 
        self.pushButton_3.raise_()     # report
        self.pushButton_4.raise_()     # motor
        self.pushButton_5.raise_()     # specimens
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Test"))
        self.label_9.setText(_translate("MainWindow", "Report"))
        self.label_10.setText(_translate("MainWindow", "Motor"))
        self.label_11.setText(_translate("MainWindow", "Specimens"))
        self.label_12.setText(_translate("MainWindow", "Setting"))
        self.pushButton_6.setText(_translate("MainWindow", "Shutdown"))
        self.pushButton_7.setText(_translate("MainWindow", "Reboot"))
        self.label_4_1.setText(_translate("MainWindow", "AnyDesk ID : "))
        self.pushButton.clicked.connect(self.open_new_window)
        self.pushButton_2.clicked.connect(self.open_new_window2)
        self.pushButton_3.clicked.connect(self.open_new_window3)
        self.pushButton_4.clicked.connect(self.open_new_window4)
        self.pushButton_5.clicked.connect(self.open_new_window5)
        self.pushButton_6.clicked.connect(self.shutdown_system)
        self.pushButton_7.clicked.connect(self.reboot_system)
        self.anydesk_open()
    def shutdown_system(self):
        os.system("sudo shutdown -P 0")
        # os.system("shutdown /s /t 0")
        
    def reboot_system(self):
        os.system("sudo reboot")
        # os.system("shutdown /r /t 0")

    def anydesk_open(self):
        self.anydesk_id =0
        os.system("rm -rf anydes_id_f.txt")
        os.system("anydesk --get-alias>> anydes_id_f.txt")
        f = open('anydes_id_f.txt','r')
        for line in f:                 
                    self.anydesk_id = line[0:29]
        print("self.anydesk_id:"+str(self.anydesk_id))
        self.label_4_1.setText("<font color=blue> AnyDesk ID: </font> "+str(self.anydesk_id))
        f.close()        
    
    def open_new_window2(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_18_TEST_TYPE_REPORTS_Ui()
        self.ui.setupUi(self.window)           
        self.window.show()        
        
    def open_new_window3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_04_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_50_LIST_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def open_new_window5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_07_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MAIN_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
