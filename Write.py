#!/usr/bin/env python
# code from https://pimylifeup.com/raspberry-pi-rfid-rc522/

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
	text = raw_input ('Data to be written:')
	print("Place tag on reader")
	reader.write(text.replace(" ", ""))
	print("Written!")
finally:
	GPIO.cleanup()
