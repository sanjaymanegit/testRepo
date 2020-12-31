# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_54_recovery.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3
from PyQt5.Qt import QTableWidgetItem


class fci_54_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 711))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(870, 30, 261, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(990, 100, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 150, 4);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_7.setGeometry(QtCore.QRect(590, 590, 711, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_44 = QtWidgets.QLabel(self.groupBox_7)
        self.label_44.setGeometry(QtCore.QRect(40, 20, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(300, 90, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); color:rgb(0, 0, 0);")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(650, 100, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 150, 4);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(820, 100, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 150, 4);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(10, 180, 1301, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(20, 620, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(209, 8, 45);\n"
"color: rgb(255, 255, 0);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(490, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(244, 244, 0);\n"
"background-color: rgb(170, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(590, 210, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 150, 4);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(20, 510, 421, 71))
        self.frame_5.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 85, 0);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(3)
        self.frame_5.setObjectName("frame_5")
        self.label_45 = QtWidgets.QLabel(self.frame_5)
        self.label_45.setGeometry(QtCore.QRect(30, 25, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_45.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(590, 270, 691, 291))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        #item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
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
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(30, 460, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 290, 421, 151))
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(3)
        self.listWidget.setObjectName("listWidget")
       
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(30, 210, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 150, 4);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(340, 620, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 150, 4);")
        self.pushButton_14.setObjectName("pushButton_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1396, 21))
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
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00 "))
        self.pushButton_9.setText(_translate("MainWindow", "RETURN"))
        self.groupBox_7.setTitle(_translate("MainWindow", " MESSAGE"))
        self.label_44.setText(_translate("MainWindow", "Invalid Password"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD :"))
        self.pushButton_10.setText(_translate("MainWindow", "SHOW"))
        self.pushButton_11.setText(_translate("MainWindow", "CLEAR"))
        self.pushButton_12.setText(_translate("MainWindow", "START RECOVERY"))
        self.label_9.setText(_translate("MainWindow", "RECOVERY"))
        self.pushButton_13.setText(_translate("MainWindow", "RECOVERY HISTORY"))
        self.label_45.setText(_translate("MainWindow", ""))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "RECOVERY DATE"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "USED FILE NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "OLD FILE NAME"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1212"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_11.setText(_translate("MainWindow", "FILE NAME"))
       
        self.pushButton_15.setText(_translate("MainWindow", "BROWSE FILES"))
        self.pushButton_14.setText(_translate("MainWindow", "REBOOT SYSTEM"))
        self.pushButton_9.clicked.connect(MainWindow.close)
        self.pushButton_11.clicked.connect(self.reset_loging)
        self.pushButton_10.clicked.connect(self.login_page)
        self.pushButton_15.clicked.connect(self.browse_file_onclick)
        self.listWidget.doubleClicked.connect(self.fetch_via_file_list)
        self.pushButton_12.clicked.connect(self.recover_data)
        self.pushButton_13.clicked.connect(self.list_report_data)
        self.pushButton_14.clicked.connect(self.reboot_system)
        self.list_report_data()
        
         #self.list_report_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        self.reset_loging()
        
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    
    
    def recover_data(self):
        date_str=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        source_file_name=str(self.label_45.text()).replace("\n","")
        old_file_name="fci_old_"+str(date_str)+".db"
        if(self.label_45.text() != ""):
             os.system("sudo cp fci.db "+str(old_file_name))
             os.system("sudo rm -rf fci.db")
             os.system("sudo umount /media/usb")
             time.sleep(1)
             os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")  
             print("sudo cp "+str(source_file_name)+" fci.db")
             os.system("sudo cp "+str(source_file_name)+" fci.db")
             os.system("sudo chmod 777 fci.db")
             print("INSERT INTO ZRECOVERY_HISTROY(USED_FILE_NAME,OLD_FILE_NAME) VALUES ('"+str(source_file_name)+"','"+str(old_file_name)+"')")
             connection = sqlite3.connect("services.db")          
             with connection:        
                        cursor = connection.cursor()                    
                        cursor.execute("INSERT INTO ZRECOVERY_HISTROY(USED_FILE_NAME,OLD_FILE_NAME) VALUES ('"+str(source_file_name)+"','"+str(old_file_name)+"')")                   
             connection.commit();
             connection.close()
             self.list_report_data()
             self.groupBox_7.show()
             self.label_44.show()
             self.label_44.setText("RECOERY SUCCESSFULLY DONE.")
             self.log_audit("RECOVERY"," DATA RECOVERED BY FILE :"+str(source_file_name))
             
        else:
             self.groupBox_7.show()
             self.label_44.show()
             self.label_44.setText("FILE NAME EMPTY.") 
    
    def browse_file_onclick(self):
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                try:
                    os.system("sudo rm -rf backupfiles_list.txt")  
                    os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")                    
                    os.system("sudo ls /media/usb/fci*.db >> backupfiles_list.txt")
                    os.system("sudo umount /media/usb")
                    try:
                       self.listWidget.clear() 
                       f = open('backupfiles_list.txt','r')
                       for line in f:
                               item= QtWidgets.QListWidgetItem(str(line))
                               item.setBackground(QtGui.QColor("black"))
                               self.listWidget.addItem(item)
                       f.close()
                       self.groupBox_7.show()       
                       self.label_44.show()
                       self.label_44.setText("BROWSE FILE DONE.")
                    except:
                       self.groupBox_7.show()
                       self.label_44.show()
                       self.label_44.setText("USB ERROR.") 
                   
                except:
                    self.groupBox_7.show()
                    self.label_44.show()
                    self.label_44.setText("OS ERROR.")
               
        else:
             #print("Please connect usb storage device")
             self.groupBox_7.show()       
             self.label_44.show()
             self.label_44.setText("PLEASE CONNECT USB DEVICE.")
        
        
    def fetch_via_file_list(self):
        v_str=str(self.listWidget.currentItem().text())
        #self.re_str = str(v_str)                
        self.label_45.setText(str(v_str)) 
    
    def get_usb_storage_id(self):
        os.system("rm -rf lsusb_data_db_bkp.txt")  
        product_id = "ERROR"
        os.system("lsusb >> lsusb_data_db_bkp.txt")
        try:
           f = open('lsusb_data_db_bkp.txt','r')
           for line in f:
               cnt=0                
               cnt=int(line.find("SanDisk"))
               if cnt > 0 :                   
                   product_id = line[28:33]
                   product_id = "0x"+str(product_id)
           f.close()
        except:
           product_id = "ERROR"
           self.label_44.show()
           self.label_44.setText("USB ERROR.")             
        return product_id   
        
    def reboot_system(self):
        os.system("sudo reboot")
        
    def login_page(self):        
        connection = sqlite3.connect("services.db")
        results=connection.execute("SELECT PWD,xxx FROM SERVICES_MST WHERE SERVICE_NAME = 'RECOVERY' AND STATUS = 'ACTIVE'") 
        for x in results:
            val=str(x[0])           
        connection.close()
        print("pwd:"+self.lineEdit.text()+" db val:"+str(val))
        if(str(self.lineEdit.text()) == str(val)):
                self.show_all()
                self.list_report_data()
                self.groupBox_7.hide()
        else:
                self.groupBox_7.show()
                self.label_44.show()
                self.label_44.setText("INCORRECT PASSWORD.")
                #self.reset_loging()
               
    
    def reset_loging(self):
        self.lineEdit.setText("")       
        self.tableWidget.hide()
        self.groupBox_7.hide()
        self.pushButton_12.hide()
        #self.label_9.hide()
        self.pushButton_13.hide()
        self.listWidget.hide()
        self.pushButton_15.hide()
        self.pushButton_14.hide()
        self.label_11.hide()
        self.frame_5.hide()
        self.listWidget.clear()
        self.label_45.setText("")  
    
    def show_all(self):           
        self.tableWidget.show()
        self.groupBox_7.show()
        self.pushButton_12.show()
        self.label_9.show()
        self.pushButton_13.show()
        self.listWidget.show()
        self.pushButton_15.show()
        self.pushButton_14.show()
        self.label_11.show()
        self.frame_5.show()
        
   

    def list_report_data(self):
        self.groupBox_7.hide()
        self.delete_all_records()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget.setHorizontalHeaderLabels(['RECOVERY DATE', 'USED FILE NAME', 'OLD FILE NAME'])               
        connection = sqlite3.connect("services.db")  
        results=connection.execute("select RECOVERY_DATE,USED_FILE_NAME, OLD_FILE_NAME  FROM ZRECOVERY_HISTROY order by RECOVERY_DATE desc ")            
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close() 
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)  

    def log_audit(self,event_name,desc_str):        
        connection = sqlite3.connect("fci.db")
        with connection:        
            cursor = connection.cursor()       
            cursor.execute("INSERT INTO AUDIT_MST(AUDIT_TYPE,MESSAGE) VALUES(?,?)",(event_name,desc_str))
            cursor.execute("UPDATE AUDIT_MST SET USER_ID = (SELECT LOGIN_USER_ID FROM GLOBAL_VAR) WHERE USER_ID IS NULL")            
        connection.commit();
        connection.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_54_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
