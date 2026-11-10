import mqtt_helper as mh
from rosebot import Rosebot
import signal
from rosebot_drive_system import DriveSystem
from rosebot_sensors import Ultrasonic
import datetime
import time


class App:

    def __init__(self):
        self.robot = Rosebot()
        self.mode = "none"
        self.is_streaming = False

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/smithic/to_pi",
                                 publish_topic_name="me435/smithic/to_computer")
        self.mqtt_client.callback = self.mqtt_callback

    def run_motors(self, left_speed, right_speed, seconds):
        self.robot.drive_system.set_speeds(left_speed, left_speed, right_speed, right_speed)
        time.sleep(seconds)
        self.robot.drive_system.stop()

    def mqtt_callback(self, message_type, message_payload):
        print("Received type: ", message_type)
        print("Received payload: ", message_payload)

        if message_type == "left":
            direction, seconds, pwm = message_payload
            print(f"Side: Left  Direction: {int(direction)}  Time: {float(seconds)}  Speed: {int(pwm)}")
            sign = 1 if direction == 1 else -1
            self.run_motors(sign * pwm, 0, seconds)

        elif message_type == "right":
            direction, seconds, pwm = message_payload
            print(f"Side: Right  Direction: {int(direction)}  Time: {float(seconds)}  Speed: {int(pwm)}")
            sign = 1 if direction == 1 else -1
            self.run_motors(0, sign * pwm, seconds)

        elif message_type == "both":
            direction, seconds, pwm_left, pwm_right = message_payload
            print(f"Side: Both  Direction: {int(direction)}  Time: {float(seconds)}  "
                  f"Speed Left: {int(pwm_left)}  Speed Right: {int(pwm_right)}")
            sign = 1 if direction == 1 else -1
            self.run_motors(sign * pwm_left, sign * pwm_right, seconds)


def main():
    print("Exam 3 MQTT Car")
    app = App()
    robot = app.robot

    try:
        while True:
            app.mqtt_client.send_message("ultra", app.robot.ultrasonic.get_cm())
            time.sleep(2)

    except KeyboardInterrupt:
        robot.drive_system.stop()
        print("Goodbye!")


main()