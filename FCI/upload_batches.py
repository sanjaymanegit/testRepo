import requests
'''
resp = requests.get('http://www.samruddhielectrotech.com/FciData/fciServer/ping')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

print("resp.status_code"+str(resp.status_code))
print("resp.status_code"+str(resp))
''' 
batch_json_str={
"batchId":"99",
"batchIdDisplay":"98",
"batchDt":"2020-08-14 23:00:45",
"accpetedWtKg":"234",
"acceptedBagsCnt":"96000",
"receivedWtKg":"95000",
"receivedBagsCnt":"67666",
"tlreceived":"34455",
"tlaccepted":"5666",
"shortageBags":"234",
"material":"Wheat -1",
"status":"In Porogres",
"wagonCnt":"40",
"requiredTrucks":"567",
"contractorName":"Contactor xxxc",  
"deviceId":"202008/12"}
 
resp = requests.post('http://www.samruddhielectrotech.com/FciData/fciServer/load_batch_mst',json=batch_json_str,headers={'Content-Type':'application/json'})
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

print("resp.status_code"+str(resp.status_code))
print("output"+str(resp.text))