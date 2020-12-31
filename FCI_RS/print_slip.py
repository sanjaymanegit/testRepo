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

def dot_matrix_print():
    serial_id=""       
    vehical_no=""
    party_name=""
    tare_wt=""
    tare_wt_dt=""
    gross_wt=""
    gross_wt_date=""        
    net_wt=""
    amount=""
    driver_in_out=""
    phone_no=""
    material=""
    
    
    printer_header=""
    printer_title=""
    printer_footer=""
    
    duplicate_flg=""
    duplicate_str="" 
    
    connection = sqlite3.connect("fci.db")       
    results=connection.execute("SELECT  PRINTER_HEATER_TITLE, PRINTER_HEADER ,  PRINTER_FOOTER FROM GLOBAL_VAR")         
    for x in results:
         printer_header=str(x[1]) 
         printer_title=str(x[0]) 
         printer_footer=str(x[2]) 
    connection.close()
    
    connection = sqlite3.connect("fci.db")       
    results=connection.execute("SELECT DUPLICATE_FLG FROM PRINTER_DATA")         
    for x in results:
         duplicate_flg=str(x[0])
         if(str(duplicate_flg) == "Yes"):
             duplicate_str="DUPLICATE"
         else:
             duplicate_str="" 
    connection.close()
    
        
    connection = sqlite3.connect("fci.db")       
    results=connection.execute("SELECT SERIAL_ID,VEHICLE_NO,PARTY_NAME,IFNULL(TARE_WT_VAL,0),TARE_WT_DATE,IFNULL(GROSS_WT_VAL,0),GROSS_WT_DATE,IFNULL(NET_WEIGHT_VAL,0),IFNULL(AMOUNT,0),DRIVER_IN_OUT,PHONE_NO,MATERIAL_NAME   FROM WEIGHT_MST_FCI_VW  WHERE  SERIAL_ID in (SELECT SERIAL_ID from PRINTER_DATA)") 
        
    for x in results:                
          serial_id=str(x[0])        
          vehical_no=str(x[1])
          party_name=str(x[2])
          tare_wt=str(x[3])
          tare_wt_dt=str(x[4])
          gross_wt=str(x[5])
          gross_wt_date=str(x[6])         
          net_wt=str(x[7])
          amount=str(x[8])
          driver_in_out=str(x[9])
          phone_no=str(x[10])
          material=str(x[11])
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
        printer.text("=======================================================\n\r")
        printer.charSpacing(1)            
        printer.bold()
        printer.text("                "+str(printer_title)+"         \n\r" )              
        printer.text("        "+str(printer_header)+"         \n\r" )
        printer.bold(False)
        printer.align("left")
        printer.text("======================================================\n\r")        
        printer.text("Serial No    : "+str(serial_id).zfill(6)+" "+str(duplicate_str)+"         Vehical No: "+str(vehical_no)+" \n\r")
        printer.text("Party Name   : "+str(party_name)+"                \n\r")
        printer.text("Phone No     : "+str(phone_no)+"                  \n\r")
        printer.text("Material     : "+str(material)+"                         \n\r")
        printer.text("|------------------------------------------------------------- \n\r")
        printer.text("| Weight Type     |    Weight (Kg)  |     Date \n\r")
        printer.text("|-------------------------------------------------------------\n\r")
        printer.text("| Tare Wt.        |     "+str(tare_wt).zfill(6)+"      |  "+str(tare_wt_dt)+"  \n\r")
        printer.text("|------------------------------------------------------------\n\r")
        printer.text("| Gross Wt.       |     "+str(gross_wt).zfill(6)+"      |  "+str(gross_wt_date)+"  \n\r")
        printer.text("|-------------------------------------------------------------\n\r")
        printer.text("  Net Weight (Kg): "+str(net_wt).zfill(6)+" \n\r")
        printer.text("  Charges (Rs)   : "+str(amount).zfill(6)+" \n\r")
        printer.text("  \n\r")
        printer.text("  \n\r")
        printer.text("  \n\r")
        printer.text("  \n\r") 
        printer.text(str(printer_footer)+" \n\r")              
        printer.lf()
        print("ok3")
    except IOError:
        print("Printer Errorr. Please check printer configuration")            
            
            


            
            



def get_vendor_id():
        os.system("rm -rf lsusb_data.txt") 
        # Extract serial from cpuinfo file
        os.system("lsusb >> /home/pi/Products/FCI_RS/lsusb_data.txt")
        v_id = "0000000000000000"
        try:
           f = open('/home/pi/Products/FCI_RS/lsusb_data.txt','r')
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
        cnt=int(line.find(str(printer_key)))  #Epson    #TVS
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
              dot_matrix_print()
              
    
           
        

    
        
