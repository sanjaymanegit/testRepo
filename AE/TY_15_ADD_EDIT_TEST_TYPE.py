
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton


import sqlite3
import re
import datetime
import time
import os,sys


class TY_15_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1321, 691))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(1050, 60, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(670, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 120, 1321, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setGeometry(QtCore.QRect(340, 60, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(180, 50, 121, 51))
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
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(790, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(350, 10, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 170, 1271, 501))
        self.frame_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.label_21 = QtWidgets.QLabel(self.frame_2)
        self.label_21.setGeometry(QtCore.QRect(40, 30, 151, 31))
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
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(30, 70, 261, 391))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(3)
        self.listWidget.setObjectName("listWidget")
        self.label_25 = QtWidgets.QLabel(self.frame_2)
        self.label_25.setGeometry(QtCore.QRect(350, 10, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("")
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_2)
        self.label_26.setGeometry(QtCore.QRect(320, 70, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("")
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.frame_2)
        self.label_28.setGeometry(QtCore.QRect(340, 140, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("")
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setGeometry(QtCore.QRect(510, 140, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_44 = QtWidgets.QLabel(self.frame_2)
        self.label_44.setGeometry(QtCore.QRect(330, 200, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("")
        self.label_44.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(510, 200, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_43 = QtWidgets.QLabel(self.frame_2)
        self.label_43.setGeometry(QtCore.QRect(340, 280, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("")
        self.label_43.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_43.setObjectName("label_43")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(510, 280, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(330, 400, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 203, 209);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 400, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 203, 209);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(620, 400, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 203, 209);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(780, 400, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 203, 209);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_27 = QtWidgets.QLabel(self.frame_2)
        self.label_27.setGeometry(QtCore.QRect(840, 100, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("")
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(890, 20, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_24.setLineWidth(1)
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(870, 150, 311, 201))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(510, 70, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_32 = QtWidgets.QLabel(self.frame_2)
        self.label_32.setGeometry(QtCore.QRect(510, 10, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(910, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.test_type_id=""
        self.list_type=""
        self.operation_flg=""
        self.rec_count=0


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00 "))
        self.pushButton_9.setText(_translate("MainWindow", "Login"))
        self.label_22.setText(_translate("MainWindow", "PASSWORD :"))
        self.pushButton_13.setText(_translate("MainWindow", "Reset"))
        self.label_23.setText(_translate("MainWindow", "Configure Test"))
        self.label_21.setText(_translate("MainWindow", "Test Type List :"))
        self.label_25.setText(_translate("MainWindow", "Serial. No.:"))
        self.label_26.setText(_translate("MainWindow", "Test Name :"))
        self.label_28.setText(_translate("MainWindow", "Active :"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Y"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "N"))
        self.label_44.setText(_translate("MainWindow", "Image File :"))
        self.label_43.setText(_translate("MainWindow", "File Path :"))
        self.lineEdit_16.setText(_translate("MainWindow", "images"))
        self.pushButton_11.setText(_translate("MainWindow", "ADD"))
        self.pushButton_7.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_10.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_8.setText(_translate("MainWindow", "REFRESH"))
        self.label_27.setText(_translate("MainWindow", "Test Description:"))
        self.label_24.setText(_translate("MainWindow", "Message: Successfully Saved ."))
        self.label_32.setText(_translate("MainWindow", "0001"))
        self.pushButton_12.setText(_translate("MainWindow", "Return"))
        self.pushButton_12.clicked.connect(MainWindow.close)
        self.pushButton_9.clicked.connect(self.login_page)
        self.pushButton_13.clicked.connect(self.reset_loging)
        self.listWidget.clicked.connect(self.selected_record)
        
        self.pushButton_11.clicked.connect(self.s_add_click) 
        self.pushButton_7.clicked.connect(self.s_edit_click)       
        self.pushButton_10.clicked.connect(self.s_delete_click)
        self.pushButton_8.clicked.connect(self.s_reset_data)
        
        self.pushButton_11.setDisabled(True) #add
        self.pushButton_7.setDisabled(True)  #save
        self.pushButton_10.setDisabled(True) #delete           
        self.pushButton_8.setDisabled(True) #reset
                       
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.frame_2.hide()
      
    
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def login_page(self):
         if(str(self.lineEdit_17.text()) == 'singhisking'):          
                self.go_ahead_flg="No"
               # self.groupBox_2.show()
                self.load_data()
         else:
                self.label_24.setText("Incorrect Password.") 
                self.label_24.show()   
                #self.groupBox_2.hide()
                self.frame_2.hide()
    
    def reset_loging(self):
        self.lineEdit_17.setText("")
        self.lineEdit_13.setText("")
        self.lineEdit_15.setText("")
        self.lineEdit_16.setText("")
        self.textEdit.setText("")
        
        self.label_24.hide()
        self.listWidget.clear()
        connection = sqlite3.connect("tyr.db")       
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'TEST_TYPE_MST'")       
        for x in results:           
                 self.label_32.setText(str(x[0]))            
        connection.close()  
        
        
        
        #self.groupBox_2.hide()
    def load_data(self):
        self.listWidget.clear() 
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  TEST_TYPE_NAME ||'-'||TEST_TYPE_ID FROM TEST_TYPE_MST order by TEST_TYPE_ID ") 
        for x in results:
            self.listWidget.addItem(str(x[0]))
            self.rec_count=self.rec_count+1
        connection.close()
        if(int(self.rec_count) > 0):
            self.listWidget.setCurrentRow(0)
            self.selected_record()
            self.frame_2.show()
        

    def selected_record(self):
        self.test_type_id=""
        #self.pushButton_15.setText("")
        self.list_type=self.listWidget.currentItem().text()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  TEST_TYPE_NAME,TEST_TYPE_DTLS,TEST_TYPE_IMG_FILE,ACTIVE_Y_N,TEST_TYPE_ID FROM TEST_TYPE_MST WHERE  TEST_TYPE_NAME ||'-'||TEST_TYPE_ID = '"+str(self.list_type)+"'")
        for x in results:                    
                   self.lineEdit_15.setText(str(x[0])) #Test Name
                   self.textEdit.setText(str(x[1])) #TEST DETAILS
                   self.lineEdit_13.setText(str(x[2])) # image File Name
                   self.lineEdit_16.setText("images/") #image file path
                   self.label_32.setText(str(x[4]))
                   if(str(x[3]) == 'Y'):
                       self.comboBox_2.setCurrentText("Y")                      
                   else:
                       self.comboBox_2.setCurrentText("N")
                   #print("Active Flag : "+str(x[3]))
                   self.test_type_id=str(x[4])
                   self.label_24.hide()
                   
                   self.pushButton_11.setDisabled(True) #add
                   self.pushButton_7.setEnabled(True)  #save
                   self.pushButton_10.setEnabled(True) #delete           
                   self.pushButton_8.setEnabled(True) #reset
                       
        connection.close()

    def s_reset_data(self):
        self.lineEdit_17.setText("")
        self.lineEdit_13.setText("")
        self.lineEdit_15.setText("")
        self.lineEdit_16.setText("")
        self.textEdit.setText("")   
        self.label_24.hide()
        self.pushButton_11.setEnabled(True) #add
        self.pushButton_7.setDisabled(True)  #save
        self.pushButton_10.setDisabled(True) #delete           
        self.pushButton_8.setEnabled(True) #reset
        connection = sqlite3.connect("tyr.db")       
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'TEST_TYPE_MST'")       
        for x in results:           
                 self.label_32.setText(str(x[0]))            
        connection.close()  
       
        
    def s_load_data(self):        
        if(self.operation_flg=="ADD"):
                #print("inside Add ")
                self.s_add_data()
        elif(self.operation_flg=="EDIT"):
                #print("inside edit ")
                self.s_edit_data()
        elif(self.operation_flg=="DELETE"):
                #print("inside delete ")
                self.s_delete_data()
        else:
                print("Invalid Operation.")
         
    def s_add_click(self):
        self.operation_flg="ADD"       
        self.s_load_data()
        
    def s_add_data(self):
        if(self.label_32.text() != ""):
            self.validate_ip()
            if(str(self.go_ahead )== 'Yes'):
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("INSERT INTO TEST_TYPE_MST(TEST_TYPE_NAME,TEST_TYPE_DTLS,TEST_TYPE_IMG_FILE,TEST_TYPE_PATH,ACTIVE_Y_N) VALUES ('"+self.lineEdit_15.text()+"','"+self.textEdit.toPlainText()+"','"+self.lineEdit_13.text()+"','"+self.lineEdit_16.text()+"','"+self.comboBox_2.currentText()+"')")                    
                    connection.commit();                    
                    connection.close()
                    self.label_24.setText("Record Added Successfully.")                   
                    self.label_24.show()
                    self.load_data()
        else :
            self.label_24.setText("Id is Empty.")
            self.label_24.show()
            
        
    
    def s_edit_click(self):
        row = self.listWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="EDIT"
            self.s_load_data()
        else:    
            self.label_24.setText("Please Select the record.")
            self.label_24.show() 
    
    def s_edit_data(self):
        if(self.label_32.text() != ""):
            self.validate_ip()
            if(str(self.go_ahead )== 'Yes'):
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("UPDATE TEST_TYPE_MST SET TEST_TYPE_NAME='"+self.lineEdit_15.text()+"',TEST_TYPE_DTLS='"+self.textEdit.toPlainText()+"',TEST_TYPE_IMG_FILE='"+self.lineEdit_13.text()+"',TEST_TYPE_PATH='"+self.lineEdit_16.text()+"',ACTIVE_Y_N='"+self.comboBox_2.currentText()+"' WHERE  TEST_TYPE_ID ='"+str(self.test_type_id)+"'")                    
                    connection.commit();                    
                    connection.close()
                    self.label_24.setText("Record Saved Successfully.")                    
                    self.label_24.show()
                    #self.load_data()   
        
     
           
                   
    
    def s_delete_click(self):
        row = self.listWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="DELETE"
            self.s_load_data()
        else:    
            self.label_24.setText("Please Select the record.")
            self.label_24.show()        
     
      
    def s_delete_data(self):        
        if(self.label_32.text() != ""):
            close = QMessageBox()
            close.setText("Confirm Deleteing Test TYPE ID : "+str(self.test_type_id))
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM TEST_TYPE_MST WHERE TEST_TYPE_ID ='"+str(self.test_type_id)+"'")
                            #cursor.execute("DELETE FROM TEST_TYPE_MST where 1=1") 
                    connection.commit();                    
                    connection.close()            
                    self.label_24.setText("Record Deleted Successfully.")
                    self.label_24.show()            
                    self.load_data()
            else:
                    self.label_24.setText("Canceled Delete..")                   
                    self.label_24.show()
            
    def validate_ip(self):
        self.go_ahead="No"
        if(self.lineEdit_15.text() == ""):
             self.label_24.setText("Test Name is Empty.")
             self.label_24.show()  
        elif(self.lineEdit_13.text()== ""):
             self.label_24.setText("Image File Name is Empty.")
             self.label_24.show() 
        elif(self.lineEdit_16.text()== ""):
             self.label_24.setText("Path is Empty.")
             self.label_24.show()
        elif(self.textEdit.toPlainText()== ""):
             self.label_24.setText("Description is Empty.")
             self.label_24.show()        
        else:
             self.go_ahead="Yes"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_15_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
