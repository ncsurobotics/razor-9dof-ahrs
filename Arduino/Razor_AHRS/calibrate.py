import serial

ser = serial.Serial('/dev/ttyUSB0', 57600)


ser.write(b'#o0') # Turn off automatic streaming
ser.write(b'#oc') # Set calibration mode
ser.timeout = 1
ser.write(b'#f')
correct_mode = ser.readline().startswith("gyro")

while not correct_mode:
    ser.write(b'#on')
    ser.write(b'#f')
    correct_mode = ser.readline().startswith("gyro")
  
while True:
    ser.write(b'#f')
    print(ser.readline())


