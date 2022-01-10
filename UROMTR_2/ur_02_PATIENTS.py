# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ur_02_PATIENTS.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from ur_03_REPORT import ur_03_Ui_MainWindow
import datetime
import sqlite3
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class ur_02_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 631)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(30, 30, 611, 561))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.frame.setFont(font)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.save_type="New"
        self.p_id="0"
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 500, 109, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(140, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 500, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(20, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(330, 20, 90, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("")
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)
        self.lineEdit.setValidator(input_validator)        
        self.lineEdit.setGeometry(QtCore.QRect(410, 20, 91, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(20, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("")
        self.label_33.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(110, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("")
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        
        
        self.label_34_1 = QtWidgets.QLabel(self.frame)
        self.label_34_1.setGeometry(QtCore.QRect(220, 60, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_34_1.setFont(font)
        #self.label_34_1.setText("Error:255 fdgdfg dfgdfg ")
        self.label_34_1.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_34_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_34_1.setObjectName("label_34_1")
        
        
        
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(20, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("")
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 110, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 110, 91, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 110, 141, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(20, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("")
        self.label_36.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_36.setObjectName("label_36")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(100, 160, 82, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(230, 160, 82, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(20, 210, 51, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("")
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 210, 131, 31))
       
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(320, 230, 296, 183))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_38 = QtWidgets.QLabel(self.frame)
        self.label_38.setGeometry(QtCore.QRect(30, 270, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("")
        self.label_38.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.frame)
        self.label_39.setGeometry(QtCore.QRect(120, 270, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("")
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame)
        self.label_40.setGeometry(QtCore.QRect(30, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("")
        self.label_40.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(98, 110, 61, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 330, 241, 31))
        self.comboBox_2.setObjectName("comboBox_2")
       
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(30, 380, 221, 41))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 440, 291, 31))
        
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_41 = QtWidgets.QLabel(self.frame)
        self.label_41.setGeometry(QtCore.QRect(30, 440, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("")
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 21))
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
        self.pushButton_3.setText(_translate("MainWindow", "Close"))
        #self.label_30.setText(_translate("MainWindow", "16 Jan 2020 12:14:15"))
        self.label_30.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        self.pushButton_7.setText(_translate("MainWindow", "Save and Procced"))
        self.pushButton_7.setDisabled(True)
        self.label_31.setText(_translate("MainWindow", "Test Created On :"))
        self.label_32.setText(_translate("MainWindow", "Patients Id:"))
        self.pushButton_4.setText(_translate("MainWindow", "Search"))
        self.label_33.setText(_translate("MainWindow", "Patients Id:"))
        self.label_34.setText(_translate("MainWindow", "000001"))
        self.label_35.setText(_translate("MainWindow", "Name :"))
        self.label_36.setText(_translate("MainWindow", "Gender  :"))
        self.radioButton.setText(_translate("MainWindow", "Male"))
        self.radioButton.setChecked(True)
        self.radioButton_2.setText(_translate("MainWindow", "Female"))
        self.radioButton_2.setChecked(False)
        self.label_37.setText(_translate("MainWindow", "DOB :"))
        self.pushButton_5.setText(_translate("MainWindow", "Date"))
        self.label_38.setText(_translate("MainWindow", "Age (Yrs):"))
        self.label_39.setText(_translate("MainWindow", "0"))
        self.label_40.setText(_translate("MainWindow", "Doctors Name :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Mr."))
        self.comboBox.setItemText(1, _translate("MainWindow", "Mrs."))
        self.comboBox.setItemText(2, _translate("MainWindow", "Miss."))
        self.comboBox.setItemText(3, _translate("MainWindow", "Cap."))
        self.comboBox.setItemText(4, _translate("MainWindow", "Shri."))
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, _translate("MainWindow", "---Select Doctor ---"))
        self.comboBox_2.currentTextChanged.connect(self.onchage_combo)
        self.lineEdit_6.textChanged.connect(self.onchage_combo)
        self.checkBox.setText(_translate("MainWindow", "Doctor Name not in  above List"))
        self.checkBox.setChecked(False)
        self.lineEdit_6.setDisabled(True)
        #self.lineEdit_5.setDisabled(True)
        self.label_41.setText(_translate("MainWindow", "Doctors Name :"))
        self.pushButton_7.clicked.connect(self.open_new_window)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_5.clicked.connect(self.DOB_on_click)
        self.checkBox.clicked.connect(self.doctors_name_on_click)
        self.pushButton_4.clicked.connect(self.fetch_data)
        self.calendarWidget.hide()
        self.default_dates()
        
        self.calendarWidget.clicked.connect(self.calendar_on_click)
        self.load_data()
        '''
        self.lineEdit.setText("search")
        self.lineEdit_2.setText("f name")
        self.lineEdit_3.setText("m name")
        self.lineEdit_4.setText("l name")
        self.lineEdit_5.setText("dob")
        '''
    def onchage_combo(self):
        self.pushButton_7.setEnabled(True)
         
    def load_data(self):
        connection = sqlite3.connect("ur.db")
        results=connection.execute("select seq+1 from sqlite_sequence where name = 'PATIENT_MST'")
        for x in results:           
                 self.label_34.setText(str(x[0]).zfill(7))
                 self.p_id=str(x[0])
                 
        '''
        rows=results.fetchall() 
        self.label_34.setText(str(rows[0][0]).zfill(7))
        self.p_id=str(rows[0][0])
        '''
        connection.close()
        self.i=1
        self.dr_id_arr=["None"]
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT 'Dr.'||fname||' '||mname||' '||lname||'('||DR_QUAL||')',DR_ID FROM DOCTORS_INFO") 
        for x in results:            
            self.comboBox_2.addItem("")
            self.dr_id_arr.append(str(x[1]))
            self.comboBox_2.setItemText(self.i,str(x[0]))
            self.i=self.i+1
        connection.close()
        
    def fetch_data(self):
        self.dr_id=""
        self.pcnt=0
        if(self.lineEdit.text() != ""):
            connection = sqlite3.connect("ur.db")
            results=connection.execute("SELECT NAME_INITIALS,F_NAME,M_NAME,L_NAME,GENDER,AGE,DOB_STR,P_ID  FROM PATIENT_MST WHERE P_ID = '"+str(int(self.lineEdit.text()))+"'") 
            for x in results:
                self.lineEdit_2.setText(str(x[1]))
                self.lineEdit_3.setText(str(x[2]))
                self.lineEdit_4.setText(str(x[3]))
                self.label_39.setText(str(x[5]))
                self.lineEdit_5.setText(str(x[6]))
                self.label_34.setText(str(x[7]).zfill(7))
                self.pcnt=self.pcnt+1
                self.save_type="Exisitng"
            connection.close()
        if(int(self.pcnt) == 0):
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
        
        
        
    def doctors_name_on_click(self):
        if not (self.checkBox.isChecked()):
            self.lineEdit_6.setDisabled(True)
            self.comboBox_2.setEnabled(True)
        else:
            self.lineEdit_6.setEnabled(True)
            self.comboBox_2.setDisabled(True)
            
    def DOB_on_click(self):
        self.calendarWidget.show()
    
    def calendar_on_click(self): 
        self.lineEdit_5.setText(str(self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)))
        self.calendarWidget.hide()
        self.age_calc()
        
    def age_calc(self):        
        bod_date=str(self.lineEdit_5.text())
        print("bod_date :"+str(bod_date))      
        b_date = datetime.datetime.strptime(bod_date, '%Y-%m-%d')
        print ("Age : %d" % ((datetime.datetime.today() - b_date).days/365))
        self.label_39.setText(str("%d" % ((datetime.datetime.today() - b_date).days/365)))
    
    def default_dates(self):               
        self.lineEdit_5.setText(str(QDate.currentDate().toString(QtCore.Qt.ISODate)))
        
    
    def open_new_window(self):
        self.label_34_1.hide()
        print("Age :"+str(int(self.label_39.text())))
        if(self.lineEdit_2.text()==""):
               self.label_34_1.setText("Error: First Name should not empty")
               self.label_34_1.show()
        elif(self.lineEdit_4.text()==""):
               self.label_34_1.setText("Error: Last Name should not empty")
               self.label_34_1.show()
        elif(str(self.label_39.text()) == "0"):
               self.label_34_1.setText("Error: Age Should be greater than 0")
               self.label_34_1.show()       
        else:
            self.save_data()        
            self.window = QtWidgets.QMainWindow()
            #self.window=myWindow()
            self.ui=ur_03_Ui_MainWindow()
            self.ui.setupUi(self.window)           
            self.window.show()
            
        
    def save_data(self):
        if(self.lineEdit_2.text() != "" and  self.lineEdit_4.text() != ""):
                print(" self.save_type :"+str(self.save_type))
                self.intials=self.comboBox.currentText()
                self.f_name=self.lineEdit_2.text()
                self.m_name=self.lineEdit_3.text()
                self.l_name=self.lineEdit_4.text()
                self.p_id=str(int(self.label_34.text()))
                if(self.radioButton_2.isChecked()):
                    self.gender="Female"
                else:
                    self.gender="Male"
                    
                self.age=self.label_39.text()
                self.dob_str=self.lineEdit_5.text()
                self.last_test_id=self.label_34.text()
                
                if(self.save_type == "New"):
                            connection = sqlite3.connect("ur.db")              
                            with connection:        
                                  cursor = connection.cursor()                                
                                  cursor.execute("insert INTO PATIENT_MST (NAME_INITIALS,F_NAME,M_NAME,L_NAME,GENDER,AGE,DOB_STR,LAST_TEST_ID) VALUES ('"+self.intials+"','"+self.f_name+"','"+self.m_name+"','"+self.l_name+"','"+self.gender+"','"+self.age+"','"+self.dob_str+"','"+self.last_test_id+"')")                                
                            connection.commit();
                            connection.close()
                else:           
                            connection = sqlite3.connect("ur.db")              
                            with connection:        
                                  cursor = connection.cursor()                                
                                  cursor.execute("UPDATE PATIENT_MST SET NAME_INITIALS='"+self.intials+"',F_NAME='"+self.f_name+"',M_NAME='"+self.m_name+"',L_NAME='"+self.l_name+"',GENDER='"+self.gender+"',AGE='"+self.age+"',DOB_STR='"+self.dob_str+"',LAST_TEST_ID='"+self.last_test_id+"' where P_ID='"+str(self.p_id)+"'")
                            connection.commit();
                            connection.close()     
                                
               
                connection = sqlite3.connect("ur.db")              
                with connection:        
                        cursor = connection.cursor()
                        if(self.checkBox.isChecked()):  
                            cursor.execute("UPDATE GLOBAL_VAR_TEST SET   p_id='"+str(self.label_34.text())+"',  DR_NAME='"+str(self.lineEdit_6.text())+"'")
                        else:
                            cursor.execute("UPDATE GLOBAL_VAR_TEST SET   p_id='"+str(self.label_34.text())+"', DR_NAME='"+str(self.comboBox_2.currentText())+"'")                          
                connection.commit();
                connection.close()
                 
                ## load test_mst 
                ## load graph_mst ,graph_mst2 tables
                ##UPDATE graph_mst , graph_mst2, test_mst for graphi_id
                connection = sqlite3.connect("ur.db")              
                with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("INSERT INTO TEST_MST(DR_NAME,TEST_START_ON,TEST_END_ON,ELAPSED_TIME,MAX_FLOW,MAX_FLOW_DEV,"+
                                       "AVG_FLOW,AVG_FLOW_DEV,VOIDING_TIME,VOIDING_TIME_DEV,FLOW_TIME,TIME_TO_MAX_FLOW,TIME_TO_MAX_FLOW_DEV,"+
                                       "VOIDED_VOL,FLOW_AT_2_SEC,ACCEL,VOLUMN_TIME_X,VOLUMN_TIME_Y,FLOW_TIME_X,FLOW_TIME_Y,TOTAL_VOLUMN,P_ID,HESITANCY_TIME) "+
                                       "SELECT DR_NAME,TEST_START_ON,TEST_END_ON,ELAPSED_TIME,MAX_FLOW,MAX_FLOW_DEV,AVG_FLOW,AVG_FLOW_DEV,VOIDING_TIME,"+
                                       "VOIDING_TIME_DEV,FLOW_TIME,TIME_TO_MAX_FLOW,TIME_TO_MAX_FLOW_DEV,VOIDED_VOL,FLOW_AT_2_SEC,ACCEL,VOLUMN_TIME_X,"+
                                       "VOLUMN_TIME_Y,FLOW_TIME_X,FLOW_TIME_Y,TOTAL_VOLUMN,P_ID,HESITANCY_TIME FROM GLOBAL_VAR_TEST")
                connection.commit();
                connection.close()
                print("TEST_MST - Populated.")
                connection = sqlite3.connect("ur.db")              
                with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("INSERT INTO GRAPH_MST(X_NUM,Y_NUM) SELECT X_NUM,Y_NUM FROM GRAPH_MST_TMP")
                        cursor.execute("INSERT INTO GRAPH_MST2(X_NUM,Y_NUM) SELECT X_NUM,Y_NUM FROM GRAPH_MST_TMP2")
                connection.commit();
                connection.close()
                print("GRAPH_MST,GRAPH_MST2 - Populated.") 
                 
                connection = sqlite3.connect("ur.db")
                results=connection.execute("SELECT IFNULL(max(GRAPHI_ID),0)+1 FROM GRAPH_MST") 
                for x in results:
                    self.graph_id=str(x[0])                   
                connection.close()
                connection = sqlite3.connect("ur.db")
                results=connection.execute("SELECT IFNULL(max(GRAPHI_ID),0)+1 FROM GRAPH_MST2") 
                for x in results:
                    self.graph_id2=str(x[0])
                connection.close()
                #print("item index :"+str(self.comboBox_2.currentIndex()))
                print("item data :"+str(self.comboBox_2.itemData(0)))
                #print("item text :"+str(self.comboBox_2.currentIndex()))
                if(self.checkBox.isChecked()):
                    self.dr_id=0
                    self.dr_name=self.lineEdit_6.text()
                else:
                    print(" array :"+str(self.dr_id_arr))
                    print("self.comboBox_2.currentIndex :"+str(self.comboBox_2.currentIndex()))
                    self.dr_id=str(self.dr_id_arr[self.comboBox_2.currentIndex()])
                    self.dr_name=self.comboBox_2.currentText()
                print("self.dr_id :"+str(self.dr_id))
                connection = sqlite3.connect("ur.db")              
                with connection:        
                        cursor = connection.cursor()                
                        cursor.execute("UPDATE GRAPH_MST SET GRAPHI_ID='"+str(self.graph_id)+"' WHERE GRAPHI_ID IS NULL")
                        cursor.execute("UPDATE GRAPH_MST2 SET GRAPHI_ID='"+str(self.graph_id2)+"' WHERE GRAPHI_ID IS NULL")
                        cursor.execute("UPDATE TEST_MST SET GRAPHI_ID='"+str(self.graph_id)+"',  GRAPHI_ID2='"+str(self.graph_id2)+"', DR_ID='"+str(self.dr_id)+"', DR_NAME='"+self.dr_name+"' WHERE TEST_ID  in (SELECT MAX(TEST_ID) FROM TEST_MST)")
                connection.commit();
                connection.close()
                
                print("GRAPH_MST,GRAPH_MST2,TEST_MST - updated with graph id :"+str(self.graph_id)+" graph id 2:"+str(self.graph_id2)) 
                print("data saved")
        else:
                print(" Names are required.")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ur_02_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
