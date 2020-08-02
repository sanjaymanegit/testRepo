# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_24_ur_RATES.ui'
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

class wt_24_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1181, 683)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1111, 591))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        
        
        
        
        self.operation_flg=""
        self.rate_id="0"
        
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(160, 60, 631, 121))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_1.setGeometry(QtCore.QRect(30, 50, 141, 31))
        self.lineEdit_1.setText("")
        self.lineEdit_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(210, 50, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 50, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 50, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(100, 210, 921, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        
        
        
        
        
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(130, 10, 451, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(380, 10, 221, 31))
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
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(850, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 240, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(920, 500, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(160, 300, 431, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(10)
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
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 240, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(440, 240, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(570, 240, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(760, 500, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(660, 300, 381, 171))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_2)
        self.lineEdit_2.setValidator(input_validator)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
        self.lineEdit_3.setValidator(input_validator)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1181, 21))
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
        
        self.groupBox.setTitle(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Show Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Return"))
        
        
        
        self.label_19.setText(_translate("MainWindow", "Rates Configuration"))
        self.label_3.setText(_translate("MainWindow", "Saved Successfully !"))
        self.label_3.hide()
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.pushButton_6.setText(_translate("MainWindow", "Add"))
        self.pushButton_7.setText(_translate("MainWindow", "Return"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Vehicle Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Rate"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Minimum Allowed Weight"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Rate ID"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Truck"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "100"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "4000"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_8.setText(_translate("MainWindow", "Edit"))
        self.pushButton_9.setText(_translate("MainWindow", "Delete"))
        self.pushButton_10.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_11.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "Vehicle Type:"))
        self.label_2.setText(_translate("MainWindow", "Rate :"))
        self.label_5.setText(_translate("MainWindow", "Mini. Wt Allowed:"))
        self.pushButton_7.clicked.connect(MainWindow.close)
        self.pushButton_11.clicked.connect(self.load_data)
        self.pushButton_10.clicked.connect(self.select_all_data)
        self.pushButton_6.clicked.connect(self.add_click)
        self.pushButton_8.clicked.connect(self.edit_click)
        self.pushButton_9.clicked.connect(self.delete_click)
        
        self.pushButton.clicked.connect(self.login_page)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.reset_loging)
        
        self.select_all_data()
        self.hide_page()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    
    
    def login_page(self):
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PWD FROM SERVICES_MST WHERE SERVICE_NAME = 'WEIGHING_MODE' AND STATUS = 'ACTIVE'") 
        for x in results:  
            if(str(self.lineEdit_1.text()) == str(x[0])):          
                #self.go_ahead_flg="No"                
                self.show_page()
            else:
                self.label_3.setText("Incorrect Password.") 
                self.label_3.show()   
                self.hide_page()
                 
        connection.close() 
        
    def reset_loging(self):
        self.lineEdit_1.setText("")         
        self.label_3.hide()
        self.hide_page()
    
    
    def hide_page(self):
        self.pushButton_6.hide()
        self.pushButton_7.hide()
        self.pushButton_8.hide()
        self.pushButton_9.hide()
        self.pushButton_10.hide()
        self.pushButton_11.hide()
        self.tableWidget.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_5.hide()
        
        
    def show_page(self):
        self.pushButton_6.show()
        self.pushButton_7.show()
        self.pushButton_8.show()
        self.pushButton_9.show()
        self.pushButton_10.show()
        self.pushButton_11.show()
        self.tableWidget.show()
        self.lineEdit.show()
        self.lineEdit_2.show()
        self.lineEdit_3.show()
        self.label.show()
        self.label_2.show()
        self.label_5.show()    
        
        
        
   
    def select_all_data(self):     
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT VEHICLE_TYPE,RATE_RS,MIN_ALLOWED_WT,RATE_ID FROM RATES_MST")                        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                #self.lineEdit.setText("")
        
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.label_3.hide()
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)  


    def add_data(self):
        if(self.lineEdit.text() != ""):
            connection = sqlite3.connect("wt.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO RATES_MST(VEHICLE_TYPE,RATE_RS,MIN_ALLOWED_WT ) values ('"+self.lineEdit.text()+"','"+self.lineEdit_2.text()+"','"+self.lineEdit_3.text()+"')")                    
            connection.commit();                    
            connection.close()   
      
        self.label_3.setText("Record Added Successfully.")
        self.label_3.show()
        self.select_all_data()
        
    def edit_data(self):
        if(self.lineEdit.text() != ""):
            connection = sqlite3.connect("wt.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE RATES_MST SET VEHICLE_TYPE='"+self.lineEdit.text()+"',RATE_RS='"+self.lineEdit_2.text()+"',MIN_ALLOWED_WT='"+self.lineEdit_3.text()+"' WHERE  RATE_ID ='"+str(self.rate_id)+"'")                    
            connection.commit();                    
            connection.close()   
       
        self.label_3.setText("Record Saved Successfully.")
        self.label_3.show()
        self.select_all_data()
      
    def delete_data(self):
        if(self.lineEdit.text() != ""):
            connection = sqlite3.connect("wt.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("DELETE FROM RATES_MST WHERE RATE_ID ='"+str(self.rate_id)+"'")                    
            connection.commit();                    
            connection.close()   
        
        self.label_3.setText("Record Deleted Successfully.")
        self.label_3.show()
        self.select_all_data()
        
    def add_click(self):
        self.operation_flg="ADD"
        self.pushButton_11.setText("ADD")
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.label_3.setText("Please add new record.")
        self.label_3.show() 
        
        
    def edit_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="EDIT"
            self.pushButton_11.setText("SAVE")
            self.lineEdit.setText(self.tableWidget.item(row, 0).text())
            self.lineEdit_2.setText(self.tableWidget.item(row, 1).text())
            self.lineEdit_3.setText(self.tableWidget.item(row, 2).text())
            self.rate_id=self.tableWidget.item(row, 3).text()
            self.label_3.setText("Please edit and save record.")
            self.label_3.show() 
            
        else:    
            self.label_3.setText("Please Select the record.")
            self.label_3.show() 
        
    def delete_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="DELETE"
            self.pushButton_11.setText("DELETE")
            self.lineEdit.setText(self.tableWidget.item(row, 0).text())
            self.lineEdit_2.setText(self.tableWidget.item(row, 1).text())
            self.lineEdit_3.setText(self.tableWidget.item(row, 2).text())
            self.rate_id=self.tableWidget.item(row, 3).text()
            self.label_3.setText("Please delete record.")
            self.label_3.show() 
        else:    
            self.label_3.setText("Please Select the record.")
            self.label_3.show() 
        
    def load_data(self):        
        if(self.operation_flg=="ADD"):
                print("inside Add ")
                self.add_data()
        elif(self.operation_flg=="EDIT"):
                print("inside edit ")
                self.edit_data()
        elif(self.operation_flg=="DELETE"):
                print("inside delete ")
                self.delete_data()
        else:
                print("Invalid Operation.")
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_24_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
