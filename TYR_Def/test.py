import datetime
import time
start_time = datetime.datetime.now()
start_time =start_time.strftime('%Y-%m-%d %H:%M:%S')
time.sleep(7)
end_time = datetime.datetime.now()
end_time =end_time.strftime('%Y-%m-%d %H:%M:%S')

elapsed_time=end_time-start_time
elapsed_time=elapsed_time.days * 24 * 3600 + elapsed_time.seconds

print(" Start:"+str(start_time))
print(" End:"+str(datetime.datetime.now()))
print(" Elapsed Time: %d seconds" %elapsed_time)
print(" Elapsed Time-int:"+str(int(elapsed_time)))

#z=datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
z=datetime.datetime.now()

print("z:"+str(z.strftime('%Y-%m-%d %H:%M:%S')))