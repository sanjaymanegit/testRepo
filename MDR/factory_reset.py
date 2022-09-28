# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop_factory_reset.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

import sqlite3

class factory_reset_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)        
        self.frame.setGeometry(QtCore.QRect(40, 30, 521, 281))
        #self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(100, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 210, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(350, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(160, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(160, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        #font.setBold(True)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Delete Now"))
        self.pushButton_3.setText(_translate("MainWindow", "Close"))        
        self.label_4.setText(_translate("MainWindow", "Deleted Data Succefully."))
        self.label_4.hide()
        self.checkBox.setText(_translate("MainWindow", "All - Test Data"))
        self.checkBox_2.setText(_translate("MainWindow", "All - Methods Data"))
        self.label_5.setText(_translate("MainWindow", "Factory Reset"))
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.delete_data)
        
        
    
    def delete_data(self):
        
        if(self.checkBox.isChecked()):
                    close = QMessageBox()
                    close.setText("Are you sure want to delete selected Test data ? Please confirm. ")
                    close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                    close = close.exec()
                    if close == QMessageBox.Yes:
                            connection = sqlite3.connect("mdr.db")            
                            with connection:        
                                    cursor = connection.cursor()       
                                    cursor.execute("DELETE FROM TEST_MST_MDR")                    
                                    cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('TEST_MST_MDR')")                    
                            connection.commit();
                            connection.close()
                            print("ok - Deleted Test Data  ")
                            self.label_4.show()
                    else:
                            print("validation Error 114")
                  
        if(self.checkBox_2.isChecked()):            
                    close = QMessageBox()
                    close.setText("Are you sure want to delete selected Methods data ? Please confirm. ")
                    close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                    close = close.exec()
                    if close == QMessageBox.Yes:
                            connection = sqlite3.connect("mdr.db")
                            with connection:        
                                    cursor = connection.cursor()       
                                    cursor.execute("DELETE FROM METHODS_MST")
                                    cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name in ('METHODS_MST')")
                                    
                            connection.commit();
                            connection.close()
                            print("ok - Deleted all Methods Data  ")
                            self.label_4.show()
                    else:
                            print("validation Error 133")
        else:
                print("validation Error")
    
    
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = factory_reset_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
