# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ur_05_ADMIN_USERS.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class ur_05_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 711))
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.operation_flg=""
        self.gender=""
        self.dr_id=""
        self.gender_toedit=""
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(30, 10, 391, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(1110, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(10, 620, 101, 71))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/backword1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(100, 100))
        self.toolButton.setObjectName("toolButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(540, 40, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(350, 110, 631, 121))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 201, 31))
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(270, 50, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 50, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(50, 270, 1241, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(160, 330, 551, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(740, 330, 71, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(850, 330, 151, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(800, 630, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(1200, 630, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(1070, 630, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(940, 630, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(1040, 330, 91, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(1150, 330, 151, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(740, 370, 71, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(850, 380, 82, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(960, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(740, 420, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(850, 430, 251, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(740, 480, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(850, 480, 251, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(740, 530, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(850, 540, 251, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reports"))
        self.label_31.setText(_translate("MainWindow", "Doctors  Details"))
        self.label_30.setText(_translate("MainWindow", "16 Jan 2020 12:14:15"))
        self.label_3.setText(_translate("MainWindow", "Incorrect Password."))
        self.label_3.hide()
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Qualification"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Contact No."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email ID"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Dr.ID"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Bharat Pise"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "M.B.B.S"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "9877765468"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "bharat@gmail.com"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "Male"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Name :"))
        self.pushButton_6.setText(_translate("MainWindow", "Add"))
        self.pushButton_10.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_9.setText(_translate("MainWindow", "Delete"))
        self.pushButton_9.setDisabled(True)
        self.pushButton_8.setText(_translate("MainWindow", "Save"))
        self.pushButton_8.setDisabled(True)
        self.label_2.setText(_translate("MainWindow", "Gender :"))
        self.radioButton.setText(_translate("MainWindow", "Male"))
        self.radioButton_2.setText(_translate("MainWindow", "Female"))
        self.label_4.setText(_translate("MainWindow", "Qualification :"))
        self.label_5.setText(_translate("MainWindow", "Email ID:"))
        self.label_6.setText(_translate("MainWindow", "Contact No :"))
        self.radioButton.setChecked(True)
        self.toolButton.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.login_page)
        #self.pushButton_2.clicked.connect(self.reset_loging)
        self.pushButton_10.clicked.connect(self.select_all_data)
        self.pushButton_6.clicked.connect(self.add_click)
        self.tableWidget.doubleClicked.connect(self.fetch_data_from_tw)
        self.pushButton_8.clicked.connect(self.edit_click)
        self.pushButton_9.clicked.connect(self.delete_click)
        self.pushButton_10.clicked.connect(self.refresh_fun)
        '''
        
        
        
        '''
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        
        self.timer1.start(1)
        #self.timer1.stop()
        self.hide_objects()
       
    def device_date(self):     
        self.label_30.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def refresh_fun(self):
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.select_all_data()
        
    def fetch_data_from_tw(self):
        self.lineEdit_2.setText("ok fname")
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            xx=str(self.tableWidget.item(row, 0).text()).split()
            '''
            #self.lineEdit_2.setText(self.tableWidget.item(row, 1).text())      
            print("1 col text :"+str(self.tableWidget.item(row, 0).text()))
           
            print("fname :"+str(xx[0])+" , mname :"+str(xx[1])+"  ,lname :"+str(xx[2]))
            print("2 col text :"+str(self.tableWidget.item(row, 1).text()))            
            print("3 col text :"+str(self.tableWidget.item(row, 2).text()))
            print("4 col text :"+str(self.tableWidget.item(row, 3).text()))
            print("5 col text :"+str(self.tableWidget.item(row, 4).text()))
            print("6 col text :"+str(self.tableWidget.item(row, 5).text()))
            '''
            self.dr_id=str(self.tableWidget.item(row, 5).text())
            self.gender_toedit=(self.tableWidget.item(row, 4).text())
            self.lineEdit_2.setText(str(xx[0]))
            self.lineEdit_3.setText(str(xx[1]))
            self.lineEdit_4.setText(str(xx[2]))
            self.lineEdit_5.setText(str(self.tableWidget.item(row, 1).text()))
            self.lineEdit_6.setText(str(self.tableWidget.item(row, 2).text()))
            self.lineEdit_7.setText(str(self.tableWidget.item(row, 3).text()))
            if(str(self.tableWidget.item(row, 4).text())== 'Male'):
                    self.radioButton.setChecked(True)                    
            else: 
                    self.radioButton_2.setChecked(True)
            
            self.pushButton_8.setEnabled(True)
            self.pushButton_9.setEnabled(True)
            
        else:    
            self.label_3.setText("Please Select the record.")
            self.label_3.show()
        
    def select_all_data(self):     
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT fname||' '||mname||' '||lname,DR_QUAL,DR_EMAIL_ID,DR_CONTACT,DR_GENDER,DR_ID FROM DOCTORS_INFO")                        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                #self.lineEdit.setText("")
        
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.lineEdit.setText("")
        #self.lineEdit_2.setText("")
        self.pushButton_8.setDisabled(True)
        self.pushButton_9.setDisabled(True)
        self.label_3.hide()
        connection.close() 
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i) 
    
    def load_data(self):        
        if(self.operation_flg=="ADD"):
                #print("inside Add ")
                self.add_data()
        elif(self.operation_flg=="EDIT"):
                #print("inside edit ")
                self.edit_data()
        elif(self.operation_flg=="DELETE"):
                #print("inside delete ")
                self.delete_data()
        else:
                print("Invalid Operation.")
         
    def add_click(self):
        self.operation_flg="ADD"       
        self.load_data()
        
    def add_data(self):
        if(self.lineEdit_2.text() != ""):
            if(self.radioButton.isChecked()):
                        self.gender="Male"
            else:           
                        self.gender="Female"
                        
            connection = sqlite3.connect("ur.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO DOCTORS_INFO(fname,mname,lname,DR_QUAL,DR_CONTACT,DR_EMAIL_ID,DR_GENDER) values ('"+self.lineEdit_2.text()+"','"+self.lineEdit_3.text()+"','"+self.lineEdit_4.text()+"','"+self.lineEdit_5.text()+"','"+self.lineEdit_6.text()+"','"+self.lineEdit_7.text()+"','"+self.gender+"')")                    
            connection.commit();                    
            connection.close()   
      
        self.label_3.setText("Record Added Successfully.")
        self.label_3.show()
        self.select_all_data()
    
    def edit_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="EDIT"
            self.load_data()
        else:    
            self.label_3.setText("Please Select the record.")
            self.label_3.show() 
    
    def edit_data(self):
        if(self.lineEdit_2.text() != ""):
            connection = sqlite3.connect("ur.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE DOCTORS_INFO SET fname='"+self.lineEdit_2.text()+"',mname='"+self.lineEdit_3.text()+
                                   "',lname='"+self.lineEdit_4.text()+"',DR_QUAL='"+self.lineEdit_5.text()+"',DR_CONTACT='"+self.lineEdit_6.text()+
                                   "',DR_EMAIL_ID='"+self.lineEdit_7.text()+"',DR_GENDER='"+self.gender_toedit+"' WHERE  DR_ID ='"+str(self.dr_id)+"'")                    
            connection.commit();                    
            connection.close()   
       
        self.label_3.setText("Record Saved Successfully.")
        self.label_3.show()
        self.select_all_data()
    
    def delete_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="DELETE"
            self.load_data()
        else:    
            self.label_3.setText("Please Select the record.")
            self.label_3.show()        
     
      
    def delete_data(self):
        if(self.lineEdit_2.text() != ""):
            connection = sqlite3.connect("ur.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("DELETE FROM DOCTORS_INFO WHERE DR_ID ='"+str(self.dr_id)+"'")                    
            connection.commit();                    
            connection.close()   
        
        self.label_3.setText("Record Deleted Successfully.")
        self.label_3.show()
        self.select_all_data()   
    def login_page(self):
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PWD FROM SERVICES_MST WHERE SERVICE_NAME = 'DOCTORS_DETAILS' AND STATUS = 'ACTIVE'") 
        for x in results:  
            if(str(self.lineEdit.text()) == str(x[0])):          
                self.go_ahead_flg="No"
                self.show_objects()
                self.label_3.hide()
                #self.load_data()
                self.select_all_data()
            else:
                self.label_3.show()   
                self.hide_objects()
                 
        connection.close()  
    
    def hide_objects(self):
        self.pushButton_8.hide()
        self.pushButton_9.hide()
        self.pushButton_10.hide()
        self.pushButton_6.hide()
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.tableWidget.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()
        
        
        
    def show_objects(self):
        self.pushButton_8.show()
        self.pushButton_9.show()
        self.pushButton_10.show()
        self.pushButton_6.show()
        self.radioButton.show()
        self.radioButton_2.show()
        self.label.show()
        self.label_2.show()
        self.label_4.show()
        self.label_5.show()
        self.label_6.show()
        self.tableWidget.show()
        self.lineEdit_2.show()
        self.lineEdit_3.show()
        self.lineEdit_4.show()
        self.lineEdit_5.show()
        self.lineEdit_6.show()
        self.lineEdit_7.show()
        self.lineEdit_2.setText("fname")
        self.lineEdit_3.setText("mname")
        self.lineEdit_4.setText("lname")
        self.lineEdit_5.setText("qual")
        self.lineEdit_6.setText("email")
        self.lineEdit_7.setText("contact")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ur_05_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
