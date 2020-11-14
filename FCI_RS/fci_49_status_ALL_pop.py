# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_30_batch_pop.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem
import datetime
import sqlite3


class fci_49_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 384)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        #MainWindow.setStyleSheet("background-color: rgb(135, 206, 235);")
        MainWindow.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 911, 321))
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(570, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 20, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 861, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(13, item)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.from_dt=""
        self.to_dt=""
        self.status=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_9.setText(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", "OTHER (PENDING)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Slip No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vehicle. No"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Material"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Slot.No."))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "No.Of.Bags"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Net.Wt.Ton"))
        connection = sqlite3.connect("fci.db")
        results=connection.execute("SELECT STATUS,STATUS_FROM,STATUS_TO FROM GLOBAL_VAR") 
        for x in results:            
            self.label.setText("ALL - "+str(x[0]))
            self.status=str(x[0])
            self.from_dt=str(x[1])
            self.to_dt=str(x[2])
        connection.close()
        
        self.pushButton_9.clicked.connect(MainWindow.close)
        self.select_all_data()
        
        
    def select_all_data(self):     
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 150)
        self.tableWidget.setColumnWidth(7, 150)
        self.tableWidget.setColumnWidth(8, 150)
        self.tableWidget.setColumnWidth(9, 150)
        self.tableWidget.setColumnWidth(10, 150)
        self.tableWidget.setColumnWidth(11, 150)
        self.tableWidget.setColumnWidth(12, 150)
        self.tableWidget.setColumnWidth(13, 150)
       
         
        self.tableWidget.setHorizontalHeaderLabels(['Slip No.','Weighing Type','Vehicle No.','First Weight Type','First Weight','First Weight On','Second Weight Type','Second Weight','Second Weight On','Material','Net.Wt','Recipt Id','Issue Id','Party Name'])        
        
         
        connection = sqlite3.connect("fci.db")
        if(self.status == "PENDING"):
                results=connection.execute("select SERIAL_ID,CASE WHEN BATCH_ISSUE_FLG='BATCH' THEN 'RECIPT' ELSE BATCH_ISSUE_FLG END AS FLG  ,VEHICLE_NO,FIRST_WEIGHT_MODE,printf(\"%6d\", IFNULL(FIRST_WEIGHT_VAL,0)) ,FIRST_WT_CRTEATED_ON,SECOND_WT_MODE,printf(\"%6d\", IFNULL(SECOND_WT_VAL,0)) ,SECOND_WT_CREATED_ON,MATERIAL_NAME,printf(\"%6d\", IFNULL(NET_WEIGHT_VAL,0)),BATCH_ID,ISSUE_ID,PARTY_NAME FROM WEIGHT_MST WHERE  STATUS='FIRST' and FIRST_WT_CRTEATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"'")                        
        else:
                results=connection.execute("select SERIAL_ID,CASE WHEN BATCH_ISSUE_FLG='BATCH' THEN 'RECIPT' ELSE BATCH_ISSUE_FLG END AS FLG,VEHICLE_NO,FIRST_WEIGHT_MODE,printf(\"%6d\", IFNULL(FIRST_WEIGHT_VAL,0)) ,FIRST_WT_CRTEATED_ON,SECOND_WT_MODE,printf(\"%6d\", IFNULL(SECOND_WT_VAL,0)) ,SECOND_WT_CREATED_ON,MATERIAL_NAME,printf(\"%6d\", IFNULL(NET_WEIGHT_VAL,0)),BATCH_ID,ISSUE_ID,PARTY_NAME FROM WEIGHT_MST WHERE  STATUS='SECOND' and FIRST_WT_CRTEATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"'")                        
        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                #self.lineEdit.setText("")
        connection.close()   
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
        
        
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_49_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
