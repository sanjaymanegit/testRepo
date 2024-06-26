from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os


class date_time_set_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 40, 711, 411))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(310, 40, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(520, 270, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 330, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"")
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(320, 330, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(190, 110, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(510, 330, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 111, 51))
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
        self.label_5.setGeometry(QtCore.QRect(190, 200, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 200, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(170, 255, 255);\n color: rgb(0, 0, 0);")
        
        self.comboBox_2.setObjectName("comboBox_2")
#         self.comboBox_2.addItem("")
#         self.comboBox_2.addItem("")
#         self.comboBox_2.addItem("")
#         self.comboBox_2.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(310, 110, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setToolTipDuration(0)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(520, 100, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"")
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(450, 200, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(520, 200, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("background-color: rgb(170, 255, 255);\n color: rgb(0, 0, 0);")        
        
        self.comboBox_3.setObjectName("comboBox_3")
#         self.comboBox_3.addItem("")
#         self.comboBox_3.addItem("")
#         self.comboBox_3.addItem("")
#         self.comboBox_3.addItem("")
#         self.comboBox_3.addItem("")
#         self.comboBox_3.addItem("")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 60, 381, 261))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setStyleSheet("background-color: rgb(170, 255, 255);\n color: rgb(0, 0, 0);")        
        
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44:09"))
        self.label_2.setText(_translate("MainWindow", "Done."))
        self.pushButton_6.setText(_translate("MainWindow", "SET"))
        self.pushButton_7.setText(_translate("MainWindow", "RESET"))
        self.label_3.setText(_translate("MainWindow", "DATE :"))
        self.pushButton_8.setText(_translate("MainWindow", "CLOSE"))
        self.label_5.setText(_translate("MainWindow", "HH :"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "01"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "02"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "03"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "04"))
        self.pushButton_9.setText(_translate("MainWindow", "GET DATE"))
        self.label_6.setText(_translate("MainWindow", "MI :"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "01"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "02"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "03"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "04"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "06"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "10"))
        self.i=0        
        for x in range(24):            
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        
        
        self.i=0        
        for x in range(60):            
            self.comboBox_3.addItem("")
            self.comboBox_3.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        
        
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.label_2.hide()
        self.calendarWidget.clicked.connect(self.date_dd_click)        
        self.pushButton_9.clicked.connect(self.dt_onclick)
        self.pushButton_6.clicked.connect(self.set_date)
        self.pushButton_7.clicked.connect(self.reset_date)
        self.calendarWidget.hide()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
       
        
        
    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    
    def set_date(self):
        print("ok....")
        self.label_2.show()
        if(self.lineEdit.text() != ""):
            #self.label_4.setText(str(self.calendarWidget.selectedDate().toString("dd MMM yyyy"))+" "+str(self.comboBox.currentText())+":"+str(self.comboBox_2.currentText())+":00")
            self.new_date=str(self.calendarWidget.selectedDate().toString("dd MMM yyyy"))+" "+str(self.comboBox_2.currentText())+":"+str(self.comboBox_3.currentText())+":00"
            #print("new_date:"+str(self.new_date))
            os.system(" sudo date -s \""+str(self.new_date)+"\"")
            os.system("sudo hwclock -w")
            os.system("sudo hwclock -r")
            self.label_2.setText("DONE !") 
            self.label_2.show() 
        else:
            self.label_2.setText("Select Date.") 
            self.label_2.show() 
        
        
    def dt_onclick(self):
        self.calendarWidget.show()
        
    def date_dd_click(self):        
        temp_var = self.calendarWidget.selectedDate() 
        var_name = temp_var.toPyDate()        
        self.from_date=str(var_name)
        self.lineEdit.setText(str(self.calendarWidget.selectedDate().toString()))        
        self.calendarWidget.hide()
    
    def reset_date(self):
        self.lineEdit.setText("")         
        self.label_2.hide()
        self.comboBox_3.setCurrentText("00")
        self.comboBox_2.setCurrentText("00")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = date_time_set_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
