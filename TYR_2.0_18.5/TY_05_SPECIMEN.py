# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TY_05_SPECIMEN.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTableWidgetItem
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class TY_05_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 1301, 691))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.operation="ADD"
        self.cs_area=0
        self.thickness=0
        self.width=0
        self.diameter=0
        self.inn_diamter=0
        self.out_diameter=0
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(360, 20, 371, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 170, 521, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        '''
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        '''
        
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setItem(0, 5, item)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(580, 160, 701, 411))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 40, 521, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)       
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        
        
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
       
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_4)
        self.lineEdit_4.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)        
        reg_ex = QRegExp("/(\d+(\.\d+)?)/")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_7)
        self.lineEdit_7.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 2, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        reg_ex = QRegExp("/(\d+(\.\d+)?)/")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_9)
        self.lineEdit_9.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 6, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget)
        reg_ex = QRegExp("/(\d+(\.\d+)?)/")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_11)
        self.lineEdit_11.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 7, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 7, 2, 1, 2)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget)
        reg_ex = QRegExp("/(\d+(\.\d+)?)/")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_12)
        self.lineEdit_12.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 7, 4, 1, 2)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        reg_ex = QRegExp("/(\d+(\.\d+)?)/")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_8)
        self.lineEdit_8.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 5, 4, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 2, 1, 2)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget)
        reg_ex = QRegExp("/(\d+(\.\d+)?)/")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_10)
        self.lineEdit_10.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 6, 4, 1, 2)
        
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)
        
        '''
        self.label_8_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8_1.setFont(font)
        self.label_8_1.setObjectName("label_8_1")
        self.gridLayout.addWidget(self.label_8_1, 2, 3, 1, 1)
        '''
        
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_5)
        self.lineEdit_5.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 0, 4, 1, 3)
        
        
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        reg_ex = QRegExp("(\d+(\.\d+)?)")
        input_validator= QRegExpValidator(reg_ex, self.lineEdit_6)
        self.lineEdit_6.setValidator(input_validator)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 1, 4, 1, 3)
        
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(340, 610, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 610, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(720, 610, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(610, 100, 371, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Specimen Information"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Spec.Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Spec.Shape"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Party"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Guage Length (Mm)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Specificfations"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Speed"))
        #item = self.tableWidget.horizontalHeaderItem(6)
        #item.setText(_translate("MainWindow", "Tested By"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Ruber"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Rectangle"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "MRF"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "HardCore"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "200"))        
        
                
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "Specimen Details"))
        self.label.setText(_translate("MainWindow", "Spec Name:"))
        self.label_2.setText(_translate("MainWindow", "Party Name:"))
        self.label_3.setText(_translate("MainWindow", "Specifications:"))
        self.label_4.setText(_translate("MainWindow", "Test Speed:"))
        self.label_5.setText(_translate("MainWindow", "Shape:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Rectangle"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cylindrical"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Pipe"))
        self.comboBox.setItemText(3, _translate("MainWindow", "DirectValue"))
        self.label_9.setText(_translate("MainWindow", "Thickness(Mm):"))
        self.label_10.setText(_translate("MainWindow", "Width(Mm):"))
        self.label_11.setText(_translate("MainWindow", "Inn.Diameter(Mm):"))
        self.label_13.setText(_translate("MainWindow", "Diameter(Mm):"))
        self.label_14.setText(_translate("MainWindow", "CS.Area(Mm2):"))
        self.label_12.setText(_translate("MainWindow", "Out.Diameter(Mm):"))
        self.label_8.setText(_translate("MainWindow", "Guage Length(Mm):"))
        #self.label_8_1.setText(_translate("MainWindow", "Tested By:"))
        self.label_7.setText(_translate("MainWindow", "Pre Load (Kg):"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Add"))
        self.pushButton_4.setText(_translate("MainWindow", "Edit"))
        self.pushButton_5.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_6.setText(_translate("MainWindow", "Delete"))
        self.pushButton_7.setText(_translate("MainWindow", "Return"))
        self.label_15.setText(_translate("MainWindow", "Error: Please fill Mandatory values"))
        self.label_15.hide()
        self.pushButton_7.clicked.connect(MainWindow.close)
        self.pushButton_5.clicked.connect(self.select_all_data)
        self.select_all_data()
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.reset_fun)
        self.pushButton_3.clicked.connect(self.add)
        self.pushButton_4.clicked.connect(self.edit)
        self.pushButton_6.clicked.connect(self.delete)
        
        '''
        self.lineEdit_2.setText("SPECIMEN_NAME")
        self.lineEdit_2.setText("Party Name")
        self.lineEdit_3.setText("specs")
        self.lineEdit_4.setText("speed")
        self.lineEdit_5.setText("pre load")
        self.lineEdit_6.setText("Guage length(Mm)")
        self.lineEdit_7.setText("Thickness")
        self.lineEdit_8.setText("width")
        self.lineEdit_9.setText("inn diameter ")
        self.lineEdit_10.setText("out diameter")
        self.lineEdit_11.setText("diameter")
        self.lineEdit_12.setText("cs area ")
        #self.lineEdit_13.setText("direct value")
        
        '''
        self.reset_fun()
        self.f_disable_inputs()
        #self.specimen_diamentions()
        self.comboBox.currentTextChanged.connect(self.specimen_diamentions)
        self.cs_area=str(self.lineEdit_12.text())
       
       
       
        
        self.lineEdit_7.textChanged.connect(self.width_onchange)
        self.lineEdit_8.textChanged.connect(self.width_onchange)
        self.lineEdit_11.textChanged.connect(self.diameter_onchange)
        self.lineEdit_9.textChanged.connect(self.out_diameter_onchange)
        self.lineEdit_10.textChanged.connect(self.out_diameter_onchange)
        self.lineEdit_12.textChanged.connect(self.direct_val)
        
    def width_onchange(self):
        if(str(self.lineEdit_7.text()) != ""):
            if(str(self.lineEdit_8.text()) != ""):
                    self.thickness=str(self.lineEdit_7.text())
                    self.width=str(self.lineEdit_8.text())
                    try:
                        self.cs_area=(float(self.thickness)) * (float(self.width))                    
                        self.lineEdit_12.setText(str(round(self.cs_area,2)))
                    except ValueError:
                        self.lineEdit_12.setText("0")
                        self.lineEdit_7.setText("0")
                        self.lineEdit_8.setText("0")
            else:
                    self.lineEdit_12.setText("0")
                    self.lineEdit_8.setText("0")
        else:
            self.lineEdit_12.setText("0")
            self.lineEdit_7.setText("0")
           
    
    def diameter_onchange(self):
        if(str(self.lineEdit_11.text()) != ""):
            self.diameter=str(self.lineEdit_11.text())
            try:
                self.cs_area=(float(self.diameter)*3.14)/2 
                self.lineEdit_12.setText(str(round(self.cs_area,2)))
            except ValueError:
                self.lineEdit_12.setText("0")
                self.lineEdit_11.setText("0")
        else:
            self.lineEdit_12.setText("0")
            self.lineEdit_11.setText("0")
            
        
    def out_diameter_onchange(self):
        if(str(self.lineEdit_9.text()) != ""):
            if(str(self.lineEdit_10.text()) != ""):
                self.inn_diamter=str(self.lineEdit_9.text())
                self.out_diameter=str(self.lineEdit_10.text())
                try:
                    self.cs_area=((float(self.out_diameter)*3.14)/2)-((float(self.inn_diamter)*3.14)/2) 
                    self.lineEdit_12.setText(str(round(self.cs_area,2)))
                except ValueError:
                    self.lineEdit_12.setText("0")
                    self.lineEdit_10.setText("0")
                    self.lineEdit_9.setText("0")
                    
            else:
                    self.lineEdit_12.setText("0")
                    self.lineEdit_10.setText("0")
        else: 
            self.lineEdit_12.setText("0")
            self.lineEdit_9.setText("0")

    def direct_val(self):
        if(str(self.lineEdit_12.text()) != ""):
            self.dc=str(self.lineEdit_12.text())
            try:
                self.cs_area=float(self.dc)
                #self.lineEdit_12.setText(str(self.cs_area))
            except ValueError:
                self.lineEdit_12.setText("0")               
        else:
            self.lineEdit_12.setText("0")
           
    def add(self):
        self.f_enabled_inputs()
        self.operation='ADD'
        self.pushButton.setText('Add')
        self.reset_fun()
        self.label_15.setText(" Please add specimen information.")
        self.label_15.show()
        self.specimen_diamentions()
    def edit(self):
        self.f_enabled_inputs()
        self.operation='EDIT'
        self.pushButton.setText('Save')
        self.label_15.setText(" Please edit specimen information.")
        self.label_15.show()
        row = self.tableWidget.currentRow()        
        if(row != -1 ):
            self.specimen_name=str(self.tableWidget.item(row, 0).text() )
            #print(" speciment_name :"+str(self.specimen_name))
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("select SPECIMEN_NAME,SPECIMEN_SPECS,PARTY_NAME,PRE_LOAD,MOTOR_SPEED,GUAGE_LENGTH_MM,THICKNESS,WIDTH,DIAMETER,C_A_AREA,IN_DIAMETER_MM,OUTER_DIAMETER_MM,SHAPE  from SPECIMEN_MST where SPECIMEN_NAME= '"+str(self.specimen_name)+"'")
            rows=results.fetchall()        
            self.lineEdit.setText(rows[0][0])    #SPECIMEN_NAME
            self.lineEdit_3.setText(rows[0][1])  #SPECIMEN_SPECS
            self.lineEdit_2.setText(rows[0][2])   #PARTY_NAME
            self.lineEdit_5.setText(str(rows[0][3])) # PRE_LOAD
            self.lineEdit_6.setText(str(rows[0][5])) #Guage 
            self.lineEdit_4.setText(str(rows[0][4])) ###Test Speed 
            
            self.lineEdit_7.setText(str(rows[0][6]))
            self.lineEdit_8.setText(str(rows[0][7]))
            self.lineEdit_9.setText(str(rows[0][10]))
            self.lineEdit_10.setText(str(rows[0][11]))
            self.lineEdit_11.setText(str(rows[0][8]))
            self.lineEdit_12.setText(str(rows[0][9]))
            #print(" shape :"+str(rows[0][12]))
            self.comboBox.setCurrentText(rows[0][12])
            connection.close()
        else:
            self.f_disable_inputs()
            self.label_15.setText("Please Select the record.")
            self.label_15.show()
        self.specimen_diamentions()    
    def delete(self):
        self.f_enabled_inputs()
        self.operation='DELETE'  
        self.pushButton.setText('Delete')    
        self.label_15.setText(" Please delete specimen information.")  
        row = self.tableWidget.currentRow()     
        if(row != -1 ):
            self.specimen_name=(self.tableWidget.item(row, 0).text() )
            print(" specimen_name-delete :"+str(self.specimen_name))
            connection = sqlite3.connect("tyr.db")
            results=connection.execute("select SPECIMEN_NAME,SPECIMEN_SPECS,PARTY_NAME,PRE_LOAD,MOTOR_SPEED,GUAGE_LENGTH_MM,THICKNESS,WIDTH,DIAMETER,C_A_AREA,IN_DIAMETER_MM,OUTER_DIAMETER_MM,SHAPE  from SPECIMEN_MST where SPECIMEN_NAME= '"+str(self.specimen_name)+"'")
            rows=results.fetchall()        
            self.lineEdit.setText(rows[0][0])    #SPECIMEN_NAME
            self.lineEdit_3.setText(rows[0][1])  #SPECIMEN_SPECS
            self.lineEdit_2.setText(rows[0][2])   #PARTY_NAME
            self.lineEdit_5.setText(str(rows[0][3])) # PRE_LOAD
            self.lineEdit_6.setText(str(rows[0][5])) #Guage 
            self.lineEdit_4.setText(str(rows[0][4])) ###Test Speed 
            
            self.lineEdit_7.setText(str(rows[0][6]))
            self.lineEdit_8.setText(str(rows[0][7]))
            self.lineEdit_9.setText(str(rows[0][10]))
            self.lineEdit_10.setText(str(rows[0][11]))
            self.lineEdit_11.setText(str(rows[0][8]))
            self.lineEdit_12.setText(str(rows[0][9]))
            self.comboBox.setCurrentText(rows[0][12])            
            connection.close()
        else:
            self.f_disable_inputs()
            self.label_15.setText("Please Select the record.")
            self.label_15.show()      
            
        self.specimen_diamentions()    
    
    def specimen_diamentions(self):              
        if (self.comboBox.currentText() == 'Rectangle'):     
           self.shape="Rectangle"
           self.lineEdit_7.setEnabled(True)    #Thickness 
           self.lineEdit_8.setEnabled(True)    #width       
           self.lineEdit_9.setDisabled(True)   # inn diam
           self.lineEdit_10.setDisabled(True)  # out diameter
           self.lineEdit_11.setDisabled(True)   # diameter
           self.lineEdit_12.setDisabled(True)  #cs area
        elif  (self.comboBox.currentText() == 'Cylindrical'):     
           self.shape="Cylindrical"
           self.lineEdit_7.setDisabled(True)    #Thickness 
           self.lineEdit_8.setDisabled(True)    #width       
           self.lineEdit_9.setDisabled(True)   # inn diam
           self.lineEdit_10.setDisabled(True)  # out diameter
           self.lineEdit_11.setEnabled(True)   # diameter
           self.lineEdit_12.setDisabled(True)  #cs area
        elif  (self.comboBox.currentText() == 'Pipe'):     
           self.shape="Pipe"
           self.lineEdit_7.setDisabled(True)    #Thickness 
           self.lineEdit_8.setDisabled(True)    #width       
           self.lineEdit_9.setEnabled(True)   # inn diam
           self.lineEdit_10.setEnabled(True)  # out diameter
           self.lineEdit_11.setDisabled(True)   # diameter
           self.lineEdit_12.setDisabled(True)  #cs area      
        elif  (self.comboBox.currentText() == 'DirectValue'):     
           self.shape="Direct Value"
           self.lineEdit_7.setDisabled(True)    #Thickness 
           self.lineEdit_8.setDisabled(True)    #width       
           self.lineEdit_9.setDisabled(True)   # inn diam
           self.lineEdit_10.setDisabled(True)  # out diameter
           self.lineEdit_11.setDisabled(True)   # diameter
           self.lineEdit_12.setEnabled(True)  #cs area   
        
    def save(self):
        print(' self.operation :'+str(self.operation))
        
        self.cs_area=str(self.lineEdit_12.text())
        self.thickness=str(self.lineEdit_7.text())
        self.width=str(self.lineEdit_8.text())
        self.diameter=str(self.lineEdit_11.text())
        self.inn_diamter=str(self.lineEdit_9.text())
        self.out_diameter=str(self.lineEdit_10.text())
        self.shape=str(self.comboBox.currentText())
        
        if(self.operation=='ADD'):
            if(self.lineEdit_6.text() != ''):
                    connection = sqlite3.connect("tyr.db")
                    #print("called save data -- "+self.lineEdit_6.text())
                    if(self.lineEdit.text() != ""):
                        results=connection.execute("select * from SPECIMEN_MST where SPECIMEN_NAME='"+self.lineEdit.text()+"'")
                        #print("called save data1")
                        rows=results.fetchall()
                        if(len(rows) == 0):
                            with connection:        
                                cursor = connection.cursor()                    
                                print("called save data2")
                                #print("SQL :INSERT INTO SPECIMEN_MST(SPECIMEN_NAME,PARTY_NAME,SPECIMEN_SPECS,PRE_LOAD,MOTOR_SPEED,GUAGE_LENGTH_MM) values ('"+self.lineEdit.text()+"','"+self.lineEdit_2.text()+"','"+self.lineEdit_2.text()+"','"+self.lineEdit_2.text()+"','"+self.lineEdit_2.text()+"','")                    
                                cursor.execute("INSERT INTO SPECIMEN_MST(SPECIMEN_NAME,PARTY_NAME,SPECIMEN_SPECS,PRE_LOAD,MOTOR_SPEED,GUAGE_LENGTH_MM,THICKNESS,WIDTH,DIAMETER,C_A_AREA,IN_DIAMETER_MM,OUTER_DIAMETER_MM,SHAPE) values ('"+self.lineEdit.text()+"','"+self.lineEdit_2.text()+"','"+self.lineEdit_3.text()+"','"+self.lineEdit_5.text()+"','"+self.lineEdit_4.text()+"','"+self.lineEdit_6.text()+"','"+str(self.thickness)+"','"+str(self.width)+"','"+str(self.diameter)+"','"+str(self.cs_area)+"','"+str(self.inn_diamter)+"','"+str(self.out_diameter)+"','"+str(self.shape)+"')")                    
                            connection.commit();                    
                            connection.close()   
                            #print (" Inserted New record into table SPECIMEN_NAME!!!")
                            self.label_15.setText("Successfully Saved !!!!!")
                            self.label_15.show()
                            self.select_all_data()
                            self.reset_fun()
                        else:
                            self.label_15.setText(" Specimen Name is already Exist!! :"+self.lineEdit.text())    
                            self.label_15.show()
            
                 
                    else:         
                            self.label_15.setText(" Specimen Name is empty !!!")
                            self.label_15.show()
            else:
                  self.label_15.setText("Guage Length is empty !!!")
                  self.label_15.show()
        
        elif(self.operation=='EDIT'):    
            connection = sqlite3.connect("tyr.db")
            #print("insed saved")  
            with connection:        
                cursor = connection.cursor()                    
                cursor.execute("UPDATE SPECIMEN_MST SET  SPECIMEN_NAME='"+self.lineEdit.text()+"',SPECIMEN_SPECS='"+self.lineEdit_3.text()+"',PARTY_NAME='"+self.lineEdit_2.text()+"',PRE_LOAD='"+self.lineEdit_5.text()+"',MOTOR_SPEED='"+self.lineEdit_4.text()+"',GUAGE_LENGTH_MM='"+self.lineEdit_6.text()+"',THICKNESS='"+str(self.thickness)+"',WIDTH='"+str(self.width)+"',DIAMETER='"+str(self.diameter)+"',C_A_AREA='"+str(self.cs_area)+"',IN_DIAMETER_MM='"+str(self.inn_diamter)+"',OUTER_DIAMETER_MM='"+str(self.out_diameter)+"',SHAPE='"+str(self.shape)+"'  WHERE SPECIMEN_NAME = '"+str(self.specimen_name)+"' ") 
            connection.commit();
            connection.close()
            self.label_15.setText("Successfully Saved !!!!!")
            self.label_15.show()  
        elif(self.operation=='DELETE'):    
            connection = sqlite3.connect("tyr.db")            
            with connection:        
                cursor = connection.cursor()                    
                cursor.execute("DELETE FROM SPECIMEN_MST WHERE SPECIMEN_NAME='"+str(self.specimen_name)+"'")
            connection.commit();
            connection.close()
            self.label_15.setText("Successfully Deleted Speciment :."+str(self.specimen_name))
            self.label_15.show()
            self.select_all_data()
            self.reset_fun()                
        else:
           self.label_15.setText(" Operation Invalid !!!")
           self.label_15.show() 
            
    def reset_fun(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("0")
        self.lineEdit_8.setText("0")
        self.lineEdit_9.setText("0")
        self.lineEdit_10.setText("0")
        self.lineEdit_11.setText("0")
        self.lineEdit_12.setText("0")
        self.label_15.hide()
        
    def f_disable_inputs(self):        
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_5.setDisabled(True)
        self.lineEdit_6.setDisabled(True)
        
        self.lineEdit_7.setDisabled(True)
        self.lineEdit_8.setDisabled(True)
        self.comboBox.setDisabled(True)
    
        self.lineEdit_9.setDisabled(True)
        self.lineEdit_10.setDisabled(True)
        self.lineEdit_11.setDisabled(True)
        self.lineEdit_12.setDisabled(True)
       
        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        
        self.label_15.hide()
        
    
    def f_enabled_inputs(self):        
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
       
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_8.setEnabled(True)
        self.comboBox.setEnabled(True)
        '''
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_10.setEnabled(True)
        self.lineEdit_11.setEnabled(True)
        '''
        #self.lineEdit_12.setEnabled(True)
        
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
       
        self.pushButton_7.setEnabled(True)
       
        
        
    
    def select_all_data(self):
        self.f_disable_inputs()
        self.delete_all_records()        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font) 
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT SPECIMEN_NAME,SHAPE,PARTY_NAME,GUAGE_LENGTH_MM,SPECIMEN_SPECS,MOTOR_SPEED FROM SPECIMEN_MST")                        
        for row_number, row_data in enumerate(results):            
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                #self.lineEdit.setText("")
        
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)   
    
    def delete_all_records(self):
        i = self.tableWidget.rowCount()       
        while (i>0):             
            i=i-1
            self.tableWidget.removeRow(i)  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TY_05_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
