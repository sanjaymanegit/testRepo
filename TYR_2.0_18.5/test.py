import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
calc_speed=45
break_sence=82.877
command_str="*P%04d"%calc_speed+"_%.4f"%break_sence+"\r"
print("Morot Speed and Breaking speed Command  :"+str(command_str))   