
import requests
import urllib.request
import sqlite3

internet_status=""
api_url=""
serial_id=""
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
            results=connection.execute("SELECT API_URL FROM API_MST WHERE API_ID = '1'")         
            for x in results:                
                     api_url=str(x[0])
            connection.close()
            print("api_url:"+str(api_url))
            
            if(str(api_url) != ""):
                    ###Get Serial Number ######
                    connection = sqlite3.connect("fci.db")       
                    results=connection.execute("SELECT SERIAL_ID FROM WEIGHT_MST  WHERE UPLOAD_STATUS IS NULL ORDER BY SERIAL_ID DESC LIMIT 1")         
                    for x in results:                
                             serial_id=str(x[0])
                    connection.close()
                    print("serial_id:"+str(serial_id))
                    if(str(serial_id) != ""):
                        #### create Json string ######
                        connection = sqlite3.connect("fci.db")       
                        results=connection.execute("SELECT SERIAL_ID, VEHICLE_NO, MATERIAL_NAME, IFNULL(BATCH_ID,0) ,STATUS ,FIRST_WEIGHT_MODE, IFNULL(FIRST_WEIGHT_VAL,0) "
                                                   +", IFNULL(FIRST_WT_CRTEATED_ON,'1999-01-01 12:00:00') ,SECOND_WT_MODE, IFNULL(SECOND_WT_VAL,0), IFNULL(SECOND_WT_CREATED_ON,'1999-01-01 12:00:00') ,IFNULL(NET_WEIGHT_VAL,0),IFNULL(ACCPTED_BAGS,0), IFNULL(AVG_BAG_WT,0),"
                                                   +"REMARK , MANNUAL_INS_FLG ,DRIVER_IN_OUT ,IFNULL(PROPOSED_BAGS,0) ,TARGET_STORAGE, IFNULL(CURR_TRUCK_CNT,0), IFNULL(TOTAL_TRUCKS_CNT,0), "
                                                   +"IFNULL(CONTRACTOR_ID,0) ,CONTRACTOR_NAME, IFNULL(ISSUE_ID,0) ,WEIGHING_TYPE, DEVICE_LOCATION_TYPE,DEVICE_ID FROM WEIGHT_MST  WHERE SERIAL_ID='"+str(serial_id)+"'")         
                        for x in results:
                            
                            json_str["serialNo"] = str(x[0])
                            json_str["vehicleNo"] = str(x[1])
                            json_str["material"] = str(x[2])
                            json_str["batchId"] = str(x[3])
                            json_str["status"] = str(x[4])
                            json_str["firstWeightMode"] = str(x[5])
                            json_str["firstWeightVal"] = str(x[6])
                            json_str["firstWeightDt"] = str(x[7])
                            json_str["secondWeightMode"] = str(x[8])
                            json_str["secondWeightVal"] = str(x[9])
                            json_str["secondWeightDt"] = str(x[10])
                            json_str["netWeightVal"] = str(x[11])
                            json_str["acceptedBags"] = str(x[12])
                            json_str["avgBagWt"] = str(x[13])
                            json_str["remark"] = str(x[14])
                            json_str["manualInsFlag"] = str(x[15])
                            json_str["driverInOut"] = str(x[16])
                            json_str["proposedBags"] = str(x[17])
                            json_str["targetStorage"] = str(x[18])
                            json_str["currTruckCount"] = str(x[19])
                            json_str["totalTruckCount"] = str(x[20])
                            json_str["contractorId"] = str(x[21])
                            json_str["contractorName"] = str(x[22])
                            json_str["issueId"] = str(x[23])
                            json_str["weighingType"] = str(x[24])
                            json_str["deviceLocationType"] = str(x[25])
                            json_str["deviceId"] = str(x[26])
                        connection.close()                        
                        print("Joson String"+str(json_str))
                        #### Call API #####
                        resp = requests.post(str(api_url),json=json_str,headers={'Content-Type':'application/json'})
                        if resp.status_code != 200:
                            connection = sqlite3.connect("fci.db")
                            with connection:        
                                    cursor = connection.cursor()
                                    cursor.execute("UPDATE WEIGHT_MST SET UPLOAD_STATUS='Failed' WHERE SERIAL_ID='"+str(serial_id)+"'")                    
                            connection.commit();                    
                            connection.close()
                        else:
                             #### Update weight_mst , API_LOGS tables
                            connection = sqlite3.connect("fci.db")
                            with connection:        
                                cursor = connection.cursor()
                                cursor.execute("UPDATE WEIGHT_MST SET UPLOAD_STATUS='SUCCESS' WHERE SERIAL_ID='"+str(serial_id)+"'")                    
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
