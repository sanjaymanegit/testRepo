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
    serial_id=""
    charges=""
    vehical_no=""
    first_wt=""
    first_wt_date=""
    first_wr_time=""
    second_wt=""
    second_wt_date=""
    second_wt_time=""
    net_wt=""
    supplier_name=""
    party_name=""
    material=""
        
    company_name=""
    address=""
    first_wt_mode=""
    second_wt_mode=""
    
    SER_ID=[]
    VEHICLE_NO=[]
    PARTY_NAME=[]
    MATERIAL_NAME=[]
    GROSS_WT_DATE=[]
    GROSS_WT_VAL=[]
    TARE_WT_DATE=[]
    TARE_WT_VAL=[]
    NET_WEIGHT_VAL=[]
    TOTAL_AMT=[]
        
    connection = sqlite3.connect("wt.db")       
    results=connection.execute("SELECT COMPANY_NAME,COMPANY_ADDR||' Phone:'||CONTACT_NO FROM USER_RIGHT_SET")
    for x in results:
         company_name=str(x[0])
         address=str(x[1])        
    connection.close()
        
    connection = sqlite3.connect("wt.db")       
    results=connection.execute("SELECT REPORT_FROM_DATE ,REPORT_TO_DATE,PARTY_NAME,ALL_FLAG,total_amount from PRINTER_DATA")
    for x in results:
         from_date=str(x[0])
         to_date=str(x[1])
         party_name=str(x[2])
         all_flag=str(x[3])
         total_amount=str(x[4])
    connection.close()
    if(str(all_flag)=='ACTIVE'):
            whr_str=" WHERE strftime('%Y-%m-%d',FIRST_WT_CRTEATED_ON)  between '"+str(from_date)+"' and '"+str(to_date)+"' limit 5000"
            party_name=""
    else:
            whr_str=" WHERE strftime('%Y-%m-%d',FIRST_WT_CRTEATED_ON)  between '"+str(from_date)+"' and '"+str(to_date)+"' AND PARTY_NAME='"+str(party_name)+"' limit 5000 "
       
    
    connection = sqlite3.connect("wt.db")
    if(whr_str != ""):
                results=connection.execute("SELECT SUM(TOTAL_AMOUNT) FROM WEIGHT_MST_VW "+str(whr_str))
    else: 
                results=connection.execute("SELECT SUM(TOTAL_AMOUNT) FROM WEIGHT_MST_VW ")
    for x in results:
                total_amount=str(x[0])
    
    
    connection = sqlite3.connect("wt.db")  
    results=connection.execute("SELECT SERIAL_ID_DISPLY,VEHICLE_NO,PARTY_NAME,MATERIAL_NAME,GROSS_WT_DATE ,GROSS_WT_VAL, TARE_WT_DATE ,TARE_WT_VAL  ,NET_WEIGHT_VAL, (IFNULL(GROSS_WT_RATE,0)+ IFNULL(TARE_WT_RATE,0)) as TOTAL_AMT FROM WEIGHT_MST_VW "+str(whr_str)) 
           
    for x in results:                
          SER_ID.append(str(x[0]))
          VEHICLE_NO.append(str(x[1]))
          PARTY_NAME.append(str(x[2]))
          MATERIAL_NAME.append(str(x[3]))
          GROSS_WT_DATE.append(str(x[4]))
          GROSS_WT_VAL.append(str(x[5]))
          TARE_WT_DATE.append(str(x[6]))
          TARE_WT_VAL.append(str(x[7]))
          NET_WEIGHT_VAL.append(str(x[8]))
          TOTAL_AMT.append(str(x[9]))
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
        printer.text("=========================================================================\n\r")
        printer.text("     \n\r")
        printer.charSpacing(1)            
        printer.bold()
        printer.text("        "+str(company_name)+"         \n\r" )              
        printer.text(" "+str(address)+"         \n\r" )
        printer.bold(False)
        printer.align("left")
        printer.text("     \n\r")
        printer.text("===========================================================================\n\r")
        printer.text("     \n\r")
        printer.text("From Date        : "+str(from_date)+"         To Date: "+str(to_date)+" \n\r")
        printer.text("Total Amount(Rs) : "+str(total_amount)+"       Report Date : "+str(datetime.datetime.now().strftime("%d %b %Y %H:%M:%S"))+" \n\r")
        printer.text("Party Name       : "+str(party_name)+" \n\r")
        printer.text("     \n\r")
        printer.text("===========================================================================\n\r")
       
        printer.text("| #      | Vehical No  |Gross Wt    | Tare Wt     | Net Wt | Total   |\n\r")
        printer.text("|                      |Gross-Date  | Tare-Date   |                        \n\r")
        printer.text("|                      |Time        | Time        |                        \n\r")
        printer.text("|--------------------------------------------------------------------------\n\r")        
        for i in range(len(SER_ID)):
                printer.text("| "+str(SER_ID[i]).zfill(6)+" | "+str(VEHICLE_NO[i])+" | "+str(GROSS_WT_VAL[i]).zfill(6)+"     | "+str(TARE_WT_VAL[i]).zfill(6)+"     | "+str(NET_WEIGHT_VAL[i]).zfill(6)+" | "+str(TOTAL_AMT[i]).zfill(7)+" | \n\r")
                printer.text("|        |              | "+str(GROSS_WT_DATE[i])[0:10]+" | "+str(TARE_WT_DATE[i])[0:10]+" |\n\r")
                printer.text("|        |              | "+str(GROSS_WT_DATE[i])[11:16]+"      | "+str(TARE_WT_DATE[i])[11:16]+"      |\n\r")
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
        cnt=int(line.find("Epson"))
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
       
           
        

    
        
