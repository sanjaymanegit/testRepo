
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import QTableWidgetItem
import sqlite3
import csv
import sys,os

class pop_graph_data_radial_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 583)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 771, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 111, 471))
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(2)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.listWidget.addItem(item)
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 5, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 0, 127);")
        self.label.setObjectName("label")
        
        
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(620, 5, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText("Close")
        self.pushButton_9.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        
        self.pushButton_9_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9_1.setGeometry(QtCore.QRect(290, 5, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9_1.setFont(font)
        self.pushButton_9_1.setText("Copy CSV Data File to Ped-Drive")
        self.pushButton_9_1.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_9.setObjectName("pushButton_9_1")
        
        
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(140, 50, 611, 471))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.graph_id="0"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Graph Id : 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Graph Id : 2"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Graph Id :3"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Please Select Graph id to view Data set"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X_MM"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "X_CM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "X_INCH"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Y_KG"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Y_N"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Y_LB"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1.00"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "1.00"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "2.00"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "3.00"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "4.00"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "6.00"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.load_data()
        self.listWidget.doubleClicked.connect(self.show_single_graph_data)
        self.pushButton_9.clicked.connect(MainWindow.close)
        self.pushButton_9_1.clicked.connect(self.COPY_CSV_USB)
        
        
    def load_data(self):      
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TEST_ID FROM GLOBAL_VAR") 
        for x in results:
            self.test_id=str(x[0])
        connection.close()
        self.i=0
        self.g=[]
        self.listWidget.clear() 
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  DISTINCT GRAPH_ID FROM TEST_DATA_RADIAL WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
            self.g.append(int(x[0]))
            self.i=self.i+1            
            self.listWidget.addItem("Specimen No: ("+str(self.i)+")")
        connection.close()
        self.listWidget.setCurrentRow(0)
        self.show_single_graph_data()
    
    def COPY_CSV_USB(self):
        self.file_name="Data_test_id_"+str(self.test_id)+"_spec_"+str(self.spec_id)+".csv"
        conn = sqlite3.connect('tyr.db')
        cursor = conn.cursor()
        cursor.execute("SELECT X_NUM,X_NUM_CM,X_NUM_INCH,Y_NUM,Y_NUM_N,Y_NUM_LB,Y_NUM_MPA,Y_NUM_KN  FROM GRAPH_MST where X_NUM >0  AND Y_NUM > 0  AND GRAPH_ID = '"+str(self.graph_id)+"' ")
        with open("./reports/"+str(self.file_name), 'w',newline='') as csv_file:                
                csv_writer = csv.writer(csv_file)               
                csv_writer.writerow([i[0] for i in cursor.description]) 
                csv_writer.writerows(cursor)
        conn.close()
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
                os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                os.system("cp ./reports/"+str(self.file_name)+" /media/usb/"+str(self.file_name))
                os.system("sudo umount /media/usb")
                print("File Name :"+str(self.file_name))
                self.label.show()
                self.label.setText("File Name :"+str(self.file_name))
        else:
                print("Please connect usb storage device")
                self.label.show()
                self.label.setText("Please connect usb storage device")
    
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
           self.label.show()
           self.label.setText("USB Error.")             
        return product_id
    
    def show_single_graph_data(self):        
        #print("inside tear list.....")
        self.delete_all_records()
        row = self.listWidget.currentRow()
        print("Current row :"+str(row))        
        if(row > -1):
                    font = QtGui.QFont()
                    font.setPointSize(10)
                    self.tableWidget.setFont(font)
                    self.tableWidget.setColumnCount(7)
                    self.tableWidget.horizontalHeader().setStretchLastSection(True)
                    self.tableWidget.setHorizontalHeaderLabels(['X_MM','X_CM','X_INCH','Y_KG','Y_N','Y_LB','Rec.ID'])  
                          
                    self.tableWidget.setColumnWidth(0, 100)
                    self.tableWidget.setColumnWidth(1, 100)
                    self.tableWidget.setColumnWidth(2, 100)
                    self.tableWidget.setColumnWidth(3, 100)
                    self.tableWidget.setColumnWidth(4, 100)
                    self.tableWidget.setColumnWidth(5, 100)
                    self.tableWidget.setColumnWidth(6, 100)
                    self.spec_id=str(row+1)
                    self.graph_id=str(self.g[row])
                    self.pushButton_9_1.setText("Copy CSV Data (Spec:"+str(self.spec_id)+")")
                    connection = sqlite3.connect("tyr.db")
                     
                    results=connection.execute("SELECT printf(\"%.2f\", X_NUM),printf(\"%.2f\", X_NUM_CM),printf(\"%.2f\", X_NUM_INCH),printf(\"%.2f\", Y_NUM),printf(\"%.2f\", Y_NUM_N),printf(\"%.2f\", Y_NUM_LB),REC_ID FROM GRAPH_MST where X_NUM >0  AND Y_NUM > 0  AND GRAPH_ID = '"+str(self.g[row])+"' ")
                    for row_number, row_data in enumerate(results):            
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
                    #self.tableWidget.resizeColumnsToContents()
                    self.tableWidget.resizeRowsToContents()
                    self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
                    connection.close()
        else:
            print("Please select Graph Id")
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = pop_graph_data_radial_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
