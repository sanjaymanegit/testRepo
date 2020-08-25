import requests
'''
resp = requests.get('http://www.samruddhielectrotech.com/FciData/fciServer/ping')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

print("resp.status_code"+str(resp.status_code))
print("resp.status_code"+str(resp))
''' 
weight_json_str={"serialNo": "0002",
  "vehicleNo": "MH43AW0302",
  "material": "Wheat-01",
  "batchId": "47",
  "status": "First",
  "firstWeightMode": "Tare",
  "firstWeightVal": "400.00",
  "firstWeightDt": "2020-08-12 12:00:00",
  "secondWeightMode": "gross",
  "secondWeightVal": "00",
  "secondWeightDt": "2020-08-12 12:00:00",
  "netWeightVal": "00", 
  "acceptedBags": "44",
  "avgBagWt": "50",
  "remark": "remark99",
  "manualInsFlag": "1",
  "driverInOut": "OUT",
  "proposedBags": "22",
  "targetStorage": "storage Patana 1",
  "currTruckCount": "23",
  "totalTruckCount": "260",
  "contractorId": "0066",
  "contractorName": "contracto xxxx",
  "issueId": "6",
  "weighingType": "BATCH",
  "deviceLocationType": "STORGAE",
  "deviceId": "202008/12"}
 
resp = requests.post('http://www.samruddhielectrotech.com/FciData/fciServer/load_weight_mst',json=weight_json_str,headers={'Content-Type':'application/json'})
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

print("resp.status_code"+str(resp.status_code))
print("output"+str(resp.text))