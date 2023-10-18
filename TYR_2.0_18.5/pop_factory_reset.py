# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop_factory_reset.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from TY_09_register import TY_09_Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class factory_reset_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 30, 521, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        
        
        self.pushButton_3_1 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3_1.setGeometry(QtCore.QRect(360, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3_1.setFont(font)
        self.pushButton_3_1.setObjectName("pushButton_3_1")
        
        
        
        
        
        
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(350, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(160, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(160, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(110, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.deleteing_count=0
        self.total_test_count=0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Delete Now"))
        self.pushButton_3.setText(_translate("MainWindow", "Close"))
        self.pushButton_3_1.setText(_translate("MainWindow", "Register"))
        self.label_4.setText(_translate("MainWindow", "Deleted Data Succefully."))
        self.label_4.hide()
        self.checkBox.setText(_translate("MainWindow", "All Test Data"))
        self.checkBox_2.setText(_translate("MainWindow", "All Specimen Data"))
        self.label_5.setText(_translate("MainWindow", "Factory Reset"))
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.delete_data_batch)
        self.pushButton_3_1.clicked.connect(self.open_new_window)
        self.load_data()
    
    def load_data(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select count(*) FROM (select TEST_ID from TEST_MST LIMIT 500)") 
        for x in results:
            self.deleteing_count=str(x[0])                                 
        connection.close()
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select count(*) from TEST_MST") 
        for x in results:
            self.total_test_count=str(x[0])                                 
        connection.close()
        self.label_4.show()
        self.label_4.setText("Test Count: "+str(self.deleteing_count)+"/"+str(self.total_test_count))
        if(int(self.total_test_count) == 0):
            connection = sqlite3.connect("tyr.db")            
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('TEST_MST','CYCLES_MST','GRAPH_MST','STG_GRAPH_MST','CYCLES_MST_CYCLIC','TEST_DATA','PEAK_MST')")                   
                    
            connection.commit();
            connection.close()
            
            connection = sqlite3.connect("tyr.db")            
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("PRAGMA auto_vacuum = FULL")
                    cursor.execute("vacuum")
                    
            connection.commit();
            connection.close()
            
            print("Sequences are also reinitiated")
        else:
            print("Still Data is not cleanned")
            
    
    def delete_data(self):
        if(self.checkBox.isChecked()):            
            connection = sqlite3.connect("tyr.db")            
            with connection:        
                    cursor = connection.cursor()       
                    cursor.execute("DELETE FROM STG_GRAPH_MST")
                    cursor.execute("DELETE FROM GRAPH_MST WHERE ")
                    cursor.execute("DELETE FROM CYCLES_MST")
                    cursor.execute("DELETE FROM CYCLES_MST_CYCLIC")
                    cursor.execute("DELETE FROM TEST_MST")
                    cursor.execute("DELETE FROM TEST_DATA")
                    cursor.execute("DELETE FROM PEAK_MST")
                    cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('TEST_MST','CYCLES_MST','GRAPH_MST','STG_GRAPH_MST','CYCLES_MST_CYCLIC','TEST_DATA','PEAK_MST')")                    
            connection.commit();
            connection.close()
            print("ok - Deleted Test Data  ")
            self.label_4.show()        
        
          
        if(self.checkBox_2.isChecked()):            
            connection = sqlite3.connect("tyr.db")
            with connection:        
                    cursor = connection.cursor()       
                    cursor.execute("DELETE FROM SPECIMEN_MST")
                    cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('SPECIMEN_MST')")
                    
            connection.commit();
            connection.close()
            print("ok - Deleted Specimen Data  ")
            self.label_4.show()
            
    def delete_data_batch(self):
        if(self.checkBox.isChecked()):            
            connection = sqlite3.connect("tyr.db")            
            with connection:        
                    cursor = connection.cursor()       
                    cursor.execute("DELETE FROM STG_GRAPH_MST")
                    cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM TEST_MST LIMIT 500)")                    
                    cursor.execute("DELETE FROM CYCLES_MST WHERE TEST_ID NOT IN (SELECT TEST_ID FROM TEST_MST)")
                    cursor.execute("DELETE FROM TEST_DATA WHERE TEST_ID NOT IN (SELECT TEST_ID FROM TEST_MST)")
                    cursor.execute("DELETE FROM CYCLES_MST_CYCLIC")
                    cursor.execute("DELETE FROM PEAK_MST")
                    cursor.execute("DELETE FROM GRAPH_MST WHERE GRAPH_ID NOT IN (SELECT GRAPH_ID FROM CYCLES_MST)")  
                    #cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('TEST_MST','CYCLES_MST','GRAPH_MST','STG_GRAPH_MST','CYCLES_MST_CYCLIC')")                    
            connection.commit();
            connection.close()
            print("ok - Deleted Test Data  ")
            self.label_4.show()        
        
          
        if(self.checkBox_2.isChecked()):            
            connection = sqlite3.connect("tyr.db")
            with connection:        
                    cursor = connection.cursor()       
                    cursor.execute("DELETE FROM SPECIMEN_MST")
                    cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('SPECIMEN_MST')")
                    
            connection.commit();
            connection.close()
            print("ok - Deleted Specimen Data  ")
            self.label_4.show()
        
        self.load_data()
    
    
    def open_new_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_09_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()    
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = factory_reset_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
