from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class urmini_14_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 20, 961, 561))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(750, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(790, 470, 120, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(390, 30, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(480, 120, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 190, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(230, 470, 120, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"")
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(420, 470, 120, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"")
        self.pushButton_10.setAutoDefault(True)
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(60, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 120, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(650, 120, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(500, 200, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(651, 200, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(610, 470, 120, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"")
        self.pushButton_11.setAutoDefault(True)
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(50, 470, 120, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"")
        self.pushButton_12.setAutoDefault(True)
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(60, 280, 851, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(370, 200, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
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
        self.pushButton_8.setText(_translate("MainWindow", "Return"))
        self.label_2.setText(_translate("MainWindow", "Patient Details "))
        self.label_3.setText(_translate("MainWindow", "Patient Name:"))
        self.label_6.setText(_translate("MainWindow", "Age :"))
        self.pushButton_9.setText(_translate("MainWindow", "Add"))
        self.pushButton_10.setText(_translate("MainWindow", "Save"))
        self.label_7.setText(_translate("MainWindow", "Saved Successfully."))
        self.radioButton.setText(_translate("MainWindow", "Male"))
        self.radioButton_2.setText(_translate("MainWindow", "Female"))
        self.pushButton_11.setText(_translate("MainWindow", "Delete"))
        self.pushButton_11.hide()
        self.pushButton_12.setText(_translate("MainWindow", "Refresh"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Age"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ID"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "( Yrs)"))
        
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.label_7.hide()
        self.tableWidget.doubleClicked.connect(self.fetch_data_from_tw)
        self.pushButton_12.clicked.connect(self.refresh_fun)
        self.select_all_data()
        
       
        self.pushButton_10.clicked.connect(self.edit_click)
        
        self.pushButton_12.clicked.connect(self.refresh_fun)
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)

    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    
    
    
    
   
        
    def refresh_fun(self):       
        self.lineEdit.setText("")        
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        
        
        self.select_all_data()
        self.label_7.hide()
        
    def fetch_data_from_tw(self):
        #self.lineEdit_2.setText("ok fname")
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            xx=str(self.tableWidget.item(row, 0).text()).split()
            
            self.dr_id=str(self.tableWidget.item(row, 3).text())
            #self.gender_toedit=(self.tableWidget.item(row, 3).text())
            self.lineEdit_4.setText(str(xx[0]))
            self.lineEdit.setText(str(xx[1]))
            self.lineEdit_5.setText(str(xx[2]))           
            self.lineEdit_3.setText(str(self.tableWidget.item(row, 2).text()))
            if(str(self.tableWidget.item(row, 1).text())== 'Male'):
                    self.radioButton.setChecked(True)                    
            else: 
                    self.radioButton_2.setChecked(True)
            
            #self.label_9.setText(str(self.tableWidget.item(row, 3).text()))
           
            self.pushButton_10.setEnabled(True)#save
            
            
        else:    
            self.label_7.setText("Please Select the record.")
            self.label_7.show()
    def select_all_data(self):     
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnWidth(0, 500)
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT F_NAME||' '||M_NAME||' '||L_NAME,GENDER,AGE,P_ID FROM PATIENT_MST order by P_ID DESC ")                        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                #self.lineEdit.setText("")
        
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)
        #self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        #self.pushButton_9.setEnabled(True) #add 
        self.pushButton_10.setDisabled(True)#save
        #self.pushButton_11.setDisabled(True) #del
        #self.label_7.hide()
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
                    cursor.execute("INSERT INTO PATIENT_MST(fname,mname,lname,DR_QUAL,DR_EMAIL_ID,DR_CONTACT,DR_GENDER) values ('"+self.lineEdit_4.text()+"','"+self.lineEdit.text()+"','"+self.lineEdit_5.text()+"','"+self.lineEdit_2.text()+"','"+self.lineEdit_3.text()+"','"+self.lineEdit_6.text()+"','"+self.gender+"')")                    
            connection.commit();                    
            connection.close()   
      
        self.label_7.setText("Added Successfully.")
        self.label_7.show()
        self.select_all_data()
    
    def edit_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="EDIT"
            self.load_data()
        else:    
            self.label_7.setText("Please Select the record.")
            self.label_7.show() 
    
    def edit_data(self):
        if(self.lineEdit_4.text() != ""):
            if(self.lineEdit.text() != ""):
                if(self.lineEdit_5.text() != ""):
                    if(self.radioButton.isChecked()):
                                self.gender="Male"
                    else:           
                                self.gender="Female"
                    connection = sqlite3.connect("ur.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("UPDATE PATIENT_MST SET f_name='"+self.lineEdit_4.text()+"',m_name='"+self.lineEdit.text()+
                                           "',l_name='"+self.lineEdit_5.text()+"', GENDER='"+self.gender+"',AGE='"+self.lineEdit_3.text()+"' WHERE  P_ID ='"+str(self.dr_id)+"'")                    
                    connection.commit();                    
                    connection.close()
                    self.label_7.setText("Saved Successfully.")
                    self.label_7.show()
                    self.select_all_data()
                else:
                    self.label_7.setText("Last Name Empty.")
                    self.label_7.show() 
            else:
                self.label_7.setText("Middle Name Empty.")
                self.label_7.show()         
        else:
            self.label_7.setText("First Name Empty.")
            self.label_7.show()
       
        
    
    def delete_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="DELETE"
            self.load_data()
        else:    
            self.label_7.setText("Please Select the record.")
            self.label_7.show()        
     
      
    def delete_data(self):
        if(self.lineEdit_2.text() != ""):
            connection = sqlite3.connect("ur.db")
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("DELETE FROM DOCTORS_INFO WHERE DR_ID ='"+str(self.dr_id)+"'")                    
            connection.commit();                    
            connection.close()   
        
        self.label_7.setText("Deleted Successfully.")
        self.label_7.show()
        self.select_all_data()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = urmini_14_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
