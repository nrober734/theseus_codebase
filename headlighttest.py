import sys, time
import RPi.GPIO as GPIO

right_headlamp = 24
photo_sensor = 19

GPIO.setup(right_headlamp, GPIO.OUT)
GPIO.setup(photo_sensor,GPIO.IN)

print(GPIO.input(photo_sensor))
