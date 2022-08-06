# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'specimen_bakup_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
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

class specimen_bkp_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 651, 451))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(450, 30, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(390, 110, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 220, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 280, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 80, 601, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(390, 340, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(50, 121, 291, 301))
        self.listWidget.setStyleSheet("background-color: rgb(230, 255, 242);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(390, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 21))
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
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44:00"))
        self.label_2.setText(_translate("MainWindow", "Backup Done Successfully."))
        self.label_2.hide()
        self.pushButton_6.setText(_translate("MainWindow", "BACKUP"))
        self.pushButton_7.setText(_translate("MainWindow", "RECOVERY"))
        self.pushButton_8.setText(_translate("MainWindow", "CLOSE"))
        self.label_4.setText(_translate("MainWindow", "Sepcimen Backup/Recovery"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)        
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_9.setText(_translate("MainWindow", "REFRESH "))
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.pushButton_9.clicked.connect(self.browse_file_onclick)
        self.browse_file_onclick()
    
    
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
           self.label_2.show()
           self.label_2.setText("USB ERROR.")             
        return product_id
    
    def browse_file_onclick(self):
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                try:
                    os.system("sudo rm -rf backupfiles_list.txt")  
                    os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")                    
                    os.system("sudo ls /media/usb/*.pdf >> backupfiles_list.txt")
                    os.system("sudo umount /media/usb")
                    try:
                       self.listWidget.clear() 
                       f = open('backupfiles_list.txt','r')
                       for line in f:
                               item= QtWidgets.QListWidgetItem(str(line))
                               #item.setBackground(QtGui.QColor("black"))
                               self.listWidget.addItem(item)
                       f.close()                           
                       self.label_2.hide()
                    except:                       
                       self.label_2.show()
                       self.label_2.setText("USB ERROR.") 
                   
                except:                    
                    self.label_2.show()
                    self.label_2.setText("OS ERROR.")
        else:
            self.label_2.show()
            self.label_2.setText("USB ERROR.")
            
    
    def backup_process(self):
        self.label_2.setText("STARTED BACKUP")
        self.label_2.show()
        time.sleep(1)
        self.bkp_f()
        
       
    def bkp_f(self):        
        #print("inside backup ")
        date_str=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                try:
                    os.system("cp fci.db fci_bkp"+str(date_str)+".db")
                    os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                    os.system("mv fci_bkp"+str(date_str)+".db /media/usb")
                    os.system("sudo umount /media/usb")
                    connection = sqlite3.connect("services.db")          
                    with connection:        
                        cursor = connection.cursor()                    
                        cursor.execute("INSERT INTO ZBACKUP_HIST(BACKUP_TYPE,FILE_NAME,PATH,STATUS,BACKUP_ON) VALUES ('Manual','fci_bkp"+str(date_str)+".db','/media/usb','Completed',CURRENT_TIMESTAMP)")                    
                    connection.commit();
                    connection.close()
                    self.list_report_data()
                    self.groupBox_7.show()       
                    self.label_44.show()
                    self.label_44.setText("BACKUP COMPLETED.")
                    self.log_audit("BACKUP"," BACKUP FILE CREATED AS :"+str(date_str)+".db")
                   
                   
                #self.label_9.setText("fci_bkp"+str(date_str)+".db")
                #self.label_44.show()
                #self.label_44.setText("wt_bkp"+str(date_str)+".db")
                except:
                    self.label_44.show()
                    self.label_44.setText("OS ERROR.")
               
        else:
             #print("Please connect usb storage device")
             self.groupBox_7.show()       
             self.label_44.show()
             self.label_44.setText("PLEASE CONNECT USB DEVICE.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = specimen_bkp_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())