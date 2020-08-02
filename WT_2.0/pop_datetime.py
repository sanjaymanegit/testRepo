# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop_datetime.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os



class DATE_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 371))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.new_date=""
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 50, 531, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(130, 280, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 280, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 280, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(200, 160, 221, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 160, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(460, 160, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(610, 160, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(510, 160, 71, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(650, 160, 71, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(190, 110, 296, 183))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setGridVisible(True)
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
        self.label.setText(_translate("MainWindow",  datetime.datetime.now().strftime("%d %B %Y %H:%M:%S")))
        self.pushButton_4.setText(_translate("MainWindow", "Select Date"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Close"))
        self.pushButton.setText(_translate("MainWindow", "Set"))
        self.label_2.setText(_translate("MainWindow", "HH :"))
        self.label_3.setText(_translate("MainWindow", "MI:"))
        self.label_4.setText(_translate("MainWindow", "Saved Successfully."))
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.calendarWidget.clicked.connect(self.date_dd_click)
        self.pushButton_4.clicked.connect(self.dt_onclick)
        self.pushButton.clicked.connect(self.set_date)
        self.calendarWidget.hide()
        self.label_4.hide()  
        self.i=0        
        for x in range(24):            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        
        
        self.i=0        
        for x in range(60):            
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
        
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):
        self.label.setText(datetime.datetime.now().strftime("%d %B %Y %H:%M:%S"))
        
    
    def set_date(self):
        print("ok....")
        self.label_4.show()
        #self.label_4.setText(str(self.calendarWidget.selectedDate().toString("dd MMM yyyy"))+" "+str(self.comboBox.currentText())+":"+str(self.comboBox_2.currentText())+":00")
        self.new_date=str(self.calendarWidget.selectedDate().toString("dd MMM yyyy"))+" "+str(self.comboBox.currentText())+":"+str(self.comboBox_2.currentText())+":00"
        #print("new_date:"+str(self.new_date))
        os.system(" sudo date -s \""+str(self.new_date)+"\"")
        
        
    def dt_onclick(self):
        self.calendarWidget.show()
        
    def date_dd_click(self):        
        temp_var = self.calendarWidget.selectedDate() 
        var_name = temp_var.toPyDate()        
        self.from_date=str(var_name)
        self.lineEdit.setText(str(self.calendarWidget.selectedDate().toString()))
        #self.lineEdit.setText(str(self.calendarWidget.selectedDate().toString("dd-MMM-yyyy"))+" "+str(self.comboBox.currentText())+":"+str(self.comboBox_2.currentText())+":00")
        #self.lineEdit.setText(temp_var.strftime("%d %B %Y %H:%M:%S"))
        self.calendarWidget.hide()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DATE_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
