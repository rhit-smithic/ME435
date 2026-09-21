import serial

print("Learning Pyserial")

#below, when the port is set... refer to the arduino with /dev/ttyACM0. refer to plateloader with /dev/ttyUSB0
ser = serial.Serial(port="/dev/ttyACM0", baudrate=19200, timeout=10) #check the com number !!! # create the object
# may or may not need ser.open()
while not ser.is_open:
    
    time.sleep(2.0) # Necessary sometimes
    ser.reset_input_buffer() # clears off old responses
    message = "RESET" # have to convert string into byte array
    message_bytes = (message + "\n").encode()
    print(message_bytes)

    ser.write(message_bytes)

    response_bytes = ser.readline()
    print(response_bytes)
    response = response_bytes.decode().strip()
    print(response)

ser.close() # what does opening and closing the serial object mean?