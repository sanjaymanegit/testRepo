# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'print_popup.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cups
from escpos.connections import getUSBPrinter
import usb.core
import usb.util
import os,sys
import sqlite3


class P_POPUi_MainWindow(object):
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
        #self.pushButton.clicked.connect(self.dot_matrix_print)
        self.pushButton.clicked.connect(self.print_pdf_report)
        self.load_data()
        
    def load_data(self):
       '''
       os.system("lsusb >> /home/pi/Products/WT/lsusb_data.txt")        
       try:
           f = open('/home/pi/Products/WT/lsusb_data.txt','r')
           for line in f:
                cnt=0
                cnt=int(line.find("Printer"))
                if cnt > 0 :
                     self.pushButton.setEnabled(True)
                     break
                     os.system("rm -rf /home/pi/Products/WT/lsusb_data.txt") 
                else:
                     self.pushButton.setDisabled(True)
                    
           f.close()
       except:
            print("Error:")
       '''     
       conn = cups.Connection ()
       printers = conn.getPrinters ()
       file="./reports/Reportxxx.pdf"       
       for printer in printers:
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
           
    def print_pdf_report(self):                
        conn = cups.Connection() 
        file="./reports/TodaysReport.pdf"
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
        for k in range(1,2):
            name=str("self.radioButton_1")
            if (self.radioButton_1.isChecked()):        
                printer=self.name.text()          
        '''
        
    
    def dot_matrix_print(self):        
        self.serial_id=""
        self.charges=""
        self.vehical_no=""
        self.first_wt=""
        self.first_wt_date=""
        self.first_wr_time=""
        self.second_wt=""
        self.second_wt_date=""
        self.second_wt_time=""
        self.net_wt=""
        self.supplier_name=""
        self.party_name=""
        self.material=""        
        self.company_name=""
        self.address=""
        self.first_wt_mode=""
        self.second_wt_mode=""
        
        connection = sqlite3.connect("wt.db")       
        results=connection.execute("SELECT COMPANY_NAME,COMPANY_ADDR FROM USER_RIGHT_SET")
        for x in results:
              self.company_name=str(x[0])
              self.address=str(x[1])        
        connection.close()
        
        dev = usb.core.find(idVendor=0x04b8, idProduct=0x0005)
        try:
             dev.reset()
        except:
             print("Error")
        printer = getUSBPrinter()(idVendor=0x04b8,  # USB vendor and product Ids for Bixolon SRP-350plus
                              idProduct=0x0005,  # printer
                              inputEndPoint=0x82,
                              outputEndPoint=0x01)

        printer.text("=============================================================================\n\r")
        printer.charSpacing(1)            
        #printer.bold()
        printer.text("              "+str(self.company_name)+"         \n\r" )              
        printer.text("           "+str(self.address)+"         \n\r" )
        #printer.bold(False)
        printer.align("left")
        printer.text("=============================================================================\n\r")        
       
        
        
        connection = sqlite3.connect("wt.db") 
        results=connection.execute("SELECT SERIAL_ID_DISPLY,VEHICLE_NO,PARTY_NAME,SUPPLIER_NAME,TRANSPORT_NAME,MATERIAL_NAME,GROSS_WT_DATE ,GROSS_WT_VAL, TARE_WT_DATE ,TARE_WT_VAL  ,NET_WEIGHT_VAL, (IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT FROM WEIGHT_MST_VW LIMIT 5 ") 
        for x in results:
             printer.text("Party Name:"+str(x[2])+"  Supplier Name: "+str(x[3])+"     Transport:"+str(x[4])+"\n\r")
             printer.text("Transport Name:"+str(x[5])+"\n\r")
             printer.text("----------------------------------------------------------------------------- \n\r")
             printer.text("Sr.ID.|Vehical.No|GrossWtDt|GrossWt|TareWtDt|TareWt|NetWt|Total Amount \n\r")
             printer.text("----------------------------------------------------------------------------- \n\r")        
             printer.text("|"+str(x[0])+"|"+str(x[1])+"|"+str(x[6])+"|"+str(x[7])+"|"+str(x[8])+"|"+str(x[9])+"|"+str(x[10])+"|"+str(x[10])+"\n\r")
             printer.text("----------------------------------------------------------------------------- \n\r")  
        connection.close()
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = P_POPUi_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
