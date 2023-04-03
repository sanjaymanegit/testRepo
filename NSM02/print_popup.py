
from PyQt5 import QtCore, QtGui, QtWidgets
import cups
import datetime
import time
from PyQt5.QtCore import QDate

class P_POPUi_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 40, 711, 381))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(470, 290, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(580, 10, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./images/nms.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 270, 111, 81))
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
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 270, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"border-radius:20px;\n"
"")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(330, 270, 101, 81))
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
        self.label_4.setGeometry(QtCore.QRect(10, 20, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(50, 120, 301, 74))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")   
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.i=0
        self.radio_buttons = []

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        self.pushButton_6.setText(_translate("MainWindow", "Print"))
        self.pushButton_7.setText(_translate("MainWindow", "Reset"))
        self.pushButton_8.setText(_translate("MainWindow", "Close"))
        self.label_4.setText(_translate("MainWindow", "Please Select Printer"))
        self.pushButton_8.clicked.connect(MainWindow.close)        
        self.load_data()        
        self.pushButton_6.clicked.connect(self.show_printer_name)
    
        
    def show_printer_name(self):
        print("Arry Length:"+str(self.verticalLayout.count()))                
        for btn in self.radio_buttons:
            if btn.isChecked():
                print(btn.text())
                conn = cups.Connection() 
                file="./reports/ur_reports.pdf"      
                printer=str(btn.text())
                conn.printFile(printer,file,"Report",{})
                self.label_4.setText("Print Started On ( "+str(btn.text())+" )")
                self.pushButton_6.setDisabled(True)
    
    
    def load_data(self):
       conn = cups.Connection ()
       self.printers = conn.getPrinters ()
       file="./reports/ur_reports.pdf"      
       for printer in self.printers:
           self.i=self.i+1           
           self.b = QtWidgets.QRadioButton(self.widget)
           font = QtGui.QFont()
           font.setPointSize(14)
           #font.setBold(True)
           #font.setWeight(75)
           self.b.setFont(font)
           self.b.setObjectName("b")
           self.b.setText(printer)
           self.b.setAccessibleName(str(self.i))
           self.verticalLayout.addWidget(self.b)
           self.radio_buttons.append(self.b)
           
'''    
    def load_data(self):
       conn = cups.Connection ()
       self.printers = conn.getPrinters ()
       file="./reports/Reportxxx.pdf"       
       for printer in self.printers:
           self.i=self.i+1           
           self.radioButton = QtWidgets.QRadioButton(self.widget)
           font = QtGui.QFont()
           font.setPointSize(10)
           font.setBold(True)
           font.setWeight(75)
           self.radioButton.setFont(font)
           self.radioButton.setObjectName("radioButton_")
           self.radioButton.setText(printer)
           self.verticalLayout.addWidget(self.radioButton)
           #self.radioButton.clicked.connect(self.getPrinter)     
           
    def print_pdf(self):                
        conn = cups.Connection() 
        file="./reports/ur_reports.pdf"        
        print("length of printers :"+str(len(self.printers)))
        if(len(self.printers) > 0):
            printer=self.radioButton.text()
            try:               
               conn.printFile(printer,file,"Report",{})        
            except cups.IPPError as e:
               print ("IPP status is %d" +str("x"))
            self.label.setText("Print Started !!")
            print ("Selected printer xxx:"+str(printer))  
            print ("Done")
            self.pushButton.setDisabled(True)
  '''      
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = P_POPUi_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
