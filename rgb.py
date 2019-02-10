import RPi.GPIO as GPIO
import time
import board
import busio

from config import *

import adafruit_tcs34725

class rgb_sensor:
    'Class to initialize and use the rgb sensors for the THESEUS robot'
    def __init__(self):
        self.r = 0
        self.b = 0
        self.g = 0
        self.c = 0
        # Initialize I2C bus and sensor.
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c)

    def process_input(self):
        # take in input and process to determine color
        self.sensor.getRawInput(r, b, g, c)


    def raw_ardu_input(self,ser_ch):
        #takes in arduino serial input and returns separate r,g,b,c values
        #ser_input = str(ser_ch.readline(),"utf-8")
        ser_input = str(ser_ch.read())
        #if ser_input.isalpha():
        #    ser_input = ""
        #rgblist = ser_input.split()
        # self.r = rgblist[0]
        # self.g = rgblist[1]
        # self.b = rgblist[2]
        # self.c = rgblist[3]


        return ser_input
        #return self.r,self.g,self.b,self.c

    def ardu_RGB_input(self,ser_ch):
        colorlist = []
        rgblist = []
        counter = 0
        rgbcount = 0
        # while counter < 5:
        #     # if self.raw_ardu_input(ser_ch).isdigit():
        #     if " " in self.raw_ardu_input(ser_ch):
        #         counter+=1
        #         rgblist.append(colorlist)
        #         colorlist = []
        #     colorlist.append(self.raw_ardu_input(ser_ch))



        print(self.raw_ardu_input(ser_ch))
        print(self.raw_ardu_input(ser_ch)[0])
        print(self.raw_ardu_input(ser_ch)[1])


        return self.raw_ardu_input(ser_ch).isdigit()

    def getR(self):
        return self.r

    def getG(self):
        return self.g

    def getB(self):
        return self.b

    def getC(self):
        return self.c


def on_line(r, g, b):
    r_difference = abs(r_line - r)
    g_difference = abs(r_line - g)
    b_difference = abs(r_line - b)

    if r_difference < r_allowable and g_difference < g_allowable and b_difference < b_allowable:
        return true
    else:
        return false
