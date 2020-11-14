
import requests
import urllib.request
import sqlite3

internet_status=""
api_url=""
issue_id=""
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
            results=connection.execute("SELECT API_URL FROM API_MST WHERE API_ID = '3'")         
            for x in results:                
                     api_url=str(x[0])
            connection.close()
            print("api_url:"+str(api_url))
            
            if(str(api_url) != ""):
                    ###Get Serial Number ######
                    connection = sqlite3.connect("fci.db")       
                    results=connection.execute("SELECT ISSUE_ID FROM ISSUE_MST  WHERE UPLOAD_STATUS IS NULL ORDER BY ISSUE_ID DESC LIMIT 1")         
                    for x in results:                
                             issue_id=str(x[0])
                    connection.close()
                    print("issue_id:"+str(issue_id))
                    if(str(issue_id) != ""):
                        #### create Json string ######
                        connection = sqlite3.connect("fci.db")       
                        results=connection.execute("SELECT  ISSUE_ID,ORDER_ID,IFNULL(ISSUE_DATE,'1999-01-01 12:00:00'),IFNULL(EXPIRY_DATE,'1999-01-01 12:00:00'),RO_TYPE,CONTRACTOR_NAME, IFNULL(TOTAL_BAGS_DEMAND,0) ,IFNULL(TOTAL_NET_WT_DEMAND,0),DEVICE_ID FROM ISSUE_MST  WHERE ISSUE_ID='"+str(issue_id)+"'")         
                        for x in results:
                            
                            json_str["issueId"] = str(x[0])
                            json_str["orderId"] = str(x[1])
                            json_str["issueDt"] = str(x[2])
                            json_str["expiryDt"] = str(x[3])
                            json_str["roType"] = str(x[4])
                            json_str["contractorName"] = str(x[5])
                            json_str["bags"] = str(x[6])
                            json_str["netWt"] = str(x[7])
                            json_str["deviceId"] = str(x[8])
                           
                        connection.close()                        
                        print("Joson String"+str(json_str))
                        #### Call API #####
                        resp = requests.post(str(api_url),json=json_str,headers={'Content-Type':'application/json'})
                        if resp.status_code != 200:
                            connection = sqlite3.connect("fci.db")
                            with connection:        
                                    cursor = connection.cursor()
                                    cursor.execute("UPDATE ISSUE_MST SET UPLOAD_STATUS='Failed' WHERE ISSUE_ID='"+str(issue_id)+"'")                    
                            connection.commit();                    
                            connection.close()
                        else:
                             #### Update weight_mst , API_LOGS tables
                            connection = sqlite3.connect("fci.db")
                            with connection:        
                                cursor = connection.cursor()
                                cursor.execute("UPDATE ISSUE_MST SET UPLOAD_STATUS='SUCCESS' WHERE ISSUE_ID='"+str(issue_id)+"'")                    
                            connection.commit();                    
                            connection.close()
                            
                            connection = sqlite3.connect("fci.db")
                            with connection:        
                                cursor = connection.cursor()
                                cursor.execute("INSERT INTO API_LOGS(URL,STATUS) values('"+str(api_url)+"','SUCCESS')")                    
                            connection.commit();                    
                            connection.close()
                    else:
                        print("Issue ID not Found.")
                        
            else:
                print("API URL is not found")
                    

else:
    print("Internet connection is Off.")
