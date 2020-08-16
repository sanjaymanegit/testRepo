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
        
    connection = sqlite3.connect("wt.db")       
    results=connection.execute("SELECT COMPANY_NAME,COMPANY_ADDR FROM USER_RIGHT_SET")
    for x in results:
         company_name=str(x[0])
         address=str(x[1])        
    connection.close()
        
        
    connection = sqlite3.connect("wt.db")       
    results=connection.execute("SELECT SERIAL_ID,VEHICLE_NO,FIRST_WEIGHT_VAL,FIRST_WT_CRTEATED_ON,SECOND_WT_VAL,SECOND_WT_CREATED_ON,"+
                                           "NET_WEIGHT_VAL ,FIRST_WEIGHT_MODE,SECOND_WT_MODE,MATERIAL_NAME,MANNUAL_INS_FLG FROM WEIGHT_MST WHERE SERIAL_ID in (SELECT SERIAL_ID from PRINTER_DATA)") 
        
    for x in results:                
          serial_id=str(x[0])
          charges=str(x[7])
          vehical_no=str(x[1])
          first_wt=str(x[2])
          first_wt_date=str(x[3])
          first_wr_time=str(x[3])
          second_wt=str(x[4])
          second_wt_date=str(x[5])
          second_wt_time=str(x[5])
          net_wt=str(x[6])
          supplier_name=str(x[9])
          party_name=str(x[8])
          first_wt_mode=str(x[10])
          second_wt_mode=str(x[11])
          material=str(x[12])
          mannual_flag=str(x[13])
          if(str(mannual_flag) == "Mannual"):
                   mannual_flag="[Tare Weight is Mannual]"
          else:
                   mannual_flag=""
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
        printer.text("===================================================================\n\r")
        printer.charSpacing(1)            
        printer.bold()
        printer.text("              "+str(company_name)+"         \n\r" )              
        printer.text("           "+str(address)+"         \n\r" )
        printer.bold(False)
        printer.align("left")
        printer.text("===================================================================\n\r")        
        printer.text("Serial No    : "+str(serial_id)+"                  Vehical No: "+str(vehical_no)+" \n\r")
        printer.text("Supplier Name: "+str("")+"              Party Name: "+str("")+" \n\r")
        printer.text("Material     : "+str(material)+"                         \n\r")
        printer.text("|---------------------------------------------------------------- \n\r")
        printer.text("| Weight Type          |    Date   |     Time    |Weight (Kg)|\n\r")
        printer.text("|-----------------------------------------------------------------\n\r")
        printer.text("| First Wt. ("+str(first_wt_mode)+")    | "+str(first_wt_date[0:10])+"  | "+str(first_wt_date[11:16])+"       |  "+str(first_wt)+"  |\n\r")
        printer.text("|-----------------------------------------------------------------\n\r")
        printer.text("| Second Wt. ("+str(second_wt_mode)+")    | "+str(second_wt_date[0:10])+" | "+str(second_wt_date[11:16])+"        |  "+str(second_wt)+"  |\n\r")
        printer.text("|-----------------------------------------------------------------\n\r")
        printer.text("                                   Net Weight (Kg): ")
        printer.doubleWidth()
        printer.doubleHeight()
        printer.text(""+str(net_wt)+"  \n\r")       
        printer.text(str(mannual_flag)+"\n\r") 
        printer.text("---------*************  Thanking You   *************----------\n\r")             
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
        cnt=int(line.find("Epson"))  #Epson    #TVS
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
              
    
           
        

    
        
