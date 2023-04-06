from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3

class factory_reset_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 711, 401))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(430, 30, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(360, 210, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 280, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"")
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(380, 280, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./images/nms.png"))
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(120, 90, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 150, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(120, 210, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44:09"))
        self.label_2.setText(_translate("MainWindow", "Done."))
        self.pushButton_6.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_8.setText(_translate("MainWindow", "CLOSE"))
        self.checkBox.setText(_translate("MainWindow", "Test Data Only"))
        self.checkBox_2.setText(_translate("MainWindow", "Master Data Only"))
        self.checkBox_3.setText(_translate("MainWindow", "All Data"))
        self.pushButton_8.clicked.connect(MainWindow.close)
        self.pushButton_6.clicked.connect(self.clean_data)
        self.label_2.hide() 
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
        
    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    
    def clean_data(self):
        close = QMessageBox()
        close.setText("Confirm.")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:
                if(self.checkBox.isChecked()):
                    connection = sqlite3.connect("ur.db")          
                    with connection:        
                                cursor = connection.cursor()                    
                                cursor.execute(" DELETE FROM TEST_MST")
                                cursor.execute(" DELETE FROM PATIENT_MST")
                                cursor.execute(" DELETE FROM GRAPH_MST")
                                cursor.execute(" DELETE FROM GRAPH_MST2")
                                cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('TEST_MST','PATIENT_MST','GRAPH_MST','GRAPH_MST2')")                        
                                
                    connection.commit();
                    connection.close()
                    
                    self.label_2.setText("Test Data Deleted .") 
                    self.label_2.show()
                elif(self.checkBox_2.isChecked()):
                    connection = sqlite3.connect("ur.db")          
                    with connection:        
                                cursor = connection.cursor()                    
                                cursor.execute(" DELETE FROM DOCTORS_INFO")                       
                                cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('DOCTORS_INFO')")                        
                                
                    connection.commit();
                    connection.close()
                    
                    self.label_2.setText("Master Data Deleted.") 
                    self.label_2.show()
                elif(self.checkBox_3.isChecked()):
                    connection = sqlite3.connect("ur.db")          
                    with connection:        
                                cursor = connection.cursor()                    
                                cursor.execute(" DELETE FROM TEST_MST")
                                cursor.execute(" DELETE FROM PATIENT_MST")
                                cursor.execute(" DELETE FROM GRAPH_MST")
                                cursor.execute(" DELETE FROM GRAPH_MST2")
                                cursor.execute(" DELETE FROM DOCTORS_INFO")    
                                cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('TEST_MST','PATIENT_MST','GRAPH_MST','GRAPH_MST2','DOCTORS_INFO')")                        
                                
                    connection.commit();
                    connection.close()
                    
                    self.label_2.setText("All Data Deleted.") 
                    self.label_2.show()
            
                else:
                    self.label_2.setText("Invalid.") 
                    self.label_2.show()
        else:
             print("Operation cancled.")
              


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = factory_reset_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
