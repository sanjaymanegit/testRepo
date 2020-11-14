
import requests
import urllib.request
import sqlite3

internet_status=""
api_url=""
slot_no=""
json_str={}
url = "http://www.google.com"
timeout = 5

### Get Internet Status
def get_internet_status():        
    try:
        request = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        internet_status="OFF"
        return False
        



### Script Started ######
print("internet_status:"+str(internet_status))        
#get_internet_status()
#internet_status="ON"
if(get_internet_status()):    
            #### Get url from API_MST
            connection = sqlite3.connect("fci.db")       
            results=connection.execute("SELECT API_URL FROM API_MST WHERE API_ID = '5'")         
            for x in results:                
                     api_url=str(x[0])
            connection.close()
            print("api_url:"+str(api_url))
            
            if(str(api_url) != ""):
                    ###Get Serial Number ######
                    connection = sqlite3.connect("fci.db")       
                    results=connection.execute("SELECT SLOT_NO FROM SLOTS_MST  WHERE UPLOAD_STATUS IS NULL ORDER BY REC_ID DESC LIMIT 1")         
                    for x in results:                
                             slot_no=str(x[0])
                    connection.close()
                    print("slot_no:"+str(slot_no))
                    if(str(slot_no) != ""):
                        #### create Json string ######
                        connection = sqlite3.connect("fci.db")
                        results=connection.execute("SELECT  SLOT_NO ,IFNULL(CAPACITY_IN_BAGS,0) ,IFNULL(CAPACITY_IN_WT,0) , MATERIAL,  BATCH_ID,  IFNULL(R_BAGS,0) , IFNULL(R_NET_WT,0) ,IFNULL(R_AVG_BAG_WT,0), IFNULL(R_DATE,'1999-01-01 12:00:00') ,IFNULL(I_BAGS,0) ,IFNULL(I_NET_WT,0),  IFNULL(I_DATE ,'1999-01-01 12:00:00'),IFNULL(I_AVG_BAG_WT,0),  IFNULL(LOSS_BAGS,0) , IFNULL(LOSS_NET_WT,0) , IFNULL(LOSS_AVG_BAG_WT,0),  IFNULL(LOSS_PERC,0) , DEVICVE_ID ,IFNULL(BAL_BAGS,0) ,IFNULL(BAL_NET_WT,0) ,IFNULL(BAL_AVG_BAG_WT,0),  STATUS FROM SLOTS_MST  WHERE SLOT_NO='"+str(slot_no)+"'")         
                        for x in results:                            
                            json_str["slotNo"] = str(x[0])
                            json_str["capacityBags"] = str(x[1])
                            json_str["capacityWt"] = str(x[2])
                            json_str["material"] = str(x[3])
                            json_str["batchId"] = str(x[4])
                            json_str["rbags"] = str(x[5])
                            json_str["rnetWt"] = str(x[6])
                            json_str["ravgbagWt"] = str(x[7])                           
                            json_str["rdt"] = str(x[8])
                            json_str["ibags"] = str(x[9])
                            json_str["inetWt"] = str(x[10])
                            json_str["idt"] = str(x[11])
                            json_str["iavgbagWt"] = str(x[12])
                            json_str["lostbags"] = str(x[13])
                            json_str["lostnetWt"] = str(x[14])
                            json_str["lostavgbagWt"] = str(x[15])
                            json_str["lostperc"] = str(x[16])                            
                            json_str["deviceID"] = str(x[17])                            
                            json_str["balbags"] = str(x[18])
                            json_str["balnetWt"] = str(x[19])
                            json_str["balavgbagWt"] = str(x[20])
                            json_str["status"] = str(x[21])
                        connection.close()                        
                        print("Joson String"+str(json_str))
                        #### Call API #####
                        resp = requests.post(str(api_url),json=json_str,headers={'Content-Type':'application/json'})
                        if resp.status_code != 200:
                            connection = sqlite3.connect("fci.db")
                            with connection:        
                                    cursor = connection.cursor()
                                    cursor.execute("UPDATE SLOTS_MST SET UPLOAD_STATUS='Failed' WHERE SLOT_NO='"+str(slot_no)+"'")                    
                            connection.commit();                    
                            connection.close()
                        else:
                             #### Update weight_mst , API_LOGS tables
                            connection = sqlite3.connect("fci.db")
                            with connection:        
                                cursor = connection.cursor()
                                cursor.execute("UPDATE SLOTS_MST SET UPLOAD_STATUS='SUCCESS' WHERE SLOT_NO='"+str(slot_no)+"'")                    
                            connection.commit();                    
                            connection.close()
                            
                            connection = sqlite3.connect("fci.db")
                            with connection:        
                                cursor = connection.cursor()
                                cursor.execute("INSERT INTO API_LOGS(URL,STATUS) values('"+str(api_url)+"','SUCCESS')")                    
                            connection.commit();                    
                            connection.close()
                    else:
                        print("Slot No not Found.")
                        
            else:
                print("API URL is not found")
                    

else:
    print("Internet connection is Off.")
