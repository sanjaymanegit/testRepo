
from PyQt5 import QtCore, QtGui, QtWidgets
from TY_05_SPECIMEN_2 import TY_05_Ui_MainWindow
from TY_05_SPECIMEN_3 import TY_05_SPECI_Ui_MainWindow
from TY_05_SPECIMEN_4 import TY_05_SPECI_4_ui_MainWindow
from TY_05_SPECIMEN_5 import TY_05_SPECI_5_ui_MainWindow
from TY_05_SPECIMEN_6 import TY_05_SPECI_6_ui_MainWindow
from TY_05_SPECIMEN_7 import TY_05_SPEC_7_Ui_MainWindow


import sqlite3
import re
import datetime
import time
import os,sys


class TY_50_LIST_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1390, 772)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 709))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.frame.setFont(font)
        self.frame.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(970, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 610, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 70, 1331, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(870, 610, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(30, 190, 341, 481))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(153, 255, 182);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(480, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(480, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(610, 140, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(490, 20, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        
        self.label_5_1 = QtWidgets.QLabel(self.frame)
        self.label_5_1.setGeometry(QtCore.QRect(10, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5_1.setFont(font)
        self.label_5_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5_1.setObjectName("label_5_1")
        
        
        
        self.lineEdit = QtWidgets.QLineEdit(self.frame)        
        self.lineEdit.setGeometry(QtCore.QRect(200, 22, 220, 41))
        #self.lineEdit.setMaxLength(6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("SU")
        self.lineEdit.setStyleSheet("color: rgb(0, 120, 200);")
        self.lineEdit.setObjectName("lineEdit")
       
        
        
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(610, 340, 401, 241))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(610, 210, 401, 101))
        self.textEdit.setObjectName("textEdit")
        ''''
       
        '''
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1390, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.modbus_port=""
        self.non_modbus_port=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00"))
        self.pushButton_4.setText(_translate("MainWindow", "ADD/EDIT Specimens"))
        self.pushButton_14.setText(_translate("MainWindow", "RETURN"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "TENSILE"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "COMPRESSION"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "TEAR"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "FLEXURAL"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "COF"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "ILLS"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "QLSS"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(_translate("MainWindow", "Test Name :"))
        self.label_10.setText(_translate("MainWindow", "Test Details :"))
        self.label_11.setText(_translate("MainWindow", "Tensile "))
        self.label_4.setText(_translate("MainWindow", "Select Test :"))
        self.label_5.setText(_translate("MainWindow", " TESTS TYPES ( SPECIMENS )"))
        self.label_5_1.setText(_translate("MainWindow", " User Name:"))
        self.pushButton_15.setText(_translate("MainWindow", "IMAGE"))
        
        self.pushButton_14.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(self.open_new_test_win)
        
        self.listWidget.doubleClicked.connect(self.selected_record)
        self.listWidget.clicked.connect(self.selected_record)
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  LOGIN_USER_NAME FROM GLOBAL_VAR") 
        for x in results:
            self.lineEdit.setText(str(x[0]))
        connection.close()
        
        self.load_data()
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
    
    
        
    
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    

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
    
    def selected_record(self):
        self.test_type_id=""
        self.pushButton_15.setText("")
        self.list_type=self.listWidget.currentItem().text()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  TEST_TYPE_NAME,TEST_TYPE_DTLS,TEST_TYPE_IMG_FILE,ACTIVE_Y_N,TEST_TYPE_ID FROM TEST_TYPE_MST WHERE ACTIVE_Y_N = 'Y' and TEST_TYPE_NAME||'('||TEST_TYPE_ID||')' = '"+str(self.list_type)+"'")
        for x in results:                    
                   self.label_11.setText(str(x[0]))
                   self.textEdit.setText(str(x[1])) #ADDRESS1
                   icon = QtGui.QIcon()
                   icon.addPixmap(QtGui.QPixmap("images/"+str(str(x[2]))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                   self.pushButton_15.setIcon(icon)
                   self.pushButton_15.setIconSize(QtCore.QSize(200, 160))
                   if(str(x[3]) == 'Y'):
                       self.pushButton_15.setEnabled(True)
                       self.pushButton_4.setEnabled(True)                       
                   else:
                       self.pushButton_15.setDisabled(True)
                       self.pushButton_4.setDisabled(True)
                   self.test_type_id=str(x[4])
                   
                   
                       
        connection.close()
        
        
        
    def open_new_test_win(self):        
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET LOGIN_USER_NAME='"+str(self.lineEdit.text())+"'")
        connection.commit();
        connection.close()
        if(str(self.test_type_id) == "18"):
            self.open_new_window_3()
        elif(str(self.test_type_id) == "19"):    
             self.open_new_window_3()
        elif(str(self.test_type_id) == "20"):    
             self.open_new_window_3()
        elif(str(self.test_type_id) == "21"):    
             self.open_new_window_3()
        elif(str(self.test_type_id) == "22"):    
             self.open_new_window_3()
        elif(str(self.test_type_id) == "23"):    
             self.open_new_window_4()
        elif(str(self.test_type_id) == "24"):    
             self.open_new_window_4()
        elif(str(self.test_type_id) == "25"):    
             self.open_new_window_4()
        elif(str(self.test_type_id) == "26"):    
             self.open_new_window_4()
        elif(str(self.test_type_id) == "28"):    
             self.open_new_window_4()
        elif(str(self.test_type_id) == "29"):    
             self.open_new_window_5()
        elif(str(self.test_type_id) == "30"):    
             self.open_new_window_5()
        elif(str(self.test_type_id) == "32"):    
             self.open_new_window_6()
        elif(str(self.test_type_id) == "33"):    
             self.open_new_window_6()
        elif(str(self.test_type_id) == "36"):    
             self.open_new_window_4()
        elif(str(self.test_type_id) == "38"):    
             self.open_new_window_7()
        elif(str(self.test_type_id) == "39"):    
             self.open_new_window_4()
        else:
            self.open_new_window()
            print("Invalid Test ID"+str(self.test_type_id))
            
    
    
    def open_new_window(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_05_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_3(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_05_SPECI_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_4(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_05_SPECI_4_ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_5(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_05_SPECI_5_ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
   
    def open_new_window_6(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_05_SPECI_6_ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
     
    def open_new_window_7(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_05_SPEC_7_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_50_LIST_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
