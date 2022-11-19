
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3
from PyQt5.Qt import QTableWidgetItem


class usb_bkp_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(849, 525)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 801, 461))
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
        self.label.setGeometry(QtCore.QRect(590, 30, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(290, 140, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 210, 261, 41))
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
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 80, 741, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(340, 30, 121, 31))
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
        self.label_4.setGeometry(QtCore.QRect(40, 30, 181, 41))
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
        self.listWidget.setGeometry(QtCore.QRect(50, 151, 191, 271))
        self.listWidget.setStyleSheet("background-color: rgb(230, 255, 242);")
        self.listWidget.setObjectName("listWidget")
#        item = QtWidgets.QListWidgetItem()
#        font = QtGui.QFont()
#        font.setFamily("Arial")
#        font.setPointSize(12)
#        font.setBold(True)
#        font.setWeight(75)
#        item.setFont(font)
#        self.listWidget.addItem(item)
#        item = QtWidgets.QListWidgetItem()
#        font = QtGui.QFont()
#        font.setFamily("Arial")
#        font.setPointSize(12)
#        font.setBold(True)
#        font.setWeight(75)
#        item.setFont(font)
#        self.listWidget.addItem(item)
#        item = QtWidgets.QListWidgetItem()
#        font = QtGui.QFont()
#        font.setFamily("Arial")
#        font.setPointSize(12)
#        font.setBold(True)
#        font.setWeight(75)
#        item.setFont(font)
#        self.listWidget.addItem(item)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 100, 191, 31))
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
        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setGeometry(QtCore.QRect(560, 150, 191, 281))
        self.listWidget_2.setStyleSheet("background-color: rgb(230, 255, 242);")
        self.listWidget_2.setObjectName("listWidget_2")
        
#        item = QtWidgets.QListWidgetItem()
#        font = QtGui.QFont()
#        font.setFamily("Arial")
#        font.setPointSize(12)
#        font.setBold(True)
#        font.setWeight(75)
#        item.setFont(font)
#        self.listWidget_2.addItem(item)
#        item = QtWidgets.QListWidgetItem()
#        font = QtGui.QFont()
#        font.setFamily("Arial")
#        font.setPointSize(12)
#        font.setBold(True)
#        font.setWeight(75)
#        item.setFont(font)
#        self.listWidget_2.addItem(item)
#        item = QtWidgets.QListWidgetItem()
#        font = QtGui.QFont()
#        font.setFamily("Arial")
#        font.setPointSize(12)
#        font.setBold(True)
#        font.setWeight(75)
#        item.setFont(font)
#        self.listWidget_2.addItem(item)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(560, 100, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_10.setAutoDefault(True)
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(270, 310, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_14.setAutoDefault(True)
        self.pushButton_14.setDefault(True)
        self.pushButton_14.setFlat(False)
        self.pushButton_14.setObjectName("pushButton_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 21))
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
        self.label_2.setText(_translate("MainWindow", ""))
        self.pushButton_6.setText(_translate("MainWindow", "MOVE TO USB"))
        self.pushButton_8.setText(_translate("MainWindow", "CLOSE"))
        self.label_4.setText(_translate("MainWindow", "Copy to USB"))
        self.pushButton_9.setText(_translate("MainWindow", "REFRESH DIR"))
        self.pushButton_10.setText(_translate("MainWindow", "REFRESH USB"))
        self.pushButton_14.setText(_translate("MainWindow", "MOVE ALL TO USB"))
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.pushButton_10.clicked.connect(self.browse_file_onclick)
        self.pushButton_9.clicked.connect(self.load_reports_files)
        self.pushButton_6.clicked.connect(self.move_to_usb)
        self.pushButton_14.clicked.connect(self.move_all)
        
        self.load_reports_files()
        #self.list_report_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
       
        
        
    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
     
     
    def move_to_usb(self):
        i=self.listWidget.currentRow()
        print("Count :"+str(i))
        if( int(i) > -1):
            file_name=str(self.listWidget.currentItem().text())
            product_id=self.get_usb_storage_id()
            if(product_id != "ERROR"):
                            if(file_name==""):
                                self.label_2.show()
                                self.label_2.setText("Select File Please.")
                            else:
                                file_name=file_name.replace("\n","")
                                os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")                   
                               
                                os.system("sudo cd  /home/pi/Products/TYR/reports")
                                print("sudo cp "+file_name+" /media/usb") 
                                os.system("sudo cp /home/pi/Products/TYR/reports/"+file_name+" /media/usb")                            
                                os.system("sudo umount /media/usb")
                                #os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                                self.label_2.show()
                                self.label_2.setText("Succesfully copied to USB.")
                                self.browse_file_onclick()
            else:
                    self.label_2.show()
                    self.label_2.setText("USB Error.")
        else:
            self.label_2.show()
            self.label_2.setText("Select File Please.")
            
        
    def move_all(self):                   
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):                           
                                
                                os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi") 
                                os.system("sudo cd  /home/pi/Products/TYR/reports")                                
                                os.system("sudo cp /home/pi/Products/TYR/reports/*.pdf /media/usb")                            
                                os.system("sudo umount /media/usb")
                                #os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                                self.label_2.show()
                                self.label_2.setText("Copied all files to USB.")
                                self.browse_file_onclick()
        else:
                self.label_2.show()
                self.label_2.setText("USB Error.")
        
     
    def load_reports_files(self):
        try:
                    os.system("sudo rm -rf report_files.txt")
                    #os.system("sudo cd /home/pi/TYR_2.0_18.5/reports")
                    os.system("sudo ls /home/pi/Products/TYR/reports/Report_of_test*.pdf >> report_files.txt")
                    #os.system("sudo cd")
                    try:
                       self.listWidget.clear() 
                       f = open('report_files.txt','r')
                       for line in f:
                               line=line.replace("/home/pi/Products/TYR/reports/","")
                               ine=line.replace("\n","")
                               item= QtWidgets.QListWidgetItem(str(line))
                               #item.setBackground(QtGui.QColor("black"))
                               font = QtGui.QFont()
                               font.setFamily("Arial")
                               font.setPointSize(8)                                
                               item.setFont(font)
                               self.listWidget.addItem(item)
                       f.close()
                       self.label_2.show()
                       self.label_2.setText("")
                       
                    except:                       
                       self.label_2.show()
                       self.label_2.setText("USB ERROR.") 
                   
        except:                   
              self.label_2.show()
              self.label_2.setText("OS ERROR.")
        
    
    def browse_file_onclick(self):
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                try:
                    os.system("sudo rm -rf backupfiles_list.txt")  
                    os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")                    
                    os.system("sudo ls /media/usb/Report_of_test*.pdf >> backupfiles_list.txt")
                    os.system("sudo umount /media/usb")
                    try:
                       self.listWidget_2.clear() 
                       f = open('backupfiles_list.txt','r')
                       for line in f:
                               line=line.replace("/media/usb/","")
                               item= QtWidgets.QListWidgetItem(str(line))
                               #item.setBackground(QtGui.QColor("black"))
                               font = QtGui.QFont()
                               font.setFamily("Arial")
                               font.setPointSize(8)                                
                               item.setFont(font)
                               self.listWidget_2.addItem(item)
                       f.close()
                              
                       #self.label_2.show()
                       #self.label_2.setText("Done.")
                    except:
                       
                       self.label_2.show()
                       self.label_2.setText("USB Error.") 
                   
                except:
                   
                    self.label_2.show()
                    self.label_2.setText("OS ERROR.")
               
        else:
             #print("Please connect usb storage device")                   
             self.label_2.show()
             self.label_2.setText("PLEASE CONNECT USB DEVICE.")
        
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
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = usb_bkp_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
