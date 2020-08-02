# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt_03_setting.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pop_datetime import DATE_Ui_MainWindow
from pop_party import POP_PARTY_Ui_MainWindow
from pop_supplier import POP_SUPP_Ui_MainWindow
from pop_transport import POP_TRANS_Ui_MainWindow
import sqlite3
import os

class wt_03_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1321, 701))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 451, 181))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(150, 40, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 40, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 40, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 40, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 111, 81))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(530, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 90, 411, 111))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 40, 131, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 40, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(980, 30, 301, 171))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 60, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setObjectName("checkBox_2")
        
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        
        
        self.groupBox_3_1 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3_1.setGeometry(QtCore.QRect(980, 230, 301, 171))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_3_1.setFont(font)
        self.groupBox_3_1.setObjectName("groupBox_3_1")
        
        self.pushButton_5_1 = QtWidgets.QPushButton(self.groupBox_3_1)
        self.pushButton_5_1.setGeometry(QtCore.QRect(100, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5_1.setFont(font)
        self.pushButton_5_1.setObjectName("pushButton_5_1")
        
                
        
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 230, 211, 231))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 50, 111, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 110, 111, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 170, 111, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setGeometry(QtCore.QRect(270, 230, 191, 141))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setGeometry(QtCore.QRect(30, 40, 82, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 90, 111, 31))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_6.setGeometry(QtCore.QRect(270, 390, 191, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
       
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 620, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_6_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6_1.setGeometry(QtCore.QRect(680, 620, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6_1.setFont(font)
        self.pushButton_6_1.setObjectName("pushButton_6_1")
        
        
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_7.setGeometry(QtCore.QRect(520, 230, 451, 351))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.widget = QtWidgets.QWidget(self.groupBox_7)
        self.widget.setGeometry(QtCore.QRect(30, 50, 379, 272))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

      
        
        
        
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Rates"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Detete"))
        self.pushButton_3.setText(_translate("MainWindow", "Reset"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "50"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "100"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "150"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "200"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.checkBox.setText(_translate("MainWindow", "Delete Slip Right"))
        self.groupBox_2.setTitle(_translate("MainWindow", "System setup"))
        self.label.setText(_translate("MainWindow", "Password:"))
        self.pushButton_4.setText(_translate("MainWindow", "Login System"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Factory Reset"))
        self.groupBox_3_1.setTitle(_translate("MainWindow", "DateTime Setting"))
        self.checkBox_2.setText(_translate("MainWindow", "Clean All Data"))
        self.pushButton_5.setText(_translate("MainWindow", "Clean"))
        self.pushButton_5_1.setText(_translate("MainWindow", "Set DateTime "))
        self.groupBox_4.setTitle(_translate("MainWindow", "Master Data Modifications"))
        self.pushButton_7.setText(_translate("MainWindow", "Party Data"))
        self.pushButton_8.setText(_translate("MainWindow", "Supplier Data"))
        self.pushButton_9.setText(_translate("MainWindow", "Transport Data"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Camera Options"))
        self.radioButton.setText(_translate("MainWindow", "DVR"))
        self.radioButton_2.setText(_translate("MainWindow", "IP Camera"))
        self.groupBox_6.setTitle(_translate("MainWindow", "SMS"))
        self.checkBox_3.setText(_translate("MainWindow", "Activated"))
        self.pushButton_6.setText(_translate("MainWindow", "Retrun"))
        self.pushButton_6_1.setText(_translate("MainWindow", "Save"))
        
        
        self.groupBox_7.setTitle(_translate("MainWindow", "Device Setting"))        
        self.label_2.setText(_translate("MainWindow", "Device ID:"))
        self.label_3.setText(_translate("MainWindow", "201910:0003"))
        self.label_4.setText(_translate("MainWindow", "Company Name:"))
        self.label_5.setText(_translate("MainWindow", "Company Address:"))
        self.label_6.setText(_translate("MainWindow", "Contact No:"))


        
        
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.rates_list_load()
        self.pushButton.clicked.connect(self.add_rate)
        self.pushButton_2.clicked.connect(self.delete_rate)
        self.pushButton_3.clicked.connect(self.reset_fun)
        self.listWidget.doubleClicked.connect(self.selected_rate)
        self.pushButton_4.clicked.connect(self.login_system)
        self.pushButton_5.clicked.connect(self.clean_data)
        self.pushButton_5_1.clicked.connect(self.pop_date_setting)
        self.checkBox.clicked.connect(self.set_delete_access)
        self.pushButton_6_1.clicked.connect(self.save_company_dtls)
        self.pushButton_7.clicked.connect(self.pop_party_window)
        self.pushButton_8.clicked.connect(self.pop_supp_window)
        self.pushButton_9.clicked.connect(self.pop_trans_window)  
        self.load_data()
     
     
    def clean_data(self):
        if(self.checkBox_2.isChecked()):
            print("ok clean data now")
            connection = sqlite3.connect("wt.db")
            with connection:        
                    cursor = connection.cursor()       
                    cursor.execute("DELETE FROM WEIGHT_MST")
            connection.commit();
            connection.close()
     
    def pop_party_window(self):         
        self.window = QtWidgets.QMainWindow()
        self.ui=POP_PARTY_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
    def pop_supp_window(self):         
        self.window = QtWidgets.QMainWindow()
        self.ui=POP_SUPP_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()     
    
    def pop_trans_window(self):         
        self.window = QtWidgets.QMainWindow()
        self.ui=POP_TRANS_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()      
        
    def save_company_dtls(self):
        connection = sqlite3.connect("wt.db")
        with connection:        
                cursor = connection.cursor()       
                cursor.execute("UPDATE SETTING_MST SET COMPANY_NAME='"+str(self.lineEdit_3.text())+"', ADDRESS='"+self.textEdit.toPlainText()+"', CONTACT_NO='"+str(self.lineEdit_4.text())+"'")
        connection.commit();
        connection.close()
        
    def load_data(self):
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT  DELETE_ACESS,COMPANY_NAME,ADDRESS,CONTACT_NO FROM SETTING_MST")       
        for x in results:        
              if(str(x[0]) == "ACTIVE"):
                   self.checkBox.setChecked(True)
              elif(str(x[0]) == "INACTIVE"):
                    self.checkBox.setChecked(False)
              self.lineEdit_3.setText(str(x[1]))
              self.textEdit.setText(str(x[2])) 
              self.lineEdit_4.setText(str(x[3])) 
             
                  
        connection.close()
        #self.groupBox_3.setDisabled(True)
        #self.groupBox_4.setDisabled(True)
        self.groupBox_5.setDisabled(True)
        self.groupBox_6.setDisabled(True)
    
    def set_delete_access(self):
        if(self.checkBox.isChecked()):
            print("Make Activate")
            connection = sqlite3.connect("wt.db")
            with connection:        
                cursor = connection.cursor()       
                cursor.execute("UPDATE SETTING_MST SET DELETE_ACESS='ACTIVE'")
            connection.commit();
            connection.close()
            
        else:
            connection = sqlite3.connect("wt.db")
            with connection:        
                cursor = connection.cursor()       
                cursor.execute("UPDATE SETTING_MST SET DELETE_ACESS='INACTIVE'")
            connection.commit();
            connection.close()
            print("Make Inactive")
            
    
    def login_system(self):
        if(self.lineEdit_2.text()=="break360"):
            os.sysddtem("Beak")
        else:
            print(" invalid password")
        
    
    
    def reset_fun(self):
        self.lineEdit.setText("")
    
    
    def selected_rate(self):
        self.list_type=self.listWidget.item(0).text()
        if(self.listWidget.currentItem().text() != self.listWidget.item(0).text()):
            if(self.list_type=="====Rates ====="):
                self.lineEdit.setText(self.listWidget.currentItem().text())                 
            else:             
                self.lineEdit.setText("Invalid")
    
    
    def add_rate(self):
        self.rate_rs = str(self.lineEdit.text())
        self.cnt_rate_rs=0
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT count(RATE_RS) FROM RATES_MST WHERE RATE_RS = '"+str(self.rate_rs)+"'")       
        for x in results:        
              self.cnt_rate_rs=int(x[0])
        connection.close()
        if(self.rate_rs  != "" and self.cnt_rate_rs ==0):
            connection = sqlite3.connect("wt.db")
            with connection:        
                    cursor = connection.cursor()       
                    cursor.execute("INSERT INTO RATES_MST(RATE_RS) VALUES('"+str(self.rate_rs)+"')")
            connection.commit();
            connection.close()
        self.rates_list_load()
        self.lineEdit.setText("")
        
    def rates_list_load(self):
        self.listWidget.clear()
        self.listWidget.addItem("====Rates =====")
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT DISTINCT RATE_RS FROM RATES_MST")       
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()
        
    def delete_rate(self):
        if(self.lineEdit.text() != ""):
            connection = sqlite3.connect("wt.db")
            with connection:        
                    cursor = connection.cursor()       
                    cursor.execute("DELETE FROM RATES_MST WHERE RATE_RS='"+str(int(self.lineEdit.text()))+"'")
            connection.commit();
            connection.close()
            self.rates_list_load() 
            self.lineEdit.setText("")
    
    def pop_date_setting(self):       
        self.window = QtWidgets.QMainWindow()
        self.ui=DATE_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = wt_03_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
