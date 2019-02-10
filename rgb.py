import RPi.GPIO as GPIO
import time
import board
import busio

from config import *

import adafruit_tcs34725

class rgb_sensor:
    'Class to initialize and use the rgb sensors for the THESEUS robot'
    def __init__(self):
        #self.r, self.b, self.g, self.c
        # Initialize I2C bus and sensor.
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c)

    def process_input(self):
        # take in input and process to determine color
        self.r, self.b, self.g, self.c = 0, 0, 0, 0
        self.sensor.getRawInput(r, b, g, c)

    def on_line(self,r, g, b, c):
        r_difference = abs(self.r - r)
        g_difference = abs(self.g - g)
        b_difference = abs(self.b - b)

        if r_difference < r_allowable and g_difference < g_allowable and b_difference < b_allowable:
            return true
        else:
            return false

    def raw_ardu_input(self,ser_ch):
        #takes in arduino serial input and returns separate r,g,b,c values
        #ser_input = str(ser_ch.readline(),"utf-8")
        ser_input = str(ser_ch.read(),"utf-8")
        #rgblist = ser_input.split()
        # self.r = rgblist[0]
        # self.g = rgblist[1]
        # self.b = rgblist[2]
        # self.c = rgblist[3]


        return ser_input
        #return self.r,self.g,self.b,self.c

    def ardu_RGB_input(self,string):

        for k in range(7):
            if string[k] is not " ":
                if k==0:
                    self.r = int(string[k])
                elif k==3:
                    self.g == int(string[k])
                elif k==5:
                    self.b == int(string[k])
                elif k==7:
                    self.c == int(string[k])

        return [self.r,self.g,self.b,self.c]

    def getR(self):
        return self.r

    def getG(self):
        return self.g

    def getB(self):
        return self.b

    def getC(self):
        return self.c
