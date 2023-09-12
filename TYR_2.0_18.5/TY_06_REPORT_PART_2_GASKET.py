# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'TY_06_REPORT_PART_2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem

import sqlite3

class TY_06_Ui_MainWindow_GASKET(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1331, 705))
        self.frame.setStyleSheet("")
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.frame.setObjectName("frame")
        
        self.shape=""       
        self.unit_typex=""
        self.lastIndex=13
        self.shear_mod_ip=""
        
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(540, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        
        self.label_6_1 = QtWidgets.QLabel(self.frame)
        self.label_6_1.setGeometry(QtCore.QRect(840, 30, 351, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_6_1.setFont(font)
        #self.label_6.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_6_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6_1.setObjectName("label_6_1")
        
        
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(570, 600, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setGeometry(QtCore.QRect(20, 111, 1291, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("background-color: rgb(221, 255, 234);")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        '''
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(670, 110, 641, 411))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        '''
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.test_type=""
        self.def_flg=""
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Report Part II")) 
        self.label_6_1.setText(_translate("MainWindow", " [ Test Id: 265 ]    [ Batch Id : 3452321qwe ] "))
        self.pushButton_14.setText(_translate("MainWindow", "Return"))
        self.pushButton_14.clicked.connect(MainWindow.close)
        self.def_flg=""
        #self.select_all_rows_2()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TEST_ID,BATCH_ID,TEST_TYPE,DEF_FLG FROM TEST_MST WHERE TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR)") 
        for x in results:           
            self.label_6_1.setText("[ Test Id: "+str(x[0])+" ]              [ Batch Id:"+str(x[1])+" ]")
            self.test_type=str(x[2])
            self.def_flg=str(x[3])
        connection.close()
        
        if(self.test_type=="Compress"):
            self.select_all_rows_compress()
        elif(self.test_type=="Tear"):
            self.select_all_rows_tear()
        elif(self.test_type=="Flexural"):
            self.select_all_rows_flexural()
        elif(self.test_type=="QLSS"):
            self.select_all_rows_qlss()
        elif(self.test_type=="ILSS"):
            self.select_all_rows_ilss()
        elif(self.test_type=="COF"):
            self.select_all_rows_cof()
        else:
            if(self.def_flg=="Y"):
                 self.guage_select_all_rows()
            else:
                 self.select_all_rows()
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)       
            
    def select_all_rows(self):
        self.delete_all_records()    
        self.tableWidget.setMidLineWidth(-4)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(13)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView { font-size:  10pt};")
        self.tableWidget.verticalHeader().setStyleSheet("QHeaderView { font-size:  10pt};")
        #self.tableWidget.horizontalHeader().setStyleSheet("::section {background-color : lightGray;font-size:10pt;}")
   
        #self.tableWidget.setRowCount(1)
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 80)
        self.tableWidget.setColumnWidth(4, 120)
        self.tableWidget.setColumnWidth(5, 80)
        self.tableWidget.setColumnWidth(6, 150)    
        self.tableWidget.setColumnWidth(7, 120)
        self.tableWidget.setColumnWidth(8, 120)
        self.tableWidget.setColumnWidth(9, 120)
        self.tableWidget.setColumnWidth(10, 120)
        self.tableWidget.setColumnWidth(11, 120)
        self.tableWidget.setColumnWidth(12, 120) 
        
        
        
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
           
        # SELECT SHAPE FROM SPECIMEN_MST WHERE SPECIMEN_NAME IN ( SELECT SPECIMEN_NAME FROM TEST_MST WHERE TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR))
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SHAPE FROM SPECIMEN_MST WHERE SPECIMEN_NAME IN ( SELECT SPECIMEN_NAME FROM TEST_MST WHERE TEST_ID IN (SELECT NEW_REPORT_TEST_ID FROM GLOBAL_VAR))") 
        for x in results:
            self.shape=x[0]
        connection.close()
        #self.shape='Pipe'                                 
        print ("shape :"+self.shape)        
        if (self.shape=="Rectangle"):
            if(self.unit_typex=="Lb/Inch"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe.No.', ' Thickness \n (Inch) ', ' Width \n (Inch) ', 'CS.Area \n (Inch2)','Break Load \n (Lb)' ,'Trvl.Dist \n (Inch)','% E@Peak','E@Break \n (Inch)','% E@Break','Tensile Strength \n (Lb/Inch2)','Mod@50% \n (Lb/Inch2)','Mod@100% \n (Lb/Inch2)','Mod@200% \n (Lb/Inch2)' ])        
            elif(self.unit_typex == "Newton/Mm"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe.No.', ' Thickness \n (mm) ', ' Width \n (mm) ', 'CS.Area \n (mm2)','Break Load \n (N)' ,'Trvl.Dist \n (mm)','% E@Peak','E@Break \n (Mm)','% E@Break','Tensile Strength \n (N/Mm2)','Mod@50% \n (N/Mm2)','Mod@100% \n (N/Mm2)','Mod@200% \n (N/Mm2)'])
            elif(self.unit_typex == "MPA"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe.No.', ' Thickness \n (mm) ', ' Width \n (mm) ', 'CS.Area \n (mm2)','Break Load \n (N)' ,'Trvl.Dist \n (mm)','% E@Peak','E@Break \n (Mm)','% E@Break','Tensile Strength \n (MPA)','Mod@50% \n (MPA)','Mod@100% \n (MPA)','Mod@200% \n (MPA)'])
            else:    
                self.tableWidget.setHorizontalHeaderLabels(['Spe.No.', ' Thickness \n (cm) ', ' Width \n (cm) ', 'CS.Area \n (cm2)','Break Load \n (Kgf)' ,'Trvl.Dist \n (cm)','% E@Peak','E@Break \n (Cm)','% E@Break','Tensile Strength \n (Kgf/Cm2)','Mod@50% \n (Kgf/Cm2)','Mod@100% \n (Kgf/Cm2)','Mod@200% \n (Kgf/Cm2)'])        
        
        
            
        elif (self.shape=="Cylindrical"):     
            self.tableWidget.setColumnCount(10)
            self.lastIndex=9
            if(self.unit_typex=="Lb/Inch"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Diameter \n (Inch)', 'CS.Area \n (Inch2)','Break Load \n (Lb)' ,'Trvl.Dist \n (Inch)','% E@Peak','E@Break \n (Inch)','% E@Break','Tensile Strength \n (Lb/Inch2)','Mod@50% \n (Lb/Inch2)','Mod@100% \n (Lb/Inch2)','Mod@200% \n (Lb/Inch2)'])
            elif(self.unit_typex == "Newton/Mm"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Diameter \n (mm)', 'CS.Area \n (mm2)','Break Load \n (N)' ,'Trvl.Dist \n (mm)','% E@Peak','E@Break \n (Mm)','% E@Break','Tensile Strength \n (N/Mm2)','Mod@50% \n (N/Mm2)','Mod@100% \n (N/Mm2)','Mod@200% \n (N/Mm2)'])
            elif(self.unit_typex == "MPA"):
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Diameter \n (mm)', 'CS.Area \n (mm2)','Break Load \n (N)' ,'Trvl.Dist \n (mm)','% E@Peak','E@Break \n (Mm)','% E@Break','Tensile Strength \n (MPA)','Mod@50% \n (MPA)','Mod@100% \n (MPA)','Mod@200% \n (MPA)'])
            else: 
                self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Diameter \n (cm)', 'CS.Area \n (cm2)','Break Load \n (Kg)' ,'Trvl.Dist \n (cm)','% E@Peak','E@Break \n (Cm)','% E@Break','Tensile Strength \n (Kg/Cm2)','Mod@50% \n (Kg/Cm2)','Mod@100% \n (Kg/Cm2)','Mod@200% \n (Kg/Cm2)'])
        
        else:
           self.tableWidget.setHorizontalHeaderLabels(['Spe. No.', 'Thickness \n (mm)', 'Width \n (mm)', 'CS.Area \n (mm2)','Break Load \n (kg)' ,'Trvl.Dist \n (mm)','% E@Peak','E@Break \n (Cm)','% E@Break','Tensile Strength \n (Kg/Cm2)','Mod@50% \n (Kg/Cm2)','Mod@100% \n (Kg/Cm2)','Mod@200% \n (Kg/Cm2)'])
       
        
        connection = sqlite3.connect("tyr.db")
        print("shape : "+str(self.shape))
        if (self.shape=="Rectangle"):            
            results=connection.execute("SELECT TYPE_STR as specimen_no,printf(\"%.2f\", THICKNESS),printf(\"%.2f\", WIDTH),printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", TENSILE_STRENGTH) ,printf(\"%.2f\", MODULUS_300) ,printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200)   FROM REPORT_PART_2_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
            results1=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.THICKNESS),printf(\"%.2f\", A.WIDTH),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", A.PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", A.PREC_E_AT_BREAK),printf(\"%.2f\", TENSILE_STRENGTH) ,printf(\"%.2f\", MODULUS_300) ,printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID,round(TENSILE_STRENGTH,2),round(MODULUS_300,2),round(MODULUS_100,2),round(MODULUS_200,2) FROM REPORT_PART_2 WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")       
        elif (self.shape=="Cylindrical"):
            results=connection.execute("SELECT TYPE_STR as specimen_no,printf(\"%.2f\", DIAMETER),printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", TENSILE_STRENGTH),printf(\"%.2f\", MODULUS_300),printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200) FROM REPORT_PART_2_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
            results1=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.2f\", A.DIAMETER),printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", TENSILE_STRENGTH),printf(\"%.2f\", MODULUS_300),printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_PART_2 WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")
        else:
            print("NO Val")
            results=connection.execute("SELECT TYPE_STR as specimen_no,printf(\"%.4f\", CS_AREA),printf(\"%.2f\", PEAK_LOAD),printf(\"%.2f\", E_PAEK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", TENSILE_STRENGTH),printf(\"%.2f\", MODULUS_300),printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200) FROM REPORT_PART_2_AGGR WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR)")
            results1=connection.execute("SELECT ((A.REC_ID)-B.MIN_REC_ID)+1 AS SPECIMEN_NO,printf(\"%.4f\", A.CS_AREA),printf(\"%.2f\", A.PEAK_LOAD),printf(\"%.2f\", A.E_BREAK_LOAD),printf(\"%.2f\", PREC_E_AT_PEAK),printf(\"%.2f\", A.E_AT_BREAK_MM),printf(\"%.2f\", PREC_E_AT_BREAK),printf(\"%.2f\", TENSILE_STRENGTH),printf(\"%.2f\", MODULUS_300),printf(\"%.2f\", MODULUS_100),printf(\"%.2f\", MODULUS_200) FROM REPORT_PART_2 A, (SELECT MIN(REC_ID) AS MIN_REC_ID, REPORT_ID FROM REPORT_PART_2 WHERE REPORT_ID IN (SELECT NEW_REPORT_ID FROM GLOBAL_VAR) ) B WHERE A.REPORT_ID=B.REPORT_ID ")           
            
        for row_number, row_data in enumerate(results):                        
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                
        for row_number, row_data in enumerate(results1):                    
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):                
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                
                                        
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)     
        connection.close()    

    
    
    
   
   
   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_06_Ui_MainWindow_GASKET()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
