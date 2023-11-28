
from pop_graph_data import pop_graph_data_Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.Qt import QTableWidgetItem
import sqlite3

## This lib is for Graph only 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import re


class pop_peal_val_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1357, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1321, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 111, 501))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(2)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 0, 127);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(1060, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(740, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(1190, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(930, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(140, 60, 1161, 501))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1357, 21))
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
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Graph Id : 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Graph Id : 2"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Graph Id :3"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Please Select Graph id to view Data set"))
        self.pushButton.setText(_translate("MainWindow", "Graph Data"))
        self.pushButton_2.setText(_translate("MainWindow", "Save Changes "))
        #self.pushButton_2.setDisabled(True)
        self.pushButton_3.setText(_translate("MainWindow", "Re-Calculate Results"))
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setText(_translate("MainWindow", "Close"))
        self.pushButton_5.setText(_translate("MainWindow", "Refresh"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Peak Value"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ignore Flag"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Test Method"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Comment"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1.00"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "1.00"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "2.00"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "3.00"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "4.00"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        
        self.load_data()
        self.listWidget.doubleClicked.connect(self.show_single_graph_data)
        self.pushButton_4.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.open_graph_data)
        self.pushButton_5.clicked.connect(self.show_single_graph_data)
        #self.tableWidget.itemClicked.connect(self.itemclick_fun)
        self.pushButton_2.clicked.connect(self.save_ignore_flg)        
        self.show_single_graph_data()
        
    
    def load_data(self):
        self.i=0
        self.g=[]
        self.listWidget.clear() 
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT  DISTINCT GRAPH_ID FROM TEST_DATA WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
        for x in results:
            self.g.append(int(x[0]))
            self.i=self.i+1            
            self.listWidget.addItem("Specimen No: ("+str(self.i)+")")
        connection.close()
        self.listWidget.setCurrentRow(0)
        #self.show_single_graph_data()
    
    def open_graph_data(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=pop_graph_data_Ui_MainWindow()
        self.ui.setupUi(self.window)           
        self.window.show()
        
     
        
    def save_ignore_flg(self):
        i = self.tableWidget.rowCount()       
        while (i > 0):
            i=i-1
            item = self.tableWidget.item(i, 2)
            item_2 = self.tableWidget.item(i, 0)
            #print("test id  :"+str(item.text()))
            currentState = item.checkState()
            if(currentState == QtCore.Qt.Checked):
                    print("Checked test ID:"+str(item.text()))
                    connection = sqlite3.connect("tyr.db")          
                    with connection:        
                            cursor = connection.cursor()
                            print("UPDATE PEAK_MST set IGNORE_FLG='Y' WHERE SQ_NO='"+str(item.text())+"' AND PEAk_LIST_ID IN (SELECT MAX(PEAK_LIST_ID) FROM TEST_DATA WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM GLOBAL_VAR2))")
                            cursor.execute("UPDATE PEAK_MST set IGNORE_FLG='Y',COMMENT='Updated - By App' WHERE SQ_NO='"+str(item_2.text())+"' AND PEAk_LIST_ID IN (SELECT MAX(PEAK_LIST_ID) FROM TEST_DATA WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM GLOBAL_VAR2))")
                            self.pushButton_3.setEnabled(True)
                    connection.commit();
                    connection.close()                    
            else:
                    print("Un-Checked test ID:"+str(item.text()))
                    connection = sqlite3.connect("tyr.db")          
                    with connection:        
                            cursor = connection.cursor()
                            
                            cursor.execute("UPDATE PEAK_MST set IGNORE_FLG='N' WHERE SQ_NO='"+str(item_2.text())+"' AND PEAk_LIST_ID IN (SELECT MAX(PEAK_LIST_ID) FROM TEST_DATA WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM GLOBAL_VAR2))")
                    connection.commit();
                    connection.close()
        self.show_grid_data()
    
    def show_single_graph_data(self):        
        #print("inside tear list.....")
        self.delete_all_records()
        row = self.listWidget.currentRow()
        print("Current row :"+str(row))        
        if(row > -1):
                    
                    connection = sqlite3.connect("tyr.db")              
                    with connection:        
                       cursor = connection.cursor()                
                       cursor.execute("UPDATE GLOBAL_VAR2 SET GRAPH_ID='"+str(self.g[row])+"'")                                   
                    connection.commit();
                    
                    self.show_grid_data()
                    
                    self.sc_data =PlotCanvas(self,width=8, height=5,dpi=90)    
                    self.gridLayout.addWidget(self.sc_data, 0, 1, 1, 1)
                    
                    
        else:
            print("Please select Graph Id")
    
    
    
    
    def show_grid_data(self):
        self.delete_all_records()
        self.tableWidget.setColumnCount(5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
                    
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setHorizontalHeaderLabels(['ID','Peak Val','Ignored[Y/N]','Test Method','Comment'])  
                          
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 90)
        self.tableWidget.setColumnWidth(4, 200)
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SQ_NO,printf(\"%.2f\", PEAK_VAL),IGNORE_FLG,TEST_METHOD_TYPE,IFNULL(COMMENT,'') FROM PEAK_MST WHERE PEAk_LIST_ID IN (SELECT MAX(PEAK_LIST_ID) FROM TEST_DATA WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM GLOBAL_VAR2)) ")
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                            if(int(column_number) == 2):
                                #print("data:"+str(data))
                                item = QtWidgets.QTableWidgetItem()
                                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                                if(str(data) == 'Y'):
                                    item.setCheckState(QtCore.Qt.Checked)
                                else:
                                    item.setCheckState(QtCore.Qt.Unchecked)
                                item.setText(str(data))
                                self.tableWidget.setItem(row_number,column_number,item)
                                #self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                            else:
                                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data)))
                               
                    #self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        connection.close()        
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)

    
    def save_calcualtions(self):        
        self.graph_id=""
        self.test_id=""
        self.test_calc_method=""
        
        row = self.listWidget.currentRow()
        print("Current row :"+str(row)+"  Graph ID :"+str(g[row]))
        self.graph_id=str(self.g[row])
        
        
        results=connection.execute("SELECT TEST_METHOD_TYPE FROM PEAK_MST WHERE GRAPH_ID = '"+str(self.graph_id)+"' LIMIT 1")
        for x in results:
              self.test_calc_method=str(x[0])              
        connection.close()
        
        
        
        
        if(str(self.test_calc_method) == "Method A"):
                   self.test_method_A_calc()
        elif(str(self.test_calc_method) == "Method B"):
                   self.test_method_B_calc()
        elif(str(self.test_calc_method) == "Method C"):
                   self.test_method_C_calc()
        elif(str(self.test_calc_method) == "Method D"): 
                   self.test_method_D_calc()
        elif(str(self.test_calc_method) == "Method E"): 
                   self.test_method_E_calc() 
        else:
                   self.test_method_A_calc()
    
    def test_method_A_calc(self):
        self.load_vals_A=[]        
        self.med = 0
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT PEAK_VALUE FROM PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"' order by ID ASC")
        for x in results:
              self.load_vals_A.append(float(x[0]))              
        connection.close()
        try:
            self.med = statistics.median(self.load_vals_A)
        except Exception as e:
                             print("median Error :"+str(e))   
        print("Median A :"+str(self.med))
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        cursor.execute("UPDATE TEST_DATA SET MEDIAN = '"+str(self.med)+"' WHERE GRAPH_ID = '"+str(self.graph_id)+"'")                          
                        cursor.execute("UPDATE TEST_DATA SET RANGE_FROM = (SELECT MIN(PEAK_VALUE) FROM PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"'  AND IGNORE_FLG = 'N' ) WHERE GRAPH_ID = '"+str(self.graph_id)+"'")
                        cursor.execute("UPDATE TEST_DATA SET RANGE_TO = (SELECT MAX(PEAK_VALUE) FROM PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"'  AND IGNORE_FLG = 'N' ) WHERE GRAPH_ID = '"+str(self.graph_id)+"'")
                  except Exception as e:
                           print("SQL Error- test_method_A_calc() :"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()                   
        
    def test_method_B_calc(self):
        self.load_vals_B=[]
        self.time_vals_B=[]
        self.t1=0
        self.t2=0
        self.time_diff=0
        self.med = 0
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TIME_VAL FROM PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"' AND SQ_NO = 1")
        for x in results:
              self.t1=(float(x[0]))              
        connection.close() 
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TIME_VAL FROM PEAK_MST  WHERE GRAPH_ID ='"+str(self.graph_id)+"' order by SQ_NO DESC LIMIT 1")
        for x in results:
              self.t2=(float(x[0]))              
        connection.close() 
        
        self.time_diff=(self.t2)-(self.t1)
        self.t1=(self.t1)+(0.1*(self.time_diff))
        self.t2=(self.t2)-(0.1*(self.time_diff))
        
        
        connection = sqlite3.connect("tyr.db")
        #print("SELECT PEAK_VALUE FROM PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"' AND TIME_VAL BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' order by ID ASC")
        
        results=connection.execute("SELECT PEAK_VALUE FROM STG_PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"' TIME_VAL BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' order by ID ASC")
        for x in results:
              self.load_vals_B.append(float(x[0]))              
        connection.close()   
        
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        print("UPDATE PEAK_MST SET COMMENT  = 'IGNORED BY 10PER',IGNORE_FLG='Y' WHERE TIME_VAL NOT BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' AND GRAPH_ID ='"+str(self.graph_id)+"'")              
                        cursor.execute("UPDATE PEAK_MST SET COMMENT  = 'IGNORED BY 10PER',IGNORE_FLG='Y' WHERE TIME_VAL NOT BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' AND GRAPH_ID ='"+str(self.graph_id)+"'")
                        
                  except Exception as e:
                           print("SQL Error- Update:"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()
        
        
        self.med = statistics.median(self.load_vals_B)
        print("Median A :"+str(self.med))
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        cursor.execute("UPDATE TEST_DATA SET MEDIAN = '"+str(self.med)+"' WHERE GRAPH_ID ='"+str(self.graph_id)+"' ")                          
                        cursor.execute("UPDATE TEST_DATA SET RANGE_FROM = (SELECT MIN(PEAK_VALUE) FROM PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"'  AND IGNORE_FLG = 'N') WHERE GRAPH_ID ='"+str(self.graph_id)+"' ")
                        cursor.execute("UPDATE TEST_DATA SET RANGE_TO = (SELECT MAX(PEAK_VALUE) FROM PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"'  AND IGNORE_FLG = 'N') WHERE GRAPH_ID ='"+str(self.graph_id)+"' ")
                  except Exception as e:
                           print("SQL Error- test_method_B_calc() :"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()
        
        
    def test_method_C_calc(self):
        self.load_vals_B=[]
        self.time_vals_B=[]
        self.t1=0
        self.t2=0
        self.time_diff=0
        self.med = 0
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TIME_VAL FROM PEAK_MST WHERE SQ_NO = 1  AND GRAPH_ID ='"+str(self.graph_id)+"'  AND IGNORE_FLG = 'N'")
        for x in results:
              self.t1=(float(x[0]))              
        connection.close() 
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT TIME_VAL FROM PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"'  AND IGNORE_FLG = 'N' order by ID DESC LIMIT 1")
        for x in results:
              self.t2=(float(x[0]))              
        connection.close() 
        
        self.time_diff=(self.t2)-(self.t1)
        self.t1=(self.t1)+(0.1*(self.time_diff))
        self.t2=(self.t2)-(0.1*(self.time_diff))
        
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT PEAK_VALUE FROM PEAK_MST WHERE TIME_VAL BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' AND GRAPH_ID ='"+str(self.graph_id)+"'  AND IGNORE_FLG = 'N' order by ID ASC")
        for x in results:
              self.load_vals_B.append(float(x[0]))              
        connection.close()   
        
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        cursor.execute("UPDATE PEAK_MST SET COMMENT  = 'IGNORED BY 10PER',IGNORE_FLG='Y' WHERE TIME_VAL NOT BETWEEN '"+str(self.t1)+"' and '"+str(self.t2)+"' AND GRAPH_ID ='"+str(self.graph_id)+"'  AND IGNORE_FLG = 'N'")
                        
                  except Exception as e:
                           print("SQL Error- Update:"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()
        
        
        
        self.med = statistics.median(self.load_vals_B)
        print("Median A :"+str(self.med))
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        cursor.execute("UPDATE TEST_DATA SET MEDIAN = '"+str(self.med)+"' WHERE GRAPH_ID ='"+str(self.graph_id)+"'")                          
                        cursor.execute("UPDATE TEST_DATA SET RANGE_FROM = (SELECT MIN(PEAK_VALUE) FROM PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"'  AND IGNORE_FLG = 'N') WHERE GRAPH_ID ='"+str(self.graph_id)+"'")
                        cursor.execute("UPDATE TEST_DATA SET RANGE_TO = (SELECT MAX(PEAK_VALUE) FROM PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"'  AND IGNORE_FLG = 'N') WHERE GRAPH_ID ='"+str(self.graph_id)+"'")
                  except Exception as e:
                           print("SQL Error- test_method_A_calc() :"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()
    
    def test_method_D_calc(self):
        self.max_peak_load=""
        self.min_low_load="" 
        self.avg_load = 0
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT max(PEAK_VALUE) FROM PEAK_MST WHERE GRAPH_ID ='"+str(self.graph_id)+"'  AND IGNORE_FLG = 'N' order by ID ASC")
        for x in results:
              self.max_peak_load=(float(x[0]))              
        connection.close()
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT min(LOW_VAL) FROM STG_LOW_VAL_MST where LOW_VAL > 0  order by ID ASC")
        for x in results:
              self.min_low_load=(float(x[0]))              
        connection.close()       
        
        self.avg_load = (self.max_peak_load + self.min_low_load)/2
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        cursor.execute("UPDATE TEST_DATA SET MEDIAN = '"+str(self.avg_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")                          
                        cursor.execute("UPDATE TEST_DATA SET RANGE_FROM = '"+str(self.min_low_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                        cursor.execute("UPDATE TEST_DATA SET RANGE_TO ='"+str(self.max_peak_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                  except Exception as e:
                           print("SQL Error- test_method_A_calc() :"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()
        
    def test_method_E_calc(self):
        self.max_peak_load=""
        self.min_peak_load="" 
        self.avg_load = 0
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT max(PEAK_VALUE) FROM STG_PEAK_MST order by ID ASC")
        for x in results:
              self.max_peak_load=(float(x[0]))              
        connection.close()
        
        connection = sqlite3.connect("tyr.db")        
        results=connection.execute("SELECT min(PEAK_VALUE) FROM STG_PEAK_MST order by ID ASC")
        for x in results:
              self.min_peak_load=(float(x[0]))              
        connection.close()       
        
        self.avg_load = (self.max_peak_load + self.min_peak_load)/2
        
        connection = sqlite3.connect("tyr.db")              
        with connection:
                  cursor = connection.cursor()
                  try:
                        cursor.execute("UPDATE TEST_DATA SET MEDIAN = '"+str(self.avg_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")                          
                        cursor.execute("UPDATE TEST_DATA SET RANGE_FROM = '"+str(self.min_peak_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                        cursor.execute("UPDATE TEST_DATA SET RANGE_TO ='"+str(self.max_peak_load)+"' WHERE GRAPH_ID IN (SELECT GRAPH_ID FROM STG_TEST_DATA)")
                  except Exception as e:
                           print("SQL Error- test_method_A_calc() :"+str(e))
                           connection.commit();
        connection.commit();
        connection.close()  

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #fig.savefig('ssdsd.png')
        self.axes = fig.add_subplot(111)        
        FigureCanvas.__init__(self, fig)
        #FigureCanvas.setStyleSheet("background-color:red;")
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)       
        
        self.plot()
        self.last_load_unit=""
        self.last_disp_unit=""
        self.graph_type=""
        self.cs_area_mm="1"       
        self.guage_length_mm="1"
        
        
    def plot(self):
        ax = self.figure.add_subplot(111)
       
        ax.set_facecolor('#CCFFFF')   
        ax.minorticks_on()
        
        ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        
        self.s=[]
        self.t=[]
        self.graph_ids=[]    
        self.x_num=[0.0]
        self.y_num=[0.0]
        self.test_type="Tear"
        self.g_id="0"
        self.color=['b','r','g','y','k','c','m','b']
        #ax.set_title('Test Id=32         Samples=3       BreakLoad(Kg)=110        Length(mm)=3')         
        '''
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT DISTINCT GRAPH_ID FROM TEST_DATA WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) order by GRAPH_ID") 
        for x in results:
              self.graph_ids.append(x[0])            
             
        connection.close()
        '''

        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT LAST_UNIT_LOAD,LAST_UNIT_DISP,GRAPH_SCAL_X_LENGTH,GRAPH_SCAL_Y_LOAD from TEST_MST  WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR) ") 
        for x in results:
              self.last_load_unit=str(x[0])
              self.last_disp_unit=str(x[1])
              ax.set_xlim(0,float(x[2]))
              ax.set_ylim(0,float(x[3]))  
        connection.close()
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT GRAPH_TYPE,GRAPH_ID from GLOBAL_VAR2") 
        for x in results:
              self.graph_type=str(x[0])
              self.graph_ids.append(x[1])
              self.g_id=str(x[1])
        connection.close()
        
                
        
        self.graph_type="Load Vs Time"
        for g in range(len(self.graph_ids)):
            self.x_num=[0.0]
            self.y_num=[0.0]
            connection = sqlite3.connect("tyr.db")
            if(self.graph_type=="Load Vs Travel"):
                    if(self.last_load_unit=="Kg" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Kg" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Kg" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Lb" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM_LB FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Lb" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM_LB FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Lb" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_LB FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="N" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="N" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="N" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM_N FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="KN" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_KN FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="KN" and self.last_disp_unit=="Cm"):
                                    results=connection.execute("SELECT X_NUM_CM,Y_NUM_KN FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="KN" and self.last_disp_unit=="Inch"):
                                    results=connection.execute("SELECT X_NUM_INCH,Y_NUM_KN FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="gm" and self.last_disp_unit=="Mm"):
                                    results=connection.execute("SELECT X_NUM,Y_NUM_MPA FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    else:    
                                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            
            elif(self.graph_type=="Load Vs Time"):                    
                    if(self.last_load_unit=="Kg"):
                        results=connection.execute("SELECT T_SEC,Y_NUM FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="Lb"):
                        results=connection.execute("SELECT T_SEC,Y_NUM_LB FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    elif(self.last_load_unit=="N"):
                        results=connection.execute("SELECT T_SEC,Y_NUM_N FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
                    else:
                        results=connection.execute("SELECT T_SEC,Y_NUM FROM GRAPH_MST WHERE T_SEC > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
         
            else:
                    results=connection.execute("SELECT X_NUM,Y_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
            for k in results:        
                self.x_num.append(k[0])
                self.y_num.append(k[1])
            connection.close()
           
            if(g < 8 ):
                ax.plot(self.x_num,self.y_num, self.color[g],label="Graph_ID:"+str(self.g_id))
        print("self.graph_type :"+str(self.graph_type))
        if(self.graph_type=="Load Vs Travel"):
                ax.set_xlabel('Elongation ('+str(self.last_disp_unit)+')')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        
        elif(self.graph_type=="Load Vs Time"):
                ax.set_xlabel('Time (sec)')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        else:
                ax.set_xlabel('Elongation ('+str(self.last_disp_unit)+')')
                ax.set_ylabel('Load ('+str(self.last_load_unit)+')')
        #self.connect('motion_notify_event', mouse_move)
        ax.legend()        
        self.draw()
        self.figure.savefig('last_graph.png',dpi=100)
        
        #ax.connect('motion_notify_event', mouse_move)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = pop_peal_val_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
