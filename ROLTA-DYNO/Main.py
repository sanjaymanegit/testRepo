import os, sys
import time, sqlite3
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtGui import QFontDatabase
from Analog import Ui_MainWindow
from SetMaxDailog import Ui_Dialog
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

class SetMaxDailog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        
        self.setup_ui = Ui_Dialog()
        self.setup_ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.setup_ui.lineEdit_20)
        self.setup_ui.lineEdit_20.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.setup_ui.lineEdit_21)
        self.setup_ui.lineEdit_21.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.setup_ui.lineEdit_22)
        self.setup_ui.lineEdit_22.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.setup_ui.lineEdit_23)
        self.setup_ui.lineEdit_23.setValidator(input_validator)
        self.setup_ui.pushButton_2.clicked.connect(self.setMaxValue)
    def setMaxValue(self):
        if (self.setup_ui.lineEdit_22.text() == ""):
            self.setup_ui.label_19.setText("Oops : \n Max Speed is \n Empty!!!")
        elif ( self.setup_ui.lineEdit_21.text() == ""):
            self.setup_ui.label_19.setText("Oops : \n Max Power is \n Empty!!!")
        elif ( self.setup_ui.lineEdit_20.text() == ""):
            self.setup_ui.label_19.setText("Oops : \n Max Torque is \n Empty!!!")
        elif ( self.setup_ui.lineEdit_23.text() == ""):
            self.setup_ui.label_19.setText("Oops : \n Max SerOT is \n Empty!!!")    
        else:
            connection = sqlite3.connect("Rolla.db")
            cursor = connection.cursor()
            with connection:
                cursor = connection.cursor() 
                cursor.execute("UPDATE CONFIGURE_METER SET MAX_MOTER_SPEED = '"+str(self.setup_ui.lineEdit_22.text())+"', MAX_POWER = '"+str(self.setup_ui.lineEdit_21.text())+"', MAX_TORQUE = '"+str(self.setup_ui.lineEdit_20.text())+"', MAX_SerOT = '"+str(self.setup_ui.lineEdit_23.text())+"'")
            connection.commit()
            connection.close()
            self.setup_ui.label_19.setText("Recorded : \n Max Setup is \n Successful!!!")   
    
            print("updated..........")



class AnalogWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        # Setup the UI main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.widget_4.setGaugeTheme(6)
        self.ui.widget_5.setGaugeTheme(7)
        self.ui.widget_6.setGaugeTheme(7)
        self.ui.widget_8.setGaugeTheme(7)
        self.refrashMeter()
        self.ui.widget_4.units = "RPM"
        
        self.ui.widget_5.units = "KW."
        self.ui.widget_6.units = "N-m"
        self.ui.widget_8.units = "℃"
        self.ui.label_23_1.hide()
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.ui.lineEdit_20)
        self.ui.lineEdit_20.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.ui.lineEdit_21)
        self.ui.lineEdit_21.setValidator(input_validator)
        input_validator = QRegExpValidator(reg_ex, self.ui.lineEdit_22)
        self.ui.lineEdit_22.setValidator(input_validator)
        self.ui.pushButton_7.clicked.connect(self.meterStart)
        self.ui.pushButton_2.clicked.connect(self.openSetMaxDialog)
        self.ui.pushButton_5.clicked.connect(self.refrashMeter)
        
        
        
        # Set self.setValue only if the text is not empty
        

    def refrashMeter(self):
        connection = sqlite3.connect("Rolla.db")
        # cursor = connection.cursor()
        results=connection.execute("SELECT MAX_MOTER_SPEED, MAX_POWER, MAX_TORQUE, MAX_SerOT FROM CONFIGURE_METER")
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
            self.ui.label_23_1.setText("Oops: Speed is Empty!!!")
            self.ui.label_23_1.show()
        elif(self.torqueValue == 0 ):
            self.ui.label_23_1.setText("Oops: Torque is Empty!!!")
            self.ui.label_23_1.show() 
        elif(self.powerValue == 0 ):
            self.ui.label_23_1.setText("Oops: Power is Empty!!!") 
            self.ui.label_23_1.show()      
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
        if (self.speedValue > 0):
            self.ui.label_23_1.setText("Running....")
            self.ui.label_23_1.show()
        elif(self.torqueValue > 0 ):
            self.ui.label_23_1.setText("Running....")
            self.ui.label_23_1.show() 
        elif(self.powerValue > 0 ):
            self.ui.label_23_1.setText("Running....") 
            self.ui.label_23_1.show()
        # self.minValue = 0
        global counterForSpeed
        global counterForPower
        global counterForTorque
        if counterForSpeed > self.speedValue :
            self.timerForSpeed.stop()
        else:    
            self.ui.widget_4.updateValue(counterForSpeed)
            counterForSpeed = counterForSpeed + 1
        if counterForTorque > self.torqueValue :
            self.timerForTorque.stop()

        else:    
            self.ui.widget_6.updateValue(counterForTorque)
            counterForTorque = counterForTorque + 1
        if counterForPower > self.powerValue :
            self.timerForPower.stop()
        else:
            self.ui.widget_5.updateValue(counterForPower)
            counterForPower = counterForPower + 1
    
    
    def openSetMaxDialog(self):
        self.dialog = SetMaxDailog(self)
        self.dialog.exec_()
        




    # def checkMoterSpeed(self):
    #     setValue = 15
    #     value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27]  
    #     for x in value:
    #         if x <= setValue:
    #             self.ui.widget_4.updateValue(x)
    #             time.sleep(0.001)  
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnalogWindow()
    window.show()
    sys.exit(app.exec_())