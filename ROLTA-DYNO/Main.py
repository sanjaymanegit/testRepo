import datetime
import os, sys
import time, sqlite3
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QLineEdit, QTextEdit, QMessageBox,QSizePolicy
from functools import partial
from PyQt5.Qt import QTableWidgetItem
from PyQt5.QtCore import QRegExp, Qt, pyqtSlot, QPoint
from PyQt5.QtGui import QRegExpValidator, QMouseEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtGui import QFontDatabase
from START_TEST import Ui_MainWindow
# from Analog import Ui_MainWindow

from DialogNumericKeyBoard import Ui_NumericKeyBo

from SPECIMEN import Ui_Specimen
from SETUP import Ui_Setup
from AlphaNumericKeyBoard import Ui_AlphabeticKeyBoard
from SELECT_REPORTS import Ui_SelectReport
from REPORTS import Ui_Reports
# os.system("pyuic5 -x Analog_Meter.ui -o Analog_Meter.py")


# import subprocess

# # Define the paths to the .ui file and the output .py file
# ui_file = 'Analog.ui'
# output_py_file = 'Analog.py'

# # Try to run the pyuic5 command
# try:
#     result = subprocess.run(['pyuic5', '-x', ui_file, '-o', output_py_file], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print("UI file converted successfully.")
#     print(result.stdout.decode())
# except subprocess.CalledProcessError as e:
#     print("Error occurred:", e.stderr.decode())
# ui_file = 'SetMaxDailog.ui'
# output_py_file = 'SetMaxDailog.py'
# try:
#     result = subprocess.run(['pyuic5', '-x', ui_file, '-o', output_py_file], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print("UI file converted successfully.")
#     print(result.stdout.decode())
# except subprocess.CalledProcessError as e:
#     print("Error occurred:", e.stderr.decode())
# current_time = datetime.datetime.now().strftime("%d %b %Y %H : %M : %S")
class DialogAlphaKeyBo(QDialog):
    def __init__(self, line_Edit):
        super(DialogAlphaKeyBo, self).__init__()
        self.keyBo_ui = Ui_AlphabeticKeyBoard()
        self.keyBo_ui.setupUi(self, line_Edit) 
        self._startPos = None
        self._endPos = None
        self._tracking = False
        # self.keyBo_ui.line_edit = line_Edit
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        # return super().mouseMoveEvent(a0) 
        if self._tracking:
            self._endPos = a0.pos() - self._startPos 
            self.move(self.pos() + self._endPos)  
    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.MouseButton.LeftButton:
            self._startPos = QPoint(a0.x(), a0.y())
            self._tracking = True
    def mouseReleaseEvent(self, a0: QMouseEvent) -> None: 
        if a0.button == Qt.MouseButton.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None 
class DialogNumericKeyBo(QDialog):
    def __init__(self, line_Edit):
        super(DialogNumericKeyBo, self).__init__()
        self.keyBo_ui = Ui_NumericKeyBo()
        self.keyBo_ui.setupUi(self, line_Edit) 
        self._startPos = None
        self._endPos = None
        self._tracking = False
        # self.keyBo_ui.line_edit = line_Edit
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        # return super().mouseMoveEvent(a0) 
        if self._tracking:
            self._endPos = a0.pos() - self._startPos 
            self.move(self.pos() + self._endPos)  
    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.MouseButton.LeftButton:
            self._startPos = QPoint(a0.x(), a0.y())
            self._tracking = True
    def mouseReleaseEvent(self, a0: QMouseEvent) -> None: 
        if a0.button == Qt.MouseButton.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None 

# class SpecimeDailog(QDialog):
#     def __init__(self, parent=None):
#         QDialog.__init__(self)
        
#         self.specimen_ui = Ui_Specimen()
#         self.specimen_ui.setupUi(self)
#         self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
#         self.specimen_ui.lineEdit_2.mousePressEvent = lambda event: self.openAlphaKeyBoard(self.specimen_ui.lineEdit_2)
#         self.specimen_ui.lineEdit_3.mousePressEvent = lambda event: self.openAlphaKeyBoard(self.specimen_ui.lineEdit_3)
#         self.specimen_ui.lineEdit.mousePressEvent = lambda event: self.openAlphaKeyBoard(self.specimen_ui.lineEdit)
#     def openAlphaKeyBoard(self, line):
#         self.aplhaKeyBo = DialogAlphaKeyBo(line)
#         self.aplhaKeyBo.exec_()                                                                                 
              
class Setup(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        
        self.setup_ui = Ui_Setup()
        self.setup_ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.timer1=QtCore.QTimer()
        self.timer1.start(1)
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.setDateAndTime)
        self.setup_ui.pushButton_3.clicked.connect(self.close)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.setup_ui.lineEdit_26)
        self.setup_ui.lineEdit_26.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.setup_ui.lineEdit_24)
        self.setup_ui.lineEdit_24.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.setup_ui.lineEdit_25)
        self.setup_ui.lineEdit_25.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.setup_ui.lineEdit_23)
        self.setup_ui.lineEdit_23.setValidator(input_validator)
        self.setup_ui.label_69.hide()
        self.setup_ui.pushButton_2.clicked.connect(self.saveTestData)
        # self.setup_ui.lineEdit_26.mousePressEvent = lambda event: self.openKeyBoard(self.setup_ui.lineEdit_26)
        # self.setup_ui.lineEdit_23.mousePressEvent = lambda event: self.openKeyBoard(self.setup_ui.lineEdit_23)
        # self.setup_ui.lineEdit_24.mousePressEvent = lambda event: self.openKeyBoard(self.setup_ui.lineEdit_24)
        # self.setup_ui.lineEdit_25.mousePressEvent = lambda event: self.openKeyBoard(self.setup_ui.lineEdit_25)
        
        
        self.setup_ui.pushButton_6.clicked.connect(self.resetFields)
        self.setup_ui.tableWidget.doubleClicked.connect(self.fetchSpecimenData)
        self.setup_ui.comboBox_2.currentTextChanged.connect(self.specimen_name_on_change)
        self.loadData()
        self.loadTableData()
    def setDateAndTime(self):
        self.setup_ui.label_72.setText(datetime.datetime.now().strftime("%d %b %Y %H : %M : %S"))
    def specimen_name_on_change(self):
        connection = sqlite3.connect("Rolla.db") 
        results=connection.execute("SELECT JOB_NAME, BATCH_ID, PRODUCT_ID, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION FROM SPECIMEN_MST WHERE PRODUCT_ID = '"+str(self.setup_ui.comboBox_2.currentText())+"'")
        
        for x in results:
            self.setup_ui.lineEdit.setText(str(x[0]))
            self.setup_ui.lineEdit_2.setText(str(x[1]))
            self.setup_ui.lineEdit_3.setText(str(x[2]))
            self.setup_ui.lineEdit_11.setText(str(x[3]))
            self.setup_ui.lineEdit_6.setText(str(x[4]))
            self.setup_ui.lineEdit_9.setText(str(x[5]))
            self.setup_ui.lineEdit_20.setText(str(x[6]))
            self.setup_ui.lineEdit_5.setText(str(x[7]))
            self.setup_ui.lineEdit_21.setText(str(x[8]))
            self.setup_ui.lineEdit_22.setText(str(x[9]))
            self.setup_ui.lineEdit_10.setText(str(x[10]))
            self.setup_ui.lineEdit_8.setText(str(x[11]))
            self.setup_ui.lineEdit_13.setText(str(x[12]))
            self.setup_ui.lineEdit_12.setText(str(x[13]))
            self.setup_ui.lineEdit_16.setText(str(x[14]))
            self.setup_ui.lineEdit_17.setText(str(x[15]))
            self.setup_ui.lineEdit_7.setText(str(x[16]))
            self.setup_ui.textEdit.setText(str(x[17]))    
        connection.close()
        

    def fetchSpecimenData(self):
        self.setup_ui.pushButton_2.setDisabled(False)
        row = self.setup_ui.tableWidget.currentRow() 
        if (row != -1):
            self.setup_ui.comboBox_2.setCurrentText(self.setup_ui.tableWidget.item(row, 0).text())
            self.setup_ui.lineEdit.setText(str(self.setup_ui.tableWidget.item(row, 1).text()))
            self.setup_ui.lineEdit_2.setText(str(self.setup_ui.tableWidget.item(row, 2).text()))
            self.setup_ui.lineEdit_3.setText(str(self.setup_ui.tableWidget.item(row, 3).text()))
            self.setup_ui.lineEdit_11.setText(str(self.setup_ui.tableWidget.item(row, 4).text()))
            self.setup_ui.lineEdit_6.setText(str(self.setup_ui.tableWidget.item(row, 5).text()))
            self.setup_ui.lineEdit_9.setText(str(self.setup_ui.tableWidget.item(row, 6).text()))
            self.setup_ui.lineEdit_20.setText(str(self.setup_ui.tableWidget.item(row, 7).text()))
            self.setup_ui.lineEdit_5.setText(str(self.setup_ui.tableWidget.item(row, 8).text()))
            self.setup_ui.lineEdit_21.setText(str(self.setup_ui.tableWidget.item(row, 9).text()))
            self.setup_ui.lineEdit_22.setText(str(self.setup_ui.tableWidget.item(row, 10).text()))
            self.setup_ui.lineEdit_10.setText(str(self.setup_ui.tableWidget.item(row, 11).text()))
            self.setup_ui.lineEdit_8.setText(str(self.setup_ui.tableWidget.item(row, 12).text()))
            self.setup_ui.lineEdit_13.setText(str(self.setup_ui.tableWidget.item(row, 13).text()))
            self.setup_ui.lineEdit_12.setText(str(self.setup_ui.tableWidget.item(row, 14).text()))
            self.setup_ui.lineEdit_16.setText(str(self.setup_ui.tableWidget.item(row, 15).text()))
            self.setup_ui.lineEdit_17.setText(str(self.setup_ui.tableWidget.item(row, 16).text()))
            self.setup_ui.lineEdit_7.setText(str(self.setup_ui.tableWidget.item(row, 17).text()))
            self.setup_ui.textEdit.setText(str(self.setup_ui.tableWidget.item(row, 18).text()))
        else:
            print("select the row...")
        
    def validation(self):
                self.go_ahead="No"
                if (self.setup_ui.lineEdit.text() == ""):
                   self.setup_ui.label_69.setText("Job Name : Should Not Be Empty..." )            
                   self.setup_ui.label_69.show()      
                elif (self.setup_ui.lineEdit_2.text() == ""):
                    self.setup_ui.label_69.setText("Batch ID : Should Not Be Empty...")                
                    self.setup_ui.label_69.show()    
                elif (self.setup_ui.lineEdit_3.text() == ""):
                    self.setup_ui.label_69.setText("Product ID : Should Not Be Empty...") 
                    self.setup_ui.label_69.show()                   
                   
                elif (self.setup_ui.lineEdit_11.text() == ""):
                    self.setup_ui.label_69.setText("Model : Should Not Be Empty...")                   
                    self.setup_ui.label_69.show() 
                elif (self.setup_ui.lineEdit_6.text() == ""):
                    self.setup_ui.label_69.setText("Part No. : Should Not Be Empty...")                   
                    self.setup_ui.label_69.show()         
                elif (self.setup_ui.lineEdit_9.text() == ""):
                    self.setup_ui.label_69.setText("Current : Should Not Be Empty...")                  
                    self.setup_ui.label_69.show() 
                elif (self.setup_ui.lineEdit_13.text() == ""):
                    self.setup_ui.label_69.setText("Phase : Should Not Be Empty...")                   
                    self.setup_ui.label_69.show() 
                elif (self.setup_ui.lineEdit_20.text() == ""):
                    self.setup_ui.label_69.setText("Client : Should Not Be Empty...")                   
              
                elif (self.setup_ui.lineEdit_5.text() == ""):
                    self.setup_ui.label_69.setText("Serial No. : Should Not Be Empty...")                   
                    self.setup_ui.label_69.show() 
                elif (self.setup_ui.lineEdit_21.text() == ""):
                    self.setup_ui.label_69.setText("Output Power : Should Not Be Empty...")                   
                    self.setup_ui.label_69.show() 
                elif (self.setup_ui.lineEdit_22.text() == ""):
                    self.setup_ui.label_69.setText("Rotational Direction : Should Not Be Empty...")                   
                    self.setup_ui.label_69.show() 
                elif (self.setup_ui.lineEdit_10.text() == ""):
                    self.setup_ui.label_69.setText("Starter Capacitor : Should Not Be Empty...")                   
                    self.setup_ui.label_69.show() 
                elif (self.setup_ui.lineEdit_8.text() == ""):
                    self.setup_ui.label_69.setText("Operation Capacitor : Should Not Be Empty...") 
                    self.setup_ui.label_69.show()       
                elif (self.setup_ui.lineEdit_12.text() == ""):
                    self.setup_ui.label_69.setText("Voltage : Should Not Be Empty...")                   
                    self.setup_ui.label_69.show() 
                elif (self.setup_ui.lineEdit_16.text() == ""):
                    self.setup_ui.label_69.setText("Pole : Should Not Be Empty...") 
                    self.setup_ui.label_69.show() 
                elif (self.setup_ui.lineEdit_17.text() == ""):
                    self.setup_ui.label_69.setText("Moter Speed : Should Not Be Empty...")                   
                    self.setup_ui.label_69.show() 
                elif (self.setup_ui.lineEdit_7.text() == ""):
                    self.setup_ui.label_69.setText("Frequency : Should Not Be Empty...") 
                    self.setup_ui.label_69.show() 
                elif (self.setup_ui.textEdit.toPlainText() == ""):
                    self.setup_ui.label_69.setText("Test Condition : Should Not Be Empty...")                   
                    self.setup_ui.label_69.show() 
                else:
                        self.go_ahead="Yes"
    def resetFields(self):
        connection = sqlite3.connect("Rolla.db")
        results=connection.execute("select seq + 1 from sqlite_sequence WHERE name = 'TEST_MST'")       
        for x in results:      
                self.setup_ui.label_59.setText(str(x[0]).zfill(3))   
        connection.close()
        lineEdits = [
            self.setup_ui.lineEdit, self.setup_ui.lineEdit_2, self.setup_ui.lineEdit_3, self.setup_ui.lineEdit_11, 
            self.setup_ui.lineEdit_6, self.setup_ui.lineEdit_9, self.setup_ui.lineEdit_20, self.setup_ui.lineEdit_5, 
            self.setup_ui.lineEdit_21, self.setup_ui.lineEdit_22, self.setup_ui.lineEdit_10, self.setup_ui.lineEdit_8, 
            self.setup_ui.lineEdit_13, self.setup_ui.lineEdit_12, self.setup_ui.lineEdit_16, self.setup_ui.lineEdit_17, 
            self.setup_ui.lineEdit_7, self.setup_ui.textEdit, self.setup_ui.lineEdit_26, self.setup_ui.lineEdit_24,
            self.setup_ui.lineEdit_25, self.setup_ui.lineEdit_23
        ]
        for line_edit in lineEdits:
            line_edit.setText("")
        
    def loadTableData(self):
        self.delete_all_records()
        connection = sqlite3.connect("Rolla.db")  
        results=connection.execute("SELECT SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_ID, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION FROM SPECIMEN_MST")
        for row_number, row_data in enumerate(results):            
            self.setup_ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data): 
                self.setup_ui.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data))) 
        
        connection.commit()
        connection.close()  
         
        if(self.setup_ui.tableWidget.rowCount() > 0):
            self.setup_ui.lineEdit.setText(str(self.setup_ui.tableWidget.item(0, 1).text()))
            self.setup_ui.lineEdit_2.setText(str(self.setup_ui.tableWidget.item(0, 2).text()))
            self.setup_ui.lineEdit_3.setText(str(self.setup_ui.tableWidget.item(0, 3).text()))
            self.setup_ui.lineEdit_11.setText(str(self.setup_ui.tableWidget.item(0, 4).text()))
            self.setup_ui.lineEdit_6.setText(str(self.setup_ui.tableWidget.item(0, 5).text()))
            self.setup_ui.lineEdit_9.setText(str(self.setup_ui.tableWidget.item(0, 6).text()))
            self.setup_ui.lineEdit_20.setText(str(self.setup_ui.tableWidget.item(0, 7).text()))
            self.setup_ui.lineEdit_5.setText(str(self.setup_ui.tableWidget.item(0, 8).text()))
            self.setup_ui.lineEdit_21.setText(str(self.setup_ui.tableWidget.item(0, 9).text()))
            self.setup_ui.lineEdit_22.setText(str(self.setup_ui.tableWidget.item(0, 10).text()))
            self.setup_ui.lineEdit_10.setText(str(self.setup_ui.tableWidget.item(0, 11).text()))
            self.setup_ui.lineEdit_8.setText(str(self.setup_ui.tableWidget.item(0, 12).text()))
            self.setup_ui.lineEdit_13.setText(str(self.setup_ui.tableWidget.item(0, 13).text()))
            self.setup_ui.lineEdit_12.setText(str(self.setup_ui.tableWidget.item(0, 14).text()))
            self.setup_ui.lineEdit_16.setText(str(self.setup_ui.tableWidget.item(0, 15).text()))
            self.setup_ui.lineEdit_17.setText(str(self.setup_ui.tableWidget.item(0, 16).text()))
            self.setup_ui.lineEdit_7.setText(str(self.setup_ui.tableWidget.item(0, 17).text()))
            self.setup_ui.textEdit.setText(str(self.setup_ui.tableWidget.item(0, 18).text()))

    def loadData(self):
        connection = sqlite3.connect("Rolla.db") 
        results = connection.execute("SELECT DISTINCT PRODUCT_ID FROM SPECIMEN_MST WHERE PRODUCT_ID IS NOT NULL")
        for x in results:
            specimen_name = x[0]
            self.setup_ui.comboBox_2.addItem(specimen_name)
        connection.close()   
        connection = sqlite3.connect("Rolla.db")
        # cursor = connection.cursor()
        results=connection.execute("SELECT MAX_MOTER_SPEED, MAX_POWER, MAX_TORQUE, MAX_SerOT FROM GLOBAL_VAR")
        for x in results:
            self.setup_ui.lineEdit_26.setText(x[0])
            self.setup_ui.lineEdit_23.setText(x[1])
            self.setup_ui.lineEdit_24.setText(x[2])
            self.setup_ui.lineEdit_25.setText(x[3])
        connection.close()
        connection = sqlite3.connect("Rolla.db")
        results=connection.execute("select seq + 1 from sqlite_sequence WHERE name = 'TEST_MST'")       
        for x in results:      
                self.setup_ui.label_59.setText(str(x[0]).zfill(3))   
        connection.close()
    def delete_all_records(self):
        i = self.setup_ui.tableWidget.rowCount()       
        while (i>0):      
            i=i-1
            self.setup_ui.tableWidget.removeRow(i)
    def openKeyBoard(self, line):
        self.callKeyBo = DialogNumericKeyBo(line)
        self.callKeyBo.exec_()  

    def saveTestData(self):
        self.validation()
        if (self.setup_ui.lineEdit_26.text() == ""):
            self.setup_ui.label_69.setText("Oops : Max Speed is Empty!!!")
        elif ( self.setup_ui.lineEdit_23.text() == ""):
            self.setup_ui.label_69.setText("Oops : Max Power is Empty!!!")
        elif ( self.setup_ui.lineEdit_24.text() == ""):
            self.setup_ui.label_69.setText("Oops : Max Torque is Empty!!!")
        elif ( self.setup_ui.lineEdit_25.text() == ""):
            self.setup_ui.label_69.setText("Oops : Max SerOT is Empty!!!")    
        else:
            if self.go_ahead == "Yes":
                connection = sqlite3.connect("Rolla.db")
                results=connection.execute("select count(*) from TEST_MST WHERE TEST_ID = '"+str(int(self.setup_ui.label_59.text()))+"'")  
                    
                for x in results:           
                        if(int(x[0]) > 0):   
                            self.test_id_exist="Yes"
                        else:
                            self.test_id_exist="No"
                                                   
                connection.close() 
                                
                if(self.test_id_exist=="No"):                   
                        
                    connection = sqlite3.connect("Rolla.db")
                    cursor = connection.cursor()
                    with connection:
                        cursor = connection.cursor() 
                        cursor.execute("""
                            INSERT INTO TEST_MST (
                                SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_NAME, MODEL, PART_NO, CURRENT, CILENT, 
                                SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, 
                                PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION, MAX_MOTER_SPEED, 
                                MAX_POWER, MAX_TORQUE, MAX_SerOT, TEST_ID
                            ) VALUES (
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                            )
                        """, (
                                str(self.setup_ui.comboBox_2.currentText()), str(self.setup_ui.lineEdit.text()), str(self.setup_ui.lineEdit_2.text()),
                                str(self.setup_ui.lineEdit_3.text()), str(self.setup_ui.lineEdit_11.text()), str(self.setup_ui.lineEdit_6.text()),
                                str(self.setup_ui.lineEdit_9.text()), str(self.setup_ui.lineEdit_20.text()), str(self.setup_ui.lineEdit_5.text()),
                                str(self.setup_ui.lineEdit_21.text()), str(self.setup_ui.lineEdit_22.text()), str(self.setup_ui.lineEdit_10.text()),
                                str(self.setup_ui.lineEdit_8.text()), str(self.setup_ui.lineEdit_13.text()), str(self.setup_ui.lineEdit_12.text()),
                                str(self.setup_ui.lineEdit_16.text()), str(self.setup_ui.lineEdit_17.text()), str(self.setup_ui.lineEdit_7.text()),
                                str(self.setup_ui.textEdit.toPlainText()), str(self.setup_ui.lineEdit_26.text()), str(self.setup_ui.lineEdit_23.text()),
                                str(self.setup_ui.lineEdit_24.text()), str(self.setup_ui.lineEdit_25.text()), str(self.setup_ui.label_59.text())
                            ))
                        cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID = '"+str(self.setup_ui.label_59.text())+"'")
                        # cursor.execute("UPDATE TEST_MST SET SPECIMEN_ID = '"+str(self.setup_ui.comboBox_2.currentText())+"', JOB_NAME = '"+str(self.setup_ui.lineEdit.text())+"', BATCH_ID = '"+str(self.setup_ui.lineEdit_2.text())+"', PRODUCT_NAME = '"+str(self.setup_ui.lineEdit_3.text())+"', MODEL = '"+str(self.setup_ui.lineEdit_11.text())+"', PART_NO = '"+str(self.setup_ui.lineEdit_6.text())+"', CURRENT = '"+str(self.setup_ui.lineEdit_9.text())+"', CILENT = '"+str(self.setup_ui.lineEdit_20.text())+"', SERIAL_NO = '"+str(self.setup_ui.lineEdit_5.text())+"', OUTPUT_POWER = '"+str(self.setup_ui.lineEdit_21.text())+"', ROTATIONAL_DIRECTION = '"+str(self.setup_ui.lineEdit_22.text())+"', STARTER_CAPACITOR = '"+str(self.setup_ui.lineEdit_10.text())+"', OPERATION_CAPACITOR = '"+str(self.setup_ui.lineEdit_8.text())+"', PHASE = '"+str(self.setup_ui.lineEdit_13.text())+"', VOLTAGE = '"+str(self.setup_ui.lineEdit_12.text())+"', POLE = '"+str(self.setup_ui.lineEdit_16.text())+"', MOTER_SPEED = '"+str(self.setup_ui.lineEdit_17.text())+"', FREQUENCY = '"+str(self.setup_ui.lineEdit_7.text())+"', TEST_CONDITION = '"+str(self.setup_ui.textEdit.toPlainText())+"', MAX_MOTER_SPEED = '"+str(self.setup_ui.lineEdit_26.text())+"', MAX_POWER = '"+str(self.setup_ui.lineEdit_23.text())+"', MAX_TORQUE = '"+str(self.setup_ui.lineEdit_24.text())+"', MAX_SerOT = '"+str(self.setup_ui.lineEdit_25.text())+"' WHERE TEST_ID = '"+str(self.setup_ui.label_59.text())+"'")
                    connection.commit()
                    connection.close()
                    self.setup_ui.label_69.setText("Recorded : Max Setup data inserted Successful!!!") 
                    self.setup_ui.label_69.show()  
                else:
                    connection = sqlite3.connect("Rolla.db")
                    cursor = connection.cursor()
                    with connection:
                        cursor = connection.cursor() 
                        cursor.execute("UPDATE TEST_MST SET SPECIMEN_ID = '"+str(self.setup_ui.comboBox_2.currentText())+"', JOB_NAME = '"+str(self.setup_ui.lineEdit.text())+"', BATCH_ID = '"+str(self.setup_ui.lineEdit_2.text())+"', PRODUCT_NAME = '"+str(self.setup_ui.lineEdit_3.text())+"', MODEL = '"+str(self.setup_ui.lineEdit_11.text())+"', PART_NO = '"+str(self.setup_ui.lineEdit_6.text())+"', CURRENT = '"+str(self.setup_ui.lineEdit_9.text())+"', CILENT = '"+str(self.setup_ui.lineEdit_20.text())+"', SERIAL_NO = '"+str(self.setup_ui.lineEdit_5.text())+"', OUTPUT_POWER = '"+str(self.setup_ui.lineEdit_21.text())+"', ROTATIONAL_DIRECTION = '"+str(self.setup_ui.lineEdit_22.text())+"', STARTER_CAPACITOR = '"+str(self.setup_ui.lineEdit_10.text())+"', OPERATION_CAPACITOR = '"+str(self.setup_ui.lineEdit_8.text())+"', PHASE = '"+str(self.setup_ui.lineEdit_13.text())+"', VOLTAGE = '"+str(self.setup_ui.lineEdit_12.text())+"', POLE = '"+str(self.setup_ui.lineEdit_16.text())+"', MOTER_SPEED = '"+str(self.setup_ui.lineEdit_17.text())+"', FREQUENCY = '"+str(self.setup_ui.lineEdit_7.text())+"', TEST_CONDITION = '"+str(self.setup_ui.textEdit.toPlainText())+"', MAX_MOTER_SPEED = '"+str(self.setup_ui.lineEdit_26.text())+"', MAX_POWER = '"+str(self.setup_ui.lineEdit_23.text())+"', MAX_TORQUE = '"+str(self.setup_ui.lineEdit_24.text())+"', MAX_SerOT = '"+str(self.setup_ui.lineEdit_25.text())+"' WHERE TEST_ID = '"+str(self.setup_ui.label_59.text())+"'")
                        cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID = '"+str(self.setup_ui.label_59.text())+"'")
                    connection.commit()
                    connection.close()
                    self.setup_ui.label_69.setText("Recorded : Max Setup Data Saved Successful!!!") 
                    self.setup_ui.label_69.show()  
                    
                self.go_ahead = "No"
        self.loadTableData()     

class SelectReport(QMainWindow):
    def __init__(self, window, parent=None):
        super(SelectReport, self).__init__()
        # Setup the UI main window
        self.select_Report_Ui = Ui_SelectReport()
        self.select_Report_Ui.setupUi(self)
        self._window = window
        self.select_Report_Ui.pushButton_3.clicked.connect(self.close)
        # self.select_Report_Ui.label_72.setText(current_time)
        self.onStart()
        self.i=0        
        for x in range(24):            
            self.select_Report_Ui.comboBox.addItem("")
            self.select_Report_Ui.comboBox.setItemText(self.i,str("%02d"%x))
            self.select_Report_Ui.comboBox_8.addItem("")
            self.select_Report_Ui.comboBox_8.setItemText(self.i,str("%02d"%x))             
            self.i=self.i+1

        
        self.i=0
        for x in range(60):            
            self.select_Report_Ui.comboBox_2.addItem("")
            self.select_Report_Ui.comboBox_2.setItemText(self.i,str("%02d"%x))
            self.select_Report_Ui.comboBox_7.addItem("")
            self.select_Report_Ui.comboBox_7.setItemText(self.i,str("%02d"%x))
            #print("i :"+str(x))
            self.i=self.i+1
    def onStart(self):
        self.delete_all_records()
        self.timer1=QtCore.QTimer()
        self.timer1.start(1)
        
        self.timer1.setInterval(1000) 
        self.select_Report_Ui.label_69.hide()       
        self.timer1.timeout.connect(self.setDateAndTime)
        self.select_Report_Ui.calendarWidget.hide()
        self.select_Report_Ui.calendarWidget_2.hide()
        self.select_Report_Ui.pushButton_5.hide()
        self.select_Report_Ui.pushButton_8.clicked.connect( lambda : self.select_Report_Ui.calendarWidget.show())
        self.select_Report_Ui.pushButton_12.clicked.connect(lambda : self.select_Report_Ui.calendarWidget_2.show())
        self.select_Report_Ui.calendarWidget.clicked.connect(partial(self.on_calendarWidget_clicked, source="_from"))
        self.select_Report_Ui.calendarWidget_2.clicked.connect(partial(self.on_calendarWidget_clicked, source="_to"))
    
        self.i=0
        self.select_Report_Ui.comboBox_3.clear()
        connection = sqlite3.connect("Rolla.db")
        results=connection.execute("SELECT DISTINCT JOB_NAME FROM TEST_MST ") 
        for x in results:            
            self.select_Report_Ui.comboBox_3.addItem("")
            self.select_Report_Ui.comboBox_3.setItemText(self.i,str(x[0]))
            
            self.i=self.i+1
        connection.close()
        
        
        self.i=0
        self.select_Report_Ui.comboBox_4.clear()
        connection = sqlite3.connect("Rolla.db")
        results=connection.execute("SELECT DISTINCT BATCH_ID FROM TEST_MST ") 
        for x in results:            
            self.select_Report_Ui.comboBox_4.addItem("")
            self.select_Report_Ui.comboBox_4.setItemText(self.i,str(x[0]))           
            self.i=self.i+1
        connection.close()
       
        self.select_Report_Ui.pushButton_4.clicked.connect(self.select_all_tests)
        self.select_Report_Ui.tableWidget.doubleClicked.connect(self.open_doubleClick_report)
        self.select_Report_Ui.checkBox.clicked.connect(self.check_uncheck_all_records)
        
        # self.select_all_tests()
    

    
    def open_doubleClick_report(self):
        row = self.select_Report_Ui.tableWidget.currentRow()
        if(row != -1 ):
            self.specimen_id=(self.select_Report_Ui.tableWidget.item(row, 0).text())
            print(" specimen_id :"+str(self.specimen_id))        
        
            connection = sqlite3.connect("Rolla.db")
            with connection:        
                  cursor = connection.cursor()                                        
                  cursor.execute("UPDATE GLOBAL_VAR SET TEST_ID = '"+str(self.specimen_id)+"'")              
            connection.commit()
            connection.close() 
        else:
            print("select record...")
        self.Report = Reports(self)
        self.Report.show() 
            
    def on_calendarWidget_clicked(self, source):
        if source == "_from":
            self.select_Report_Ui.lineEdit.setText(str(self.select_Report_Ui.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)))
            self.select_Report_Ui.calendarWidget.hide()
        else:
            self.select_Report_Ui.lineEdit_2.setText(str(self.select_Report_Ui.calendarWidget_2.selectedDate().toString(QtCore.Qt.ISODate)))
            self.select_Report_Ui.calendarWidget_2.hide()

    def setDateAndTime(self):
        self.select_Report_Ui.label_72.setText(datetime.datetime.now().strftime("%d %b %Y %H : %M : %S"))

    def delete_all_records(self):
        i = self.select_Report_Ui.tableWidget.rowCount()       
        while (i>0):      
            i=i-1
            self.select_Report_Ui.tableWidget.removeRow(i)
    def select_all_tests(self):
        self.delete_all_records()
        self.from_dt=f"{str(self.select_Report_Ui.lineEdit.text())} {str(self.select_Report_Ui.comboBox.currentText())}:{str(self.select_Report_Ui.comboBox_2.currentText())}:00"        
        self.to_dt=f"{str(self.select_Report_Ui.lineEdit_2.text())} {str(self.select_Report_Ui.comboBox_8.currentText())}:{str(self.select_Report_Ui.comboBox_7.currentText())}:00"
        
        # Convert the date strings to datetime objects
        from_dt = datetime.datetime.strptime(self.from_dt, '%Y-%m-%d %H:%M:%S')
        to_dt = datetime.datetime.strptime(self.to_dt, '%Y-%m-%d %H:%M:%S')
        # Check if to_dt is less than from_dt
        if to_dt < from_dt:
            # Show an error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("The 'to' date cannot be less than the 'from' date.")
            msg.setWindowTitle("Invalid Date Range")
            msg.exec_()
        else:
            connection = sqlite3.connect("Rolla.db") 
            if(self.select_Report_Ui.radioButton.isChecked()):
                results=connection.execute("SELECT TEST_ID, SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_NAME, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION FROM TEST_MST WHERE CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' AND JOB_NAME = '"+str(self.select_Report_Ui.comboBox_3.currentText())+"'")
            elif(self.select_Report_Ui.radioButton_2.isChecked()):
                results=connection.execute("SELECT TEST_ID, SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_NAME, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION FROM TEST_MST WHERE CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' AND BATCH_ID = '"+str(self.select_Report_Ui.comboBox_4.currentText())+"'")
            else:
                results = connection.execute("SELECT TEST_ID, SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_NAME, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION FROM TEST_MST WHERE CREATED_ON BETWEEN '" + self.from_dt + "' AND '" + self.to_dt + "'")

                # results=connection.execute("SELECT TEST_ID, SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_NAME, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION FROM TEST_MST WHERE CREATED_ON between '"+str(self.from_dt)+"' and '"+str(self.to_dt)+"' AND")
            for row_number, row_data in enumerate(results):            
                self.select_Report_Ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data): 
                    if(int(column_number) == 0):
                        item = QtWidgets.QTableWidgetItem()
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item.setCheckState(not QtCore.Qt.Checked)
                        item.setText(str(data))
                        self.select_Report_Ui.tableWidget.setItem(row_number,column_number,item)
                    else:
                        self.select_Report_Ui.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data))) 
            connection.commit()
            connection.close() 

    def check_uncheck_all_records(self):
        i = self.select_Report_Ui.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            item = self.select_Report_Ui.tableWidget.item(i, 0)
            if(self.select_Report_Ui.checkBox.isChecked()):
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(not QtCore.Qt.Checked)

class Reports(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        # Setup the UI main window
        self.reports_ui = Ui_Reports()
        self.reports_ui.setupUi(self)
        self.timer1=QtCore.QTimer()
        self.timer1.start(1)
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.setDateAndTime)
        self.reports_ui.label_53.hide()
        
        self.reports_ui.pushButton_3.clicked.connect(self.close)
        self.load_Data()
        self.reports_ui.label_69.hide()
    def setDateAndTime(self):
        self.reports_ui.label_72.setText(datetime.datetime.now().strftime("%d %b %Y %H : %M : %S"))
    def load_Data(self):
        self.readOnly()
        connection = sqlite3.connect("Rolla.db")
        results=connection.execute("SELECT TEST_ID, SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_NAME, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            self.reports_ui.label_54.setText(str(x[0]).zfill(3))
            # self.reports_ui.comboBox_2.addItem(str(x[1]))
            self.reports_ui.label_59.setText("( "+str(x[1]).zfill(3)+" )")
            self.reports_ui.lineEdit.setText(str(x[2]))
            self.reports_ui.lineEdit_2.setText(str(x[3]))
            self.reports_ui.lineEdit_3.setText(str(x[4]))
            self.reports_ui.lineEdit_11.setText(str(x[5]))
            self.reports_ui.lineEdit_6.setText(str(x[6]))
            self.reports_ui.lineEdit_9.setText(str(x[7]))
            self.reports_ui.lineEdit_20.setText(str(x[8]))
            self.reports_ui.lineEdit_5.setText(str(x[9]))
            self.reports_ui.lineEdit_21.setText(str(x[10]))
            self.reports_ui.lineEdit_22.setText(str(x[11]))
            self.reports_ui.lineEdit_10.setText(str(x[12]))
            self.reports_ui.lineEdit_19.setText(str(x[13]))
            self.reports_ui.lineEdit_13.setText(str(x[14]))
            self.reports_ui.lineEdit_12.setText(str(x[15]))
            self.reports_ui.lineEdit_16.setText(str(x[16]))
            self.reports_ui.lineEdit_17.setText(str(x[17]))
            self.reports_ui.lineEdit_7.setText(str(x[18]))
            self.reports_ui.textEdit.setText(str(x[19]))
        self.delete_all_records() 
        connection.commit()
        connection.close() 
        connection = sqlite3.connect("Rolla.db")
        results=connection.execute("SELECT TEST_ID, SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_NAME, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION FROM TEST_MST WHERE SPECIMEN_ID IN (SELECT SPECIMEN_ID FROM GLOBAL_VAR)")  
        for row_number, row_data in enumerate(results):            
            self.reports_ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.reports_ui.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))                
        self.reports_ui.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()
        self.reports_ui.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
        connection.commit()
        connection.close()  
        # self.sc_blank =PlotCanvas(self, width=8, height=5, dpi=100)          
        # self.reports_ui.graphicsView.setScene(self.sc_blank)  
    
    def readOnly(self):
        lineEdits = [
            self.reports_ui.lineEdit, self.reports_ui.lineEdit_2, self.reports_ui.lineEdit_3, self.reports_ui.lineEdit_11, 
            self.reports_ui.lineEdit_6, self.reports_ui.lineEdit_9, self.reports_ui.lineEdit_20, self.reports_ui.lineEdit_5, 
            self.reports_ui.lineEdit_21, self.reports_ui.lineEdit_22, self.reports_ui.lineEdit_10, self.reports_ui.lineEdit_19,
            self.reports_ui.lineEdit_13, self.reports_ui.lineEdit_12, self.reports_ui.lineEdit_16, self.reports_ui.lineEdit_17, 
            self.reports_ui.lineEdit_7, self.reports_ui.textEdit
        ]
        for x in lineEdits:
            x.setReadOnly(True) 
    def delete_all_records(self):
        i = self.reports_ui.tableWidget.rowCount()       

        while (i>0):      
            i=i-1
            self.reports_ui.tableWidget.removeRow(i)

class Specimen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        # Setup the UI main window
        self.specimen_ui = Ui_Specimen()
        self.specimen_ui.setupUi(self)
        self.timer1=QtCore.QTimer()
        self.timer1.start(1)
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.setDateAndTime)
        self.specimen_ui.label_69.hide()
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.specimen_ui.lineEdit_9)
        self.specimen_ui.lineEdit_9.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.specimen_ui.lineEdit_21)
        self.specimen_ui.lineEdit_21.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.specimen_ui.lineEdit_17)
        self.specimen_ui.lineEdit_17.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.specimen_ui.lineEdit_12)
        self.specimen_ui.lineEdit_12.setValidator(input_validator)
        self.specimen_ui.pushButton_3.clicked.connect(self.close)
        self.specimen_ui.pushButton_2.setDisabled(True)
        self.specimen_ui.pushButton_4.setDisabled(True)
        self.specimen_ui.pushButton_5.setDisabled(True)
        self.specimen_ui.pushButton_6.clicked.connect(self.resetFields)
        self.specimen_ui.pushButton_5.clicked.connect(self.addSpecimeDetails)
        self.specimen_ui.pushButton_2.clicked.connect(self.saveSpecimeDetails)
        self.specimen_ui.pushButton_4.clicked.connect(self.deleteSpecimen)

        self.load_Data()
        self.specimen_ui.label_69.hide()
        self.specimen_ui.tableWidget.doubleClicked.connect(self.fetchSpecimenData)
    
    

    def setDateAndTime(self):
        self.specimen_ui.label_72.setText(datetime.datetime.now().strftime("%d %b %Y %H : %M : %S"))
    def saveSpecimeDetails(self):
        self.validation()
        if self.go_ahead == "Yes":
            SPECIMEN_ID = self.specimen_ui.label_54.text()
            JOB_NAME = self.specimen_ui.lineEdit.text()
            BATCH_ID = self.specimen_ui.lineEdit_2.text()
            PRODUCT_ID = self.specimen_ui.lineEdit_3.text()
            MODEL = self.specimen_ui.lineEdit_11.text()
            PART_NO = self.specimen_ui.lineEdit_6.text()
            CURRENT = self.specimen_ui.lineEdit_9.text()
            CILENT = self.specimen_ui.lineEdit_20.text()
            SERIAL_NO = self.specimen_ui.lineEdit_5.text()
            OUTPUT_POWER = self.specimen_ui.lineEdit_21.text()
            ROTATIONAL_DIRECTION = self.specimen_ui.lineEdit_22.text()
            STARTER_CAPACITOR = self.specimen_ui.lineEdit_10.text()
            OPERATION_CAPACITOR = self.specimen_ui.lineEdit_8.text()
            PHASE = self.specimen_ui.lineEdit_13.text()
            VOLTAGE = self.specimen_ui.lineEdit_12.text()
            POLE = self.specimen_ui.lineEdit_16.text()
            MOTER_SPEED = self.specimen_ui.lineEdit_17.text()
            FREQUENCY = self.specimen_ui.lineEdit_7.text()
            TEST_CONDITION = self.specimen_ui.textEdit.toPlainText()
            connection = sqlite3.connect("Rolla.db")
            with connection:        
                cursor = connection.cursor()                                        
                cursor.execute(
                    "UPDATE SPECIMEN_MST SET SPECIMEN_ID = ?, JOB_NAME = ?, BATCH_ID = ?, PRODUCT_ID = ?, MODEL = ?, PART_NO = ?, CURRENT = ?, CILENT = ?, SERIAL_NO = ?, OUTPUT_POWER = ?, ROTATIONAL_DIRECTION = ?, STARTER_CAPACITOR = ?, OPERATION_CAPACITOR = ?, PHASE = ?, VOLTAGE = ?, POLE = ?, MOTER_SPEED = ?, FREQUENCY = ?, TEST_CONDITION = ? WHERE SPECIMEN_ID = ?",
                    (SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_ID, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION, SPECIMEN_ID)
                )

            connection.commit()
            connection.close()
            self.specimen_ui.label_69.setText("Great : Details Save....")
            self.specimen_ui.label_69.show()
            self.load_Data()
        else :
            print("go ahead is no...")
    def deleteSpecimen(self):
        if(self.specimen_ui.label_54.text() != ""):
            close = QMessageBox()
            close.setText("Confirm Deleteing SpecimenID : "+str(self.specimen_ui.label_54.text()))
            close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            close = close.exec()
            if close == QMessageBox.Yes:
                    connection = sqlite3.connect("Rolla.db")
                    with connection:        
                            cursor = connection.cursor()
                            cursor.execute("DELETE FROM SPECIMEN_MST WHERE SPECIMEN_ID ='"+str(self.specimen_ui.label_54.text()+"'") )                   
                    connection.commit()                    
                    connection.close()
                    
                    self.specimen_ui.label_69.setText("Record Deleted Successfully.")                   
                    self.specimen_ui.label_69.show()                    
                    self.load_Data()
            else:
                    self.specimen_ui.label_69.setText("Canceled Delete..")                   
                    self.specimen_ui.label_69.show()

    def fetchSpecimenData(self):
        self.specimen_ui.pushButton_2.setDisabled(False)
        self.specimen_ui.pushButton_4.setDisabled(False)
        self.specimen_ui.pushButton_5.setDisabled(True)
        row = self.specimen_ui.tableWidget.currentRow() 
        if (row != -1):
            self.specimen_ui.label_54.setText(str(self.specimen_ui.tableWidget.item(row, 0).text()).zfill(3))
            self.specimen_ui.lineEdit.setText(str(self.specimen_ui.tableWidget.item(row, 1).text()))
            self.specimen_ui.lineEdit_2.setText(str(self.specimen_ui.tableWidget.item(row, 2).text()))
            self.specimen_ui.lineEdit_3.setText(str(self.specimen_ui.tableWidget.item(row, 3).text()))
            self.specimen_ui.lineEdit_11.setText(str(self.specimen_ui.tableWidget.item(row, 4).text()))
            self.specimen_ui.lineEdit_6.setText(str(self.specimen_ui.tableWidget.item(row, 5).text()))
            self.specimen_ui.lineEdit_9.setText(str(self.specimen_ui.tableWidget.item(row, 6).text()))
            self.specimen_ui.lineEdit_20.setText(str(self.specimen_ui.tableWidget.item(row, 7).text()))
            self.specimen_ui.lineEdit_5.setText(str(self.specimen_ui.tableWidget.item(row, 8).text()))
            self.specimen_ui.lineEdit_21.setText(str(self.specimen_ui.tableWidget.item(row, 9).text()))
            self.specimen_ui.lineEdit_22.setText(str(self.specimen_ui.tableWidget.item(row, 10).text()))
            self.specimen_ui.lineEdit_10.setText(str(self.specimen_ui.tableWidget.item(row, 11).text()))
            self.specimen_ui.lineEdit_8.setText(str(self.specimen_ui.tableWidget.item(row, 12).text()))
            self.specimen_ui.lineEdit_13.setText(str(self.specimen_ui.tableWidget.item(row, 13).text()))
            self.specimen_ui.lineEdit_12.setText(str(self.specimen_ui.tableWidget.item(row, 14).text()))
            self.specimen_ui.lineEdit_16.setText(str(self.specimen_ui.tableWidget.item(row, 15).text()))
            self.specimen_ui.lineEdit_17.setText(str(self.specimen_ui.tableWidget.item(row, 16).text()))
            self.specimen_ui.lineEdit_7.setText(str(self.specimen_ui.tableWidget.item(row, 17).text()))
            self.specimen_ui.textEdit.setText(str(self.specimen_ui.tableWidget.item(row, 18).text()))
        else:
            print("select the row...")
    def validation(self):
                self.go_ahead="No"
                if (self.specimen_ui.lineEdit.text() == ""):
                   self.specimen_ui.label_69.setText("Job Name : Should Not Be Empty..." )            
                   self.specimen_ui.label_69.show()      
                elif (self.specimen_ui.lineEdit_2.text() == ""):
                    self.specimen_ui.label_69.setText("Batch ID : Should Not Be Empty...")                
                    self.specimen_ui.label_69.show()    
                elif (self.specimen_ui.lineEdit_3.text() == ""):
                    self.specimen_ui.label_69.setText("Product ID : Should Not Be Empty...") 
                    self.specimen_ui.label_69.show()                   
                   
                elif (self.specimen_ui.lineEdit_11.text() == ""):
                    self.specimen_ui.label_69.setText("Model : Should Not Be Empty...")                   
                    self.specimen_ui.label_69.show() 
                elif (self.specimen_ui.lineEdit_6.text() == ""):
                    self.specimen_ui.label_69.setText("Part No. : Should Not Be Empty...")                   
                    self.specimen_ui.label_69.show()         
                elif (self.specimen_ui.lineEdit_9.text() == ""):
                    self.specimen_ui.label_69.setText("Current : Should Not Be Empty...")                  
                    self.specimen_ui.label_69.show() 
                elif (self.specimen_ui.lineEdit_13.text() == ""):
                    self.specimen_ui.label_69.setText("Phase : Should Not Be Empty...")                   
                    self.specimen_ui.label_69.show() 
                elif (self.specimen_ui.lineEdit_20.text() == ""):
                    self.specimen_ui.label_69.setText("Client : Should Not Be Empty...")                   
              
                elif (self.specimen_ui.lineEdit_5.text() == ""):
                    self.specimen_ui.label_69.setText("Serial No. : Should Not Be Empty...")                   
                    self.specimen_ui.label_69.show() 
                elif (self.specimen_ui.lineEdit_21.text() == ""):
                    self.specimen_ui.label_69.setText("Output Power : Should Not Be Empty...")                   
                    self.specimen_ui.label_69.show() 
                elif (self.specimen_ui.lineEdit_22.text() == ""):
                    self.specimen_ui.label_69.setText("Rotational Direction : Should Not Be Empty...")                   
                    self.specimen_ui.label_69.show() 
                elif (self.specimen_ui.lineEdit_10.text() == ""):
                    self.specimen_ui.label_69.setText("Starter Capacitor : Should Not Be Empty...")                   
                    self.specimen_ui.label_69.show() 
                elif (self.specimen_ui.lineEdit_8.text() == ""):
                    self.specimen_ui.label_69.setText("Operation Capacitor : Should Not Be Empty...") 
                    self.specimen_ui.label_69.show()       
                elif (self.specimen_ui.lineEdit_12.text() == ""):
                    self.specimen_ui.label_69.setText("Voltage : Should Not Be Empty...")                   
                    self.specimen_ui.label_69.show() 
                elif (self.specimen_ui.lineEdit_16.text() == ""):
                    self.specimen_ui.label_69.setText("Pole : Should Not Be Empty...") 
                    self.specimen_ui.label_69.show() 
                elif (self.specimen_ui.lineEdit_17.text() == ""):
                    self.specimen_ui.label_69.setText("Moter Speed : Should Not Be Empty...")                   
                    self.specimen_ui.label_69.show() 
                elif (self.specimen_ui.lineEdit_7.text() == ""):
                    self.specimen_ui.label_69.setText("Frequency : Should Not Be Empty...") 
                    self.specimen_ui.label_69.show() 
                elif (self.specimen_ui.textEdit.toPlainText() == ""):
                    self.specimen_ui.label_69.setText("Test Condition : Should Not Be Empty...")                   
                    self.specimen_ui.label_69.show() 
                else:
                        self.go_ahead="Yes"
        

    def resetFields(self):
        connection = sqlite3.connect("Rolla.db")
        results=connection.execute("select seq + 1 from sqlite_sequence WHERE name = 'SPECIMEN_MST'")       
        for x in results:      
                 self.specimen_ui.label_54.setText(str(x[0]).zfill(3))   
        connection.close()
        self.specimen_ui.pushButton_2.setDisabled(True)
        self.specimen_ui.pushButton_4.setDisabled(True)
        self.specimen_ui.pushButton_5.setDisabled(False)
        lineEdits = [
            self.specimen_ui.lineEdit, self.specimen_ui.lineEdit_2, self.specimen_ui.lineEdit_3, self.specimen_ui.lineEdit_11, 
            self.specimen_ui.lineEdit_6, self.specimen_ui.lineEdit_9, self.specimen_ui.lineEdit_20, self.specimen_ui.lineEdit_5, 
            self.specimen_ui.lineEdit_21, self.specimen_ui.lineEdit_22, self.specimen_ui.lineEdit_10, self.specimen_ui.lineEdit_8, 
            self.specimen_ui.lineEdit_13, self.specimen_ui.lineEdit_12, self.specimen_ui.lineEdit_16, self.specimen_ui.lineEdit_17, 
            self.specimen_ui.lineEdit_7, self.specimen_ui.textEdit
        ]
        for line_edit in lineEdits:
            line_edit.setText("")
        
    
    def addSpecimeDetails(self):
        self.validation()
        if self.go_ahead == "Yes":
            fieldsValue = []
            lineEdits = [  
                self.specimen_ui.lineEdit, self.specimen_ui.lineEdit_2, self.specimen_ui.lineEdit_3, self.specimen_ui.lineEdit_11, 
                self.specimen_ui.lineEdit_6, self.specimen_ui.lineEdit_9, self.specimen_ui.lineEdit_20, self.specimen_ui.lineEdit_5, 
                self.specimen_ui.lineEdit_21, self.specimen_ui.lineEdit_22, self.specimen_ui.lineEdit_10, self.specimen_ui.lineEdit_8, 
                self.specimen_ui.lineEdit_13, self.specimen_ui.lineEdit_12, self.specimen_ui.lineEdit_16, self.specimen_ui.lineEdit_17, 
                self.specimen_ui.lineEdit_7, self.specimen_ui.textEdit
            ]
            for line_edit in lineEdits:
                if isinstance(line_edit, QTextEdit):
                    fieldsValue.append(line_edit.toPlainText())
                else:
                    fieldsValue.append(line_edit.text())
            print(fieldsValue)
            
            column_names = [
                "JOB_NAME", "BATCH_ID", "PRODUCT_ID", "MODEL", "PART_NO", "CURRENT", "CILENT", 
                "SERIAL_NO", "OUTPUT_POWER", "ROTATIONAL_DIRECTION", "STARTER_CAPACITOR", "OPERATION_CAPACITOR", 
                "PHASE", "VOLTAGE", "POLE", "MOTER_SPEED", "FREQUENCY", "TEST_CONDITION"
            ]
            SPECIMEN_ID = self.specimen_ui.label_54.text()
            JOB_NAME = fieldsValue[0]
            BATCH_ID = fieldsValue[1]
            PRODUCT_ID = fieldsValue[2]
            MODEL = fieldsValue[3]
            PART_NO = fieldsValue[4]
            CURRENT = fieldsValue[5]
            CILENT = fieldsValue[6]
            SERIAL_NO = fieldsValue[7]
            OUTPUT_POWER = fieldsValue[8]
            ROTATIONAL_DIRECTION = fieldsValue[9]
            STARTER_CAPACITOR = fieldsValue[10]
            OPERATION_CAPACITOR = fieldsValue[11]
            PHASE = fieldsValue[12]
            VOLTAGE = fieldsValue[13]
            POLE = fieldsValue[14]
            MOTER_SPEED = fieldsValue[15]
            FREQUENCY = fieldsValue[16]
            TEST_CONDITION = fieldsValue[17]
            
            connection = sqlite3.connect("Rolla.db")
            with connection:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO SPECIMEN_MST (SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_ID, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?,?, ?, ?, ?)",(SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_ID, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION))
                self.specimen_ui.label_69.setText("Great : Specimen added......")
                self.specimen_ui.label_69.show()
            connection.commit()
            connection.close()
            self.load_Data()
        else :
            print("go ahead is no...")

    def delete_all_records(self):
        i = self.specimen_ui.tableWidget.rowCount()       
        while (i>0):      
            i=i-1
            self.specimen_ui.tableWidget.removeRow(i)
    def load_Data(self):
        self.delete_all_records()
        connection = sqlite3.connect("Rolla.db")  
        results=connection.execute("SELECT SPECIMEN_ID, JOB_NAME, BATCH_ID, PRODUCT_ID, MODEL, PART_NO, CURRENT, CILENT, SERIAL_NO, OUTPUT_POWER, ROTATIONAL_DIRECTION, STARTER_CAPACITOR, OPERATION_CAPACITOR, PHASE, VOLTAGE, POLE, MOTER_SPEED, FREQUENCY, TEST_CONDITION FROM SPECIMEN_MST")
        for row_number, row_data in enumerate(results):            
            self.specimen_ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data): 
                self.specimen_ui.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str (data))) 
        
        connection.commit()
        connection.close()  
         
        
        if(self.specimen_ui.tableWidget.rowCount() > 0):
            
            self.specimen_ui.lineEdit.setText(str(self.specimen_ui.tableWidget.item(0, 1).text()))
            self.specimen_ui.lineEdit_2.setText(str(self.specimen_ui.tableWidget.item(0, 2).text()))
            self.specimen_ui.lineEdit_3.setText(str(self.specimen_ui.tableWidget.item(0, 3).text()))
            self.specimen_ui.lineEdit_11.setText(str(self.specimen_ui.tableWidget.item(0, 4).text()))
            self.specimen_ui.lineEdit_6.setText(str(self.specimen_ui.tableWidget.item(0, 5).text()))
            self.specimen_ui.lineEdit_9.setText(str(self.specimen_ui.tableWidget.item(0, 6).text()))
            self.specimen_ui.lineEdit_20.setText(str(self.specimen_ui.tableWidget.item(0, 7).text()))
            self.specimen_ui.lineEdit_5.setText(str(self.specimen_ui.tableWidget.item(0, 8).text()))
            self.specimen_ui.lineEdit_21.setText(str(self.specimen_ui.tableWidget.item(0, 9).text()))
            self.specimen_ui.lineEdit_22.setText(str(self.specimen_ui.tableWidget.item(0, 10).text()))
            self.specimen_ui.lineEdit_10.setText(str(self.specimen_ui.tableWidget.item(0, 11).text()))
            self.specimen_ui.lineEdit_8.setText(str(self.specimen_ui.tableWidget.item(0, 12).text()))
            self.specimen_ui.lineEdit_13.setText(str(self.specimen_ui.tableWidget.item(0, 13).text()))
            self.specimen_ui.lineEdit_12.setText(str(self.specimen_ui.tableWidget.item(0, 14).text()))
            self.specimen_ui.lineEdit_16.setText(str(self.specimen_ui.tableWidget.item(0, 15).text()))
            self.specimen_ui.lineEdit_17.setText(str(self.specimen_ui.tableWidget.item(0, 16).text()))
            self.specimen_ui.lineEdit_7.setText(str(self.specimen_ui.tableWidget.item(0, 17).text()))
            self.specimen_ui.textEdit.setText(str(self.specimen_ui.tableWidget.item(0, 18).text()))

            
            
class AnalogWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        # Setup the UI main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.select_Report_Ui = SelectReport().select_Report_Ui
        self.select_report = SelectReport(self)
        self.timer=QtCore.QTimer() 
        self.timer.start(1)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.setDateAndTime)
        
        # self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.widget_4.setGaugeTheme(6)
        self.ui.widget_5.setGaugeTheme(6)
        self.ui.widget_6.setGaugeTheme(6)
        self.ui.widget_8.setGaugeTheme(6)
        self.refrashMeter()
        self.ui.widget_4.units = "RPM"
        
        self.ui.widget_5.units = "KW."
        self.ui.widget_6.units = "N-m"
        self.ui.widget_8.units = "℃"
        self.ui.label_27.hide()
        self.ui.label_28.hide()
        self.ui.label_29.hide()
        self.ui.label_36.hide()
        self.ui.label_59.hide()
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.ui.lineEdit_20)
        self.ui.lineEdit_20.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.ui.lineEdit_21)
        self.ui.lineEdit_21.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.ui.lineEdit_22)
        self.ui.lineEdit_22.setValidator(input_validator)
        self.ui.label_35.hide()
        self.ui.label_37.hide()
        self.ui.pushButton_7.setDisabled(True)
        self.ui.pushButton_8.setDisabled(True)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_7.clicked.connect(self.meterStart)
        self.ui.pushButton_2.clicked.connect(self.openSetMaxDialog)
        self.ui.pushButton_14.clicked.connect(self.openSpecimen)
        self.ui.pushButton_9.clicked.connect(self.openSelectReport)
        self.ui.pushButton_5.clicked.connect(self.refrashMeter)
        self.ui.lineEdit_22.mousePressEvent = lambda event: self.ui.pushButton_5.setEnabled(True)
        # self.ui.lineEdit_22.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_22)
        # self.ui.lineEdit_21.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_21)
        # self.ui.lineEdit_20.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_20)
        # self.ui.lineEdit_9.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_9)
        # self.ui.lineEdit_10.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_10)
        # self.ui.lineEdit_11.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_11)
        # self.ui.lineEdit_19.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_19)
        # self.ui.lineEdit.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit)
        # self.ui.lineEdit_2.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_2)
        # self.ui.lineEdit_3.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_3)
        # self.ui.lineEdit_4.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_4)
        # self.ui.lineEdit_5.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_5)
        # self.ui.lineEdit_6.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_6)
        # self.ui.lineEdit_8.mousePressEvent = lambda event: self.openKeyBoard(self.ui.lineEdit_8)
        

        
        
        
        # Set self.setValue only if the text is not empty
        
    def setDateAndTime(self):
        # self.ui.label_60.setText(datetime.datetime.now().strftime("%d %b %Y %H : %M : %S"))
        # self.select_Report_Ui.label_72.setText(datetime.datetime.now().strftime("%d %b %Y %H : %M : %S"))
        current_time = datetime.datetime.now().strftime("%d %b %Y %H : %M : %S")
        self.ui.label_60.setText(current_time)
        self.select_report.select_Report_Ui.label_72.setText(current_time)
    def refrashMeter(self):
        self.ui.pushButton_7.setDisabled(False)
        connection = sqlite3.connect("Rolla.db")
        # cursor = connection.cursor()
        results=connection.execute("SELECT MAX_MOTER_SPEED, MAX_POWER, MAX_TORQUE, MAX_SerOT FROM TEST_MST")
        for x in results:
            self.ui.widget_4.maxValue = int(x[0])
            self.ui.widget_4.update() 
            self.ui.widget_5.maxValue = int(x[1]) 
            self.ui.widget_5.update()
            self.ui.widget_6.maxValue = int(x[2]) 
            self.ui.widget_6.update()
            self.ui.widget_8.maxValue = int(x[3]) 
            self.ui.widget_8.update()
        connection.close()
        connection = sqlite3.connect("Rolla.db")
        results=connection.execute("SELECT SPECIMEN_ID, TEST_ID FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)")
        for x in results:
            self.ui.label_37.setText("Specimen ID: "+ str(x[0]))
            self.ui.label_35.setText("Test ID: "+ str(x[1]).zfill(3))
            self.ui.label_37.show()
            self.ui.label_35.show()
        connection.close()
    
    def meterStart(self):
        global counterForSpeed
        global counterForPower
        global counterForTorque
        counterForSpeed = 0
        counterForPower = 0 
        counterForTorque = 0
        self.speedValue = 0 if self.ui.lineEdit_22.text() == "" else int(self.ui.lineEdit_22.text())
        self.torqueValue = 0 if self.ui.lineEdit_20.text() == "" else int(self.ui.lineEdit_20.text())
        self.powerValue = 0 if self.ui.lineEdit_21.text() == "" else int(self.ui.lineEdit_21.text())
        if (self.speedValue == 0):
            self.ui.label_28.setText("Oops: Speed is Empty!!!")
            self.ui.label_28.show()
        elif(self.powerValue == 0 ):
            self.ui.label_28.setText("Oops: Power is Empty!!!") 
            self.ui.label_28.show()
        elif(self.torqueValue == 0 ):
            self.ui.label_28.setText("Oops: Torque is Empty!!!")
            self.ui.label_28.show()  
        else:
            self.ui.label_28.hide()

        self.timerForSpeed=QtCore.QTimer()       
        self.timerForSpeed.start(1) 
        self.timerForSpeed.timeout.connect(self.setValueToMeter)
        self.timerForTorque=QtCore.QTimer()       
        self.timerForTorque.start(1) 
        self.timerForTorque.timeout.connect(self.setValueToMeter)
        self.timerForPower=QtCore.QTimer()       
        self.timerForPower.start(1) 
        self.timerForPower.timeout.connect(self.setValueToMeter)
        
    def setValueToMeter(self):
        self.ui.pushButton_7.setDisabled(True)
        self.ui.pushButton_8.setDisabled(False)
        if (self.speedValue > 1 ):
            self.ui.label_27.setText("Motor Is Running...")
            self.ui.label_27.show()
        if(self.torqueValue > 1 ):
            self.ui.label_36.setText("Torque Meter Running...")
            self.ui.label_36.show() 
        if(self.powerValue > 1):
            self.ui.label_29.setText("Power Meter Running...") 
            self.ui.label_29.show()
        
        global counterForSpeed
        global counterForPower
        global counterForTorque
        if counterForSpeed > self.speedValue :
            self.timerForSpeed.stop()
            if counterForSpeed == 1 :
                pass
            else:
                self.ui.label_27.setText("Moter Stoped...")
                self.ui.label_27.show()

        else:    
            self.ui.widget_4.updateValue(counterForSpeed)
            counterForSpeed = counterForSpeed + 1
        if counterForTorque > self.torqueValue :
            self.timerForTorque.stop()
            if counterForSpeed == 1 :
                pass
            else:
                self.ui.label_36.setText("Torque Stoped...")
                self.ui.label_36.show()
        else:    
            self.ui.widget_6.updateValue(counterForTorque)
            counterForTorque = counterForTorque + 1
        if counterForPower > self.powerValue :
            self.timerForPower.stop()
            if counterForSpeed == 1 :
                pass
            else:
                self.ui.label_29.setText("Power Stoped...")
                self.ui.label_29.show()
        else:
            self.ui.widget_5.updateValue(counterForPower)
            counterForPower = counterForPower + 1
        # self.ui.label_27.hide()
        
    def openSetMaxDialog(self):
        self.setup = Setup(self)
        self.setup.show()
    def openKeyBoard(self, line):
        self.callKeyBo = DialogNumericKeyBo(line)
        self.callKeyBo.exec_()    
    def openSpecimen(self): 
        self.specimen = Specimen(self)
        self.specimen.show()  
    def openSelectReport(self): 
        self.selectReport = SelectReport(self)
        self.selectReport.show()
# class PlotCanvas(FigureCanvas):
#     def __init__(self, parent=None, width=8, height=5, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         #fig.savefig('ssdsd.png')
#         self.axes = fig.add_subplot(111)        
#         FigureCanvas.__init__(self, fig)
#         #FigureCanvas.setStyleSheet("background-color:red;")
#         FigureCanvas.setSizePolicy(self,
#                 QSizePolicy.Expanding,
#                 QSizePolicy.Expanding)
#         FigureCanvas.updateGeometry(self)       
        
#         self.plot()        
        
        
#     def plot(self):
#         ax = self.figure.add_subplot(111)
       
#         ax.set_facecolor('#CCFFFF')   
#         ax.minorticks_on()
#         ax2 = ax.twinx()
#         color = 'tab:green'
#         ax2.set_ylabel('TEMP (.C)', color = color)
# #        ax.set_xlim(0,200)
# #        ax.set_ylim(0,200)
#         ax2.set_ylim(0,200)
        
#         ax.grid(which='major', linestyle='-', linewidth='0.50', color='black')
#         ax.grid(which='minor', linestyle=':', linewidth='0.50', color='black')
        
#         self.s=[]
#         self.t=[]
#         self.graph_ids=[]    
#         self.x_num=[0.0]
#         self.y_num=[0.0]
#         self.r_num=[0.0]
#         self.test_type="Tensile"
#         self.color=['b','r','g','y','k','c','m','b']
#         #ax.set_title('Test Id=32         Samples=3       BreakLoad(Kg)=110        Length(mm)=3')         
        
        
        
#         connection = sqlite3.connect("mdr.db")
#         results=connection.execute("SELECT GRAPH_SCALE_CELL_2,GRAPH_SCALE_CELL_1 from SETTING_MST") 
#         for x in results:
#              ax.set_xlim(0,int(x[0]))
#              ax.set_ylim(0,int(x[1]))            
# #             self.xlim=int(x[0])
# #             self.ylim=int(x[1])            
#         connection.close()
        
#         connection = sqlite3.connect("mdr.db")
#         results=connection.execute("SELECT GRAPH_ID FROM TEST_MST_MDR WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR)") 
#         for x in results:
#              self.graph_ids.append(x[0])             
#         connection.close()
        
        
#         for g in range(len(self.graph_ids)):
#             self.x_num=[0.0]
#             self.y_num=[0.0]
        
#             connection = sqlite3.connect("mdr.db")               
#             results=connection.execute("SELECT X_NUM,Y_NUM,R_NUM FROM GRAPH_MST WHERE X_NUM > 0 AND  GRAPH_ID='"+str(self.graph_ids[g])+"'")
#             for k in results:        
#                 self.x_num.append(k[0])
#                 self.y_num.append(k[1])
#                 self.r_num.append(k[2])
#             connection.close() 
        
#             if(g < 8 ):
#                 ax.plot(self.x_num,self.y_num, self.color[g],label="Specimen_"+str(g+1))
#                 ax2.plot(self.x_num,self.r_num, 'g',label="Temparature")
        
        
#         ax.set_xlabel('TIME (Min)')
#         ax.set_ylabel('TORQUE(N)')
       
#         #self.connect('motion_notify_event', mouse_move)
#         ax.legend()
#         #ax2.legend() 
#         self.draw()
#         self.figure.savefig('last_graph.png',dpi=100)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AnalogWindow()
    window.show()
    # window.select_report.show()
    sys.exit(app.exec_())