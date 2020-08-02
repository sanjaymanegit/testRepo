# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop_party.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class POP_PARTY_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 771, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.save_flag=""
        
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(490, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(50, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 100, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(50, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 150, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(450, 50, 256, 241))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(50, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(150, 200, 221, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(50, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "Close"))
        self.label_4.setText(_translate("MainWindow", "Saved Successfully."))
        self.label_3.setText(_translate("MainWindow", "Party Name:"))
        self.label_5.setText(_translate("MainWindow", "Phone No:"))
        self.label_6.setText(_translate("MainWindow", "Email Id :"))
        self.label_7.setText(_translate("MainWindow", "Address:"))
        self.label_8.setText(_translate("MainWindow", "Edit Party Details"))
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.save_data)
        self.pushButton_2.clicked.connect(self.reset) 
        self.listWidget.doubleClicked.connect(self.selected_party)
        self.label_4.hide()
        self.parties_list_load()
        
    def parties_list_load(self):
        self.listWidget.clear()
        self.listWidget.addItem("====Parties =====")
        connection = sqlite3.connect("wt.db")
        results=connection.execute("SELECT DISTINCT PARTY_NAME FROM WEIGHT_MST where PARTY_NAME !=''")       
        for x in results:        
               self.listWidget.addItem(str(x[0]))
        connection.close()
                
    def selected_party(self):
        self.save_flag="save"
        self.list_type=self.listWidget.item(0).text()
        if(self.listWidget.currentItem().text() != self.listWidget.item(0).text()):
            if(self.list_type=="====Parties ====="):
                self.lineEdit.setText(self.listWidget.currentItem().text())
                connection = sqlite3.connect("wt.db")
                results=connection.execute("SELECT PARTY_NAME,PARTY_ADDR, PARTY_PHONE,PARTY_EMAIL FROM WEIGHT_MST WHERE PARTY_NAME ='"+self.listWidget.currentItem().text()+"' LIMIT 1")       
                for x in results:        
                     self.lineEdit_2.setText(str(x[2]))
                     self.lineEdit_3.setText(str(x[3]))
                     self.textEdit.setText(str(x[1])) 
                connection.close()
                
                
    def save_data(self):
        if(str(self.save_flag) != ""):
            connection = sqlite3.connect("wt.db")
            with connection:        
                    cursor = connection.cursor()       
                    cursor.execute("UPDATE WEIGHT_MST SET PARTY_NAME='"+str(self.lineEdit.text())+"', PARTY_ADDR='"+self.textEdit.toPlainText()+"', PARTY_PHONE='"+str(self.lineEdit_2.text())+"', PARTY_EMAIL='"+str(self.lineEdit_3.text())+"'  WHERE PARTY_NAME ='"+self.listWidget.currentItem().text()+"'")
            connection.commit();
            connection.close()
            self.label_4.show()
            self.parties_list_load() 
            
    def reset(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.textEdit.setText("")
        self.save_flag=""
        self.parties_list_load()   
                    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = POP_PARTY_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
