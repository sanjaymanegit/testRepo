# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TY_00_TEST_TYPES.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from TY_01_TEST_BATCH import TY_01_Ui_MainWindow
from TY_01_TEST_BATCH_QLSS import TY_01_qlss_Ui_MainWindow
from TY_01_TEST_BATCH_ILSS import TY_01_ilss_Ui_MainWindow

import sqlite3

class TY_00_T_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1367, 768)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1281, 709))
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 90, 201, 181))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/tensile2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(200, 160))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 90, 191, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/compress.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(200, 160))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(840, 90, 191, 181))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/tear.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(200, 160))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 350, 191, 181))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/flexural.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(200, 160))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(530, 600, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        
        
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 350, 191, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setText("Shear \n QLSS")
        self.pushButton_6.setStyleSheet("background-color: rgb(70,130,180);")
        '''
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/shear_qlss.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(200, 160))
        '''
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(840, 350, 191, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setText("Shear \n ILSS")
        self.pushButton_7.setStyleSheet("background-color: rgb(70,130,180);")
        
        self.pushButton_7.setObjectName("pushButton_7")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reports"))
        self.pushButton_5.setText(_translate("MainWindow", "Return"))
        
        self.pushButton_5.clicked.connect(MainWindow.close)        
        self.pushButton.clicked.connect(self.save_test_tensile)
        self.pushButton_2.clicked.connect(self.save_test_compress)
        #self.pushButton_2.setDisabled(True)        
        self.pushButton_3.clicked.connect(self.save_test_tear)
        #self.pushButton_3.setDisabled(True)
        self.pushButton_4.clicked.connect(self.save_test_flexural)
        self.pushButton_6.clicked.connect(self.save_test_qlss)
        self.pushButton_7.clicked.connect(self.save_test_ilss) 
        self.pushButton_4.setDisabled(True)
        self.load_data()
   
    def load_data(self):      
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT TENSILE_TEST_FLG,COMPRESS_TEST_FLG,TARE_TEST_FLG,flexural_test,QLSS_TEST,ILSS_TEST  FROM GLOBAL_VAR") 
        for x in results:            
            if(str(x[0])=='ACTIVE'):
                self.pushButton.setEnabled(True)
            else:
                self.pushButton.setEnabled(False)
                
            if(str(x[1])=='ACTIVE'):
                self.pushButton_2.setEnabled(True)
            else:
                self.pushButton_2.setEnabled(False) 
                
            if(str(x[2])=='ACTIVE'):
                self.pushButton_3.setEnabled(True)
            else:
                self.pushButton_3.setEnabled(False)    
             
             
            if(str(x[3])=='ACTIVE'):
                self.pushButton_4.setEnabled(True)
            else:
                self.pushButton_4.setEnabled(False)
                
            
            if(str(x[4])=='ACTIVE'):
                self.pushButton_6.setEnabled(True)
            else:
                self.pushButton_6.setEnabled(False)    
             
             
            if(str(x[5])=='ACTIVE'):
                self.pushButton_7.setEnabled(True)
            else:
                self.pushButton_7.setEnabled(False)   
                
        connection.close()
        #self.label_3.hide()
        
        
    def save_test_tensile(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Tensile'")            
        connection.commit();
        connection.close()    
        self.open_new_window()
        
    def save_test_compress(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Compress'")            
        connection.commit();
        connection.close()    
        self.open_new_window()
        
        
    def save_test_tear(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Tear'")            
        connection.commit();
        connection.close()    
        self.open_new_window()
        
    def save_test_flexural(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Flexural'")            
        connection.commit();
        connection.close()    
        self.open_new_window()
        
    def save_test_qlss(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='QLSS'")            
        connection.commit();
        connection.close()    
        self.open_new_window_qlss()
    
    def save_test_ilss(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='ILSS'")            
        connection.commit();
        connection.close()    
        self.open_new_window_ilss()
        
    def open_new_window(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_01_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
   

    def open_new_window_qlss(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_01_qlss_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_ilss(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_01_ilss_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_00_T_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
