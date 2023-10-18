import sys
import os
import sqlite3



 #### Get All records based on rec id ascending
load_vals=[]
rec_id=[]
FLAG=""
UP_COUNT=0
peak_val_arr=[]
        
connection = sqlite3.connect("tyr.db")        
results=connection.execute("SELECT round(Y_NUM,2),REC_ID FROM STG_GRAPH_MST order by REC_ID ASC")
for x in results:
              load_vals.append(float(x[0]))
              rec_id.append(int(x[1]))
connection.close()   
print("Total Records :"+str(len(rec_id)))
total_count=len(rec_id)
for x in range(len(rec_id)):
             if(x < total_count-1):
                 if(load_vals[x] < load_vals[x+1]):
                     print("ID: "+str(x)+"  ....FLAG : UP")
                     FLAG="UP"
                     UP_COUNT=UP_COUNT+1
                 else:
                     print("ID: "+str(x)+"  ....FLAG : DOWN")
                     FLAG="DOWN"
                     if(UP_COUNT > 0):
                         peak_val_arr.append(load_vals[x])
                         UP_COUNT=0
                 
#peak_val_arr.sort()       
print("All Peak Values :"+str(peak_val_arr))
        #### Check First record with Second record
        #### Set Flag UP Or DOWN
        #### Loop
        #### UP - Condition if First is > than secodn then change flag Down.
        #### Down -- Conition if First < Second Then chnage Flag Up
        ### During change flag UP to Down push record in array of UP   
       