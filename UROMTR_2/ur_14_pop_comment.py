# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ur_14_pop_comment.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class ur_14_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 331)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 70, 521, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 481, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 351, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(40, 280, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "dfgdfgdfgdf dfgfdgdfg fdgdfgdfgdfg dfgdfgdfgdf dfgdfgdfgdfg"))
        self.label_2.setText(_translate("Form", "Comment  and Observations :"))
        self.pushButton_10.setText(_translate("Form", "Close"))
        self.pushButton_10.clicked.connect(Form.close)
        connection = sqlite3.connect("ur.db")
        results=connection.execute("SELECT DR_COMMNETS FROM TEST_MST WHERE TEST_ID IN (SELECT TEST_ID FROM GLOBAL_VAR_REPORT)")       
        for x in results:        
               self.label.setText(str(x[0]))
        connection.close() 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ur_14_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
