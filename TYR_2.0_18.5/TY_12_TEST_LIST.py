


from PyQt5 import QtCore, QtGui, QtWidgets
from TY_01_TEST_BATCH import TY_01_Ui_MainWindow
from TY_01_TEST_BATCH_QLSS import TY_01_qlss_Ui_MainWindow
from TY_01_TEST_BATCH_ILSS import TY_01_ilss_Ui_MainWindow
from TY_01_TEST_BATCH_FLXURL import TY_01_fluxurl_Ui_MainWindow
from TY_11_START_TEST_COF import TY_11_Ui_MainWindow
from TY_22_TEST_BATCH_TENSILE_8 import TY_01_T8_Ui_MainWindow
from TY_23_START_TEST_PEELOFF import TY_23_PEELOFF_Ui_MainWindow
from TY_26_START_TEST_FOUND_BRK_TEST import TY_26_Ui_MainWindow
from TY_29_START_TEST_PROOF import ty_29_Ui_MainWindow
from TY_32_START_TEST_CYCLICK import TY_32_Ui_MainWindow
from TY_37_START_TEST_COMPRESS_02 import TY_37_Ui_MainWindow
from TY_39_START_TEST_TEAR_03 import TY_39_START_TEST_TEAR_Ui_MainWindow
from TY_40_START_TEST_WEBBING import TY_40_START_TEST_WEBBING_Ui_MainWindow
from TY_43_START_TEST_SHEAR_STRENGTH import TY_43_START_TEST_SHEAR_Ui_MainWindow
from TY_45_START_TEST_PEEL_STRENGTH import TY_45_START_TEST_PEEL_STR_Ui_MainWindow

import sqlite3
import re
import datetime
import time
import os,sys


class TY_12_LIST_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1390, 772)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1321, 709))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.frame.setFont(font)
        self.frame.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(970, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 610, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 180, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 70, 1331, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(870, 610, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(90, 90, 134);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(30, 190, 341, 481))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(153, 255, 182);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(480, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(480, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(610, 140, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(490, 20, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        
        self.label_5_1 = QtWidgets.QLabel(self.frame)
        self.label_5_1.setGeometry(QtCore.QRect(10, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5_1.setFont(font)
        self.label_5_1.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5_1.setObjectName("label_5_1")
        
        
        
        self.lineEdit = QtWidgets.QLineEdit(self.frame)        
        self.lineEdit.setGeometry(QtCore.QRect(200, 22, 220, 41))
        #self.lineEdit.setMaxLength(6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("SU")
        self.lineEdit.setStyleSheet("color: rgb(0, 120, 200);")
        self.lineEdit.setObjectName("lineEdit")
       
        
        
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(610, 340, 401, 241))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(610, 210, 401, 101))
        self.textEdit.setObjectName("textEdit")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(1050, 130, 261, 351))
        self.frame_2.setStyleSheet("background-color: rgb(196, 255, 187);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(20, 30, 181, 111))
        self.frame_3.setStyleSheet("background-color: rgb(254, 207, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(20, 170, 221, 151))
        self.frame_5.setStyleSheet("background-color: rgb(228, 244, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.hide()
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 30, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 80, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1390, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.modbus_port=""
        self.non_modbus_port=""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "05 Aug 2020 12:45:00"))
        self.pushButton_4.setText(_translate("MainWindow", "GO FOR TEST"))
        self.pushButton_14.setText(_translate("MainWindow", "RETURN"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "TENSILE"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "COMPRESSION"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "TEAR"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "FLEXURAL"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "COF"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "ILLS"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "QLSS"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(_translate("MainWindow", "Test Name :"))
        self.label_10.setText(_translate("MainWindow", "Test Details :"))
        self.label_11.setText(_translate("MainWindow", "Tensile "))
        self.label_4.setText(_translate("MainWindow", "Select Test :"))
        self.label_5.setText(_translate("MainWindow", " TESTS TYPES ( NEW TEST )"))
        self.label_5_1.setText(_translate("MainWindow", " User Name:"))
        self.pushButton_15.setText(_translate("MainWindow", "IMAGE"))
        self.radioButton.setText(_translate("MainWindow", "Non -Metal"))
        self.radioButton_2.setText(_translate("MainWindow", "Metal"))
        self.radioButton_5.setText(_translate("MainWindow", "External (Ext/Encoder)"))
        self.radioButton_6.setText(_translate("MainWindow", "Internal  (Ext/Encoder)"))
        
        self.pushButton_14.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(self.open_new_test_win)
        
        self.listWidget.doubleClicked.connect(self.selected_record)
        self.listWidget.clicked.connect(self.selected_record)
        self.radioButton.clicked.connect(self.show_extiometer_setting)
        self.radioButton_2.clicked.connect(self.show_extiometer_setting)
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  LOGIN_USER_NAME FROM GLOBAL_VAR") 
        for x in results:
            self.lineEdit.setText(str(x[0]))
        connection.close()
        
        self.load_data()
        
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
    
    def show_extiometer_setting(self):
        if(self.radioButton.isChecked()):
            self.frame_5.hide()            
        elif(self.radioButton_2.isChecked()):
            self.frame_5.show()
        else:
            self.frame_5.hide()
        
    
    def device_date(self):     
        self.label_20.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
    
    

    def load_data(self):
        self.listWidget.clear() 
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  TEST_TYPE_NAME||'('||TEST_TYPE_ID||')' FROM TEST_TYPE_MST WHERE ACTIVE_Y_N = 'Y'") 
        for x in results:
            self.listWidget.addItem(str(x[0]))
        connection.close()
        self.listWidget.setCurrentRow(0)
        self.selected_record()
        self.load_modbus_port()
    
    def selected_record(self):
        self.test_type_id=""
        self.pushButton_15.setText("")
        self.list_type=self.listWidget.currentItem().text()
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  TEST_TYPE_NAME,TEST_TYPE_DTLS,TEST_TYPE_IMG_FILE,ACTIVE_Y_N,TEST_TYPE_ID FROM TEST_TYPE_MST WHERE ACTIVE_Y_N = 'Y' and TEST_TYPE_NAME||'('||TEST_TYPE_ID||')' = '"+str(self.list_type)+"'")
        for x in results:                    
                   self.label_11.setText(str(x[0]))
                   self.textEdit.setText(str(x[1])) #ADDRESS1
                   icon = QtGui.QIcon()
                   icon.addPixmap(QtGui.QPixmap("images/"+str(str(x[2]))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                   self.pushButton_15.setIcon(icon)
                   self.pushButton_15.setIconSize(QtCore.QSize(200, 160))
                   if(str(x[3]) == 'Y'):
                       self.pushButton_15.setEnabled(True)
                       self.pushButton_4.setEnabled(True)                       
                   else:
                       self.pushButton_15.setDisabled(True)
                       self.pushButton_4.setDisabled(True)
                   self.test_type_id=str(x[4])
                   
                   if(self.label_11.text() == "TENSILE"):
                       self.frame_2.show()
                       connection = sqlite3.connect("tyr.db")
                       results=connection.execute("SELECT  IS_METAL,IS_INTERNAL_ENCODER FROM GLOBAL_VAR")
                       for x in results:
                            if(str(x[0]) == 'Y'):
                                self.radioButton_2.setChecked(True)
                                self.radioButton.setChecked(False)
                                self.frame_5.show()
                            else:
                                self.radioButton_2.setChecked(False)
                                self.radioButton.setChecked(True)
                                self.frame_5.hide()
                                
                                
                            if(str(x[1]) == 'Y'):
                                self.radioButton_5.setChecked(True)
                                self.radioButton_6.setChecked(False)
                            else:
                                self.radioButton_5.setChecked(False)
                                self.radioButton_6.setChecked(True)
                                
                       connection.close()  
                       
                       
                   else:
                       self.frame_2.hide()
                       
        connection.close()
        
        
        
    def open_new_test_win(self):
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()                   
                    if(self.radioButton_2.isChecked()):
                         cursor.execute("UPDATE GLOBAL_VAR SET IS_METAL='Y',GUAGE_EXT_FLG='Y', DEF_FLG='Y'")
                    elif(self.radioButton_5.isChecked()):
                         cursor.execute("UPDATE GLOBAL_VAR SET IS_METAL='Y',IS_INTERNAL_ENCODER='Y',GUAGE_EXT_FLG='Y', DEF_FLG='Y'")     
                    else:
                         cursor.execute("UPDATE GLOBAL_VAR SET IS_METAL='N',IS_INTERNAL_ENCODER='N',GUAGE_EXT_FLG='N', DEF_FLG='N'")
        connection.commit();
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET LOGIN_USER_NAME='"+str(self.lineEdit.text())+"'")
        connection.commit();
        connection.close()
        
        
        if(str(self.test_type_id) == "1"):
            self.save_test_tensile()
        elif(str(self.test_type_id) == "2"):
            self.save_test_compress()
        elif(str(self.test_type_id) == "3"):
            self.save_test_tear()
        elif(str(self.test_type_id) == "4"):
            self.save_test_flexural()
        elif(str(self.test_type_id) == "5"):
            self.save_test_cof()
        elif(str(self.test_type_id) == "6"):
            self.save_test_ilss()
        elif(str(self.test_type_id) == "7"):
            self.save_test_qlss ()
        elif(str(self.test_type_id) == "8"):
            self.save_test_tensile_8()
        elif(str(self.test_type_id) == "14"):
            self.save_test_peeloff()
        elif(str(self.test_type_id) == "15"):
            self.save_test_FBST()
        elif(str(self.test_type_id) == "16"):
            self.save_test_PROOF()
        elif(str(self.test_type_id) == "17"):
            self.save_test_CYCLICK()
        elif(str(self.test_type_id) == "18"):
            self.save_test_compress_2()
        elif(str(self.test_type_id) == "19"):    
            self.save_test_dot_tear_test()
        elif(str(self.test_type_id) == "20"):    
            self.save_peel_strength_test()
        elif(str(self.test_type_id) == "21"):    
            self.save_shear_strength_test()
        elif(str(self.test_type_id) == "22"):    
            self.save_test_webbing()
        else:
            print("Invalid Test ID"+str(self.test_type_id))
            
    
    def save_peel_strength_test(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Peel Strength'")                    
        connection.commit();
        connection.close()
        self.open_new_window_peel_strength()
        
    def save_shear_strength_test(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Shear Strength'")                    
        connection.commit();
        connection.close()
        self.open_new_window_shear_strength()    
    
    def save_test_webbing(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Webbing'")                    
        connection.commit();
        connection.close()
        self.open_new_window_Webbing()
        
    def save_test_tensile(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Tensile'")                    
        connection.commit();
        connection.close()
        
        
        self.open_new_window()
        
        
    def save_test_tensile_8(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='Tensile_8'")                    
        connection.commit();
        connection.close()
        
        
        self.open_new_window_tensile_8()
        
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
        self.open_new_window_flexurl()
        
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
    
    def save_test_cof(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='COF'")            
        connection.commit();
        connection.close()    
        self.open_new_window_cof()
    
    def save_test_peeloff(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='PEELOFF'")            
        connection.commit();
        connection.close()    
        self.open_new_window_peeloff()
     
    def save_test_FBST(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='FBST'")            
        connection.commit();
        connection.close()    
        self.open_new_window_FBST()
    
    def save_test_PROOF(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='PROOF'")            
        connection.commit();
        connection.close()    
        self.open_new_window_PROOF()
    
    
    def save_test_CYCLICK(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='CYCLICK'")            
        connection.commit();
        connection.close()    
        self.open_new_window_CYCLICK()
    
    def save_test_compress_2(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='COMPRESS_2'")            
        connection.commit();
        connection.close()    
        self.open_new_window_COMPRESS_2()
    
    def save_test_dot_tear_test(self):                     
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE GLOBAL_VAR SET NEW_TEST_NAME='DOT_TEAR_TEST'")            
        connection.commit();
        connection.close()    
        self.open_new_window_DOT_TEAR_TEST()
        


   
    
    def open_new_window_peel_strength(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_45_START_TEST_PEEL_STR_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_shear_strength(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_43_START_TEST_SHEAR_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()    
    
        
    def open_new_window_FBST(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_26_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()    
    
    
    def open_new_window_peeloff(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_23_PEELOFF_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()    
    
    
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
    
    def open_new_window_flexurl(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_01_fluxurl_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_cof(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_11_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window_tensile_8(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_01_T8_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    def open_new_window_PROOF(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=ty_29_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_CYCLICK(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_32_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_COMPRESS_2(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_37_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_DOT_TEAR_TEST(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_39_START_TEST_TEAR_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
    
    def open_new_window_Webbing(self):                
        self.window = QtWidgets.QMainWindow()
        self.ui=TY_40_START_TEST_WEBBING_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
    
    def get_USB_0_DEVICE(self):
        os.system("rm -rf lsusb_USB0.txt")
        port_type="ERROR"
        
        ### Check for Controller #######
        os.system("udevadm info /dev/ttyUSB0 | grep PL2303 >> lsusb_USB0.txt")
        try:
           f = open('lsusb_USB0.txt','r')
           for line in f:
               cnt=0                
               cnt=int(line.find("PL2303")) ## For controller Port
               if cnt > 0 :
                    port_type="C"
               else:
                    port_type="ERROR"  
                   
           f.close()
        except:          
             port_type="ERROR"     
        
        
        if(port_type == "ERROR"):
        
                #### Check For Modbus ########
                os.system("udevadm info /dev/ttyUSB0 | grep Future >> lsusb_USB0.txt")
                try:
                   f = open('lsusb_USB0.txt','r')
                   for line in f:
                       cnt=0                
                       cnt=int(line.find("Future")) ## For controller Port
                       if cnt > 0 :
                            port_type="M"
                       else:
                            port_type="ERROR"     
                   f.close()
                except:          
                      port_type="ERROR"
                   
         
        return port_type
    
    
    def get_USB_1_DEVICE(self):
        os.system("rm -rf lsusb_USB1.txt")
        port_type="ERROR"
        
        ### Check for Controller #######
        os.system("udevadm info /dev/ttyUSB1 | grep PL2303 >> lsusb_USB1.txt")
        try:
           f = open('lsusb_USB1.txt','r')
           for line in f:
               cnt=0                
               cnt=int(line.find("PL2303")) ## For controller Port
               if cnt > 0 :
                    port_type="C"
               else:
                    port_type="ERROR"  
                   
           f.close()
        except:          
             port_type="ERROR"     
        
        
        if(port_type == "ERROR"):
        
                #### Check For Modbus ########
                os.system("udevadm info /dev/ttyUSB1 | grep Future >> lsusb_USB1.txt")
                try:
                   f = open('lsusb_USB1.txt','r')
                   for line in f:
                       cnt=0                
                       cnt=int(line.find("Future")) ## For controller Port
                       if cnt > 0 :
                            port_type="M"
                       else:
                            port_type="ERROR"     
                   f.close()
                except:          
                      port_type="ERROR"
                   
         
        return port_type
        
    def load_modbus_port(self):
        self.modbus_port=""
        self.non_modbus_port=""
        self.port=""        
        connection = sqlite3.connect("tyr.db") 
        results=connection.execute("SELECT ISACTIVE_MODBUS FROM SETTING_MST") 
        for x in results:
                   if(str(x[0]) == 'Y'):                       
                        self.port=self.get_USB_0_DEVICE()
                        print("USB0: "+str(self.port))
                        if(self.port == "C"):
                             self.non_modbus_port="/dev/ttyUSB0"
                        elif(self.port == "M"):
                             self.modbus_port="/dev/ttyUSB0"
                        else:                             
                             print("Error 468")  
                            
                        
                        print("USB0: "+str(self.port)+" non_modbus: "+(self.non_modbus_port))     
                        
                        self.port=self.get_USB_1_DEVICE()
                        
                        if(self.port == "C"):
                             self.non_modbus_port="/dev/ttyUSB1"
                        elif(self.port == "M"):
                             self.modbus_port="/dev/ttyUSB1"
                        else:
                             print("Error 480")        
                   else:
                         print("Modbus Flag :"+str(x[0]))                       
        connection.close()
        
        connection = sqlite3.connect("tyr.db")              
        with connection:        
                    cursor = connection.cursor()
                    cursor.execute("UPDATE SETTING_MST SET MODBUS_PORT='"+str(self.modbus_port)+"',NON_MODBUS_PORT='"+str(self.non_modbus_port)+"'")            
        connection.commit();


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_12_LIST_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
