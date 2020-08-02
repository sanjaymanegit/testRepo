# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_28_SMS_HISTORY.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem
import sqlite3
from PyQt5.QtCore import QDate
import datetime

class wt_29_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1142, 573)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1091, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.from_date=""
        self.to_date=""
        self.whr_str=""   
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 321, 451))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 49, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(220, 50, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 71, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 100, 111, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 100, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 170, 91, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 220, 91, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 220, 161, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 270, 101, 31))
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 310, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 310, 101, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 380, 101, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        #self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 170, 161, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(350, 30, 721, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
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
        self.tableWidget.setHorizontalHeaderItem(6, item)        
        item = QtWidgets.QTableWidgetItem()
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
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget_2.setGeometry(QtCore.QRect(360, 140, 296, 183))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.calendarWidget_2.setFont(font)
        self.calendarWidget_2.setGridVisible(True)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(690, 140, 296, 183))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1142, 21))
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
        self.groupBox.setTitle(_translate("MainWindow", "SMS History"))
        self.label.setText(_translate("MainWindow", "From Date:"))
        self.pushButton.setText(_translate("MainWindow", "Date"))
        self.label_2.setText(_translate("MainWindow", "To Date:"))
        self.pushButton_2.setText(_translate("MainWindow", "Date"))
        self.checkBox.setText(_translate("MainWindow", "Serial ID"))
        self.checkBox_2.setText(_translate("MainWindow", "Status"))
        self.checkBox_4.setText(_translate("MainWindow", "All"))
        self.pushButton_3.setText(_translate("MainWindow", "Search"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset"))
        self.pushButton_6.setText(_translate("MainWindow", "Return"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PHONE_NO"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SMS_STATUS"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "SMS_DATE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SMS_MSG"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ERROR_MSG"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "SERIAL_ID"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "SMS_ID"))        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "001"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "SENT"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "14 Nov 2019"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "212"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "1"))        
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.from_dt_onclick)
        self.pushButton_2.clicked.connect(self.to_dt_onclick)
        self.calendarWidget.clicked.connect(self.date_dd_click_from)
        self.calendarWidget_2.clicked.connect(self.date_dd_click_to)
        
        self.checkBox.clicked.connect(self.serial_id_onclick)
        #self.checkBox_2.clicked.connect(self.status_on_click)
        self.checkBox_4.clicked.connect(self.all_onclick)
        self.pushButton_3.clicked.connect(self.list_report_data)
        self.calendarWidget.hide()
        self.calendarWidget_2.hide()
        self.list_report_data()
        self.load_data()
        
        
    
    def all_onclick(self):
        if (self.checkBox_4.isChecked()):
             self.checkBox.setChecked(True)
             self.checkBox.setDisabled(True)
             self.lineEdit_3.setDisabled(True)                          
        else:
             self.checkBox.setEnabled(True)   
             self.lineEdit_3.setEnabled(True)          
             
        '''     
        if(self.checkBox_2.isEnabled()):
             self.checkBox_2.setDisabled(True)             
        else:            
             self.checkBox_2.setEnabled(True)
        '''
    def serial_id_onclick(self):
        if(self.checkBox.isChecked()):            
             self.lineEdit_3.setEnabled(True)             
        else:            
             self.lineEdit_3.setDisabled(True)             
             
    def status_on_click(self):                 
        if(self.checkBox_2.isChecked()):
             self.comboBox_2.setEnabled(True)             
        else:            
             self.comboBox_2.setDisabled(True)             
                     
        
    def load_data(self):
        self.checkBox_4.setChecked(True)
        self.checkBox.setChecked(True)
        self.checkBox_2.setDisabled(True)
        self.checkBox.setDisabled(True)
        
        self.lineEdit_3.setDisabled(True)
        self.comboBox_2.setDisabled(True)
        
        self.default_dates()
    
    def default_dates(self):
        temp_var =QDate.currentDate()
        var_name = temp_var.toPyDate()
        self.from_date=str(var_name)
        self.to_date=str(var_name) 
        self.lineEdit.setText(str(QDate.currentDate().toString()))
        self.lineEdit_2.setText(str(QDate.currentDate().toString())) 
     
    def from_dt_onclick(self):
        self.calendarWidget.show()
        
    def to_dt_onclick(self):
        self.calendarWidget_2.show()
        
    def date_dd_click_from(self):        
        temp_var = self.calendarWidget.selectedDate() 
        var_name = temp_var.toPyDate()        
        self.from_date=str(var_name)        
        self.lineEdit.setText(str(self.calendarWidget.selectedDate().toString()))
        self.calendarWidget.hide()
        #self.lineEdit.show()
        
    def date_dd_click_to(self):        
        temp_var = self.calendarWidget_2.selectedDate() 
        var_name = temp_var.toPyDate()        
        self.to_date=str(var_name)        
        self.lineEdit_2.setText(str(self.calendarWidget_2.selectedDate().toString()))
        self.calendarWidget_2.hide()
        #self.lineEdit_2.show()     
    
    def cr_where_clause(self):
        if(self.checkBox_4.isChecked()):
                self.whr_str=" AND strftime('%Y-%m-%d',CREATED_ON)  between '"+str(self.from_date)+"' and '"+str(self.to_date)+"' "
        elif(self.checkBox.isChecked()) :
                self.whr_str=" AND strftime('%Y-%m-%d',CREATED_ON)  between '"+str(self.from_date)+"' and '"+str(self.to_date)+"' AND SERIAL_ID='"+str(self.lineEdit_3.text())+"' "
        
       
            
    def list_report_data(self):
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setHorizontalHeaderLabels(['Phone.No', 'SMS Status', 'Created On','Error','Serial Id' ,'SMS Message','SMS ID'])        
        self.whr_str=""
        connection = sqlite3.connect("services.db")        
        print ("from_date :"+str(self.from_date)+" to_date :"+str(self.to_date));
        self.cr_where_clause()
        print(" Where clause :"+self.whr_str)
        if(self.whr_str != ""):
            results=connection.execute("select PHONE_NO,STATUS,CREATED_ON,ERROR_MSG,SERIAL_ID,SMS_MSG,SMS_ID from SMS_HISTORY where SMS_TYPE='REPORT'  "+str(self.whr_str)+ " order by CREATED_ON desc")
        else:
            results=connection.execute("select PHONE_NO,STATUS,CREATED_ON,ERROR_MSG,SERIAL_ID,SMS_MSG,SMS_ID from SMS_HISTORY where SMS_TYPE='REPORT'  "+str(self.whr_str)+ " order by CREATED_ON desc")
            
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close() 
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_29_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
