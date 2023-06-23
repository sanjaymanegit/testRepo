
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import QTableWidgetItem
import sqlite3
import datetime
import sys
from PyQt5.QtCore import QDate
import sys,os
import sqlite3
import csv


class TY_47_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 685)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1021, 631))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(255, 237, 250);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(530, 20, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 85, 127);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(530, 80, 451, 451))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(226, 255, 225);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
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
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(20, 560, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(860, 560, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 560, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(20, 20, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(230, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(770, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(85, 0, 0);")
        self.checkBox.setObjectName("checkBox")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 461, 451))
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(3)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(660, 560, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-style:outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"background-color: rgb(226, 239, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1055, 21))
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
        self.label.setText(_translate("MainWindow", "Import Specimens"))
        self.label_21.setText(_translate("MainWindow", "Please select the record to Edit."))
        self.pushButton_5.setText(_translate("MainWindow", "Refresh USB "))
        self.pushButton_9.setText(_translate("MainWindow", "Close"))
        self.pushButton_6.setText(_translate("MainWindow", "Import"))
        self.pushButton_6.setDisabled(True)
        self.label_22.setText(_translate("MainWindow", "USB Connection Status:"))
        self.label_23.setText(_translate("MainWindow", "Connected !"))
        self.checkBox.setText(_translate("MainWindow", "Check All"))
        self.pushButton_7.setText(_translate("MainWindow", "Refresh Specs List"))
        self.tableWidget.setHorizontalHeaderLabels(['Spec.Id.','Product Name', ' Party Name ','Validation'] )
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.label_21.hide()
        self.pushButton_9.clicked.connect(MainWindow.close)
        self.listWidget.doubleClicked.connect(self.validation)
        self.pushButton_7.clicked.connect(self.load_data)
        self.pushButton_6.clicked.connect(self.actual_import)
        self.checkBox.clicked.connect(self.check_uncheck_all_records)
        self.check_for_usb()
        #self.load_data()
        
    
    
    def load_data(self):     
        self.c_delete_all_records()        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
  
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        self.tableWidget.setHorizontalHeaderLabels(['Spec.Id.','Product Name', ' Party Name ','Validation'] )       
           
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select SPECIMEN_ID ,SPECIMEN_NAME ,PARTY_NAME ,COMMENTS FROM STG_SPECIMEN_MST")                        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if(int(column_number) == 0):
                    #print("data-column_number :"+str(column_number))
                    item = QtWidgets.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(QtCore.Qt.Unchecked)
                    item.setText(str(data))
                    self.tableWidget.setItem(row_number,column_number,item)
                    #self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                else:
                    self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                    #self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))                
        connection.close()   
        #self.tableWidget.resizeColumnsToContents()
        
        
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.checkBox.setChecked(False)
        
    def c_delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
    
    
    def check_for_usb(self):
        product_id=self.get_usb_storage_id()
        if(product_id != "ERROR"):
            try:
                    os.system("sudo rm -rf specs_csv_files_list.txt")  
                    os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")                    
                    os.system("sudo ls /media/usb/specimens*.csv >> specs_csv_files_list.txt")
                    os.system("sudo umount /media/usb")
                    try:
                       self.listWidget.clear() 
                       f = open('specs_csv_files_list.txt','r')
                       for line in f:
                               line=line.replace("/media/usb/","")
                               item= QtWidgets.QListWidgetItem(str(line))
                               #item.setBackground(QtGui.QColor("black"))
                               font = QtGui.QFont()
                               font.setFamily("Arial")
                               font.setPointSize(10)                                
                               item.setFont(font)
                               self.listWidget.addItem(item)
                       f.close()                              
                       self.label_23.setText("Connected !")
                       self.label_21.show()
                       self.label_21.setText("Double click on the file to verify Specimens data.")
                       self.pushButton_6.setEnabled(True)
                    except:                       
                       self.label_21.show()
                       self.label_21.setText("USB Error.") 
                   
            except:
                    self.label_21.show()
                    self.label_21.setText("OS ERROR.")
        else:
             print("Please connect usb storage device")                   
             self.label_21.show()
             self.label_21.setText("USB Error.")
             self.label_23.setText("NA")
             self.pushButton_6.setDisabled(True)
        
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
           self.label_21.show()
           self.label_21.setText("USB Error.")             
        return product_id
        
    def validation(self):
        self.pushButton_6.setEnabled(True)
        connection = sqlite3.connect("tyr.db")
        with connection:        
                     cursor = connection.cursor()
                     cursor.execute("DELETE FROM STG_SPECIMEN_MST")                    
        connection.commit();                    
        connection.close()
        
        print("Import Process started !!")
        conn = sqlite3.connect('tyr.db')
        cursor = conn.cursor()
        os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")  
        file = open("/media/usb/specimens.csv")
        headings = next(file)  ### skipiing header.
        os.system("sudo umount /media/usb")
        contents = csv.reader(file)
        insert_records = "INSERT INTO STG_SPECIMEN_MST (SPECIMEN_ID,SPECIMEN_NAME,SPECIMEN_SPECS,SHAPE,THICKNESS,WIDTH,DIAMETER,C_A_AREA,MOTOR_SPEED,PARTY_NAME,PRE_LOAD,GUAGE_LENGTH_MM,IN_DIAMETER_MM,OUTER_DIAMETER_MM,CREATED_ON,TESTED_BY,REV_MOTOR_SPEED,LAST_UNIT_LOAD,LAST_UNIT_DISP) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"                        
        cursor.executemany(insert_records, contents)
        conn.commit()
        conn.close()
        file.close()
        
        ########################
        #### Validation ########
        ########################       
        
        self.ERR_MSG="ok"
        self.spec_id_arr=[]
        self.error_msg_arr=[]
        self.spec_name_arr=[]
        self.arr_len=0
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select SPECIMEN_NAME ,PARTY_NAME ,C_A_AREA,MOTOR_SPEED,PRE_LOAD,GUAGE_LENGTH_MM,SPECIMEN_ID,upper(SPECIMEN_NAME)  FROM STG_SPECIMEN_MST") 
        for x in results:
            self.spec_id_arr.append(str(x[6]))
            self.spec_name_arr.append(str(x[7]))
            if(str(x[0]) == ""):
                 self.ERR_MSG=str(self.ERR_MSG)+" Spec Name Empty"
            elif(str(x[1]) == ""):
                  self.ERR_MSG=str(self.ERR_MSG)+", Party Name Empty"
            elif(str(x[2]) == ""):
                  self.ERR_MSG=str(self.ERR_MSG)+", AREA Empty"
            elif(str(x[3]) == ""):
                  self.ERR_MSG=str(self.ERR_MSG)+", Motor Speed Empty"
            elif(str(x[4]) == ""):
                  self.ERR_MSG=str(self.ERR_MSG)+", PRE_LOAD Empty"
            elif(str(x[5]) == ""):
                  self.ERR_MSG=str(self.ERR_MSG)+", length Empty"
            else:
                  self.ERR_MSG="ok"
            self.error_msg_arr.append(str(self.ERR_MSG))
            print("inside validation ")
        connection.close()
        
        
        self.arr_len=len(self.spec_id_arr)
        
        ###### Validation ########
        connection = sqlite3.connect("tyr.db")
        with connection:        
                     cursor = connection.cursor()
                     for j in range(len(self.spec_id_arr)):
                             cursor.execute("UPDATE STG_SPECIMEN_MST  SET COMMENTS = '"+str(self.error_msg_arr[j])+"' WHERE SPECIMEN_ID='"+str(self.spec_id_arr[j])+"'")
                             
        connection.commit();                    
        connection.close()
        
        self.ERR_MSG="DUPLICATE RECORD"
        self.spec_id_arr=[]
        self.error_msg_arr=[]
        self.arr_len=0
        connection = sqlite3.connect("tyr.db")
        for k in range(len(self.spec_name_arr)):
             connection = sqlite3.connect("tyr.db")
             results=connection.execute("select count(*)  FROM SPECIMEN_MST where UPPER(SPECIMEN_NAME)='"+str(self.spec_name_arr[k])+"'") 
             for x in results:
                 if(int(x[0]) > 0):
                     self.spec_id_arr.append(str(self.spec_name_arr[k]))
                     self.error_msg_arr.append("DUPLICATE RECORD")                     
                 else:
                     self.spec_id_arr.append(str(self.spec_name_arr[k]))
                     self.error_msg_arr.append("ok")
                                         
        connection.close()
            
        
        connection = sqlite3.connect("tyr.db")
        with connection:        
                     cursor = connection.cursor()
                     for l in range(len(self.spec_id_arr)):
                             cursor.execute("UPDATE STG_SPECIMEN_MST  SET COMMENTS = '"+str(self.error_msg_arr[l])+"' WHERE UPPER(SPECIMEN_NAME)='"+str(self.spec_id_arr[l])+"'")                             
        connection.commit();                    
        connection.close()
        self.load_data()
        
        
    def actual_import(self):
        self.del_uncheked()
        print("Import Started !!")
        ####### Clean Data copy to main tables #########
        connection = sqlite3.connect("tyr.db")
        with connection:
                     cursor = connection.cursor()
                     print("INSERT INTO SPECIMEN_MST (SPECIMEN_NAME,SPECIMEN_SPECS,SHAPE,THICKNESS,WIDTH,DIAMETER,C_A_AREA,MOTOR_SPEED,PARTY_NAME,PRE_LOAD,GUAGE_LENGTH_MM,IN_DIAMETER_MM,OUTER_DIAMETER_MM,CREATED_ON,TESTED_BY,REV_MOTOR_SPEED,LAST_UNIT_LOAD,LAST_UNIT_DISP) SELECT SPECIMEN_NAME,SPECIMEN_SPECS,SHAPE,THICKNESS,WIDTH,DIAMETER,C_A_AREA,MOTOR_SPEED,PARTY_NAME,PRE_LOAD,GUAGE_LENGTH_MM,IN_DIAMETER_MM,OUTER_DIAMETER_MM,CREATED_ON,TESTED_BY,REV_MOTOR_SPEED,LAST_UNIT_LOAD,LAST_UNIT_DISP FROM STG_SPECIMEN_MST WHERE COMMENTS ='ok' and SPECIMEN_ID IN (SELECT TEST_ID FROM TEST_IDS)")
                     
                     cursor.execute("INSERT INTO SPECIMEN_MST (SPECIMEN_NAME,SPECIMEN_SPECS,SHAPE,THICKNESS,WIDTH,DIAMETER,C_A_AREA,MOTOR_SPEED,PARTY_NAME,PRE_LOAD,GUAGE_LENGTH_MM,IN_DIAMETER_MM,OUTER_DIAMETER_MM,CREATED_ON,TESTED_BY,REV_MOTOR_SPEED,LAST_UNIT_LOAD,LAST_UNIT_DISP) SELECT SPECIMEN_NAME,SPECIMEN_SPECS,SHAPE,THICKNESS,WIDTH,DIAMETER,C_A_AREA,MOTOR_SPEED,PARTY_NAME,PRE_LOAD,GUAGE_LENGTH_MM,IN_DIAMETER_MM,OUTER_DIAMETER_MM,CREATED_ON,TESTED_BY,REV_MOTOR_SPEED,LAST_UNIT_LOAD,LAST_UNIT_DISP FROM STG_SPECIMEN_MST WHERE COMMENTS ='ok' and SPECIMEN_ID IN (SELECT TEST_ID FROM TEST_IDS)")
                     print("Inserted Records :"+str(cursor.rowcount))
                     self.label_21.show()
                     self.label_21.setText("Inserted Records :"+str(cursor.rowcount))  
        connection.commit();                    
        connection.close()        
        print("Import Process Completed !!")
        self.pushButton_6.setDisabled(True)
        
          
    def check_uncheck_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            item = self.tableWidget.item(i, 0)
            if(self.checkBox.isChecked()):
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(not QtCore.Qt.Checked)
    
    def del_uncheked(self):
        connection = sqlite3.connect("tyr.db")
        with connection:        
                     cursor = connection.cursor()
                     cursor.execute("DELETE FROM TEST_IDS")                    
        connection.commit();                    
        connection.close()
        i = self.tableWidget.rowCount()       
        while (i > 0):
            i=i-1
            item = self.tableWidget.item(i, 0)
            print("spec id :"+str(item.text()))
            currentState = item.checkState()
            if(currentState == QtCore.Qt.Checked):
                    print("Checked Spec.ID:"+str(item.text()))
                    connection = sqlite3.connect("tyr.db")          
                    with connection:        
                            cursor = connection.cursor()                            
                            cursor.execute("INSERT INTO TEST_IDS SELECT B.SPECIMEN_ID,''   FROM STG_SPECIMEN_MST B WHERE B.SPECIMEN_ID='"+str(item.text())+"' AND B.SPECIMEN_ID NOT IN (SELECT TEST_ID FROM TEST_IDS)") 
                            print("Inserted Records :"+str(cursor.rowcount))
                    connection.commit();
                    connection.close()                    
            else:
                    print("Un-Checked Spec.ID:"+str(item.text()))
                    connection = sqlite3.connect("tyr.db")          
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM TEST_IDS WHERE TEST_ID = '"+str(item.text())+"'")                             
                            print("Deleted Records :"+str(cursor.rowcount))
                    connection.commit();
                    connection.close()
        
        
        
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_47_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
