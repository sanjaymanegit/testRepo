# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '16_factory_reset.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 511, 321))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(360, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(250, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(160, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(160, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(160, 150, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(160, 200, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 21))
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
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44:09"))
        self.label_2.setText(_translate("MainWindow", "Done."))
        self.pushButton_6.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_8.setText(_translate("MainWindow", "CLOSE"))
        self.label_4.setText(_translate("MainWindow", "FACTORY RESET"))
        self.checkBox.setText(_translate("MainWindow", "Test Data Only"))
        self.checkBox_2.setText(_translate("MainWindow", "Master Data Only"))
        self.checkBox_3.setText(_translate("MainWindow", "ALL Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
