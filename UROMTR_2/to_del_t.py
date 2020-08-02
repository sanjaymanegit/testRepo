import sqlite3


started_time=""
flow_x_time="0"
started_time="0"
stoped_time="0"
flow_x_time_curr="0"
flow_x_time="0"

connection = sqlite3.connect("ur.db")        
results=connection.execute("SELECT MAX(Y_NUM),AVG(Y_NUM) FROM GRAPH_MST2 where GRAPHI_ID=42")
for x in results:
     print(" Max Flow :"+str(x[0])+"   Avg Flow :"+str(x[1]))
     '''
     if(float(x[1]) > 0 ):
                #print(str(x[0])+":"+str(x[1]))
                status="started"
                stoped_time="0"
                if(started_time == "0"):
                        started_time=str(x[0])
                                  
     else:
                #print(str(x[0])+":"+str(x[1]))
                status="stopped"                                 
                if(stoped_time == "0"):
                        stoped_time=str(x[0])

     #print("started_time: "+str(started_time)+" stoped_time:"+str(stoped_time))
     if( float(started_time) > 0 and float(stoped_time) > 0):
                        flow_x_time_curr=float(str(stoped_time))-float(str(started_time))
                        flow_x_time=float(flow_x_time)+float(flow_x_time_curr)
                        print("flow_x_time_curr :"+str(float(flow_x_time_curr))+"started_time: "+str(float(started_time))+" stoped_time:"+str(float(stoped_time)))
                        started_time="0"
                        stoped_time="0"
                        
     '''                   
connection.close()
#print("Total flow_time  Time :"+str(flow_x_time))
        