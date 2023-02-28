
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import serial,time
from PyQt5.QtCore import QDate
import datetime
import sys
import os
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

class popup_email_test_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 671, 451))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);\n")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(280, 30, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(190, 290, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 380, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 380, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(190, 110, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 330, 591, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(480, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
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
        self.label_4.setGeometry(QtCore.QRect(10, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 0, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 170, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 240, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight)       
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(510, 240, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 21))
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
        self.label.setText(_translate("MainWindow", "08 Feb 2021 11:44:00"))
        #self.label_2.setText(_translate("MainWindow", "Successfully Sent Email."))
        self.pushButton_6.setText(_translate("MainWindow", "SEND"))
        self.pushButton_7.setText(_translate("MainWindow", "RESET"))
        self.label_3.setText(_translate("MainWindow", "Email ID (To) :"))
        self.pushButton_8.setText(_translate("MainWindow", "CLOSE"))
        self.label_4.setText(_translate("MainWindow", "SEND EMAIL"))
        self.label_5.setText(_translate("MainWindow", "Subject   :"))
        self.label_6.setText(_translate("MainWindow", "File Name :"))
        self.label_7.setText(_translate("MainWindow", ".pdf"))
        self.label_7.hide()
        self.pushButton_8.clicked.connect(MainWindow.close)        
        self.pushButton_6.clicked.connect(self.send_email)
        self.pushButton_7.clicked.connect(self.reset_fields)
        
        self.load_data()
        self.timer1=QtCore.QTimer()
        self.timer1.setInterval(1000)        
        self.timer1.timeout.connect(self.device_date)
        self.timer1.start(1)
        
    
    def device_date(self):     
        self.label.setText(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))
       
    
    
    def load_data(self):
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("SELECT EMAIL_DEFAULT,EMAIL_SUBJECT,EMAIL_FILE_NAME,EMAIL_TEST_ID FROM GLOBAL_VAR") 
        for x in results:
            self.lineEdit.setText(str(x[0]))
            self.lineEdit_2.setText(str(x[1]))
            #self.lineEdit_3.setText(str(x[2]))
            self.lineEdit_3.setText("Report_of_test_"+str(x[3]).zfill(4)+".pdf")
            self.lineEdit_3.setDisabled(True)
            self.label_2.setText("Current Test ID is : "+str(x[3]))
            os.system("cp ./reports/test_report.pdf ./reports/Report_of_test_"+str(x[3]).zfill(4)+".pdf")
            self.filename="Report_of_test_"+str(x[3]).zfill(4)+".pdf"
        connection.close()
    
    
    #validate email id string format
    #
    
    def connect(self):
        try:
            urllib.request.urlopen('http://google.com') #Python 3.x
            return True
        except:
            return False
        
    def validate(self):
        self.validation_flg="FALSE"
        self.label_2.setText("")
        #Check for internet connect
        if(self.connect()):
            #self.validation_flg="TRUE"
            if(str(self.lineEdit.text()) != ""):                
                self.match_txt = str(self.lineEdit.text())
                self.matched_token = re.findall("@", self.match_txt)            
              
                if(len(self.matched_token) == 1):
                   #self.validation_flg="TRUE"
                   self.match_txt = str(self.lineEdit.text())
                   self.matched_token = re.findall("\.", self.match_txt)
                   if(len(self.matched_token) > 0):
                       #self.validation_flg="TRUE"
                       if(str(self.lineEdit_2.text()) != ""):
                           self.validation_flg="TRUE"
                           if(str(self.lineEdit_3.text()) != ""):
                                #self.validation_flg="TRUE"
                                self.match_txt = str(self.lineEdit_3.text())
                                self.matched_token = re.findall("\.pdf", self.match_txt)
                                if(len(self.matched_token) == 1):
                                       self.validation_flg="TRUE"
                                else:
                                       self.validation_flg="FALSE"
                                       self.label_2.setText("Invalid File Name[.pdf].")
                                
                           else:
                                self.validation_flg="FALSE"
                                self.label_2.setText("File name  is Empty.") 
                           
                       else:
                           self.validation_flg="FALSE"
                           self.label_2.setText("Subject is Empty.") 
                       
                       
                       
                       
                   else:
                       self.validation_flg="FALSE"
                       self.label_2.setText("Invalid Email Id ( DOT Missed )")
                   
                   
                   
                else:
                   self.validation_flg="FALSE"
                   self.label_2.setText("Invalid Email Id ( @ Missied ).")           
            else:
                self.validation_flg="FALSE"
                self.label_2.setText("EmailId is Empty.") 
            
            
        else:
           self.label_2.setText("Intenet is  OFF.")
        
        
    
    
    def reset_fields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        #self.lineEdit_3.setText("")
        self.label_2.setText("") 
        
    def send_email(self):
        
        self.sender_email = "utmapp3@gmail.com" #
        self.receiver_email = str(self.lineEdit.text()) #"sanjaymane1610@gmail.com"
                    #password = input("Type your password and press enter:")
        self.password = "Dhruv@1210"
        self.smtp_server="smtp.gmail.com"
        
        
        connection = sqlite3.connect("tyr.db")
        results=connection.execute("select FROM_EMAIL_ID,FROM_EMAIL_PWD,FROM_EMAIL_SMTP_SERVER from GLOBAL_VAR") 
        for x in results:
            self.sender_email =str(x[0])
            self.password =str(x[1])
            self.smtp_server=str(x[2])            
        connection.close()
        
        

        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = str(self.lineEdit_2.text())
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
                        <p>Hi,<br>
                          Refer the attached testing report<br>                  
                        </p>
                      </body>
                    </html>
                    """

                    # Turn these into plain/html MIMEText objects
        self.part1 = MIMEText(self.text, "plain")
        self.part2 = MIMEText(self.html, "html")
        self.filenamewithpath = "./reports/"+str(self.filename)  # In same directory as script

                    # Open PDF file in binary mode
        with open(self.filenamewithpath, "rb") as attachment:
                        # Add file as application/octet-stream
                        # Email client can usually download this automatically as attachment
                        self.part = MIMEBase("application", "octet-stream")
                        self.part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(self.part)

        # Add header as key/value pair to attachment part
        self.part.add_header(
                        "Content-Disposition",
                        "attachment; filename= "+str(self.filename)+"",
        )            

        
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        self.message.attach(self.part1)
        self.message.attach(self.part2)
                    # Add attachment to message and convert message to string
        self.message.attach(self.part)
                   
                    # Create secure connection with server and send email 465
        self.context = ssl.create_default_context()
        self.validate()
        if(self.validation_flg=="TRUE"):
                with smtplib.SMTP_SSL(self.smtp_server, 465, context=self.context) as server:
                    try:
                        server.login(self.sender_email, self.password)
                        server.sendmail(
                                self.sender_email, self.receiver_email, self.message.as_string()
                                    #self.sender_email, self.receiver_email, self.message
                                )
                            
                        self.label_2.setText("Successfully Sent Email.")
                        connection = sqlite3.connect("tyr.db")        
                        with connection:        
                                cursor = connection.cursor()                
                                cursor.execute("update global_var set EMAIL_DEFAULT='"+self.lineEdit.text()+"',EMAIL_SUBJECT='"+self.lineEdit_2.text()+"',EMAIL_FILE_NAME='"+self.lineEdit_3.text()+"'")                 
                        connection.commit()
                        connection.close()
                    except Exception as e:
                        self.label_2.setText("Error !!.")
                        print("Error:"+str(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = popup_email_test_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
