import serial

print("Learning Pyserial")

#below, when the port is set... refer to the arduino with /dev/ttyACM0. refer to plateloader with /dev/ttyUSB0
ser = serial.Serial(port="/dev/ttyACM0", baudrate=19200, timeout=10) #check the com number !!! # create the object
# may or may not need ser.open()
while not serial.is_open:
    print("Opening...")

# TODO: use the serial object

ser.close() # what does opening and closing the serial object mean?