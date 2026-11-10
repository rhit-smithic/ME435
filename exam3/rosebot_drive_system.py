## Naming conflicts: be careful naming class, file, and instance variables the same thing
import time
import motor

class DriveSystem:
    def __init__(self):
        self.car = motor.Ordinary_Car()

    def scale_speed(self, speed):
        """ Returns an int duty of 0 to 4095 (or 0 to -4095) based on the given speed. """
        return int(speed / 100 * 4095)

    def set_speeds(self, left_front, left_rear, right_front, right_rear):
        """ Pass in 4 speeds, each -100 to 100 to set the wheel duty cycle. """
        self.car.set_motor_model(self.scale_speed(left_front),
                                self.scale_speed(left_rear),
                                self.scale_speed(right_front),
                                self.scale_speed(right_rear))

    def go(self, left_wheel_speed, right_wheel_speed):
        """ Speeds as integers from -100 to 100. """
        self.set_speeds(left_wheel_speed * 0.90, left_wheel_speed * 0.90, right_wheel_speed, right_wheel_speed)

    def stop(self):
        self.set_speeds(0, 0, 0, 0)

    def go_straight_for_seconds(self, seconds, speed):
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop()


    def spin_in_place_for_seconds(self, seconds, speed):
        self.go(-speed, speed)
        time.sleep(seconds)
        self.stop()


    def go_straight_for_inches(self, inches, speed):
        a = 0
        b = 0.29
        c = 20.6
        s = abs(speed)
        inches_per_second = a * s * s + b * s + c
        seconds = inches / inches_per_second
        self.go_straight_for_seconds(seconds, speed)

    def spin_in_place_for_degrees(self, degrees, speed):
        s = abs(speed)
        degrees_per_second = -0.05927 *s*s + 9.6895 *s + 65
        extra = 0.1309 - 0.001326 *s
        seconds = abs(degrees) / degrees_per_second + extra
        if degrees < 0:
            speed = -abs(speed)
        else:
            speed = abs(speed)
        self.spin_in_place_for_seconds(seconds, speed)