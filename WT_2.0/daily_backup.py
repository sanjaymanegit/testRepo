import datetime
import time
from PyQt5.QtCore import QDate
import sys,os
import sqlite3
 
def auto_bkp_f():
        print("inside auto backup ")
        date_str=datetime.datetime.now().strftime("%Y%m%d%H%M%S")        
        product_id=get_usb_storage_id()
        if(product_id != "ERROR"):        
                    os.system("cp /home/pi/Products/WT/wt.db /home/pi/Products/WT/wt_auto_bkp"+str(date_str)+".db")
                    os.system("sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi")
                    os.system("mv /home/pi/Products/WT/wt_auto_bkp"+str(date_str)+".db /media/usb")
                    os.system("sudo umount /media/usb")         
                    connection = sqlite3.connect("/home/pi/Products/WT/wt.db")          
                    with connection:        
                        cursor = connection.cursor()                    
                        cursor.execute("INSERT INTO BACKUP_HIST(BACKUP_TYPE,FILE_NAME,PATH,STATUS,BACKUP_ON) VALUES ('Auto','wt_auto_bkp"+str(date_str)+".db','/media/usb','Completed',CURRENT_TIMESTAMP)")                    
                    connection.commit();
                    connection.close()
                    print(" Done ")
        else:
             print("Please connect usb storage device")

def get_usb_storage_id():
        os.system("rm -rf lsusb_data_db_bkp.txt")  
        product_id = "ERROR"
        os.system("lsusb >> lsusb_data_db_bkp.txt")
        try:
           f = open('lsusb_data_db_bkp.txt','r')
           for line in f:
               cnt=0                
               cnt=int(line.find("SanDisk"))
               if cnt > 0 :                   
                   product_id = line[28:33]
                   product_id = "0x"+str(product_id)
           f.close()
        except:
           product_id = "ERROR"
        return product_id

auto_bkp_f()