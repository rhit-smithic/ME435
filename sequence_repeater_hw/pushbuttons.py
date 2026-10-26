import gpiozero
import time
import signal

"""
def button_state():
	button = gz.Button(25)

	while True:
		if button.is_pressed:
			print("Button is pressed.")
		else:
			print("Button is not pressed.")
		time.sleep(0.5)


def function_using_def():
	print("This is a function using the keyword def")
	print("It can have many lines")

"""

led_board = gpiozero.LEDBoard(14, 15, 18)

red_PB = gpiozero.Button(22)
yellow_PB = gpiozero.Button(23)
green_PB = gpiozero.Button(24)
reset_PB = gpiozero.Button(25)

sequence = []

#function_using_lambda = lambda: print("This is a func object using the keyword lambda")


def press(led_board, i):
    led_board[i].on()
    sequence.append(i)

def release(led_board, i):
    led_board[i].off()

def play_sequence(led_board):
	print("Playing Sequence")
	for k in range(len(sequence)):
		led_board[sequence[k]].value = 1
		time.sleep(0.5)
		led_board.off()
		if k < len(sequence) - 1:
			time.sleep(0.1)
	sequence.clear()
	

def button_events():
	print("Button Events")
	#button = gz.Button(25)
	#led_board = gz.LEDBoard(14, 15, 18)

	#button.when_pressed = function_using_def
	#button.when_released = function_using_lambda
	red_PB.when_pressed = lambda: press(led_board, 0)
	red_PB.when_released = lambda: release(led_board, 0)
	
	yellow_PB.when_pressed = lambda: press(led_board, 1)
	yellow_PB.when_released = lambda: release(led_board, 1)
	
	green_PB.when_pressed = lambda: press(led_board, 2)
	green_PB.when_released = lambda: release(led_board, 2)
	
    reset_PB.when_pressed = lambda: play_sequence(led_board)

    signal.pause()

def main():
	print("Sequence Repeater HW")
	button_events()


if __name__ == "__main__": main()