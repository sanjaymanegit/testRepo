import serial
ser = serial.Serial('/dev/ttyAMA0', 9600)
#ser = serial.Serial('/dev/ttyS4', 9600)
ser.write("hello world!")
