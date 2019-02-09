import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
time.sleep(5)
# infinite loop
while True:
	print "Sound Output: " ,GPIO.input(channel)
	if GPIO.input(channel) == 1:
		print "SOUND DETECTED BITCHES"
	else:
		print "fookin hell m8"
	time.sleep(0.1)
