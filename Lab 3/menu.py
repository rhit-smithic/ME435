import plateloader

def main():
    while True:
        print("Serial Menu")

        #loader = plateloader.PlateLoader("/dev/tty/USB0")
        loader = plateloader.PlateLoader()
        loader.connect()

        print("0. Exit")
        print("1. RESET")
        print("2. X-AXIS")
        print("3. GRIPPER")
        print("4. Z-AXIS")
        print("5. MOVE")
        print("6. Status")

        selection = int(input("Selection: "))
        if selection == 0:
            break

        elif selection == 1:
            response = loader.send_command("RESET")
            print(response)

        elif selection == 2:
            x_pos = input("To which x position? ")
            response = loader.send_command("X-AXIS " + x_pos)

        elif selection == 3:
            gripper_status = input("OPEN or CLOSED?")
            response = loader.send_command("GRIPPER " + gripper_status)

        elif selection == 4:
            z_pos = input("EXTEND or RETRACT?")
            response = loader.send_command("Z_AXIS " + z_pos)

        elif selection == 5:
            pos1 = input("From: ")
            pos2 = input("To: ")
            response = loader.send_command("MOVE " + pos1 + " " + pos2)

        elif selection == 6:
            response = loader.send_command("STATUS")
            print(response)

    loader.disconnect

main()