import arduino

def main():
    while True:
        print("Serial Menu")

        builtinled = arduino.BuiltinLED("/dev/ttyACM0")
        builtinled.connect()

        print("0. Exit")
        print("1. LED ON")
        print("2. LED OFF")
        print("3. FLASH")


        selection = int(input("Selection: "))
        if selection == 0:
            break

        elif selection == 1:
            response = builtinled.send_command("LED ON")
            print(response)

        elif selection == 2:
            response = builtinled.send_command("LED OFF")
            print(response)

        elif selection == 3:
            count = input("Flash Count: ")
            period = input("Flash Period: ")
            response = builtinled.send_command("FLASH " + count + period)

    builtinled.disconnect

main()