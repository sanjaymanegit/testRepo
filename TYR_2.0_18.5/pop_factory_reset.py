
from TY_09_register import TY_09_Ui_MainWindow

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class factory_reset_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 369)
        MainWindow.setMinimumSize(QtCore.QSize(612, 369))
        MainWindow.setMaximumSize(QtCore.QSize(612, 369))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#frame_2{\n"
"border:3px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"#frame{\n"
"border:2px solid black;\n"
"border-radius: 10px;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));\n"
"border-radius: 25px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 591, 351))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setGeometry(QtCore.QRect(220, 150, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_2.setGeometry(QtCore.QRect(220, 190, 181, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(90, 20, 411, 51))
        self.frame.setStyleSheet("border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(220, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border: none;\n"
"\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(20, 260, 551, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 0, 0), stop:1  rgb(158, 3, 3));\n"
"    \n"
"    \n"
"\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(158, 3, 3), stop:1  rgb(255, 0, 0));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton:pressed {\n"
"background-color: rgb(255, 0, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setStyleSheet("#pushButton_6 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(198, 198, 198), stop:1  rgb(255, 255, 255));\n"
"    \n"
"\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_6:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 255, 255), stop:1  rgb(198, 198, 198));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_6:pressed {\n"
"background-color: rgb(198, 198, 198);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("#pushButton_3 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(37, 197, 255), stop:1  rgb(44, 69, 211));\n"
"    \n"
"    \n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_3:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(44, 69, 211), stop:1  rgb(37, 197, 255));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_3:pressed {\n"
"background-color: rgb(37, 197, 255);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3_1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3_1.setFont(font)
        self.pushButton_3_1.setStyleSheet("#pushButton_3_1 {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(85, 255, 0), stop:1  rgb(7, 240, 151));\n"
"    \n"
"\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:3px;\n"
"}\n"
"#pushButton_3_1:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(7, 240, 151), stop:1  rgb(85, 255, 0));\n"
"padding-bottom: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_3_1:pressed {\n"
"background-color: rgb(85, 255, 0);\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"}")
        self.pushButton_3_1.setObjectName("pushButton_3_1")
        self.horizontalLayout.addWidget(self.pushButton_3_1)
        self.widget1 = QtWidgets.QWidget(self.frame_2)
        self.widget1.setGeometry(QtCore.QRect(50, 100, 481, 21))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(150)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "All Test Data"))
        self.checkBox_2.setText(_translate("MainWindow", "All Specimen Data"))
        self.label.setText(_translate("MainWindow", "Factory Reset"))
        self.pushButton.setText(_translate("MainWindow", "Delete Now"))
        self.pushButton_6.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Close"))
        self.pushButton_3_1.setText(_translate("MainWindow", "Register"))
        self.label_5.setText(_translate("MainWindow", "Test Data Deteled Successfully..."))
        self.label_4.setText(_translate("MainWindow", "Test Count: "))
        self.label_5.hide()
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.delete_data_batch)
        self.pushButton_3_1.clicked.connect(self.open_new_window)
        self.pushButton_6.clicked.connect(self.reset_Fields)
        self.load_data()
    def reset_Fields(self):
          
        self.label_5.hide()
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
          
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
                    cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('TEST_MST','CYCLES_MST','GRAPH_MST','STG_GRAPH_MST','CYCLES_MST_CYCLIC','TEST_DATA','PEAK_MST','DEFLECTION_DATA','LOAD_DATA','LOW_VAL_MST','TEST_DATA_RADIAL')")                   
                    
            connection.commit()
            connection.close()
            
            connection = sqlite3.connect("tyr.db")            
            with connection:        
                    cursor = connection.cursor()
                    cursor.execute("PRAGMA auto_vacuum = FULL")
                    cursor.execute("vacuum")
                    
            connection.commit()
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
                    cursor.execute("DELETE FROM GRAPH_MST ")
                    cursor.execute("DELETE FROM CYCLES_MST")
                    cursor.execute("DELETE FROM CYCLES_MST_CYCLIC")
                    cursor.execute("DELETE FROM TEST_MST")
                    cursor.execute("DELETE FROM TEST_DATA")
                    cursor.execute("DELETE FROM PEAK_MST") 
                    cursor.execute("DELETE FROM LOW_VAL_MST")
                    cursor.execute("DELETE FROM TEST_DATA_RADIAL")
                    cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('TEST_MST','CYCLES_MST','GRAPH_MST','STG_GRAPH_MST','CYCLES_MST_CYCLIC','TEST_DATA','PEAK_MST','LOW_VAL_MST','DEFLECTION_DATA','LOAD_DATA','LOW_VAL_MST','TEST_DATA_RADIAL')")                    
            connection.commit()
            connection.close()
            print("ok - Deleted Test Data  ")
            self.label_4.show()  
            

        
          
        if(self.checkBox_2.isChecked()):            
            connection = sqlite3.connect("tyr.db")
            with connection:        
                    cursor = connection.cursor()       
                    cursor.execute("DELETE FROM SPECIMEN_MST")
                    cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('SPECIMEN_MST')")
                    
            connection.commit()
            connection.close()
            print("ok - Deleted Specimen Data  ")
            self.label_4.show()
            
    def delete_data_batch(self):

        if(self.checkBox.isChecked()) or (self.checkBox_2.isChecked()):
             pass
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please check atleast One data type to be delete...")
            msg.setWindowTitle("Field Not Checked")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_() 


        if(self.checkBox.isChecked()): 
                delete = QMessageBox()
                delete.setWindowTitle("Confirm To Delete")
                delete.setText("Message: Are you sure to delete All Test Data...?")
                delete.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                delete = delete.exec()
                if delete == QMessageBox.Yes:
                # print("see the msg: ", msg)           
                        connection = sqlite3.connect("tyr.db")            
                        with connection:        
                                cursor = connection.cursor()       
                                cursor.execute("DELETE FROM STG_GRAPH_MST")
                                cursor.execute("DELETE FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM TEST_MST LIMIT 500)")                    
                                cursor.execute("DELETE FROM CYCLES_MST WHERE TEST_ID NOT IN (SELECT TEST_ID FROM TEST_MST)")
                                cursor.execute("DELETE FROM TEST_DATA WHERE TEST_ID NOT IN (SELECT TEST_ID FROM TEST_MST)")
                                cursor.execute("DELETE FROM DEFLECTION_DATA WHERE TEST_ID NOT IN (SELECT TEST_ID FROM TEST_MST)")
                                cursor.execute("DELETE FROM LOAD_DATA WHERE TEST_ID NOT IN (SELECT TEST_ID FROM TEST_MST)")                    
                                cursor.execute("DELETE FROM CYCLES_MST_CYCLIC")
                                cursor.execute("DELETE FROM PEAK_MST")
                                cursor.execute("DELETE FROM LOW_VAL_MST")
                                cursor.execute("DELETE FROM TEST_DATA_RADIAL")
                                cursor.execute("DELETE FROM GRAPH_MST WHERE GRAPH_ID NOT IN (SELECT GRAPH_ID FROM CYCLES_MST)")  
                                #cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('TEST_MST','CYCLES_MST','GRAPH_MST','STG_GRAPH_MST','CYCLES_MST_CYCLIC')")                    
                        connection.commit()
                        connection.close()
                        print("ok - Deleted Test Data  ")
                        self.label_4.show()
                        self.label_5.setText(("Test Data Deteled Successfully..."))        
                        self.label_5.show() 
          
        if(self.checkBox_2.isChecked()): 
                delete = QMessageBox()
                delete.setWindowTitle("Confirm To Delete")
                delete.setText("Message: Are you sure to delete All Specimen Data...?")
                delete.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                delete = delete.exec()
                if delete == QMessageBox.Yes:           
                        connection = sqlite3.connect("tyr.db")
                        with connection:        
                                cursor = connection.cursor()       
                                cursor.execute("DELETE FROM SPECIMEN_MST")
                                cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('SPECIMEN_MST')")
                                
                        connection.commit()
                        connection.close()
                        print("ok - Deleted Specimen Data  ")
                        self.label_4.show()
                        self.label_5.setText(("Specimen Data Deteled Successfully..."))
                        self.label_5.show() 
        
        if(self.checkBox.isChecked()) and (self.checkBox_2.isChecked()):
             self.label_5.setText(("All Data Deteled Successfully..."))
             self.label_5.show() 
             self.checkBox.setChecked(False)
             self.checkBox_2.setChecked(False)
        
        
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
