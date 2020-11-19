# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fci_10_batch_report.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.Qt import QTableWidgetItem
import datetime
import sqlite3
from PyQt5.QtCore import QDate
import os,sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import landscape, letter,inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak,Spacer, PageTemplate
from reportlab.lib import colors
import os,sys
from reportlab.rl_config import defaultPageSize
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import landscape, letter,inch,A4

class fci_10_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        #MainWindow.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 711))
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        #self.label.setStyleSheet("color: rgb(170, 85, 127);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(1140, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 190, 1261, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(5)
        '''
       
        '''
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(20, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        #self.label_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(280, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 650, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 650, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(410, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        #self.label_8.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 650, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(500, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(610, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        #self.label_11.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(270, 70, 551, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("")
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(16, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(140, 120, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        #self.label_9.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        
        self.pushButton_8_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8_1.setGeometry(QtCore.QRect(470, 650, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8_1.setFont(font)
        self.pushButton_8_1.setObjectName("pushButton_8_1")
        
        self.label_30_1 = QtWidgets.QLabel(self.frame)
        self.label_30_1.setGeometry(QtCore.QRect(620, 650, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_30_1.setFont(font)
        self.label_30_1.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_30_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30_1.setObjectName("label_30")
        
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
        self.from_dt=""
        self.to_dt=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Buy Report as on "+datetime.datetime.now().strftime("%d %b %Y")))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45 :00"))
        
        self.label_22.setText(_translate("MainWindow", "Report Type: "))
        self.label_2.setText(_translate("MainWindow", "Monthly"))
        self.label_29.setText(_translate("MainWindow", "Net. Weight :"))
        self.pushButton_5.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_7.setText(_translate("MainWindow", "PRINT"))
        self.label_8.setText(_translate("MainWindow", "5450"))
        self.pushButton_8.setText(_translate("MainWindow", "RETURN"))
        
        self.pushButton_8_1.setText(_translate("MainWindow", "VIEW PRINT"))
        self.label_30_1.setText(_translate("MainWindow", "Max. Print Pages : 4"))
        
        self.label_30.setText(_translate("MainWindow", "Total Trucks :"))
        self.label_11.setText(_translate("MainWindow", "150"))
        self.label_36.setText(_translate("MainWindow", "Report selected Month : MAY 2020"))
        self.label_23.setText(_translate("MainWindow", "No.Of Recipts:"))
        self.label_9.setText(_translate("MainWindow", "5450"))
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.startx()
    
    def startx(self):
        self.whr_sql=""
        self.whr_sql2=""
        self.pushButton_5.clicked.connect(self.select_all_data)
        self.pushButton_7.clicked.connect(self.print_report)
        self.pushButton_8_1.clicked.connect(self.open_pdf)
        connection = sqlite3.connect("fci.db")
        results=connection.execute("SELECT LOGIN_USER_ID ,LOGIN_USER_ROLE FROM GLOBAL_VAR") 
        for x in results:
            self.login_user_id=str(x[0])
            self.login_user_role=str(x[1])
        connection.close()
        #print("self.login_user_role :"+str(self.login_user_role))
        
        connection = sqlite3.connect("fci.db")
        results=connection.execute("SELECT REPORT_ENTITY,REPORT_BY,REPORT_FROM_DATE,REPORT_TO_DATE,REPORT_BATCH_ID  FROM GLOBAL_VAR") 
        for x in results:            
                 self.label_2.setText(str(x[1]))
                 self.from_dt=str(x[2])
                 self.to_dt=str(x[3])
                 
                 if(self.label_2.text() == 'DATE_RANGE'):
                     self.label_36.setText("Report selected for date range  <font color=blue> [ "+str(x[2])+" ] </font>  to  <font color=blue> [ "+str(x[3])+" ] </font>.")
                     
                     self.whr_sql=" WHERE strftime('%Y-%m-%d',START_DATE)  between '"+str(x[2])+"' and '"+str(x[3])+"' limit 400"
                     self.whr_sql2=" WHERE  BATCH_ISSUE_FLG='BUY'  AND  IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON)  between '"+str(x[2])+"' and '"+str(x[3])+"' order by batch_id,CURR_TRUCK_CNT limit 400"
                 elif(self.label_2.text() == 'BY_BATCH_ID'):
                     self.label_36.setText("Report selected for batch id:"+str(x[4])+".")
                     
                     self.whr_sql="WHERE BATCH_ID = '"+str(x[4])+"'"
                     self.whr_sql2="WHERE  BATCH_ID = '"+str(x[4])+"' order by batch_id,CURR_TRUCK_CNT "
                     
                 else:
                     self.label_36.setText("Report selected for unknow.")
        connection.close()
        
        connection = sqlite3.connect("fci.db")
        #print("select count(BATCH_ID),sum(TOTAL_TRUCKS),SUM(TOTAL_NET_WT) from BATCH_LIST_VW "+str(self.whr_sql))
        results=connection.execute("select count(BATCH_ID),sum(TOTAL_TRUCKS),round(SUM(TOTAL_NET_WT),3) from BATCH_LIST_VW "+str(self.whr_sql)) 
        for x in results:            
                     self.label_9.setText(str(x[0]))
                     self.label_11.setText(str(x[1]))
                     self.label_8.setText(str(x[2]))
        connection.close()
        
        connection = sqlite3.connect("fci.db")        
        results=connection.execute("SELECT count(*),printf(\"%.3f\",  sum(net_weight_val)),count(distinct batch_id)  FROM WEIGHT_MST_FCI_VW "+str(self.whr_sql2))        
        for x in results:
                self.label_11.setText(str(x[0]))
                self.label_8.setText(str(x[1]))
                self.label_9.setText(str(x[2]))
        connection.close()
        
        self.select_all_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1) 
        
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def print_report(self):        
         os.system("./job_print_report.sh")
                        
    def select_all_data(self):
        
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 100)    
        self.tableWidget.setColumnWidth(7, 100)
        self.tableWidget.setColumnWidth(8, 150)
        self.tableWidget.setColumnWidth(9, 200)    
        self.tableWidget.setColumnWidth(10, 100)
        
        
        
        #print("whr_sql2 :"+str(self.whr_sql2))
        self.tableWidget.setHorizontalHeaderLabels(['Serial Id ','Vehical No.','No. Bags','Release Date','Release Time' ,'Net. Wt.','Tare Wt.','Gross Wt.','Storage Name'])        
           
        connection = sqlite3.connect("fci.db")
        if(self.login_user_role in ['SUPER_ADMIN','ADMIN','SUPERVISOR']):                
                results=connection.execute("SELECT SERIAL_ID,VEHICLE_NO,printf(\"%3d\", ACCPTED_BAGS) ,SUBSTR(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON),1,11) AS RELEASE_DATE,SUBSTR(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON),11,6) AS RELEASE_TIME,printf(\"%6d\", NET_WEIGHT_VAL) as NET_WEIGHT_VAL,printf(\"%6d\", TARE_WT_VAL) as TARE_WT_VAL,printf(\"%6d\", GROSS_WT_VAL) as GROSS_WT_VAL,TARGET_STORAGE FROM WEIGHT_MST_FCI_VW "+str(self.whr_sql2))                       
      
        else:
                results=connection.execute("SELECT SERIAL_ID,VEHICLE_NO,printf(\"%3d\", ACCPTED_BAGS) ,SUBSTR(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON),1,11) AS RELEASE_DATE,SUBSTR(IFNULL(SECOND_WT_CREATED_ON,FIRST_WT_CRTEATED_ON),11,6) AS RELEASE_TIME,printf(\"%6d\", NET_WEIGHT_VAL) as NET_WEIGHT_VAL,printf(\"%6d\", TARE_WT_VAL) as TARE_WT_VAL,printf(\"%6d\", GROSS_WT_VAL) as GROSS_WT_VAL,TARGET_STORAGE FROM WEIGHT_MST_FCI_VW "+str(self.whr_sql2))                        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                #self.lineEdit.setText("")
        connection.close()   
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)
            
    def open_pdf(self):
        self.create_report_pdf()
        os.system("xpdf ./reports/dr_other_report.pdf")
    
    def create_report_pdf(self):
        PAGE_HEIGHT=defaultPageSize[1]
        styles = getSampleStyleSheet()
        total_amount="0"
        #styles.add(ParagraphStyle(name="x", fontSize=12, leading = 7, alignment=TA_LEFT))
        #styles.add(ParagraphStyle(name="x2", fontSize=10, leading = 7, alignment=TA_LEFT))
        
        connection = sqlite3.connect("fci.db")       
        results=connection.execute("SELECT  PRINTER_HEATER_TITLE,PRINTER_HEADER,PRINTER_FOOTER FROM GLOBAL_VAR") 
        for x in results:
                   Title = Paragraph(str(x[0]), styles["Title"])
                   ptext = "<font name=Helvetica size=10>"+str(x[1])+" </font>"
                   Title2 = Paragraph(str(ptext), styles["Title"])
        connection.close()
        
        
        connection = sqlite3.connect("fci.db")        
        results=connection.execute("SELECT count(*) FROM WEIGHT_MST_FCI_VW "+str(self.whr_sql2))        
        for x in results:
                total_amount=str(x[0])                
        connection.close()
        
        
                
                
                
        summary_data=[["From Date: "+str(self.from_dt),"To Date: "+str(self.to_dt) , "Total Trucks: "+str(total_amount), "Report Date: "+str(datetime.datetime.now().strftime("%d %b %Y %H:%M"))]]
                       
        
        
         
        f3=Table(summary_data)
        #f3.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 10)]))       
        
        Elements = [Title,Spacer(1,12),Title2,Spacer(1,12),f3,Spacer(1,12),Spacer(1,12)]
         
        
        childs_data=[]
        childs_data=[['Serial ID.','Recipt Id', ' Vehicle.No ','Material Name' ,' Net Wt.',' Tare Wt.',' Gross Wt.','Storage Name']]
        connection = sqlite3.connect("fci.db")           
           
        results=connection.execute("SELECT SERIAL_ID_DISPLY,(SELECT A.BATCH_ID_DISPLAY FROM BATCH_MST A WHERE A.BATCH_ID=BATCH_ID) as BATCH_ID,VEHICLE_NO,MATERIAL_NAME,printf(\"%3d\",IFNULL(NET_WEIGHT_VAL,0)),printf(\"%3d\", TARE_WT_VAL) as TARE_WT_VAL,printf(\"%6d\", GROSS_WT_VAL) as GROSS_WT_VAL,TARGET_STORAGE FROM WEIGHT_MST_FCI_VW "+str(self.whr_sql2))             
        for k in results:
                childs_data.append(k)
        connection.close()
        f=Table(childs_data)
        f.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.20, colors.black),('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),('FONT', (0, 0), (-1, -1), "Helvetica", 9)]))       
         
        Elements.append(f)
        
        doc = SimpleDocTemplate('./reports/dr_other_report.pdf',pagesize=A4)
        doc.pagesize = landscape(A4)
        doc.build(Elements)
        print("Done")
        self.filter_col_name=""
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fci_10_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
