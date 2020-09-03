
import requests
import urllib.request
import sqlite3

internet_status=""
api_url=""
batch_id=""
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
            results=connection.execute("SELECT API_URL FROM API_MST WHERE API_ID = '2'")         
            for x in results:                
                     api_url=str(x[0])
            connection.close()
            print("api_url:"+str(api_url))
            
            if(str(api_url) != ""):
                    ###Get Serial Number ######
                    connection = sqlite3.connect("fci.db")       
                    results=connection.execute("SELECT BATCH_ID FROM BATCH_MST  WHERE UPLOAD_STATUS IS NULL ORDER BY BATCH_ID DESC LIMIT 1")         
                    for x in results:                
                             batch_id=str(x[0])
                    connection.close()
                    print("batch_id:"+str(batch_id))
                    if(str(batch_id) != ""):
                        #### create Json string ######
                        connection = sqlite3.connect("fci.db")       
                        results=connection.execute("SELECT  BATCH_ID,BATCH_ID_DISPLAY,IFNULL(BATCH_DATE,'1999-01-01 12:00:00'), IFNULL(ACCPT_WT_TON,0) ,IFNULL(ACCPT_BAGS_CNT,0), IFNULL(RECV_WT_TON,0), IFNULL(RECV_BAGS_CNT,0) ,IFNULL(TL_RECVED,0), IFNULL(TL_ACCPTED,0) ,IFNULL(STORAGE_BAGS,0), MATERIAL_TYPE, STATUS ,IFNULL(WAGON_CNT,0), IFNULL(REQUIRED_TRUCKS,0) ,CONTRACTOR_NAME ,DEVICE_ID FROM BATCH_MST  WHERE BATCH_ID='"+str(batch_id)+"'")         
                        for x in results:
                            
                            json_str["batchId"] = str(x[0])
                            json_str["batchIdDisplay"] = str(x[1])
                            json_str["batchDt"] = str(x[2])
                            json_str["accpetedWtKg"] = str(x[3])
                            json_str["acceptedBagsCnt"] = str(x[4])
                            json_str["receivedWtKg"] = str(x[5])
                            json_str["receivedBagsCnt"] = str(x[6])
                            json_str["tlreceived"] = str(x[7])                           
                            json_str["tlaccepted"] = str(x[8])
                            json_str["shortageBags"] = str(x[9])
                            json_str["material"] = str(x[10])
                            json_str["status"] = str(x[11])
                            json_str["wagonCnt"] = str(x[12])
                            json_str["requiredTrucks"] = str(x[13])
                            json_str["contractorName"] = str(x[14])
                            json_str["deviceId"] = str(x[15])
                           
                        connection.close()                        
                        print("Joson String"+str(json_str))
                        #### Call API #####
                        resp = requests.post(str(api_url),json=json_str,headers={'Content-Type':'application/json'})
                        if resp.status_code != 200:
                            connection = sqlite3.connect("fci.db")
                            with connection:        
                                    cursor = connection.cursor()
                                    cursor.execute("UPDATE BATCH_MST SET UPLOAD_STATUS='Failed' WHERE BATCH_ID='"+str(batch_id)+"'")                    
                            connection.commit();                    
                            connection.close()
                        else:
                             #### Update weight_mst , API_LOGS tables
                            connection = sqlite3.connect("fci.db")
                            with connection:        
                                cursor = connection.cursor()
                                cursor.execute("UPDATE BATCH_MST SET UPLOAD_STATUS='SUCCESS' WHERE BATCH_ID='"+str(batch_id)+"'")                    
                            connection.commit();                    
                            connection.close()
                            
                            connection = sqlite3.connect("fci.db")
                            with connection:        
                                cursor = connection.cursor()
                                cursor.execute("INSERT INTO API_LOGS(URL,STATUS) values('"+str(api_url)+"','SUCCESS')")                    
                            connection.commit();                    
                            connection.close()
                    else:
                        print("Serial ID not Found.")
                        
            else:
                print("API URL is not found")
                    

else:
    print("Internet connection is Off.")
