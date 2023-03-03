
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

import datetime
from PyQt5.Qt import QTableWidgetItem
import sqlite3

class users_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        #MainWindow.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 711))
        self.frame.setStyleSheet("background-color: rgb(215, 255, 252);")
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(1130, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(920, 610, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(1180, 610, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 631, 561))
        self.tableWidget.setStyleSheet("background-color: rgb(225, 255, 227);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 7, item)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(790, 610, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(670, 610, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(1050, 610, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(1000, 40, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(320, 30, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(690, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(790, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(690, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(790, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(1020, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(1130, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(690, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(790, 210, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(221, 255, 234) ; color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(690, 270, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(790, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(690, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(690, 390, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(790, 330, 151, 31))
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(790, 390, 151, 31))
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        #self.lineEdit_5.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(690, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(790, 460, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(690, 530, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(790, 530, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(1020, 260, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.login_user_id=""
        self.login_user_role=""
        self.login_user_name=""
        self.go_ahead="No"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "User Management"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00 "))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton_5.setText(_translate("MainWindow", "Return"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "EmailId"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Role"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Login Id"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Mobile No"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.pushButton_4.setText(_translate("MainWindow", "Add"))
        self.pushButton_6.setText(_translate("MainWindow", "Reset"))
        self.label_21.setText(_translate("MainWindow", "Login By : Sanjaykumar Mane(ADMIN)"))
        self.label_22.setText(_translate("MainWindow", "Successfully added user :Sanjaykuymar Mane"))
        self.label_2.setText(_translate("MainWindow", "User Id:"))
        self.label_23.setText(_translate("MainWindow", "00001"))
        self.label_3.setText(_translate("MainWindow", "First Name :"))
        self.label_4.setText(_translate("MainWindow", "Last Name :"))
        self.label_5.setText(_translate("MainWindow", "Role Name:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "OPERATOR"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SUPERVISOR"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ADMIN"))
        self.label_6.setText(_translate("MainWindow", "Login Id:"))
        self.label_7.setText(_translate("MainWindow", "Password:"))
        self.label_8.setText(_translate("MainWindow", "Confirm:"))
        self.label_9.setText(_translate("MainWindow", "Phone.No.:"))
        self.label_10.setText(_translate("MainWindow", "Email Id:"))
        self.label_11.setText(_translate("MainWindow", "User Id: xxxx Already Exist."))
        self.label_11.hide()
        self.lineEdit.setText("lineEdit")
        self.lineEdit_2.setText("lineEdit_2")
        self.lineEdit_3.setText("lineEdit_3")
        self.lineEdit_4.setText("lineEdit_4")
        self.lineEdit_5.setText("lineEdit_5")
        self.lineEdit_6.setText("lineEdit_6")
        self.lineEdit_7.setText("lineEdit_7")
        
        
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.load_login_dtls()
        self.s_rest_fun()
        
        #self.s_select_all_data()        
        self.tableWidget.doubleClicked.connect(self.s_fetch_data_from_tw)
        self.pushButton_4.clicked.connect(self.s_add_click) 
        self.pushButton_3.clicked.connect(self.s_edit_click)       
        self.pushButton_2.clicked.connect(self.s_delete_click)
        self.pushButton_6.clicked.connect(self.s_rest_fun)
        
        
        self.label_21.setText("Login By : "+str(self.login_user_name))
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
    
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))


    def load_login_dtls(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select login_user_id,login_user_role,login_user_name from global_var")       
        for x in results:           
                 self.login_user_id=str(x[0])
                 self.login_user_role=str(x[1])
                 self.login_user_name=str(x[2])
        connection.close()       



            
    def s_fetch_data_from_tw(self):        
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.dr_id=str(self.tableWidget.item(row, 0).text())
            self.label_23.setText(str(self.tableWidget.item(row, 0).text()).zfill(4)) 
            self.lineEdit.setText(str(self.tableWidget.item(row, 1).text())) 
            self.lineEdit_2.setText(str(self.tableWidget.item(row, 2).text()))
            self.comboBox.setCurrentText(str(self.tableWidget.item(row, 3).text()))
            self.lineEdit_3.setText(str(self.tableWidget.item(row, 4).text()))
            self.lineEdit_4.setText(str(self.tableWidget.item(row, 7).text())) 
            self.lineEdit_5.setText(str(self.tableWidget.item(row, 7).text()))
            self.lineEdit_6.setText(str(self.tableWidget.item(row, 5).text()))
            self.lineEdit_7.setText(str(self.tableWidget.item(row, 6).text()))
            if(str(self.login_user_role) ==  'OPERATOR'):
                    self.pushButton_4.setDisabled(True)
                    self.comboBox.setDisabled(True)
                    self.pushButton_2.setDisabled(True) #delete           
                    self.pushButton_6.setDisabled(True) #reset
                    self.pushButton_3.setEnabled(True)  #save
            else:
                    self.pushButton_4.setDisabled(True) #add
                    self.pushButton_3.setEnabled(True)  #save
                    self.pushButton_2.setEnabled(True) #delete           
                    self.pushButton_6.setEnabled(True) #reset
            
        else:    
            self.label_22.setText("Please Select the record.")
            self.label_22.show()
            
            
    def s_rest_fun(self):
        self.lineEdit.setText("")  
        self.lineEdit_2.setText("") 
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")  
        self.lineEdit_5.setText("") 
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.pushButton_4.setEnabled(True) #add
        self.pushButton_3.setDisabled(True)  #save
        self.pushButton_2.setDisabled(True) #delete           
        self.pushButton_6.setEnabled(True) #reset
        self.label_22.hide()
        self.s_select_all_data()        
  
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select seq+1 from sqlite_sequence WHERE name = 'USERS_MST'")       
        for x in results:           
                 self.label_23.setText(str(x[0]).zfill(6))            
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
        if(self.label_23.text() != ""):
            self.validate_ip()
            if(str(self.go_ahead )== 'Yes'):
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("INSERT INTO USERS_MST(FIRST_NAME,LAST_NAME,ROLE,LOGIN_ID,PWD,PHONE_NO,EMAIL_ID) VALUES('"+self.lineEdit.text()+"','"+self.lineEdit_2.text()+"','"+self.comboBox.currentText()+"','"+self.lineEdit_3.text()+"','"+self.lineEdit_4.text()+"','"+self.lineEdit_6.text()+"','"+self.lineEdit_7.text()+"')")                    
                    connection.commit();                    
                    connection.close()  
              
                    self.label_22.setText("Record Added Successfully.")
                    #self.log_audit("Users Management","Added New User: " +str(self.label_23.text()))
                    self.label_22.show()
        else :
            self.label_22.setText("Id is Empty.")
            self.label_22.show()
            
        self.s_select_all_data()
    
    def s_edit_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="EDIT"
            self.s_load_data()
        else:    
            self.label_22.setText("Please Select the record.")
            self.label_22.show() 
    
    def s_edit_data(self):
        if(self.label_23.text() != ""):
            self.validate_ip()
            if(str(self.go_ahead )== 'Yes'):
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("UPDATE USERS_MST SET FIRST_NAME='"+self.lineEdit.text()+"',LAST_NAME='"+self.lineEdit_2.text()+"',ROLE='"+self.comboBox.currentText()+"',LOGIN_ID='"+self.lineEdit_3.text()+"',PWD='"+self.lineEdit_4.text()+"',PHONE_NO='"+self.lineEdit_6.text()+"',EMAIL_ID='"+self.lineEdit_7.text()+"' WHERE  USER_ID ='"+str(self.dr_id)+"'")                    
                    connection.commit();                    
                    connection.close()
                    self.label_22.setText("Record Saved Successfully.")
                    #self.log_audit("Users Management","Updated User: " +str(self.label_23.text()))
                    self.label_22.show()
                    self.s_select_all_data()
           
                   
    
    def s_delete_click(self):
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.operation_flg="DELETE"
            self.s_load_data()
        else:    
            self.label_22.setText("Please Select the record.")
            self.label_22.show()        
     
      
    def s_delete_data(self):
        if(self.label_23.text() != ""):
            close = QMessageBox()
            close.setText("Confirm Deleteing User ID : "+str(self.dr_id))
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Yes:
                    connection = sqlite3.connect("tyr.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM USERS_MST WHERE USER_ID ='"+str(self.dr_id)+"'")                    
                    connection.commit();                    
                    connection.close()
                    
                    self.label_22.setText("Record Deleted Successfully.")
                    #self.log_audit("Users Management","Deleted User: " +str(self.label_23.text()))
                    self.label_22.show()
                    
                    self.s_select_all_data()
            else:
                   self.label_22.setText("Delete Cancled !!!.")
                    #self.log_audit("Users Management","Deleted User: " +str(self.label_23.text()))
                   self.label_22.show()
            
         
    def s_select_all_data(self):     
        self.s_delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font) 
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
      
        self.tableWidget.setHorizontalHeaderLabels(['User Id.', ' First Name ', 'Last Name','Role','LoginId','Phone','Email Id','Password'])
        print("role :"+str(self.login_user_role))
       
        connection = sqlite3.connect("tyr.db")
        if(str(self.login_user_role) ==  'SUPER_ADMIN'):
                results=connection.execute("select USER_ID,FIRST_NAME,LAST_NAME,ROLE,LOGIN_ID,PHONE_NO,EMAIL_ID,PWD from USERS_MST where ROLE != 'SUPER_ADMIN'")
                self.comboBox.setEnabled(True)
                self.pushButton_2.setDisabled(True) #delete           
                self.pushButton_6.setEnabled(True) #reset
                #self.pushButton_4.setEnabled(True) #add
        elif(str(self.login_user_role) ==  'ADMIN'):
                self.comboBox.clear()
                self.comboBox.addItem("")
                self.comboBox.setItemText(0, "OPERATOR")
                self.comboBox.addItem("")
                self.comboBox.setItemText(1, "SUPERVISOR")                
            
                results=connection.execute("select USER_ID,FIRST_NAME,LAST_NAME,ROLE,LOGIN_ID,PHONE_NO,EMAIL_ID,PWD from USERS_MST WHERE USER_ID IN (SELECT USER_ID FROM ADMINS_USER_IDS_VW)")
        elif(str(self.login_user_role) ==  'SUPERVISOR'):
                self.comboBox.clear()
                self.comboBox.addItem("")
                self.comboBox.setItemText(0, "OPERATOR")
               
                
                
                results=connection.execute("select USER_ID,FIRST_NAME,LAST_NAME,ROLE,LOGIN_ID,PHONE_NO,EMAIL_ID,PWD from USERS_MST WHERE USER_ID IN (SELECT USER_ID FROM SUPERVISORS_USER_IDS_VW)")
        else:
                results=connection.execute("select USER_ID,FIRST_NAME,LAST_NAME,ROLE,LOGIN_ID,PHONE_NO,EMAIL_ID,PWD from USERS_MST WHERE USER_ID='"+str(self.login_user_id)+"'")
                self.comboBox.setDisabled(True)
                self.pushButton_2.setDisabled(True) #delete           
                self.pushButton_6.setDisabled(True) #reset
                self.pushButton_4.setDisabled(True) #add
        
        
        
        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))                
        connection.close()   
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
    
    def s_delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
            
     
    def validate_ip(self):
        self.go_ahead="No"
        if(self.lineEdit.text() == ""):
             self.label_22.setText("First Name is Empty.")
             self.label_22.show()  
        elif(self.lineEdit_3.text()== ""):
             self.label_22.setText("Login Id is Empty.")
             self.label_22.show() 
        elif(self.lineEdit_4.text()== ""):
             self.label_22.setText("Password is Empty.")
             self.label_22.show()
        elif(self.lineEdit_5.text()== ""):
             self.label_22.setText("Confirm Password is Empty.")
             self.label_22.show()
        elif(str(self.lineEdit_5.text()) != str(self.lineEdit_4.text())):
             self.label_22.setText("Both Passwords are not same.")
             self.label_22.show() 
        else:
             self.go_ahead="Yes"
    
#    def log_audit(self,event_name,desc_str):        
#        connection = sqlite3.connect("tyr.db")
#        with connection:        
#            cursor = connection.cursor()       
#            cursor.execute("INSERT INTO AUDIT_MST(AUDIT_TYPE,MESSAGE) VALUES(?,?)",(event_name,desc_str))
#            cursor.execute("UPDATE AUDIT_MST SET USER_ID = (SELECT LOGIN_USER_ID FROM GLOBAL_VAR) WHERE USER_ID IS NULL")
#            
#        connection.commit();
#        connection.close()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = users_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
