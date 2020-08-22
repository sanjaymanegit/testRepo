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
    Title="Dispatch Report as on "+datetime.datetime.now().strftime("%d %b %Y")
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
    results=connection.execute("select BATCH_ID ,TOTAL_TRUCKS, TOTAL_NET_WT, TOTAL_ACCEPTED_BAGS from BATCH_LIST_VW "+str(whr_sql)) 
    for x in results:            
                BATCH_IDS.append(str(x[0]))
                TOTAL_TRUCKS.append(str(x[1]))
                TOTAL_NET_WT.append(str(x[2]))
                TOTAL_ACCEPTED_BAGS.append(str(x[3]))
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
        printer.text(" "+str(Title)+"         \n\r" )              
        printer.text(" "+str(SiteAddress)+"         \n\r" )
        printer.bold(False)
        printer.align("left")
        printer.text("     \n\r")
        printer.text("========================================================================\n\r")
        printer.text("     \n\r")
        for i in range(len(BATCH_IDS)):
                    printer.text("Batch Id        : "+str(BATCH_IDS[i]).zfill(6)+"                     Total Trucks    : "+str(TOTAL_TRUCKS[i]).zfill(4)+" \n\r")
                    printer.text("Total Net Wt(Kg): "+str(TOTAL_NET_WT[i]).zfill(6)+"                Total Accepted Bags  : "+str(TOTAL_ACCEPTED_BAGS[i]).zfill(4)+" \n\r")
                    
                    printer.text("     \n\r")
                    printer.text("|------------------------------------------------------------------------\n\r")
                    printer.text("| Slip.No. |  Vehical No  | No.Of.Bags. | Net Wt | Target Location    |\n\r")
                    printer.text("|------------------------------------------------------------------------\n\r")        
                    
                    
                    connection = sqlite3.connect("fci.db")        
                    results=connection.execute("select SERIAL_ID,VEHICLE_NO,ACCPTED_BAGS,NET_WEIGHT_VAL,TARGET_STORAGE from WEIGHT_MST_FCI_VW WHERE BATCH_ID='"+str(BATCH_IDS[i])+"'") 
                    for x in results: 
                            printer.text("|  "+str(x[0]).zfill(6)+"  | "+str(x[1])+"  |     "+str(x[2]).zfill(4)+"    |  "+str(x[3]).zfill(6)+" | "+str(x[4])+" \n\r")
                            printer.text("|                                                                  \n\r") 
                    
                    printer.text("|------------------------------------------------------------------------\n\r") 
        
              
        printer.text("*********************  Thanking You   **************************\n\r")             
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
                cnt=int(line.find(str(printer_key)))
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
               cnt=int(line.find(str(printer_key)))
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
printer_key="Epson"
connection = sqlite3.connect("fci.db")       
results=connection.execute("SELECT PRINTER_KEY FROM GLOBAL_VAR")         
for x in results:                
         printer_key=str(x[0])
connection.close()
print("printer_key:"+str(printer_key))
#### Check for Printer Availablility #####
os.system("rm -rf lsusb_data.txt") 
os.system("lsusb >> lsusb_data.txt")        
try:
    f = open('lsusb_data.txt','r')
    for line in f:
        cnt=0
        cnt=int(line.find(str(printer_key)))  #Epson #TVS
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
       
           
        

    
        
