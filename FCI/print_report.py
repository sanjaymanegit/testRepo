# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'print_popup.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!



from escpos.connections import getUSBPrinter
import usb.core
import usb.util
import os,sys
import sqlite3
import datetime
import time

import sys,os

def report_print():
    whr_sql=""
    Title="Dispatch Report as on"+datetime.datetime.now().strftime("%d %b %Y")
    SiteAddress="Niharika 401, Plot No 105,Sector 50 new Nerul Navi Mumbai Pin 400706"
    BATCH_IDS=[]
    TOTAL_TRUCKS=[]
    TOTAL_NET_WT=[]
    TOTAL_ACCEPTED_BAGS=[]
    
    connection = sqlite3.connect("fci.db")
    results=connection.execute("SELECT REPORT_ENTITY,REPORT_BY,REPORT_FROM_DATE,REPORT_TO_DATE,REPORT_BATCH_ID  FROM GLOBAL_VAR") 
    for x in results:
            if(str(x[1]) == 'DATE_RANGE'):
                whr_sql=" WHERE strftime('%Y-%m-%d',START_DATE)  between '"+str(x[2])+"' and '"+str(x[3])+"' limit 400"
            elif(str(x[1]) == 'BY_BATCH_ID'):
                whr_sql="WHERE BATCH_ID = '"+str(x[4])+"'"
    connection.close()
    
    connection = sqlite3.connect("fci.db")        
    results=connection.execute("select BATCH_ID from BATCH_LIST_VW "+str(self.whr_sql)) 
    for x in results:            
                BATCH_IDS.append(str(x[0]))
                TOTAL_TRUCKS.append()
                TOTAL_NET_WT.append()
                TOTAL_ACCEPTED_BAGS.append()
    connection.close()
        
        
    try:
        vendor_id=get_vendor_id()
        hex_int_v = int(vendor_id, 16)
        product_id=get_product_id()
        hex_int_p = int(product_id, 16)
        print("ok1")
        dev = usb.core.find(idVendor=hex_int_v, idProduct=hex_int_p)
        try:
            dev.reset()
        except ValueError:
            print("Error")
        printer = getUSBPrinter(commandSet='Generic')(idVendor=hex_int_v,  # 0x04b8: 0x0005
                              idProduct=hex_int_p,  # printer #0x
                              inputEndPoint=0x82,
                              outputEndPoint=0x01)
        print("ok2")
        printer.text("=======================================================================\n\r")
        printer.text("     \n\r")
        printer.charSpacing(1)            
        printer.bold()
        printer.text("        "+str(company_name)+"         \n\r" )              
        printer.text(" "+str(address)+"         \n\r" )
        printer.bold(False)
        printer.align("left")
        printer.text("     \n\r")
        printer.text("========================================================================\n\r")
        printer.text("     \n\r")
        for i in range(len(BATCH_IDS)):
                    printer.text("Batch Id       : "+str(BATCH_IDS[i]).zfill(6)+"                     Total Trucks     : "+str(TOTAL_TRUCKS[i])+" \n\r")
                    printer.text("Total Net Wt(Kg) : "+str(TOTAL_NET_WT[i])+"                Total Accepted Bags: "+str(TOTAL_ACCEPTED_BAGS[i])+" \n\r")
                    
                    printer.text("     \n\r")
                    printer.text("|------------------------------------------------------------------------\n\r")
                    printer.text("| Slip.No.      |  Vehical No  |Gross Wt|Gross-Date  |Time   |Tare Wt | Tare-Date  |Time   | Net Wt | Target Location   |Driver IN_OUT Name |\n\r")
                    printer.text("|------------------------------------------------------------------------\n\r")        
                    
                    connection = sqlite3.connect("fci.db")        
                    results=connection.execute("select BATCH_ID from BATCH_LIST_VW "+str(self.whr_sql)) 
                    for x in results:            
                                BATCH_IDS.append(str(x[0]))
                                TOTAL_TRUCKS.append()
                                TOTAL_NET_WT.append()
                                TOTAL_ACCEPTED_BAGS.append()
                    connection.close()
                    connection = sqlite3.connect("fci.db")        
                    results=connection.execute("select SERIAL_ID,VEHICLE_NO,GROSS_WT_VAL,GROSS_WT_DATE,TARE_WT_VAL,TARE_WT_DATE,NET_WEIGHT_VAL,TARGET_STORAGE,DRIVER_IN_OUT from WEIGHT_MSTFCI_VW WHERE BATCH_ID='"+str(BATCH_IDS[i])+"'") 
                    for x in results: 
                            printer.text("| "+str(x[0]).zfill(6)+" | "+str(x[1])+" | "+str(x[2]).zfill(6)+" | "+str(x[3])[0:10]+" | "+str(x[3])[11:16]+" | "+str(x[4]).zfill(6)+" | "+str(x[5])[0:10]+" | "+str(x[5])[11:16]+" | "+str(x[6]).zfill(6)+" | "+str(x[7]).zfill(7)+" | "+str(x[8])+" |\n\r")
                            printer.text("|                                                                  \n\r") 
                    
                    printer.text("|------------------------------------------------------------------------\n\r") 
        
              
        printer.text("*******************************  Thanking You   **************************\n\r")             
        printer.lf()
        print("ok3")
    except IOError:
        print("Printer Errorr. Please check printer configuration")
            

def get_vendor_id():
        os.system("rm -rf lsusb_data.txt") 
        # Extract serial from cpuinfo file
        os.system("lsusb >> /home/pi/Products/WT/lsusb_data.txt")
        v_id = "0000000000000000"
        try:
           f = open('/home/pi/Products/WT/lsusb_data.txt','r')
           for line in f:
                cnt=0
                #print("line ==>"+str(line))
                #print("line ==>"+str(line.find("Printer")))
                cnt=int(line.find("Epson"))
                if cnt > 0 :
                   #print("line ==>"+str(line))
                   #print("vendor Id ==>"+str(line[23:27]))
                   #print("Product Id ==>"+str(line[28:33]))
                   v_id = line[23:27]
                   v_id ="0x"+str(v_id)                   
           f.close()
        except:
           v_id = "ERROR000000000"
        return v_id
    

def get_product_id():
        os.system("rm -rf lsusb_data.txt") 
        # Extract serial from cpuinfo file
        product_id = "0000000000000000"
        os.system("lsusb >> lsusb_data.txt")
        try:
           f = open('lsusb_data.txt','r')
           for line in f:
               cnt=0
                #print("line ==>"+str(line))
                #print("line ==>"+str(line.find("Printer")))
               cnt=int(line.find("Epson"))
               if cnt > 0 :
                   #print("line ==>"+str(line))
                   #print("vendor Id ==>"+str(line[23:27]))
                   #print("Product Id ==>"+str(line[28:33]))
                   product_id = line[28:33]
                   product_id = "0x"+str(product_id)
           f.close()
        except:
           product_id = "ERROR000000000"
        return product_id


###### Main Code Started here ######
    
go_for_print="No"

#### Check for Printer Availablility #####
os.system("rm -rf lsusb_data.txt") 
os.system("lsusb >> lsusb_data.txt")        
try:
    f = open('lsusb_data.txt','r')
    for line in f:
        cnt=0
        cnt=int(line.find("Epson"))  #Epson #TVS
        print (str(cnt))
        if cnt > 0 :
             go_for_print="Yes"
             break;
        else:
            go_for_print="No"                    
    f.close()
except:
     print("Error:")
 
#### Check fir Printer Configuration ########
if(go_for_print =="Yes"):     
    report_print()
else:
    print("Printer is not configured !!!!!")
       
           
        

    
        
