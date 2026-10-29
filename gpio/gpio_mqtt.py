import mqtt_helper as mh
import gpiozero as gz
import time

class App():
	def __init__(self):

		self.red_led = gz.LED(14)
		self.yellow_led = gz.LED(15)
		self.green_led = gz.LED(18)
		
        self.mqtt_client = mh.MqttClient()
		self.mqtt_client.connect(subscription_topic_name="me435/smithic/#",
					publish_topic_name="me435/smithic/to_computer")
        self.mqtt_client.callback = self.mqtt_callback

        self.button23 = gz.Button(23)
	    self.button23.when_pressed = lambda: self.mqtt_client.send_message("button")
        self.button25 = gz.Button(25)
	    self.button25.when_pressed = lambda: self.mqtt_client.send_message("reset")


def mqtt_callback(self, msg_type, msg_payload):
		print("Received type: ", msg_type)
		print("Received type: ", msg_payload)

    if msg_type == "red":
        if msg_payload == "on":
			self.red_led.on()
        elif msg_payload == "off":
			self.red_led.on()

    if msg_type == "yellow":
        if msg_payload == 1:
			self.yellow_led.on()
		elif msg_payload == 0:
			self.yellow_led.off()

    if msg_type == "green":
        if msg_payload == True:
            self.green_led.on()
		elif msg_payload == False:
            self.green_led.off(0)

    if msg_type == "leds":
        if msg_payload[0] == 1:
			self.red_led.on()
		else:
			self.red_led.off()
			
        if msg_payload[1] == 1:
			self.yellow_led.on()
		else:
			self.yellow_led.off()
			
        if msg_payload[2] == 1:
			self.green_led.on()
		else:
			self.green_led.off()

def main():
	print("GPIO MQTT")
	app = App()

	# while True:
	#     app.mqtt_client.send_message("red","on")
	# 	app.mqtt_client.send_message("yellow", 1)
	# 	app.mqtt_client.send_message("green", True)
	# 	#app.mqtt_client.send_message("leds", [1, 0, 1])
	# 	time.sleep(1)
	#     app.mqtt_client.send_message("red","off")
	# 	app.mqtt_client.send_message("yellow", 0)
	# 	app.mqtt_client.send_message("green", False)
	# 	#app.mqtt_client.send_message("leds", [0, 1, 0])
	# 	time.sleep(1)

    signal.pause()

main()