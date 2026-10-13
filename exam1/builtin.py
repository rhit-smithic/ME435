import serial
import time

class BuiltinLED:
    def __init__(self, port="/dev/ttyACM0"):
        self.port = port #argument passed in called port
        # uses self. saves it so it doesnt go away when the call ends
        self.ser = None

    def connect(self):
        if self.ser and self.ser.is_open:
            return
        self.ser = serial.Serial(port=self.port, baudrate=19200, timeout=15)
        time.sleep(2.0)

    def disconnect(self):
        if self.ser and self.ser.is_open:
            self.ser.close()

    def send_command(self, command):
        self.ser.reset_input_buffer() # clears off old responses
        message_bytes = (command + "\n").encode()
        print(message_bytes)

        self.ser.write(message_bytes)

        response_bytes = self.ser.readline()
        print(response_bytes)
        response = response_bytes.decode().strip()
        return response

        
if __name__ == "__main__":
    ##print("Quick PlateLoader testing")
    builtinled = BuiltinLED()
    builtinled.connect()
    response = builtinled.send_command("LED OFF")
    print("Response: ", response)
    builtinled.disconnect()
    

