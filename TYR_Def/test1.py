import time
start = time.time()
#do something
time.sleep(5)
end = time.time()
temp = end-start
print(temp)
hours = temp//3600
temp = temp - 3600*hours
minutes = temp//60
seconds = temp - 60*minutes
print("start:"+str(start))
print("end:"+str(end))
print('%d:%d:%d' %(hours,minutes,seconds))