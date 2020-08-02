# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_26_ur_TARE_CONF.ui'
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

class wt_26_Ui_MainWindow(object):
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
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(160, 40, 521, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(380, 130, 221, 31))
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
        self.pushButton_6.setGeometry(QtCore.QRect(160, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(710, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(160, 230, 431, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
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
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(440, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(570, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(700, 520, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(640, 240, 361, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
        self.lineEdit_3.setValidator(input_validator)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(840, 520, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
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
        self.label_19.setText(_translate("MainWindow", "TARE Weight Configuration"))
        self.label_3.setText(_translate("MainWindow", "Saved Successfully !"))
        self.label_3.hide()
        self.label_4.setText(_translate("MainWindow", "24 Nov 2019 12:23:11"))
        self.pushButton_6.setText(_translate("MainWindow", "Add"))
        self.pushButton_7.setText(_translate("MainWindow", "Return"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Vehicle No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vehicle Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tare Weight (Kg)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Rec Id"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "4000"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Truck"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "100"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_8.setText(_translate("MainWindow", "Edit"))
        self.pushButton_9.setText(_translate("MainWindow", "Delete"))
        self.pushButton_10.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_11.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "Vehicle No:"))
        self.label_2.setText(_translate("MainWindow", "Vehicle Type :"))
        self.label_5.setText(_translate("MainWindow", "Tare Wt. Kg"))
        #self.comboBox.setItemText(0, _translate("MainWindow", "Truck"))
        #self.comboBox.setItemText(1, _translate("MainWindow", "Trailer"))
        self.pushButton_12.setText(_translate("MainWindow", "Reset"))
        self.pushButton_7.clicked.connect(MainWindow.close)
        
        self.pushButton_11.clicked.connect(self.load_data)
        self.pushButton_10.clicked.connect(self.select_all_data)
        self.pushButton_6.clicked.connect(self.add_click)
        self.pushButton_8.clicked.connect(self.edit_click)
        self.pushButton_9.clicked.connect(self.delete_click)
        self.pushButton_12.clicked.connect(self.reset_fun)
        
        self.select_all_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.load_vehicle_types()
    
    def reset_fun(self):
        self.lineEdit_3.setText("")
        self.lineEdit.setText("")
    
    def load_vehicle_types(self):
        self.i=0
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT distinct VEHICLE_TYPE FROM RATES_MST") 
        for x in results:            
            self.comboBox.addItem("")
            self.comboBox.setItemText(self.i,str(x[0]))
            #print("i :"+str(x[0]))
            self.i=self.i+1
        connection.close()  
    
    
    def device_date(self):     
        self.label_4.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    def select_all_data(self):     
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT VEHICLE_NO,VEHICLE_TYPE,TARE_WT_KG,REC_ID FROM TARE_WT_MST")                        
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
        #self.lineEdit_2.setText("")
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
                    cursor.execute("INSERT INTO TARE_WT_MST(VEHICLE_NO,VEHICLE_TYPE,TARE_WT_KG) values ('"+self.lineEdit.text()+"','"+self.comboBox.currentText()+"','"+self.lineEdit_3.text()+"')")                    
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
                    cursor.execute("UPDATE TARE_WT_MST SET VEHICLE_NO='"+self.lineEdit.text()+"',VEHICLE_TYPE='"+self.comboBox.currentText()+"',TARE_WT_KG='"+self.lineEdit_3.text()+"' WHERE  REC_ID ='"+str(self.rate_id)+"'")                    
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
                    cursor.execute("DELETE FROM TARE_WT_MST WHERE REC_ID ='"+str(self.rate_id)+"'")                    
            connection.commit();                    
            connection.close()   
        
        self.label_3.setText("Record Deleted Successfully.")
        self.label_3.show()
        self.select_all_data()
        
    def add_click(self):
        self.operation_flg="ADD"
        self.pushButton_11.setText("ADD")
        self.lineEdit.setText("")
        #self.comboBox.setText("")
        self.lineEdit_3.setText("")
        self.label_3.setText("Please add new record.")
        self.label_3.show() 
        
        
    def edit_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="EDIT"
            self.pushButton_11.setText("SAVE")
            self.lineEdit.setText(self.tableWidget.item(row, 0).text())
            self.comboBox.setCurrentText("ok")
            print("current text :"+str(self.tableWidget.item(row, 1).text()))
            self.comboBox.setCurrentText(self.tableWidget.item(row, 1).text())
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
            self.comboBox.setCurrentText(self.tableWidget.item(row, 1).text())
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
    ui = wt_26_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
