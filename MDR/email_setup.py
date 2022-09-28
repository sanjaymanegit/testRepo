# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '16_email_setup.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import sqlite3
import time

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
import email, smtplib, ssl
import re
import urllib.request

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class email_setup_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 581, 411))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(410, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 350, 101, 31))
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
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(80, 170, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 170, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(80, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 230, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 350, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(180, 350, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_10.setAutoDefault(True)
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(390, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 290, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        #self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 80, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(40, 140, 501, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_11 = QtWidgets.QLineEdit(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(410, 350, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        #self.pushButton_11.setStyleSheet("background-color: rgb(170, 170, 127);n""")
        #self.pushButton_11.setAutoDefault(True)
        #        self.pushButton_11.setDefault(True)
#        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setGeometry(QtCore.QRect(480, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_12.setAutoDefault(True)
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(390, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_13.setAutoDefault(True)
        self.pushButton_13.setDefault(True)
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(390, 290, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        reg_ex = QRegExp("(\\d+\\.\\d+)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit_6)
        self.lineEdit_6.setValidator(input_validator)
        self.lineEdit_6.setGeometry(QtCore.QRect(470, 290, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #==============================================================
        self.sender_email = "utmapp3@gmail.com" #
        self.receiver_email = "sanjaymane1610@gmail.com"
        #password = input("Type your password and press enter:")
        self.password = "Dhruv@1210"
        self.filename=""
        self.filenamewithpath=""

        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "multipart test11"
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email        
        
        # Create the plain-text and HTML version of your message
        self.text = ""
        self.html = ""

        # Turn these into plain/html MIMEText objects
        self.part1 = MIMEText(self.text, "plain")
        self.part2 = MIMEText(self.html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        self.message.attach(self.part1)
        self.message.attach(self.part2)
        self.context = ""
        self.validation_flg="FALSE"
        ##============================================================

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44:09"))
        self.pushButton_8.setText(_translate("MainWindow", "TEST ON :"))
        self.label_2.setText(_translate("MainWindow", "Email Setup"))
        self.label_5.setText(_translate("MainWindow", "Email ID:"))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.pushButton_9.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_10.setText(_translate("MainWindow", "RESET"))
        self.label_7.setText(_translate("MainWindow", "Saved Successfully."))
        self.label_7.hide()
        self.label_8.setText(_translate("MainWindow", "SMTP Server :"))
        self.label_9.setText(_translate("MainWindow", "Login  :"))
        #self.pushButton_11.setText(_translate("MainWindow", ""))
        self.pushButton_12.setText(_translate("MainWindow", "CLOSE"))
        self.pushButton_13.setText(_translate("MainWindow", "LOGIN"))
        self.label_10.setText(_translate("MainWindow", "SMTP Port :"))
        self.lineEdit_5.setText("singhisking")
        self.pushButton_12.clicked.connect(MainWindow.close)
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.pushButton_9.clicked.connect(self.save_data)
        self.pushButton_10.clicked.connect(self.load_data)
        self.pushButton_13.clicked.connect(self.login_page)
        self.pushButton_8.clicked.connect(self.send_test_email)
        
        self.timer1.start(1)
        #self.load_data()
        self.hide_all()

    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
        
    def load_data(self):
        self.show_all()
        connection = sqlite3.connect("mdr.db")
        results=connection.execute("SELECT FROM_EMAIL_ID,FROM_EMAIL_PWD,FROM_EMAIL_SMTP_SERVER,FROM_EMAIL_PORT FROM GLOBAL_VAR")       
        for x in results:
              self.lineEdit_2.setText(str(x[0]))
              self.lineEdit_3.setText(str(x[1])) 
              self.lineEdit_4.setText(str(x[2]))
              self.lineEdit_6.setText(str(x[3]))  
        connection.close()
    
    def save_data(self):
        self.save_validate()
        if(self.validation_flg=="TRUE"):
            connection = sqlite3.connect("mdr.db")          
            with connection:        
                    cursor = connection.cursor()                    
                    cursor.execute("UPDATE GLOBAL_VAR SET FROM_EMAIL_ID='"+self.lineEdit_2.text()+"', FROM_EMAIL_PWD='"+self.lineEdit_3.text()+"', FROM_EMAIL_SMTP_SERVER='"+self.lineEdit_4.text()+"',FROM_EMAIL_PORT='"+self.lineEdit_6.text()+"' ") 
            connection.commit();
            connection.close()                    
            self.label_7.setText("Saved Successfully.") 
            self.label_7.show()
    
    def hide_all(self):
        self.lineEdit_2.hide()
        self.lineEdit_3.hide() 
        self.lineEdit_4.hide()
        self.lineEdit_6.hide()        
        self.label_2.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.pushButton_9.hide()
        self.pushButton_10.hide()        
        self.label_8.hide()
        #self.label_9.hide()
        self.label_10.hide()
        self.pushButton_8.hide()
        self.pushButton_11.hide()       
        
    
    def show_all(self):
        self.lineEdit_2.show()
        self.lineEdit_3.show() 
        self.lineEdit_4.show()
        self.lineEdit_6.show()        
        self.label_2.show()
        self.label_5.show()
        self.label_6.show()
        self.pushButton_9.show()
        self.pushButton_10.show()        
        self.label_8.show()
        #self.label_9.hide()
        self.label_10.show()
        self.pushButton_8.show()
        self.pushButton_11.show()
     
    def login_page(self):
         print("password :"+str(self.lineEdit_5.text()))
         if(str(self.lineEdit_5.text()) == 'singhisking'):
                self.load_data()
         else:
                self.label_7.setText("Incorrect Password.") 
                self.label_7.show()   
                #self.groupBox_2.hide() 
     
     
     
    def connect(self):
        try:
            urllib.request.urlopen('http://google.com') #Python 3.x
            return True
        except:
            return False
        
        
    def save_validate(self):
        self.validation_flg="FALSE"
        if(self.lineEdit_2.text() != ""):
                self.match_txt = str(self.lineEdit_2.text())
                self.matched_token = re.findall("@", self.match_txt)
                if(len(self.matched_token) == 1):
                    self.match_txt = str(self.lineEdit_2.text())
                    self.matched_token = re.findall("\.", self.match_txt)
                    if(len(self.matched_token) > 0):                        
                        if(self.lineEdit_3.text() != ""):
                            if(self.lineEdit_4.text() != ""):
                                if(self.lineEdit_6.text() != ""):
                                    self.validation_flg="TRUE"
                                else:
                                    self.validation_flg="FALSE"
                                    self.label_7.setText("Port Should not be Null") 
                                    self.label_7.show() 
                            else:
                                self.validation_flg="FALSE"
                                self.label_7.setText("SMTP Server Should not null") 
                                self.label_7.show()                        
                        else:
                            self.validation_flg="FALSE"
                            self.label_7.setText("Password should not null") 
                            self.label_7.show()
                    else:
                         self.validation_flg="FALSE"
                         self.label_7.setText("Invalid Email Id ( DOT Missed )")
                         self.label_7.show()
                else:
                   self.validation_flg="FALSE"
                   self.label_7.setText("Invalid Email Id ( @ Missied ).")
                   self.label_7.show()
        else:
            self.label_7.setText("Email Id should not null") 
            self.label_7.show()
    
    def test_validate(self):       
        self.validation_flg="FALSE"
        if(self.pushButton_11.text() != ""):
                self.match_txt = str(self.pushButton_11.text())
                self.matched_token = re.findall("@", self.match_txt)
                if(len(self.matched_token) == 1):
                    self.match_txt = str(self.pushButton_11.text())
                    self.matched_token = re.findall("\.", self.match_txt)
                    if(len(self.matched_token) > 0):
                        self.validation_flg="TRUE"                               
                    else:
                         self.validation_flg="FALSE"
                         self.label_7.setText("Test Email Id ( DOT Missed )")
                         self.label_7.show()
                else:
                   self.validation_flg="FALSE"
                   self.label_7.setText("Test Email Id ( @ Missied ).")
                   self.label_7.show()
        else:
            self.label_7.setText("Test Email Id should not null") 
            self.label_7.show()
            
      
    def send_test_email(self):
        self.save_validate()
        self.test_validate()
        if(self.validation_flg=="TRUE"):
            
            '''
            self.sender_email = "utmapp4ae@gmail.com" #
            self.receiver_email = "sanjaymane1610@gmail.com"
            self.password = "Dhruv@1210"
            self.smtp_server="smtp.gmail.com"
            '''
            self.sender_email = str(self.lineEdit_2.text())
            self.receiver_email = str(self.pushButton_11.text())
            self.password = str(self.lineEdit_3.text())
            self.smtp_server=str(self.lineEdit_4.text())
            
            print("From Email ID: "+str(self.sender_email))
            print("TO Email ID: "+str(self.receiver_email))
            print("PWD: "+str(self.password))
            print("SMTP SERVER: "+str(self.smtp_server))

            self.message = MIMEMultipart("alternative")
            self.message["Subject"] = "From Email Test"
            self.message["From"] = self.sender_email
            self.message["To"] = self.receiver_email
                        
                        # Create the plain-text and HTML version of your message
            self.text = """\
                        Hi,
                        How are you?
                        Real Python has many great tutorials:
                        www.realpython.com"""
            self.html = """\
                        <html>
                          <body>
                            <p>Hi,<br> xxxxxx
                              From Email Test xxxxxx<br>                  
                            </p>
                          </body>
                        </html>
                        """

                        # Turn these into plain/html MIMEText objects
            self.part1 = MIMEText(self.text, "plain")
            self.part2 = MIMEText(self.html, "html")

            
            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            self.message.attach(self.part1)
            self.message.attach(self.part2)
                        # Add attachment to message and convert message to string
            #self.message.attach(self.part)
                       
                        # Create secure connection with server and send email 465
            self.context = ssl.create_default_context()           
            if(self.validation_flg=="TRUE"):
                    with smtplib.SMTP_SSL(self.smtp_server, 465, context=self.context) as server:
                        try:
                            server.login(self.sender_email, self.password)
                            server.sendmail(
                                    self.sender_email, self.receiver_email, self.message.as_string()
                                        #self.sender_email, self.receiver_email, self.message
                                    )
                                
                            self.label_7.setText("Successfully Sent Email.")
                            self.label_7.show()
                        except Exception as e:
                            self.label_7.setText("Error !!!!.")
                            self.label_7.show()
                            print("Error:"+str(e))
    
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = email_setup_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

