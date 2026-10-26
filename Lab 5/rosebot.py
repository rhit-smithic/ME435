import gpiozero as gz
from rosebot_drive_system import DriveSystem

class Rosebot:
    def __init__(self):
        ## initialize subsystems
        self.drive_sysyem = DriveSystem()
        self.leds = LED()
        self.ultrasonic = None
        self.line_sensors = None
        self.servo_head = None ## may not be used
        self.buzzer = gz.Buzzer(17)
        self.adc = None

    
        