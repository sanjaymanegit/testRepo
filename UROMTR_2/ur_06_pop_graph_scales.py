# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ur_06_pop_graph_scales.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class ur_06_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1267, 561)
        MainWindow.setBaseSize(QtCore.QSize(15, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1211, 491))
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
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 420, 91, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(640, 420, 91, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 220, 212);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 440, 281, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(40, 120, 501, 271))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 60, 141, 71))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 141, 71))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(200, 20, 51, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(360, 20, 51, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(190, 80, 61, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_2)
        self.lineEdit_2.setValidator(input_validator)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 80, 61, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 150, 61, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_4)
        self.lineEdit_4.setValidator(input_validator)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 150, 61, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(10, 50, 461, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(20, 120, 451, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(10, 200, 461, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.groupBox)
        self.line_4.setGeometry(QtCore.QRect(123, 30, 20, 211))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setGeometry(QtCore.QRect(290, 30, 20, 211))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(660, 120, 501, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 60, 141, 71))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 130, 141, 71))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(200, 20, 51, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(360, 20, 51, 31))
        self.label_13.setObjectName("label_13")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(190, 80, 61, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_2)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_10)
        self.lineEdit_10.setValidator(input_validator)
        self.lineEdit_10.setGeometry(QtCore.QRect(350, 80, 61, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_11.setGeometry(QtCore.QRect(190, 150, 61, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_2)
        reg_ex = QRegExp("\d+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_12)
        self.lineEdit_12.setValidator(input_validator)
        self.lineEdit_12.setGeometry(QtCore.QRect(350, 150, 61, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.line_15 = QtWidgets.QFrame(self.groupBox_2)
        self.line_15.setGeometry(QtCore.QRect(10, 50, 461, 16))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.groupBox_2)
        self.line_16.setGeometry(QtCore.QRect(20, 120, 451, 16))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.groupBox_2)
        self.line_17.setGeometry(QtCore.QRect(10, 200, 461, 16))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.groupBox_2)
        self.line_18.setGeometry(QtCore.QRect(123, 30, 20, 211))
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.groupBox_2)
        self.line_19.setGeometry(QtCore.QRect(290, 30, 20, 211))
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(350, 30, 461, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1267, 21))
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
        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.pushButton_5.setText(_translate("MainWindow", "Close"))
        self.label_2.setText(_translate("MainWindow", " Saved Successfully ...."))
        self.label_2.hide()
        self.groupBox.setTitle(_translate("MainWindow", "Flow Scale"))
        self.label.setText(_translate("MainWindow", "X-Axis  \n"
"   Time [ sec]    :"))
        self.label_3.setText(_translate("MainWindow", "Y-Axis \n"
"     Flow [ ml/s]    : "))
        self.label_4.setText(_translate("MainWindow", "Min"))
        self.label_5.setText(_translate("MainWindow", "Max"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Volumn Scale"))
        self.label_10.setText(_translate("MainWindow", "X-Axis  \n"
"   Time [ sec]    :"))
        self.label_11.setText(_translate("MainWindow", "Y-Axis \n"
"     Volumn [ ml ]    : "))
        self.label_12.setText(_translate("MainWindow", "Min"))
        self.label_13.setText(_translate("MainWindow", "Max"))
        self.lineEdit_9.setText(_translate("MainWindow", "0"))
        self.lineEdit_11.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "Set Graph Scale"))
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(self.save_data)
        self.load_data()
        
    def load_data(self):
       connection = sqlite3.connect("ur.db")
       results=connection.execute("SELECT VOLUMN_TIME_X_AXIS,VOLUMN_TIME_Y_AXIS,FLOW_TIME_X_AXIS,FLOW_TIME_Y_AXIS FROM OTER_INFO")
       rows=results.fetchall()     
       
       self.lineEdit_10.setText(str(rows[0][0]))
       self.lineEdit_12.setText(str(rows[0][1]))
       
       self.lineEdit_2.setText(str(rows[0][2]))
       self.lineEdit_4.setText(str(rows[0][3]))
       '''
       self.lineEdit_10.setText(str("1"))
       self.lineEdit_12.setText(str("2"))
       
       self.lineEdit_2.setText(str("3"))
       self.lineEdit_4.setText(str("4"))
       '''
       connection.close()
       
    def save_data(self):
       connection = sqlite3.connect("ur.db")
       #print("insed saved")  
       with connection:        
                cursor = connection.cursor()                    
                cursor.execute("UPDATE OTER_INFO SET  VOLUMN_TIME_X_AXIS='"+self.lineEdit_10.text()+"',VOLUMN_TIME_Y_AXIS='"+self.lineEdit_12.text()+"',FLOW_TIME_X_AXIS='"+self.lineEdit_2.text()+"',FLOW_TIME_Y_AXIS='"+self.lineEdit_4.text()+"'")
       connection.commit();
       connection.close()
       self.label_2.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ur_06_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
