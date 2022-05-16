# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'print_popup.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cups

class P_POP_TEST_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 241)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 19, 511, 191))
        self.frame.setStyleSheet("background-color: rgb(210, 255, 218);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 150, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(110, 60, 301, 74))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.i=0 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please Select Printer"))
        self.pushButton.setText(_translate("MainWindow", "Print"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))        
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.print_pdf)
        self.load_data()
        
    def load_data(self):
       conn = cups.Connection ()
       self.printers = conn.getPrinters ()
       file="./reports/test_report.pdf"       
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
        file="./reports/test_report.pdf"        
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
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = P_POP_TEST_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
