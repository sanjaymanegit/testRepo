import sys
import os
from PyQt5.QtWidgets import QApplication, QFileDialog, QSlider, QComboBox, QCheckBox, QWidget, QMainWindow, QPushButton, QLabel, QGridLayout, QGroupBox, QRadioButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal

import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'GUI TESTS'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 400
        self.statusBarMessage = "GUI TEST"
        self.currentSprite = 'TEST.png'
        self.btn1Active = False
        self.btn2Active = False
        self.btn3Active = False
        self.btn4Active = False
        self.btn5Active = False
        self.btn6Active = False
        self.btn7Active = False
        self.btn8Active = False
        self.saveLocationDir = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage(self.statusBarMessage)

        self.userNameLabel = QLabel(self)
        self.userNameLabel.move(0,125)
        self.userNameLabel.setText("What is your name?")
        self.userNameLabel.resize(120,20)

        self.nameInput = QLineEdit(self)
        self.nameInput.move(0,145)
        self.nameInput.resize(200,32)
        self.nameInput.setEchoMode(0)
        self.nameInput.mousePressEvent=self.showKeyboard

    @pyqtSlot()
    def showKeyboard(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            QtWidgets.QLineEdit.mousePressEvent(QLineEdit, event)
            command = "matchbox-keyboard"
            os.system(command)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())