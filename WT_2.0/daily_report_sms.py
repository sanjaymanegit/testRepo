import urllib.request
import urllib.parse
import sqlite3
import datetime
import json

def sendSMS(apikey, numbers, sender, message):
        if(numbers != ""):            
            connection = sqlite3.connect("/home/pi/Products/WT/services.db")       
            results=connection.execute("SELECT STATUS FROM  SMS_REPORTS_CONFIG")
            for x in results:
                status=str(x[0])               
            
            
            connection = sqlite3.connect("/home/pi/Products/WT/wt.db")       
            results=connection.execute("SELECT SMS_ACTIVATION,SMS_API_KEY,SMS_API_URL FROM USER_RIGHT_SET")
            for x in results:
                if(status == "ACTIVE"):
                    apikey=str(x[1])
                    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,'message' : message, 'sender': sender})
                    data = data.encode('utf-8')                   
                    request = urllib.request.Request(str(x[2]))
                    f = urllib.request.urlopen(request, data)
                    fr = f.read()
                    return(fr)
                
                else:
                    print(" SMS Deactivated")
                    return("ERROR")
            connection.close()  
                
                
        else:
            print("SendSMS : Invalid Number.")
            return("ERROR")
 

sms_message_str="Unit Name:<unit_name>,Report Dt: <r_dt> , From Time: <f_t> , To Time: <t_t> , Total Collection (Rs): <tot_coll> , Collection Count: <coll_cnt>, Device Count: <dev_cnt>"
phone1=""
phone2=""
phone3=""
phone4=""
phone5=""
from_time=""
to_time=""
total_collection=""
collection_cnt=""
device_cnt=""
unit_name=""
device_count_reset_flg="No"

## Get Configuration Data
######### From time , to time ,
connection = sqlite3.connect("/home/pi/Products/WT/services.db")
results=connection.execute("select PHONE_1,PHONE_2,PHONE_3,PHONE_4,PHONE_5, FROM_TIME,TO_TIME FROM SMS_REPORTS_CONFIG")
for x in results:
        phone1=str(x[0])
        phone2=str(x[1])
        phone3=str(x[2])
        phone4=str(x[3])
        phone5=str(x[4])
        from_time=str(x[5])
        to_time=str(x[6])
        #device_cnt="12"
connection.close()

connection = sqlite3.connect("/home/pi/Products/WT/services.db")
results=connection.execute("select DEVICE_VEHICAL_COUNTER FROM DEVICE_CONF")
for x in results:
        device_cnt=str(x[0])
connection.close()

print("phone1 :"+str(phone1)+"phone2: "+str(phone2)+" phone3 : "+str(phone3)+" phone4: "+str(phone4)+" phone5 :"+str(phone5)+ " from_time "+str(from_time)+" to_time :"+str(to_time)+ " device_cnt :"+str(device_cnt) )


from_date=str(datetime.datetime.now().strftime("%Y-%m-%d"))+" "+str(from_time)+":00"
to_date=str(datetime.datetime.now().strftime("%Y-%m-%d"))+" "+str(to_time)+":00"

whr_str=" WHERE strftime('%Y-%m-%d %H:%M:%S',FIRST_WT_CRTEATED_ON)  between '"+str(from_date)+"' and '"+str(to_date)+"' "

print (" whr clause "+str(whr_str))

connection = sqlite3.connect("/home/pi/Products/WT/wt.db")       
results=connection.execute("SELECT COMPANY_NAME FROM USER_RIGHT_SET")
for x in results:
        unit_name=str(x[0])        
connection.close()

########## total collection , collection count, device count 
connection = sqlite3.connect("/home/pi/Products/WT/wt.db")       
results=connection.execute(" SELECT sum(AMOUNT+AMOUNT_2),count(*) as COLL_CNT FROM WEIGHT_MST "+str(whr_str))
for x in results:
        total_collection=str(x[0])
        collection_cnt=str(x[1])        
connection.close()
print("total_collection :"+str(total_collection)+"collection_cnt: "+str(collection_cnt));


sms_message_str=sms_message_str.replace("<r_dt>",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
sms_message_str=sms_message_str.replace("<f_t>",str(from_time))
sms_message_str=sms_message_str.replace("<t_t>",str(to_time))
sms_message_str=sms_message_str.replace("<tot_coll>",str(total_collection))
sms_message_str=sms_message_str.replace("<coll_cnt>",str(collection_cnt))
sms_message_str=sms_message_str.replace("<dev_cnt>",str(device_cnt))
sms_message_str=sms_message_str.replace("<unit_name>",str(unit_name))

print(" SMS str  : "+str(sms_message_str))
vcnt=0
if(phone1 != ""):
    for sms_phnoe_no in (phone1,phone2,phone3,phone4,phone5):
                vcnt=vcnt+1
                print ("phone No :"+str(sms_phnoe_no))
                if(len(sms_phnoe_no) ==10):
                        resp =sendSMS('', sms_phnoe_no,'', sms_message_str)
                        sms_status=""
                        sms_error=""                
                        if(resp != 'ERROR'):                                
                                y = json.loads(str(resp,'utf-8'))
                                print (str(y))
                                print (y["status"])
                                if(y["status"]=="failure"):
                                        sms_status="failure"
                                        sms_error=str(y["errors"][0]["message"])
                                else:
                                        sms_status="success"                                        
                                        
                        else:        
                                print (resp)
                                sms_status="failure"
                                sms_error="SMS Deactivated OR Phone Number is empty"                                   
                                                    
                        connection = sqlite3.connect("/home/pi/Products/WT/services.db")
                        with connection:                            
                             cursor = connection.cursor()
                             cursor.execute("INSERT INTO SMS_HISTORY(PHONE_NO,SMS_TYPE,STATUS,ERROR_MSG,SERIAL_ID,SMS_MSG) values('"+str(sms_phnoe_no)+"','REPORT','"+str(sms_status)+"','"+str(sms_error)+"','','"+str(sms_message_str)+"')")
                        connection.commit();
                        connection.close()
                       
                        
                else:
                    print("Invalid Phone No :"+str(sms_phnoe_no))
                    
                if(vcnt == 5):
                    device_count_reset_flg="Yes"
                    print("device_count_reset_flg :"+str(device_count_reset_flg))
                else:
                    device_count_reset_flg="No"
                    
if(device_count_reset_flg=="Yes"):
        print("Device Count updated ot zero")
        connection = sqlite3.connect("/home/pi/Products/WT/services.db")          
        with connection:        
            cursor = connection.cursor()                    
            cursor.execute("UPDATE DEVICE_CONF set DEVICE_VEHICAL_COUNTER=0") 
        connection.commit();
        connection.close()            
print("Done")
