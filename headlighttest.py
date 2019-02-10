import sys, time
import RPi.GPIO as GPIO

right_headlamp = 24
photo_sensor = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(right_headlamp, GPIO.OUT)
GPIO.setup(photo_sensor,GPIO.IN)

while True:
    print(GPIO.input(photo_sensor))
