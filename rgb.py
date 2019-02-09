import RPi.GPIO as GPIO
import time
import board
import busio

from config import *

import adafruit_tcs34725

class rgb_sensor:
    'Class to initialize and use the rgb sensors for the THESEUS robot'
    def __init__(self):
        r, b, g, c
        # Initialize I2C bus and sensor.
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_tcs34725.TCS34725(i2c)

    def process_input(self):
        # take in input and process to determine color
        self.r, self.b, self.g, self.c = 0, 0, 0, 0
        self.sensor.getRawInput(r, b, g, c)

    def on_line(r, g, b, c):
        r_difference = abs(self.r - r)
        g_difference = abs(self.g - g)
        b_difference = abs(self.b - b)

        if r_difference < r_allowable AND g_difference < g_allowable AND b_difference < b_allowable:
            return true
        else:
            return false

    def ardu_input(ser_ch):
        #takes in arduino serial input and returns separate r,g,b,c values
        ser_input = ser_ch.readline()
        rgblist = ser_input.split(',')
        r = rgblist[0]
        g = rgblist[1]
        b = rgblist[2]
        c = rgblist[3]

        return r,g,b,c
