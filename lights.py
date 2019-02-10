import sys, time
import RPi.GPIO as GPIO

# pins for each LED
left_headlamp = 22
right_headlamp = 24


left_blinker = 11
right_blinker = 13

class lights:
    'class to initialize and toggle lights for THESEUS'
    def __init__(self):
        GPIO.setMode(GPIO.BCM)
        GPIO.setup(left_headlamp, GPIO.OUT)
        GPIO.setup(right_headlamp, GPIO.OUT)
        GPIO.setup(left_blinker, GPIO.OUT)
        GPIO.setup(right_blinker, GPIO.OUT)


    def turn_right(self):
        GPIO.output(right_blinker, GPIO.HIGH)
        GPIO.output(right_blinker, GPIO.LOW)

    def turn_left(self):
        GPIO.output(left_blinker, GPIO.HIGH)
        GPIO.output(left_blinker, GPIO.LOW)

    def headlamps(self, on_off):
        if on_off == True:
            GPIO.setup(right_headlamp, GPIO.HIGH)
            GPIO.setup(left_headlamp, GPIO.HIGH)
        else:
            GPIO.setup(right_headlamp, GPIO.LOW)
            GPIO.setup(left_headlam, GPIO.LOW)
    def when_dark(self):
